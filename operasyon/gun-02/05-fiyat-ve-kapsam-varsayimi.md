# GÜN 02 | Fiyat ve kapsam varsayımı — TEST FİYATI / SATIŞ AÇIK DEĞİL
**Tarih:** 2026-10-14 · **Sahip:** SYNAPSE Automate · **Kaynak:** V6 MAX Gün 02, resmî rakip kaynakları `03-bes-alternatif-fiyat-kaynaklari.md`.

## Ürün hiyerarşisi (yalnız tek temel çözüm)
| Kademe | Deneysel fiyat | İçerik hipotezi | Satış öncesi doğrulama | Statü |
|---|---|---|---|---|
| **P1 İndirilebilir yerel CSV kontrol aracı** | **990 TL / test fiyatı** | Örnek sentetik CSV, yerel kural kontrolü, UTF-8 bulgu CSV, kural sözlüğü, kısa kurulum ve destek sınırı | İki kaynak şeması, test setleri, işletim sistemi/Python gereksinimi, lisans/iade/teslim şartları, gerçek kabul testi | **TASLAK; satılamaz** |
| P2 İsteğe bağlı sınırlı kurulum | **4.900 TL / test fiyatı** | Sadece P1'in kabul edilen veri şemasına eşlenmesi ve bir kurulum/doğrulama oturumu; net veri hacmi/teslimat ayrıca belirlenir | Taleple başlayan B2B sözleşme/kapsam, veri işleme şartları, vergi/fatura, müşteri kabul ölçütleri | **TASLAK; teklif/tahsilat yok** |
| P3 Sınırları belirli B2B pilot/analiz | **24.900 TL / test fiyatı** | Aynı temel kural motorunun belirli süreçte uygulanması ve manuel onaylı bulgu raporu; otomasyon/entegrasyon otomatik eklenmez | Ayrı keşif, yazılı teklif, ticari uygunluk, SLA, hizmet kapsamı, veri erişim izni ve kabul | **TASLAK; ücretli müşteri yok** |

**KDV, süre, kullanıcı sayısı, üst satır limiti, komisyon, destek düzeyi ve ödeme vadesi belirlenmediği için bu fiyatlar BAĞLAYICI DEĞİLDİR.** Şirket ve faturalandırma imkânı henüz bulunmadığından ödeme kabul edilmez ve kamuya “satın al” CTA'sı açılmaz. Rakiplerin abonelik/entegrasyon ücretleri bu fiyatların piyasa tarafından kabul edildiğini kanıtlamaz.

## Alternatifler fiyatı niçin doğrudan doğrulamıyor?
- Dopigo (24.999 TL/yıl) ve StockMount (25.000 TL/yıl ürün+stok kampanyası) bağlantılı operasyon platformlarıdır; P1 ise bağlanmayan, tek kullanımlı yerel kontrol olabilir.
- Workspace/Sheets (71,20 TL/ay yıllık görünüm), Excel web (7 USD/ay yıllık), Airtable (Free veya 20 USD/editor/ay) ücretsiz/düşük maliyetli ikame baskısı yaratır. SYNAPSE, bu araçların ücretsiz filtre/formüllerinden daha az iş veya daha net risk sınıflaması sunduğunu **henüz müşteriyle kanıtlamadı**.
- Coupler.io rapor aktarımı sunar, yerel CSV validasyonu aynı değildir.

## Sınanabilir fiyat hipotezleri — 0 TL bütçe
- **H990:** Organik ve niyetli kullanıcı, sentetik demoyu ve gerekleri anladıktan sonra yerel aracı 990 TL test fiyatıyla değerlendirmek ister. *Gözlem:* ayrı onaylı sayfada fiyatın yanındaki bilgilendirme CTA olayı ve nitelikli gönüllü talep; *geçerlik:* satın alma eğilimi ≠ ödenmiş satış. Henüz ölçüm yok.
- **H4900:** Veri eşleme ihtiyacı olan nitelikli B2B talep, tek seferlik kurulum kapsamını sormaya razı olabilir. *Gözlem:* müşteri **kendi isteğiyle** gönderdiği kapsamlı keşif talebi; bugün böyle talep verisi yok.
- **H24900:** Şeması karmaşık işletme, yazılı pilot kapsamını incelemek ister. *Gözlem:* belgeli ihtiyaç ve izinli teklif talebi; bugünkü listeleme/satış istatistiği yok.
- **İtiraz falsifikasyonu:** İlk gerçek gönüllü talepler sürekli “Ücretsiz Excel ile yapıyoruz”, “CSV hiç çıkaramıyoruz”, “Yerel Python kullanamayız” diyorsa ürün/teslim gereksinimi gözden geçirilir. Talep yokken “pazar fiyatı onayladı” denmez.

## Satışa geçiş / onay sırası
1. Gün 03 dosya sözleşmesi ve her kural için açıklanabilir kabul testi.
2. Gün 04 çalışan ürün, Gün 05 kalite sertleştirme.
3. Gün 06 fatura, ödeme, dijital teslim, Türkiye tüketici/veri ve platform koşullarının resmî denetimi (hesap sahibinin gerçek yasal statüsü).
4. Gün 07 ilk yayın kapısı — **ayrı spesifik kullanıcı onayı**; 0 TL ücretli trafik; soğuk temas yok.

**Bugünkü hüküm:** Üç rakamın hepsi **TEST FİYATI**dır; hiçbirini “geçerli satın alma fiyatı” olarak kamuya sunma.
