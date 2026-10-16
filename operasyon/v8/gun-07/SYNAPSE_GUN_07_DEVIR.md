# Gün 07 — İlk kamusal görünürlük kararı
Denetim 2026-10-15. **İç taslak hazır, yayın onayı BEKLENİYOR.**

| Kapı | Sonuç |
|---|---|
| Ürün | Gün 05 sentetik 25/25 PASS; ticari ürün hazır değil |
| Ödeme | HAYIR |
| Hukuki | BİLİNMİYOR, P0 |
| Trafik ölçümü | BİLİNMİYOR, canlı GA4/çerez testi yok |

**P0-01:** Vergi/fatura durumu doğrulanmadı; checkout yok. **P0-02:** GitHub Pages ticari barındırma sınırı. **P1-01:** Gerçek Safari cihaz testi yok. **P1-02:** Canlı çerez/GA4 ağ testi yok. **P1-03:** LinkedIn panel kırpma testi yok. **P0/P1=0 DEĞİL; yayına hazır kararı YOK.**

**Ekran QA:** Bilgilendirme demosu Chromium'da 320,375,390,768,1024,1440 px yerel render PASS; tek H1, 3 H2, logo alt, yatay taşma yok, sentetik etiketi var. Yerel tarayıcıda ağ erişimi engellendiği için HTML içerik enjeksiyonuyla render alındı; bu canlı HTTP/404 veya Safari testi değildir. Link hedefi örnek CSV dosyası PR içinde mevcut. Klavye odağı CSS kuralı var; gerçek cihaz/panel QA açık.

**Geri alma:** Bu PR yalnız draft; merge edilmez. İleride yazılı onayla merge edilirse merge SHA kaydedilir, sorun halinde `git revert <merge_sha>` için yeni PR hazırlanır. Canlı önce/sonra görüntüsü ve HTTP testi ancak yayından sonra mümkün; şu an YAPILMADI.

**İki QA turu:** Teknik Chromium altı genişlik PASS, canlı Safari/HTTP/çerez BLOCKED. Editoryal fiyat, sahte müşteri, ödeme iddiası yok; sentetik etiket PASS. **Tam yayına hazır QA PASS değildir.**

**Ayrı onaylar:** WEB-G07-01 demo sayfası PR merge: BEKLENİYOR; LI-G07-01 metin: BEKLENİYOR; LI-G07-02 görsel: BEKLENİYOR. LinkedIn post URL YOK; yeni canlı demo URL YOK; trafik ve talep BİLİNMİYOR. Dış yayın yapılmadı.

## 15.10.2026 — premium görsel QA ek kanıtı
- PDF Gün 07 ile uyumlu tek grafik, **1080×1350 PNG** olarak yerel üretildi; **320×400** küçültme ayrıca alındı.
- **Kanonik SYNAPSE logo artık nihai kompozisyonda** (önceki logo eksik P0 görsel düzeltildi).
- Kullanıcıya sunulan kanıt paketi: `SYNAPSE_G07_MARKALI_GORSEL_QA.zip` (sohbet eki; GitHub PR içine ikili dosya yüklenmedi).
- PNG SHA256: `4f06e9a80c9309710aae3d1de0ae8f3d538e95f10f133cc063e8f428b4003b9c`.
- **Yerel görsel incelemesi PASS**: logo görünür, ana mesaj okunabilir, sentetik etiket mevcut, öğeler taşmıyor.
- **LinkedIn panel önizlemesi NOT_TESTED**; yayın onayı NOT_GRANTED; canlı paylaşım YOK.
- IBAN kullanıcı tercihi olup vergi/fatura uygunluğu kanıtı değildir. Kullanıcı mevcut iletişim bağlantılarının doğru yönlendirdiğini teyit etti; canlı HTTP testi değildir.
- Nihai karar: P0/P1 açık, yayına hazır değil; PR draft ve yayından bağımsız.
