# Gün 11 — Google panel denetimi, 20.10.2026

Kanıt kaynağı: Hesap sahibinin sohbet içinde sağladığı beş GSC görüntüsü; GA4 0 verisi yalnız hesap sahibinin beyanıdır. GSC/GA4 API hesabına erişim yoktur.

| Ölçü | Gerçek ekran/beyan | Durum ve sınır |
|---|---|---|
| Web arama tıklaması | 0; performans 3 ay | GSC ekran kanıtı, site ziyaretlerinin tamamı değildir |
| Görünen sorgular | site tarama, synapse automate, e-ticaret otomasyonu, site:.github.io | Bu dört sorgunun her birindeki tıklama 0; gösterimler henüz gösterilmedi |
| Toplam Google gösterimi | BİLİNMİYOR | GSC toplam gösterim kartı görünmüyor |
| Dizine eklenen sayfalar | 12 | GSC genel bakış, tüm repo HTML dosyaları sayısı değildir |
| Dizine eklenmeyen sayfalar | 3 | GSC genel bakış, nedenler ekranı yok |
| Yeni fatura URL'si | Google'da yok / Google tarafından bilinmiyor | Canlı URL testinde dizine eklenebilir |
| URL dizine eklenme isteği | Kabul edildi | Öncelikli sırada, indeks garantisi yok |
| sitemap.xml | 31 Ağustos 2026 gönderilmiş; türü Bilinmiyor | İşleme durumu/son okunma/keşfedilen URL bilgisi ekranda yok |
| sitemap-demand.xml | GSC'de gönderilip gönderilmediği BİLİNMİYOR | robots.txt kaynakta atıf içeriyor |
| GA4 göstergeleri | Tümü 0: kullanıcı beyanı | Gerçek zamanlı olay, dönem ve mülk ID test edilmedi |
| Gerçek ziyaret, uygun talep, gelir | BİLİNMİYOR | Arama tıklaması veya panel sıfırından çıkarılamaz |

Kaynak kodu (GitHub main) kontrolü: sitemap.xml ve sitemap-demand.xml URL dosyaları var, robots.txt her ikisini bildiriyor ve Google'a / erişimi veriyor. Yeni finans bilgi sayfasında self canonical/index-follow ve mevcut synapse-measurement-v1.js var. Ölçüm betiği yalnız açık analitik tercihi synapse_analytics_consent_v1=granted olduğunda G-HQSRRJ5HMZ için GA4 ağ yüklemesi yapıyor. Rıza verilmemiş ziyaretlerde sıfır GA4 olayı olağandır; hukukî uygunluk ilanı değildir.

Sonraki kullanıcı testi 1: Search Console > Site Haritaları > /sitemap.xml satırını açıp Durum, Son okunma, Keşfedilen URL ve özel hatayı gör. Türü Bilinmiyor olmak tek başına bozuk XML kanıtı değildir.
Sonraki kullanıcı testi 2: Search Console > Performans > 3 ay > Toplam gösterimler kartını seç; 0 tıklama ile gösterim ayrı raporlanacak.
Sonraki kullanıcı testi 3: GA4 > Yönetici > Veri akışları > G-HQSRRJ5HMZ doğrula; Raporlar > Gerçek zamanlı açıkken kendi sitede açık izin ver ve ayrı tarayıcıda sayfa/kontrol listesi aç. Gerçek zamanlı page_view ve finance_checklist_click olaylarını bekle. Kişisel kontrollü QA testini müşteri/lead olarak raporlama, rıza reddedilirse toplama YOK. Normal raporların işlenmesi 24-48 saat sürebilir.

Resmî kaynak: https://support.google.com/webmasters/answer/7451001 ; https://support.google.com/analytics/answer/9333790?hl=tr ; https://support.google.com/analytics/answer/11198161?hl=tr
Durum: G4 kısmi, G5 indeks talebi kabul edildi ancak indeks BİLİNMİYOR, G6 sitemap paneli kısmi, G7/G8 ham veri ve gerçek zaman testi hâlâ açık. S10 genel site_qa eski test borcu ayrıca açık. FULL CLOSED YOK.
