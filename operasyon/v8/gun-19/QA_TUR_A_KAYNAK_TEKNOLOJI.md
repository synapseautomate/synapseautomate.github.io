# QA A — Kaynak, negatif akış, ölçüm, gizlilik
Date: 28.10.2026 · Repo main SHA `b2db84e1db00e4acbf0a6882e66c4b55643a113d` · PR #49 DRAFT.
1. Gerçek hizmet #11: “Sesli Yapay Zekâ ve Çağrı Merkezi — Sesli asistan, çağrı merkezi otomasyonu, sipariş ve randevu akışları.” **PASS** kaynak. Çalışan bot delili: **BİLİNMİYOR / gösterilmiyor**.
2. Kavramsal örneklerde gerçek müşteri, ses kaydı, canlı takvim, CRM, satın alma, otomatik rezervasyon yok. **PASS** metin kontrolü.
3. Sesli AI hizmet kartı href → taslak yeni sayfa; tek gönüllü CTA → iletişim formu ve konu preselect. **PASS** kod / lokal gerçek Chromium 42/42 ilk tur.
4. Genel süreç formunda FormSubmit aktarım için zorunlu checkbox taslak olarak eklendi. **PASS** kaynak ve otomasyon validasyon özelliği; gerçek teslim YAPILMADI.
5. Eski ticari listelerde satışa hazır görünüm riski: genel süreç sayfasında test fiyat etiketi ve JSON-LD Offer kaldırıldı. Diğer site fiyatları bütünsel P1/P0 kontrolü bekliyor.
6. 6 viewport × 7 rota = **42/42 PASS**; komut: `python scripts/v8_gun19_browser_qa.py` GitHub Actions iş logu [40659256869](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659256869). Test yalnız yerel PR checkout Chromium; canlı siteye POST yok.
7. 01–18 devir kapsamı: main'de Gün11 devir dosyası doğrulandı; Gün18 draft #47 devri okundu; Gün16–17 önceki taslak içerik bilgileri mevcut. Diğerleri main'de bulunmadı; eksik kaydedildi.
8. Ölçüm: gerçek trafik/satış/lead/inbox/GA4/Search Console BİLİNMİYOR; negatif gerçek test POST 0 (gönderim yok).
**Karar:** Bu tur kaynak açısından belirli kontroller PASS; ticari yayın ve gerçek sesli bot iddiaları HOLD.


## 28.10.2026 kaynak güncellemesi — CI ve HTTP doğrulaması
- GÜNCEL ve üstün kanıt: GitHub Actions [run 40659965759](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759); [artifact 12802534718](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759/artifacts/12802534718). Gerçek **salt-okunur HTTPS GET main**: ana sayfa, hizmetler, surec-analizi, iletisim, talep-alindi ve 404.html 6/6 **HTTP 200**; bulunmayan URL **404**; **YENİ taslak sesli AI URL canlıda 404 (beklenen)**. Bu testler gerçek FormSubmit POST veya checkout değildir.
- İki sürümden Chromium gerçek render: main-before ↔ draft-after `hizmetler.html` ve `surec-analizi.html`, 320/390/768/1440, **16 gerçek PNG** ve `before-after-summary.json`.
- [Commit e295052](https://github.com/synapseautomate/synapseautomate.github.io/commit/e295052a9476ac433afa828dbc46f48661ca9c6e) sonrası bağımsız CI workflow'ları: Site Integrity, Commercial SEO, Finance SEO, Day12 HR ve **Synapse Release Preflight = SUCCESS**, Gün19 Browser QA = SUCCESS. Önceki Release Preflight FAIL gerçek regresyondu, sonra yerel sentetik consent işaretlemesiyle düzeltildi; gerçek kullanıcı POST'u yok.
- Gün19 canlı yeni sayfa yayımlanmadı. Form başarı/inbox, canlı draft sayfa 200, gerçek Safari ve ödeme hâlâ **TEST EDİLEMEDİ / HOLD**.
