# Gün 01 blokaj ve öncelik kayıtları
**Tarih:** 2026-10-13 | **Sahip:** SYNAPSE hesap sahibi | **Denetleyen:** AI operatörü
**Referans:** https://github.com/synapseautomate/synapseautomate.github.io/pull/10

## Satışa/yayına çıkışı durduran dört P0
- **P0-01 — Nihai ticari ürün/kabul:** Sentetik CSV prototipi ve örnek rapor var; ticari ürün dosyası, kapsam kabulü, sorumluluk sınırları ve müşteri teslim teyidi yok. **Sahip:** operatör ve hesap sahibi. **Önlem:** Gün 02–05 ürün/şema ve QA kapıları. Kanıt: `operasyon/b2b/csv_kontrol.py`, `operasyon/b2b/07-sentetik-qa-ve-rapor.md` (taslak PR).
- **P0-02 — Hukuki/fatura:** Şirket ve fatura düzenleme imkânı kullanıcı beyanına göre yok. Sözleşme, vergi, veri işleme, KYC ve yükümlülükler uygunluk bakımından açık. **Sahip:** hesap sahibi/mali müşavir. **Önlem:** Ticari teklif ve tahsilat yalnız onaylı uygunluk sonrası. Kanıt: `kurulus-durumu-ve-b2b-hazirlik.md`.
- **P0-03 — Tahsilat:** Hiçbir uçtan uca checkout/ödeme kanıtı yok. FormSubmit müşteri keşif formudur. **Sahip:** hesap sahibi. **Önlem:** Gün 06–07 ödeme koşulları ve güvenli doğrulama. Kanıt: https://synapseautomate.github.io/surec-analizi.html
- **P0-04 — Teslim ve kabul:** Dijital dosya otomatik teslimi veya imzalı B2B kabul akışı kanıtı yok. **Sahip:** operatör/hesap sahibi. **Önlem:** Ürün/kurulum teslim ve kabul tutanağı taslağı; canlı test ayrıca onaylı. Kanıt: `operasyon/b2b/01-hizmet-paketi.md`.

## P1 / P2
- **P1-01 — GA4 çerez rızası:** Mevcut ölçüm betiği doğrudan GA4 çağırıyor; uygun opt-in kapısı kaynakta görünmüyor. Tarayıcı çerez davranışı test edilmedi. **Sahip:** teknik operatör; yayın onayı hesap sahibinde. Kaynak: https://github.com/synapseautomate/synapseautomate.github.io/blob/main/assets/js/synapse-measurement-v1.js ; resmî KVKK: https://www.kvkk.gov.tr/Icerik/8884/2024-1361
- **P1-02 — Gerçek mobil/a11y/bağlantı testi:** Yerel rapor 6 genişlikte QA'dan geçti; canlı site 6 viewport, klavye ve tüm HTTP linkleri test edilemedi. **Sahip:** teknik operatör. Kaynak: `KANIT_VE_QA_MATRISI.md`.
- **P1-03 — Metrik kaynağı yok:** GA4, LinkedIn, ödeme/satış paneli okunamadı. Bilinmeyen ≠ 0. **Sahip:** hesap sahibi.
- **P2-01 — Marka tokenları:** Farklı sayfalarda renk tokenları uyumu iyileştirilebilir; P0/P1 giderilmeden kozmetik yayın yapılmaz.
- **P2-02 — Logo hakları:** Marka logosunun hak sahipliği/onay kaydı bağımsız teyit bekliyor.

**Karar:** Bu engellerin varlığı Gün 01 *tespit raporu* kapanışını engellemez; ödeme, ürün yayınlama ve ticari satış kapılarını açık tutar. Açık P0 sayısı: **4** (operasyonel sınıflandırma; bunlar giderildi iddiası yok).
