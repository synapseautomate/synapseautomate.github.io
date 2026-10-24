# V8 / Gün 01 — Operasyon durumu
**14.10.2026, UTC+3; 01/30.** Sapma 0 gün. **Sahip:** SYNAPSE hesap sahibi; denetim operatörü AI.

**Tek amaç ve esas blokaj:** Satışın bugün doğrulanabilir ana engeli, hukuki satıcı/fatura statüsü ve güvenli tahsilat zincirinin kanıtlanmamış olmasıdır. 'Şirket yok', 'ödeme reddedildi', 'satış yapıldı' denemez. **Belge taslağı var / teknik ürün hazır HAYIR / ticari satış hazır HAYIR / doğrulanmış ödeme kapısı BİLİNMİYOR.**

## Kaynaklı başlangıç
- Canlı ana sayfa https://synapseautomate.github.io/ kamuya açık okundu. Genel süreç analizi 4.900 TL, pilot 24.900 TL başlangıç ifadesi var; V8 iki CSV ürünü için bunlar **onaylanmış satış fiyatı değil**. Alt canlı URL'lerin HTTP/render durumu TEST EDİLEMEDİ.
- LinkedIn https://www.linkedin.com/company/synapseautomate/ kamu profili görüntülenebiliyor/indeksleniyor; Services aktivasyonu/admin paneli, gösterim, izinli talep BİLİNMİYOR; sosyal paylaşımlar için bu gün kota yok.
- Repo https://github.com/synapseautomate/synapseautomate.github.io : `main` SHA `bc79409c8f672884a00dcdb89b0b6119cac42f6c` (13.10.2026 14:08:40 TSİ); ana sitenin ana sayfası kaynak ve kamu içeriği eşleşiyor.
- https://github.com/synapseautomate/synapseautomate.github.io/pull/10 V6 Gün 01, #11 V6 Gün 02, #12 V7, #13 V8: **hepsi open/draft/merged=false**. Main'de `operasyon/v8` başlangıçta yok. PR #10/11 devirleri ve #12/13 QA/strateji dosyaları branch'ten okundu.
- Önceki **27 gün 0 ücretli satış kullanıcı beyanı**, doğrulanmış banka kanıtı değildir; yeni V8 trafik, gösterim, ziyaret, demo, talep, sipariş, tahsilat, gelir ve iade **BİLİNMİYOR**.
- V6 birleşik CSV prototipi V8'in iki ayrı `sipariş.csv` + `stok.csv` kabul edilmiş ürünü değildir.

## Hukuki satış kapıları (sıralı)
1. Gerçek satıcı, mükellefiyet/fatura veya e-belge yetkisi; 20/B istisna belgesi ve banka/tevkifat şartları kişiye/faaliyete göre mali müşavir/GİB'den doğrulanır. MoR yerel vergiyi otomatik kaldırmaz.
2. B2B/B2C ayrımı, mesafeli satış/ön bilgilendirme, tüketici iade ve dijital teslim, vergi/KDV, gerekiyorsa ETBİS.
3. Upwork B2B hizmet için platform içi ödeme/fonlama; MoR dijital dosya için ayrı KYC/IBAN/komisyon/negatif bakiye/teslim/iade.
4. Gerçek iki CSV ürün testi, hash/versiyon, teslim onayı, KVKK/çerez, lisans ve platform uygunluğu.

**Bugün:** Sadece araştırma ve taslak. 0 TL peşin; Shopier, soğuk iletişim, main merge, yayın, post, katalog inceleme, satış/kart testi yok.

Kaynaklar (14.10.2026 erişimi):
- GitHub: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (güncelleme tarihi gösterilmedi)
- Cloudflare: https://developers.cloudflare.com/pages/platform/limits/ (05.09.2026); https://developers.cloudflare.com/pages/functions/pricing/ (08.09.2026)
- GİB: https://istanbul.gib.gov.tr/mevzuat/kanun/433 (GVK 20/B, kişi/faaliyet teyidi gerekir)
- Ticaret Bakanlığı: https://tuketici.ticaret.gov.tr/yayinlar/tuketici-bilgi-rehberi/mesafeli-sozlesmeler-hakkinda-bilgilendirme (17.08.2026); https://etbis.ticaret.gov.tr/tr/SSS
- KVKK: https://www.kvkk.gov.tr/Icerik/7353/Cerez-Uygulamalari-Hakkinda-Rehber (Temmuz 2025)
- LinkedIn: https://www.linkedin.com/help/linkedin/answer/a7436041 (Company Services koşullu ücretsiz)
