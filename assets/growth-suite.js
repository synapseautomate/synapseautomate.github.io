
(function(){
 var f=document.getElementById('growth-brief');
 if(f)f.addEventListener('submit',function(e){
  e.preventDefault();
  var s=f.elements.hizmet.value,k=f.elements.sektor.value,h=f.elements.hedef.value;
  var q=new URLSearchParams({konu:s,mesaj:'Büyüme ve AI pazarlama talebi. Hizmet: '+s+'. Sektör: '+k+'. Öncelik: '+h+'. Kapsam ve fiyat hakkında görüşmek istiyorum.',utm_source:'growth_suite',utm_medium:'website'});
  location.assign('/iletisim.html?'+q);
 });
})();
