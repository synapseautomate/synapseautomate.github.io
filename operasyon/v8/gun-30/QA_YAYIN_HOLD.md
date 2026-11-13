# V8 Gün 30 QA/Yayın Kapısı — 2026-11-13

## Tur A — kaynak, veri, teknik
- GitHub HEAD `defdb2f66e998533541daa57e031e91b5a62b02a`: doğrulandı.
- Mevcut site, sitemap, robots, JS kaynak: okundu; canlı HTTP 200/404 ve JS yürütümü **TEST EDİLEMEDİ**.
- Ticari metrik ve banka/panel: **BİLİNMİYOR**.
- Yerel iki dikey MP4: H264 yuv420p, 1080x1920, 24fps, 9s, AAC; ffprobe ve tam ffmpeg decode PASS.
- LinkedIn PDF: 4 sayfa, fitz ile 4/4 açılma ve render PASS.

## Tur B — marka, erişilebilirlik, hukuki dönüşüm
- Kullanıcının özgün logo PNG'si doğrudan kullanıldı, yeniden çizilmedi; düşük alfa kalıntısı temizlendi. Yeni görseller kullanıcıya özgü özgün vektör tasarımlar; gerçek ürün UI görüntüsü değildir.
- Önizlemelerde taşan grafik düzeltilip yeniden render edildi.
- Gerçek iOS/Safari, klavye, alt'ın platforma girilmesi, WCAG 320–1440 ve FormSubmit teslimi TEST EDİLEMEDİ.
- Fatura/vergisel uygunluk, fizikî tahsilat, satış teslim/iade şartları TEST EDİLEMEDİ.
- Site NEW DEPLOY: YAPILMADI; sosyal/Upwork aktivasyonu: YAPILMADI.

**Karar:** açığı ölçülmemiş P0/P1 sıfır denemez. Kullanıcı site yayın izni verdi ama teknik/hukuki kapılar karşılanmadığından yeni main merge yapılmadı; taslak PR'da tutuldu.
