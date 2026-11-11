# Gün 02 — Tek ürün karar matrisi
| Hipotez | Problem netliği /5 | 0 TL prototip uygunluğu /5 | Karar |
|---|---:|---:|---|
| Sipariş/stok CSV farkı | 5 | 5 | **TEK BİRİNCİL** |
| Haftalık Sheets raporu | 3 | 4 | PARK |
| Genel sipariş hata taraması | 2 | 4 | PARK |

**Karar D02-01:** Tek yerel CSV kontrol motoru, iki teslim: (1) indirilebilir sabit şema ürünü; (2) aynı motorun dar B2B şema eşleme hizmeti. Üç ayrı ürün başlatılmayacak.

| Hipotez | TEST FİYATI | Kapsam |
|---|---:|---|
| Yerel ürün | 990 TL | İki CSV, uyarı raporu, API yok |
| Dar B2B kurulum | 4.900 TL | Tek şema eşleme, ayrı teslim |
| Opsiyonel pilot | 24.900 TL | Ayrı sözleşmeyle sınırlı pilot |

KDV dahil/hariç kararı BİLİNMİYOR; USD rakip fiyatları TL'ye çevrilmedi; fiyatlar satış onayı değil.

**Üç alıcı sorusu:** (1) Excel yerine neden? Gerekçeli, tekrarlanabilir kontrol hipotezi; Excel de çözebilir. (2) Veri dışarı çıkar mı? Yerel tasarım amaçlanıyor, dağıtım telemetri QA'sı bekliyor. (3) Yanlış alarm? Varyant, rezervasyon, iptal ve stok tarih farkında insan incelemesi gerekir.

**Bağımsız karşıt hipotez:** Excel ve mevcut SaaS yeterli olabilir, format farkları destek maliyetini yükseltebilir, 990 TL ödeme isteği doğrulanmamış. Pazar GO HAYIR.