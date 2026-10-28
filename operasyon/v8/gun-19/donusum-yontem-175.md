# SYNAPSE Automate — V8 Gün 19 · 28.10.2026
**Konu:** Sesli Yapay Zekâ / Randevu, Çağrı Yönlendirme, İnsan Devri. **Bütçe:** 0 TL peşin. **Durum:** YALNIZ TASLAK; kamuya yayın ve dış temas YOK.
**Gerçek site hizmet kaynağı:** [hizmetler.html — #11](https://github.com/synapseautomate/synapseautomate.github.io/blob/b2db84e1db00e4acbf0a6882e66c4b55643a113d/hizmetler.html). Canlı telefon/CRM/demo kanıtı yok. 3 örnek kavramsal sentetiktir.
## Yöntem 175 — Kullanıcı yolculuğu ve karar engelinin giderilmesi
**Alıcı:** Çağrı merkezi operasyon yöneticisi. **Tek soru:** “Asistan randevuyu ne zaman insana devretmeli?”
**Önce:** `hizmetler.html` #11 sesli AI kartı yalnız iki cümle; konuya özgü kapsam, kaynak ve rıza rotası yok.
**Sonra (taslak):** #11 → `cozumler/sesli-yapay-zeka-randevu-insan-devri.html` üç sentetik karar → tek `/iletisim.html?konu=sesli-yapay-zeka` CTA → form otomatik konu seçimi → zorunlu rıza → **gerçek form teslimi doğrulanmadı**.
**Form kıyası:** `surec-analizi.html` öncesi aktarıma dair zorunlu consent yok; draft ile eklendi. `iletisim.html` hâlihazırda rıza içeriyordu. Gerçek müşteri verisi, telefon numarası, kayıt veya çağrı dökümü toplanmadı.
| Viewport | Browser kaynağı | CTA / input | Sonuç |
|---|---|---|---|
| 320, 375, 390, 768, 1024, 1440 | GitHub Actions Chromium (localhost PR checkout) | Link + konu seçimi + consent | 42/42 kaynak kontrol PASS (ilk otomasyon turu) |
**Dış sınırlar:** gerçek Safari TEST_EDİLEMEDİ; HTTP 200 canlı TEST_EDİLEMEDİ; FormSubmit kutusu ve başarı sayfası gerçek teslim için TEST_EDİLEMEDİ. Yanlış müşteri/fiyat/test değeri kullanılmadı.

## Resmî kaynak ve denetim tarihi
- [Google İşletme Profili uygunluk](https://support.google.com/business/answer/13763036?hl=en) — 28.10.2026.
- [KVKK aydınlatma tebliği](https://www.kvkk.gov.tr/Icerik/4132/aydinlatma-yukumlulugunun-yerine-getirilmesinde-uyulacak-usul-ve-esaslar-hakkinda-teblig) — 28.10.2026.
- [Google canonical](https://developers.google.com/search/docs/crawling-indexing/canonicalization) ve [taranabilir bağlantılar](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) — 28.10.2026.
- GitHub kaynak revizyonu: `main b2db84e1db00e4acbf0a6882e66c4b55643a113d`; [Gün19 draft PR #49](https://github.com/synapseautomate/synapseautomate.github.io/pull/49).
