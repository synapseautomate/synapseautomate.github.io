# QA TUR A — kanıt ve teknik negatif kontrol
**24.10.2026.** Kaynak: hizmetler.html `main` ve aynı dosya draft, doğrulanmış var olan arac URL'si. Kullanıcıya satışı/araç faaliyeti gösteren sahte ekran yok.
1. Tek diff değişkeni: hizmet kartına tek `<a class=more>` bağlantısı eklenir, fiyat/başlık/resim/CSS/JS değişmez. GitHub compare ile ayrıca doğrulanmalıdır.
2. Sözlü örnek AI okuryazarlığı karar çerçevesidir; hiçbir gerçek müşteri, ROI, sertifika veya kullanım sayısı yok.
3. Süreç haritası aracı repo main'de bulundu; **canlı HTTP FORM teslimi TEST EDİLEMEDİ**.
4. PDF **gerçek 5 sayfa** 1080×1350 ve PNG ile birebir render diff: 5/5 null bounding box; 5 ayrı PNG; kullanıcı yüklediği logonun alfa pikselleri korunarak orantılı ölçeklendi.
5. Yerel bağımsız kart HTML Chrome 320,375,390,768,1024,1440 **6/6 PASS**, tek H1/tek CTA, klavye focus, touch 57–84px, yatay taşma YOK. Bu canlı site regresyonu DEĞİL.
6. Rıza olmadan GA4 olay üretildiği iddia edilmedi; JS kaynakta `synapse_analytics_consent_v1`, `generate_lead` sadece sessionStorage eşleşen dönüş koşuluna bağlı.
7. Yanlış pozitif test: PDF'deki eğitim/karar kartı **gerçek demo değil**, her görselde sentetik etiketi var.
**İstatistik:** gerçek CTA görüntülenme, klik, GSC ve lead BİLİNMİYOR. Fiyat, tahsilat, mali süreç PASS değildir.

**Kısıt:** İç çalışma. Kazanan kanal BİLİNMİYOR, gerçek kullanıcı örneklemi BİLİNMİYOR, satış BİLİNMİYOR. Yalnız **Yapay Zekâ Eğitimi ve Danışmanlık — AI okuryazarlığı ve otomasyona hazırlık** konusu. CSV/stock önceki gün örnekleri yeni konu olarak kullanılmadı. Gerçek müşteri veya ürün demosu YOK. GitHub main/site, LinkedIn ve Instagram için yeni eylem onayı gerekir; hesap/ödeme/DM/uygulama YOK.
**Dayanak:** Kaynak denetimi 24.10.2026: main ca2a47a0c6cf22149a47b48b74c38c4a8a24cd96; hizmetler.html, surec-analizi.html, iletisim.html, assets/styles-v33.css, assets/js/synapse-measurement-v1.js, araclar/surecini-20-dakikada-haritala.html; önceki Gün14 SYNAPSE_V8_GUN_14_DEVIR.md (#39 arşiv dalı). Resmî: https://developers.google.com/analytics/devguides/collection/ga4/reference/events ; https://www.linkedin.com/help/linkedin/answer/a518909 ; https://developers.google.com/search/docs/crawling-indexing/links-crawlable
