# Gün 17 — Eylem bazlı onay ve geri alma
- **WEB-G17-SEO-001:** `rehberler/ai-surec-denetimi.html` içerik/title/meta revizyonunun `main` dalına birleştirilmesi ve canlı yayın: **ONAY BEKLİYOR**. Sadece içerik değişikliği; fiyat, ödeme, formlar, analytics yok.
- **SOC-G17-000:** Sosyal paylaşım üretim kotası yok; `video-yontem-013.md` storyboard ancak yeni video/gönderi onayı verilirse prodüksiyon ve paylaşım ayrı onay gerektirir. **ONAYSIZ/YAYINLANMADI**.
- **UPWORK-G17-000:** Katalog ilan aktivasyonu/revizyon gönderimi/yanıt: **YAPILMADI**; ayrı izin.
- **PAY-G17-000:** Ödeme/KYC/IBAN/gerçek test: **YAPILMADI**, satış uygunluğu yok.
- **SEO-G17-INDEX-000:** Sitemap/robots/hreflang/schema değişimi: **YAPILMADI**, bugün gerek görülmedi.
- **G17 draft PR:** Oluşturulan dal yalnız iç çalışma; otomatik merge yok.

**Geri alma (merge onaylanırsa):** `git checkout 6de1c4ad10feef1fef37e93d2731dad5e7886574 -- rehberler/ai-surec-denetimi.html` komutu yalnız eski kaynak sürümü örneğidir; sonradan değişen `main`e kör force-push yapma, ayrı ters commit/PR üret.

**Ön yayın QA kapısı:** P0/P1 yeni kusur=0 gerçek render ve kullanıcı onayı, gizlilik/telif/ticari eylem sınırları; halen HOLD.
