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
