# Gün 15 olay/gerçeklik sözlüğü (24.10.2026)
| Ölçü | Pay / payda ve tanım | Değer / birim | Gerçek kaynak güveni |
|---|---|---|---|
| nitelikli gösterim→talep | izinli nitelikli gerçek inbound / aynı sayfa ve döneminde nitelikli görünüm | BİLİNMİYOR % | GA4 / FormSubmit paneli YOK |
| gerçek_test_orneklemi | benzersiz nitelikli gerçek kullanıcı gözlemi | BİLİNMİYOR kişi | hesap verisi yok |
| degisen_tek_degisken | Eğitim hizmet kartındaki **bir CTA bağlantısının varlığı** | 1 taslak değişken | GitHub diff, yüksek kaynak güveni |
| karsilama_cta_hatasi | gerçek canlı ziyaretçi akışında CTA kırık/yanlış yönlendirme | BİLİNMİYOR hata | GitHub hedef dosyası var; HTTP yok |
| sosyal_pdf_sayfa_sayisi | gerçekten oluşturulan LinkedIn PDF | 5 sayfa | fitz page count, yüksek |
| gösterim, sayfa oturumu, demo | farklı olay adımları | BİLİNMİYOR | consentli GA4/GSC yok |
| gönüllü talep, izinli teklif | FormSubmit gerçek teslim + yetkili cevap | BİLİNMİYOR | panel yok |
| fonlanan sipariş, tahsilat, iade, net gelir | ayrı finansal belgeler | BİLİNMİYOR | banka/Upwork paneli yok |
| bu üretimde dış yayın/peşin ücret | kullanıcıya gönderi veya ücretli işlem | 0 olay / 0 TL | bu oturum eylem kaydı |
**Örnek payload (gerçek olay değil):** `{ "event":"cta_click", "page_path":"/hizmetler.html", "cta_id":"ai_egitim_readiness", "utm_source":"site", "utm_medium":"organic", "utm_campaign":"ai_readiness_g15" }`. Bu kod siteye eklenmedi; mevcut JS yalnız `data-synapse-event` üzerinden olay çıkarır ve rıza olmadan GA4 göndermez.
**UTM örneği:** `https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html?utm_source=site&utm_medium=organic&utm_campaign=ai_readiness_g15` sadece *test metni*; draft CTA doğrudan temiz URL'yi kullanır. Gizlilik: kişi, IP, ham sözleşme, banka detayı yok. Test dönüşü `git revert <commit>` ya da bağlantı satırı kaldırma.

**Kısıt:** İç çalışma. Kazanan kanal BİLİNMİYOR, gerçek kullanıcı örneklemi BİLİNMİYOR, satış BİLİNMİYOR. Yalnız **Yapay Zekâ Eğitimi ve Danışmanlık — AI okuryazarlığı ve otomasyona hazırlık** konusu. CSV/stock önceki gün örnekleri yeni konu olarak kullanılmadı. Gerçek müşteri veya ürün demosu YOK. GitHub main/site, LinkedIn ve Instagram için yeni eylem onayı gerekir; hesap/ödeme/DM/uygulama YOK.
**Dayanak:** Kaynak denetimi 24.10.2026: main ca2a47a0c6cf22149a47b48b74c38c4a8a24cd96; hizmetler.html, surec-analizi.html, iletisim.html, assets/styles-v33.css, assets/js/synapse-measurement-v1.js, araclar/surecini-20-dakikada-haritala.html; önceki Gün14 SYNAPSE_V8_GUN_14_DEVIR.md (#39 arşiv dalı). Resmî: https://developers.google.com/analytics/devguides/collection/ga4/reference/events ; https://www.linkedin.com/help/linkedin/answer/a518909 ; https://developers.google.com/search/docs/crawling-indexing/links-crawlable
