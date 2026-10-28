# Gün19 — kaynaklı metrikler ve ayrı yetki kapıları
Tarih: 28.10.2026 Europe/Istanbul (plan 01.11.2026).
| Kanal | Metrik/tanım | Değer | Birim | Kaynak / kanıt güveni |
|---|---|---|---|---|
| Lokal PR Chromium | viewport_pass (6×7) | 42 | kontrol | GitHub Actions run 40659256869 / yüksek |
| Lokal PR Chromium | ekran kanıtı | 42 | PNG | Artifact 12803231704 / yüksek |
| Lokal PR Chromium | gözlenen JS pageerror | 0 | hata | Test betiği / test aralığıyla sınırlı |
| GitHub kaynak | yeni hizmet href | 1 | bağlantı | Draft PR #49 / yüksek |
| GitHub kaynak | zorunlu consent eklemesi | 1 | alan | Draft PR #49 / yüksek |
| Canlı web | canlı 200/404 | BİLİNMİYOR | durum | Ortam HTTP kapalı; Actions read-only test ekli |
| Canlı web | kırık kritik link adedi | BİLİNMİYOR | link | Canlı bağımsız doğrulama yok |
| Gerçek FormSubmit | form_basari_kaynagi | BİLİNMİYOR | onay | Kullanıcı hesabına erişim yok; POST yok |
| Gerçek Safari | safari_durumu | TEST_EDİLEMEDİ | motor | Chromium ≠ Safari |
| Analitik | kanal gösterimi/nitelikli ziyaret | BİLİNMİYOR | gösterim/oturum | GA4 paneli yok |
| Funnel | gönüllü talep/izinli teklif | BİLİNMİYOR | lead/teklif | Gerçek panel yok |
| Satış | fonlanmış sipariş/tahsil edilmiş satış/iade/net gelir | BİLİNMİYOR | sipariş/TL | Finansal kaynak yok |
| Operasyon | bu oturum dış gönderim/ödeme | 0 | eylem/TL | Operatör işlem günlüğü |

## ONAY BEKLİYOR (ayrı yetkiler)
- `WEB-G19-20261028`: PR #49'in **main'e merge / canlı yayın** izni. Henüz verilmedi; kullanıcı yalnız Gün18 için yayın izni vermişti.
- `LI-G19-20261028`, `YT-G19-20261028`, `IG-G19-20261028`, `X-G19-20261028`, `TT-G19-20261028`, `FB-G19-20261028`, `TH-G19-20261028`, `PIN-G19-20261028`, `BS-G19-20261028`: sosyal paylaşımların her biri ayrı açık onay ister; bugünkü politika **SOSYAL YAYIN YOK**.
- `FORM-G19-20261028`: Gerçek test başvurusu ve alıcı inbox teslim kontrolü (kişisel veri/hukuk incelemesi sonrası); henüz izin yok.
- `CHECKOUT-G19-20261028`: Gerçek ödeme/tahsilat; **AÇILMADI**, vergi/fatura/KYC/mesafeli satış ispatı gerekir.
- Google Business Profile, yerel dizin, Merchant Center, Snapchat, harita hesap oluşturma: NO-GO; hesap sahibinin resmî uygunluk kanıtı olmadan açılmaz.


## 28.10.2026 kaynak güncellemesi — CI ve HTTP doğrulaması
- GÜNCEL ve üstün kanıt: GitHub Actions [run 40659965759](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759); [artifact 12802534718](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759/artifacts/12802534718). Gerçek **salt-okunur HTTPS GET main**: ana sayfa, hizmetler, surec-analizi, iletisim, talep-alindi ve 404.html 6/6 **HTTP 200**; bulunmayan URL **404**; **YENİ taslak sesli AI URL canlıda 404 (beklenen)**. Bu testler gerçek FormSubmit POST veya checkout değildir.
- İki sürümden Chromium gerçek render: main-before ↔ draft-after `hizmetler.html` ve `surec-analizi.html`, 320/390/768/1440, **16 gerçek PNG** ve `before-after-summary.json`.
- [Commit e295052](https://github.com/synapseautomate/synapseautomate.github.io/commit/e295052a9476ac433afa828dbc46f48661ca9c6e) sonrası bağımsız CI workflow'ları: Site Integrity, Commercial SEO, Finance SEO, Day12 HR ve **Synapse Release Preflight = SUCCESS**, Gün19 Browser QA = SUCCESS. Önceki Release Preflight FAIL gerçek regresyondu, sonra yerel sentetik consent işaretlemesiyle düzeltildi; gerçek kullanıcı POST'u yok.
- Gün19 canlı yeni sayfa yayımlanmadı. Form başarı/inbox, canlı draft sayfa 200, gerçek Safari ve ödeme hâlâ **TEST EDİLEMEDİ / HOLD**.
