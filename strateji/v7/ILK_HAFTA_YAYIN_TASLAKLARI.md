# SYNAPSE V7 — İlk haftanın yayına alınmamış kreatif ve huni taslakları
**Tarih:** 14.10.2026 · **Durum:** DRAFT — kullanıcıdan eylem bazlı onay yok. Her metin hukuki/ödeme, çalışan demo ve iki tur mobil QA sonrasında yayımlanabilir.
**Kaynak veri:** Sadece sentetik sipariş/stok CSV. Müşteri, vaka, sonuç/ROI, gerçek sipariş veya referans iddiası YOK.

## A) Sitenin tek ana ürün sayfası — önizleme metni
**SEO başlık taslağı:** Sipariş–Stok CSV Uyuşmazlık Kontrolü | SYNAPSE Automate
**H1:** Sipariş ve stok kayıtlarındaki farkları, satır satır görün.
**Alt başlık:** İki CSV dosyasındaki seçili eksik, tekrar ve stok uyarılarını insan incelemesine uygun bir rapora dönüştüren yerel kontrol paketi. Mağazanızın stoklarını otomatik değiştirmez.
**Kanıt sırası:**
1. 10 satırlık *SENTETİK ÖRNEK*: 2 sipariş, 2 stok kaydı, açık şema ve tarihler. Ürün henüz kabul testinden geçmemişse yalnız statik “beklenen çıktı” tablosu kullanılır, **çalışan demo denmez**.
2. **Kontrol kuralları:** Boş SKU, yinelenen sipariş–SKU, negatif stok, sipariş adedi > tanımlı stok anı; eşleşmeyen SKU (Gün 03 testine bağlı).
3. **Çıktı:** Sipariş/SKU/kurala göre işaretlenmiş CSV inceleme listesi.
4. **Kapsam dışı:** ERP/pazaryeri bağlantısı, otomatik veri değişimi, hata/tasarruf garantisi, PII yükleme zorunluluğu.
5. **Gizlilik:** Örnekler sentetik; ürünün müşteri cihazında çalıştığı ancak test ile kanıtlandığında iddia edilebilir.

**CTA / satış ve ödeme hazır DEĞİLKEN:** “Sentetik örnek kontrolü incele” (ücretsiz, veri toplamayan içerik bağlantısı).
**İkincil CTA / KVKK ve form altyapısı uygun olduğunda:** “Kurumsal kapsamı sor” (yalnız gönüllü talep; canlı form bir üçüncü tarafa veri yolluyorsa açık aydınlatma gerekli).
**CTA / satış, fatura, teslim ve hukuk kapıları açıldıktan sonra:** “Kontrol paketinin teslim koşullarını gör” ve ayrıca onaylı, güvenli harici ödeme sağlayıcısı. GitHub Pages üzerinde hassas ödeme yok.
**Kesin canlı fiyat:** BELİRLENMEDİ. 990 / 4.900 / 24.900 TL sayıları yalnız iç test fiyatıdır.

## B) LinkedIn Company Service Page — TASLAK
**Hizmet adı:** E-Ticaret Sipariş/Stok CSV Veri Kalitesi Kontrolü
**Hizmet tanımı:** “CSV sipariş ve stok dışa aktarımlarında tanımlı tekrar, eksik SKU, negatif stok ve eşleştirme tutarsızlıkları için satır bazlı, açıklanabilir inceleme çıktısı hazırlamaya odaklanıyoruz. Temel çözümde mağaza/ERP entegrasyonu ve otomatik veri değişimi yoktur. Çalışmalar sentetik demo ve kabul kriteriyle gösterilir. Gerçek müşteri veri paylaşımı ancak yazılı kapsam ve uygun veri işleme şartları sağlanırsa değerlendirilir.”
**Konum:** Uzaktan, Türkiye. **İşletme resmî statüsü:** doğru beyan edilmeden şirket varmış gibi yazılmayacak.
**Fiyat:** “Kapsam görüşmesi sonrası”, fiyat alanı açık liste verilmeyebilir. Ödeme/fatura uygunluğu teyit edilmeden **aktif satış** iddiası yok.
**Onay:** Kullanıcı marka sayfasını seçtiğini ve ≤500 çalışan koşulunun sağlandığını doğrular; hizmet sayfası aktivasyonu ayrıca onay ister.

