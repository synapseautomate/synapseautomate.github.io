# GÜN 02 | İki turlu bağımsız QA ve kanıt matrisi
**Tarih:** 2026-10-14 (Europe/Istanbul) · **Sahip:** SYNAPSE Automate · **Operatör:** AI
**Gün 02 PR:** https://github.com/synapseautomate/synapseautomate.github.io/pull/11 (**draft**, main değil).
**Gün 01 devri:** https://github.com/synapseautomate/synapseautomate.github.io/pull/10
**PDF dayanak:** SYNAPSE V6 MAX, Gün 02 Operasyon s.11 ve Prompt/Gün 02 s.43–44 (kullanıcı mesajı).

## Kanıt: başlangıç erişimleri
- `main` üzerindeki `index.html` GitHub içeriği başarıyla okundu: blob SHA `b188ed7115aa12837d98c05036e85dbf4c012cb9`; Gün 01 baz `bc79409c8f672884a00dcdb89b0b6119cac42f6c`. Doğrudan canlı site `https://synapseautomate.github.io/` URL okuması tarayıcı aracında **DisabledError**; 200/404 veya mobil davranışı doğrulanmadı.
- LinkedIn açık indekslenmiş profil `https://tr.linkedin.com/company/synapseautomate` aramada görüldü; yönetici hesabı, görüntülenme/CTA/lead/ödeme panellerine erişim YOK. Yorum ve gösterim miktarı doğrulanmış metrik sayılmaz.
- Gün 01 devri, `metrikler.csv`, karar günlüğü, açık P0'lar ve sentetik hizmet/CSV kural dosyaları GitHub'dan okundu. Gün 01 PR #10 açık ve taslak.
- Hiçbir yetkili ödeme, fatura, reklam, GA4 veya satış paneline giriş yapılmadı. Mevcut veri erişimi GitHub + kamuya açık ürün sayfalarıyla sınırlı.

## QA tur 1 — görev kapsamı ve doğruluk
**Metot:** GitHub API üzerinden Gün 02 dosyalarını tekrar okuyup yapı ve sayıları bağımsız kontrol etme.
| Kontrol | Kanıt / komut özeti | Sonuç |
|---|---|---|
| Gün 02 zorunlu brif | `01-icp-problem-brifi.md` — tek persona, üç alıcı sorusu, tek ürün cümlesi | **GEÇTİ** |
| Niyetli arama adayları | `02-alici-niyetli-arama-ifadeleri.md` — `Q01..Q12` (12 benzersiz) | **GEÇTİ**; hacim doğrulanmadı |
| Gerçek alternatif ve fiyat | `03-bes-alternatif-fiyat-kaynaklari.md` — altı farklı resmî ürün | **GEÇTİ**; kullanıcı ödemesi/gerçek talep değil |
| Tek ürün / alternatifleri park et | `04-urun-hipotezi-karsilastirma.md`: H1 seçildi, H2 ve H3 'PARK ET' | **GEÇTİ** |
| Ticari kapsam ve etiket | `05-fiyat-ve-kapsam-varsayimi.md`: 990, 4.900, 24.900 TL her biri TEST FİYATI | **GEÇTİ** |
| Metrik dürüstlüğü | `06-metrikler.csv` — 7 sütunlu 14 kayıt, tüm satırlar aynı alan sayısı; erişilemeyen panel verileri 'bilinmiyor' | **GEÇTİ** |
| Yayın/harcama/iletişim yasağı | `07-onay-kapilari-ve-kusurlar.md` — ayrı onay eylemleri, 4 açık satış P0 | **GEÇTİ** |

**Tur 1 bulgu:** İlk otomatik metin eşleme kuralı (tam karakter dizisi araması) kapsam dışı ifadelerde eşanlamlı/sözcük dizilişi farklarını negatif saydı; kaynak belgede bu sınırlar açıkça bulunuyor. Bu bir içerik kusuru değil, test eşleme eşiği; ikinci kontrolde anlam bazlı eşleşme teyit edildi.

