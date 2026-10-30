#!/usr/bin/env python3
import urllib.request,time,json,sys
base="https://synapseautomate.github.io/"
uris=["","surec-analizi.html","rehberler/ai-otomasyon-fiyatlari.html","assets/media/g20/SYNAPSE_G20_TALEP_TAHMINI_YATAY.mp4","assets/media/g20/SYNAPSE_G20_TALEP_TAHMINI_DIKEY.mp4"]
rows=[];fails=[]
for p in uris:
 url=base+p;done=None
 for attempt in range(1,5):
  try:
   req=urllib.request.Request(url,headers={"User-Agent":"SYNAPSE-V8-ReadOnly-QA/1.0"})
   with urllib.request.urlopen(req,timeout=20) as resp:
    data=resp.read()
    typ=resp.headers.get("Content-Type","").lower()
    done={"url":url,"status":resp.status,"bytes":len(data),"type":typ,"attempt":attempt}
    if resp.status!=200:raise ValueError("Unexpected status")
    if p.endswith(".mp4") and (("video/" not in typ) or len(data)<10000 or data[4:8]!=b"ftyp"):
     raise ValueError("MP4 MIME or binary box verification failed")
    if p.endswith("ai-otomasyon-fiyatlari.html") and "Talep tahmini için görünen fiyat kesin mi?".encode("utf8") not in data:
     raise ValueError("Published FAQ missing")
    if p=="surec-analizi.html" and b"rehberler/ai-otomasyon-fiyatlari.html" not in data:
     raise ValueError("Price guide is not linked from actual site path")
    break
  except Exception as e:
   done={"url":url,"attempt":attempt,"status":"FAIL","reason":str(e)[:180]}
   if attempt<4:time.sleep(12)
 if done["status"]!="FAIL" and done.get("status")==200:rows.append(done)
 else:fails.append(done)
print(json.dumps({"passed":len(rows),"failed":len(fails),"results":rows,"failures":fails},ensure_ascii=False))
if fails:sys.exit(1)
