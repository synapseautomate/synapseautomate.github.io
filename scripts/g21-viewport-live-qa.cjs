const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const browser = await chromium.launch({headless:true});
  const widths=[320,375,390,768,1024,1440];
  fs.mkdirSync('g21-viewport-evidence',{recursive:true});
  let fail=0;
  for(const width of widths){
    const page=await browser.newPage({viewport:{width,height:900},deviceScaleFactor:1,locale:'tr-TR'});
    const errs=[];
    page.on('pageerror',e=>errs.push(e.message));
    const res=await page.goto('https://synapseautomate.github.io/cozumler/musteri-asistani-sss-insan-devri.html',{waitUntil:'networkidle',timeout:30000});
    const stat=await page.evaluate(()=>{
      let de=document.documentElement; const h1=document.querySelectorAll('h1');const logo=document.querySelector('header img');
      return {width:innerWidth,scroll:de.scrollWidth,client:de.clientWidth,h1:h1.length,logoReady:Boolean(logo&&logo.complete&&logo.naturalWidth>0),cta:document.querySelectorAll('a[href*="surec-analizi.html"]').length,disclosure:document.body.textContent.includes('SENTETİK ÖRNEK'), nav:[...document.querySelectorAll('.navlinks a')].map(x=>({text:x.textContent,rect:x.getBoundingClientRect().toJSON()}))};
    });
    let pass=Boolean(res&&res.status()===200&&stat.scroll<=width+1&&stat.h1===1&&stat.logoReady&&stat.cta>=1&&stat.disclosure&&!errs.length);
    await page.screenshot({path:'g21-viewport-evidence/g21-'+width+'.png',fullPage:true});
    console.log(JSON.stringify({viewport:width,status:res?.status(),pass,metric:stat,js_errors:errs.slice(0,2)}));
    if(!pass) fail++;
    await page.close();
  }
  await browser.close();
  if(fail){console.log('G21 VIEWPORT FAIL',fail);process.exit(1)}
  console.log('G21 CHROMIUM 6/6 PASS (not Safari)');
})().catch(e=>{console.error(e);process.exit(1)});
