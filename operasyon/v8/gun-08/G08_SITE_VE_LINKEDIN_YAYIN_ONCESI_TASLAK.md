# Gün 08 — Site ve LinkedIn yayın öncesi metin taslağı

**DURUM: YAYINLANMADI — ONAY BEKLİYOR.** Gerçek müşteri sonucu değildir. Sentetik örnek kullanılır.

## Site hizmet bloğu (Türkçe)
### Sipariş ve Stok CSV Uyuşmazlık Kontrolü
İki dışa aktarım dosyanızdaki veri uyuşmazlıklarını görünür kılın: bir sipariş CSV'si ve bir stok CSV'si üzerinde tanımlı kurallarla sınırlı, dosya bazlı kontrol.

**Kontrol kapsamı:** eksik SKU; aynı sipariş/SKU tekrarları; SKU ve depo eşleşmeme; negatif eldeki stok; ancak zaman kesiti, depo ve rezervasyon tanımı yeterliyse koşullu stok yetersizliği kontrolü. Tanım yetersizse bu son kontrol **değerlendirilmedi** olarak raporlanır.

**Teslim:** bulgu satırları ve kural kodları içeren CSV raporu + tek sayfalık açıklama özeti. Örnekler sentetiktir; müşteri verisi veya doğrulanmış iş sonucu olarak sunulmaz.

**Hariç:** canlı ERP/e-ticaret bağlantısı, API entegrasyonu, sistem üzerinde stok değiştirme, otomatik düzeltme, sürekli izleme, finansal getiri/ROI garantisi.

**İşleyiş:** dosya alanları ve iş kuralları netleştirilir; uygunluk doğrulanır; kapsam ve takvim yazılı teyit edildikten sonra kontrol yapılır. Teslim süresi ve fiyat canlı sitedeki mevcut tekliflerle çelişmeyecek şekilde ayrıca kesinleştirilir.

**CTA taslağı:** 'Örnek raporu ve kapsamı inceleyin' → yalnız mevcut, doğrulanmış SYNAPSE sayfası/iletişim yolu. Bağlantı eklenmeden canlıya alınmaz.

## LinkedIn şirket gönderisi (Türkçe, taslak)
İki CSV dosyası birbiriyle konuşmuyorsa, küçük bir veri hatası büyük bir operasyonel belirsizliğe dönüşebilir.

Örnek: sipariş dosyasında bir SKU var, stok dosyasında aynı SKU ve depo kombinasyonu yok. Bu durumda ilk adım stok değiştirmek değil; uyuşmazlığı satır bazında görünür kılmak.

SYNAPSE'nin dar kapsamlı CSV kontrol yaklaşımında beş başlık var: eksik SKU, yinelenen sipariş/SKU, SKU–depo eşleşmeme, negatif stok ve **yalnız yeterli bağlam varsa** koşullu stok yetersizliği kontrolü.

Çıktı: kural kodlu bulgu raporu ve kısa değerlendirme özeti. Gösterilen örnekler sentetiktir; gerçek müşteri vakası veya başarı iddiası değildir.

Önce veriyi anlamlandırın; sonra aksiyona karar verin.

#VeriKalitesi #ECommerceOperations #EnvanterYonetimi #Otomasyon

## Yayın öncesi QA
- [ ] Site bilgi mimarisi ve mevcut hizmetlerle çakışma kontrolü
- [ ] Fiyat ve kapsam tutarlılığı
- [ ] Mevcut gerçek CTA hedefinin doğrulanması
- [ ] Gerçek logo ve marka uyumu
- [ ] Mobil 320/375/390/768/1024/1440, klavye, kontrast, link/404 kontrolleri (erişilemiyorsa TEST EDİLEMEDİ)
- [ ] KVKK/veri güvenliği ve sentetik etiketlerinin görünürlüğü
- [ ] WEB-G08 açık canlı yayın onayı
- [ ] LI-G08 açık paylaşım onayı

**Not:** Upwork bağlantısı, ücretli platform veya yeni hesap gerektirmez.
