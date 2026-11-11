# GÜN 02 | P0/P1/P2, tek tek onay kapıları
**Tarih:** 2026-10-14 | **Sahip:** SYNAPSE hesap sahibi; **QA:** operatör.
## P0 — satış/yayın engelleri; çözülmedi
1. **P0-01 Ticari ürün tamamlanmadı:** Gün 02 yalnız ürün hipotezi. Gün 03 iki CSV sözleşmesi; Gün 04 çalışan indirilebilir sürüm; Gün 05 kabul testleri.
2. **P0-02 Şirket/fatura/vergi:** Hesap sahibinin henüz kurulmuş şirketi ve fatura yetkisi yok. Hukuk/mali müşavir uygunluğu ve resmî belgeler doğrulanmadı.
3. **P0-03 Ödeme sistemi:** Satıcı hesabı/kimlik/ödeme uygunluğu ve gerçek checkout kanıtı yok; test parası harcanmayacak.
4. **P0-04 Teslim/kabul:** İndirme, lisans/teslim bildirimi, dijital tüketici koşulları ve B2B hizmet kabulü doğrulanmadı.
## P1 — ürün/UX/ölçüm
- **P1-01 Dosya sözleşmesi:** PDF Gün 03 iki ayrı CSV (sipariş ve stok) ister; mevcut Gün 01 prototipi birleşik CSV kullanıyor. Örnek stok dosyası/eşleme ve test gerekir.
- **P1-02 CSV tanımı:** Stok zaman penceresi, depo ve sipariş statüsü doğrulanmadan stok açığına “kesin hata” deme.
- **P1-03 Veri/erişim:** Gerçek kullanıcı verisi yüklenmeden sentetik örnek; yerel işleme yolu ispatlanacak.
- **P1-04 Analitik/KVKK:** Mevcut sitede GA4 izin kapısı tarayıcıda doğrulanmadı. Kaynak: https://www.kvkk.gov.tr/Icerik/7353/Cerez-Uygulamalari-Hakkinda-Rehber
- **P1-05 Canlı mobil/a11y/bağlantı:** Bugün canlı site üstünde altı viewport/klavye ve form sunucu testi yapılamadı.
- **P1-06 Değer/fiyat:** Alıcı görüşmesi, gösterim veya ödeme kanıtı yok; rakip entegrasyon aboneliğiyle doğrudan fiyat üstünlüğü iddiası yasak.
## P2 — tasarım/ölçek
- Marka görsel tokenları, illüstrasyon/telif envanteri, katalog SEO mikro kopyası. Bunlar Gün 07 yayını için ayrı QA'dan geçecek.
## Ayrı ve spesifik kullanıcı onayı gerektiren işler
- **A01:** Gün 02 draft PR'ı `main` ile birleştirmek ve canlıya yayınlamak (**bugün YAPILMADI**).
- **A02:** Canlı ürün/teklif fiyatını değiştirmek, yeni CTA, ürün sayfası, demo, ilan veya LinkedIn postu yayınlamak (**YAPILMADI**).
- **A03:** Müşteriye DM/e-posta/WhatsApp/telefon göndermek, izinli teklif başlatmak (**YAPILMADI**).
- **A04:** Hesap/ödeme sağlayıcı başvurusu, kimlik/IBAN/fatura/ücretli işlem (**YAPILMADI**).
- **A05:** Canlı form/analitik gerçek veri testi ve izleme izni (**YAPILMADI**).
**Karar:** Gün 02 araştırma dosyaları iç taslakta kalır. Kullanıcı açık izin vermedikçe A01–A05 hiçbiri yapılmaz.
