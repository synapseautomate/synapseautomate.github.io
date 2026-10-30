# SYNAPSE V8 — GÜN 20 / SIFIR BAĞLAMLI DEVİR
**Fiilî tarih:** 30.10.2026 Europe/Istanbul. **Plan tarihi:** 02.11.2026 — üç gün erken. Gün numarası DEĞİŞTİRİLMEDİ.
**Marka:** SYNAPSE Automate, Türkiye odaklı B2B otomasyon.
**Tek başarı amacı:** Gözlenmiş nitelikli talep varsa tek dönüşüm sürtünmesini azalt; gözlem yoksa bir açıklık hipotezini *test sonucu iddiası olmadan* hazırlamak.
**Konu:** Tahmine Dayalı Analitik — talep tahmini, belirsizlik ve veri ön koşulları.
**Tek karar sorusu:** “Talep tahminindeki görünen fiyat kesin mi? Verim yetersizse ne olur?”
**Tek rol:** E-ticaret talep planlama sorumlusu. Gerçek müşteri değil, karar verici hipotezi.

## Sürüm / PR / yetki
- Bugün başlangıç GitHub `main` SHA `05bd1f2a31d36fe92134e756e485a104337fbe9f` (28.10.2026 tarihli Gün19 video varlık yayını). 30.10.2026 anında açık PR sorgusu = boş; Gün20 hazırlığı başlamadan main tekrar kontrol edildi.
- Repo https://github.com/synapseautomate/synapseautomate.github.io
- Draft PR #52 https://github.com/synapseautomate/synapseautomate.github.io/pull/52
- Branch `draft/v8-gun-20-talep-tahmini-fiyat-belirsizlik-20261030`.
- **WEB-G20-20261030: ONAY BEKLİYOR.** Main merge, canlı site yayını, FormSubmit POST, ödeme, katalog, sosyal post, DM/e-posta ve hesabı değiştirme YAPILMADI.
- 0 TL peşin ve 0 dış gönderim; GitHub üzerinde sadece branch + draft PR + izole Chromium.
- Kullanıcının Gün19 yayını Gün20 için yetki sayılmaz.

## Önceki günlerin gerçeklik taraması
- Main'de `operasyon/v8/gun-11/SYNAPSE_V8_GUN_11_DEVIR.md` var. Main'de 01–10, 12–19 yolları bulunmadı; bu durum özel branch veya farklı arşivde olmayacakları anlamına gelmez. Gün19 eski taslak devir `draft/v8-gun-19-sesli-ai-talep-yolu-20261028` dalından okundu. Gün18 önceki arşiv dalı ve kullanıcı brifi ile biliniyor; tüm geçmiş günlerde satış ve trafik ölçümleri tahmin edilmedi.
- Önceki farklı hizmetler: Gün18 Süreç Madenciliği, Gün19 Sesli Yapay Zekâ ve Çağrı Merkezi; Gün20 talep tahmininde stokta bulunmama ve belirsizlik sorusunu farklılaştırır. Gerçek çalışan model kanıtı yok.

