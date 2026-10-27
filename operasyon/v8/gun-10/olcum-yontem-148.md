# Gün 10 — Yöntem 148: İzinli kohort ve tekrar davranışı

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Kohort anahtarı: ilk anlamlı temas haftası + açık kaynak kanalı + CRM devri problem kategorisi (anonim toplu). Kişi adı/e-posta/cihaz kimliği ekleme.

2. Tablo: kaynak / ilk anlamlı eylem / uygun talep / teyitli müşteri / tekrar kullanım / tavsiye / gözlenen değer; tamamı BİLİNMİYOR.

3. `localStorage` atıf state'i PR #28 opt-in ile ancak rızada saklanır; tutma süresi sınırsızsa P1/açık, hukuk onayı olmadan 'uygun' raporu yok.

4. Dark social ve farklı cihazlar aynı kişiye bağlıymış gibi birleştirilmez; IP/fingerprint kullanılmaz.

5. Negatif test: consent reddinde first/last write olmaması; izin geri çekilince atıf temizlenmesi; aynı oturumda tek doğrulanmış redirect sinyali.

6. Örnek olay (`SENTETİK`): `{"source":"linkedin","first_action":"asset_view","cohort_week":"2026-w43"}` — gerçek kullanıcı/veri değil.

7. Geri alma: rıza veya kitle sınıflamasında hatalı bir güncelleme olursa taslak analitik değişikliğini eski SHA'ya geri döndür, panel raporunu geçersiz işaretle.

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
