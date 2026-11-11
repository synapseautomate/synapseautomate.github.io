# Gün 10 — Yöntem 230: UTM isimlendirme sözlüğü

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. `utm_source` yayın kaynağı (`linkedin`, `instagram`, `youtube`, `seo` gibi); `utm_medium` trafik türü (`organic_social`, `organic_search`, `referral`), `utm_campaign` konu (`crm_devir_kontrolu`), `utm_content` kreatif slotu (`karusel`, `profil_link`).

2. PR #28 `utm()` fonksiyonu değerleri trim+lowercase yapıp yalnız `[a-z0-9_-]` izin verir; kişisel bilgi URL parametresinde bulunmamalı.

3. İç sayfa gezinmelerine `utm_` parametreleri eklemek atıf kaynak bilgisini bozar; PR #28 ana sayfa iç linkinde UTM YOK.

4. Negatif test: `Instagram`→`instagram`; `ig` otomatik `instagram` eşitlenmez (elle kurallandırma önerilir), e-posta sembolü içeren UTM boş geçmeli; duble kampanya asla tekile çevrilmiş gibi raporlanmamalı.

5. Örnek payload (`SENTETİK`): `{"source":"linkedin","medium":"organic_social","campaign":"crm_devir_kontrolu","event":"asset_view"}`; bu GA4 panel gerçekleşmesi değildir.

6. QA: statik kod PASS; rızalı network test CI RUN kanıtıyla; platform URL gerçekte paylaşılmış mı BİLİNMİYOR.

7. Yanlış UTM rakamı gözlenirse geçmişe dönük sahte düzeltme yazma; normalize mekanizmasını geri al, yeni kampanya sözlüğü sürümü aç.

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
