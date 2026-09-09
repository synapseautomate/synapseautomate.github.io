# AI Workflow Güven Teardown — Transcript

Bir AI workflow'unu değerlendirirken ilk soru “model ne kadar iyi cevap veriyor?” olmamalı.

İlk soru şu olmalı:

**Bu sistem hangi durumda ilerlemeli, hangi durumda durmalı ve hangi kararda kontrolü insana bırakmalı?**

Bu teardown sentetik ve hassas olmayan bir örnek üzerinden dört katmanı inceler: girdi, karar politikası, insan kontrolü ve çıktı izi.

## 1. Girdi

Örnek bir teklif talebi düşünün. Formdan gelen bilgiler ile ek dokümanda yazan bilgiler aynı süreci tarif ediyor.

İlk kontrol, modelin cevap üretip üretemediği değildir. Önce şu sorular sorulur:

- Kaynak doğrulanmış mı?
- Kritik alan eksik mi?
- Girdiler birbiriyle çelişiyor mu?
- Gereksiz hassas veri var mı?

Kaynak doğrulanamıyorsa sistem kesinlik üretmemeli. Eksik veya çelişkili bilgi varsa otomatik karar yerine inceleme yolu açılmalı.

## 2. Karar politikası

Aynı girdi, risk ve eylem tipine göre farklı davranış gerektirebilir.

Düşük riskli, doğrulanmış ve yeterli girdiye sahip bir süreç otomatik ilerleyebilir.

Eksik, çelişkili veya orta riskli durum insan incelemesine gidebilir.

Yüksek etkili karar veya dış aksiyon içeren süreç ise insan onayı gerektirebilir.

Buradaki amaç otomasyon oranını mümkün olduğunca yükseltmek değil. Yanlış durumda otomatik ilerleme ihtimalini azaltmaktır.

## 3. İnsan kontrolü

İnsan onayı yalnızca bir “Onayla” butonu olmamalıdır.

Karar sahibi en az şu bilgileri görmelidir:

- kullanılan kaynak,
- önerilen eylem,
- kalan belirsizlik,
- risk seviyesi,
- düzenleme, reddetme ve üst seviyeye taşıma seçenekleri.

Bu bağlam görünmüyorsa insan kontrolü gerçek bir güvenlik mekanizması olmaktan çıkabilir.

## 4. Hata modları

Üç basit örnek:

**Kaynak yok:** Sistem cevap üretmek yerine kaynak istemeli veya incelemeye geçmeli.

**Girdiler çelişkili:** Sistem sessizce bir değeri seçmek yerine çelişkiyi görünür yapmalı ve kararı bekletmeli.

**Yüksek etkili karar:** Finans, sağlık, hukuk veya bağlayıcı dış aksiyonlarda insan son sözü söylemeli.

## 5. Çıktı ve karar izi

Güvenilir bir workflow yalnızca sonuç üretmez. Kararın izini de bırakır:

- ne üretildi,
- hangi kaynak kullanıldı,
- neden bu yol seçildi,
- kim onayladı,
- ne zaman üretildi.

Bu kayıt, hata analizi ve operasyonel denetim için gereklidir.

## 6. Açık test

Synapse Automate güvenilirlik karşılaştırması 100 sentetik vakada iki karar yaklaşımını aynı beklenen etiketlerle değerlendirir.

Kontrollü yaklaşım, tanımlanan karar politikasıyla 100/100 vakada eşleşti; insan veya güvenlik kapısı gereken 64/64 vakayı doğru kontrol yoluna yönlendirdi ve 15/15 yanıltıcı veya kötü niyetli senaryoyu bloke etti.

Bu test gerçek kullanım doğruluğu, yatırım getirisi veya mevzuat uyumu garantisi değildir. Maliyet, gecikme süresi ve insan düzenleme süresi bu testte ölçülmemiştir.

## Canonical kaynaklar

Güvenilirlik karşılaştırması:
https://synapseautomate.github.io/kanit/workflow-guven-benchmark-v1.html

Ücretsiz süreç haritası:
https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html

Süreç Analizi:
https://synapseautomate.github.io/surec-analizi.html