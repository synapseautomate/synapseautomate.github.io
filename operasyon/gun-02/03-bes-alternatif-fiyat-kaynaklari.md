# GÜN 02 | Gerçek alternatifler — fiyat, kapsam, kaynak, doğrulama tarihi
**Araştırma tarihi:** 2026-10-14 · **Sahip:** SYNAPSE Automate · **Kaynak tipi:** Her satır ilgili ürünün kendi resmî fiyat/ürün sayfası; kamuya açık liste fiyatıdır, satın alma, vergi/hesap uygunluğu veya fiilî kullanıcı talebi değildir.

## Altı doğrulanabilen alternatif (en az beş koşulu aşıldı)
| # | Gerçek ürün / sınıf | Resmî kaynakta görülen fiyat (para birimi / dönem) | Doğrulanan kapsam | SYNAPSE CSV aracından farkı / kritik not | Kaynak |
|---|---|---|---|---|---|
| A1 | **Dopigo Pazaryeri** / doğrudan operasyon alternatifi | **24.999 TL / yıl** (Pazaryeri paketi) | Pazaryeri, e-ticaret site, e-fatura ve kargo entegrasyonları; limitsiz ürün/sipariş başlıkları. | Canlı entegrasyon ve sipariş yönetimi sunar; indirilebilir yerel CSV kontrolüyle aynı hizmet değildir. | https://www.dopigo.com/fiyatlar/ |
| A2 | **StockMount Sipariş ve Ürün Paketi** / doğrudan operasyon alternatifi | **25.000 TL / yıl** (*o tarihte sitedeki kampanya; 1 Ocak koşullu, yeniden kontrol gerekir*) | Sipariş yönetimi + stok senkronizasyonu + ürün listeleme; 14 gün deneme; şirket/kanal koşulları ayrıca. | Bağlantılı stok senkronizasyonu sağlar; SYNAPSE bu yetkiyi **sunmaz**. Siteye göre KDV dahil; ek mağaza/alt kullanıcı ücreti olabilir. | https://www.stockmount.com/tr-tr/fiyatlar/ |
| A3 | **Google Workspace Starter + Sheets** / genel amaçlı tablo ikamesi | **71,20 TL / kullanıcı / ay** yıllık taahhüt görünümü; ayrıca **85,40 TL / kullanıcı / ay** alternatif fiyat sayfada gösteriliyor (faturalama seçimine göre teyit gerek) | Sheets/Drive üzerinde müşteri kendi eşleştirme formüllerini yazabilir; abonelik paketinin doğrudan CSV denetim kural seti içerdiği iddia edilmez. | Daha ucuz/ücretsiz hesap seçeneği olabilir; özelleştirme sorumluluğu müşteride. Veriler buluta gidebilir. | https://workspace.google.com/intl/tr/business/ |
| A4 | **Microsoft 365 İş Temel + Excel web/mobil** / genel amaçlı tablo ikamesi | **7 USD / kullanıcı / ay**, yıllık ödeme planı; **vergiler hariç** | Excel web/mobil, OneDrive ve diğer Microsoft 365 iş uygulamaları. | Hazır sipariş/stok kural paketi değildir; Excel formülleri için kullanıcı işi gerekir. USD fiyat TL ürünle kur çevrimi yapılmadan kıyaslanamaz. | https://www.microsoft.com/tr-tr/microsoft-365/business/compare-all-microsoft-365-business-products-b?v=1.0.26 |
| A5 | **Airtable Free / Team** / esnek veri tabanı ikamesi | **Free 0 USD**; **Team 20 USD / düzenleme yetkili kullanıcı / ay** yıllık ödemede | Hafif veri tabloları, otomasyon/veri tabanı yapıları; Free plan limitli (resmî destek sayfasına göre 1.000 kayıt/tablo). | Müşterinin kendi uygulama/kurallarını oluşturmasını gerektirir; doğrudan yerel CSV hata raporu ürünü değildir. | https://airtable.com/pricing ; https://support.airtable.com/articles/2277136852-airtable-plans-overview |
| A6 | **Coupler.io Free / Starter** / rapor/veri çekme ikamesi | **Free 0 USD** (manuel güncelleme); **Starter 32 USD / ay** aylık ödeme veya **24 USD / ay** yıllık faturalama | Çok sayıda uygulama veri kaynağını tablo/BI çıktısına bağlama, ücretli planlarda zamanlanmış yenileme. | Alternatif haftalık rapor otomasyonu hipotezine daha yakın; varsayılan araç veriyi dış servislere taşır. | https://www.coupler.io/pricing |

**Fiyat standardı:** Fiyatlar yerel resmî sitede 14.10.2026 tarihinde görüldüğü şekliyle kaydedildi. İndirim ve vergi/taahhütler firma/plan bazında farklıdır; **kullanıcının gerçekten ödediği fiyat veya piyasanın kabul edeceği SYNAPSE fiyatı değildir**. USD/TL tutarları aynı sütunda olsa bile para birimine ve döneme göre dönüştürülmeden ekonomik üstünlük hükmü kurulmaz.

**Karar gerekçesi:** A1/A2 kapsamlı ve devam eden entegrasyon çözümü; A3/A4/A5 müşterinin kendi kuracağı tablo; A6 veri yenileme/rapor aracı. **SYNAPSE'ın savunulabilir boşluğu yalnız sınırlı, yerel, denetlenebilir, tek seferlik CSV istisna taraması hipotezidir.** Rakip karşılaştırması bunu doğrulamaz; gerçek alıcı ve ödeme kanıtı yoktur.

## Kaynak kontrol kaydı
| Kayıt | Kaynak sahibi | Doğrulama tarihi | Erişim yöntemi | Güven |
|---|---|---|---|---|
| E1 | Dopigo | 2026-10-14 | resmî fiyat sayfası | Görünür liste fiyatı |
| E2 | StockMount | 2026-10-14 | resmî fiyat sayfası | Kampanyalı görünür liste fiyatı |
| E3 | Google | 2026-10-14 | resmî Workspace fiyat sayfası | İki gösterim; ödeme planı net değil |
| E4 | Microsoft | 2026-10-14 | resmî İş Temel fiyat sayfası | USD, vergiler hariç, yıllık taahhüt |
| E5 | Airtable | 2026-10-14 | resmî fiyat ve destek sayfası | ABD doları, kullanıcı başı |
| E6 | Coupler.io | 2026-10-14 | resmî fiyat sayfası | Aylık ve yıllık ayrı |
