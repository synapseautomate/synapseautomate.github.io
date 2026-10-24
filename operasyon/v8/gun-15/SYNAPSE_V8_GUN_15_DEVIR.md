# SYNAPSE Automate — V8 MAX Gün 15 sıfır bağlamlı tam devir
**Fiilî tarih:** 24.10.2026, Europe/Istanbul UTC+3. **Plan tarihi:** 28.10.2026, **4 takvim günü erken**, numaralandırma 15/30 kalır. Gün adı: **Kazanan kanala tek değişkenli iyileştirme**.
**Güncel içerik odağı:** Yapay Zekâ Eğitimi ve Danışmanlık — *AI okuryazarlığı ve otomasyona hazırlık karar matrisi*. Bu konu, önceki Gün 13 Pazarlama & İçerik ve Gün 14 Hukuk/Uyum ve CSV stok ayrı örneklerinden farklıdır. Metindeki eski CSV özel sosyal brief, kullanıcının güncel öncelikli hizmet odağı blokuyla değiştirildi; **çalışan CSV ürünü hipotezi/kanal ve veri kısıtları aynen geçerlidir.**

## A) Girdi / tek amaç / satış etkisi
**Repo:** https://github.com/synapseautomate/synapseautomate.github.io
**İşe başlanırken main SHA:** `ca2a47a0c6cf22149a47b48b74c38c4a8a24cd96` (24.10.2026).
**Gün15 draft PR #41:** https://github.com/synapseautomate/synapseautomate.github.io/pull/41
**Dal:** `draft/v8-gun-15-ai-egitim-tek-cta-20261024` — **main MERGE YOK**.
**Önceki durum:** Gün14 CLOSED (kullanıcı 11/11 PASS), iç PR #39 CLOSED arşiv, web PR #40 MERGED. Gün 01–13 devirleri Gün 14 arşivinde, Gün09 standart devri bulunamadı (PR #26 kaynak). Gün01–07 dokunulmaz. Gün08 Upwork açmama/kapatma kararı korunur. Metricool başka hesap, kullanılmadı.
**Tek amaç:** en iyi niyetli kullanıcıya giden *kanıtlı* kaynakta bir açıklık sürtünmesi kaldırılacak bir taslak hazırlamak. **Gerçek kanal kazananı BİLİNMİYOR**, çünkü GA4/GSC/LinkedIn Services/gerçek inbound paneli yok. Performans kazananı ilan edilmedi. Mevcut sahip olunan site/organik arama **koşullu deney yüzeyi**, LinkedIn **ikincil aday**, Upwork kapsam dışı. A/B başarı rakamı yok.

## B) Gerçek yapılanlar / kaynaklar / önce sonra
- `hizmetler.html` AI Eğitim & Danışmanlık kartında **tek kaynakta gözlenebilen açıklık eksikliği:** sonraki adım linki yoktu. Site kodu hizmeti “yapay zekâ okuryazarlığı, strateji danışmanlığı ve dijital dönüşüm yol haritası” diye tanımlıyor. Ayrı çalışan AI eğitim ürünü kanıtı YOK; `sektorler/egitim.html` eğitim *sektörü* sayfası, aynı hizmet ürünü sayılmaz.
- Hedef `araclar/surecini-20-dakikada-haritala.html` main'de gerçek HTML ve haritalama girişleriyle bulundu. Form teslimi canlı HTTP ile doğrulanamadı.
- **Tek değişken:** yalnız `hizmetler.html` Eğitim kartında `<a class="more" href="araclar/surecini-20-dakikada-haritala.html">Otomasyona hazırlık için sürecini haritala</a>`. Öncesi kart başlık ve metin aynı, link yoktu. Sonrasında diğer unsurlar AYNEN korundu. İlk değişiklik commit `925cd21734c51098ed70c62d761088d57d3722aa`.
- `assets/js/synapse-measurement-v1.js` **değiştirilmedi**; analitik `synapse_analytics_consent_v1` izin ve `generate_lead` yönlendirme mantığı kaynakta okundu. Gerçek event paneli yok. Yeni `cta_click` yalnız olay sözlüğü hipotezi, çalışan kod değil.
- **Sosyal kaynak dosya ve PDF:** gerçek 5 sayfalı 1080×1350 LinkedIn PDF, ayrı 5 PNG 1080×1350 Instagram varyantı, 320px contact sheet, birebir render/eşitlik testleri ve kaynak script'i kullanıcıya ZIP olarak verildi. Binary bu PR'da bulunmaz. Her görsel `SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL` taşıyor; kullanıcının sağladığı RGBA SYNAPSE logosu oranı korunarak kullanıldı, üçüncü taraf varlık yok.
- Hikâye/alıcısı: B2B operasyon yöneticisi, veri izni → süreç haritası → insan devri → ölçüm kapısı. Senaryo bütünüyle KAVRAMSAL; kurs, sertifika, canlı yazılım, ROI/gelir, gerçek müşteri, demo ispatı yok.
- **Zorunlu metinler:** `TEK_DEGISKEN_DENEY_NOTU.md`, `ONCE_SONRA_KOPYA_VE_KONTROL.md`, `QA_ROLLBACK_ONAY_KAPISI.md`, `SOSYAL_LINKEDIN_INSTAGRAM_KOPYA_VE_IZIN.md`, `GERCEK_METRIK_SOZLUGU_VE_EKSIK_KANIT.md`, `QA_TUR_A_KAYNAK_TEKNIK.md`, `QA_TUR_B_MARKA_ERISILEBILIRLIK.md` ve 10 yönteme özel `063/088/110/125/128/149/174/233/234/251` dosyası. Gün15 tam devri bu dosyadır.

