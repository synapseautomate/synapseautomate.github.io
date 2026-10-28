# Gün19 | Form, 404, CTA, üçüncü taraf bağlantılar
**28.10.2026**, kaynak: GitHub `main` ve draft #49.
| Yol / alan | Kaynak bulgu | Test / gerçek statü |
|---|---|---|
| index → hizmetler | href yerinde | GitHub kaynak PASS, canlı HTTP TEST EDİLEMEDİ |
| hizmetler #11 → sesli AI | main'de eksik, draftta eklendi | Chromium lokal 6/6 PASS |
| sesli AI → iletişim | `/iletisim.html?konu=sesli-yapay-zeka` | Chromium lokal 6/6 PASS |
| İletişim `#konu` | draftta otomatik sesli AI seçimi | Chromium lokal 6/6 PASS |
| İletişim `form#contact-form` | https://formsubmit.co/synapseautomate.ai@gmail.com | Kaynak/browser target PASS, gerçek POST YAPILMADI |
| Süreç analizi formu | FormSubmit / zorunlu consent | DRAFT browser 6/6 PASS |
| `_next` | surec-analizi `talep-alindi.html?submitted=process_analysis`; iletişim `talep-alindi.html` | Kaynak PASS; gerçek redirect ve inbox TEST EDİLEMEDİ |
| Kasıtlı olmayan URL | Statik site 404.html kaynağı var | Canlı 404 HTTP TEST EDİLEMEDİ, ayrı salt-okunur HTTP scripti yazıldı |
| `mailto`, `tel`, `wa.me` | iletisim.html kaynakta var | Dış tıklama / mesaj / arama YAPILMADI |
| GA4 | `assets/js/synapse-measurement-v1.js` localStorage consent kontrol kodu içeriyor | Kaynak var, gerçek ağ consent/GA4 panel TEST EDİLEMEDİ |
| Gizlilik | `gizlilik.html` ve temas formu onayı | Kaynak PASS, hukuki yeterlilik dış teyit bekliyor |
| Fiyat→checkout→teslim | Etkin checkout/ödeme uygunluğu kanıtı yok | NO-GO, gerçek para hareketi YOK |
**İlk istek hatası:** canlı HTTP karşılığı bu oturumda alınamadığı için BİLİNMİYOR. Lokal Chromium QA tarayıcı JS exception: ilk otomasyon turunda 0 gözlenen, tam canlı JS güvence değildir. **Kırık kritik link:** lokal denetimde 0 tespit; canlı adet BİLİNMİYOR.
