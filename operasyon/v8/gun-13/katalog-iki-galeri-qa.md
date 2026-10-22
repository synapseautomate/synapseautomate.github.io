# SYNAPSE / GÜN 13

**İÇ TASLAK • 22.10.2026 • Gün13 plan tarihi 26.10.2026 • dört gün erken • YAYINLANMADI.** Gün08'de Upwork kapsam dışına çıkarıldı. Yeni talep nedeniyle metin hazırlanıyor, hesap/ilan etkinleştirilmiyor.

# Galeri: iki ayrı gerçek üretilmiş sentetik PNG / QA

**Gerçek yerel teslim paketi:** galeri/01_SENTETIK_KURAL_BULGULARI.png ; galeri/02_SENTETIK_KAPSAM_KARARI.png ; iki 320×240 px önizleme; galeri/QA_GALERI.json; galeri/SENTETIK_DENEME_SONUCU.json; galeri_uret_ve_test.py.

**Veri:** Yeni yapay beş sipariş ve iki stok satırında R01–R04 için birer bulgu, R05 bilinçli DEĞERLENDİRİLMEDİ. Bu yeni deney, mevcut SYNAPSE CLI ekran görüntüsü veya ücretli müşteri referansı DEĞİL. Alıcıya ürün ekranı diye sunulması P0.

| Kontrol | Tur A teknik | Tur B marka/optik | Karar |
|---|---|---|---|
| Deterministik test | python galeri_uret_ve_test.py → PASS, 4 bulgu | R05 ilan metniyle tutarlı | PASS: yeni sentetik deney |
| PNG ebatı ve etiket | İki 1200×900 görsel + 320×240 küçültme | Açılan ikisinde de tam “SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL” | PASS |
| Crop ve küçük önizleme | 320px çıktı üretildi | Platform içi gerçek crop ve küçük metin P1 | AÇIK |
| Telif | Özgün şekil ve metin, sistemdeki DejaVu Sans font | Lisans/dağıtım için nihai kontrol | P1 AÇIK |
| Gerçek ürün ekranıyla eşleşme | Gün04 eski ZIP/log yeniden elde edilmedi | Gerçek sürüm bağımsız ekran kontrolü | TEST EDİLEMEDİ P0 |
| Hesaba yükleme | Yapılmadı | Ayrı onay gerekir | YAPILMADI |

Alt metin 1: “SENTETİK örnekte R01 boş SKU, R02 tekrarlı sipariş/SKU, R03 depo/SKU uyumsuzluğu, R04 negatif stok.”
Alt metin 2: “SENTETİK örnekte R05 bağlam yetersizliğinden DEĞERLENDİRİLMEDİ; dahil ve hariç işlemler.”

**Karar:** İki görsel iç gösterim açısından üretildi; Upwork galeriye yüklemeye veya müşteri kanıtı diye sunmaya henüz uygun değil.

**Kaynaklar (22.10.2026):** https://support.upwork.com/hc/en-us/articles/360057397533-How-to-create-a-project-in-Project-Catalog ; https://support.upwork.com/hc/en-us/articles/360052511133-Circumvention-and-why-it-s-against-the-rules ; https://support.upwork.com/hc/en-us/articles/4407886701459-How-to-manage-your-Project-Catalog-order-on-Upwork ; https://www.kvkk.gov.tr/Icerik/4189/Kisisel-Verilerin-Islenmesine-Iliskin-Temel-Ilkeler.