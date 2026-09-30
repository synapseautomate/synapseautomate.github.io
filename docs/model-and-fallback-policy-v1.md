# Model ve Geri Dönüş Politikası v1

## Kamu politikası

- Model seçimi proje tasarım kararıdır; genel kalite garantisi değildir.
- Deterministik iş kuralları doğrudan uygulanabiliyorsa model yorumuna bırakılmaz.
- Kanıt eksikse makul görünen bir değer uydurulmaz; alan “bilinmiyor” kalır.
- Model çıktısı doğrulama sınırını geçemiyorsa akış insan incelemesine gidebilir, durabilir veya tanımlı deterministik geri dönüşü kullanabilir.
- Geri dönüş her zaman “başka model” değildir; en güvenli seçenek eylem yapmamak ve insan incelemesine geçmek olabilir.
- Davranışı etkileyebilecek model/sürüm değişiklikleri kapsam büyümeden önce üzerinde mutabık kalınan test setiyle yeniden test edilmelidir.

Bu dosya gizli güvenlik mimarisi, kimlik bilgileri, tedarikçi sırları veya müşteri özel ayarlarını açıklamaz.
