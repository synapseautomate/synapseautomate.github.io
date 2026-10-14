# GÜN 02 | Tek sayfalık ICP ve müşteri problemi brifi
**Tarih:** 2026-10-14 (Europe/Istanbul) · **Sahip:** SYNAPSE Automate · **Statü:** İç hipotez; gerçek müşteri görüşmesi/ödeme kanıtı değildir.
**Dayanak:** V6 MAX PDF Gün 02 (s.11), Gün 01 [devir ve metrikler](https://github.com/synapseautomate/synapseautomate.github.io/pull/10).

## Tek seçilen müşteri
**ICP (hipotez):** Türkiye'de en az iki satış kanalı veya depo tablosuyla çalışan, her hafta sipariş ve stok verilerini CSV/XLSX olarak dışa aktarabilen **küçük e-ticaret işletmesi**. Kullanıcı: operasyon/ürün sorumlusu; alıcı/karar verici: işletme sahibi ya da operasyon yöneticisi. Kesin çalışan sayısı, ciro ve sipariş hacmi **henüz araştırma dışı ve doğrulanmamış**; ICP'yi yapay rakamla daraltma.

**Girdi:** Müşterinin kendi cihazında iki kaynaktan hazırlanmış CSV dışa aktarımı: `siparis_kodu`, `sku`, `siparis_adedi`, `stok_adedi`, `sevk_durumu`; mümkünse stok zaman damgası ve depo kimliği (ilk araçta desteklenmesi ayrıca doğrulanacak). PDF Gün 03 iki ayrı CSV dosyasını öngörür; Gün 01 prototipi tek bir birleşik CSV ile çalışır. Bu **ürün sözleşmesi uyuşmazlığı** Gün 03'te çözülmeli.

**Tetikleyici sorun:** “Bu sipariş niye stokta yok?”, boş SKU, yinelenen sipariş/SKU, negatif stok, sevk durumu ile stok kayıtlarının tutarsızlığı. Bunlar **uyarı/inceleme işareti**dir; farklı kayıt anları nedeniyle otomatik kesin ticari hata sayılmaz.

**Mevcut çözüm/satın alma alternatifi:** Elle Excel/Sheets filtreleri/VLOOKUP veya kapsamlı ERP/pazaryeri entegrasyonu. Problem tam entegrasyona yatırım yapmak değil, CSV dışa aktarımlarında bir kerelik hızlı veri kalitesi/istisna kontrolü olabilir (hipotez).

**Ödeme motivasyonu (kanıtlanmadı):** Manuel satır aramayı azaltma isteği, sorgulanabilir bulgu listesi, insanın karar verebildiği güvenli ve yerel veri kontrolü. **Gelir/ROI veya zaman tasarrufu iddiası yok.**

## Üç alıcı sorusu — bugünkü yanıtlar
1. **Hangi işi / ne sıklıkta?** Sipariş-stok CSV uyuşmazlıklarını dönemsel kontrol etmek; haftalık tekrar **ICP varsayımı**, müşteri görüşmesiyle doğrulanacak.
2. **Hangi veri ve hangi eylem?** CSV dosyaları cihazda okunur; çıktı `satir/siparis/sku/kural/aciklama` bulgu listesi ve manuel inceleme. Stok/ERP kayıtlarını değiştirmez.
3. **Neden bunun için ödeme?** Büyük entegrasyon gerekmeyen, tanımlı kontrol kurallarını tekrar çalıştırabilme. Bu değer önerisi **henüz ödemeyle test edilmedi**; ücretsiz Excel/Sheets alternatifi kuvvetli itirazdır.

## Bir cümlelik ürün vaadi
**“Sipariş ve stok CSV dosyalarındaki stok açığı, negatif stok, boş SKU ve yinelenen kayıt gibi tanımlı tutarsızlıkları yerel olarak işaretleyen kontrol paketi.”**

**Kritik sınır:** Mağaza/ERP entegrasyonu yok; otomatik stok değişimi yok; kâr/sonuç garantisi yok; kişisel veri yükleme zorunluluğu yok. Gerçek müşteri dosyası ve hassas veri istenmez. 
**Konumlandırma:** İndirilebilir araç temel ürün; yalnız talep üzerine sınırları belirli kurulum; B2B analiz/pilot sonraki kapı. Hesap sahibinin kurumsal B2B satış tercihi ayrı karar kaydında korunur. **Bugün satış veya ödeme açık değildir.**
