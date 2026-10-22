# SYNAPSE / GÜN 13

**İÇ TASLAK • 22.10.2026 • Gün13 plan tarihi 26.10.2026 • dört gün erken • YAYINLANMADI.** Gün08'de Upwork kapsam dışına çıkarıldı. Yeni talep nedeniyle metin hazırlanıyor, hesap/ilan etkinleştirilmiyor.

# Asgari veri / teslim / kabul matrisi

| Adım | Minimum giriş | Kabul / durdurma | Çıkış | Sorumlu |
|---|---|---|---|---|
| Gönüllü soru | Satır sayısı aralığı, dosya başlıkları, depo/tarih varlığı | Hassas veri paylaşma; özel bilgi gerekiyorsa DUR | Uygunluk yanıtı taslağı | Hesap sahibi |
| İş açma | Kanal, fiyat, takvim, gereksinim ve veri izni | Platform işi/fonlama ve fatura şartı teyitsizse DUR | Yazılı kapsam | Hesap sahibi / hukuk |
| Veri kabul | 1 sipariş + 1 stok CSV, başlık eşlemesi, ayraç, kodlama, veri yetkisi | Kimlik/sır içeriği veya şema uyumsuzsa DUR | Girdi kabul tutanağı | Operasyon + veri sahibi |
| R01 | sipariş SKU | Boşsa uyarı, otomatik düzeltme yok | Kural/satır | Operasyon |
| R02 | sipariş ID+SKU | Yinelenen ikiliyi işaretle | Kural/satır | Operasyon |
| R03 | SKU+depo, stok anahtarı | Eşleşmiyorsa işaretle, tahmin yok | Kural/satır | Operasyon |
| R04 | eldeki_stok | Negatifse uyarı; stok değiştirme yok | Kural/satır | Operasyon |
| R05 | stok anı, rezervasyon, dönem, depo | Eksikse DEĞERLENDİRİLMEDİ | Kural ve gerekçe | Operasyon |
| Teslim | Rapor CSV, bir sayfa özet, sürüm/test logu | Girdi kapsamı ve istisnalar karşılaştırılır | Platform içi teslim | Operasyon |
| Revizyon | Açık hata ve onaylı kapsam | Sayı henüz BELİRLENMEDİ; yeni kural ücretli ayrı teklif olabilir | Yazılı değişiklik | İki taraf |
| Kapanış | Taraf onayı/platform kabulü, log erişim/silme protokolü | Silme/izin takvimi net değilse veri işleme başlamaz | Kabul tutanağı | Hesap sahibi |

## Müşteri tarafından başlatılan proje / ASGARİ GEREKSİNİMLER
- G1 Projenin Upwork veya bağımsız site kaynaklı olduğunu teyit et.
- G2 Ticari kapsamı ve kesin fiyat/süre/revizyon hakkını resmî kanalda onayla.
- G3 CSV başlık listesini **gizli veri olmadan** yaz.
- G4 SKU ve depo alanı nasıl birleştirilecek, stok tarihi ve rezervasyon tanımı var mı belirt.
- G5 Kişisel veri yokluğu veya hukukî paylaşım yetkisini doğrula; güvenli aktarım/saklama/silme planını kabul et.

## TESLİM KONTROL TUTANAĞI — BOŞ
Proje kanalı: [ ] • gerçek fonlanan sipariş: [BİLİNMİYOR] • girdi adı ve satırları: [ ] • schema/encoding: [ ] • kural R01–R05: [PASS/BULGU/DEĞERLENDİRİLMEDİ] • sürüm/SHA: [ ] • bulgu dosyası/özet: [ ] • teslim tarihi: [ ] • platform kabulü: [BİLİNMİYOR] • revizyon: [ ] • log/silme: [HUKUKİ ONAY BEKLİYOR] • fatura: [BİLİNMİYOR].

**Örnek şema (yalnız yapay):** siparis_id,sku,adet,depo / sku,depo,eldeki_stok. Kimlik verisi ilk talepte gerekmez.

**Kaynaklar (22.10.2026):** https://support.upwork.com/hc/en-us/articles/360057397533-How-to-create-a-project-in-Project-Catalog ; https://support.upwork.com/hc/en-us/articles/360052511133-Circumvention-and-why-it-s-against-the-rules ; https://support.upwork.com/hc/en-us/articles/4407886701459-How-to-manage-your-Project-Catalog-order-on-Upwork ; https://www.kvkk.gov.tr/Icerik/4189/Kisisel-Verilerin-Islenmesine-Iliskin-Temel-Ilkeler.