# Asgari veri / teslim / kabul matrisi — İÇ TASLAK
| Faz | Giriş | Teslim veya kontrol | Eksikse |
|---|---|---|---|
| İlk gönüllü talep | 2 CSV şema başlığı, satır sayısı, karar sahibi rolü | Yalnız uygunluk açıklaması | gerçek CSV isteme |
| Kapsam sözleşmesi | yetki, fiyat, kanal, süre, revizyon, saklama, fatura | imzalı/yazılı şartlar | P0 DUR |
| R01 | sku | eksik SKU satırları | değerlendirilmedi |
| R02 | siparis_id + sku | mükerrer çiftler | değerlendirilmedi |
| R03 | sku + depo eşleme tanımı | eşleşmeyen anahtarlar | değerlendirilmedi |
| R04 | eldeki_stok sayısal | negatif stok satırları | parse hatası |
| R05 | stok tarihi+depo+rezervasyon+adet semantiği | koşullu uyarı | DEĞERLENDİRİLMEDİ |
| Teslim | sözleşmeyle yetkilendirilmiş veri | bulgular.csv + tek sayfa özet + sürüm/şema notu | kabul yok |
| Kabul | rapor/hata ve revizyon ölçütü | müşteri onay kaydı, dosya hash/tarih/satır adedi | eksik kabul |
**Minimum müşteri tarafından başlatılan gereksinimler:** yalnız 2 dosyanın kolon adları; satır sayısı; SKU/depo politikası; stok zamanı/rezerve tanımı; görevlendirilen onay rolü; veri işleme ve fatura uygunluğunun sözleşmesi.
**Boş teslim tutanağı:** proje [ ]; sözleşme kanalı [ ]; şema [ ]; sürüm [ ]; R01 [ ]; R02 [ ]; R03 [ ]; R04 [ ]; R05 [ ]; bulgu sayısı [ ]; istisnalar [ ]; hash [ ]; kabul [ ]; revizyon [ ]. Bu belge gerçek müşteri teslimi kanıtı değildir.
Upwork gereksinim ve kabul iş akışı platformda yerleşik, proje iş adımları listesinde müşteri kabulünü yeniden vaat etmeyin.