# Gün 11 — Eski `site_qa.py` 191 bulgu triyajı

**Kaynak:** GitHub Actions gerçek logu, [Gün11 QA](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/39387512587) / `legacy_site_qa.log`; işlenen **20.10.2026**. Exit **1 = FAIL**. Bu başarısızlık hiçbir yerde PASS yapılmadı. `site_integrity.py`, `day8_quality_gate.py` ve ayrı Gün 11 yeni rota QA'nın başarıları farklı kapsamdır.

| Tür | Eski test bulgusu | Gerçekliğe göre ayrım | Plan / sahip |
|---|---:|---|---|
| Teknik kısaltma/jargon | 130 | Otomatik regex sayımı; bazıları gerçek okunabilirlik sorunu, bazıları konuya uygun ve açıklanabilir teknik terim; her bulgu P0 değil | Site UX editörü; kullanıcı sayfasında tek tek okuma |
| Site haritasını teknik kaynak sayan eski navigasyon varsayımı | 11 | `site-haritasi.html` mevcut public navigasyonda bilinçli erişim rotası; eski script bunu gereksiz teknik saymış olabilir | Test sahibi; işlevsel sayfa haritasını körlemesine kaldırma |
| Sitemap'te gizli/noindex sanılan dosyalar | 2 | `site-haritasi.html` ve `ai-bilgi.html` gerçek kaynakta `index,follow` ve self canonical taşıyor; eski scriptin hard-code ayırımıyla çelişiyor. Gerçek Google seçimi BİLİNMİYOR | Site QA sahibi; noindex kararını HTML ile karşılaştır |
| Eksik metadata işaretleri | 11 | Eski sayfalardaki gerçek meta eksikleri olabilir; **özellikle Google doğrulama dosyasına HTML title/meta eklemek gerekmez** | Site QA / içerik sahibi; ayrı kontrollü eski sayfa düzeltmesi |
| Önceki ürün mimarisi/fiyat metni beklentisi | 13 | Eski satış sürümü/sabit fiyatlar güncel satıcı/fatura kapısına aykırı olabilir; doğru iş eski fiyatları geri eklemek DEĞİL | Test sahibi + ticari yetkili |
| Eski müşteri sözleşmesi/senaryosu token beklentisi | 17 | Kaynak sözleşme öncekine bağlı, mevcut çözüm için doğrulama gerekir; müşteri sonucu iddiası üretilmez | Test sahibi, ayrıca ürün yetkilisi |
| Ana sayfada tam sektör etiketi eşleşmesi | 7 | Değişen yazım/etiket/IA kaynaklı olabilir; gerçek kullanıcı yolu ve sektör URL'si ayrı kontrol edilmeli | Bilgi mimarisi sahibi |
| **TOPLAM** | **191** | Tek tek triyağa ayrılmadan tamamen çözüldü DENEMEZ | Gün 12 teknik borç |

**Yeni Gün 11 sayfasındaki tek eski jargon regex bulgusu**: 'ERP' içeriğiydi; kullanıcıya dönük metinde “muhasebe yazılımı/banka bağlantısı” ile değiştirildi. Gelecek Actions logunda bu dar düzeltmenin sonucunu yeniden kontrol et. `site_qa.py` test dosyası veya önceki fiyatlar bu PR'da değiştirilmedi.

**Açık risk:** Eski scriptin 191 bulgusu hem muhtemel gerçek meta/erişilebilirlik borcunu hem eski iş kapsamı varsayımını karıştırıyor. **Bu test fail olmaya devam eder**; CI'da log olarak tutulup Gün 11 dar kapsamını ölçen yeni test ayrıca çalıştırılır. Veri/hukuk/platform kapsamı bu ayıklamayla kapanmaz.

**Yayın kararı:** Gün 11 sayfası, hizmetler iç linki, sektör iç linki, sitemap merge **ONAY BEKLİYOR**. Ana dalı kapatmadan ayrı QA iyileştirme PR hazırlanabilir; hesap sahibinin onayı olmadan canlı içerik değişmez.
