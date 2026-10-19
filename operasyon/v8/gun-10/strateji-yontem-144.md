# Gün 10 — Yöntem 144: Birinci taraf izinli talep altyapısı

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. İlk temas alanları: e-posta, ihtiyaç özeti, karar sahibi rolü; gerçek alıcı listesi, gizli teklif eki, kimlik/IBAN, parola ve API anahtarı istenmez.

2. Temas yanıtı izni ayrı; pazarlama bülteni aboneliği değildir. Pazarlama için ayrı özgür iradeli opt-in, aydınlatma, silme/abonelikten çıkış işlevi hukuki onay olmadan AKTİF EDİLMEZ.

3. FormSubmit üçüncü taraftır; gerçek iletim, aktarımlar, teslim e-postası ve saklama koşulları panel/uzman teyidi olmadan PASS değildir.

4. İsteğe bağlı `Bizi ilk nerede duydunuz?` sorusu ancak insan onayı ve ayrı gizlilik kontrolünden sonra taslak olarak düşünülebilir; bugün formlara eklenmedi.

5. Yalnız toplu, kimliksiz segment önerisi: `teklif_onayi`, `takip_sorumlusu`, `crm_devir`; gerçek kişiye bağlanan gizli profil yok.

6. Karar: FormSubmit JS-off fallback PR #28 taslak; gerçek form POST 0 adet (bu çalışma eylem kaydı), posta teslim ve saklama TEST_EDİLEMEDİ.

7. KVKK [resmî çerez rehberi](https://www.kvkk.gov.tr/Icerik/7353/Cerez-Uygulamalari-Hakkinda-Rehber) hukuki uygunluk sertifikası değildir; gerekli veri sorumlusu/açık rıza metni için hukuk uzmanı P0 kapısı sürer.

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
