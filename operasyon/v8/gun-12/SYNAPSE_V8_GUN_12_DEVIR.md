# SYNAPSE V8 GÜN 12 — SIFIR BAĞLAMLI DEVİR (TASLAK)
**Fiilî tarih:** 21.10.2026. **Plan:** 25.10.2026 / Gün 12, **4 gün erken**. Gün numarası değiştirilmedi.
**Ana repo:** https://github.com/synapseautomate/synapseautomate.github.io ; doğrulanan main SHA `06ab1885c44ad4a9e00ccc158543a3388eda6c24`.
**Üretim dalı:** `draft/v8-gun-12-ik-cv-human-gate-shorts-20261021`. **main değişmedi**. Açık Gün11 video PR #33; PR #34 finance SEO merged. V6 #10/#11, V7 #12, V8 #13, V8 Gün01–08 ve Gün10 devirleri ilgili PR dallarında; Gün07 ve Gün09 standart devirleri main içinde bulunamadı. Gün11 finans, Gün10 CRM, Gün08 CSV; Gün12 farklı hizmet / farklı karar.
## A) Tek amaç
İK/CV ön elemede eksik belgeyi otomatik eleme kararıyla karıştırmamak. Alıcı: işe alım operasyon yöneticisi. Tek soru: CV'de SQL beyanı eksikse otomatik ret mi, yetkili insan incelemesi mi? Sitenin `hizmetler.html` sayfası CV ön eleme ve nihai istihdam kararının insanda kalacağını açıklar. **Mevcut çalışan SYNAPSE CV analiz ürünü bu denetimde kanıtlanmadı**.
## B) Gerçek üretim ve kanıtın statüsü
Ayrı sohbet teslim paketinde aynı oturumda yazılmış **kavramsal yerel prototip**, iki sentetik CSV, negatif `yaş` testi, Python kodu, gerçek 22sn Xvfb terminal kaydı ve iki dikey Shorts MP4 (69s + 27s, 1080×1920), iki SRT, konuşma metni ve dört sayfalı LinkedIn/Instagram 4:5 PDF/PNG bulunur. **Bu PR'a ikili video dosyaları eklenmedi**, kamuya ürün demosu değildir. Yalnız editoryal/test kaydıdır; canlı müşteri verisi yok, ATS/API/aday sıralama yok.
Test: `python cv_kontrol.py adaylar_SENTETIK.csv rol_kriterleri_SENTETIK.csv --output sonuc_SENTETIK.json` → exit 0, iki insan incelemesi, hiçbir otomatik ret yok; `python cv_kontrol.py adaylar_YASAK_ALAN_NEGATIF_TEST.csv rol_kriterleri_SENTETIK.csv` → `DATA_MINIMIZATION_BLOCKED: yaş`, exit 2; `python -m unittest -v test_cv_kontrol.py` → 4/4 PASS. Bu yeni prototip testidir, mevcut ürüne ait performans kanıtı değildir.
Shorts 69s SHA256: `fa8254f9edc09fc9f66d5208feac89d07d28377bf2e54ab468eaceca73652372`.
Shorts 27s SHA256: `b15f3dbbe7a777ce95ce4cc73ba0909757f487b0df780799110fd531720fd9dc`.
## C) Açık kusurlar
**P0=3 açık:** gerçek çalışan İK/CV ürünü kanıtı yok; işe alım/adillik/KVKK gerçek uygulama kabulü yok; bağımsız kamu yayın onayları yok. **P1=3 açık:** gerçek konuşma+SRT senkronu, gerçek mobil/platform safe zone, canlı alt URL/form/UTM testleri. **P1 2 düzeltildi:** bozuk CTA glifi ve iç kreatif notu. **P2=2:** ileri motion ve resmi logo/brand book kıyası.
## D) QA turları
**A:** CLI/negatif test/ham JSON, SHA, gerçek ekran kaydı. **B:** iki MP4 ffprobe 1080×1920, 69/27sn, PAL contrast; 320/375/390/768/1024/1440 px raster mobil preview; 4 sayfalı PDF render, Türkçe, telif ve gizlilik kontrolü. Raster ölçekleme **gerçek cihaz testi değildir**. Kullanıcı JPG logosu kullanıldı; Noto Sans OFL-1.1 yerel font, üçüncü taraf müzik yok; özgün sentetik ses üretildi. Gerçek YouTube/LinkedIn/Instagram hesap paneli, Safari, Lighthouse, FormSubmit, GA4 **NOT_TESTED**.
## E) Gerçek metrikler
Bu operatör oturumunda peşin harcama 0 TL, dış yayın 0, kanal onayı 0. Tekil izleyici, gösterim, CTR, 30sn izleme, nitelikli site ziyareti, gönüllü talep, izinli teklif, fonlanan sipariş, tahsilat, iade, net gelir **BİLİNMİYOR**; sıfır olduğu iddia edilmez.
## F) Kopya ve ayrı izinler
Sohbet teslim paketinde storyboard, 2 farklı Shorts başlığı/açıklaması, LinkedIn Post #2 özgün tam metin, LinkedIn/IG native 4:5 PDF, alt metinler, SRT ve tüm yöntem MD dosyaları mevcut. İzin ID'leri: `YT-SHORT-69-20261021`, `YT-SHORT-27-20261021`, `LI-POST-02-20261021`, `LI-CAROUSEL-20261021`, `IG-022-20261021`, `IG-079-20261021`, `WEB-CV-SCOPE-20261021`. **HEPSİ ONAY BEKLİYOR**, hiçbir yayın, yükleme, schedule, DM veya ödeme yok.
## G) Kapsam sınırları ve engellenenler
Gerçek CV, aday kimliği, profil, fotoğraf, yaş, kişisel veriler alınmadı. Hukuki uygunluk için KVKK ve işe alım uzmanı incelemesi gerekli. Gerçek şirket/KYC/vergi/fatura ve ödeme paneli bilinmiyor. Shopier/Upwork kapsam dışı; 0 TL peşin. Satışa açık iddiası yasak.
## H) Sonraki **tek öncelik**
Önce mevcut yetkili SYNAPSE İK/CV motorunun varlığı ve gerçek çalıştırma kanıtını belirle; ürün yoksa kavramsal MP4'leri ürün gösterimi diye yayımlama. Varlık başına bağımsız onay ve açık P0/P1 kapıları kapanmadan internet yayını yok. Main/PR/SHA yeniden kontrol edilmeli.
## Kaynaklar (21.10.2026)
- İK hizmeti: https://github.com/synapseautomate/synapseautomate.github.io/blob/main/hizmetler.html
- İnsan onayı: https://github.com/synapseautomate/synapseautomate.github.io/blob/main/rehberler/ai-otomasyonunda-insan-onayi.html
- Örnek onay: https://github.com/synapseautomate/synapseautomate.github.io/blob/main/kanit/ornek-insan-onay-karti.html (İK değil)
- KVKK: https://www.kvkk.gov.tr/Icerik/4189/Kisisel-Verilerin-Islenmesine-Iliskin-Temel-Ilkeler
- YouTube Shorts resmî: https://support.google.com/youtube/answer/12779649?co=GENIE.Platform%3DDesktop
- WCAG: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum


