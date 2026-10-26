# SYNAPSE V8 Gün 17 — QA B: bağımsız marka, UX, erişilebilirlik, yayın kapısı

**Tarih:** 26.10.2026. **Kamuya yazma/gönderme:** YAPILMADI.

| Alan | Durum | Ölçülen veya incelenen |
|---|---|---|
| Teknik içerik doğru kapsam | GEÇTİ (statik kaynak) | Tek rol, doğru kaynak sürümü, yetki kontrolü, maliyet belirsizliği ve insan onayı anlatımı |
| Sentetik etiket ve doğrulanmamış sonuç | GEÇTİ (statik kaynak) | 'SENTETİK ÖRNEK / GERÇEK MÜŞTERİ VERİSİ DEĞİL' mevcut; gerçek müşteri/ROI yüzdesi yok |
| Marka/telif | GEÇTİ (yeni fark) | Rakip logosu, harici fotoğraf/müzik/font, iç QA notu veya eğreti 'SYNAPSE / Automate' kullanımı eklenmedi |
| Kaynak H1, canonical, CTA | GEÇTİ (statik) | İki HTML H1 tek; rehberin self canonical'i sabit; hizmet 09 iç linki taslakta var |
| Kontrast örnekleri | GEÇTİ (seçili CSS renk ikilileri) | normal metin #f2f8fb/#06111f **17.69:1**, paragraf #ccdae2/#0d2234 **11.34:1**, sessiz metin #a9bdc8/#0d2234 **8.34:1**, bağlantı #8cece4/#06111f **13.75:1**. Bu tam renk paleti/grafik WCAG sertifikası değildir |
| Altı viewport: 320/375/390/768/1024/1440 px | **TEST EDİLEMEDİ** | Güncel PR branch gerçek tarayıcı görselleri oluşturulmadı |
| Klavye ve ekran okuyucu | **TEST EDİLEMEDİ** | focus/Tab/Enter, touch target ve screen reader gerçek etkileşim testi yok |
| HTTP, 404, site yönlendirmesi | **TEST EDİLEMEDİ** | site doğrudan web erişiminde hata; git dosya yolu bulunması HTTP başarısı değildir |
| Lighthouse / gerçek LCP, INP, CLS | **TEST EDİLEMEDİ** | CrUX, PageSpeed saha verisi ve Lighthouse gerçek çıktısı yok |
| Gizlilik / ölçüm | GEÇTİ (yeni kod farkı) | hiçbir yeni form, cookie, localStorage veya ileti izni uygulaması eklenmedi. Mevcut JS'nin tüm KVKK durumu ayrıca incelenmeli |
| Sözleşme, gerçek KYC/IBAN, satış | HOLD | ürün/satış yetkisi, fatura ve platform gerçek onayı yok |
| Algoritma/sıralama/ROI sonucu | **BİLİNMİYOR** | gerçek GSC/GA4/satış paneli erişimi yok |

## Sınıflı açık kalemler
- **P0**: Yeni iki sayfalık dar metin/link farkında kaynak kontrolünde saptanan P0 = 0; **tüm site için 0 P0 garantisi yok**.
- **P1 doğrulama kapısı**: gerçek responsive, focus, görsel taşma, ekrandan erişim ve HTTP testi eksik. Sorumlu: UX+teknik QA. Belirlenmiş bir grafiksel taşma kusuru ile eksik test aynı şey değildir.
- **P2**: geçmiş canonical/noindex köprüleri, belirsiz GSC organik talep, 112 regex iddia adayının insan kaynak incelemesi. Sorumlu: SEO/editoryal.

**QA kararı:** Statik taslak hazır. **Teknik canlı yayın = HOLD** (gerçek tarayıcı/URL testi eksik). **Ticari satış = HOLD**. **PR #46 draft; sosyal paylaşım kotası 0.** Yeni web eylemine ayrı onay yok.
