#!/usr/bin/env python3
"""Read-only live HTTP audit. Tests CURRENT published main; NOT preview PR."""
import urllib.request,urllib.error,json,pathlib,datetime
urls=[
"https://synapseautomate.github.io/",
"https://synapseautomate.github.io/hizmetler.html",
"https://synapseautomate.github.io/surec-analizi.html",
"https://synapseautomate.github.io/iletisim.html",
"https://synapseautomate.github.io/talep-alindi.html",
"https://synapseautomate.github.io/404.html",
"https://synapseautomate.github.io/cozumler/sesli-yapay-zeka-randevu-insan-devri.html",
"https://synapseautomate.github.io/assets/media/g19/synapse-voice-human-handoff-horizontal.mp4",
"https://synapseautomate.github.io/assets/media/g19/synapse-voice-human-handoff-vertical.mp4",
"https://synapseautomate.github.io/bu-olmayan-gun19-sayfa-404-deneme.html"
]
rows=[]
for url in urls:
 try:
  req=urllib.request.Request(url,headers={"User-Agent":"SynapseDay19ReadOnlyQA/1.0"})
  with urllib.request.urlopen(req,timeout=12) as r:
   data=r.read(200000)
   rows.append({"url":url,"status":r.status,"bytes_read":len(data),"content_type":r.headers.get("Content-Type"),"note":"GET read-only; no form posts"})
 except urllib.error.HTTPError as ex: rows.append({"url":url,"status":ex.code,"note":"GET HTTP exception; no form posts"})
 except Exception as ex: rows.append({"url":url,"status":"TEST_EDILEMEDI","error":str(ex)[:180]})
out=pathlib.Path("operasyon/v8/gun-19/qa-browser-artifacts")
out.mkdir(parents=True,exist_ok=True)
(out/"http-readonly-live-main.json").write_text(json.dumps({"date_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"scope":"LIVE CURRENT MAIN ONLY; NOT draft branch","results":rows},ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(rows,ensure_ascii=False))
required=[r for r in rows if "/assets/media/g19/" in r["url"] or "/cozumler/sesli-yapay-zeka-randevu-insan-devri.html" in r["url"]]
fail=[r for r in required if r["status"]!=200 or (r["url"].endswith(".mp4") and "video/" not in (r.get("content_type") or ""))]
if fail:raise SystemExit("LIVE NEW MEDIA QA FAILED: "+json.dumps(fail,ensure_ascii=False))
