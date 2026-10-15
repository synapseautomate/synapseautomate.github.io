# V8 / Gün 07 — zorunlu devir ve karar kaydı
Tarih: 2026-10-15 (PDF plan tarihi: 20.10.2026). **DURUM: İÇ HAZIRLIK TAMAM; KAMUSAL YAYIN BLOKE.** Bu dosya PDF'de istenen tam adla kaydedilmiştir.

## 03–06 birleşik kanıt
- Gün 03: iki CSV sözleşmesi, R01–R05 ve sentetik kabul testleri; arşiv kanıtı yerel teslim paketindedir. Gün 04–05: 25/25 yerel test PASS (önceki QA paketi). Bu satırlar canlı kullanıcı testi değildir.
- Gün 06: [ödeme/hukuk matrisi](../gun-06/SYNAPSE_V8_GUN_06_DEVIR.md); hesap/fatura durumu doğrulanmadı. Kullanıcı IBAN üzerinden teklif sonrası ödeme planını beyan etti; **IBAN hukuki/fatura yükümlülüğünü kaldırmaz**. Kullanıcı mevcut iletişim bağlantılarının doğru yönlendirdiğini teyit etti; canlı otomatik HTTP kontrolü ayrıca yapılmadı.
- **Ürün:** Sentetik yerel demo test edilmiş, canlı ticari teslimat doğrulanmadı.
- **Ödeme:** Entegrasyon planlanmıyor, IBAN teklif sonrası. Ödeme sağlayıcısı doğrulanmadı; ödeme testi yok.
- **Hukuki:** Bilinmiyor, P0.
- **Trafik ölçümü:** Bilinmiyor, canlı GA4/çerez testi yok.

## Öncelik matrisi
| Kimlik | Seviye | Durum | Kapatma kanıtı |
|---|---|---|---|
| LEGAL-01 | P0 | Açık | Kullanıcının şirket/fatura beyanı ve gerekirse GİB/müşavir görüşü |
| HOST-01 | P0 | Açık | GitHub Pages kullanım şartlarına uygun yayın/alternatif barındırma kararı |
| MOBILE-01 | P1 | Açık | Gerçek Safari cihaz ekran/klavye kontrolü |
| PRIVACY-01 | P1 | Açık | Gerçek sunucu üzerinden KVKK/GA4/çerez ağı denetimi |
| LINK-01 | P1 | Açık | PR sonrası canlı HTTP/404 ve tüm link hedeflerinin doğrulanması |
| SOCIAL-01 | P1 | Açık | LinkedIn görsel panel kırpma ve gerçek yayın önizlemesi |

**Kritik kusur sıfır mı? HAYIR. Yayına hazır mı? HAYIR.** Bilgi sayfası yalnız branch/PR içinde. Kırık bağlantı olmadığını iddia etmiyoruz; yerel relative path mantığı ayrıca gözden geçirildi. Canlı öncesi/sonrası ekran seti henüz yok, çünkü onaylı canlı sürüm yok. Yerel Chromium altı genişlik görüntüsü: 320, 375, 390, 768, 1024, 1440 px (önceki teslim arşivinde). Bu gerçek Safari değildir.

## Geri alma
PR #22 taslaktır, merge yok. Onaylı merge olursa SHA ve ekran setini kaydet; hata halinde merge commit revert PR'si aç; önceki çalışan sürüme dön; ardından HTTP ve ekran QA tekrarla. Revert provası yapılmadı.

## Ayrı yayın eylemleri
| Onay kodu | Eylem | Kapsam | Durum |
|---|---|---|---|
| WEB-G07-01 | PR #22 içindeki bilgi/demoyu ana dala birleştirmek | https://github.com/synapseautomate/synapseautomate.github.io/pull/22 | **ONAY YOK** |
| LI-G07-01 | LinkedIn metnini paylaşmak | [taslak](LINKEDIN_ONAY_TASLAGI.md) | **ONAY YOK** |
| LI-G07-02 | LinkedIn görselini paylaşmak | 1080×1350 formatlı, sentetik kanıt etiketli görsel | **ONAY YOK** |

**Yayın URL'si: YOK. LinkedIn gönderi URL'si: YOK.** Kullanıcının “çalış” talimatı, yayın onayı olarak yorumlanmaz.

## İki QA turu
1. Teknik: Altı yerel Chromium viewport testi PASS; canlı 404/GA4/Safari testi BLOCKED. Bilgi sayfasında ödeme/checkout yok.
2. Editoryal: Yanlış müşteri/satış/fiyat vaadi yok; sentetik veri açık. İddia denetimi PASS. Sosyal panel/görsel son önizleme BLOCKED.

Metrik kaynakları: önceki Gün 04–05 yerel test raporu; PR #22 commit kayıtları; kullanıcının iletişim/IBAN beyanı. SHA: PR #22 HEAD GitHub'dan yeniden okunmalı; tekil sabit SHA'yı yanlış güncel göstermemek için burada dondurulmadı. Yapılmayanlar: merge, yayın, gerçek ödeme, gerçek Safari, GA4/çerez ve canlı HTTP testleri. 
