import fs from "node:fs/promises";
import { chromium } from "playwright";

// Render the STAGED public artifact locally, not production, before deployment.
const base = process.env.SMOKE_BASE || "http://127.0.0.1:8765";
const paths = [
  "/", "/kaynaklar.html", "/surec-analizi.html",
  "/rehberler/ai-otomasyon-fiyatlari.html",
  "/cozumler/roofing-ev-hizmetleri.html",
  "/kanit/ev-hizmetleri-talep-yonlendirme-ornek-akis.html",
  "/teklif/ev-hizmetleri-surec-analizi.html"
];
const sizes = [{width: 360,height: 740}, {width: 390,height: 844}];
const browser = await chromium.launch({headless:true, args:["--no-sandbox"]});
const issues = [];
try {
  await fs.mkdir("/tmp/synapse-mobile-qa",{recursive:true});
  for(const path of paths) {
    for(const viewport of sizes) {
      const page = await browser.newPage({viewport,deviceScaleFactor:1});
      const url = base+path, label=path.replace(/[^a-z0-9]/gi,"_") || "home";
      try {
        const response = await page.goto(url,{waitUntil:"networkidle",timeout:25000});
        if(!response || response.status()!==200) issues.push(path+": HTTP "+(response?.status()??"none"));
        const x=await page.evaluate(()=>{
          const w=document.documentElement.clientWidth;
          const sw=Math.max(document.documentElement.scrollWidth,document.body?.scrollWidth||0);
          const imgs=[...document.images].filter(img=>img.getAttribute("src")?.startsWith("/") || img.getAttribute("src")?.startsWith("../") || img.getAttribute("src")?.startsWith("assets/"));
          return {clientWidth:w,scrollWidth:sw,brokenLocalImages:imgs.filter(i=>!i.complete || i.naturalWidth===0).map(i=>i.getAttribute("src")).slice(0,8)};
        });
        if(x.scrollWidth>x.clientWidth+3) issues.push(path+" "+viewport.width+"px: horizontal overflow "+(x.scrollWidth-x.clientWidth)+"px");
        if(x.brokenLocalImages.length) issues.push(path+" "+viewport.width+"px: image failures "+JSON.stringify(x.brokenLocalImages));
        await page.screenshot({path:"/tmp/synapse-mobile-qa/"+label+"_"+viewport.width+".png",fullPage:true});
      } catch(e) {issues.push(path+" "+viewport.width+"px: "+String(e).slice(0,300));}
      finally {await page.close();}
    }
  }
} finally {await browser.close();}
console.log(JSON.stringify({status:issues.length?"FAIL":"PASS",tested:paths.length*sizes.length,issues},null,2));
if(issues.length) process.exit(1);
