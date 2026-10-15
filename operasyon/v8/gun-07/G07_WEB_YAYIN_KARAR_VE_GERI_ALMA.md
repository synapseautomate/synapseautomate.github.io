# SYNAPSE V8 — Gün 07 web teslimi / yayın kararı / geri alma

Tarih: 2026-10-15. Referans: V8 PDF, **GÜN 07 / OPERASYON**, p. 21. Durum: **PR #23 KULLANICI İZNİYLE YAYINLANDI; HOST/LEGAL P0 İLE CANLI QA P1 AÇIK**.

## Kullanıcının yetkisi ve kapsam
Kullanıcı 2026-10-15'te mevcut canlı sitenin içeriğini, hiçbir eski sayfayı silmeden/bozmadan, PDF kapsamı içinde güncellemeye açık izin verdi; ayrıca yeni içeriğe **menü ve ilgili çözüm sayfasından doğal erişim yolu** istedi. Yayın izni vardır ancak PDF'nin teknik/barındırma koşullarının doğrulandığı anlamına gelmez.

## Yeni içerik ve doğal yollar
- Yeni, tamamı sentetik eğitim sayfası: `/kanit/stok-farki-baglam-kontrolu.html`; tek H1, kanonik kaynak ve gerçek logo, ücret/checkout/gerçek müşteri performansı iddiası yok.
- İndirilebilir temsili rapor: `/kanit/stok-farki-ornek-rapor.csv`, R01/R02/R03/R05; motor çalıştırılmış üretim sonucu olarak sunulmuyor.
- Doğal erişim A: Ana menü **Kaynaklar → Açık Kanıt → “Stok farkı her zaman kayıp değildir”** bağlantısı; `kaynaklar.html#kanit`.
- Doğal erişim B: **E-ticaret Operasyon Otomasyonu** sayfasındaki “Stok farkı örneği” bölümü; `cozumler/e-ticaret-operasyon-otomasyonu.html#stok-farki-ornek`.
- `sitemap.xml` sonuna kanonik URL eklendi. Mevcut girdiler korunuyor.

## Teknik kalite kontrol / iddia sınırları
- Kaynak dosyaları yeniden okunarak karşılaştırılmalı. Ana sayfa, mevcut kategori ve teklif yolları korunmalı.
- Statik kontrol: başlık, canonical, OG, gerçek logo dosyası, internal href ve CSV yapısı, no checkout/ücret iddiası, gizlilik bağlantısı.
- Ekran QA: altı viewport ve klavye odağı / karşılaştırma paneli; tarayıcı testinin hangi revizyonda koştuğu ayrıca işaretlenmeli.
- **Gerçek iPhone Safari, FormSubmit gönderimi, ödeme, canlı HTTP/404, GA4 ve KVKK/cookie ağı** testleri yapılmadıysa PASS sayılamaz.
- Eski pratik örnek “12 sipariş/8 stok” kayıp kanıtı değil; zaman-depo-rezervasyon bağlamına dikkat çekmek için sentetik değer.
- Bu örnek **çalışan otomasyon veya gerçek müşteri teslimi değildir**.

## Açık P0/P1 ve yayın kapısı
**HOST-01 P0:** GitHub Pages resmî kullanım şartı, ücretsiz Pages'in ticari iş/e-ticaret/SaaS işletilmesi için kullanılmaması gerektiğini belirtiyor: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits . Mevcut işletme sitesinin barındırma uyumu ayrı doğrulanmadı; Cloudflare Pages ücretsiz statik dağıtım alternatifi olabilir ama hesap, alan adı ve uygunluk teyidi yok. https://developers.cloudflare.com/pages/platform/limits/
**LEGAL-01 P0:** Fatura/vergi statüsü kullanıcı beyanı ve yetkili teyidi olmadan doğrulanmış sayılmaz. Ödeme eklenmedi.
**MOBILE-01 P1:** Gerçek Safari testini kullanıcı cihazında belgelemek gerekir.
**PRIVACY-01 P1:** Canlı ağ/çerez/ölçüm doğrulaması.
**LINK-01 P1:** Yalnız tam canlı yayından sonra HTTP + 404 + görsel link kontrolleri geçerli.
**Yayın yönergesi:** PDF Gün 07 adım 04 “yalnız branch/PR”, açıkça “canlıya geçme” der; kritik P0/P1 varken “yayına hazır” denemez. Kullanıcının yayına izin vermesi yayının otomatik olarak güvenli/uyumlu olduğu anlamına gelmez.

