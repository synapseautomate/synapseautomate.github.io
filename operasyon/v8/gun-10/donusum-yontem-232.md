# Gün 10 — Yöntem 232: İyi lead ve tek CTA karar engeli

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Tek hedef alıcı: satış operasyonları yöneticisi. Tek sorun: onaylanan teklifin CRM kaydı için sürüm/onay/sorumlu/tarih devir bilgisinin belirlenmemesi.

2. Uygunluk ölçütü (3–5): gerçek teklif-takip ihtiyacı; hizmet verilebilir B2B kapsam; yetkili süreç muhatabı; iletişim isteği; kapsam üzerinde ortak karar. Bütçe/uygunluk yalnız alıcı gönüllü beyanıyla değerlendirilebilir.

3. İnsan değerlendirmesi: UYGUN / BELİRSİZ / KAPSAM DIŞI. Korunan/kişisel özelliklere göre skor oluşturma YOK.

4. Önce CTA: `Süreç Analizi İste`; yeni kamuya açık sayfada kullanılacak metin: `Analiz yaklaşımını incele` → mevcut ayrı `cozumler/musteri-talebi-surec-analizi.html` (formu doğrudan göndermeden sınırları açıklar).

5. Bir değişkenli gelecekteki hipotez: ana sayfa kart başlığında `Teklif onaylandı. CRM devir kaydı hazır mı?` ile genel `Müşteri takibi` başlığını karşılaştır; güncel PR #28 aday başlığı zaten içerir, kontrollü deney başlatılmadı.

6. CTA ve erişilebilirlik: staged Chromium 320/375/390/768/1024/1440 koşulları PASS; canlı Safari, ekran okuyucu, FormSubmit gerçek teslim TEST_EDİLEMEDİ.

7. Bu sayfa çalışan ürün, gerçek CRM entegrasyonu, müşteri referansı veya kesin fiyat taahhüdü içermez; ana sitenin diğer fiyatlarının doğruluğu ayrıca ticari kapıda kalır.

## Kabul ve iki bağımsız QA turu

| Kabul kontrolü | QA A (kaynak/kod) | QA B (hukuk/tasarım/canlı) |
|---|---|---|
| PDF yöntem ilkesini ayrı dosyaya yazma | GEÇTİ / kaynak eşlemesi | GEÇTİ / iç metin |
| Konu tekrarını önleme | GEÇTİ: CRM devir | GEÇTİ: CSV/stok değil |
| Panelden gerçek sonuç | TEST_EDİLEMEDİ | TEST_EDİLEMEDİ |
| Rıza, ödeme, FormSubmit gerçek teslim | KOD/CI koşullu PASS | P0 AÇIK: hukuk, üretim, teslim |
| Kamuya aktarım | TASLAK | ONAY verilmiş site güncellemesi bile canlı yayıma bağlı QA koşullu |

Önce/sonra CTA, 320/390/768/1440 staged kontrol ve gerçek POST yapmama sınırı açıkça belirtilmiştir. Yayınlanmış sonuç raporu YOK.

## Geri alma / sahibine devir

Gerçek rızaya aykırı trafik, yanlış kaynak, çift lead veya bozuk CTA saptanırsa kamu eylemi durur; onaylı eski commit'e geri alma PR'si hazırlanır. **Veri yoksa 0 yazılmaz.** Gün11–14'te ancak erişim/kanıt varsa gerçek ölçümle güncellenir.
