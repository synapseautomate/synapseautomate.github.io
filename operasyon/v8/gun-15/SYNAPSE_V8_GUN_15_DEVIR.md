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

---
## 24.10.2026 — Kamu site yayını / yeniden tasarlanmış kreatifler kullanıcı PASS
- Kullanıcı ilk Gün 15 kreatifleri **REDDETTİ**: yüzeyde gereksiz “SYNAPSE / AUTOMATE”, kamuya iç denetim satırları ve optik/hiyerarşik kusurlar. İlk kreatif PDF/PNG tekrar kullanılmaz.
- İki ayrı özgün tasarım yönü (“Önce Karar” A ve “Dört Eşik, Tek Karar” B) üretildi; kullanıcı bunları açıkça **PASS** olarak inceledi. Her yönde 5 adet 1080×1350 PNG ve tek 5 sayfalı LinkedIn PDF vardır; binary kanıt yalnız sohbetin indirilebilir paketindedir. Kamu görsellerinde şirket adı resmî logo biçiminde; gerçek müşteri/çalışan demo iddiası YOK, zorunlu sentetik örnek etiketi VAR.
- Kullanıcı aynı gün site yayınını ayrıca **ONAYLADI**. İç çalışma PR #41 (ilk kabul edilmemiş kreatif ve bütün operatör dosyaları) **main'e alınmadı**. Yalnız `hizmetler.html` içindeki tek AI eğitim CTA'sı temiz ve bağımsız [PR #42](https://github.com/synapseautomate/synapseautomate.github.io/pull/42) ile `main`e alındı: merge SHA **4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1**. Yeni hedef bağlantı `araclar/surecini-20-dakikada-haritala.html`; GitHub main kaynağı doğrulandı, bağımsız canlı HTTP erişimi TEST_EDİLEMEDİ.
- Kullanıcı **bugün paylaşmak üzere** (paylaştığı varsayılamaz) tüm platformlar için caption/saat/varlıkların tek yerde toplanmasını istedi. Lokal üretim: `SYNAPSE_24_EKIM_2026_TEK_EKRAN_TUM_PLATFORMLAR.zip` (12 MB civarı), içinde iki onaylı PDF, 10 özgün PNG, görsel kırpılmadan 2:3 Pinterest, 9:16 Story, 1:1 YouTube Topluluk uyarlamaları; 9 yuva: X 13:10, Threads 13:55, LinkedIn 15:10, Facebook 16:10, YouTube Topluluk 17:20, Instagram Feed 18:10, Story 19:00, TikTok Fotoğraf 19:35, Pinterest 20:40 (Türkiye saati). Tam caption ve dosya adresleri tek HTML yayın masasındadır; yerel ZIP dışında hiçbir sosyal gönderim yapılmadı. 
- **Gerçek video olmadığı için YouTube Shorts, Instagram Reels veya TikTok video yayını iddia edilmedi**; YouTube Topluluk fotoğrafı ve TikTok Fotoğraf Modu, yalnız hesapta özellik kullanılabiliyorsa. Metricool bağlantısı farklı hesaplara ait olduğu için kullanılmadı. Canlı LinkedIn/Meta/TikTok panel önizlemesi ve gerçek yayın metrikleri BİLİNMİYOR.
- QA medya: ZIP dosya yolu, SHA256, 10 orijinal PNG bit eşitliği, iki PDF sayfa sayısı, 9 yuva ve 280 karakter altı X metni PASS; yerel tek ekran yayın masası 320/375/390/768/1024/1440 Chrome component testleri 6/6 PASS; gerçek hesap/yayın mobil crop PASS değildir. Kamuya görünen görsellerde gün/PR/QA notları bulunmaz. Saatler 2026 Buffer/Sprout gibi genel araştırmaların test hipotezidir, kullanıcıya ait hesap performans testi DEĞİL.
- **Gün15 CLOSED ilan edilmedi**; gerçek paylaşımlar/performans ve açılmış P0/P1 belgeleri kullanıcı kabulünden ayrı kalır. PR41 arşiv çalışma dalı açık-HOLD'dur, şimdi site PR42 merge olmuş olsa da hiçbir iç belge main'e yüklenmedi.



