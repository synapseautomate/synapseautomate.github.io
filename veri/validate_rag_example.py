"""Sentetik RAG kaynak envanteri testi. Canlı RAG asistanı veya model testi DEĞİLDİR."""
import csv
from pathlib import Path
P=Path(__file__).parent
D=list(csv.DictReader((P/'rag_ornek_kaynak_envanteri.csv').open(encoding='utf-8-sig'),delimiter=';'))
T=list(csv.DictReader((P/'rag_beklenen_kontrol_sonuclari.csv').open(encoding='utf-8-sig'),delimiter=';'))
d={x['kaynak_id']+'@'+x['surum']+'#'+x['bolum']:x for x in D if x['durum']=='GUNCEL' and x['erisim']=='EKIP'}
assert len(D)==5 and len(T)==5
assert 'KB-OPS-01@v2#3.2' in d
assert 'KB-OPS-01@v1#3.2' not in d
assert 'KB-IK-03@v1#1.1' not in d
assert T[3]['kaynak']=='YOK' and T[3]['karar']=='BILINMIYOR'
assert T[4]['karar']=='INSAN_INCELEMESI'
print('5/5 PASS — deterministik sentetik kaynak denetimi; canlı RAG testi yapılmadı')