## Gerçek hizmet kaynağı
- [`hizmetler.html` ana dal](https://github.com/synapseautomate/synapseautomate.github.io/blob/05bd1f2a31d36fe92134e756e485a104337fbe9f/hizmetler.html), kart #12: “Tahmine Dayalı Analitik — Talep tahmini, müşteri kaybı analizi, fiyat karar desteği ve tedarik projeksiyonları.” Burada canlı uygulama / doğruluk / veri paylaşımı / API iddiası ispatlanmaz.
- Tek iş akışı TASLAK: zamanlı talep verisi, ürün-kimlik/birim, stokta bulunmama ve kampanya geçmişi → eksik veriyi ayır → basit baseline → ileriye doğru zaman validasyonu + belirsizlik aralığı → insan stok/tedarik onayı.
- İlgili yöntem araştırması: https://link.springer.com/article/10.1007/s10618-022-00894-5 ve https://www.sciencedirect.com/science/article/pii/S0169207023000961 .
- Kapsam dışı: otomatik stok/sipariş, canlı müşteri entegrasyonu, fiyat/performans/ROI garantisi, gerçek tahmin doğruluğu, müşteri/ses kaydı.

## Tek değişken: doğrudan diff
**Dosya:** `rehberler/ai-otomasyon-fiyatlari.html` (başka kamu dosyası değiştirilmedi).
**Önce:** fiyat/teslim FAQ dizisinde “Talep tahmini için görünen fiyat kesin mi?” sorusu YOK.
**Sonra:** tek `<details><summary>Talep tahmini için görünen fiyat kesin mi?</summary><p>Hayır ... TEST FİYATI ... veri ön koşulları ... belirsizlik ... insan onayı ...</p></details>` öğesi.
**Fiyat kaynakları:** `veri/offer-ladder.json` 4.900 TRY/149 USD süreç, 24.900 TRY/750 USD pilot, 14.900 TRY/449 USD aylık; sitede mevcut fiyat ifadeleri kesin teklif gibi algılanma P1'i taşıyabilir. Yeni FAQ bu riski açıklamaya yarar ama diğer sayfalardaki meta/şema ve kesin fiyat imasını bütünüyle kapatmaz. Diğer sayfalar değişmedi.
**Rollback:** eklenen tek FAQ HTML detay bloğunu geri al. Kod/meta/form/CTA/sitemap aynı kalır.

## İki bağımsız QA turu
**Tur A:** `QA_TUR_A_KAYNAK_TEKNIK.md`. Gerçek GitHub main kaynak karşılaştırması, fiyat/çıktı sınıfı, nitelikli talep paneli yokluk kaydı; bir varyant dışında CTA ve form değişmedi. Test kaynak veri/kapsam doğruluğu PASS, canlı tahmin motoru BİLİNMİYOR.
**Tur B:** `QA_TUR_B_GORSEL_ERISIM_HUKUK.md`.
Komut: `python scripts/v8_g20_faq_browser_qa.py`. [GitHub Actions run 41033820118](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820118) **SUCCESS**; [artifact 12967440538](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820118/artifacts/12967440538), 12 PNG (main önce, draft sonra; 320/375/390/768/1024/1440). **10 PASS, 2 BASELINE_P1, 0 YENİ REGRESYON HATASI**. 320px'te her iki sürüm scrollWidth 347px, viewport 320px, yani **27px mevcut yatay taşma P1**; teknik ve mobil kabulde bunu PASS sayma. Yeni FAQ mouse/Enter aç-kapa PASS; H1=1 ve eksik img alt=0; gözlenen JS exception=0.
[Site Integrity run 41033820097](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820097) SUCCESS. [Release Preflight run 41033820108](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/41033820108) SUCCESS.
**Canlı HTTP:** web araçları canlı SYNAPSE URL'lerine ulaşamadı; GitHub dosya kanıtı gerçek canlı 200 değildir, TEST_EDİLEMEDİ. Safari/iPhone/VoiceOver, Lighthouse saha verisi, GA4 consent network ve FormSubmit alıcı paneli TEST_EDİLEMEDİ.
**İki geçmiş kayıt:** ilk browser run FAIL: main/draft aynı 27px taşma; doğru baseline P1 sınıflaması ardından SUCCESS, tarihi hata saklanmıyor.

## Gün20 kreatif
- Yeni üretilen orijinal soyut 3D 'belirsizlikte ayrılan yollar' görseli; marka/ürün logosu taklit edilmedi. Son yerel PNG: `/mnt/data/gun20_talep_tahmini/talep_belirsizlik_1920x1080.png` SHA256 `ed705e8c04dcc81d1ae6213ec90f43c9920b6a6bfde6b915ab4e0b53aefc590c` ve `talep_belirsizlik_1080x1350.png` SHA256 `e9f1ef15256e24d2d9763830d5d483714b591d23a24dd1aeff2510020471e3bd`.
- İlk renderda arka plan birleşim çizgisi ve mobil metin/görsel çakışma riski bulundu, yeniden render edildi, son iki önizleme açıldı. Metin “TAHMİN, KESİN SİPARİŞ DEĞİLDİR.” 3 ön koşul, kamuya çıkacak etiket “SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL”.
- Nike “Rip the Script” (Haziran 2026) ve Pepsi “Football Nation” (Nisan 2026) yalnız fikir/ritim/kampanya bütünlüğü benchmark'ı. **Tüm paylaşımlar incelendi demiyoruz**. Resmî markanın logo dosyası render içinde yok; bu nedenle logolu final kreatif HOLD. Gün20 sosyal kotası 0, içerik YAYINLANMADI.
- Fotoğraf veya gerçek tahmin paneli/performans rakamı olarak kullanma. Yeni görsel dosyaları GitHub main'e aktarılmadı, yerel dosya olarak kullanıcıya sunulabilir.

## 16 iç teslim dosyası
- TEK_HIPOTEZ_FIYAT_BELIRSIZLIK.md; FIYAT_TESLIM_CTA_UYUM.md; SON_YEDI_GUN_GOZLEM_VE_ITIRAZ_TAKSONOMISI.md; QA_TUR_A_KAYNAK_TEKNIK.md; QA_TUR_B_GORSEL_ERISIM_HUKUK.md; BENCHMARK_VE_YENI_KREATIF_KARARLAR.md.
- linkedin-yontem-042.md, strateji-yontem-049.md, strateji-yontem-056.md, donusum-yontem-106.md, strateji-yontem-139.md, strateji-yontem-185.md, seo-yontem-186.md, strateji-yontem-201.md, strateji-yontem-215.md, strateji-yontem-216.md. Hepsinde uygunluk, kaynak, karar, maliyet, onay ve no-go var.

## Ölçümler / gerçek 0 ≠ bilinmiyor
| Kanal / Metrik | Değer | Kanıt |
|---|---|---|
| 30.10.2026 PR kaynak Chromium test | 10 PASS + 2 BASELINE_P1 / 12 | run 41033820118, yüksek |
| Yeni regresyon | 0 bulgu | karşılaştırmalı test yüksek, yalnız bu sayfa |
| 320px yatay taşma | 27 px (main ve draft) | Playwright, mevcut P1 |
| Son 7 gün gerçek fiyat tereddüdü, gerçek anket/talep | BİLİNMİYOR | yetkili CRM/FormSubmit/GA4 yok |
| CTA→gönüllü talep, gerçek form teslimi, nitelikli ziyaret | BİLİNMİYOR | GA4/FormSubmit yok |
| Fonlanmış sipariş / tahsil edilmiş satış / iade / net gelir | BİLİNMİYOR | yetkili platform/finans paneli yok |
| Dış paylaşım, gerçek DM, gönderi, hesap işlemi | 0 | bu oturumun işlem günlüğü |
| Peşin harcama | 0 TL | bu oturumun işlem günlüğü |
| Önce/sonra görsel QA | 12 PNG | gerçek Chromium / yüksek |
| iPhone/Safari/GA4 sahası | TEST_EDİLEMEDİ | erişim yok |

## Açık risk, sahip ve yayın kapısı
- **P0:** vergi/fatura/işletme/KYC ve gerçek ödeme kanıtı yok → checkout ve satış NO-GO. Sahip hesap sahibi + mali müşavir.
- **P1:** fiyat rehberi diğer fiyat bölümleri ve homepage/teklif meta kesin fiyat gibi anlaşılabilir → yalnız tek FAQ eklendi; kapsamlı gelecekteki ayrı onaylı revizyon gerekli. Sahip operatör + ticari onay hesap sahibi.
- **P1:** 320px 27px taşma eski main'de de var → açık, tek değişkeni bozmadan başka gün çöz. Sahip tasarım/UX.
- **P1:** resmî logo/lisans ve gerçek cihaz kreatif QA eksik → yeni görsel nihai sosyal teslim değil, HOLD. Sahip marka sahibi.
- **P2:** gerçek arama niyeti, Search Console, GA4 ve son 7 gün paneli BİLİNMİYOR. Sahip hesap sahibi.
- **ONAY BEKLİYOR:** `WEB-G20-20261030` yalnız FAQ ekli PR #52 main/yayın. `LI-G20-20261030` olası gelecekte LinkedIn ayrıca onay, bugün paylaşım yok. Diğer tüm dış sosyal platformlar: YAYINLANMADI / ayrı onay gerekir.
- **Teknik karar:** Site Integrity/Preflight ve FAQ regressions iyi, ancak 320 P1 ve kullanıcı site yayın onayı yok → HOLD. Ticari karar NO-GO.
- **Gün20 CLOSED DEĞİL**; kullanıcı onayı ve P1 kapanışı eksik.

## Ertesi günün TEK önceliği
320px fiyat rehberi mevcut taşmasını kök öğesi ile tam belirle, tek regresyon düzeltmesini ayrıca taslakla, gerçek Safari/cihaz test yolunu doğrula; yeni fiyat beyanlarını ve tüketici/fatura durumunu satışa hazır sanma. Gün20 PR #52 otomatik merge edilmez; açık `WEB-G20-20261030` izni yalnız spesifik kullanıcı eylemiyle alınır.
