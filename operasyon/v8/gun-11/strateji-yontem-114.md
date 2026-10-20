# Gün 11 — Yöntem 114: Query fan-out

**Tarih:** 20.10.2026 (PDF planı 24.10.2026; 4 gün erken, gün numarası 11). **Durum:** İÇ TASLAK. **Hizmet:** Muhasebe ve Finans Otomasyonu; fatura ön işleme, insan onaylı mutabakat. **Uygulama kaynağı:** Google Search Central AI features; finans rehberleri.

## Alıcıya tek soru
Bir sorunun bütün alt yanıtları için yeni sayfalar gerekir mi?

## Tek karar / gerçeklik sınırı
Hayır. Başlıca alt sorular tek hedef sayfada: fatura/ödeme farkı, ön koşul, yetkili onay, belirsizlik, örnek, kapsam dışı, sık sorulanlar.

## Artefakt ve kanıt türü
Mevcut finans satın alma rehberiyle yeni soru sayfası ayrıdır; 'mutabakat' kelimesinin her varyantı için yeni sayfa yok.

**Hedef alıcı:** KOBİ finans operasyonları yöneticisi / yetkili muhasebe sorumlusu. **Ön koşullar:** yasal ve izinli veri kaynağı, eşleştirme anahtarı, para birimi/dönem, yetki ve insan onay rolü. **Örnek iş akışı:** sentetik fatura satırı → referans/tutar kontrolü → fark kaydı → HUMAN_REVIEW → kurumun yetkilisi. **Kapsam dışı:** gerçek defter işleme, e-fatura düzenleme, banka/API entegrasyonu, ödeme/mahsup, vergi/kredi/ticari sonuç garantisi.

**SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL:** Fatura 12.500 TL ve tek ilişkili ödeme satırı varsayımı 12.000 TL → 500 TL matematiksel fark; neden/sonuç BİLİNMİYOR, insan inceler. Çalışan finans mutabakat ürünü veya demo kanıtı yok. Mevcut 8 soruluk finans web aracı ayrı öz değerlendirmedir.

## Yönteme özgü karar tablosu
| Seçenek | Karar | Sorumlu | Tarih | Durum |
|---|---|---|---|---|
| Aynı CSV sipariş-stok içerik tekrarı | UYGULAMA | Operatör: RED | 2026-10-20 | PASS (tekrarlanmadı) |
| Fatura ön işleme / insan inceleme | TASLAK | Operatör | 2026-10-20 | PASS (kaynak kapsamı) |
| Gerçek müşteri dili / GSC sonuç iddiası | YASAK | Hesap sahibi / GSC | 2026-10-20 | BİLİNMİYOR |
| Yeni site yayın / sitemap | ONAY BEKLİYOR | Hesap sahibi | 2026-10-20 | YAPILMADI |

## Somut uygulama ve sonraki adım
Alt sorgu bazında gerçek GSC verisi olmadığında ayrı sayfa açmama kararı

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
