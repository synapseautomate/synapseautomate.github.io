import fs from 'node:fs/promises';
import {chromium} from 'playwright';
const base='http://127.0.0.1:8765';
const out='/tmp/synapse-v8-day11-evidence';
await fs.mkdir(out,{recursive:true});
const sizes=[320,375,390,768,1024,1440];
const paths=['/cozumler/fatura-on-isleme-mutabakat-kontrolu.html','/hizmetler.html','/sektorler/finans-bankacilik.html'];
const issues=[],tests=[];
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
try{
 for(const vp of sizes){
  const page=await browser.newPage({viewport:{width:vp,height:vp<768?780:900},deviceScaleFactor:1});
  await page.route(/google-analytics\.com|googletagmanager\.com|formsubmit\.co/,route=>route.abort());
  const response=await page.goto(base+paths[0],{waitUntil:'networkidle',timeout:30000});
  if(response?.status()!==200)issues.push('Page HTTP '+vp+': '+response?.status());
  const a=await page.evaluate(()=>{
    const w=document.documentElement.clientWidth;
    const sw=Math.max(document.documentElement.scrollWidth,document.body.scrollWidth);
    const imgs=[...document.images];
    const targets=[...document.querySelectorAll('.btn')].map(e=>({text:e.textContent.trim(),height:Math.round(e.getBoundingClientRect().height)}));
    return {scrollWidth:sw,viewportWidth:w,brokenImages:imgs.filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),missingAlt:imgs.filter(i=>!i.getAttribute('alt')).map(i=>i.src),h1:document.querySelectorAll('h1').length,canonical:document.querySelector('link[rel="canonical"]')?.href,targets,synthetic:document.body.innerText.includes('SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL')};
  });
  if(a.scrollWidth>a.viewportWidth+3)issues.push('horizontal overflow '+vp+' '+(a.scrollWidth-a.viewportWidth));
  if(a.brokenImages.length)issues.push('broken images '+vp+': '+a.brokenImages.join(','));
  if(a.missingAlt.length)issues.push('missing alt '+vp);
  if(a.h1!==1)issues.push('wrong H1 '+vp);
  if(!a.canonical?.endsWith(paths[0]))issues.push('bad canonical '+vp);
  if(!a.synthetic)issues.push('missing synthetic label '+vp);
  if(a.targets.some(t=>t.height<44))issues.push('short CTA '+vp+' '+JSON.stringify(a.targets));
  if(vp===390){
   await page.keyboard.press('Tab');
   const focus=await page.evaluate(()=>document.activeElement?.getAttribute('href'));
   if(focus!=='#icerik')issues.push('skip link not first keyboard focus');
   await page.getByText('8 soruluk kontrol listesini aç').click();
   if(!page.url().includes('/araclar/finans-surec-kontrol-listesi.html'))issues.push('buyer CTA incorrect target');
   const inputs=page.locator('[data-check]');
   if(await inputs.count()!==8)issues.push('live self-assessment should have 8 checks');
   else{
    const before=await page.locator('#result').innerText();
    if(!before.includes('0/8'))issues.push('real tool missing 0/8 state');
    await inputs.first().check();
    const one=await page.locator('#result').innerText();
    if(!one.includes('1/8'))issues.push('real tool failed 1/8 update');
    tests.push({type:'existing-real-web-tool',initial:before.slice(0,70),first_checked:one.slice(0,100)});
   }
  }
  if(vp===375||vp===390||vp===1440)await page.screenshot({path:out+'/GUN11_SEO_'+vp+'.png',fullPage:true});
  tests.push({viewport:vp,...a});
  await page.close();
 }
 for(const p of paths.slice(1)){
  const page=await browser.newPage();
  const response=await page.goto(base+p,{waitUntil:'domcontentloaded'});
  if(response?.status()!==200)issues.push('source link parent HTTP failure '+p);
  if(await page.locator('a[href*="fatura-on-isleme-mutabakat-kontrolu.html"]').count()===0)issues.push('no contextual link: '+p);
  await page.close();
 }
}finally{await browser.close()}
const result={status:issues.length?'FAIL':'PASS',viewportCount:sizes.length,tests,issues,scope:'Chromium local source preview, not Safari, GSC or production live form'};
await fs.writeFile(out+'/SEO_QA_B_TARAYICI.json',JSON.stringify(result,null,2));
console.log(JSON.stringify({status:result.status,viewports:sizes.length,issues,controls:tests.length},null,2));
if(issues.length)process.exit(1);
