# Üç kanıt içeriği

## 1 — Unknown vs fabricated
Bir alan kaynakta yoksa güvenilir otomasyon onu tamamlamaya çalışmaz. `null` bırakır, hangi kaynağın eksik olduğunu işaretler ve karar önemliyse insan incelemesine yönlendirir. Hedef daha dolu JSON değil; hatanın nerede duracağını görünür kılmaktır.

## 2 — Structured output ≠ truth
JSON şemasına uyan bir cevap hâlâ yanlış olabilir. Güvenilir akışta şema, provenance ve deterministik doğrulama ayrı katmanlardır. Yapı okunabilirliği sağlar; kaynak izi doğrulanabilirliği, kural motoru ise izin verilmeyen eylemi durdurur.

## 3 — Human gate as product behavior
İnsan onayı sonradan eklenen bir güvenlik notu değil, workflow state'idir. Kaynak, önerilen eylem, beklenen etki, yetki sahibi ve reddetme/geri alma yolu aynı karar kartında görünür olmalıdır.
