# AI Operasyonlarında Kanıt: Otomasyondan Önce Ölçüm

AI otomasyonu çoğu zaman yanlış soruyla başlıyor:

**“Hangi modeli kullanalım?”**

Daha iyi başlangıç sorusu şu:

**“Bu workflow'un işe yaradığını nasıl anlayacağız ve yanlış durumda ne olacak?”**

Bir demo için model seçimi önemli olabilir. Production için tek başına yeterli değildir.

Çünkü gerçek iş akışında model; kaynaklar, eksik girdiler, entegrasyonlar, yetkiler, insan onayı, dış aksiyonlar ve geri dönüşü zor kararlarla birlikte çalışır.

Bu yüzden kanıtı model skorundan değil, workflow davranışından başlatmak daha sağlıklı.

## 1. Önce baz çizgiyi ölçün

Bir süreci otomatikleştirmeden önce bugünkü durum görünür olmalı.

En az şu sorulara cevap verebilmelisiniz:

- Haftada kaç vaka geliyor?
- Bir vaka bugün kaç dakika sürüyor?
- En çok bekleme nerede oluşuyor?
- Hangi hata yeniden işleme yaratıyor?
- Hangi kararın sahibi kim?
- Hangi hata kritik kabul ediliyor?

Bu alanlar bilinmiyorsa “%30 daha hızlı” veya “ROI yaratır” gibi ifadeler ölçüm değil, varsayımdır.

İyi pilot önce mevcut durumu ölçer, sonra aynı metriklerle kontrollü yeni akışı karşılaştırır.

## 2. Ortalama doğruluk tek başına yeterli değildir

Bir workflow 100 vakanın 95'inde doğru çalışabilir.

Ama kalan 5 vaka nerede?

Eğer bu hatalar düşük etkili metin biçimlendirme sorunlarıysa tablo farklıdır.

Eğer bu hatalar yanlış ödeme, yetkisiz dış aksiyon, hukuki bağlayıcılık, sağlık kararı veya kritik kalite serbest bırakma gibi alanlarda toplanıyorsa aynı “%95” tamamen farklı bir risk anlamına gelir.

Bu yüzden hata sayısının yanında en az üç şey daha gerekir:

**Severity:** Hata ne kadar etkili?

**Detectability:** Hata production'a çıkmadan yakalanabiliyor mu?

**Owner:** Hata olduğunda kim durduruyor ve düzeltiyor?

Hata taksonomisi burada işe yarar. Input, context, reasoning, tool, format, policy ve human-process hatalarını aynı kutuya koymak yerine ayrı ayrı izlemek gerekir.

## 3. “İnsan döngüde” demek kontrol kurulduğu anlamına gelmez

Bir onay butonu tek başına human-in-the-loop değildir.

İyi bir insan onay yüzeyi en az şunları göstermelidir:

- hangi kaynak kullanıldı,
- sistem ne öneriyor,
- nerede belirsizlik var,
- hangi aksiyon gerçekleşecek,
- reddetme ve escalation yolu ne.

Eğer reviewer her vakayı tek tıkla onaylıyor, kaynak görünmüyor ve reddetme yolu kullanılmıyorsa insan kapısı kağıt üzerinde vardır ama gerçek bir kontrol olmayabilir.

## 4. Benchmark doğru soruyu sormalı

Bir benchmarkın amacı yalnızca bir yaklaşımı “kazanan” ilan etmek değildir.

Karar verici için daha faydalı soru şudur:

**Hangi iş sonucunda hangi trade-off oluşuyor?**

Synapse Automate'in public workflow benchmark v1 testinde aynı 100 sentetik vaka iki karar yaklaşımına verildi.

Yaklaşım A her durumda otomatik ilerleyen basit bir baseline'dı.

Yaklaşım B kaynak doğrulama, girdi kalitesi, risk, dış aksiyon ve insan onayı kapılarını kullandı.

V1 test setinde sonuç:

- Yaklaşım A: 36/100 policy uyumu
- Yaklaşım B: 100/100 policy uyumu
- Yaklaşım B: 64/64 insan veya güvenlik kapısını yakaladı
- Yaklaşım B: 15/15 adversarial vakayı bloke/escalate yoluna taşıdı

Bu sonuç bir LLM'nin production doğruluğunu kanıtlamaz.

Latency, maliyet ve insan edit süresi bu testte ölçülmedi.

Ayrıca sentetik test seti gerçek müşteri ROI'si, mevzuat uyumu veya production başarısı değildir.

Kanıtın değeri burada başka yerde: sistemin hangi durumda ilerlediği, hangi durumda durduğu ve hangi kararın insana geçtiği yeniden üretilebilir biçimde test edilebiliyor.

## 5. En iyi otomasyon bazen “henüz değil” der

Bir süreçte kaynak belirsizse, kritik hata tanımı yoksa veya karar sahibi belli değilse doğru hareket hemen entegrasyon kurmak olmayabilir.

Önce workflow'u küçültmek daha iyi olabilir.

Örneğin:

- bağlayıcı kararı otomatik vermek yerine taslak hazırlamak,
- dış aksiyonu otomatik yapmak yerine insan onayına bırakmak,
- tüm süreci değiştirmek yerine tek bir yüksek hacimli adımı test etmek,
- başarıyı tahmin etmek yerine baz çizgiyi ölçmek.

Bu yaklaşım daha az gösterişli görünebilir.

Ama production'da güven çoğu zaman daha fazla otonomiden değil, daha iyi sınırlandırılmış otonomiden gelir.

## Sonuç

AI otomasyonunda kanıt şu sırayla kurulmalı:

**Baz çizgi → test seti → hata sınıfları → insan gate → kontrollü pilot → production ölçümü.**

Model seçimi bu zincirin bir parçasıdır; zincirin tamamı değildir.

Asıl hedef “AI cevap verdi” demek değil.

**Doğru durumda ilerleyen, yanlış durumda duran ve kritik kararda kontrolü insana bırakan bir operasyon sistemi kurmaktır.**

Kendi sürecinizde bu kontrol noktalarını görmek için ücretsiz başlangıç:

https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html