## C) LinkedIn özgün içerik taslakları — sadece organik, aynı sorun
### Post 1 — 5 kontrol
“İki stok dışa aktarımında aynı SKU farklı görünüyorsa, önce hangi tarih ve depo ölçüldüğünü sormak gerekir.

Bizim sentetik testimizde beş inceleme işareti var: boş SKU, yinelenen sipariş–SKU, negatif stok, tanımlı stok anına göre sipariş açığı ve sevk durumu çelişkisi.

Bu işaretler otomatik hata hükmü değil, insan kontrolü için açıklanabilir bir listedir.

SYNAPSE Automate | Sentetik veri örneği. Mağaza entegrasyonu veya otomatik stok değişikliği yok.”
**Görsel:** Gerçek test edilmiş sentetik kural tablosu; ticari kullanıma izinli Inter font, 1080×1350, alt açıklama.

### Post 2 — yanlış pozitif
“Negatif stok kaydı her zaman gerçek stok kaybı mıdır? Hayır, tek başına kesin hüküm verilemez. Rezervasyon tarihi, sipariş anı ve depo ayrımı kontrol edilmeden CSV verisi yanlış yorumlanabilir.

Yerel kontrol aracında her bulgu **kural koduyla** görünür olacak; düzeltme kararı operatörde kalacak.
Sentetik test — gerçek müşteri sonucu veya tasarruf iddiası değildir.”
**Görsel:** Solda sentetik iki dosya, sağda ‘manuel incele’ uyarısı; ürün fiilen çalışır test olmadan “çalışıyor” yazılmaz.

### Post 3 — veri gizliliği
“Operasyon verisini yorumlamak için her zaman buluta taşımak zorunda değilsiniz. Tasarladığımız küçük CSV kontrolünde amaç, dosyayı yerel ortamda işleyip uyarı listesini orada oluşturmaktır.

İlk kapsamımız sınırlı: dışa aktarılmış CSV, tanımlı kural seti, insan onayı.
Gerçek veriyle çalışma, teknik ve hukuki uygunluk testlerine bağlı.”
**Görsel:** Yerel akış diyagramı, gerçek veri içermeyen örnek; 1080×1350 ve 1080×1920 ayrıca QA.

## D) YouTube / kısa demo storyboard (önceden kayıtlı, 60 sn)
- 0–8 sn: “Bir CSV'de eksik SKU ve mükerrer kayıt fark edilir mi?” sentetik veri etiketi.
- 8–20 sn: `siparis.csv` + `stok.csv` şema tablosu; gerçek dosya içeriği üretim testinden alınacak.
- 20–38 sn: deterministik kural motoru çalışmasının **gerçek** ekran kaydı; çalışır motor yoksa video henüz çekilmez.
- 38–48 sn: çıktı CSV'de kural ve satır kodu; “manuel inceleme gerektirir”.
- 48–60 sn: “Kapsam, örnek veri ve sınırlamalar SYNAPSE sitesinde”; para/aktif satın alma vaadi YOK.
**Teknik QA:** 16:9 1920×1080 esas + 9:16 1080×1920 kırpılmadan yeniden düzenleme; Türkçe altyazı, 320 px mobil okunurluk, telif hakkı belirsiz müzik yok.

## E) Yayın talebi ve geri alma formu
Her kalem için **bağımsız onay**:
1. Onaylı ticari barındırmada ana sayfa/ürün sayfası URL'si, PR commit SHA, kapsam ve rollback yolu.
2. LinkedIn Company Service Page hesabı / profil tercihi / hizmet metni ve kategori.
3. Her LinkedIn postunun görseli, metni, kaynak/test etiketi, günü.
4. YouTube kanal, başlık, video, thumbnail, açıklama.
5. Ödeme linki, fatura/teslim politikası, şirket ve platform uygunluğu **tamamen ayrı**.

**Unutma:** Marka stratejisi onayı, gönderi yayını veya site merge onayı değildir.
