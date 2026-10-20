# QA A — Kaynak, arama niyeti, kanonik ve metrik doğruluğu

20.10.2026; plan 24.10.2026. Test zemini `main` SHA cfbcd0c4bb9c084771b9562291b52a95a2c2c339; draft dalı son commit ve gerçek sonuç CI’dan ayrı kaydedilir.

| Kontrol | İlk kaynak incelemesi | Nihai durum |
|---|---|---|
| Gerçek hizmette fatura ön işleme / mutabakat desteği | `hizmetler.html` mevcut metinde var | KAYNAK_PASS |
| Finans sektörü insan onayı / tavsiye sınırı | `sektorler/finans-bankacilik.html` | KAYNAK_PASS |
| Yeni fatura farkı örneği | Dört işlem kaynakları sentetik; çalışan CRM/ERP yok | KAYNAK_PASS |
| Tek sorgu, title/H1/canonical, 2 sitemap | Kodda özgün; çift sitemap kaydı planlanmadı | CI bekliyor |
| 146 sayfa envanteri / yanlış 0 | repo Git tree gerçek 146 HTML; full metadata CSV CI üretecek | ENVENTER_PASS; FULL_QA_BEKLIYOR |
| GSC organik trafik, indeks, sıralama | Gerçek yetkili Search Console paneli yok | BİLİNMİYOR |
| Kod kontrol `site_integrity.py/site_qa.py/day8_quality_gate.py` | CI workflow eklendi | TEST_EDİLEMEDİ; CI sonucu şart |

İddialar gerçek kaynak kodla sınırlı; Google Search Central resmî kaynak: https://developers.google.com/search/docs/fundamentals/creating-helpful-content .
