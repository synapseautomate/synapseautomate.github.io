# 088 — İçerik performansı altı aşamalı teşhis
| Aşama | AI eğitim senaryosunda soru | Gerçek kanıt olmadan karar |
|---|---|---|
| A Dağıtım yok | GSC'de eğitim/hazırlık niyeti sorgusu var mı, sayfa indeksli mi? | BİLİNMİYOR |
| B Görülüyor seçilmiyor | Hizmet adı hedef role karar sorusu olarak net mi? | Nitel kullanıcı testi gerekir |
| C Seçiliyor terk ediliyor | Matris ilk ekranda gerçek faydayı açıklıyor mu? | Davranış verisi yok |
| D Fayda var paylaşılmıyor | Karar tablosu ekibe taşınabilir mi? | LinkedIn save paneli yok |
| E Trafik var talep yok | Tek CTA yanlış sayfaya mı gidiyor; kullanıcı niyet uyumu? | GitHub hedef var; HTTP teyitsiz |
| F Talep var müşteri yok | Çözüme/teslime yetki, fiyat, uygunluk ve yanıt süresi mi? | Gerçek alıcı yok |
**Olay sözlüğü:** `asset_view` ≠ `lead_form_submit` ≠ `generate_lead` ≠ fonlanmış teklif ≠ banka tahsilatı.
**Test URL/payload:** örnek `?utm_source=site&utm_medium=organic&utm_campaign=ai_readiness_g15`; `{"page_path":"/hizmetler.html","event":"asset_view"}` sentetik.
**Gizlilik:** consent yoksa GA4 ölçümü yok; IP/kimlik/öğrenci veya kurumsal sır toplanmaz. **Rollback:** tek CTA'yı geri al; metrik gerçekliği yenilenmeden kategori değişikliği yapma.

**Konu ve sınırlar (24.10.2026):** Kullanıcı öncelikli güncellemesi: **Yapay Zekâ Eğitimi ve Danışmanlık / AI okuryazarlığı ve otomasyona hazırlık**. Önceki CSV stok örneğini yeni gönderi diye çoğaltma. Site main `ca2a47a0c6cf22149a47b48b74c38c4a8a24cd96`; `hizmetler.html`, `araclar/surecini-20-dakikada-haritala.html`, `surec-analizi.html`, `iletisim.html`, `assets/js/synapse-measurement-v1.js` gerçekten okundu. Gerçek talep/GA4/LinkedIn paneli BİLİNMİYOR. Taslak dal dışına eylem YOK. **Sorumlu:** SYNAPSE operasyon + hesap sahibi; **izin:** WEB-G15-TEK-CTA-20261024 ayrıca gerekli.
