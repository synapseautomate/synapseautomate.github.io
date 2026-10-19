import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { chromium } from 'playwright';
const dir=process.env.SYNAPSE_MEDIA_DIR||'/tmp/synapse-social-v8-g10';
fs.mkdirSync(dir,{recursive:true});
const template=fs.readFileSync('operasyon/v8/gun-10/social/ig-template.html','utf8');
const logo='data:image/png;base64,'+fs.readFileSync('assets/brand/synapse-logo-clean.png').toString('base64');
const slides=[
 ['SATIŞ OPERASYONLARI / KARAR NOTU',['Her talep,','fırsat değildir.'],'Çok başvuru, tek başına uygun müşteri veya satış sonucu kanıtı değildir.','ÖNCE İHTİYACI ANLA','Gönüllü talep ≠ onaylı teklif','#86f1bd'],
 ['01 / İHTİYAÇ',['Sorun gerçekten','tanımlı mı?'],'İstenen yazılım değil; aksayan süreç, beklenen çıktı ve eksik bilgi anlaşılmalı.','İHTİYAÇ NETLİĞİ','Problem belli değilse teklif erkendir.','#5fdcf4'],
 ['02 / KAPSAM',['İhtiyaç,','kapsama','uygun mu?'],'Veri kaynağı, insan onayı ve uygulanabilir sınır baştan değerlendirilir.','KAPSAM KARARI','Belirsizse insan değerlendirmesi.','#90f4bd'],
 ['03 / YETKİ',['Kararı kim','verecek?'],'Görüşmek isteyen kişiyle fiyat, teklif ve satın alma yetkisi aynı şey değildir.','YETKİLİ MUHATAP','Ticari kararda insan onayı.','#6cceff'],
 ['04 / İLETİŞİM',['Sonraki adım','gönüllü mü?'],'İzinli talebe yanıt, otomatik pazarlama veya izinsiz takip yetkisi vermez.','İLETİŞİM SINIRI','Soğuk DM yok. İzinsiz teklif yok.','#85f0bf'],
 ['SYNAPSE / DEĞERLENDİRME',['Daha çok mesaj','değil.','Daha net karar.'],'İhtiyaç · Kapsam · Yetki · İzin. Dört karar sorusu, tek kontrollü başlangıç.','SÜREÇ ANALİZİ YAKLAŞIMI','synapseautomate.github.io','#84f1bd']
];
const story=['TALEP NİTELİĞİ / HIZLI KONTROL',['Talep geldi.','Peki hazır mı?'],'İhtiyaç net mi? Kapsam uygun mu? Kararı kim verir? İletişim gönüllü mü?','KARAR VERMEDEN ÖNCE','Süreç yaklaşımını keşfet: synapseautomate.github.io','#87f1bc'];
function escapeHTML(x){return String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','"':'&#39;'}[c]));}
function render(s,index,isStory){
 const heads=s[1].map((h,i)=>i===s[1].length-1?'<strong>'+escapeHTML(h)+'</strong>':escapeHTML(h)).join('<br>');
 let res=template;
 const pairs=[['__FORMAT__',isStory?'story':''],['__COLOR__',s[5]],['__TOP__',isStory?'INSTAGRAM STORY':'PERSPECTIVE'],['__LOGO__',logo],['__KICKER__',s[0]],['__HEAD__',heads],['__BODY__',s[2]],['__TAG__',s[3]],['__CHIP__',s[4]],['__PAGE__',isStory?'STORY':String(index+1).padStart(2,'0')+' / 06']];
 for(const [from,to] of pairs)res=res.replaceAll(from,to);
 return res;
}
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const output=[];
try{
 const all=[...slides.map((x,i)=>({d:x,i,story:false})),{d:story,i:0,story:true}];
 for(const x of all){
   const page=await browser.newPage({viewport:{width:1080,height:x.story?1920:1350},deviceScaleFactor:1});
   await page.setContent(render(x.d,x.i,x.story),{waitUntil:'load'});
   await page.locator('img').evaluate(el=>el.decode());
   const audit=await page.evaluate(()=>{
      const frame=document.querySelector('.frame').getBoundingClientRect();
      return [...document.querySelectorAll('.header,.content,.box,.footer')].filter(n=>{let r=n.getBoundingClientRect();return r.x<frame.x||r.right>frame.right||r.y<frame.y||r.bottom>frame.bottom}).map(n=>n.className);
   });
   if(audit.length)throw Error('Clipped '+JSON.stringify(audit));
   const filename=x.story?'SYNAPSE_INSTAGRAM_STORY_1080x1920.png':'SYNAPSE_INSTAGRAM_'+String(x.i+1).padStart(2,'0')+'_1080x1350.png';
   const location=path.join(dir,filename);
   await page.locator('.frame').screenshot({path:location,animations:'disabled'});
   const buffer=fs.readFileSync(location);
   const width=buffer.readUInt32BE(16),height=buffer.readUInt32BE(20);
   if(width!==1080||height!==(x.story?1920:1350))throw Error('Bad image size '+filename);
   output.push({name:filename,width,height,sha256:crypto.createHash('sha256').update(buffer).digest('hex'),clippedElements:0});
   await page.close();
 }
}finally{await browser.close()}
fs.writeFileSync(path.join(dir,'IG_STORY_QA.json'),JSON.stringify({result:'PASS',screens:output,officialLogo:'assets/brand/synapse-logo-clean.png',creativeSource:'conceptual original; not a working CRM dashboard'},null,2));
fs.writeFileSync(path.join(dir,'ALT_METINLER.txt'),slides.map((x,i)=>String(i+1)+'. '+x[1].join(' ')+' — '+x[2]+' SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL').join('\n')+'\nStory: Dört soruyla gönüllü talebin değerlendirilebilirliği; sentetik çerçeve.\n');
console.log(JSON.stringify({status:'PASS',count:output.length,files:output.map(x=>x.name)}));
