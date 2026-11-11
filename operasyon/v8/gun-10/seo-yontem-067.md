# Gün 10 — Yöntem 067: Marka sözü, arama talebi ve talep yaratımı

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Marka vaadi: **SYNAPSE Automate — Satış talebi ve teklif takibinde kritik CRM devir kararı insanda kalır.** Bu, çalışan bir CRM yazılımı iddiası değildir.

2. Başlangıç sorgusu: `synapse automate` (markalı), `teklif onayı crm devri`, `satış talebi teklif takip süreci` (markasız, ticari/öğretici karışık). Arama hacmi ve sıralama BİLİNMİYOR.

3. Önce/sonra: `index.html` genel AI H1 korunur → yeni görünür giriş `Teklif onaylandı. CRM devir kaydı hazır mı?`; `hizmetler.html` satış alt hizmeti korunur → yeni iç bağlantı.

4. Yeni hedef title `Teklif Onayı ve CRM Devir Kontrolü | Synapse Automate`; H1 `Teklif onaylandı. CRM kaydı hazır mı?`; canonical `https://synapseautomate.github.io/cozumler/satis-talep-teklif-takibi.html`.

5. `surec-analizi.html` gerçek form yoludur; `kanit/stok-farki-baglam-kontrolu.html` farklı CSV konusudur, Gün 10 CRM içeriğiyle karıştırılmadı; `sitemap.xml` ek URL PR #28 ile düzeltilmiştir.

6. Repo title/H1/canonical/iç bağlantı KOD PASS. Staged Site Integrity CI PASS; canlı HTTP 200/robots/Safari, Search Console/indeks TEST_EDİLEMEDİ.

7. Değişiklik PR #28 taslak, onay ve uygun barındırma koşulu çözülmeden main yayını yapılmadı.

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
