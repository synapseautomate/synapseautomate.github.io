# Sentetik veri kontrol kuralları
**Kaynak:** `04-ornek-veri.csv`; gerçek müşteri verisi değildir.

- R01: siparis_adedi > stok_adedi → stok açığı; örnek S-1002.
- R02: stok_adedi < 0 → negatif stok; örnek S-1003.
- R03: aynı siparis_kodu + sku birden çok kez → mükerrer satır; örnek S-1004.
- R04: boş sku → zorunlu alan eksik; örnek S-1005.
- R05: sevk_edildi + stok_adedi < 0 → ayrıca manuel inceleme; örnek S-1003.

Bu kurallar iş hipotezidir: stok anlık mı, sipariş zamanı mı, depo bazlı mı soruları cevaplanmadan kesin finansal hata iddiası kurulmaz.
