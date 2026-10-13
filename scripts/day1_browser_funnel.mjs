import { chromium } from 'playwright';
// No real form POST, no GA4/Google collection, no real inbox delivery.
const base=process.env.SMOKE_BASE||'http://127.0.0.1:8765';
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const failures=[];
const expect=(condition,message)=>{if(!condition)failures.push(message)};
const ctx=await browser.newContext({viewport:{width:390,height:844}});
try {
  await ctx.route(/https?:\/\/(?:www\.)?(?:googletagmanager\.com|google-analytics\.com|analytics\.google\.com)\//,r=>r.abort());
  const page=await ctx.newPage();
  await page.addInitScript(()=>{
    window.addEventListener('synapse:event',(e)=>{
      try { const arr=JSON.parse(sessionStorage.getItem('__day1_test_events')||'[]'); arr.push(e.detail.event);sessionStorage.setItem('__day1_test_events',JSON.stringify(arr)); } catch(e) {}
    });
  });
  // A direct thank-you URL must not manufacture a lead.
  await page.goto(base+'/talep-alindi.html?submitted=process_analysis',{waitUntil:'networkidle'});
  let events=await page.evaluate(()=>JSON.parse(sessionStorage.getItem('__day1_test_events')||'[]'));
  expect(events.filter(x=>x==='generate_lead').length===0,'Direct thank-you visit generated a false lead');
  for(const path of ['/sektorler/e-ticaret.html','/rehberler/e-ticaret-ai-otomasyon-satin-alma-rehberi.html','/urunler.html']) {
    await page.goto(base+path,{waitUntil:'domcontentloaded'});
    const anchor=page.locator('a[href*="teklif/e-ticaret-surec-analizi.html"]').first();
    expect(await anchor.count()===1,path+': offer link missing');
    if(await anchor.count()){
      await anchor.click();
      expect(new URL(page.url()).pathname==='/teklif/e-ticaret-surec-analizi.html',path+': offer link broken');
    }
  }
  await page.goto(base+'/',{waitUntil:'domcontentloaded'});
  const homePrimary=page.locator('.hero .actions .btn-primary').first();
  expect((await homePrimary.getAttribute('href'))==='teklif/e-ticaret-surec-analizi.html','Home primary CTA missing e-commerce offer');
  await homePrimary.click();
  expect(new URL(page.url()).pathname==='/teklif/e-ticaret-surec-analizi.html','Home CTA does not open offer');
  const offerLink=page.locator('a[href^="../surec-analizi.html"]').first();
  await offerLink.click();
  expect(new URL(page.url()).pathname==='/surec-analizi.html','Offer CTA does not open single form');
  expect(await page.locator('form[data-synapse-lead="process_analysis"]').count()===1,'Primary form missing');
  // Intercept submission: this validates the client-side redirect contract only.
  await page.route('https://formsubmit.co/**',route=>{
    expect(route.request().method()==='POST','Form submission did not use POST');
    route.fulfill({status:302,headers:{location:base+'/talep-alindi.html?submitted=process_analysis'},body:''});
  });
  await page.locator('#email').fill('test@example.invalid');
  await page.locator('#volume').fill('Haftada on iade incelemesi');
  await page.locator('#loss').fill('Görev sahipliği karışıyor');
  await page.locator('#owner').fill('İşletme sahibi');
  await Promise.all([page.waitForURL('**/talep-alindi.html**',{timeout:15000}),page.locator('button[type=submit]').click()]);
  await page.waitForTimeout(250);
  events=await page.evaluate(()=>JSON.parse(sessionStorage.getItem('__day1_test_events')||'[]'));
  expect(events.filter(x=>x==='generate_lead').length===1,'Simulated valid return failed to emit one lead event');
  await page.reload({waitUntil:'networkidle'});
  events=await page.evaluate(()=>JSON.parse(sessionStorage.getItem('__day1_test_events')||'[]'));
  expect(events.filter(x=>x==='generate_lead').length===1,'Reload double-counted simulated lead');
  expect(!page.url().includes('submitted=process_analysis'),'Confirmation query not cleaned after one use');
} catch(e){failures.push(String(e).slice(0,700));}
finally {await browser.close()}
console.log(JSON.stringify({test:'Day1 simulated buyer funnel, zero real submits',status:failures.length?'FAIL':'PASS',failures},null,2));
if(failures.length) process.exit(1);
