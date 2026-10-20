import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';
const out=process.env.SYNAPSE_MEDIA_DIR||'/tmp/synapse-v8-day11-finans-youtube';
fs.mkdirSync(out,{recursive:true});
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const context=await browser.newContext({viewport:{width:1920,height:1080},recordVideo:{dir:out,size:{width:1920,height:1080}},locale:'tr-TR'});
const page=await context.newPage();
const checks=[];
let vpath;
try{
  await page.route(/google-analytics\.com|googletagmanager\.com|formsubmit\.co/,r=>r.abort());
  await page.goto('http://127.0.0.1:8765/araclar/finans-surec-kontrol-listesi.html',{waitUntil:'domcontentloaded'});
  const count=await page.locator('[data-check]').count();
  if(count!==8)throw Error('Expected 8 real finance tool checkboxes, got '+count);
  const badge='SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL';
  await page.evaluate(label=>{
    const b=document.createElement('div');b.innerText=label+'  •  GERÇEK WEB ARACI';
    Object.assign(b.style,{position:'fixed',bottom:'18px',left:'27px',padding:'14px 18px',color:'#f3ffff',background:'#052431',font:'bold 19px Arial',border:'2px solid #87edbf',borderRadius:'10px',zIndex:'2147483647'});
    document.body.appendChild(b);
  },badge);
  await page.locator('#checks').scrollIntoViewIfNeeded();
  await page.waitForTimeout(850);
  const score=async()=>await page.locator('#result').innerText();
  let got=await score();
  if(!got.includes('0/8'))throw Error('Real initial state missing 0/8: '+got);
  checks.push({checked:0,actual:'0/8'});
  await page.screenshot({path:path.join(out,'FINANS_ARAC_00_1920x1080.png')});
  await page.waitForTimeout(1300);
  for(let i=1;i<=8;i++){
    await page.locator('[data-check]').nth(i-1).check();
    got=await score();
    if(!got.includes(i+'/8'))throw Error('Actual state mismatch: '+i+'/8, got '+got);
    checks.push({checked:i,actual:i+'/8'});
    await page.screenshot({path:path.join(out,'FINANS_ARAC_'+String(i).padStart(2,'0')+'_1920x1080.png')});
    await page.waitForTimeout(1450);
  }
  vpath=await page.video().path();
}finally{
 await context.close();
 if(vpath&&fs.existsSync(vpath))fs.copyFileSync(vpath,path.join(out,'FINANS_GERCEK_TARAYICI_HAM.webm'));
 await browser.close();
}
if(!fs.existsSync(path.join(out,'FINANS_GERCEK_TARAYICI_HAM.webm')))throw Error('Actual capture video missing');
fs.writeFileSync(path.join(out,'FINANS_YOUTUBE_GERCEK_ARAC_KANIT.json'),JSON.stringify({
  status:'PASS',source:'real existing web page on repository',url:'https://synapseautomate.github.io/araclar/finans-surec-kontrol-listesi.html',
  checkedSteps:checks,allSynthetic:true,label:'SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL',
  limitations:'A 8-checkbox browser self-assessment; NOT actual invoice preprocessing, bank, tax, ERP, or accounting reconciliation'
},null,2));
console.log(JSON.stringify({status:'PASS',verifiedSteps:checks.length,video:true}));
