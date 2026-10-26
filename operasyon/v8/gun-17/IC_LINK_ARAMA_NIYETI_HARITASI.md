# Gün 17 — konu çakışması ve gerçek iç link akışı
**Öncelikli niyet:** AI sistemlerinde doğruluk, güvenlik ve maliyet denetimi — tek soruya yanıt. GSC gerçek sorgu verisi BİLİNMİYOR.

| Repo yolu | Arama / kullanıcı sorusu | Karar |
|---|---|---|
| `hizmetler.html` | Hangi hizmet? | kart 09'a draft olarak rehber linki eklendi |
| `rehberler/ai-surec-denetimi.html` | Bir sistemi hangi kriterlerle incelemeli? | Mevcut kanonik üzerinde editoryal revizyon |
| `cozumler/kurumsal-ai-operasyon-denetimi.html` | Bu incelemenin B2B hizmet kapsamı ne? | Bağlamsal link ile ayrılır; yeni fiyat iddiası yok |
| `rehberler/ai-otomasyon-guvenilirlik-testi.html` | Risk kapıları ve regresyon testleri | Test yöntemi ayrık kalır |
| `kanit/100-vaka-ai-guvenilirlik-regresyon-raporu.html` | Sentetik dondurulmuş test koşulları | Müşteri doğruluk yüzdesi gibi gösterilmez |
| `rehberler/kaynak-gosteren-rag-bilgi-tabani-rehberi.html` | Bilgi tabanı kaynaklı RAG | Gün 16 farklı problem; aynı içerik çoğaltılmaz |
| `en/ecommerce-process-analysis.html` | İngilizce e-ticaret süreci | Başka niyet; yanlış hreflang eşdeğeri kurma |

**Gerçek kaynak rotası (draft):** `/` → `hizmetler.html` → kart 09 linki → `rehberler/ai-surec-denetimi.html` → ilgili kurumsal denetim kapsamı.

**Teknik not:** GitHub dosya ağacı ve link varlığı kaynakta doğrulandı; canlı HTTP/sitemap crawl ve tıklama akışı TEST EDİLEMEDİ. Devir sözleşmesi gereği onaysız main ve sitemap değişimi YOK.