## C) P0/P1/P2 ve yayın kararları
| Seviye | Hata / risk | Sorumlu | Sonuç |
|---|---|---|---|
| P0 | Türkiye satıcı/fatura/tahsilat, KYC, veri işleme ve teslim yükümlülükleri bağımsız kanıtlı değil | hesap sahibi + uzman | AÇIK; gerçek satış açma YOK |
| P0 | Kanıtlanmamış kanal kazananı veya gelir iddiası | operatör | ÖNLENDİ: kazanan BİLİNMİYOR |
| P1 | Canlı site, mobil/Safari, 404/HTTP, gerçek form teslimi ve Lighthouse | teknik QA | TEST EDİLEMEDİ |
| P1 | Nitelikli test örneklemi, CTA/lead gerçek panel verisi | hesap sahibi | BİLİNMİYOR |
| P1 | LinkedIn/Instagram hesapta gerçek crop ve alt text UI | içerik/panel | TEST EDİLEMEDİ |
| P2 | Yerel 320px karusel önizlemesinde tablonun küçük metni | tasarım QA | görünür ama küçültüldüğünde temkinli kullanım |
**Teknik taslak üretimi:** hazır. **Kamu ve ticari yayın:** ONAY BEKLİYOR, yayına hazır olarak değerlendirilmedi.

## D) İki ayrı QA turu / gerçek testler
**QA A / Kaynak-teknik:** GitHub diff (main ↔ draft) yalnız tek kamuya yönelik `hizmetler.html` diff'i; diğerleri `operasyon/v8/gun-15`. Orijinal eğitim kartı kaynak metni aynen sabit. Resmî LinkedIn PDF kullanım şartı 100 MB ve 300 sayfa sınırı:
https://www.linkedin.com/help/linkedin/answer/a518909
Google GA4 önerilen olay kaynak:
https://developers.google.com/analytics/devguides/collection/ga4/reference/events
Google bağlantı rehberi:
https://developers.google.com/search/docs/crawling-indexing/links-crawlable
**QA B / Marka-UX:** yerel *yalnız izole CTA komponenti* Chromium 320/375/390/768/1024/1440 **6/6 PASS**, tek H1/CTA, dokunma 57–84px, yatay taşma 0, klavye odak PASS. Script `python preview_test.py`, kaynak ve ekran görüntüleri ZIP içindedir. **Bu tam canlı site sonucu DEĞİL.**
**PDF testi:** `python build.py` (PIL+reportlab+fitz). PDF 5 sayfa, her sayfa 1080×1350; PDF'den yeniden rendera karşı 5/5 piksel eşitlik (`diff_bbox:null`), contact sheet 320px. İlk render'da etiket ve logo birbirine yakındı; yeniden yerleştirildi, PDF/PNG tekrar üretildi. Üçüncü taraf logo/foto/müzik kullanılmadı.
**Gerçek site HTTP:** https://synapseautomate.github.io/hizmetler.html ve https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html web üzerinden açma denemesi yapıldı, erişilemedi; **HTTP TEST_EDİLEMEDİ**. Safari/gerçek iPhone/analytics/FormSubmit ayrıca TEST EDİLEMEDİ.

