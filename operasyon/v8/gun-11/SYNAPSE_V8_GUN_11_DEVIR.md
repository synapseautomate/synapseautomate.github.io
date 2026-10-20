# SYNAPSE V8 / GÜN 11 — SIFIR BAĞLAMLI OPERATÖR DEVİR KAYDI

## Kimlik / tarih / repo
- **Görev:** Gün 11 / 30. **Plan:** 24.10.2026; **fiilî yürütme:** 20.10.2026 (4 gün erken). Gün numarası değiştirilmez.
- Marka: SYNAPSE Automate. Resmî site https://synapseautomate.github.io/ ; repo https://github.com/synapseautomate/synapseautomate.github.io ; `main` baz SHA `cfbcd0c4bb9c084771b9562291b52a95a2c2c339`.
- **Bu güne ait ayrı yayınsız dal:** `draft/v8-gun-11-finans-fatura-mutabakat-seo-20261020`; **DRAFT PR #32** https://github.com/synapseautomate/synapseautomate.github.io/pull/32 ; `main` merge YOK. İleride kullanıcıdan net yayın onayı olmadan birleştirme YOK.
- Önceki devirler: Gün 01–08 GitHub PR dallarında okundu; Gün 09 beklenen `SYNAPSE_V8_GUN_09_DEVIR.md` erişiminde **NOT_FOUND**; Gün 10 PR #27 dalında okundu. Gün 10 sosyal içerikleri hesap sahibi tarafından CLOSED, tekrar yok. Gün 08 devir: Upwork hesap/Project Catalog kapsam dışına alındı; yeni Upwork eylemi başlatma.

## Satış/müşteri kararı ve kapsam
- Günün tek amacı: tek arama sorgusuna bağlı, yeni ama mevcut finans sektör/rehber niyetiyle çakışmayan, doğrulanabilir **bilgi sayfası** hazırlamak.
- Hizmet: muhasebe ve finans otomasyonu; yalnız **fatura ön işleme ve insan onaylı mutabakat hazırlığı**. Hedef alıcı: KOBİ muhasebe/finans operasyonları yöneticisi.
- **Tek karar sorusu:** `Faturadaki tutar ile ilişkili ödeme kaydı uyuşmadığında, hangi kanıt kontrol edilip kim onay vermeli?`
- Örnek: SENTETİK fatura 12.500 TRY, taslak kayıt 12.500 TRY, varsayımsal tek ödeme 12.000 TRY; aritmetik fark 500 TRY, neden BİLİNMİYOR, güvenli çıkış HUMAN_REVIEW. `fatura-mutabakat-SENTETIK-ornek.csv` ve özel Python testi.
- Webde gerçekten bulunan referans: https://synapseautomate.github.io/araclar/finans-surec-kontrol-listesi.html (8 maddelik web kontrol listesi). Bu araç gerçek fatura dosyası almaz, bankaya veya ERP'ye bağlanmaz; canlı muhasebe uygulaması değildir.
- Ticari fiyat, satın alma/checkout, e-fatura düzenleme, ödeme/mahsup, finansal/vergi tavsiyesi, sonuç/ROI iddiası YOK. Katalog, sosyal post, canlı API entegrasyonu YOK.
- İşleme ön koşulu: yetkili veri kaynağı, referans ve dönem, kurallı karşılaştırma, para birimi, veri erişim izni ve onay rolü. İnsan onayı ödeme/kayıt düzeltmede kritik.

## Kaynaklar, varlık sayıları ve çakışma kararı
- main GitHub tree 20.10.2026: **146 HTML, 392 blob dosyası**; kullanıcı promptunun eski 144 HTML/389 dosya sayısını güncel kabul etme. PR staging kaynak envanteri **147 HTML** (bir yeni sayfa).
- Ana resmî içerik: `hizmetler.html` fatura ön işleme, gider sınıflandırma, mutabakat desteği, raporlama; `sektorler/finans-bankacilik.html` kaynak-kural-insan onayı; `rehberler/finans-ai-otomasyonu-guvenli-baslangic.html` finans kontrol sınırları; `rehberler/finans-ai-otomasyon-satin-alma-rehberi.html` genel satın alma; `araclar/finans-surec-kontrol-listesi.html` gerçekten çalışan sekiz checkbox.
- Sırf 'finans otomasyonu' kelimesini çoğaltma: yeni sayfa /cozumler/fatura-on-isleme-mutabakat-kontrolu.html yalnız *fatura ve mutabakat farkı* kararını yanıtlar.
- Draft iç kullanıcı yolu: `index.html` mevcut finans sektör kartı → `sektorler/finans-bankacilik.html` özel sayfa linki → yeni sayfa → çalışan finans kontrol aracı. Ayrıca `hizmetler.html` finans kartına bir açıklayıcı link.
- Yalnız hedef URL'nin `sitemap.xml` kaydı taslak, `sitemap-demand.xml` değişmedi. `robots.txt`, `llms.txt`, `content-manifest.json` değişmedi. Search Console indekslenme/ranking garanti değil.
- Google resmî kaynaklar: https://developers.google.com/search/docs/appearance/ai-features?hl=tr , https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls , https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=tr . İnceleme fiilî 20.10.2026.

