# Gün 03 referans kodu — açık teknik karşıt testler
Kaynak: 15.10.2026 yerel `csv_validator.py` ve 9/9 unittest.

- R01 boş SKU `E_REQUIRED` hatası olarak bastırılıyor; `findings` içinde R01 yok. Belge-kod eşlemesi netleştirilmeli.
- R04 negatif stok `E_NUMBER` + `negative_stock_R04` olarak raporlanıyor; bulgu değil. Dış sözleşme bunu açıkça söylemeli.
- R05 uygulanmıyor; depo/zaman/rezerve stok eksikliği nedeniyle **bilinçli**.
- Boş `durum` hata; ama izin verilen durum kümesi henüz doğrulanmıyor.
- Birden fazla stok satırında aynı SKU'nun depo/zaman bağlamı belirsiz; yanlış eşleme riski.
- `splitlines()` + `join()` gömülü satır sonu olan alıntılı CSV hücrelerini değiştirebilir.
- Satır numarası gerçek fiziksel satır sayısı olmayabilir; çok satırlı hücre negatif testi gerekir.
- İsim/boşluk/case normalizasyonu bilinçli politika gerektirir; otomatik eşit sayılmamalı.

**Karar:** Gün 03 sözleşme ve sentetik temel QA kapalı; bu açık teknik maddeler çözülmeden gerçek ürün GO yok. Kamuya doğrulanmamış özellik iddiası yok.