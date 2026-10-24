# QA TUR B — ayrı marka/UX/hukuk/konversiyon okuması
- **Metin ve UX:** Türkçe, tek mesaj, tek CTA, sahte kullanıcı ve iç operasyon notu yok. Resmî kullanıcı sağlama logosunun oranları korundu.
- **PDF üretim:** 5/5 gerçek PNG açıldı ve 320px küçük önizleme contact sheet üzerinde kontrol edildi. İlk taslakta logo zorunlu etiketle çakışıyordu, logo üst sağa taşınıp **yeniden render edildi**. İkinci versiyonda alt etiket serbest.
- **Telif:** yalnız kullanıcı sağladığı logo, özgün PIL geometrileri ve sistemde lisans dosyası dağıtılmadan yer alan Inter ailesi (font varlığı dosyası teslim edilmedi). Profesyonel üçüncü taraf fotoğraf/müzik YOK.
- **Bağımsız komponent CTA QA:** Chromium 320/375/390/768/1024/1440 6/6 PASS, klavye odak görünür, buton 57–84px, taşma yok. Mevcut sitedeki dış CSS'le tam canlı sayfa aynı kabul edilmez.
- **Sınırlar:** AI eğitimi sonuç garantisi ve eğitim sertifikası yok; karar matrisi örnek/hipotezdir.
- **Platform:** LinkedIn PDF 5 sayfa, 1.1MB altı; resmî PDF destekli. LinkedIn şirket/Instagram yayın paneli ve gerçek crop test edilmedi. İki platform için kullanıcı **ayrı yayım izni** zorunlu.
- **Açık P0:** ticari/fatura/veri yetkileri güncel bağımsız panel görmeden kanıtlanmadı. **P1:** gerçek sayfa HTTP, Safari/Lighthouse, LinkedIn/Instagram gerçek uygulama crop ve FormSubmit teslimi TEST EDİLEMEDİ.
- **Karar:** Taslak/medya üretimi QA PASS; yayına ve gerçek dönüşüm testine hazır değil.

**Kısıt:** İç çalışma. Kazanan kanal BİLİNMİYOR, gerçek kullanıcı örneklemi BİLİNMİYOR, satış BİLİNMİYOR. Yalnız **Yapay Zekâ Eğitimi ve Danışmanlık — AI okuryazarlığı ve otomasyona hazırlık** konusu. CSV/stock önceki gün örnekleri yeni konu olarak kullanılmadı. Gerçek müşteri veya ürün demosu YOK. GitHub main/site, LinkedIn ve Instagram için yeni eylem onayı gerekir; hesap/ödeme/DM/uygulama YOK.
**Dayanak:** Kaynak denetimi 24.10.2026: main ca2a47a0c6cf22149a47b48b74c38c4a8a24cd96; hizmetler.html, surec-analizi.html, iletisim.html, assets/styles-v33.css, assets/js/synapse-measurement-v1.js, araclar/surecini-20-dakikada-haritala.html; önceki Gün14 SYNAPSE_V8_GUN_14_DEVIR.md (#39 arşiv dalı). Resmî: https://developers.google.com/analytics/devguides/collection/ga4/reference/events ; https://www.linkedin.com/help/linkedin/answer/a518909 ; https://developers.google.com/search/docs/crawling-indexing/links-crawlable
