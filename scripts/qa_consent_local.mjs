import { chromium } from "playwright";

const browser=await chromium.launch({headless:true,args:["--no-sandbox"]});
const errors=[], checks=[];
try{
  const context=await browser.newContext({viewport:{width:390,height:844}});
  const page=await context.newPage();
  const requests=[];
  page.on("request",request=>{if(/googletagmanager\.com|google-analytics\.com/.test(request.url()))requests.push(request.url())});
  await page.route(/googletagmanager\.com|google-analytics\.com/,route=>route.abort());
  await page.goto("http://127.0.0.1:8765/",{waitUntil:"networkidle"});
  const initial=await page.evaluate(()=>({consent:localStorage.getItem("synapse_analytics_consent_v1"),attribution:localStorage.getItem("synapse_attribution_v1"),collector:!!document.querySelector('script[data-synapse-ga4="v1"]')}));
  if(requests.length||initial.attribution||initial.collector)errors.push("No-consent external request / attribution / collector detected");
  else checks.push("before-consent no requests / attribution: PASS");
  const agree=page.getByRole("button",{name:"İzin ver"});
  if(!(await agree.isVisible()))errors.push("Analytic opt-in control hidden initially");
  else checks.push("accessible opt-in: PASS");
  await agree.click();
  await page.waitForLoadState("networkidle");
  const granted=await page.evaluate(()=>({consent:localStorage.getItem("synapse_analytics_consent_v1"),attribution:!!localStorage.getItem("synapse_attribution_v1"),collector:!!document.querySelector('script[data-synapse-ga4="v1"]')}));
  if(granted.consent!=="granted"||!granted.attribution||!granted.collector||requests.length===0)errors.push("Consent grant missing tracking or preference");
  else checks.push("granted triggers collector/attribution: PASS");
  await page.getByRole("button",{name:"Analitik ölçüm tercihlerini değiştir"}).click();
  const num=requests.length;
  await page.getByRole("button",{name:"Reddet"}).click();
  await page.waitForLoadState("networkidle");
  const declined=await page.evaluate(()=>({consent:localStorage.getItem("synapse_analytics_consent_v1"),attribution:localStorage.getItem("synapse_attribution_v1"),collector:!!document.querySelector('script[data-synapse-ga4="v1"]')}));
  if(declined.consent!=="denied"||declined.attribution||declined.collector||requests.length>num)errors.push("Revocation did not stop subsequent requests/storage");
  else checks.push("revocation and reload stops analytics: PASS");
  // Negative tests: legacy pre-consent attribution is erased and raw PII-like UTMs are suppressed.
  await page.evaluate(()=>localStorage.setItem("synapse_attribution_v1",JSON.stringify({first:{ts:new Date().toISOString(),source:"legacy"}})));
  await page.goto("http://127.0.0.1:8765/?utm_source=person%40example.com&utm_medium=Organic_Social",{waitUntil:"networkidle"});
  const unsafe=await page.evaluate(()=>({
    attribution:localStorage.getItem("synapse_attribution_v1"),
    source:window.SynapseMeasurement.attribution().last.source,
    medium:window.SynapseMeasurement.attribution().last.medium,
    analyticsLoaded:!!document.querySelector('script[data-synapse-ga4="v1"]')
  }));
  if(unsafe.attribution!==null||unsafe.source!==""||unsafe.medium!=="organic_social"||unsafe.analyticsLoaded)
    errors.push("PII-like UTM or legacy pre-consent storage negative test failed");
  else checks.push("legacy storage purge and PII-like UTM rejection: PASS");
  await context.close();
}finally{await browser.close()}
console.log(JSON.stringify({status:errors.length?"FAIL":"PASS",checks,errors},null,2));
if(errors.length)process.exit(1);
