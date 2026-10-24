# Gün 10 — Yöntem 231: Gecikmeli markalı sorgu değerlendirmesi

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Markalı sorgular: `synapse automate`, `synapseautomate`, `synapse otomasyon` olası yazımlar; marka benzerleri kesin aynı işletme değil.

2. Kontrol: `index.html`, `hizmetler.html`, `surec-analizi.html`, `kanit/stok-farki-baglam-kontrolu.html`, `sitemap.xml`. Gün 10'un CRM sayfası PR #28 yeni URL, önceki stok kanıtı ayrı tutulur.

3. Önce → sonra: ana hizmet genel otomasyon → yeni CRM devir alt niyetiyle iç rota; başka sayfada title/H1 zorla değiştirme yok, yalnız gerekli link ve sitemap.

4. Search Console olmadan markalı/markasız tıklama ve indekslenme BİLİNMİYOR; video sonrası artış anlatısı gözlemsel olabilir ama nedensellik iddiası değil.

5. Yayın tarihini/tıklama tarihini aynı tabloda tut; PR veya promosyon/güncelleme gibi karıştırıcıları da sakla.

6. Kaynak tablosunda robots.txt/HTML meta/canonical/sitemap kod inceleme PASS; canlı HTTP200/noindex/robots ve GSC TEST_EDİLEMEDİ.

7. Yayın sonrası önerilen kontrol: resmî GSC URL denetimi hesabın sahibi tarafından, hiçbir parolayı paylaşmadan; kullanıcı onayı olmadan panel verisi üretilemez.

## Kabul ve iki bağımsız QA turu

| Kabul kontrolü | QA A (kaynak/kod) | QA B (hukuk/tasarım/canlı) |
|---|---|---|
| PDF yöntem ilkesini ayrı dosyaya yazma | GEÇTİ / kaynak eşlemesi | GEÇTİ / iç metin |
| Konu tekrarını önleme | GEÇTİ: CRM devir | GEÇTİ: CSV/stok değil |
| Panelden gerçek sonuç | TEST_EDİLEMEDİ | TEST_EDİLEMEDİ |
| Rıza, ödeme, FormSubmit gerçek teslim | KOD/CI koşullu PASS | P0 AÇIK: hukuk, üretim, teslim |
| Kamuya aktarım | TASLAK | ONAY verilmiş site güncellemesi bile canlı yayıma bağlı QA koşullu |

Ek SEO kabulü: title/H1/canonical/iç rota PR #28'de doğrulanır; HTTP 200, robots, GSC ve canlı SERP **BİLİNMİYOR**.

## Geri alma / sahibine devir

Gerçek rızaya aykırı trafik, yanlış kaynak, çift lead veya bozuk CTA saptanırsa kamu eylemi durur; onaylı eski commit'e geri alma PR'si hazırlanır. **Veri yoksa 0 yazılmaz.** Gün11–14'te ancak erişim/kanıt varsa gerçek ölçümle güncellenir.
