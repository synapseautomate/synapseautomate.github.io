#!/usr/bin/env python3
"""Day19: isolated local Chromium QA on full GitHub checkout. No real form submissions."""
import contextlib, functools, http.server, json, pathlib, socketserver, threading, sys
from playwright.sync_api import sync_playwright

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT / "operasyon" / "v8" / "gun-19" / "qa-browser-artifacts"
OUT.mkdir(parents=True,exist_ok=True)
WIDTHS=[320,375,390,768,1024,1440]
PAGES=["index.html","hizmetler.html","cozumler/sesli-yapay-zeka-randevu-insan-devri.html","iletisim.html?konu=sesli-yapay-zeka","surec-analizi.html","talep-alindi.html","404.html"]
class Server(socketserver.ThreadingMixIn,http.server.HTTPServer): daemon_threads=True
handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT))
server=Server(("127.0.0.1",0),handler)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
base=f"http://127.0.0.1:{server.server_port}"
results=[];failures=[]
try:
 with sync_playwright() as pw:
  browser=pw.chromium.launch(headless=True,args=["--no-sandbox"])
  for width in WIDTHS:
   context=browser.new_context(viewport={"width":width,"height":870},device_scale_factor=1,reduced_motion="reduce")
   # Internet blocked for QA; analytics, FormSubmit and phone platforms cannot receive data.
   context.route("**/*", lambda route:route.continue_() if route.request.url.startswith(base) else route.abort())
   page=context.new_page()
   page_errors=[];page.on("pageerror",lambda exc:page_errors.append(str(exc)))
   for target in PAGES:
    route=target.split("?")[0]
    response=page.goto(base+"/"+target,wait_until="domcontentloaded",timeout=20000)
    page.wait_for_timeout(160)
    data=page.evaluate("""() => ({
      viewport: innerWidth,
      scrollWidth: document.documentElement.scrollWidth,
      h1:document.querySelectorAll('h1').length,
      imgWithoutAlt:document.querySelectorAll('img:not([alt])').length,
      title:document.title,
      links:[...document.querySelectorAll('a[href]')].length
    })""")
    slug=route.replace("/","_").replace(".html","")
    screenshot=OUT/f"{slug}-{width}.png"
    page.screenshot(path=str(screenshot),full_page=True,animations="disabled")
    ok=(response.status==200 and data["scrollWidth"]<=width+1 and data["h1"]==1 and data["imgWithoutAlt"]==0)
    result={"width":width,"page":target,"local_http":response.status,"scroll_width":data["scrollWidth"],"h1":data["h1"],"img_without_alt":data["imgWithoutAlt"],"screenshot":str(screenshot.relative_to(ROOT)),"result":"PASS" if ok else "FAIL"}
    results.append(result)
    if not ok: failures.append(result)
    if route=="iletisim.html":
     chosen=page.locator("select#konu").input_value()
     if chosen!="Sesli Yapay Zekâ ve Çağrı Merkezi":failures.append({"test":"voice contact preselection","got":chosen,"width":width})
     if page.locator('form#contact-form input[name="consent"][required]').count()!=1:failures.append({"test":"contact consent", "width":width})
     if page.locator('form#contact-form').get_attribute("action")!="https://formsubmit.co/synapseautomate.ai@gmail.com":failures.append({"test":"contact form target", "width":width})
    if route=="surec-analizi.html":
     if page.locator('form[data-synapse-lead="process_analysis"] input[name="consent"][required]').count()!=1:failures.append({"test":"process form consent","width":width})
    if route=="cozumler/sesli-yapay-zeka-randevu-insan-devri.html":
     if page.locator('a[href="/iletisim.html?konu=sesli-yapay-zeka"]').count()!=1:failures.append({"test":"voice CTA missing","width":width})
    if route=="hizmetler.html":
     if page.locator('a[href="cozumler/sesli-yapay-zeka-randevu-insan-devri.html"]').count()!=1:failures.append({"test":"service->voice link","width":width})
   if page_errors:failures.append({"width":width,"js_errors":page_errors})
   page.close();context.close()
  browser.close()
finally:server.shutdown()
report={"scope":"local Chromium on checked-out PR source. NOT live HTTP, Safari, real physical device, GA4, or FormSubmit delivery.","results":results,"failures":failures,"viewport_pass":sum(r["result"]=="PASS" for r in results),"viewport_total":len(results)}
(OUT/"qa-browser-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"passed":report["viewport_pass"],"total":report["viewport_total"],"failures":failures},ensure_ascii=False))
sys.exit(1 if failures else 0)
