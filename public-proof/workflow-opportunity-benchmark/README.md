# Synapse Automate — Workflow Opportunity Benchmark

**30 tekrarlı operasyon iş akışını, teknoloji seçmeden önce aynı karar çerçevesinde değerlendiren public proof paketi.**

> **Kanıt statüsü:** Bu çalışma sentetik ve iş-akışı seviyesindedir. Müşteri performans verisi, müşteri başarı hikâyesi veya ROI garantisi değildir.

## Kamuya açık kaynaklar

- **Canlı karar tablosu:** https://synapseautomate.github.io/rehberler/ai-otomasyon-is-akisi-karar-tablosu.html
- **Ücretsiz süreç haritalama aracı:** https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html
- **Ücretli Süreç Analizi:** https://synapseautomate.github.io/surec-analizi.html
- **30 satırlık public CSV:** https://synapseautomate.github.io/veri/gun4-workflow-inventory-public.csv
- **Puanlama metodolojisi:** https://synapseautomate.github.io/veri/gun4-workflow-opportunity-methodology.md

## Kapsam

- 30 tekrarlı operasyon iş akışı
- 8 değerlendirme boyutu
- Para yakınlığı ve veri erişimine çift ağırlık
- Risk ve uzun satış çevrimine negatif ağırlık
- Kritik kararlar için açık insan kapısı
- İlk 10 fırsatın karşılaştırmalı görünümü

### Kategori dağılımı

| Kategori | İş akışı sayısı |
|---|---:|
| E-Ticaret | 14 |
| Muhasebe | 6 |
| İhracat | 5 |
| Satın Alma | 5 |

## İlk 10 fırsat

| Sıra | İş akışı | Kategori | Puan | İnsan kapısı |
|---:|---|---|---:|---|
| 1 | Pazaryeri feed hata triage | E-Ticaret | 36 | Değişiklik/yayın insanda |
| 2 | Ürün katalog veri kalite kontrolü | E-Ticaret | 36 | Yayın insanda |
| 3 | Sipariş istisna triage | E-Ticaret | 35 | İade/ödeme/müşteri mesajı insanda |
| 4 | Fatura-PO eşleştirme ön kontrolü | Muhasebe | 34 | Muhasebe kaydı/onay insanda |
| 5 | Müşteri talebi önceliklendirme | E-Ticaret | 34 | Yanıt/taahhüt insanda |
| 6 | Stok tükenme sinyali | E-Ticaret | 34 | Sipariş/tedarik kararı insanda |
| 7 | Cari mutabakat fark triage | Muhasebe | 33 | Düzeltme/kayıt insanda |
| 8 | Tedarikçi teklif karşılaştırma | Satın Alma | 33 | Tedarikçi seçimi insanda |
| 9 | Sepet terk neden analizi | E-Ticaret | 32 | Deney/yayın kararı insanda |
| 10 | İade talebi ön sınıflandırma | E-Ticaret | 32 | İade kararı/ödeme insanda |

> Puan yalnız **keşif önceliğini** sıralar. Satış, ROI, doğruluk veya otomasyon başarısı garantisi değildir.

## Opportunity Score

```text
acı + sıklık + (2 × para yakınlığı) + (2 × veri erişimi)
+ ölçülebilirlik + dağınıklık - risk - satış çevrimi
```

Detaylı metodoloji: [`veri/gun4-workflow-opportunity-methodology.md`](../../veri/gun4-workflow-opportunity-methodology.md)

## İnsan denetimi sınırı

AI; sınıflandırma, özet, taslak, ön kontrol veya sinyal üretebilir. Fiyat/ödeme, müşteri taahhüdü, hassas veri, hukuki-tıbbi-finansal kararlar, geri döndürülemez dış eylemler ve yüksek etkili belirsiz kararlar insan onayında kalır.

## Nasıl kullanılır?

1. Public CSV’den kendi operasyonunuza en yakın iş akışını bulun.
2. Para yakınlığı, veri erişimi, ölçülebilirlik ve riski değerlendirin.
3. AI’ın yapacağı kısmı ve insanın onaylayacağı kısmı ayırın.
4. Önce ücretsiz araçla süreci haritalayın.
5. Ekonomik olarak anlamlıysa Süreç Analizi’ne geçin.

Bkz. [`USAGE.md`](USAGE.md) ve [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md).

## Tek source of truth

Bu klasör kanıt vitrini; kaynak veriyi kopyalamaz:

- [`veri/gun4-workflow-inventory-public.csv`](../../veri/gun4-workflow-inventory-public.csv)
- [`veri/gun4-opportunity-scorecard.csv`](../../veri/gun4-opportunity-scorecard.csv)
- [`veri/gun4-workflow-opportunity-methodology.md`](../../veri/gun4-workflow-opportunity-methodology.md)
- [`rehberler/ai-otomasyon-is-akisi-karar-tablosu.html`](../../rehberler/ai-otomasyon-is-akisi-karar-tablosu.html)

Makinece okunabilir manifest: [`proof-manifest.json`](proof-manifest.json)

## Sonraki adım

Ücretsiz haritalama: **https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html**

Uygun görünüyorsa Süreç Analizi: **https://synapseautomate.github.io/surec-analizi.html**

---

**Synapse Automate** · Kurumsal AI otomasyonu · İnsan denetimi · Ölçülebilir iş akışları  
https://synapseautomate.github.io/
