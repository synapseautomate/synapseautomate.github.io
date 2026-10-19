# Gün 10 — Yöntem 236: Ölçüm veri kalitesi eşiği

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Kontrol tablosu: GA4 iki config; onamsız ağ isteği; JS-off; UTM case; first/last localStorage; internal/direct yönlendirme; 30dk pending; teşekkür sayfası refresh; yeniden çoklu form; iki cihaz; farklı channel referrer; yanlış `lead`/`sale` ataması.

2. PR #28 staging tarayıcı CI `qa_consent_local.mjs`: onamsız GA4 isteği ve atıf depolaması yok → kullanıcı opt-in → yükleme → geri çekme; `day1_browser_funnel.mjs`: yalnız consent sonrası sentetik POST mock'undan tek redirect eventi.

3. Negatif örnek: doğrudan `talep-alindi.html?submitted=process_analysis` açılışında `generate_lead` olmamalı; gerçek FormSubmit mail teslimi olmadan nitelikli talep yazılmamalı.

4. Test URL örnek: `surec-analizi.html?utm_source=linkedin&utm_medium=organic_social&utm_campaign=crm_devir_kontrolu`; payload `{"event":"generate_lead","confirmation":"formsubmit_redirect"}` SİNYALDİR, teslim kanıtı değil.

5. Gerçek GA4 DebugView/posta kutusu/Safari/network erişimi yok: TEST_EDİLEMEDİ. Canlı site izleme uygunluğu hukuk uzmanı teyidi yok: P0 AÇIK.

6. Veri kusuru görülürse raporu dondur, `generate_lead` ile tahsilat asla eşitleme ve regresyon sürümünü yayına taşımayı durdur.

## Kabul ve iki bağımsız QA turu

| Kabul kontrolü | QA A (kaynak/kod) | QA B (hukuk/tasarım/canlı) |
|---|---|---|
| PDF yöntem ilkesini ayrı dosyaya yazma | GEÇTİ / kaynak eşlemesi | GEÇTİ / iç metin |
| Konu tekrarını önleme | GEÇTİ: CRM devir | GEÇTİ: CSV/stok değil |
| Panelden gerçek sonuç | TEST_EDİLEMEDİ | TEST_EDİLEMEDİ |
| Rıza, ödeme, FormSubmit gerçek teslim | KOD/CI koşullu PASS | P0 AÇIK: hukuk, üretim, teslim |
| Kamuya aktarım | TASLAK | ONAY verilmiş site güncellemesi bile canlı yayıma bağlı QA koşullu |

Örnek JSON/UTM kaynaklarda yalnız **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL** niteliğindedir. Consent, kişisel bilgi sızıntısı, sahte `lead` ve geriye dönüşte eski SHA'ya revert stratejisi gereklidir.

## Geri alma / sahibine devir

Gerçek rızaya aykırı trafik, yanlış kaynak, çift lead veya bozuk CTA saptanırsa kamu eylemi durur; onaylı eski commit'e geri alma PR'si hazırlanır. **Veri yoksa 0 yazılmaz.** Gün11–14'te ancak erişim/kanıt varsa gerçek ölçümle güncellenir.
