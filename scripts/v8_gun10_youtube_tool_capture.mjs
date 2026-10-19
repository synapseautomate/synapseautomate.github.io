import fs from 'node:fs';
import path from 'node:path';
import {chromium} from 'playwright';
const dir=process.env.SYNAPSE_MEDIA_DIR||'/tmp/synapse-social-v8-g10';
fs.mkdirSync(dir,{recursive:true});
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const context=await browser.newContext({
 viewport:{width:1920,height:1080},deviceScaleFactor:1,
 recordVideo:{dir,size:{width:1920,height:1080}},locale:'tr-TR'
});
const page=await context.newPage();
const expected=[];
let videoSource;
try{
 await page.route(/google-analytics|googletagmanager|doubleclick/,route=>route.abort());
 await page.addInitScript(()=>{try{localStorage.setItem('synapse_analytics_consent_v1','denied')}catch(e){}});
 await page.goto('http://127.0.0.1:8765/araclar/surec-hazirlik-skoru.html',{waitUntil:'domcontentloaded'});
 await page.waitForSelector('.q');
 await page.evaluate(()=>{
   const chip=document.createElement('div');
   chip.textContent='SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL • GERÇEK WEB ARACI KAYDI';
   Object.assign(chip.style,{position:'fixed',bottom:'22px',left:'22px',zIndex:'2147483000',color:'#f6fff9',background:'#072c3e',border:'2px solid #8af0b7',borderRadius:'12px',padding:'12px 22px',font:'bold 19px Arial, sans-serif'});
   document.body.appendChild(chip);
 });
 const score=page.locator('#score');
 if((await score.innerText()).trim()!=='0/100')throw Error('initial score not 0/100');
 await page.locator('.q').first().scrollIntoViewIfNeeded();
 await page.waitForTimeout(1600);
 const values=[15,15,15,15,15,10,10,5];
 let sum=0;
 for(let i=0;i<values.length;i++){
   await page.locator('.q').nth(i).check();
   sum+=values[i];
   const actual=(await score.innerText()).trim();
   if(actual!==sum+'/100')throw Error('score error '+(i+1)+': '+actual+' expected '+sum);
   expected.push({question:i+1,score:actual});
   await page.waitForTimeout(1650);
 }
 const end=(await page.locator('#scoreText').innerText()).trim();
 if(end!=='Dar ve ölçülebilir bir ilk uygulama adayı.')throw Error('unexpected final score category '+end);
 await page.waitForTimeout(2500);
 videoSource=await page.video().path();
}finally{await context.close();await browser.close();}
if(!videoSource)throw Error('video not recorded');
fs.copyFileSync(videoSource,path.join(dir,'SYNAPSE_GERCEK_ARAC_SENTETIK_KAYIT.webm'));
fs.writeFileSync(path.join(dir,'YOUTUBE_GERCEK_ARAC_QA.json'),JSON.stringify({
 status:'PASS',sourceFile:'araclar/surec-hazirlik-skoru.html',
 publicURL:'https://synapseautomate.github.io/araclar/surec-hazirlik-skoru.html',
 kind:'Real interactive web tool recorded in Chromium',input:'All 8 checkboxes selected using synthetic example',
 checkpoints:expected,scoreFinal:'100/100',
 scopeLimits:'Not a CRM product, not a customer system, not a commercial outcome; no live integration'
},null,2));
console.log(JSON.stringify({result:'PASS',checkpoints:expected,recorded:true}));
