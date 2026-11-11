# Gün 10 — Yöntem 147: Gösterişten iş metriğine büyüme ağacı

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Tek üst karar göstergesi: **kaynağı ve insan uygunluk değerlendirmesi teyitli fırsat sayısı**; gösterimler ayrı kanallarda kendi tanımıyla saklanır.

2. Keşif (gösterim) → dikkat (tıklama/kaydetme) → güven (hizmet sayfasını inceleme) → eylem (gönüllü form/posta) → müşteri (gerçek tahsil edilmiş satış) → devam (doğrulanmış tavsiye).

3. CTA görüntüleme = lead değildir. Form `lead_form_submit` = gönderim girişimi, `generate_lead` = işaretli yönlendirme; gerçek e-posta teslimi yoksa nitelikli talep BİLİNMİYOR.

4. Hiçbir platformun gösterimini diğerine ekleyip toplam tekil kişi yazma. Aynı alıcı birden çok mesaj bırakırsa izinli anonim tekilleştirme kuralıyla değerlendir; bugünkü gerçek kişi bazlı kayıt yok.

5. `<30` kanıtlı ilgili ziyaret eşiğinde ürün/mesaj başarısızlığı kararı verilmez. Düşük sayıda yalnız mutlak sayı ve nitel soru yazılır.

6. Karar matrisinde yüksek gösterim/yetersiz tıklama -> başlık, nitelikli ziyaret var/demo yok -> kanıt, demo var/inbound yok -> CTA, nitelikli inbound var/sipariş yok -> hukuki/teklif kalite kontrolü; bu eşikler örnek, gerçek veri değil.

7. Statü: tanımlar PASS; paneller BİLİNMİYOR, gerçek funnel oranları HESAPLANAMAZ.

## Kabul ve iki bağımsız QA turu

| Kabul kontrolü | QA A (kaynak/kod) | QA B (hukuk/tasarım/canlı) |
|---|---|---|
| PDF yöntem ilkesini ayrı dosyaya yazma | GEÇTİ / kaynak eşlemesi | GEÇTİ / iç metin |
| Konu tekrarını önleme | GEÇTİ: CRM devir | GEÇTİ: CSV/stok değil |
| Panelden gerçek sonuç | TEST_EDİLEMEDİ | TEST_EDİLEMEDİ |
| Rıza, ödeme, FormSubmit gerçek teslim | KOD/CI koşullu PASS | P0 AÇIK: hukuk, üretim, teslim |
| Kamuya aktarım | TASLAK | ONAY verilmiş site güncellemesi bile canlı yayıma bağlı QA koşullu |

Sahip: hesap sahibi (hesap/panel/hukuk), geliştirici (PR), QA operatörü (kaynak/render); tarih 2026-10-19. Kaynağı olmayan sonuç **BİLİNMİYOR**. Ayrı onay kaydı yayın için şarttır.

## Geri alma / sahibine devir

Gerçek rızaya aykırı trafik, yanlış kaynak, çift lead veya bozuk CTA saptanırsa kamu eylemi durur; onaylı eski commit'e geri alma PR'si hazırlanır. **Veri yoksa 0 yazılmaz.** Gün11–14'te ancak erişim/kanıt varsa gerçek ölçümle güncellenir.
