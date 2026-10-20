# Gün 11 — Tek alıcı sorgusu ve kontrollü geri alma

**Hipotez sorgu (GSC hacmi doğrulanmadı):** “fatura ön işleme ve mutabakat kontrolü nasıl yapılır?”
**Alıcı:** KOBİ muhasebe/finans operasyonları yöneticisi. **Problem:** Fatura ve tek varsayılan banka kayıt satırı arasında fark çıkarsa otomatik eşleşme kararının doğruluğu belirsiz.
**Tek kontrol kararı:** "500 TL matematiksel farkı ödeme eksikliği olarak mı, HUMAN_REVIEW istisnası olarak mı işaretlemeliyiz?" → kaynak net değilse HUMAN_REVIEW.
**Ön koşullar:** yetkili kaynak, fatura referansı, onaylı eşleme kuralı, dönem ve para birimi eşleşmesi, insan onay rolü, işleme izni.
**Kapsam dışı:** mali müşavirlik, e-fatura oluşturma, vergi/KDV, banka hareketi, otomatik ödeme/mahsup, canlı ERP/banka entegrasyonu.

**Kanıt türleri:** (1) açık aritmetik tablo *sentetik/kavramsal*, (2) mevcut çalışan finans kontrol listesi *öz değerlendirme aracı*, (3) gerçek müşteri/entegrasyon/gelir/ROI = **YOK**. Fatura örneği her tablonun üstünde etiketli.

**Niyet çakışması:** mevcut `sektorler/finans-bankacilik.html` geniş finans sektör yaklaşımı, `rehberler/finans-ai-otomasyon-satin-alma-rehberi.html` tedarik sorusu, `rehberler/finans-ai-otomasyonu-guvenli-baslangic.html` güven sınırı, `araclar/finans-surec-kontrol-listesi.html` sekiz maddelik öz değerlendirme; yeni sayfa bunları kopyalamaz, tek sentetik mutabakat farkı kararıyla ayrılır.

**Site yolu (taslak):** index → finans-bankacilik → fatura-on-isleme-mutabakat-kontrolu → finans-surec-kontrol-listesi; ayrıca hizmetler finans kartı → yeni sayfa. SEO sitemap yalnız bir ek URL.

**Geri alma:** Henüz main merge olmadığı için draft PR kapatılır; üretim etkisi sıfır. İleride yazılı yayın onayından ve başarılı CI’dan sonra yayımlanırsa `git revert` ile yeni sayfa, iki açıklayıcı link ve XML sitemap kaydı birlikte çıkarılır. Asıl finans rehberleri/araç aynen kalır.

**Canlı yetki:** ONAY BEKLİYOR; otomatik yayın, gönderi, ödeme, GSC indeks isteği, hesap işlemi YOK.
