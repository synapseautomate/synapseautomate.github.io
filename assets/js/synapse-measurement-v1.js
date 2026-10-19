(function(){
'use strict';
var GA_ID='G-HQSRRJ5HMZ';
var KEY='synapse_attribution_v1';
var LEAD_PENDING_KEY='synapse_lead_pending_v1';

/* Optional analytics: zero network or attribution storage before explicit opt-in. */
var CONSENT_KEY='synapse_analytics_consent_v1';
function preference(){try{return localStorage.getItem(CONSENT_KEY)||''}catch(e){return''}}
var enabled=preference()==='granted';
function startCollector(){
  if(!enabled||window.__synapseGA4V1)return;
  window.__synapseGA4V1=true;
  window.dataLayer=window.dataLayer||[];
  window.gtag=window.gtag||function(){window.dataLayer.push(arguments)};
  window.gtag('js',new Date());
  window.gtag('config',GA_ID,{
    send_page_view:true,
    page_location:location.origin+location.pathname,
    allow_google_signals:false,
    allow_ad_personalization_signals:false
  });
  if(!document.querySelector('script[data-synapse-ga4="v1"]')){
    var ga=document.createElement('script');
    ga.async=true;
    ga.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GA_ID);
    ga.setAttribute('data-synapse-ga4','v1');
    document.head.appendChild(ga);
  }
}
if(enabled)startCollector();

function privacyControls(){
  if(document.querySelector('[data-synapse-privacy-controls]'))return;
  var css=document.createElement('style');
  css.textContent='.synapse-privacy-panel{position:fixed;bottom:16px;left:16px;z-index:2147483000;width:min(490px,calc(100% - 32px));box-sizing:border-box;padding:24px;border:1px solid #5a93a0;border-radius:20px;background:#071d2d;color:#f5fbff;box-shadow:0 16px 55px rgba(0,0,0,.52);font:400 15px/1.55 system-ui,-apple-system,Segoe UI,sans-serif}.synapse-privacy-panel[hidden]{display:none}.synapse-privacy-panel p{margin:0 0 16px}.synapse-privacy-panel a{color:#8df3da}.synapse-privacy-buttons{display:flex;flex-wrap:wrap;gap:12px}.synapse-privacy-buttons button,.synapse-privacy-toggle{min-height:44px;border:1px solid #8ccbd1;border-radius:30px;padding:10px 18px;font:700 14px/1.25 system-ui,sans-serif;cursor:pointer}.synapse-privacy-buttons [data-analytics-choice=granted]{background:#8af0b7;border-color:#8af0b7;color:#071a21}.synapse-privacy-buttons [data-analytics-choice=denied]{background:#163244;color:#fff}.synapse-privacy-toggle{position:fixed;bottom:12px;right:12px;z-index:2147482999;background:#0d2738;color:#d8eef1}.synapse-privacy-panel button:focus-visible,.synapse-privacy-toggle:focus-visible{outline:3px solid #fff;outline-offset:3px}@media(max-width:420px){.synapse-privacy-panel{bottom:60px;padding:20px}.synapse-privacy-toggle{font-size:12px;bottom:8px;right:8px}}';
  document.head.appendChild(css);
  var panel=document.createElement('aside');
  panel.className='synapse-privacy-panel';
  panel.setAttribute('data-synapse-privacy-controls','v1');
  panel.setAttribute('aria-label','Analitik ölçüm tercihi');
  panel.innerHTML='<p><strong>İsteğe bağlı analitik</strong></p><p>Site kullanımını anlamak için Google Analytics yalnız izin verirseniz yüklenir. Reddetmeniz hizmet içeriğini etkilemez. <a href="/gizlilik.html">Gizlilik bilgisi</a></p><div class="synapse-privacy-buttons"><button type="button" data-analytics-choice="denied">Reddet</button><button type="button" data-analytics-choice="granted">İzin ver</button></div>';
  var toggle=document.createElement('button');
  toggle.type='button';
  toggle.className='synapse-privacy-toggle';
  toggle.textContent='Ölçüm tercihleri';
  toggle.setAttribute('aria-label','Analitik ölçüm tercihlerini değiştir');
  toggle.addEventListener('click',function(){panel.hidden=false;panel.querySelector('button').focus()});
  panel.querySelectorAll('button[data-analytics-choice]').forEach(function(b){
    b.addEventListener('click',function(){
      var value=b.getAttribute('data-analytics-choice');
      try{
        localStorage.setItem(CONSENT_KEY,value);
        if(value==='denied'){localStorage.removeItem(KEY);sessionStorage.removeItem(LEAD_PENDING_KEY)}
        location.reload();
      }catch(e){
        panel.querySelector('p:nth-child(2)').textContent='Tercihiniz saklanamadı; analitik etkinleştirilmedi. Bu sayfada ölçüm başlatılmayacak.';
        if(value==='denied')panel.hidden=true;
      }
    })
  });
  panel.hidden=preference()==='granted'||preference()==='denied';
  document.body.appendChild(toggle);
  document.body.appendChild(panel);
}

function clean(v,n){return String(v||'').trim().slice(0,n||160)}
function utm(v,n){var x=clean(v,n).toLowerCase();return /^[a-z0-9_-]+$/.test(x)?x:''}
function refClass(ref){try{if(!ref)return'direct';var h=new URL(ref).hostname.toLowerCase();if(h.includes('google.'))return'search_google';if(h.includes('bing.com'))return'search_bing';if(h.includes('chatgpt.com')||h.includes('openai.com'))return'ai_chatgpt';if(h.includes('perplexity.ai'))return'ai_perplexity';if(h.includes('copilot.microsoft.com'))return'ai_copilot';if(h.includes('gemini.google.com'))return'ai_gemini';if(h.includes('linkedin.com'))return'social_linkedin';if(h.includes('youtube.com')||h.includes('youtu.be'))return'social_youtube';return'referral_other'}catch(e){return'unknown'}}
function touch(){var p=new URLSearchParams(location.search),r=refClass(document.referrer);return{source:utm(p.get('utm_source')||p.get('src')||(r==='direct'?'direct':r),80),medium:utm(p.get('utm_medium')||'',80),campaign:utm(p.get('utm_campaign')||'',120),content:utm(p.get('utm_content')||'',120),term:utm(p.get('utm_term')||'',120),asset:clean(location.pathname,160),cluster:utm(p.get('cluster')||'',120),referrer_class:r,landing:clean(location.pathname,160),ts:new Date().toISOString()}}
var last=touch(),first=last;if(enabled)try{var s=localStorage.getItem(KEY);if(s){var x=JSON.parse(s);if(x&&x.first)first=x.first}localStorage.setItem(KEY,JSON.stringify({first:first,last:last}))}catch(e){}
function emit(name,meta){var payload=Object.assign({event_version:'1',page_path:location.pathname,source:last.source,medium:last.medium,campaign:last.campaign,content:last.content,asset:last.asset,cluster:last.cluster,referrer_class:last.referrer_class},meta||{});try{if(enabled)window.gtag('event',name,payload)}catch(e){}try{window.dispatchEvent(new CustomEvent('synapse:event',{detail:Object.assign({event:name},payload)}))}catch(e){}return Object.assign({event:name},payload)}
function hidden(form,name,value){var x=form.querySelector('input[name="'+name.replace(/"/g,'')+'"]');if(!x){x=document.createElement('input');x.type='hidden';x.name=name;form.appendChild(x)}x.value=clean(value,240)}
function enrich(form){if(!enabled)return;hidden(form,'Attribution_Source',last.source);hidden(form,'Attribution_Medium',last.medium);hidden(form,'Attribution_Campaign',last.campaign);hidden(form,'Attribution_Content',last.content);hidden(form,'Attribution_Asset',last.asset);hidden(form,'Attribution_Cluster',last.cluster);hidden(form,'Attribution_Referrer',last.referrer_class);hidden(form,'Attribution_First_Touch',JSON.stringify(first));hidden(form,'Attribution_Last_Touch',JSON.stringify(last))}
function markLeadPending(form){if(!enabled)return;var kind=clean(form.getAttribute('data-synapse-lead')||'',80);if(!kind)return;try{sessionStorage.setItem(LEAD_PENDING_KEY,JSON.stringify({kind:kind,ts:Date.now()}))}catch(e){}}
function emitConfirmedLead(){if(!enabled)return;try{var p=new URLSearchParams(location.search),kind=clean(p.get('submitted')||'',80),pageKind=clean(document.body&&document.body.getAttribute('data-synapse-success')||'',80);if(!kind||kind!==pageKind)return;var raw=sessionStorage.getItem(LEAD_PENDING_KEY);if(!raw)return;var pending=JSON.parse(raw),age=Date.now()-Number(pending&&pending.ts||0);if(!pending||pending.kind!==kind||age<0||age>1800000)return;sessionStorage.removeItem(LEAD_PENDING_KEY);emit('generate_lead',{lead_type:kind,confirmation:'formsubmit_redirect'});var u=new URL(location.href);u.searchParams.delete('submitted');history.replaceState({},'',u.pathname+(u.searchParams.toString()?'?'+u.searchParams.toString():'')+u.hash)}catch(e){}}
function init(){privacyControls();document.querySelectorAll('form').forEach(function(f){enrich(f);f.addEventListener('submit',function(){enrich(f);markLeadPending(f);emit('lead_form_submit',{form_action:clean(f.getAttribute('action')||'',160)})},{capture:true})});emit('asset_view');emitConfirmedLead();document.querySelectorAll('[data-synapse-event]').forEach(function(el){el.addEventListener('click',function(){emit(el.getAttribute('data-synapse-event'),{event_label:clean(el.getAttribute('data-synapse-label')||el.textContent,100)})})})}
window.SynapseMeasurement={emit:emit,enrichForm:enrich,attribution:function(){return{first:first,last:last}},referrerClass:refClass,collector:function(){return{provider:'ga4',measurement_id:GA_ID}}};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
