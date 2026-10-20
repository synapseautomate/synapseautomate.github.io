# Gün 11 — Yöntem 172: Gerçek örnekten niyet haritası

**Tarih:** 20.10.2026 (PDF planı 24.10.2026; 4 gün erken, gün numarası 11). **Durum:** İÇ TASLAK. **Hizmet:** Muhasebe ve Finans Otomasyonu; fatura ön işleme, insan onaylı mutabakat. **Uygulama kaynağı:** Yeni hedef sayfanın sentetik karşılaştırması.

## Alıcıya tek soru
Finans yetkilisi 500 TL fark görünce hangi işlemi arar?

## Tek karar / gerçeklik sınırı
Örnek: sentetik faturada 12.500, taslak kayıtta 12.500, varsayılan tek ödeme satırında 12.000. Tutar farkı otomatik eksik ödeme kararı değildir.

## Artefakt ve kanıt türü
Alıcı türü finans operasyon sorumlusu; kaynak kısıtları ve tahsilat kısmi olabilir; 'bilinmiyor' güvenli çıkıştır.

**Hedef alıcı:** KOBİ finans operasyonları yöneticisi / yetkili muhasebe sorumlusu. **Ön koşullar:** yasal ve izinli veri kaynağı, eşleştirme anahtarı, para birimi/dönem, yetki ve insan onay rolü. **Örnek iş akışı:** sentetik fatura satırı → referans/tutar kontrolü → fark kaydı → HUMAN_REVIEW → kurumun yetkilisi. **Kapsam dışı:** gerçek defter işleme, e-fatura düzenleme, banka/API entegrasyonu, ödeme/mahsup, vergi/kredi/ticari sonuç garantisi.

**SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL:** Fatura 12.500 TL ve tek ilişkili ödeme satırı varsayımı 12.000 TL → 500 TL matematiksel fark; neden/sonuç BİLİNMİYOR, insan inceler. Çalışan finans mutabakat ürünü veya demo kanıtı yok. Mevcut 8 soruluk finans web aracı ayrı öz değerlendirmedir.

## Mevcut → Taslak kontrolü
| Yüzey | Mevcut | Taslak | Kanıt / durum |
|---|---|---|---|
| Ana sayfa | Genel insan denetimli otomasyon; finans sektörü kartı | Aynı; finans sektör sayfasına mevcut link korundu | KAYNAK_PASS |
| Hizmetler | Muhasebe-finans: fatura ön işleme ve mutabakat desteği, alt link yok | Özgün özel sayfaya tek açıklayıcı bağlantı | KOD_TASLAK |
| Finans sektörü | Kaynak/kural/onay genel yaklaşım | Örnekli fatura karşılaştırma sayfasına bağlamsal link | KOD_TASLAK |
| Yeni özel sayfa | Yok | Benzersiz title + H1 + self canonical; bir örnek soru | TASLAK |
| Sitemap + robots | İki XML / robots izin veriyor | Hedef URL yalnız bir sitemap'e ekli; main değiştirilmez | TASLAK |
| GSC / HTTP | Panel veya yeni URL canlı kanıtı yok | BİLİNMİYOR / LIVE_TEST_EDİLEMEDİ | GSC_YOK |

## Somut uygulama ve sonraki adım
Sorgu–semptom–kanıt–yetkili incelemesi; para transferi gerçekleştirme yok

## QA A — kaynak / SEO / veri
- Ana kaynaklar: https://github.com/synapseautomate/synapseautomate.github.io/blob/cfbcd0c4bb9c084771b9562291b52a95a2c2c339/hizmetler.html ; https://github.com/synapseautomate/synapseautomate.github.io/blob/cfbcd0c4bb9c084771b9562291b52a95a2c2c339/sektorler/finans-bankacilik.html ; https://github.com/synapseautomate/synapseautomate.github.io/blob/cfbcd0c4bb9c084771b9562291b52a95a2c2c339/araclar/finans-surec-kontrol-listesi.html.
- Resmî SEO: https://developers.google.com/search/docs/appearance/ai-features?hl=tr; https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls; https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=tr (20.10.2026 kontrol).
- Kaynak, gerçek müşteri ve çalışan ERP kanıtı yoksa iddia üretmeme: **PASS (metin taslak doğruluğu)**.
- Teknik HTTP, son GSC indeks ve organik tıklama: **TEST_EDİLEMEDİ / BİLİNMİYOR**; yerel/bulut CI ayrıca kanıtlanacak.

## QA B — UX / erişilebilirlik / hukuk / dönüşüm
- Yeni sayfa kırpma, klavye, 320/375/390/768/1024/1440 gerçek Chromium ekranı: CI sonucu ayrı `QA_TUR_B` belgesine taşınacak; şimdilik **TEST_EDİLEMEDİ**.
- Fiyat/checkout/yerel tescil/gerçek müşteri veya ödeme garantisi: **YOK**. Gerekli hukuk/KVKK/izin kanıtları: **BİLİNMİYOR, P0 açık**.
- Kullanıcı yalnız ayrı URL/sitemap/site yayın onayı verirse main'e merge; otomatik yayın **YOK**.

## Geri alma
Draft PR kapanırsa main değişmez. İleride yayımlanırsa yalnız bu sayfa, iki bağlamsal iç bağlantı ve sitemap kaydı ters commit ile geri alınır; mevcut finans kılavuzları korunur.
