# Gayrimenkul bakım talebi triage — sentetik/spec before/after metodolojisi v1

**Sürüm:** 1.0  
**Tarih:** 2026-09-26  
**Veri statüsü:** Tamamen sentetik/spec. Gerçek müşteri, bina, kiracı, gelir veya üretim verisi içermez.

## Amaç

Tek bir bakım talebi sınıflandırma akışında, yalnız konu bazlı otomatik yönlendirme ile güvenlik/eksik-bilgi sınırları eklenmiş kontrollü yaklaşımı aynı sabit 12 sentetik vaka üzerinde karşılaştırmak.

Bu çalışma üretim doğruluğu, müşteri tasarrufu, yatırım getirisi, uyum veya güvenlik garantisi değildir. Yalnızca tanımlı test setinde karar sınırı davranışını gösterir.

## Durum modeli

- `AUTO_PROCEED`: düşük etkili, açık ve yeterli girdide tanımlı rutin yönlendirme devam edebilir.
- `HUMAN_REVIEW`: kaynak/girdi yetersiz veya belirsiz; insan incelemesi gerekir.
- `STOP_ESCALATE`: güvenlik veya yüksek etki sinyali; otomasyon durur ve yetkili insana/acil prosedüre yükseltilir.

## Before / başlangıç yaklaşımı

Konu sınıfı ve dar bir açık acil kelime listesiyle otomatik yönlendirme. Belirsizlik, eksik kaynak ve dolaylı güvenlik belirtileri için ayrı bir kapı yoktur.

## After / kontrollü yaklaşım

Aynı vakalara dört kontrol eklenir:

1. güvenlik etkili tetikleyicilerin ayrı değerlendirilmesi,
2. iki veya daha fazla risk sinyali varsa otomatik kapatmanın engellenmesi,
3. kaynak/girdi yetersizse `HUMAN_REVIEW`,
4. yüksek etkili durumda otomatik eylem yerine `STOP_ESCALATE`.

## Değerlendirme

Beklenen durum, before/after karşılaştırmasından önce vaka dosyasında sabitlenmiştir. Puanlama tam durum eşleşmesidir.

- **Karar eşleşmesi:** sistem durumu = beklenen durum.
- **Kritik kaçırma:** beklenen durum `HUMAN_REVIEW` veya `STOP_ESCALATE` iken sistem `AUTO_PROCEED` üretirse.
- **Rutin otomatik yönlendirme korunumu:** beklenen `AUTO_PROCEED` vakalarının kaçında `AUTO_PROCEED` korunuyor.

## Sabit test sonucu

- Before: **8/12** karar eşleşmesi.
- Kontrollü: **12/12** karar eşleşmesi.
- Kritik kaçırma: **4 → 0**.
- Rutin otomatik yönlendirme: **4/4 → 4/4**.

Bu sayılar yalnız bu 12 sabit sentetik vakaya aittir. Yeni veri üzerinde genelleme veya üretim performansı iddiası değildir.

## Dosyalar

- `veri/gayrimenkul-bakim-triage-spec-v1.csv` — dondurulmuş test seti ve beklenen/before/after durumları.
- `veri/gayrimenkul-bakim-triage-eval-v1.py` — aynı CSV üzerinden sonuçları tekrar hesaplayan küçük değerlendirme betiği.
- `kanit/gayrimenkul-bakim-onceliklendirme-before-after-spec.html` — public kanıt sayfası.