## E) Ölçümler (24.10.2026; 0/BİLİNMİYOR ayrımı)
| Kanal ve ölçü | Birim | Değer | Kanıt |
|---|---|---|---|
| AI eğitim CTA nitelikli gösterim→gönüllü talep | % | BİLİNMİYOR | GA4 izinli oturum/teyitli FormSubmit yok |
| Gerçek test örneklemi | kişi | BİLİNMİYOR | panel yok |
| Değişen tek değişken | adet | 1 | GitHub diff, yüksek |
| Gerçek CTA hata sayısı | hata | BİLİNMİYOR | canlı tarayıcı yok |
| LinkedIn PDF sayfa | sayfa | 5 | fitz, yüksek |
| LinkedIn/Instagram gösterim, kaydetme, nitelikli teknik soru | olay | BİLİNMİYOR | platform panel yok |
| izinli teklif, funded platform siparişi, tahsilat, iade, net gelir | işlem/TRY | BİLİNMİYOR | satış paneli yok |
| Bu çalışmanın peşin ücretli işlemi | TRY | 0 | yeni ücretli eylem yok |
| Bu çalışmanın sosyal paylaşımı/main merge | eylem | 0 | kullanıcı yayım onayı yok |
**Kanal kararı:** G14 seçimi “koşullu site testi” kazanmış kanal demek değil; ≥5 gerçek nitelikli talep eşik kanıtı yok.

## F) Ürün/kreatif ve ayrı izinler
- LinkedIn tam kopya+başlık+PDF+alt açıklaması, Instagram ayrı caption+5 PNG ve telif/etiket sınırları `SOSYAL_LINKEDIN_INSTAGRAM_KOPYA_VE_IZIN.md`.
- `WEB-G15-TEK-CTA-20261024` — **ONAY BEKLİYOR** (site main merge).
- `LI-G15-AI-EGITIM-20261024` — **ONAY BEKLİYOR** (LinkedIn Company PDF).
- `IG-G15-AI-EGITIM-20261024` — **ONAY BEKLİYOR** (Instagram 5 PNG).
- Açık müşteri talebine cevap, satış/ödeme, başka hesap aktivasyonu ayrı onay gerektirir.
Bugün **YAYINLANMADI**; hiçbir izinsiz DM/e-posta/teklif/Youtube/Metricool işlemi yok.

## G) Kanıtlı açık iş ve engellenen adımlar
Yetkili gerçek GSC/GA4/FormSubmit/LinkedIn panel olmadan performans/deney zaferi yok. Gerekirse hesap sahibi yalnız kişisel veri içermeyen toplam metrik sağlayabilir; parola/IBAN/kimlik/gerçek sözleşme isteme. Satıcı/vergi/veri/mesafeli satış uygunluğu önce ayrı uzman ve resmî panel ile.
**Geri alma:** tek yeni `<a>` öğesini hizmet kartından silerek eski kartı geri getir; commit `925cd21734c51098ed70c62d761088d57d3722aa` branch düzeyinde tersine çevirilebilir. Main henüz değişmedi; rollback canlı uygulama diye raporlanmaz.

## H) Sonraki tek öncelik / sıfır bağlamlı operatöre
**Gerçek panelden** aynı hizmet kartının izinli nitelikli görünüm→gönüllü talep işaretleri alınabiliyor mu kontrol et; yoksa performans kazananı BİLİNMİYOR ve A/B HOLD. **Başka sayfa/başlık/renk/CTA değiştirme.** Kullanıcı önizleme ve kanıtları onaylarsa yalnız spesifik WEB-G15-TEK-CTA-20261024 için ayrı merge izni gerekir. Gün 15 **CLOSED DEĞİL**; eylem bazlı izinler bekliyor.