## Geri alma / yayın hazırlığı
**PR #23 squash merge ile ana dala aktarıldı.** Yayın commit'i: `3e93a293913344750be455ac595f732655ac9353`. Önceki ana dal commit'i: `7d51dbb2c4d167c96a3f1a7fd968ea0e16588f44`. Bu bölümdeki adımlar yayın sonrası geri alma kontrol listesi olarak uygulanır.
Geri alma veya yeni yayın gerektiğinde:
1. Yayından önce ana dal commit SHA'sı, ilgili 5 dosyanın blob SHA'ları, 6 viewport ekranları ve başarılı test komutları kayda alınır.
2. Yalnız bu özellik dalındaki değişiklikler kontrol edilerek birleştirilir; önceki geniş kapsamlı PR #22 otomatik birleştirilmez.
3. Beklenmeyen davranışta merge/squash commit SHA üzerinden `git revert <commit>` (uygun durumda `git revert -m 1 <merge_sha>`) için ayrı PR oluşturulur. Kullanıcı onayı olmadan geriye dönüş canlıya geçirilmez.
4. Revert sonrası HTTP, menü, köprü bağlantıları, mobil ve 404 QA yeniden yapılır.
5. **Geri alma prosedürünün varlığı, gerçek canlı revert provası değildir**.

## Kaynak ve metrik
Repo: https://github.com/synapseautomate/synapseautomate.github.io
Dalı: `feat/v8-g07-stock-context-public-20261015`.
Yayın hedefi: https://synapseautomate.github.io/kanit/stok-farki-baglam-kontrolu.html . PR: https://github.com/synapseautomate/synapseautomate.github.io/pull/23 . GitHub Pages dağıtım iş akışları başarıyla tamamlandı; bağımsız HTTP / gerçek Safari kontrolü henüz doğrulanmadı.
Yayımlanmış ziyaretçi, lead veya dönüşüm metriği: **BİLİNMİYOR**. Sosyal yayınlar kullanıcının beyanı düzeyinde kayıtlı.

## 2026-10-15 — PR #23 teknik ve editoryal QA sonuçları (feature HEAD)

- **Taslak PR:** https://github.com/synapseautomate/synapseautomate.github.io/pull/23 ; HEAD: `47f99d3c001cecf5ff355157759ea5ade4a3f9cb` (bu satır eklendiği andaki sürüm; yeni belge commit'i HEAD'i değiştirir).
- **1. tur / statik teknik denetim: 19/19 PASS.** GitHub commit ağacında yeni dosyalar ve yedi yerel link/görsel hedefi bulundu; canonical, description, OG, tek H1, gerçek logo, iki gelen kaynak bağlantısı, sitemap tekil URL, örnek CSV yedi kolon ve sentetik sınır doğrulandı. Sayfada veri toplayan form, checkout, veya kullanıcıya gösterilen iç gün/QA notu bulunmuyor.
- **2. tur / geriye dönük içerik denetimi: 6/6 PASS.** `kaynaklar.html`, `cozumler/e-ticaret-operasyon-otomasyonu.html` ve `sitemap.xml` yeni ekleme parçaları çıkarılınca `main` sürümleriyle **birebir aynı**; `index.html`, `hizmetler.html` ve `gizlilik.html` aynı blob SHA'larını koruyor. PR dosya listesi 6 dosya: 3 eklenen kaynak/belge, 3 var olan dosyaya yalnız ekleme; silinen dosya yok.
- **QA kapsamı sınırı:** Bu rakamlar GitHub kaynak/bağlantı denetimleridir. Yayımlanmamış PR'yi gerçek iPhone Safari üzerinden, canlı HTTP veya 404 sunucu cevabı üzerinden PASS göstermeyin. Geçmişteki benzer yerel HTML viewport kayıtları **bu commit için** birebir mobil test kanıtı değildir.
- **P0 kararı:** HOST-01 ve LEGAL-01 açık; PDF Gün 07 yalnız PR'yi öngörüyor. **Bu satır PR incelemesi sırasındaki tarihsel karardır.** Kullanıcının daha sonraki açık canlı yayın izniyle bu PR yayımlandı; P0/P1 uygunluk kapanmış sayılmadı.


