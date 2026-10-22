# SYNAPSE V8 Gün 13 — Sıfır bağlamlı tam devir / 22.10.2026
**Plan 26.10.2026**, fiilî 22.10.2026: **4 gün erken**; görev numarası **13** korunmuştur. Gün adı: **Katalog itirazları, teslim ve güven sözleşmesi**. PDF'nin güncel ek hizmet odağı: **Pazarlama ve İçerik Otomasyonu — içerik onayı/kampanya risk kapısı**; orijinal dar CSV katalog görevi de uygulandı.

## Repo / önceki iş / durum
- Repo https://github.com/synapseautomate/synapseautomate.github.io ; başlangıç main SHA **6481fd512a68a844e573a9b0d29d3a0f1e45d008** (22.10.2026).
- Yeni iç taslak dalı **draft/v8-gun-13-katalog-teslim-guven-20261022**; **main değişmedi**. **Draft PR #37:** https://github.com/synapseautomate/synapseautomate.github.io/pull/37 ; merge yetkisi verilmedi.
- V8 Gün01–08 devirleri ana daldan değil geçmiş ilgili PR dallarından erişildi; Gün09 main devir yolu NOT_FOUND, kayıt eksik; Gün10 PR #27'den, Gün11 main'den, Gün12 #35 dalından incelendi. Main üzerindeki #36 birleştirildi, #35 draft açık, #24 eski katalog draft açık.
- **Gün08 nihai karar:** kullanıcı Upwork hesabı açmamayı ve Upwork katalog kanalını sonlandırmayı seçmiş. Gün13 bu kararı değiştirmiyor. Katalog aktifliği ve gerçek Upwork inbound panel verisi **BİLİNMİYOR**; 0 gibi gösterme.

## Somut müşteri/satış etkisi
Alıcıya iki dosya, kolon/SKU, R01 eksik SKU, R02 mükerrer kimlik+SKU, R03 SKU/depo uyuşmazlığı, R04 negatif stok ve koşullu R05 stok yeterliliği; veri izinleri, tek rapor, revizyon/destek, süre ve kabul sınırlarını ayıran pasif satın alma SSS'si. R05 tarih/depo/rezervasyon tanımı yoksa **DEĞERLENDİRİLMEDİ**. Gerçek stok değiştirme, API/ERP, otomatik onarım, ROI/sıfır hata garantisi yok.

## Fiyat, kanal, hukuk
- Main veri/offer-ladder.json: Süreç Analizi 4.900 TRY / ayrı 149 USD, pilot 24.900 / 750, aylık 14.900 / 449. Site surec-analizi.html ve teklif/e-ticaret-surec-analizi.html fiyat metni var. Test hipotezleri: yerel ürün 990 TL, dar kurulum 4.900 TL, pilot 24.900 TL; gerçek Upwork panel USD, komisyon, kur, KDV, süre ve kabul bilinmiyor. **Ürün ile Süreç Analizi aynı rakamı taşısa da aynı ticari teslim değil.**
- Upwork alıcısı → yalnız Upwork Messages/sözleşme/teslim/ödeme; site/IBAN yönlendirme yok. Site gönüllü inbound → index/teklif/surec-analizi/iletisim → FormSubmit metadatası → kapsam ve veri/vergisel hukuk izni → yalnız hesap sahibi yasal tahsilat kararı. Gerçek form teslimi **TEST EDİLEMEDİ**.
- GitHub Pages ticari checkout/SaaS barındırma sınırı P0. Merchant of Record vergi muafiyeti değildir. GİB/20B, fatura, KVKK ve veri saklama silme hukuk kapıları açık; hiç bir doğrulanmış ödeme veya satış yok.

## Gerçek dosyalar / linkler
- Bu dal altında KATALOG_ALICI_SSS.md, ASGARI_VERI_TESLIM_KABUL_MATRISI.md, ONCE_SONRA_ILAN_KOPYASI.md, FIYAT_VE_KANAL_YETKI_MATRISI.md, IKI_KANAL_KARAR_YOLU.md, HUKUKI_GOZDEN_GECIRME_KAPISI.md, KATALOG_REVIZYON_ONAY_KARTI.md, QA_TUR_A_KAYNAK_TEKNIK.md, QA_TUR_B_MARKA_HUKUK_DONUSUM.md, GUN13_METRIK_VE_ONAY_KAYDI.md, SHORTS_YOUTUBE_CREATIVE_QA.md ve yöntem 050/051/055/074/091/108/140/142/222/239/250 taslakları var.
- Ayrı sohbet ZIP'de gerçekten oluşturulmuş statik HTML önizleme, 1200x900 4:3 iki sentetik galeri PNG + 320px thumbnail, sentetik JSON test, 2 bağımsız 1080x1920 12sn sessiz Shorts MP4 + SRT + kapak + QA manifest ve altı Chromium ekran görüntüsü yer alır. **Bu binary dosyalar PR'ye eklenmedi**; içerikteki repo linkleri binary varlığı sanılmamalı.

