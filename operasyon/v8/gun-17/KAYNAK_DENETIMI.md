# Gün 17 — kaynağı dondurulan site taraması / güncel sonuç
**26.10.2026 — plan tarihi 30.10.2026; GitHub main 6de1c4ad10feef1fef37e93d2731dad5e7886574.**
- **428 dosya / 150 HTML**: **150/150** HTML dosyası GitHub'dan açılarak title/H1/canonical/robots/CTA/idda dili örnekleri kaydedildi. Bu gerçek tarayıcı kontrolü değildir.
- 18 noindex, H1 içermeyen 5 (4 noindex + 1 Google doğrulama dosyası), canonical bulunmayan 3 özel dosya, explicit robots olmayan 4 ve 8 ortak canonical grubu. Kanıtsız olduğu kesinleşen iddia sayısı BİLİNMİYOR; **112 adet otomatik metin eşleşmesi inceleme adayı** ayrı CSV'de.
- Kayıt kaynağı: `veri/public-content-version-registry-v1.json` generated_at=2026-10-13, 27 asset. 26 HTML eşleşmesi; dış uzman incelemesi varsayılmaz. İnceleme tarihlerini ileri taşıma yok.
- **Gerçek eksik**: `hizmetler.html` hizmet 09 kartında ilgili rehber CTA'sı yoktu. PR #46 draft'ta tek yol eklendi: Hizmetler → AI Sistem İncelemesi ve Optimizasyonu → `rehberler/ai-surec-denetimi.html`. Eski rehber URL'sine aynı konuya yönelik dar kapsamlı üç eksenli bölüm eklendi.
- İki kaynak HTML'ye karşı 16/16 statik regresyon PASS; gerçek altı cihaz/browser, HTTP, GSC ve FormSubmit bilinmiyor. **Bu sebeple yayın=HOLD; main merge yok.**
- Kapsam/sınır: Yeni URL, sitemap, haksız ranking, fiyat, ödeme, sosyal gönderi, sahte müşteri, izin dışı temas YOK.
