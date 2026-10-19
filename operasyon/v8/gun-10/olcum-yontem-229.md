# Gün 10 — Yöntem 229: Dark social / kaynağı görünmeyen trafik

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Boş `document.referrer` → kodda `direct`; bu ne adresi elle yazmayı ne WhatsApp/özel konuşma kaynaklı ziyareti kanıtlar.

2. Kaynak açıklaması: `direct_or_unknown` yorumunu raporda kullan; kesin kaynaktan alıcı profili oluşturma ve izinsiz mesaj takibi YOK.

3. UTM kodu sadece SYNAPSE'nin kamuya yayınladığı bağlantılarda, küçük harf ve kişisel veri olmadan kullanılacak.

4. Test URL: `...?utm_source=linkedin&utm_medium=organic_social&utm_campaign=crm_devir_kontrolu&utm_content=karusel` (yalnız örnek, yayın yapılmış bağlantı değil).

5. Referrer negatif testleri: boş, https://www.linkedin.com, google, Bing, farklı site, bozuk URL, mobil in-app browser; sonuçlar gerçek tarayıcı/GA paneli olmadan BİLİNMİYOR.

6. Geri alma: yanlış UTM/dark-social tahmini ölçümü bozar ise kampanya sınıflandırmasını durdur, geçmişi veri yok olarak not et.

7. Kaynak anonim ilk temas vs kullanıcı isteğe bağlı beyanı ayrı sütunda tutulacak; hassas kişi verisi toplanmayacak.

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