## 21.10.2026 - V2 kreatif düzeltme ve kullanıcı geri bildirimi
- Kullanıcı önceki videolarda iç QA/yönetim metni ile JPEG logo arka planı kusuru buldu. V1 doğrudan yayın için uygun görülmedi.
- V2: iki yeniden render 9:16 Shorts 69s ve 27s, 1080x1920 H.264/AAC; iki kapak, Türkçe sahne metinleri, ayrıca LinkedIn ve Instagram native dört sayfa PDF. İkili medya sohbet dosya teslimindedir, GitHub PR'a yüklenmedi.
- V2'de kamu görsellerinden QA/test iç notları kaldırıldı. Her karede orijinal görev gereği SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL korunur. Kullanıcı kaynaklı logo yeniden çizilmeden algoritmik alfa matlandı; önceki JPG dikdörtgeni kaldırıldı.
- V2 negatif QA: ilk yeniden kayıtta 42. saniyede kaynak terminalin siyaha düşmesi bulundu. 16s gerçek kaydın son sağlam karesi tutularak düzeltildi, terminale sahte çıktı eklenmedi. Son kayıt 42. saniye gerçek kaynak satırlarını gösterir.
- SHA256 (69s): 0c4bffb05e266a5445027569819edc981cb339d9ddbad3b86fec402b6c7767e3
- SHA256 (27s): c3afd89402017c827377961d6d578da5f305fe66ffb677f56e85f427744e095d
- QA A: sentetik yerel prototip pozitif exit=0, yasak yaş exit=2, 4/4 unittest; video codec/süre/oran testleri PASS. Bu var olan SYNAPSE ticari CV ürünü kanıtı değildir.
- QA B: 320/375/390 px küçültme görselleri, 4:5 PDF yeniden render ve metin kontrastı 9.53:1 test edildi. Gerçek telefon/platform paneli, canlı HTTP, yasal/KVKK denetimi NOT_TESTED. Konuşma seslendirmesi yok, ses sentezlenmiş, SRT sahne metni.
- Eylem kapıları: YT 69s, YT 27s, LinkedIn gönderi/belge ve Instagram karusel için birbirinden ayrı ONAY BEKLİYOR; hiçbir hesapta yayın/planlama, main merge, ödeme ve özel iletişim yapılmadı.
- Sonraki tek adım: Kullanıcının gerçek mobil YouTube Shorts önizlemesi ve içerik doğruluğu onayı. Canlı İK ürünü gibi göstermeden yalnız doğru kavramsal/sentetik açıklama ile kullanılabilir.
