import { chromium } from 'playwright';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const base = 'http://127.0.0.1:8765';
const path = '/cozumler/ik-cv-on-eleme-insan-karari.html';
const widths=[320,375,390,768,1024,1440];
const dir='/tmp/synapse-v8-day12-evidence';
fs.mkdirSync(dir,{recursive:true});
const browser=await chromium.launch({headless:true});
const results=[];
try {
 for(const width of widths){
  const page=await browser.newPage({viewport:{width,height:900},deviceScaleFactor:1});
  const response=await page.goto(base+path,{waitUntil:'networkidle',timeout:25000});
  assert.equal(response.status(),200);
  const data=await page.evaluate(()=>{
   const img=document.querySelector('.brand img');
   const h1=document.querySelectorAll('h1');
   const overflow=document.documentElement.scrollWidth-window.innerWidth;
   const cta=document.querySelector('.last .btn.primary');
   const rect=cta.getBoundingClientRect();
   const match=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
   const panel=document.querySelector('.synapse-privacy-panel');
   const hero=document.querySelector('.mast');
   const consentInFlow=!!(panel&&panel.nextElementSibling===document.getElementById('main')&&getComputedStyle(panel).position!=='fixed');
   const consentOccludesHero=!!(panel&&!panel.hidden&&panel.getBoundingClientRect().bottom>hero.getBoundingClientRect().top);
   return {overflow,logoLoaded:img.complete&&img.naturalWidth>0,headings:h1.length,ctaSize:[rect.width,rect.height],ctaVisible:rect.width>0,synthetic:document.body.textContent.includes('SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL'),match,consentInFlow,consentOccludesHero};
  });
  assert.equal(data.headings,1,'H1 count '+width);
  assert.ok(data.overflow<=1,'horizontal overflow '+width+': '+data.overflow);
  assert.ok(data.logoLoaded,'brand original failed to load at '+width);
  assert.ok(data.ctaVisible&&data.ctaSize[1]>=44,'CTA tap target '+width);
  assert.ok(data.synthetic,'synthetic disclaimer missing '+width);
  assert.ok(data.consentInFlow&&!data.consentOccludesHero,'consent overlaps hero '+width);
  await page.screenshot({path:`${dir}/ik_${width}.png`,fullPage:true});
  await page.keyboard.press('Tab');
  const focus=await page.evaluate(()=>document.activeElement?.className||document.activeElement?.tagName);
  assert.ok(String(focus).includes('skip'),'skip navigation accessibility '+width);
  results.push({width,status:'PASS',...data,keyboardSkip:focus});
  await page.close();
 }
 const page=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});
 await page.goto(base+path,{waitUntil:'networkidle'});
 const reduced=await page.evaluate(()=>getComputedStyle(document.documentElement).scrollBehavior);
 assert.equal(reduced,'auto','Reduced motion preference');
 await page.close();
 const nav=await browser.newPage();
 await nav.goto(base+'/hizmetler.html',{waitUntil:'domcontentloaded'});
 const link=nav.locator('a[href="cozumler/ik-cv-on-eleme-insan-karari.html"]');
 assert.equal(await link.count(),1,'service link');
 await link.click();
 assert.ok(nav.url().endsWith(path),'main service navigation');
 await nav.close();
 fs.writeFileSync(dir+'/viewport-results.json',JSON.stringify({test:'v8_day12_ik',results,reducedMotion:reduced},null,2));
 console.log('QA-B BROWSER PASS:',JSON.stringify(results.map(x=>({w:x.width,overflow:x.overflow,logo:x.logoLoaded,cta:x.ctaSize}))));
 console.log('SIX RENDER SCREENSHOTS + KEYBOARD + REDUCED MOTION: PASS; Safari/real device: NOT_TESTED.');
}catch(e){console.error('QA-B FAIL:',e.stack);process.exitCode=1}finally{await browser.close()}
