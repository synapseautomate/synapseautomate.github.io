# QA TUR B — 23.10.2026 / Bağımsız tasarım, okunabilirlik, hukuk ve dönüşüm
| Konu | Gerçek kanıt | Durum |
|---|---|---|
| Türkçe ve hizmet sınırı | sektörler/hukuk: insan kararı; sentetik dört madde; hukuki yorum yok | PASS (iç metin) |
| İç prototip bağımsız Chromium | `python qa_local_dashboard.py` → **320/375/390/768/1024/1440 6/6 PASS**. Gerçek sayfa değil, salt okunur local HTML. 320/390/768/1440 PNG ve `QA_B_VIEWPORT.json` mevcut. | PASS (yerel) |
| 320px taşma/klavye | `scrollWidth<=viewport`, 1 H1, gerçek odak alan footer bağlantısı, tutarlı tipografi | PASS (yerel) |
| Gerçek site/cihaz | Safari, mobil iOS/Android, Lighthouse, site HTTP/canlı form ekranları | TEST EDİLEMEDİ |
| Veri gizliliği | gerçek kişisel veri yok; yalnız sentetik dört kısa madde; email/TCKN görünümü negatif testte blok; üçüncü taraf logo/font/ses yok | PASS (sentetik sınır) |
| Telif/marka | salt okunur dashboard özgün CSS, system font; yanlış logo/sosyal proof/ROI yok; sentetik etiket görünüyor | PASS |
| Sonucun yanıltıcılığı | keyword hit != geçerli sözleşme; `legal_conclusion:null`, M04 eşleşmez ama uzman incelemesi gerekli | PASS |
| Platform uygunluğu | Upwork kapsam dışı, LinkedIn Services panel BİLİNMİYOR; ücretsiz kaynak yalnız resmî şartıyla | PASS metin/karar; hesap TEST EDİLEMEDİ |
| CTA / gerçek inbound | mevcut `surec-analizi.html` aday, değişiklik yayınlanmadı; onay/teslim ve kaynak ölçümü yok | TASLAK PASS; gerçek FAIL/HOLD |
| Hukuki yorum ve fatura | veri rolü, uzman onayı, gerçek sözleşme, KVKK/satıcı/fatura teyidi | P0 AÇIK |
| Gün14 yayın yasağı | main merge, sosyal post, hesap aktivasyon, DM, ödeme YAPILMADI | PASS |
**Kusurlar:**
- **P0** gerçek hukuki hizmette avukat incelemesi, KVKK rol ve izinleri, belge gizliliği, satıcı/fatura/ödeme; gerçek platform tahsilat kanıtı YOK → kamuya 'ticari/çalışan ürün' olarak yayıma HAYIR.
- **P1** ürün/mobil canlı render ve event delivery bağımsız TEST EDİLEMEDİ; tek CTA varyantı canlı veri olmadan karar verilemez.
- **P2** salt okunur kanıt panosunun büyük tablo görünümü 320px'de yoğun; yatay viewport taşması yok ama gerçek sayfa değildir. Mobil öznel erişilebilirlik kullanıcı teyidi yok.
**Sonuç:** **TEKNİK yerel taslak = PASS; TİCARİ / KAMU YAYIN = HAYIR; GÜN14 CLOSED değil.**
