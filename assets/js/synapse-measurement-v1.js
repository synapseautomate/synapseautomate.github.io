(function(){
'use strict';
var GA_ID='G-HQSRRJ5HMZ';
var KEY='synapse_attribution_v1';

/* Google Analytics 4 collector. No advertising signals are enabled here. */
window.dataLayer=window.dataLayer||[];
window.gtag=window.gtag||function(){window.dataLayer.push(arguments)};
window.gtag('js',new Date());
window.gtag('config',GA_ID,{
  send_page_view:true,
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

function clean(v,n){return String(v||'').trim().slice(0,n||160)}
function refClass(ref){try{if(!ref)return'direct';var h=new URL(ref).hostname.toLowerCase();if(h.includes('google.'))return'search_google';if(h.includes('bing.com'))return'search_bing';if(h.includes('chatgpt.com')||h.includes('openai.com'))return'ai_chatgpt';if(h.includes('perplexity.ai'))return'ai_perplexity';if(h.includes('copilot.microsoft.com'))return'ai_copilot';if(h.includes('gemini.google.com'))return'ai_gemini';if(h.includes('linkedin.com'))return'social_linkedin';if(h.includes('youtube.com')||h.includes('youtu.be'))return'social_youtube';return'referral_other'}catch(e){return'unknown'}}
function touch(){var p=new URLSearchParams(location.search),r=refClass(document.referrer);return{source:clean(p.get('utm_source')||p.get('src')||(r==='direct'?'direct':r),80),medium:clean(p.get('utm_medium')||'',80),campaign:clean(p.get('utm_campaign')||'',120),content:clean(p.get('utm_content')||'',120),term:clean(p.get('utm_term')||'',120),asset:clean(p.get('asset')||p.get('utm_content')||location.pathname,160),cluster:clean(p.get('cluster')||'',120),referrer_class:r,landing:clean(location.pathname,160),ts:new Date().toISOString()}}
var last=touch(),first=last;try{var s=localStorage.getItem(KEY);if(s){var x=JSON.parse(s);if(x&&x.first)first=x.first}localStorage.setItem(KEY,JSON.stringify({first:first,last:last}))}catch(e){}
function emit(name,meta){var payload=Object.assign({event_version:'1',page_path:location.pathname,source:last.source,medium:last.medium,campaign:last.campaign,content:last.content,asset:last.asset,cluster:last.cluster,referrer_class:last.referrer_class},meta||{});try{window.gtag('event',name,payload)}catch(e){}try{window.dispatchEvent(new CustomEvent('synapse:event',{detail:Object.assign({event:name},payload)}))}catch(e){}return Object.assign({event:name},payload)}
function hidden(form,name,value){var x=form.querySelector('input[name="'+name.replace(/"/g,'')+'"]');if(!x){x=document.createElement('input');x.type='hidden';x.name=name;form.appendChild(x)}x.value=clean(value,240)}
function enrich(form){hidden(form,'Attribution_Source',last.source);hidden(form,'Attribution_Medium',last.medium);hidden(form,'Attribution_Campaign',last.campaign);hidden(form,'Attribution_Content',last.content);hidden(form,'Attribution_Asset',last.asset);hidden(form,'Attribution_Cluster',last.cluster);hidden(form,'Attribution_Referrer',last.referrer_class);hidden(form,'Attribution_First_Touch',JSON.stringify(first));hidden(form,'Attribution_Last_Touch',JSON.stringify(last))}
function init(){document.querySelectorAll('form').forEach(function(f){enrich(f);f.addEventListener('submit',function(){enrich(f);emit('lead_form_submit',{form_action:clean(f.getAttribute('action')||'',160)})},{capture:true})});emit('asset_view');document.querySelectorAll('[data-synapse-event]').forEach(function(el){el.addEventListener('click',function(){emit(el.getAttribute('data-synapse-event'),{event_label:clean(el.getAttribute('data-synapse-label')||el.textContent,100)})})})}
window.SynapseMeasurement={emit:emit,enrichForm:enrich,attribution:function(){return{first:first,last:last}},referrerClass:refClass,collector:function(){return{provider:'ga4',measurement_id:GA_ID}}};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
