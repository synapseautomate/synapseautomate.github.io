# AI Operasyonlarında Kanıt: Otomasyondan Önce Ölçüm

Bir AI otomasyonunun iyi görünmesi ile güvenilir çalışması aynı şey değildir.

Bir demo hızlı olabilir, metin düzgün olabilir, birkaç örnek başarılı görünebilir. Fakat üretim ortamında asıl soru şudur:

**Sistem doğru durumda ilerliyor, yanlış durumda durabiliyor mu?**

## Başlangıç noktası: modeli değil kararı ölçün

Bir workflow'u değerlendirirken yalnızca çıktı kalitesine bakmak yetersizdir. En az dört katman birlikte görünür olmalıdır:

1. **Kaynak:** Kullanılan bilgi doğrulanabilir mi?
2. **Girdi:** Kritik alanlar eksik veya çelişkili mi?
3. **Risk:** Kararın etkisi ne kadar yüksek?
4. **İnsan kontrolü:** İnceleme, onay, red veya üst seviyeye taşıma yolu var mı?

Bu katmanlardan biri belirsizse sistemin varsayılan davranışı ilerlemek değil, kontrollü biçimde durmak olmalıdır.

## 100 sentetik vakada iki yaklaşım

Synapse Automate'in açık güvenilirlik karşılaştırmasında aynı 100 sentetik vaka iki farklı karar yaklaşımıyla değerlendirildi.

- Basit yaklaşım her durumda otomatik ilerledi ve tanımlanan karar politikasıyla 36/100 vakada eşleşti.
- Kontrollü yaklaşım kaynak, girdi kalitesi, risk, dış aksiyon ve insan onayı kapılarını kullandı ve 100/100 vakada tanımlanan karar politikasıyla eşleşti.
- İnsan veya güvenlik kapısı gereken 64 vakanın 64'ü doğru kontrol yoluna yönlendirildi.
- Yanıltıcı veya kötü niyetli 15 senaryonun 15'i bloke edildi.

Bu sonuçlar gerçek kullanım doğruluğu, yatırım getirisi veya mevzuat uyumu garantisi değildir. Test seti sentetiktir ve beklenen davranış etiketleri önceden tanımlanmıştır.

## Başarısız örnekleri saklamayın

Güvenilirlik testi yalnızca sistemin ne kadar sık doğru çalıştığını değil, hangi durumda hata verdiğini de göstermelidir.

Örneğin:

- Kaynak yoksa cevap üretmek yerine kaynak istemeli veya incelemeye geçmeli.
- İki girdi çelişiyorsa sessizce birini seçmek yerine çelişkiyi görünür kılmalı.
- Dış aksiyon veya yüksek etkili karar varsa doğrudan işlem yapmak yerine insan onayı istemeli.

Başarısız örnek görünmüyorsa test setinin gerçekten zorlayıcı olup olmadığını anlamak da zorlaşır.

## İnsan onayı yalnızca bir buton değildir

İyi bir inceleme yüzeyi karar sahibine şunları göstermelidir:

- hangi kaynakların kullanıldığı,
- önerilen eylemin ne olduğu,
- hangi belirsizliğin kaldığı,
- neden insan kontrolü gerektiği,
- onaylama dışında düzenleme, reddetme ve üst seviyeye taşıma seçenekleri.

Bu bilgiler yoksa insan kontrolü operasyonel bir güvenlik mekanizması yerine formaliteye dönüşebilir.

## Ticari karar için daha iyi soru

"Hangi AI modeli daha iyi?" sorusu çoğu süreç için fazla genel kalır.

Daha yararlı soru şudur:

**Hangi workflow, hangi veri ve hangi risk sınırları içinde güvenli biçimde otomatikleştirilebilir?**

Bu sorunun cevabı model seçiminden önce sürecin kendisini anlamayı gerektirir.

Kendi sürecinizde aynı kontrol sorularını uygulamak için ücretsiz süreç haritasını kullanabilirsiniz:

https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html

Güvenilirlik karşılaştırması:

https://synapseautomate.github.io/kanit/workflow-guven-benchmark-v1.html

---

Synapse Automate — Kritik kararlar insan kontrolünde.