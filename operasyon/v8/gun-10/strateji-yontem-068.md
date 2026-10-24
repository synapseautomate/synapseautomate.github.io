# Gün 10 — Yöntem 068: Marka işaretlerinin uyumu

- Fiilî çalışma: 2026-10-19; PDF planı: 23.10.2026 (gün numarası değiştirilmedi).
- Hizmet: Satış, Müşteri Talebi ve Satış Takibi; özgün örnek: teklif onayı → CRM devir sahipliği.
- Sınır: **SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL**. Çalışan CRM entegrasyonu veya gerçek satış verisi yok.
- Gerçek kaynak: [hizmetler.html](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/hizmetler.html), [müşteri talebi analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/cozumler/musteri-talebi-surec-analizi.html), [süreç analizi](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/surec-analizi.html), [ölçüm JS](https://github.com/synapseautomate/synapseautomate.github.io/blob/fb7cbbd77abf2abe5cb0b201cec83799e9338558/assets/js/synapse-measurement-v1.js), [web güncellemesi taslağı](https://github.com/synapseautomate/synapseautomate.github.io/pull/28).

## Uygulanan karar, örnek ve negatif kontroller

1. Tek anlatı: `SYNAPSE Automate`; premium ama abartısız hizmet analiz yaklaşımı; logonun repodaki `assets/brand/synapse-logo-clean.png` dosyası kullanılır.

2. Karar: web anasayfa+Hizmetler+CRM devir sayfası kaynak anlatısı PASS (taslak); LinkedIn paylaşımını kullanıcı yaptığını bildirdi, gerçek permalink/panel BİLİNMİYOR; Instagram/YouTube SYNAPSE hesap erişimi teyitsiz.

3. Sahiplik: GitHub PR bağlantısı bulundu; marka hesabının LinkedIn yönetici, Search Console, iki faktörlü doğrulama/kurumsal temsilci sahipliği BİLİNMİYOR. Hesap şifresi istenmez.

4. SERP aramasında aynı marka adını taşıyan sonuçlar görülse bile resmî hesaba aitliği dışarıdan doğrulanmadan yanlış işletme bilgisi 'düzeltildi' denmez.

5. İddia denetimi: müşteri sayısı/sonuç/ROI/lead dönüşümü/pilot kapasitesi gibi gerçek kayıtsız iddialar kullanılmadı.

6. Gizlilik sayfasının eski 'e-posta taslağı' anlatısı ile FormSubmit action uyumsuzluğu PR #28'de kod/taslak olarak düzeltildi; canlıya alınmadığı için canlı çelişki AÇIK.

7. Karar tablosu: web (QA operatörü, 2026-10-19, statik PASS, yayın kapısı açık); LinkedIn (hesap sahibi, BİLİNMİYOR, kullanıcı beyanı); hesap/2FA (hesap sahibi, TEST_EDİLEMEDİ).

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