## Gerçek üretilen dosyalar
- Müşteri bilgilendirme taslağı: `cozumler/fatura-on-isleme-mutabakat-kontrolu.html`.
- İki iç bağlantı taslağı: `hizmetler.html`, `sektorler/finans-bankacilik.html`. `sitemap.xml` yeni canonical URL taslağı.
- 12 ek yöntem dosyası: `strateji-yontem-003.md`, `seo-yontem-006.md`, `seo-yontem-007.md`, `seo-yontem-008.md`, `seo-yontem-012.md`, `seo-yontem-016.md`, `seo-yontem-076.md`, `seo-yontem-077.md`, `strateji-yontem-114.md`, `seo-yontem-172.md`, `seo-yontem-184.md`, `seo-yontem-248.md`.
- `146-SAYFA-KONU-KUMESI-ENVANTER.csv` main path bazlı envanter (147 sayfanın tam metadata'sı ayrıca Actions artefaktında `gercek_html_metaanaliz.csv`).
- `SEO_TEK_URL_KANONIK_ROBOTS_MATRİS.md`, `ALICI_SEO_KARARI_VE_ROLLBACK.md`, `tek-sorgu-niyet-haritasi.csv`, `fatura-mutabakat-SENTETIK-ornek.csv`, `METRIKLER_BILINMIYOR.csv`, QA A/B, yayın/kusur kaydı.
- QA komutları: `python scripts/site_integrity.py`; `python scripts/site_qa.py`; `python scripts/day8_quality_gate.py`; `python scripts/v8_day11_finance_qa.py`; `node scripts/v8_day11_finance_browser.mjs`. GitHub Actions `.github/workflows/v8-day11-finance-seo-qa.yml` bunları koşar.
- CI kanıtı ve 375/390/1440 screenshot arşivi (önceki 6 viewport başarılı test): https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/39386605289 . **SENTETİK CSV testini de içeren son commit'in yeni CI sonucunu ayrıca doğrula:** https://github.com/synapseautomate/synapseautomate.github.io/pull/32/checks .

## QA ve açık kusurlar
- **QA A kaynak/teknik:** bağlam kontrolü ve mevcut site bütünlüğü PASS; 147 HTML envanteri ve yeni özel sayfa self canonical, eksik duplicate, örnek aritmetik; son koşu kaynak olarak yukarıdaki Actions. Gün 11 CI öncesi testler bu devre PASS yazılmaz. Kodda gerçek lisanslı marka logosu kullanıldı.
- **QA B tasarım/erişilebilirlik:** 320/375/390/768/1024/1440 gerçek Chromium, 0 yatay taşma, 0 kırık sayfa görseli, tek H1, klavye skip, >=44px CTA, finans aracı 0/8→1/8. İlk denemede 320–390 P1 yatay taşma **FAIL**; `minmax(0,1fr)` / `min-width:0` düzeltildi; sonraki koşu PASS; kanıt Actions run 39386605289. Nihai ekran görselleri manuel incelendi; Safari, Lighthouse field data, canlı kullanıcı tarayıcısı, GSC **TEST EDİLEMEDİ**.
- **Eski test borcu:** `scripts/site_qa.py` main'deki eski bazı ürün/fiyat metinlerini (ör. artık kullanılmayan `$99`) zorunlu tutuyor ve var olan eski meta açıklama eksiklerini işaretliyor. GitHub Actions bunu **gerçek FAIL** olarak `legacy_site_qa.log` / `legacy_site_qa_exit_code.txt` içine kaydeder, yalnız Gün 11 yeni rota testi başarısıyla maskelenmez. P1 teknik borç, ayrı talep olarak çözülmeli; sahte fiyat metnini geri koyma.
- **P0 AÇIK:** GitHub Pages ticari kullanım uygunluğu, yerel vergi/fatura/KYC, FormSubmit gerçek teslim ve KVKK/çerez uzman denetimi. Yeni bilgi sayfasına form/ödeme entegre edilmedi.
- **P1 AÇIK:** önceki günlerden SEO/meta test borcu; Safari ve bağımsız gerçek tarayıcı/ağ erişimi; Google gerçek indeksi (önceden yok). Fiyatsız bilgi sayfası taslak P1 sonrası tekrar QA.
- **P2:** GSC'de sorgu başlığı/mobil snippet varyasyonu ve olası niyet rekabeti ancak yayından sonra ölçülebilir.

## Metrikler ve yetkiler
- GSC gerçek gösterim/tıklama, GSC doğrulanmış sorgu, gerçek nitelikli ziyaret, gönüllü talep, izinli teklif, fonlanmış sipariş, tahsil edilen satış, iade ve net gelir = **BİLİNMİYOR**. Ulaşılmayan sıfır değil. Gerçek kullanıcı verisi dışarı aktarılmadı.
- Kırık hedef sayfa iç link / kanonik hedef uyumsuzluğu CI lokal smoke'da 0 (kapsam yalnız Gün 11 hedef ve iki kaynak yönlendirmesi), global Search Console kanonik seçimi BİLİNMİYOR.
- Peşin harcama **0 TL**; reklam, abonelik/Premium, kart, bot, soğuk DM, sosyal post veya Upwork YOK.
- WEB (yeni sayfa, hizmet/finans linki ve sitemap) **ONAY BEKLİYOR**, yayın YAPILMADI. LinkedIn, Instagram, Facebook, Threads, X, YouTube Gün 11 yeni gönderi YAPILMADI; kullanıcıya otomatik post YOK. PR **DRAFT**, main merge YOK.

## Gün 12 sıfır bağlamlı sonraki tek öncelik
Önce gerçek `main`/PR SHA, kullanıcı yayın izni, PR #32 QA kanıtı ve GSC erişimini doğrula. Eski `site_qa.py` kaynak borcunu ayrı ele al; yeni finans sayfasının yayın kapısını yalnız kullanıcının ayrı açık onayı ve hukuki/uyum kararlarıyla ilerlet. Sayfa paylaşımı/anahtar kelime kopyası üretme; kullanıcı onayı gelene kadar taslak korunur.