## 2026-10-15 — CANLI YAYIN GERÇEKLEŞME KAYDI (GÜNCEL)

- **Yetki:** Kullanıcı mevcut `synapseautomate.github.io` adresinden devam edilmesini ve mevcut sayfalar silinmeden/bozulmadan eklemelerin canlıya alınmasını açıkça istedi. Barındırma taşınması ve ödeme entegrasyonu istenmedi. Bu istek PDF'nin Gün 07 'yalnız PR' yayın sınırını **yayın eylemi bakımından** daha sonra değiştirdi; bunun dışında PDF'nin kanıt ve risk şartları aynen açıktır.
- **Kapsam:** Sadece PR #23 birleştirildi. PR #22 birleştirilmedi; mevcut eski içerikler korunarak üç dosya eklendi, üç mevcut dosyaya bilgi/navigasyon eklemesi yapıldı; silme yok.
- **GitHub birleşme:** `main` squash commit `3e93a293913344750be455ac595f732655ac9353`; önceki `main` `7d51dbb2c4d167c96a3f1a7fd968ea0e16588f44`. Güncel yayın linki `https://synapseautomate.github.io/kanit/stok-farki-baglam-kontrolu.html`.
- **Site içi keşif:** `/kaynaklar.html#kanit` içindeki 'Açık Kanıt' kartı ve `/cozumler/e-ticaret-operasyon-otomasyonu.html#stok-farki-ornek` içindeki 'Stok farkı örneği' bağlantısı; her iki kaynak `main` üzerinde mevcut. `sitemap.xml` tekil giriş eklendi. CSV bağlantısı yalnız temsili veri indirir.
- **CI / dağıtım kanıtı:** Merge commit'inde GitHub Actions `quality-gate`, `integrity`, standart `pages build and deployment` ve `Deploy Current Main to GitHub Pages` sonuçları **SUCCESS**. GitHub `main` dosyalarından sayfa ve Kaynaklar menü bağlantısı geri okundu.
- **QA sınırı:** GitHub'ın başarılı deploy bildirimi = son kullanıcının Safari/HTTP testi değildir. Bu ortamdan canlı Pages URL'sinin HTTP durumunu ve gerçek iPhone Safari görünümünü bağımsız teyit edemedik. `LINK-01`, `MOBILE-01` ve `PRIVACY-01` kanıt bekliyor. Gerçek form talebi ve analitik sonuç sayılmadı.
- **Geri alma:** Sadece yayın commit'i `3e93a293913344750be455ac595f732655ac9353` hedeflenerek yeni bir düzeltme/revert PR'si hazırlanır; otomatik revert yapılmaz. Önceki çalışan commit `7d51dbb2c4d167c96a3f1a7fd968ea0e16588f44` korunmuştur. Revert provası yapılmadı.
- **Uygunluk:** GitHub Pages'in ticari çevrim/sunum kısıtı (HOST-01) ve fatura/tahsilat uygunluğu (LEGAL-01) **P0 açık**. Kullanıcının adresi koruma isteği, resmî barındırma şartlarının karşılandığı anlamına gelmez. Bu yüzden **Gün 07 bütün olarak CLOSED değildir**; tamamlanan tek eylem yeni bilgilendirici içeriğin canlıya alınmasıdır.
