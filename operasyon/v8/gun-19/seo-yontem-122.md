# SYNAPSE Automate — V8 Gün 19 · 28.10.2026
**Konu:** Sesli Yapay Zekâ / Randevu, Çağrı Yönlendirme, İnsan Devri. **Bütçe:** 0 TL peşin. **Durum:** YALNIZ TASLAK; kamuya yayın ve dış temas YOK.
**Gerçek site hizmet kaynağı:** [hizmetler.html — #11](https://github.com/synapseautomate/synapseautomate.github.io/blob/b2db84e1db00e4acbf0a6882e66c4b55643a113d/hizmetler.html). Canlı telefon/CRM/demo kanıtı yok. 3 örnek kavramsal sentetiktir.
## Yöntem 122: Google Merchant Center
**Karar:** NO-GO
**Neden:** Bugünkü konu fiziksel ürün, onaylı katalog, vergi/checkout/stok/iadeli teslim değil; sesli AI kapsam hizmeti.
**Gerçek değişiklik:** Merchant Center, GTIN, feed, fiyat veya ürün satın alma düğmesi açılmadı. Tek CTA gönüllü kapsam talebi.
**Sorumlu:** SYNAPSE hesap sahibi (hesap uygunluğu), operatör (kaynak/SEO). **Yayın izni:** ONAY BEKLİYOR.

## Ana kaynak kontrol tablosu (main → draft)
| Yol | Önce title/H1 | Sonra | Canonical / robots / HTTP |
|---|---|---|---|
| index.html | Synapse Automate / Tekrarlayan işi otomatikleştirin | Değişmedi | Self canonical, canlı HTTP TEST_EDİLEMEDİ |
| hizmetler.html | Kurumsal hizmet listesi / hizmetler | #11 karta yeni doğal href eklendi | Mevcut canonical korunur, canlı HTTP TEST_EDİLEMEDİ |
| surec-analizi.html | Süreç Analizi İste / Önce doğru süreci seçin | Zorunlu FormSubmit aktarım onayı ve TEST FİYATI beyanı | Canlı HTTP TEST_EDİLEMEDİ |
| kanit/stok-farki-baglam-kontrolu.html | Fark var. Kayıp kesin mi? | Gün19 sesli AI için GÜNCELLENMEDİ; farklı hizmet | Self canonical, canlı HTTP TEST_EDİLEMEDİ |
| sitemap.xml | Eski sesli AI hedefi yok | Yeni sesli AI karar sayfası eklendi | Statik XML kaynakta PASS; canlı robots/200 TEST_EDİLEMEDİ |
| cozumler/sesli-yapay-zeka-randevu-insan-devri.html | YOK / YOK | Sesli Yapay Zekâ… / Randevu talebini anlayın… | Self canonical, index-follow, canlı HTTP TEST_EDİLEMEDİ |
## Teknik test
- Kaynak meta/H1/canonical/href: GitHub içerik API ile gözlendi; draft kaynak testleri çalıştırıldı.
- index/noindex/robots: kaynak düzeyinde incelendi; dış sunucu HTTP 200/404 ve Search Console durumu **TEST EDİLEMEDİ / BİLİNMİYOR**.
- Google İşletme Profili uygunluğu doğrulanmadan kayıt yapılamaz. Özellikle `LocalBusiness` adres şeması eklenmedi.

## Resmî kaynak ve denetim tarihi
- [Google İşletme Profili uygunluk](https://support.google.com/business/answer/13763036?hl=en) — 28.10.2026.
- [KVKK aydınlatma tebliği](https://www.kvkk.gov.tr/Icerik/4132/aydinlatma-yukumlulugunun-yerine-getirilmesinde-uyulacak-usul-ve-esaslar-hakkinda-teblig) — 28.10.2026.
- [Google canonical](https://developers.google.com/search/docs/crawling-indexing/canonicalization) ve [taranabilir bağlantılar](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) — 28.10.2026.
- GitHub kaynak revizyonu: `main b2db84e1db00e4acbf0a6882e66c4b55643a113d`; [Gün19 draft PR #49](https://github.com/synapseautomate/synapseautomate.github.io/pull/49).
