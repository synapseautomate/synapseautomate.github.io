from playwright.sync_api import sync_playwright
import http.server,socketserver,threading,functools,os,json,pathlib
P=pathlib.Path("qa/g20-mobile-fix"); P.mkdir(parents=True,exist_ok=True)
class S(socketserver.ThreadingMixIn,http.server.HTTPServer): daemon_threads=True
s=S(("127.0.0.1",0),functools.partial(http.server.SimpleHTTPRequestHandler,directory=os.getcwd()))
threading.Thread(target=s.serve_forever,daemon=True).start()
base=f"http://127.0.0.1:{s.server_port}/rehberler/ai-otomasyon-fiyatlari.html"
results=[];bad=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(headless=True,args=["--no-sandbox"])
 for w in [320,375,390,768,1024,1440]:
  context=b.new_context(viewport={"width":w,"height":850},device_scale_factor=1)
  pg=context.new_page();errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
  resp=pg.goto(base,wait_until="domcontentloaded",timeout=15000)
  dims=pg.evaluate("""() => ({root:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length,missingAlt:document.querySelectorAll('img:not([alt])').length,heading:document.querySelector('h1')?.textContent})""")
  out={"width":w,"http":resp.status,"scroll":dims["root"],"h1":dims["h1"],"missingAlt":dims["missingAlt"],"jsErr":errs}
  if resp.status!=200 or dims["root"]>w+1 or dims["h1"]!=1 or dims["missingAlt"] or errs:bad.append(out)
  pg.screenshot(path=str(P/f"fix-{w}.png"),full_page=True)
  results.append(out);pg.close();context.close()
 b.close()
s.shutdown();(P/"results.json").write_text(json.dumps({"results":results,"failures":bad},ensure_ascii=False,indent=2))
print(json.dumps({"passed":len(results)-len(bad),"total":len(results),"failures":bad},ensure_ascii=False))
if bad:raise SystemExit(1)
