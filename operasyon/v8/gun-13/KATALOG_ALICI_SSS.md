# SYNAPSE — Katalog alıcı SSS | İÇ TASLAK | 22.10.2026
**Upwork katalog aktifliği BİLİNMİYOR.** Gün 08 devir kararı Upwork hesabı açmamak ve kataloğu kapsam dışına almaktı. Bu belge kararı değiştirmez. Gönderim ve yayın yok.
## Asgari hizmet çerçevesi
1. **Kaç CSV?** Bir sipariş CSV'si ve bir stok CSV'si; tam iki dosya. Ek CSV/ERP/API yok.
2. **Başlıklar?** Siparişte siparis_id, sku, isteğe bağlı adet/depo/siparis_tarihi; stokta sku, eldeki_stok ve R05 için depo, stok_zamani ile rezervasyon tanımı. Gerçek müşteri verisini ilk temasta göndermeyin. Eşdeğer kolon adları yazılı eşleme ister.
3. **SKU?** R01 boş SKU; R02 yinelenen siparis_id+sku; R03 eşleşmeyen SKU/depo; R04 negatif stok. Normalizasyon ve depo varsayımları yazılı belirlenir.
4. **Stok zamanı?** R05 yalnız karşılaştırılabilir tarih/depo/rezervasyon ön koşulları varsa incelenir. Yoksa DEĞERLENDİRİLMEDİ; stok kararı verilmez.
5. **Kişisel veri?** İlk talep için hayır; yalnız şema/satır adedi/süreç amacı. İsim, adres, telefon, ödeme verisi, API anahtarı istemeyin. Sözleşme/veri işleme izni olmadan gerçek veri almayın.
6. **Teslim?** Satır+kural bulguları CSV, tek sayfa yorum özeti, şema/sürüm notu; gerçek ürünün bugünkü sürümü ayrıca test edilmeden kesin işlev taahhüdü yok.
7. **Süre?** Panelde belirlenmemiş: BİLİNMİYOR. Dosya büyüklüğü ve sözleşme şartları sonrası teyit.
8. **Sürüm?** Eski sentetik CLI kanıtı geçmiş arşivdir. İşletim sistemi, CSV encoding ve mevcut motor sürümü bugünkü doğrulamayı bekliyor.
9. **Destek?** Süresiz bakım yok; teslim içeriği açıklanır. Süre ve yanıt SLA'sı gerçek sözleşmede belirlenir.
10. **Revizyon?** Öneri: aynı iki CSV ve onaylanmış kurallar için bir açıklama/etiket düzeltmesi; yeni veri ve entegrasyon hariç. Platformun resmî revizyon alanıyla uyarlanması şart.
11. **İade?** Upwork koşulları/sözleşme veya site kanalı için ayrı hukukî koşullar; kesin garanti verilmez.
12. **Ödeme ve iletişim?** Upwork işi Upwork mesaj/ödeme/teslim içinde kalır. Site/IBAN/e-posta yönlendirmesi kesinlikle yok.
13. **Referans?** Görseller SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL. Gerçek vaka/ciro/ROI iddiası yok.
14. **Fiyat?** Upwork panel USD ve komisyon bilinmiyor; 4.900 TL başka hizmetin web liste fiyatı veya TEST hipotezi olarak katalog fiyatı değildir.
15. **Uygun değil?** Canlı stok değiştirme, pazar yeri API, ERP, sınırsız dosya, otomatik onarım veya garanti bekleyen işler.
**Resmî kaynaklar 22.10.2026:** https://support.upwork.com/hc/en-us/articles/360057397533-How-to-create-a-project-in-Project-Catalog ; https://support.upwork.com/hc/en-us/articles/360052511833-Get-to-know-each-other-before-a-contract .