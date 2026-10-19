# Instagram / Story / YouTube — 19.10.2026

Bu klasör **iç QA** dosyasıdır; sosyal platforma otomatik yayın yapmaz.

## Instagram / Story
- Kendi konusu: **Her talep fırsat değildir** — ihtiyaç, kapsam, yetki ve izin ayrımı.
- Aynı günkü LinkedIn CRM devri, Facebook marka tanıtımı, Threads durdurma kararı ve X veri kaynağı gönderilerinin tekrarı değildir.
- 6 özgün PNG 1080×1350 ve 1 Story PNG 1080×1920. Resmî `assets/brand/synapse-logo-clean.png` doğrudan kullanılır.
- Her görselde `SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL` etiketi. Çalışan CRM ekranı yok.

**Instagram caption taslağı:**
> Her talep fırsat değildir.
>
> Gelen talebi değerlendirmek için önce ihtiyacın netliğine, uygulanabilir kapsama, kararı verecek role ve gönüllü iletişim iznine bakın.
>
> Daha çok mesaj her zaman daha nitelikli müşteri anlamına gelmez.
>
> Bu görseller kavramsal/sentetik bir karar çerçevesidir; gerçek müşteri başvurusu veya sonuç içermez.
>
> İş akışı yaklaşımı: https://synapseautomate.github.io/cozumler/musteri-talebi-surec-analizi.html
>
> #SynapseAutomate #SatışOperasyonları #SüreçAnalizi

**Story paylaşım notu:** Aynı 4 kontrol sorusu, marka sitesine bağlantı etiketi (varsa platformda ayrı eklenir). Metinde satış/dönüşüm garantisi yok.

## YouTube
- Görüntü: mevcut gerçek çalışan web aracı `araclar/surec-hazirlik-skoru.html`.
- Playwright tarayıcı kaydı: sekiz checkbox işaretle, sırasıyla skor 0→15→30→45→60→75→85→95→100; final metni doğrula.
- Sadece sentetik örnek yanıtlar; gerçek müşteri, canlı CRM entegrasyonu, API veya gelir iddiası yok.
- Başlık: **Otomasyona Hazırlık Skoru: 8 Soruluk Gerçek Web Aracı | SYNAPSE Automate**
- Açıklama: SYNAPSE'nin gerçek 8 soruluk öz değerlendirme aracını sentetik yanıtlarla kullanıyoruz. Sonuç genel bir öz değerlendirme örneğidir; gerçek müşteri verisi veya uygulama garantisi değildir. https://synapseautomate.github.io/araclar/surec-hazirlik-skoru.html
- Ses/müzik: yok; son QA'da altyazı/sessiz oynatma ve gerçek platform küçük önizlemesi ayrıca kontrol edilmeli.

**Yayın yetkisi:** Kullanıcı Instagram ve YouTube hazırlığını istedi. Üretim/yükleme burada yalnız taslak, gerçek hesap postu yayınlanmadı. Her iki platformun ayrı kanala özel yayın kontrolü şarttır.

## 19.10.2026 — gerçek çıktılar ve son yerel QA
- Ayrı GitHub Actions medya QA çalışması **PASS**: https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/39263203148 (Instagram kaynak logo + sentetik karusel / gerçek arayüz checkbox testi 0→100).
- Nihai yerel dağıtım paketi: `SYNAPSE_IG_STORY_YOUTUBE_YAYIN_TASLAKLARI_FINAL.zip` (platforma yüklenmedi; çalışma oturumu teslimi, GitHub'da public asset değildir). İçerik: 6×1080×1350 Instagram PNG, 2×1080×1920 Story PNG, 1280×720 thumbnail, 1920×1080 / 30.447s H.264 sessiz YouTube video, isteğe bağlı Türkçe SRT, kapak açıklaması/alt metinler/iki QA turu.
- Nihai video CI'nın gerçek web aracı ekran kaydına 3.5 saniye giriş ve 6 saniye açıklayıcı kapanış eklenerek üretildi; gerçek Chromium skor serisi 15/30/45/60/75/85/95/100; kayıtta hiçbir gerçek müşteri veya CRM entegrasyonu yok.
- Yerel ikinci QA: kaynak logo, benzersiz dosya hash'leri, PNG boyutu, okunur kontrast paleti ve sahne örnekleri; Story üst UI bölgesi ile alt açıklama bölgesinin çakışma riski azaltıldı. Instagram/YouTube **canlı uygulama kırpma ve yayım testi** yapılmadı.
- PR #29 üzerindeki *genel site* CI kontrolleri bu bağımsız medya QA'dan ayrıdır ve en son sorguda başarısızdı. Medya QA PASS, tüm repo/site QA PASS değildir.
- Kullanıcı X'teki ilk gönderiyi yayımladığını belirtti, gerçek X permalink/analitik bilinmiyor. Instagram ve YouTube henüz kullanıcı tarafından yayımlanmadı.
- Başlık/açıklama taslakları insanın hesabından paylaşması içindir; onaysız otomatik post, DM, ücretli reklam veya abonelik yok.
