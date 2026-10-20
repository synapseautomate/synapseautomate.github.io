# Gün 11 — Açık web sorgu niyeti taraması (iç araştırma)

**Gerçek araştırma:** 20.10.2026, Türkçe açık web arama sonuçları ve Google Search Central resmî dokümanı.
**İlgili tek alıcı sorusu:** “Faturadaki tutar ile ilişkili ödeme kaydı uyuşmadığında, hangi kanıt kontrol edilmeli ve kim onaylamalı?”

**DİKKAT:** Bu bulgular **Google Search Console performans paneli**, Google autocomplete/PAA ham çıktısı, gerçek SYNAPSE müşterisi, arama hacmi, ilk sayfa sırası, CTR veya dönüşüm kaydı değildir. Arama sonuçlarından otomatik müşteri niyeti ya da ziyaret/gelir sonucu çıkarılmaz. Türkiye arama SERP'i kişiselleştirme, lokasyon, hesap ve zamanla değişebilir. Rakip markaları müşteri sayfasında kullanma veya haklarına ait görsel/marka kopyalama yok.

## Açık kaynaklar ve doğrulanan konu çeşitleri

| Kaynak | Kaynak tarihi | Tarama tarihi | Nitel gözlem | SYNAPSE kararı |
|---|---|---|---|---|
| [Bilsoft: e-Fatura Mutabakatı Nasıl Yapılır?](https://www.bilsoft.com/tr/blog/e-fatura-mutabakati-nasil-yapilir-cari-hesap-banka-ve-on-muhasebe-kontrol-rehberi) | 16.10.2026 | 20.10.2026 | Ön muhasebe kaydı ile banka/tahsilat eşleştirmesi farklı aşamalar; fatura oluşturulması tahsilat kanıtı değil | Tek hedef sayfada **fatura alanı/kayıt karşılaştırması + belirsizlik** |
| [FinansFix: Cari hesap mutabakatı nasıl yapılır?](https://finansfix.com/tr/blog/cari-mutabakat-nasil-yapilir) | 01.07.2026 | 20.10.2026 | Karşılıklı bakiye incelemesi / onay veya itiraz, tek belge ön işlemeden farklı niyet | Hedef sayfaya cari hesap tam mutabakatı vaat ETME |
| [Faturika: Banka mutabakatı nasıl yapılır?](https://faturika.com/blog/banka-mutabakati-nasil-yapilir-ay-sonu) | 03.09.2026 | 20.10.2026 | Banka ve muhasebe kayıtları arasındaki fark/kayıt zamanlaması; insanın açıklama yapma noktası | Banka/API canlı entegrasyonu veya ödeme emirleri yok |
| [TAM Mutabakat: Fatura ve cari hesap mutabakatı farkları](https://tammutabakat.com/blog/fatura-mutabakati-ve-cari-hesap-mutabakati-arasindaki-farklar) | 28.03.2026 | 20.10.2026 | Fatura bazında belge ile cari hesap bakiye bazında dönem sorusu ayrıdır | **Tek bir bilgi sayfası**; ikinci benzer “finans otomasyonu” sayfası açma |
| [IBAN Aracı: Banka ekstresi mutabakatında ödeme açıklaması](https://ibanaraci.com/blog/banka-ekstresi-mutabakati-aciklama) | 17.09.2026 | 20.10.2026 | Eşleştirme referansı ve işlem açıklaması kritik olabilir; tarih/tutar tek başına yeterli olmayabilir | Hedef sayfada **ön koşul: benzersiz eşleştirme anahtarı** |

**Sonuç:** Karar odaklı ayrı bir sayfa mantıklı olabilir: farklı kaynaklardaki sayısal farkı **insan inceleme kuyruğuna** bırakan, sentetik aritmetik kanıtı bulunan eğitim içeriği. Ancak *sorgu hacmi, rekabet seviyesi, ilk sayfa konumu, gerçek lead ve satış = BİLİNMİYOR*. Bu kaynaklar bağımsız müşteri görüşmesi yerine geçmez. Dış yazışma ve kişisel veri toplama yok.

## Resmî Google teknik temeli
- [AI özellikleri ve web sitesi](https://developers.google.com/search/docs/appearance/ai-features): 20.10.2026 incelendi. Özel GEO dosyası veya özel AI schema gerekmez; kullanıcıya yararlı, teknik olarak taranabilir içerik ve doğal bağlantılar. AI Overviews query fan-out tek anahtar kelime için çok sayıda sayfa açma zorunluluğu değildir. İndekslenme garanti edilmez.
- [Google: Kanonik URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls?hl=tr): 20.10.2026 incelendi. Self canonical + sitemap tercihi Google için sinyal, **Google'ın seçtiği canonical'ın doğrulaması değildir**.
- [Google: İnsan odaklı yararlı içerik](https://developers.google.com/search/docs/fundamentals/creating-helpful-content): özgün bilgi/kanıt ve açık sınırlar; başka sitelerin kopyası veya anahtar kelime varyasyon yığını olmamalı.

## Yöntem 003 / 077 / 114 / 172 onay kapıları
| İş | Statü | Sorumlu / sonraki kontrol |
|---|---|---|
| Açık webde 5 ilgili niyet örneği | TAMAMLANDI (yalnız dış gözlem) | Operatör / 20.10.2026 |
| GSC mülkiyet, sorgu, CTR, indeks | BİLİNMİYOR | Hesap sahibi / resmî Google paneli |
| Otomatik tamamlama, PAA, Reddit gerçek sayfa/dil/persona | TEST_EDİLEMEDİ | Günlük araştırma görevi bu alt yüzeyler için tamamlandı iddiası YOK |
| Mevcut finans sayfalarının niyet çakışması | KOD_KAYNAK_PASS | PR #32; ayrı sonuç izleme yayımdan sonra |
| Yeni URL ve sitemap canlı yayın | ONAY BEKLİYOR | Hesap sahibi, belirli URL |
| Yeni sitenin satıcı/vergi/KVKK yükümlülükleri | AÇIK P0 | Hesap sahibi / uzman; araştırma bunları çözmez |

**Yayına yönelik sonuç:** Daha çok site sayfası değil, tek hedef soruya özgün ve sentetik kaynaklı bir yanıt. Tam SEO riskleri ve mevcut eski `site_qa.py` FAIL, Gün 11 QA/devirlerinde açık tutulur.
