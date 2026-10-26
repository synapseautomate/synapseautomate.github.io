# Gün 17 — QA TUR A: kaynak, teknik tutarlılık ve veri
**Tarih:** 26.10.2026 | **Plan tarihi:** 30.10.2026. **Repo main:** 6de1c4ad10feef1fef37e93d2731dad5e7886574. **İnsan/dış model veya platform testi:** yapılmadı.
## 1. Gerçek uygulanan kontroller
1. GitHub recursive tree kaynağı 150 HTML / 428 dosya; eski 144 / 389 sayımı güncel değil. Tam envanter 150 dosya yolu + sha + boyut; **yalnız 14 HTML'nin meta/title/H1/canonical/CTA içeriği** incelendi, kalan 136 için 'META_TEST_EDILEMEDI' yazıldı. Bu tam 150 sayfa semantik QA tamamlandı iddiası DEĞİLDİR.
2. `veri/public-content-version-registry-v1.json`: 27 asset, generated_at 2026-10-13. Depodaki `scripts/check-public-content-freshness.py` şartlarının JS ile eşdeğer kontrolü 26.10.2026 tarihinde **27/27 PASS**; review_due tarihi geçmiş current yok; external_expert_reviewed değerleri boolean. Python dosyasının kendisi bu çalışmada yerel olarak çalıştırılamadı; 'Python PASS' iddia edilmez.
3. Sitemap XML `<loc>` sayımı 131; tek başına 150 HTML'nin indekslenmesi veya sitemap hatası değildir. Mevcut hedef `/rehberler/ai-surec-denetimi.html` sitemap içinde yer alıyor.
4. Yeni taslak `rehberler/ai-surec-denetimi.html`: `<h1>` 1 adet, canonical 1 adet ve eski URL korunmuş, kendi meta title/description güncellenmiş; `index` robots korunmuş; yerel `../cozumler/kurumsal-ai-operasyon-denetimi.html` hedefi main'de mevcut; PUBLIC içerikte 'Gün 17', 'QA TUR', 'PR #' ibaresi yok.
5. Sentetik altı senaryo veri negatif kural kontrolünde: eski sürüm PASS alamaz; ziyaretçi yetkisiz erişim PASS alamaz; varsayılan kullanım limiti üzerindeki vaka PASS alamaz. Sonuç: A01 PASS, A02/A05/A06 HOLD, A03/A04 STOP. Bunlar model inference sonuçları değil, test tasarımındaki beklenen politikalardır.
6. Fiyat, ödeme, onay akışı, global JS, sitemap, schema, hizmet sayfaları ve Gün 01–07 dosyaları değiştirilmedi.
7. GitHub statik sayfalarda kaynak karşılaştırmaları: doğruluk/güvenlik/maliyet sözcüklerinin varlığı yeterli değil; belgedeki örnek ilgili kaynak/rol/tavan koşullarını açıklıyor. Altı satırdan performans ölçüsü çıkarılmadı.
8. Resmî teknik dayanak: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls ; https://developers.google.com/search/docs/fundamentals/creating-helpful-content ; https://developers.google.com/search/docs/appearance/core-web-vitals

## Gerçek sonuçlar
| Kontrol | Sonuç | Kanıt |
|---|---|---|
| Dosya envanteri | PASS | 150 HTML satırı, GitHub main kaynak ağacı |
| 150 HTML'nin tüm meta/görsel/CTA verileri | TEST EDİLEMEDİ | sadece 14 HTML açıldı |
| Tazelik mantığı | PASS | 27 asset eşdeğer mantık kontrolü, Python komutu çalıştırılmadı |
| Canonical/tek H1/yalnız bir URL | PASS | kaynak değişkenleri assert ile doğrulandı |
| 6 sentetik karar kuralı | PASS | altı sentetik satır, negatif koşul |
| Canlı ölçüm/GSC veya gerçek model testi | TEST EDİLEMEDİ | yetkili platform ve gerçek müşteri izni yok |
| 150 sayfada kanıtsız iddia=0 | TEST EDİLEMEDİ | kapsam eksik |

## Açık teknik kusur ve önlem
- **P1 / SAHİP: Teknik QA:** Tam 150 HTML meta/idda/bağlantı kontrolü yapılmadı (136 eksik). Tamamlanmış denetim veya P0=0 site geneli ilan edilmez.
- **P2 / SAHİP: SEO:** GSC sorgu örneklemi ve gerçek organik trafik BİLİNMİYOR; hipotez olarak kalır.
- İlk 14 sayfanın bazı nicel kanıt cümleleri `SEO-KANONIK-IDDA-KUSUR-DEFTERI.csv` içinde inceleme adayı; sentetik vaka verisi üretim başarısı sayılamaz.

## Tekrar edilebilir gerçek komutlar
- `python3 scripts/check-public-content-freshness.py` — **ÖNERİLEN, BU OTURUMDA DOĞRUDAN ÇALIŞTIRILMADI**.
- `python3 -m http.server 8000` ardından altı viewport + keyboard/URL istek testi — **ÖNERİLEN, HENÜZ ÇALIŞTIRILMADI**.
- Bu turda icra edilen eşdeğer kaynak kontrolü: JS koşulu `status==="current" && review_due_at < "2026-10-26"` ve `typeof external_expert_reviewed === "boolean"`; 27 asset, uygunsuz=0.
