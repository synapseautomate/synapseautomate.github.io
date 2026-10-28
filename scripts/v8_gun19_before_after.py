#!/usr/bin/env python3
"""Reproducible Git source before/after browser screenshots. No live customer activity."""
import pathlib,subprocess,tempfile,threading,http.server,socketserver,functools,json
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parents[1]
out=root/"operasyon/v8/gun-19/qa-before-after";out.mkdir(parents=True,exist_ok=True)
baseline="b2db84e1db00e4acbf0a6882e66c4b55643a113d"
class Server(socketserver.ThreadingMixIn,http.server.HTTPServer):daemon_threads=True
servers=[]; records=[]
with tempfile.TemporaryDirectory(prefix="synapse-before-") as temp:
 p=pathlib.Path(temp)/"source"
 subprocess.run(["git","worktree","add","--detach",str(p),baseline],cwd=root,check=True,stdout=subprocess.DEVNULL)
 try:
  for label,folder in [("before_main",p),("after_draft",root)]:
   h=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(folder))
   srv=Server(("127.0.0.1",0),h);servers.append(srv);threading.Thread(target=srv.serve_forever,daemon=True).start()
   with sync_playwright() as w:
    browser=w.chromium.launch(headless=True,args=["--no-sandbox"])
    for width in [320,390,768,1440]:
     pg=browser.new_page(viewport={"width":width,"height":850},device_scale_factor=1,reduced_motion="reduce")
     for fname in ["hizmetler.html","surec-analizi.html"]:
      u=f"http://127.0.0.1:{srv.server_port}/{fname}"
      pg.goto(u,wait_until="domcontentloaded",timeout=25000)
      name=f"{label}__{fname.replace('.html','')}__{width}.png"
      pg.screenshot(path=str(out/name),full_page=True,animations="disabled")
      records.append({"source":label,"path":fname,"width":width,"png":name,"link_voice":pg.locator('a[href="cozumler/sesli-yapay-zeka-randevu-insan-devri.html"]').count(),"required_consent":pg.locator('form[data-synapse-lead="process_analysis"] input[name="consent"][required]').count()})
     pg.close()
    browser.close()
 finally:
  for s in servers:s.shutdown()
  subprocess.run(["git","worktree","remove","--force",str(p)],cwd=root,check=False)
(out/"before-after-summary.json").write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"screenshots":len(records),"before_voice_link":next(x["link_voice"] for x in records if x["source"]=="before_main" and x["path"]=="hizmetler.html"),"after_voice_link":next(x["link_voice"] for x in records if x["source"]=="after_draft" and x["path"]=="hizmetler.html"),"before_consent":next(x["required_consent"] for x in records if x["source"]=="before_main" and x["path"]=="surec-analizi.html"),"after_consent":next(x["required_consent"] for x in records if x["source"]=="after_draft" and x["path"]=="surec-analizi.html")}))