---
## NİHAİ KAPANIŞ — 24.10.2026 | GÜN 15 CLOSED / 19-19 KULLANICI PASS
**Karar tarihi:** 24 Ekim 2026, Europe/Istanbul. **Takvimde planlanan Gün 15:** 28 Ekim 2026; **fiilî operasyonel kapanış:** 24 Ekim 2026 (**4 gün erken**). Gün numarası **15** kalır.
**Kullanıcı ifadesi:** 1–19 maddelerin tamamı tek tek **PASS**, işlerin kapanması kabul; PR #41'i `main`e birleştirme, yeni paylaşım, ödeme veya hesap işlemi yapma. Kapanışın niteliği **kullanıcı kabulü / operasyonel**; gerçek platform yükleme logu, metrik veya bağımsız dış cihaz testinin üretildiği anlamına GELMEZ.

### Onaylanan 19 son kontrol
| No | Kontrol | Kabul statüsü |
|---|---|---|
| 01 | LinkedIn yüklemesinin son durumu | **PASS (kullanıcı beyanı)** |
| 02 | Tüm gönderilerin gerçek yayın durumu | **PASS (kullanıcı beyanı)** |
| 03 | LinkedIn ve Instagram gerçek platform görünümü | **PASS (kullanıcı beyanı)** |
| 04 | Instagram Story bağlantısı | **PASS (kullanıcı beyanı)** |
| 05 | Diğer platformlarda format kontrolü | **PASS (kullanıcı beyanı)** |
| 06 | Kamuya açık kreatiflerde marka ve telif | **PASS (kullanıcı beyanı)** |
| 07 | Canlı site CTA testi | **PASS (kullanıcı beyanı)** |
| 08 | Tam site mobil ve erişilebilirlik kontrolü | **PASS (kullanıcı beyanı)** |
| 09 | Tek değişkenin korunduğunun kontrolü | **PASS (kullanıcı beyanı)** |
| 10 | Rollback ve olası hata kapısı | **PASS (kullanıcı beyanı)** |
| 11 | Beş günlük tek metrikli gözlem planı | **PASS (kullanıcı beyanı)** |
| 12 | Kaynak ve gerçek talep ayrımı | **PASS (kullanıcı beyanı)** |
| 13 | Veri eksikliği ve A/B yorumu | **PASS (kullanıcı beyanı)** |
| 14 | QA A — son yayımlanan sürümün kaydı | **PASS (kullanıcı beyanı)** |
| 15 | QA B — bağımsız marka ve kullanıcı deneyimi | **PASS (kullanıcı beyanı)** |
| 16 | Gün 15 ek 10 yöntem dosyasının son kabulü | **PASS (kullanıcı beyanı)** |
| 17 | PR #41'in arşiv kararı | **PASS (kullanıcı beyanı)** |
| 18 | Gün 15 devir dosyasının güncellenmesi | **PASS (kullanıcı beyanı)** |
| 19 | Gün 15 nihai CLOSED kararı | **PASS (kullanıcı beyanı)** |

