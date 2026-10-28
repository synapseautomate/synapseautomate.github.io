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


## 28.10.2026 kaynak güncellemesi — CI ve HTTP doğrulaması
- GÜNCEL ve üstün kanıt: GitHub Actions [run 40659965759](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759); [artifact 12802534718](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759/artifacts/12802534718). Gerçek **salt-okunur HTTPS GET main**: ana sayfa, hizmetler, surec-analizi, iletisim, talep-alindi ve 404.html 6/6 **HTTP 200**; bulunmayan URL **404**; **YENİ taslak sesli AI URL canlıda 404 (beklenen)**. Bu testler gerçek FormSubmit POST veya checkout değildir.
- İki sürümden Chromium gerçek render: main-before ↔ draft-after `hizmetler.html` ve `surec-analizi.html`, 320/390/768/1440, **16 gerçek PNG** ve `before-after-summary.json`.
- [Commit e295052](https://github.com/synapseautomate/synapseautomate.github.io/commit/e295052a9476ac433afa828dbc46f48661ca9c6e) sonrası bağımsız CI workflow'ları: Site Integrity, Commercial SEO, Finance SEO, Day12 HR ve **Synapse Release Preflight = SUCCESS**, Gün19 Browser QA = SUCCESS. Önceki Release Preflight FAIL gerçek regresyondu, sonra yerel sentetik consent işaretlemesiyle düzeltildi; gerçek kullanıcı POST'u yok.
- Gün19 canlı yeni sayfa yayımlanmadı. Form başarı/inbox, canlı draft sayfa 200, gerçek Safari ve ödeme hâlâ **TEST EDİLEMEDİ / HOLD**.
