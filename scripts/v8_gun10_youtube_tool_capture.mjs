import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';

const out=process.env.SYNAPSE_MEDIA_DIR||'/tmp/synapse-social-v8-g10';
fs.mkdirSync(out,{recursive:true});
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const context=await browser.newContext({viewport:{width:1920,height:1080},deviceScaleFactor:1,locale:'tr-TR',recordVideo:{dir:out,size:{width:1920,height:1080}}});
const page=await context.newPage();
const weights=[15,15,15,15,15,10,10,5];
const steps=[];
let videoPath='';
try {
  await page.route(/googletagmanager\.com|google-analytics\.com/,route=>route.abort());
  await page.addInitScript(()=>{
    try{localStorage.setItem('synapse_analytics_consent_v1','denied')}catch(e){}
  });
  // The opening card is editorial, clearly distinguished from the working site.
  await page.setContent('<!doctype html><html lang="tr"><meta charset="utf-8"><body style="margin:0;background:#041723;color:#f1fbff;font-family:Arial,sans-serif"><div style="margin:180px auto;width:1460px;border-left:10px solid #80e6b4;padding:45px 70px"><p style="font-size:30px;letter-spacing:3px;color:#75ddeb">SYNAPSE AUTOMATE / GERÇEK WEB ARACI KAYDI</p><h1 style="font-size:100px;line-height:1.08;margin:40px 0">8 soru.<br>Kontrollü başlangıç.</h1><p style="font-size:36px;color:#c0dce7">Gerçek arayüz · Sentetik yanıtlar · Satış veya CRM entegrasyonu değildir.</p><p style="font-size:24px;color:#9ddfc9">SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL</p></div></body></html>');
  await page.waitForTimeout(2700);
  await page.goto('http://127.0.0.1:8765/araclar/surec-hazirlik-skoru.html',{waitUntil:'domcontentloaded'});
  await page.addStyleTag({content:'html {scroll-behavior:auto!important;} body {zoom:1.18;} #score {font-weight:900!important;} .progress {display:none!important;}'});
  await page.evaluate(()=>{
    const badge=document.createElement('div');
    badge.textContent='SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL · ÇALIŞAN WEB ARACI';
    Object.assign(badge.style,{position:'fixed',left:'28px',bottom:'22px',zIndex:2147483000,background:'#051e2b',border:'2px solid #8ef0bf',borderRadius:'10px',padding:'14px 20px',color:'#f6ffff',font:'bold 20px Arial',boxShadow:'0 12px 35px rgba(0,0,0,.5)'});
    document.body.appendChild(badge);
  });
  const score=page.locator('#score');
  if((await score.innerText()).trim()!=='0/100')throw Error('Initial score not 0/100');
  await page.locator('.q').first().scrollIntoViewIfNeeded();
  await page.waitForTimeout(1300);
  let total=0;
  for(let i=0;i<weights.length;i++){
    await page.locator('.q').nth(i).check();
    total+=weights[i];
    const observed=(await score.innerText()).trim();
    if(observed!==total+'/100')throw Error('Unexpected score at step '+(i+1)+' observed='+observed+' expected='+total);
    steps.push({question:i+1,points:weights[i],score:observed});
    await page.waitForTimeout(1400);
  }
  const result=(await page.locator('#scoreText').innerText()).trim();
  if(result!=='Dar ve ölçülebilir bir ilk uygulama adayı.')throw Error('Unexpected result: '+result);
  await score.scrollIntoViewIfNeeded();
  await page.waitForTimeout(2200);
  videoPath=await page.video().path();
}finally{
  await context.close();
  if(videoPath && fs.existsSync(videoPath))fs.copyFileSync(videoPath,path.join(out,'SYNAPSE_YOUTUBE_GERCEK_TARAYICI_KAYDI.webm'));
  await browser.close();
}
fs.writeFileSync(path.join(out,'YOUTUBE_GERCEK_ARAC_QA.json'),JSON.stringify({
 result:'PASS',source:'araclar/surec-hazirlik-skoru.html',method:'real browser interactions, not invented UI',
 testKind:'all 8 user choices synthetic',steps,finalScore:steps.at(-1)?.score,
 label:'SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL',
 disclaimer:'A web-based readiness self-assessment, not a working CRM integration or customer case.'
},null,2));
console.log(JSON.stringify({result:'PASS',score:steps.at(-1)?.score,checks:steps.length,videoExists:fs.existsSync(path.join(out,'SYNAPSE_YOUTUBE_GERCEK_TARAYICI_KAYDI.webm'))}));
