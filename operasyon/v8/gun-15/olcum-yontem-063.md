# 063 — İçerik deneyi, algoritma efsanesi değil
**Hipotez:** AI eğitim kartındaki somut bir sonraki adım linki, uygun operasyon yöneticisinin gönüllü süreç analizi talebini açıklık nedeniyle artırabilir; sonuç değil sınanacak beklenti.
| Olay | Anlamı | Kaynak | Güven |
|---|---|---|---|
| `asset_view` | Sayfa göründü; nitelikli talep değildir | mevcut JS | consent/tarayıcı teyitsiz |
| `cta_click` (taslak) | Eğitim kartının linki tıklandı; siteye eklenmiş olay değil | yalnız örnek event sözlüğü | BİLİNMİYOR |
| `lead_form_submit` | Form gönderme denemesi; teslim kanıtı değil | mevcut JS | izin/teslim teyitsiz |
| `generate_lead` | Teşekkür redirect+önceki session eşleşti; e-posta teslimi hâlâ ayrıca teyit | JS | panel yok |
**Örnek test URL:** `https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html?utm_source=site&utm_medium=organic&utm_campaign=ai_readiness_g15`. **Örnek payload:** `{"event":"cta_click","cta_id":"ai_egitim_readiness","page_path":"/hizmetler.html","consent":"granted_only"}` (sentetik; gönderim yok).
**Ana metrik:** izinli ve panelde doğrulanmış, nitelikli CTA→gönüllü talep oranı. Gerçek pay/payda yok; hesaplanmaz. Rıza reddinde GA4 gönderme; kişisel veri/ham prompt kaydetme. **Rollback:** karttaki tek `<a>` öğesini kaldır.

**Konu ve sınırlar (24.10.2026):** Kullanıcı öncelikli güncellemesi: **Yapay Zekâ Eğitimi ve Danışmanlık / AI okuryazarlığı ve otomasyona hazırlık**. Önceki CSV stok örneğini yeni gönderi diye çoğaltma. Site main `ca2a47a0c6cf22149a47b48b74c38c4a8a24cd96`; `hizmetler.html`, `araclar/surecini-20-dakikada-haritala.html`, `surec-analizi.html`, `iletisim.html`, `assets/js/synapse-measurement-v1.js` gerçekten okundu. Gerçek talep/GA4/LinkedIn paneli BİLİNMİYOR. Taslak dal dışına eylem YOK. **Sorumlu:** SYNAPSE operasyon + hesap sahibi; **izin:** WEB-G15-TEK-CTA-20261024 ayrıca gerekli.