## QA A — kaynak/teknik
- python galeri_uret_ve_test.py → 4 sentetik bulgu R01–R04, R05 DEĞERLENDİRİLMEDİ, iki 1200x900 PNG PASS. Bu gerçek müşteriye ait değil, mevcut ürün motoruna ait güncel terminal kaydı değildir.
- python /mnt/data/qa_stage13.py → yalnız taslak HTML için Chromium 320,375,390,768,1024,1440 → 6/6 PASS: tek H1, tek CTA, yatay taşma yok, minimum 49.9px click/touch, klavye focus. Başta file:// net::ERR_BLOCKED_BY_ADMINISTRATOR; set_content ile düzeltildi. Canlı sayfa testi DEĞİL.
- ffprobe → iki MP4 1080×1920, 24 fps, 12.0sn, yuv420p; ilk renderda logo kırpılması tespit edilip yeniden renderlandı. Gerçek MP4 karelerinde logo artık tam. Ses izi kasıtlı yok; Türkçe SRT altyazı var.
## QA B — marka/hukuk/dönüşüm
- Galeri 4:3 ve 320px thumbnail mevcuttur fakat text-heavy küçük görünüm nedeniyle P1 AÇIK; Upwork'e yüklemeye hazır değil.
- Shorts gerçek YouTube platform, telefon safe zone, profesyonel ses miksajı, Safari, Lighthouse, canlı site HTTP/404, FormSubmit e-posta teslimi, Upwork/KYC/GA4: TEST EDİLEMEDİ.
- Kamu kreatifinde marka/ciro/gerçek müşteri/yanlış ürün ekranı veya iç yönetim notu iddiası yok; görsellerin ve videonun her karesinde sentetik etiket var. Kullanıcının verdiği gerçek RGBA SYNAPSE logosu orantılı kullanıldı.
- P0: yasal satıcı/fatura/vergi; KVKK/veri işleme/saklama/silme; Upwork panel/kanal kararı ve fiyat/komisyon; Pages ticari kullanım; canlı form işleyişi; ayrı yayın izinleri. P1: galeri çok metinli; gerçek canlı mobil/klavye/Safari/Lighthouse; Shorts gerçek platform ve ses QA. **Kamu yayınına/teslimli ücretli satışa hazır HAYIR.**

## Gerçek ölçümler
Bu oturumdaki yeni peşin harcama **0 TL**, bu oturumdaki dış yayın **0 eylem**. Gerçek katalog aktif mi, P0 canlı ilan kusuru, inbound soru, teklif→sipariş dönüşümü, gösterim, nitelikli ziyaret, demo görüntüleme, gönüllü talep, izinli teklif, platform fonlu sipariş, tahsil edilen satış, iade, net gelir ve fatura statüsü **BİLİNMİYOR**. 1 adet olası kavramsal fiyat çakışması; gerçek fiyat şikâyeti BİLİNMİYOR. Açık hukuk başlıkları en az 8.

## Resmî kaynak URL + kontrol tarihi 22.10.2026
- https://support.upwork.com/hc/en-us/articles/360057397533-How-to-create-a-project-in-Project-Catalog
- https://support.upwork.com/hc/en-us/articles/1500011309082-How-to-add-images-and-video-to-your-Project-Catalog-project
- https://support.upwork.com/hc/en-us/articles/4408644453395-How-we-review-your-Project-Catalog-project
- https://support.upwork.com/hc/en-us/articles/360052511833-Get-to-know-each-other-before-a-contract
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- https://support.google.com/youtube/answer/15424877

## Yetki durumu ve sonraki tek adım
Tüm izin ID'leri GUN13_METRIK_VE_ONAY_KAYDI.md içindedir; **ONAY BEKLİYOR**. Upwork revizyon, incelemeye gönderme/otomatik aktif risk, main/site, LinkedIn, iki YouTube Shorts, gerçek alıcı yanıtı ve tahsilat birbirinden ayrıdır. Metricool başka hesaplar olduğundan kullanılmadı. Hiçbir yayına gönderim, site merge, özel mesaj, satış, gerçek ödeme, KYC, komisyon veya Connects satın alma olmadı.
**Sonraki tek öncelik:** Gün08 Upwork kapatma kararını koruyarak site Süreç Analizi (4.900 TL kaynak kod liste fiyatı) ile dar CSV kurulum TEST 4.900 TL ayrımını ve satış/fatura kapısını müşteri karşısında açık hale getirecek yalnız taslak teknik/hukuk revizyonunu değerlendir. Bütün P0/P1 kapanmadan yayıma geçme.
**Son kanıt paketi güncellemesi (22.10.2026):** iki MP4 tekrar render edildi; 1080×1920, 24 fps, 12sn. Yerel ZIP'de PNG, Shorts, SRT, kaynak test kayıtları ve SHA256 manifest var. HEAD bu metni ekleyen commit SHA'dan sonra değişebilir; bundan sonraki operatör GitHub'dan main ve branch HEAD'i tekrar çekmelidir.
