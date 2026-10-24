# 174 — Aynı hazırlık bilgisinin üç farklı sunumu (post A/B DEĞİL)
**Tek ham bilgi:** AI için veri izni, tanımlı süreç, insan kararı ve ölçüm mekanizması gerekir (çalışma çerçevesi; kesin kural değil).
| Paket | Açılış | Ne zaman uygun |
|---|---|---|
| Problem | “Ekibiniz AI kullanmak istiyor; önce hangi işi seçeceğini biliyor mu?” | alıcı problemi belirsiz |
| Kanıt | “Bu dört karar kartında hangi satır boş kalıyor?” | gerçek sentetik karar görseli varsa |
| Karar | “Önce eğitim mi, süreç haritası mı, sınırlı deneme mi?” | karar rolü net ise |
**Bugünkü site CTA testi bunlar değildir:** bu üç başlık çevrim içi test edilmedi. Tek değişken linkin varlığıdır; aynı anda üçünün yayını A/B değildir.
**Önerilen olay/URL:** `asset_view` + izinli `cta_click`, `?utm_source=site&utm_medium=organic&utm_campaign=ai_readiness_g15`.
**Örnek payload:** `{"event":"content_variant_view","variant":"decision","synthetic":true}` sadece dokümantasyon. Rıza, gerçek panel, karıştırıcı dönem, tek CTA rollback saklı.

**Konu ve sınırlar (24.10.2026):** Kullanıcı öncelikli güncellemesi: **Yapay Zekâ Eğitimi ve Danışmanlık / AI okuryazarlığı ve otomasyona hazırlık**. Önceki CSV stok örneğini yeni gönderi diye çoğaltma. Site main `ca2a47a0c6cf22149a47b48b74c38c4a8a24cd96`; `hizmetler.html`, `araclar/surecini-20-dakikada-haritala.html`, `surec-analizi.html`, `iletisim.html`, `assets/js/synapse-measurement-v1.js` gerçekten okundu. Gerçek talep/GA4/LinkedIn paneli BİLİNMİYOR. Taslak dal dışına eylem YOK. **Sorumlu:** SYNAPSE operasyon + hesap sahibi; **izin:** WEB-G15-TEK-CTA-20261024 ayrıca gerekli.
