# Gün 11 XML/robots/kanonik matrisi (taslak; fiili 20.10.2026)

Kaynak SHA: cfbcd0c4bb9c084771b9562291b52a95a2c2c339. Denetlenen kaynaklar: `index.html`, `site-haritasi.html`, `sitemap.xml`, `sitemap-demand.xml`, `robots.txt`, `llms.txt`, `content-manifest.json`, `sektorler/finans-bankacilik.html`, `hizmetler.html`, `araclar/finans-surec-kontrol-listesi.html`.

| Özellik | main durumu | Draft farkı | Sonuca güven |
|---|---|---|---|
| HTML sayfaları | 146, GitHub tree | 147 (tek yeni özel sayfa) | GitHub tree PATH_PASS; gerçek HTML metadata CI bekliyor |
| `sitemap.xml` | Var, mevcut canonical URL’ler | Tek `fatura-on-isleme-mutabakat-kontrolu.html` ekli, `lastmod` 2026-10-20 | KOD_KONTROLU; main değişmedi |
| `sitemap-demand.xml` | Var, genel ticari niyet/çözüm adresleri | Değişiklik yok (ikinci kayıt yok) | KOD_KONTROLU |
| `robots.txt` | `Allow: /`, sitemap bildirimleri var | Değişiklik yok | KAYNAK_PASS |
| `site-haritasi.html` | Finans aracı/sektörü kaynak sayfaları var | Ana site haritasına site geneli link spam’i yok | KAYNAK_PASS |
| `llms.txt` | Finans rehberleri zaten listeleniyor | Yeni 'GEO özel dosyası' oluşturulmadı | KAYNAK_PASS |
| `content-manifest.json` | 2026-10-09 kaynak envanteri; tam Google indeks kanıtı değil | Değişiklik yok | KAYNAK_PASS |
| Yeni özel sayfa | Mevcut main’de yok | Tek H1, özgün meta, self canonical, `index,follow`; hiç `Product/SoftwareApplication Offer` schema yok | KOD_KONTROLU |
| `200/404` | Staging repo gerçek dosya / QA | Yeni URL main’de canlı değil, canlı HTTP BİLİNMİYOR | TEST EDİLEMEDİ |
| Search Console | Mülkiyet ve sorgu paneli okunamadı | Yayın sonrası bile indeks garantisi yok | BİLİNMİYOR |

Not: Google Search Central canonical tercihi bir ipucudur, garanti değil: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls . Google gerçek önemli sayfa güncellemeleriyle tutarlı `lastmod` önerir: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=tr .

## Yasak/izin
**ONAY BEKLİYOR:** sitemap, indekslenebilir sayfa ve canlı site güncellemesi. Kaynaklardan sistemin vergi/ödeme uygunluğu çıkmaz. Yeni sayfa bir hizmet kararı açıklamasıdır, dijital ürün satış aktivasyonu değildir.
