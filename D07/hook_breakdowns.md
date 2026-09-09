# AI Workflow Güven Karşılaştırması — 3 Hook Breakdown

## Hook 1 — “Yanlış durumda durabiliyor mu?”

**Açılış:**
AI otomasyonunda asıl soru “çalışıyor mu?” değil.
**Yanlış durumda durabiliyor mu?**

**Neden çalışır:**
Başarıyı yalnız hız ve çıktı kalitesiyle değil, kontrol davranışıyla çerçeveler. Karar vericiye güvenlik, yetki ve hata maliyeti açısından doğrudan bir iş sorusu sunar.

**Kanıt:**
100 sentetik vakalık karşılaştırmada kontrollü yaklaşım insan veya güvenlik kapısı gereken 64/64 vakayı doğru yola yönlendirdi.

**Sınır:**
Bu sonuç gerçek kullanım doğruluğu, yatırım getirisi veya mevzuat uyumu garantisi değildir.

---

## Hook 2 — “Daha çok otomasyon her zaman daha iyi değildir.”

**Açılış:**
Bir sistemin 100 işlemin 100'ünü otomatik yapması etkileyici görünebilir.
Ama 64'ünün insan kontrolüne gitmesi gerekiyorsa, bu başarı değildir.

**Neden çalışır:**
Otomasyon oranını tek başına başarı metriği olmaktan çıkarır ve doğru kontrol yoluna yönlendirme davranışını öne çıkarır.

**Kanıt:**
Basit yaklaşım 100 vakada da otomatik ilerledi; tanımlanan karar politikasıyla yalnız 36/100 vakada eşleşti. Kontrollü yaklaşım 100/100 eşleşme gösterdi.

**Sınır:**
Karşılaştırma sentetik ve deterministiktir; maliyet, gecikme süresi ve insan düzenleme süresi bu testte ölçülmedi.

---

## Hook 3 — “İnsan onayı bir buton değildir.”

**Açılış:**
Workflow'unuzda bir “Onayla” butonu olması, insan kontrolü olduğu anlamına gelmez.

**Neden çalışır:**
Karar vericinin görebildiği kaynak, belirsizlik, önerilen eylem ve reddetme/üst seviyeye taşıma seçeneklerini gerçek kontrol mekanizması olarak tanımlar.

**Kanıt:**
Kontrollü yaklaşım yüksek etkili veya dış aksiyon içeren vakaları insan onayına yönlendirir; kaynak eksikliği ve çelişkili girdileri inceleme yoluna taşır.

**Sınır:**
İnsan kontrolünün gerçek etkinliği üretim ortamında ayrıca ölçülmelidir; bu benchmark insan edit süresi veya onay davranış kalitesini ölçmez.