## QA tur 2 — bağımsız çapraz kontrol ve kaynak
| Kontrol | Yeniden doğrulama | Sonuç |
|---|---|---|
| Altı rakip isim/fiyat ve URL | Dopigo 24.999 TL/yıl; StockMount 25.000 TL/yıl kampanya; Google Workspace 71,20 TL/kullanıcı/ay (yıllık taahhüt görünümü); Microsoft 7 USD/kullanıcı/ay (yıllık, vergi hariç); Airtable Free ve 20 USD; Coupler.io Free ve 32 USD/ay. Her birinin resmî URL'si dosyada. | **GEÇTİ (sayfa/etiket)** |
| Ürün semantiği | Stok anı/depo ve SKU eşleme belirsizliği raporlanmış; hata garantisi verilmedi | **GEÇTİ (taslak)** |
| Hariç tutulanlar | API/ERP/mağaza bağlantısı YOK, otomatik stok değişimi YOK, sonuç garantisi YOK, gerçek kişisel veri yükleme zorunluluğu YOK | **GEÇTİ** |
| B2B / PDF uzlaşmazlığı | PDF indirilebilir ürün önceliği ve hesap sahibinin kurumsal B2B tercihi **iki ayrı karar** olarak kaydedilmiş | **GEÇTİ (açık karar ayrımı)** |
| Kaynak gösterimi | Tüm altı alternatif resmî şirket fiyat sayfasına bağlantılı; kapsamlar farklı diye not düşüldü | **GEÇTİ** |
| Gün 02 ayrı PR | PR #11: draft=true, merged=false, base=main. Kod veya canlı site kök dosyası değiştirilmedi. | **GEÇTİ** |
| Tek sayfa PDF | `SYNAPSE_GUN_02_ICP_PROBLEM_BRIFI.pdf` yerel A4 tek sayfa; PDF metninde başlık, 3 soru, vaat, hariç işler, test fiyatları; PyMuPDF'de bozuk Unicode `U+FFFD` yok | **GEÇTİ** |
| Yerel PDF görseli | 120 DPI PNG'ye render ve gözle kontrol: tipografi, kenarlar, Türkçe harfler, boşluk, kayma / taşma sorunu görülmedi | **GEÇTİ (tek sayfalık rapor)** |
| 320/375/390/768/1024/1440 canlı site | Site bugün düzenlenmedi; canlı tarayıcı görüntüleme ve her çözünürlükte QA kanıtı mevcut değil | **TEST EDİLEMEDİ** |
| Checkout / fatura / KVKK | Ödeme paneli ve fatura yetkisi bulunmuyor; GA4 izin davranışı uçtan uca denenmedi. KVKK resmî rehberi: https://www.kvkk.gov.tr/Icerik/7353/Cerez-Uygulamalari-Hakkinda-Rehber | **SATIŞA ÇIKIŞ KALDI** |

## P0/P1/P2 ve kalite kapısı
- **P0 (ticari satış): 4 AÇIK** — satış dosyası, şirket/fatura, güvenli ödeme, teslim/kabul.
- **P1 (ürün/kanıt):** Gün 03 iki CSV sözleşmesi; veri zaman/depo semantiği; analitik/çerez; gerçek müşteri talep sinyali yok.
- **P2:** Marka tokenları, SEO ve görsel varyantlar (ayrı yayın QA işi).
- **Gün 02 iç araştırma kalite hükmü:** Teslimler **GEÇTİ**, ürün hipotezi *belirlendi*, pazar ödeme niyeti **DOĞRULANMADI**.
- **Canlı site veya ticari ürün hükmü:** **NOT READY**. Kullanıcının spesifik onayı olmadan yayın/merge, müşteri iletişimi, ödeme, harcama yapılmadı.

## Ekran görüntüsü ve öncesi/sonrası
- Yerel rapor önizleme resmi: `gun02_work/onepage.png`; PDF: `SYNAPSE_GUN_02_ICP_PROBLEM_BRIFI.pdf` (konuşma eki; GitHub'a ikili belge yüklenmedi).
- Canlı site değiştirilmediği için canlı **önce/sonra ekran görüntüsü yok**; yokmuş gibi sunulmaz.
- Kirli/kırık link listesi: Gün 02 iç belgelerdeki altı üretici URL'si resmî sayfadan okundu; canlı sitenin bütün bağlantılarının HTTP durum taraması yapılamadı.
