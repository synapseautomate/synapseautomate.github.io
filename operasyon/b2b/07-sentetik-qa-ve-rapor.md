# Sentetik örnek QA ve yönetici özeti
Tarih: 2026-10-13 | Kaynak: `04-ornek-veri.csv` ve `csv_kontrol.py`
**Veri türü:** Tamamen sentetik; gerçek müşteri sonucu değildir.

## Yerel çalışma sonucu
Komut: `python csv_kontrol.py 04-ornek-veri.csv --out bulgular.csv`
- İncelenen veri satırı: **6**
- Bulgu sayısı: **7**
- R01 stok açığı: 2 (S-1002, S-1003)
- R02 negatif stok: 1 (S-1003)
- R03 mükerrer sipariş/SKU satırı: 2 (S-1004, iki satır)
- R04 boş SKU: 1 (S-1005)
- R05 sevk edildi + negatif stok: 1 (S-1003)

## Yönetici özeti taslağı
Örnek veride öncelikli inceleme S-1003 ve S-1002 kayıtlarında. S-1004 iki kez göründüğünden mükerrerlik kaynağı incelenmeli. S-1005 kaydının SKU alanı eksik. Bu bulgular birbirinden bağımsız olay sayıları değildir; aynı satır birden fazla kurala takılabilir.

## Yorum sınırları
Sipariş/stok karşılaştırması, stok anlık görüntüsü ve rezervasyon zamanlaması bilinmeden kesin stok hatası olarak sunulamaz. Negatif stok bir veri veya entegrasyon semantiği olabilir. Mükerrer satır, bölünmüş sevkiyat veya farklı depo bilgisi taşımıyorsa sorun olabilir.

## Test planı
`python -m unittest -v test_csv_kontrol.py`
7 senaryo: temiz veri, stok açığı, negatif stok/sevkiyat, mükerrer, eksik SKU, geçersiz sayı, eksik başlık.

## Açık iyileştirmeler
Gerçek müşteri verisi kabulünden önce alan eşleştirme, büyük dosya performansı, bozuk CSV satırları, gizlilik, stok zamanı, çoklu depo, iade/iptal ve erişim kontrolü testleri gerekir.
