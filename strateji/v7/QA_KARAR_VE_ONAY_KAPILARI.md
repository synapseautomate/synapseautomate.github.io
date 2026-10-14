# SYNAPSE V7 | İki tur strateji kalite ve güven denetimi
**Tarih:** 2026-10-14 · **Durum:** ÖNERİ / YAYIN ve SATIŞ YETKİSİ YOK.
**Kaynak:** V6 MAX Gün 02–30 kalite/günlük devir sınırları ve 14.10.2026 güncel resmî platform politikaları.

## TUR 1 — iş modelinin uygulanabilirlik ve marka denetimi
- **Tek problem / tek çözüm:** EVET, CSV sipariş-stok uyuşmazlık kontrolü; DIY ve B2B kurulum iki teslim biçimi, ikinci ürün geliştirme yok.
- **0 TL peşin trafik:** EVET, ücretli reklam / Premium LinkedIn / Upwork Connect satın alımı planlanmadı. Platformların tamamen ücretsiz olduğu iddia edilmiyor; ücretsiz katman limitleri ve satış sonrası kesintiler değişebilir.
- **İstenmeyen iletişim:** YOK. Açık LinkedIn Service Page, profesyonel yazılar ve isteğe bağlı kullanıcı formu; inbound isteklere cevap da kullanıcı eylem onayıyla.
- **Yanıltıcı referans:** YOK. Yalnız sentetik CSV örnek; gerçek müşteri, satış, ROI ve ölçülmüş fayda iddiası yok.
- **Yayın onayı:** Plan, içerik metni, site değişikliği, servis ilanı ve ödeme için *ayrı* kullanıcı onayını açıkça istiyor. Gerçek yayına çıkılmadı.
- **Fiyat gerçeği:** 990 / 4.900 / 24.900 TL TEST FİYATI. “Ödeme çalışıyor” veya “yasal olarak satışa açığız” iddiası yok.

## TUR 2 — resmî kaynak / nicel tutarlılık / teknik risk
| Test | Referans | Sonuç / sınır |
|---|---|---|
| LinkedIn Services ücretsiz | https://www.linkedin.com/help/linkedin/answer/a569534 | DOĞRULANDI. Premium ek özellikler ücretsiz değil. |
| Company Page sınırı | https://www.linkedin.com/help/linkedin/answer/a7436041 | ≤500 çalışan ve Page admini koşulları var; SYNAPSE hesap uygunluğu henüz panelden test edilmedi. |
| LinkedIn spam yasağı | https://www.linkedin.com/help/linkedin/answer/a1338787 | Soğuk özel iletişim ve otomatik etkileşim yasak. |
| Google indeks zamanlaması | https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl | Günler/haftalar, garanti yok; Google tek başlangıç kanalı seçilmiyor. |
| Google Business Profile uygunluğu | https://support.google.com/business/answer/13763036 | Tamamen online iş için kayda öneri YOK; yüz yüze iş kanıtı gerekir. |
| GitHub Pages ticaret politikası | https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits | **Yeni P0 platform uygunluk riski**: özellikle ticari işlemlere dönük barındırma yasak. Site/portföy kapsamı ayrı değerlendirilmeli. |
| Netlify/Cloudflare ücretsiz seçenek | https://www.netlify.com/pricing/ ; https://developers.cloudflare.com/pages/functions/pricing/ | Fiyat planı var; işleme/kota/kullanım şartları ve hesap onayı henüz test edilmedi. |
| Türkiye mevzuatı | https://tuketici.ticaret.gov.tr/yayinlar/tuketici-bilgi-rehberi/mesafeli-sozlesmeler-hakkinda-bilgilendirme | Satış türü, vergi, fatura ve müşteri statüsü profesyonel/hesap sahibi teyidi gerektirir. |
| 70 × 4% × 15% | `V7_SENARYO_VE_OLCUM.csv` | 0,42; keyfî planlama varsayımı |
| 180 × 6% × 20% | `V7_SENARYO_VE_OLCUM.csv` | 2,16; keyfî planlama varsayımı |
| 300 × 7% × 25% | `V7_SENARYO_VE_OLCUM.csv` | 5,25; keyfî planlama varsayımı |

## Kritik blokajlar
- **P0-01:** Şirket/fatura/ödeme/teslim şartları doğrulanmadan tahsil edilmiş satış beklentisi gerçekleştirilemez. Rakam bazen gerçek 0 olur.
- **P0-02:** Ürün henüz iki CSV sözleşmesi, kabul ve KVKK testlerinden geçmedi. Statik sahte “canlı demo” yayınlama.
- **P0-03:** GitHub Pages ticari işletme / e-ticaret hosting yasağına uygunluk incelenmeli; onaysız ticari siteye dönüştürme.
- **P0-04:** Ana site üzerinde izin/rıza kaydı, 320–1440 gerçek responsive QA ve gerçek talep formu uçtan uca doğrulanmadı.
- **P1-01:** Mevcut trafik/LinkedIn erişim verisi yok; senaryolar istatistiksel tahmin DEĞİL. Metricool hesabında SYNAPSE için bağlı sosyal ağ bulunmadığından API analitiği alınamadı. GSC kaynak ölçümleri de erişilebilir değildi.
- **P1-02:** LinkedIn Company Service Page kullanıcı hesabında oluşturulmadı; ücretsiz olması talep getireceği anlamına gelmez.
- **P2-01:** Stil rehberi, özgün ekran anlatımları ve görsel export QA tamamlanmadan kreatif paylaşılmaz.

## Uygulanmış gerçek eylem
GitHub üzerinde yalnız **strategic draft branch ve taslak PR** açma, öneri ve ilk hafta metinleri kaydetme. **Main merge, canlı yayın, ilan, LinkedIn gönderi veya müşteri iletişimi YOK.**
**KALİTE HÜKMÜ:** Araştırma/strateji taslakları iki turdan geçti; ticari platform, ürün, fatura ve canlı yayın **NOT READY**.
