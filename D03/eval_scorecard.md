# eval_v0 — sentetik yapılandırma karşılaştırması

- Tarih: 2026-08-06
- Veri: 20/20 sentetik, gerçek müşteri verisi yok.
- Dağılım: 12 normal, 5 istisna, 3 adversarial/bozuk.
- Config A: basit çıkarım / sınırlı guardrail.
- Config B: şema + explicit unknown + failure guardrail + human escalation.

| Ölçü | Config A | Config B |
|---|---:|---:|
| Doğru güvenli davranış | 17/20 | 20/20 |
| Kritik/adversarial yakalama | 0/3 | 3/3 |

## Yorum
Bu test bir müşteri veya genel LLM performansı iddiası değildir. Aynı sentetik vaka setinde, explicit kurallar ve escalation davranışının basit çıkarımdan daha güvenilir olup olmadığını reproducible biçimde kontrol eder. Canlı pilot öncesi gerçek/redakte vakalarla yeniden ölçülmelidir.
