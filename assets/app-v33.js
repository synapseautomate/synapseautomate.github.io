
document.documentElement.classList.remove('no-js');
const menu=document.querySelector('.menu-button'),links=document.querySelector('.nav-links');
if(menu&&links){menu.addEventListener('click',()=>{const open=links.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));}
const progress=document.querySelector('.progress');
addEventListener('scroll',()=>{const d=document.documentElement;{const max=d.scrollHeight-d.clientHeight;progress.style.width=(max>0?d.scrollTop/max*100:0)+'%';}},{passive:true});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.08});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const form=document.querySelector('#contact-form');
if(form){form.addEventListener('submit',e=>{e.preventDefault();const fd=new FormData(form);const subject=encodeURIComponent('Synapse Automate — '+(fd.get('konu')||'AI otomasyon talebi'));const body=encodeURIComponent(
`Ad / Şirket: ${fd.get('ad')||''}
E-posta: ${fd.get('email')||''}
Telefon: ${fd.get('telefon')||''}
Konu: ${fd.get('konu')||''}

Mesaj:
${fd.get('mesaj')||''}`
);location.href=`mailto:synapseautomate.ai@gmail.com?subject=${subject}&body=${body}`;});}
const canvas=document.querySelector('#hero-canvas');
if(canvas && !matchMedia('(prefers-reduced-motion: reduce)').matches){
 const ctx=canvas.getContext('2d');let w,h,dpr,pts=[];
 const resize=()=>{dpr=Math.min(devicePixelRatio||1,2);w=canvas.clientWidth;h=canvas.clientHeight;canvas.width=w*dpr;canvas.height=h*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);pts=Array.from({length:34},()=>({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*.18,vy:(Math.random()-.5)*.18,r:Math.random()*1.8+1}));};resize();addEventListener('resize',resize);
 const draw=()=>{ctx.clearRect(0,0,w,h);for(const p of pts){p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;}
 for(let i=0;i<pts.length;i++){for(let j=i+1;j<pts.length;j++){const a=pts[i],b=pts[j],dx=a.x-b.x,dy=a.y-b.y,dist=Math.hypot(dx,dy);if(dist<150){ctx.strokeStyle=`rgba(67,227,208,${.13*(1-dist/150)})`;ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}}}
 for(const p of pts){ctx.fillStyle='rgba(0,180,216,.55)';ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();}requestAnimationFrame(draw)};draw();
}

/* D03_FREE_AI_TOOLS_NAV_GUARD */
(() => {
  const ensureFreeToolsLink = () => {
    document.querySelectorAll('.nav-links, .navlinks').forEach(nav => {
      let link = Array.from(nav.querySelectorAll('a')).find(a => /kaynaklar\.html(?:$|[?#])/.test(a.getAttribute('href') || ''));
      if (link) {
        link.textContent = 'Ücretsiz AI Araçları';
        link.classList.add('nav-free-tools');
        return;
      }
      link = document.createElement('a');
      link.href = '/kaynaklar.html';
      link.textContent = 'Ücretsiz AI Araçları';
      link.className = 'nav-free-tools';
      const sector = Array.from(nav.querySelectorAll('a')).find(a => /sektorler\.html/.test(a.getAttribute('href') || ''));
      if (sector && sector.nextSibling) nav.insertBefore(link, sector.nextSibling);
      else nav.appendChild(link);
    });
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ensureFreeToolsLink);
  else ensureFreeToolsLink();
})();