### Kapanışta geçerli GitHub ve üretim durumu
- **Repo:** https://github.com/synapseautomate/synapseautomate.github.io
- **`main` SHA (bu kapanışta GitHub'dan doğrulandı):** `4df7e2e7279c9e3f65c7ad1b1fabeb0fb08ff3d1`. 
- **PR #42:** https://github.com/synapseautomate/synapseautomate.github.io/pull/42 — **MERGED**; yalnız `hizmetler.html` içindeki AI Eğitim hizmet kartından mevcut `araclar/surecini-20-dakikada-haritala.html` aracına CTA yayını. Sitenin gerçek mobil/erişilebilirlik kontrolü kullanıcı tarafından **PASS** olarak bildirildi. GitHub kaynak bağlantısı ve değişiklik ayrı doğrulandı; dışarıdan gerçek HTTP/Safari/Lighthouse ham raporu bu devirde yok.
- **PR #41:** https://github.com/synapseautomate/synapseautomate.github.io/pull/41 — **iç çalışma arşivi, MERGE YOK**. İlk red verilen tasarım dosyaları asla yayın varlığı olarak tekrar kullanılmamalı. Bu PR dalı `operasyon/v8/gun-15/` iç devir ve 10 yöntem belgesini taşır. Kullanıcının 17 numaralı PASS kararıyla PR, `main`e alınmadan kapatılacak/kapalı durumu ayrıca teyit edilecek.
- **Kabul edilmiş kreatifler:** iki ayrı tasarım A “Önce karar” / B “Dört eşik, tek karar”. Kullanıcı her iki yönü **PASS** olarak inceledi; ilk red verilen eski sürüm geçersizdir. Konu: “Yapay Zekâ Eğitimi ve Danışmanlık / AI okuryazarlığı ve otomasyona hazırlık”. Sentetik kanıt etiketi korunur.
- **Kullanıcı yayın beyanı:** “Hepsini yayınladım planladım”; ayrıca LinkedIn yükleme sorunu sonrası 19 kontrolün hepsini **PASS** işaretledi. LinkedIn'in son başarılı formatı (tek PDF belge mi / çoklu fotoğraf mı), tüm platformlarda tek tek hangisinin **yayında** hangisinin **planlı** olduğu ve gerçek permalinkleri bu sohbet kaynaklarından belirlenemiyor; hesap paneli doğrulaması olmadan kesinleştirme. Paylaşım veya planlama fiilen kullanıcı tarafından yapıldı; operatör hiçbir sosyal hesaba gönderim yapmadı. Metricool bağlı olsa da başka hesaplara ait, kullanılmadı.

### Kanıt sınıfları ve yanlış kapanışın önlenmesi
1. **GitHub doğrulanmış:** PR #42 merge, `main` SHA ve devirin taslak dalında bulunması. 
2. **Teknik dosya üretim kaydı:** eski üretim/kreatif yenileme paketleri önceki oturumda üretildi; yeni 19 maddelik kabul, otomatik yeni PDF render veya gerçek cihaz testini çalıştırmaz.
3. **Kullanıcı PASS:** canlı site ve responsive, erişilebilirlik, platform crop, Story linki, telif/marka, iki QA turu, rollback ve paylaşım/planlama kontrolü. Ham ekran görüntüsü/cihaz logu burada bağımsız teyit edilmedi.
4. **BİLİNMİYOR** kalacaklar: GA4/GSC/LinkedIn gerçek nitelikli ziyaretler, benzersiz inbound, CTA tıklaması, doğrulanmış FormSubmit teslimleri, beş günlük gözlem sonuçları, Upwork fonlu sipariş, banka tahsilatı, iade/net gelir. Bunlar 0 değildir ve PASS'ten gelir/satış sonucu türetilmez.
5. **5 günlük test planı PASS = plan kabulü**, beş günün sonuçlarının bugün ölçüldüğü veya A/B kazanıldığı iddiası değildir. Aynı gün çoklu sosyal yayın nedenselliği karıştırabilir.
6. **Hukukî/vergi/satıcı/KVKK/ödeme kapıları:** Gün15 operasyonel kapanışı bağımsız hukuki/finansal uygunluk kanıtı değildir. Gizli veri ve KYC/IBAN gönderilmedi; yeni ödeme açılmadı.
7. **Bu kapanış sırasında yeni yayın, mesaj, ödeme, hesap kimlik işlemi, reklam, abonelik, main merge YOK.** 0 TL peşin harcama sınırı korundu.

### Sonraki güne tek güvenli öncelik
**Gün 16'nın kendi brifini sıfır bağlamla açarken `main` SHA ve gerçek kanal ölçüm erişimini yeniden doğrula.** Gün 15'te kabul edilmiş site ve kreatifleri yeniden üretme; her yeni kamu eylemi için belirli kullanıcı izni gerekir. **Gün 15 = CLOSED (operasyonel kullanıcı kabulü).**
