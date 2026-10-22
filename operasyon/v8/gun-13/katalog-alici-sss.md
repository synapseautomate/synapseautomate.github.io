# SYNAPSE / GÜN 13

**İÇ TASLAK • 22.10.2026 • Gün13 plan tarihi 26.10.2026 • dört gün erken • YAYINLANMADI.** Gün08'de Upwork kapsam dışına çıkarıldı. Yeni talep nedeniyle metin hazırlanıyor, hesap/ilan etkinleştirilmiyor.

# Katalog alıcı SSS

1. **Kaç CSV?** Bir sipariş CSV'si ve bir stok CSV'si. Ek dosya/depo/dönem ayrı yazılı kapsamdır. Boyut/satır sınırı panelde henüz belirlenmedi.
2. **Hangi başlıklar?** Sipariş için siparis_id, sku, adet, depo; stok için sku, depo, eldeki_stok önerilen yapay şema; gerçek müşteri başlıklarının eşlemesi yazılı teyit edilecek. Ayraç/UTF-8/ondalık/boşluk kuralı kabul öncesi test edilir.
3. **SKU?** Kimlik ve SKU sessizce düzeltilmez. SKU + depo anahtarları esas; normalizasyon ancak müşteri onayıyla.
4. **Stok tarihi ve depo?** Stok anı, depo, rezervasyon ve sipariş dönemi belirsizse stok yeterliliği R05 DEĞERLENDİRİLMEDİ; garantili stok önerisi yapılmaz.
5. **Beş kural?** R01 boş SKU, R02 aynı sipariş kimliği + SKU tekrarı, R03 SKU + depo eşleşmeme, R04 negatif eldeki stok, R05 bağlamı yeterliyse koşullu stok yeterliliği.
6. **Kişisel veri?** İlk görüşmede gerçek dosya, müşteri kimliği, telefon, adres, ödeme ve anahtar GÖNDERMEYİN. Gerçek veri ancak izin/rol/aktarım/silme koşulları yazılı teyit edilirse.
7. **Teslim süresi?** Henüz taahhüt edilmedi; Upwork'te gerekli gereksinimler sağlanınca sözleşmedeki süre işler. Net gün sayısı resmi ilan ekranında ayrı onaylanır.
8. **Sürüm ve tekrar üretim?** Çalışan yazılım sürümü, test komutu ve çıktı checksum'ı tutanağa yazılacak. Yeni sentetik deneme mevcut SYNAPSE CLI ürününün kanıtı değildir.
9. **Destek?** Destek penceresi ve yanıt kanalı henüz BELİRLENMEDİ; süresiz destek sözü yok.
10. **Revizyon?** Dahil sayısı henüz BELİRLENMEDİ. Aynı kabul edilmiş kuralın yanlış uygulanması düzeltilebilir; yeni API, ekstra ay/dosya, yeni kural ek kapsamdır.
11. **Teslim?** Satır + kural bazlı bulgu CSV, tek sayfa kapsam/istisna özeti, kullanılabilir sürüm/test kaydı. Gerçek vaka veya referans yayımlanmaz.
12. **Hariç?** Mağaza/ERP API entegrasyonu, otomatik stok değiştirme, canlı izleme, sınırsız geliştirme, garantili gelir/ROI.
13. **Ücretsiz örnek?** Galeri yalnız yapay 5 sipariş+2 stok örneğinde dört uyarı veren yeni sentetik deneyi gösteriyor; ücretli müşteri teslimi değildir.
14. **İade/iptal?** Upwork kaynaklı siparişte resmi Upwork kabul/iptal/ödeme kuralları; bağımsız site talebinde ayrı sözleşme/ilgili hukuk kapısı uygulanacak. İade garantisi/istisnası hukuk teyidi olmadan yazılmaz.
15. **Fiyat/kur/KDV/komisyon?** Katalog resmi fiyatı BİLİNMİYOR. Sitenin 4.900 TL süreç analizi, 990 TL yazılım test fiyatı ve Upwork dar inceleme aynı ürün sayılmaz; nihai rakam panel ve fatura teyidi gerektirir.

**Upwork ilanında IBAN, site formu, WhatsApp, harici e-posta yok.**

**Kaynaklar (22.10.2026):** https://support.upwork.com/hc/en-us/articles/360057397533-How-to-create-a-project-in-Project-Catalog ; https://support.upwork.com/hc/en-us/articles/360052511133-Circumvention-and-why-it-s-against-the-rules ; https://support.upwork.com/hc/en-us/articles/4407886701459-How-to-manage-your-Project-Catalog-order-on-Upwork ; https://www.kvkk.gov.tr/Icerik/4189/Kisisel-Verilerin-Islenmesine-Iliskin-Temel-Ilkeler.