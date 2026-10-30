#!/usr/bin/env python3
"""Day20 single-variable actual Chromium QA on main and draft, isolated no outbound submit."""
import pathlib, tempfile, subprocess, http.server, socketserver, functools, threading, json, sys
from playwright.sync_api import sync_playwright
ROOT=pathlib.Path(__file__).resolve().parents[1]
ART=ROOT/"operasyon/v8/gun-20/browser-evidence"
ART.mkdir(parents=True,exist_ok=True)
MAIN_SHA="05bd1f2a31d36fe92134e756e485a104337fbe9f"
WIDTHS=[320,375,390,768,1024,1440]
class Server(socketserver.ThreadingMixIn,http.server.HTTPServer):
 daemon_threads=True
handlers=[];failures=[];results=[]
target="rehberler/ai-otomasyon-fiyatlari.html"
newquestion="Talep tahmini için görünen fiyat kesin mi?"
with tempfile.TemporaryDirectory(prefix="synapse-g20-baseline-") as t:
 old=pathlib.Path(t)/"main"
 subprocess.run(["git","worktree","add","--detach",str(old),MAIN_SHA],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
 try:
  with sync_playwright() as pw:
   browser=pw.chromium.launch(headless=True,args=["--no-sandbox"])
   for label,site in [("before_main",old),("after_draft",ROOT)]:
    srv=Server(("127.0.0.1",0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(site)))
    handlers.append(srv)
    threading.Thread(target=srv.serve_forever,daemon=True).start()
    base=f"http://127.0.0.1:{srv.server_port}"
    for w in WIDTHS:
     context=browser.new_context(viewport={"width":w,"height":900},device_scale_factor=1,reduced_motion="reduce")
     context.route("**/*",lambda route:route.continue_() if route.request.url.startswith(base) else route.abort())
     page=context.new_page();errs=[]
     page.on("pageerror",lambda e:errs.append(str(e)))
     response=page.goto(base+"/"+target,wait_until="domcontentloaded",timeout=25000)
     page.wait_for_timeout(120)
     question=page.get_by_text(newquestion,exact=True)
     count=question.count()
     if label=="before_main" and count!=0: failures.append({"label":label,"width":w,"issue":"question unexpectedly on baseline"})
     if label=="after_draft" and count!=1: failures.append({"label":label,"width":w,"issue":"question missing or duplicate","count":count})
     if count:
      question.click()
      opened=question.evaluate("(el) => !!el.closest('details')?.open")
      if not opened:failures.append({"label":label,"width":w,"issue":"FAQ not open by pointer"})
      question.focus()
      page.keyboard.press("Enter")
      closed=question.evaluate("(el) => !el.closest('details')?.open")
      if not closed:failures.append({"label":label,"width":w,"issue":"FAQ not toggle by keyboard"})
      page.keyboard.press("Enter")
     if w==320:
      overflow=page.evaluate("""() => [...document.querySelectorAll('body *')].map(el=>({tag:el.tagName,classes:el.className?.toString().slice(0,65),text:el.textContent?.trim().slice(0,60),right:Math.ceil(el.getBoundingClientRect().right),left:Math.floor(el.getBoundingClientRect().left),width:Math.ceil(el.getBoundingClientRect().width)})).filter(x=>x.right>321 && x.width>0).sort((a,b)=>b.right-a.right).slice(0,18)""")
      print("OVERFLOW_ELEMENTS",label,json.dumps(overflow,ensure_ascii=False))
     info=page.evaluate("""() => ({h1:document.querySelectorAll('h1').length, imagesWithoutAlt:document.querySelectorAll('img:not([alt])').length, scrollWidth:document.documentElement.scrollWidth, title:document.title, hrefs:[...document.querySelectorAll('a[href]')].length})""")
     shot=f"{label}-{w}.png";page.screenshot(path=str(ART/shot),full_page=True,animations="disabled")
     okay=response.status==200 and info["h1"]==1 and info["imagesWithoutAlt"]==0 and not errs
     if not okay:failures.append({"label":label,"width":w,"issue":"render/check fail","status":response.status,"info":info,"js":errs})
     results.append({"kind":label,"width":w,"status":response.status,"h1":info["h1"],"horizontalOverflow":max(0,info["scrollWidth"]-w),"missingAlt":info["imagesWithoutAlt"],"FAQCount":count,"jsErrors":len(errs),"screenshot":shot,"result":("FAIL" if not okay else ("BASELINE_P1" if info["scrollWidth"]>w+1 else "PASS"))})
     page.close();context.close()
    srv.shutdown()
   browser.close()
 finally:subprocess.run(["git","worktree","remove","--force",str(old)],cwd=ROOT,check=False)
for w in WIDTHS:
 before=next(q for q in results if q["kind"]=="before_main" and q["width"]==w)
 after=next(q for q in results if q["kind"]=="after_draft" and q["width"]==w)
 if after["horizontalOverflow"]>before["horizontalOverflow"]:
  failures.append({"width":w,"issue":"NEW overflow regression","before":before["horizontalOverflow"],"after":after["horizontalOverflow"]})
report={"date":"2026-10-30","scope":"Chromium from checked out source; NOT real Safari, real FormSubmit, Search Console or field conversion.","main_sha":MAIN_SHA,"QA_turn":"Independent browser and source-regression","cases":results,"failures":failures}
(ART/"g20-qa-results.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"browserCases":len(results),"passed":sum(r["result"]=="PASS" for r in results),"existingP1":sum(r["result"]=="BASELINE_P1" for r in results),"failed":len(failures),"failures":failures},ensure_ascii=False))
sys.exit(1 if failures else 0)
