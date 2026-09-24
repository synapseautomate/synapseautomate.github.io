# Kontrollü AI İş Akışı Pilotu - SOW v1

**Durum:** Partner-ready spesifikasyon; müşteri sonucu değildir.

## Kapsam
- 1 iş akışı
- Maksimum 50 vaka
- 1 ana veri kaynağı + gerekiyorsa 1 doğrulama kaynağı
- 14 gün: 7 gün shadow/baseline, 7 gün kontrollü kullanım
- Otonom external action yok

## Başarı metrikleri
- Onaylanmış sonuca toplam süre
- İnsan düzeltme dakikası
- Kritik/major hata
- Escalation doğruluğu

## Human gate
Approve / Edit / Reject / Escalate. Para, sözleşme, yüksek etkili write veya belirsiz kaynak insan onayı olmadan commit edilmez.

## Exclusions
Hukuki/klinik nihai karar, otonom para hareketi, sınırsız write/egress, çok-workflow production rollout, garanti edilen ROI veya doğruluk.
