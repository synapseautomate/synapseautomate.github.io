# Gün 11 — Yöntem 003: Hedef kitle araştırması

**Tarih:** 20.10.2026 (PDF planı 24.10.2026; 4 gün erken, gün numarası 11). **Durum:** İÇ TASLAK. **Hizmet:** Muhasebe ve Finans Otomasyonu; fatura ön işleme, insan onaylı mutabakat. **Uygulama kaynağı:** Kamuya açık site soru/cevapları; sektör sayfası.

## Alıcıya tek soru
Muhasebe sorumlusu gerçekte hangi ifadeyle mutabakat öncesi farkı arar?

## Tek karar / gerçeklik sınırı
Gerçek müşteri mesajları/DM kaydı yok; forum ve otomatik tamamlama hacmini doğrulanmış veri sayma. Aday alıcı sorgusu olarak 'fatura ön işleme mutabakat kontrolü' etiketlenir.

## Artefakt ve kanıt türü
Soru–niyet–itiraz–yanıt tablosu; fatura/kayıt eşleşmeme, eksik referans ve insan inceleme ayrı tutulur.

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
İlk görüşmede isteğe bağlı anonim soru kategorisi toplama taslağı; kişisel veri yok

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

## 20.10.2026 — Ek açık web SERP araştırması
- İlk 5 kaynak + resmî Google SEO belgeleri: [SERP_ACIK_KAYNAK_2026-10-20.md](SERP_ACIK_KAYNAK_2026-10-20.md). Gerçek GSC/lead/arama hacmi/ilk sayfa sırası sonucu yerine geçmez.
- Klasik 'e-Fatura Mutabakatı' ile cari/banka mutabakatı daha geniş başlıklardır; yeni sayfanın tek farkı 500 TL sentetik kararda kanıt ve insan inceleme ön koşulunu açıklamasıdır.
