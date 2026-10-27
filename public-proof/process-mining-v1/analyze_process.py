#!/usr/bin/env python3
"""Kavramsal süreç-madenciliği ön kontrolü: gerçek SYNAPSE ürünü değildir.
Yalnız stdlib, sentetik CSV; hiçbir harici sisteme yazmaz.
"""
import argparse, collections, csv, datetime as dt, json, pathlib, sys
NEEDED = ['case_id','event_id','activity','timestamp','actor','ornek_etiketi']
LABEL = 'SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL'
VALID = {'start','qualify','review','approve','close'}
def run(path, threshold=30):
    path=pathlib.Path(path)
    with path.open(encoding='utf-8-sig', newline='') as f:
        rd=csv.DictReader(f)
        missing=[k for k in NEEDED if k not in (rd.fieldnames or [])]
        if missing:
            return {'dataset':path.name,'status':'STOP','rules':[{'rule':'R1_SCHEMA','row':1,'decision':'STOP','detail':'Eksik kolon: '+', '.join(missing),'human':'Kaynak şemasını doğrulayın; tahmini tamamlamayın.'}],'events':0,'cases':0,'evidence_type':'GERÇEK YEREL KOD TESTİ / SENTETİK VERİ'}
        rows=list(rd)
    issues=[];bycase=collections.defaultdict(list); ids={}
    for lineno,row in enumerate(rows,2):
        if row['ornek_etiketi'] != LABEL: raise ValueError(f'Sentetik etiket eksik: satır {lineno}')
        eid=row['event_id'];key=row['case_id']
        if eid in ids:
            issues.append({'rule':'R3_DUPLICATE','row':lineno,'decision':'HOLD','detail':f"{eid}: tekrar eden event_id (ilk satır {ids[eid]})",'human':'Kaynak kayıt sürümü ve kimliği incelensin; otomatik silme yok.'})
        else: ids[eid]=lineno
        try: ts=dt.datetime.fromisoformat(row['timestamp'])
        except ValueError: ts=None
        if ts is None or ts.tzinfo is None:
            issues.append({'rule':'R2_ORDER','row':lineno,'decision':'HOLD','detail':'Zaman damgası geçersiz/saat dilimi yok','human':'Kaynağın saat dilimini teyit edin.'})
        bycase[key].append((lineno,row,ts))
    for key,events in bycase.items():
        for (line0,r0,t0),(line1,r1,t1) in zip(events,events[1:]):
            if t0 and t1:
                delta=(t1-t0).total_seconds()/60
                if delta<0: issues.append({'rule':'R2_ORDER','row':line1,'decision':'HOLD','detail':f'{key}: olay sırası -{abs(delta):g} dakika; {r0["activity"]} → {r1["activity"]}','human':'Saat dilimi, geç yükleme ve sıralama teyidi olmadan hatalı süreç denmez.'})
                elif delta>threshold: issues.append({'rule':'R4_WAIT','row':line1,'decision':'WARN','detail':f'{key}: {r0["activity"]} → {r1["activity"]} arasında {delta:g} dakika; eşik {threshold} dakika','human':'Takvim/mesai, kuyruk nedeni ve SLA kontrol edilsin; gecikme kesin hata değildir.'})
        closed=[(ln,r) for ln,r,_ in events if r['activity']=='close']
        if closed and not any(r['activity']=='approve' for ln,r,t in events if ln<closed[0][0]):
            issues.append({'rule':'R5_APPROVAL','row':closed[0][0],'decision':'HOLD','detail':f'{key}: kapanıştan önce approve olayı yok','human':'Gerçek onay kaydı veya süreç istisnası yetkili insanca teyit edilsin.'})
    issues.sort(key=lambda a:(a['row'],a['rule']))
    return {'dataset':path.name,'status':'REVIEW' if issues else 'PASS','events':len(rows),'cases':len(bycase),'threshold_minutes':threshold,'rules':issues,'rule_checks':['R1_SCHEMA','R2_ORDER','R3_DUPLICATE','R4_WAIT','R5_APPROVAL'],'evidence_type':'GERÇEK YEREL KOD TESTİ / SENTETİK VERİ','exclusion':'Canlı entegrasyon, SLA doğruluğu, gerçek müşteri, uygulama garantisi yok.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('csv');p.add_argument('--threshold',type=int,default=30);p.add_argument('--out');a=p.parse_args();result=run(a.csv,a.threshold);data=json.dumps(result,ensure_ascii=False,indent=2)
    if a.out:pathlib.Path(a.out).write_text(data+'\n',encoding='utf-8')
    print(data)
    # STOP negative outcome is designed domain outcome (not exception)
