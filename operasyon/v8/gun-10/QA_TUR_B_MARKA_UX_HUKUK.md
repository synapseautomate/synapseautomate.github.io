# QA B — bağımsız marka, erişilebilirlik, hukuk, yayın ve dönüşüm — 19.10.2026
## Görsel ve erişilebilirlik
- Public yeni sayfa tek H1, canonical, Türkçe başlık, SYNAPSE logosu, mobil nav, klavye focus-visible, minimum CTA hedefi kod/tarayıcı kanıtıyla PASS.
- CI gerçek Chromium 320/375/390/768/1024/1440 staged renderi, yatay taşma/kırık yerel görsel/CTA alanı negatif kontrolü PASS.
- SVG/PDF sosyal karusel kullanıcı tarafından LinkedIn'de yayımlandı beyanı var; gerçek permalink yok; yeniden gönderilmez.
- Safari cihaz, VoiceOver/ekran okuyucu ve canlı üretim 6 breakpoint **TEST_EDİLEMEDİ**.
- Düşük kontrast veya görsel kırpılma için tüm üretim tarayıcılarında sıfır hata garanti edilemez, nihai canlı cihaz QA bekliyor.
## Marka/doğruluk
- CRM devir sayfası mevcut genel müşteri talebi analiz sayfasından ayrı özgün konu; 'çalışan CRM ürünü', 'gerçek müşteri', 'ROI', 'satış yaptık' iddiası yok.
- Sentetik iş akışında 'SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL' etiketi korunmuştur. Anasayfa yeni kartı 'Gün10/PR/QA' iç notu içermez.
- Logo mevcut repo varlığı; üçüncü taraf rakip tasarımı kopyalanmadı.
## Hukuk / güvenlik / platform
- Consent teknik staged testi PASS; [KVKK çerez rehberi](https://www.kvkk.gov.tr/Icerik/7353/Cerez-Uygulamalari-Hakkinda-Rehber) nedeniyle hukuk uzmanı doğrulaması P0 AÇIK.
- Üçüncü taraf FormSubmit aktarım politikası/inbox gerçek teslimi TEST_EDİLEMEDİ; üretimde gerçek insan verisiyle form denemesi YOK.
- GitHub Pages [resmî sınırlamaları](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) nedeniyle ticari yayım barındırma P0, uygun alternatif/hesap sahibi kararı bekliyor.
- Şirket/fatura/ödeme uygunluğu ve gerçek tahsilat kanıtı yok; satış açma P0 AÇIK.
## Yayın statüsü
- Kullanıcı siteyi güncellemeye açık yetki verdi, ancak P0 açıkken main merge yapılmadı. Bu kontrol siteyi **YAYINA HAZIR** ilan etmez.
- LinkedIn: kullanıcı tarafından yayınlandığı bildirildi, gerçek URL/panel BİLİNMİYOR.
- Instagram, YouTube ve başka platformlar: gerçek hesap/kreatif/video kanıtı olmadan YAYINLANMADI.
- Sonuç: Staged frontend teknik QA GEÇTİ; hukuki/ticari üretim QA BEKLEMEDE; kayıtlar gün devrine aktarıldı.
