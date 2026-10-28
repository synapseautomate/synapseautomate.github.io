# QA B — Bağımsız grafik/erişilebilirlik/hukuki kontrol
**28.10.2026** · Operatör.
## Otomasyon gerçek ekran kanıtı
Chromium kaynak checkout: [GitHub Actions run 40659256869](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659256869), ekran artefaktı [id 12803231704](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659256869/artifacts/12803231704).
- Genişlikler: **320,375,390,768,1024,1440**. Kritik kaynak sayfaları: index, hizmetler, yeni sesli AI, iletisim, surec-analizi, talep-alindi, 404 — toplam 42 otomasyon sonucu **PASS**.
- H1 adedi 1, resimde eksik alt 0, yatay taşma yok ve yerel kaynak HTTP 200; 42 screenshot tutuldu. **Bunlar yerel Chromium, canlı HTTP değil.**
- Yeni sayfanın varsayılan renk çiftleri için bağımsız WCAG kontrast hesaplaması: normal ana metin/arka plan 17.45:1; muted/panel 9.88:1; birincil CTA koyu/cyan 13.44:1 — üçünün de AA eşiğinin üstünde.
- Yeni sayfada nav linkleri 44px ve CTA 48px CSS minimum hedef. Gerçek dokunmatik cihaz/VoiceOver/Safari testi **TEST EDİLEMEDİ**.
- Klavyeyle tüm form alanlarının gerçek gezinme sırası ve 404 canlı HTTP/GA4 waterfall birebir denenmedi → **TEST EDİLEMEDİ**.
- Kaynakta lisanssız müzik, gerçek çağrı sesi veya taklit UI yok; sitenin gerçek logo dosyasına referans veriliyor. Görsel gerçek referans çıktı yerine kavramsal akış ve zorunlu SENTETİK etiketi.
- Hukuk: KVKK aydınlatma ve aktarım, FormSubmit üçüncü taraf sözleşmesi/bölge, çağrı kaydı/özel nitelikli veriler hesap sahibinin hukuki teyidine bağlı.
**KARAR:** Kaynak görsel tarayıcı QA geçti; canlı/Safari/teslim/ticari uygunluk HOLD. P0/P1 kapanmadan WEB yayınlama yok.


## 28.10.2026 kaynak güncellemesi — CI ve HTTP doğrulaması
- GÜNCEL ve üstün kanıt: GitHub Actions [run 40659965759](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759); [artifact 12802534718](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40659965759/artifacts/12802534718). Gerçek **salt-okunur HTTPS GET main**: ana sayfa, hizmetler, surec-analizi, iletisim, talep-alindi ve 404.html 6/6 **HTTP 200**; bulunmayan URL **404**; **YENİ taslak sesli AI URL canlıda 404 (beklenen)**. Bu testler gerçek FormSubmit POST veya checkout değildir.
- İki sürümden Chromium gerçek render: main-before ↔ draft-after `hizmetler.html` ve `surec-analizi.html`, 320/390/768/1440, **16 gerçek PNG** ve `before-after-summary.json`.
- [Commit e295052](https://github.com/synapseautomate/synapseautomate.github.io/commit/e295052a9476ac433afa828dbc46f48661ca9c6e) sonrası bağımsız CI workflow'ları: Site Integrity, Commercial SEO, Finance SEO, Day12 HR ve **Synapse Release Preflight = SUCCESS**, Gün19 Browser QA = SUCCESS. Önceki Release Preflight FAIL gerçek regresyondu, sonra yerel sentetik consent işaretlemesiyle düzeltildi; gerçek kullanıcı POST'u yok.
- Gün19 canlı yeni sayfa yayımlanmadı. Form başarı/inbox, canlı draft sayfa 200, gerçek Safari ve ödeme hâlâ **TEST EDİLEMEDİ / HOLD**.


## Son QA doğrulaması — 28.10.2026
- Eklenen **klavye gerçek Tab odağı** (`#main` skip link) ve 44 px dokunmatik hedef kontrolü dahil final Day19 Browser QA **SUCCESS**, [run 40660651653](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40660651653); [artifact 12803034739](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40660651653/artifacts/12803034739). 42/42 Chromium ekran rotası ve 16 before-after PNG; gerçek Safari/VoiceOver henüz TEST_EDİLEMEDİ.
- **Synapse Release Preflight SUCCESS**, [run 40660651781](https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/40660651781). Site Integrity, Commercial SEO, Finance SEO ve Day12 HR QA ayrıca SUCCESS. Başarısız önceki CI koşusu onay kutusu eklenmesine uyarlanan local simüle testle düzeltildi.
- **GO kararı verilmedi**: gerçek FormSubmit teslimi / veri aktarımı ve genel kamu ticari hazırlık kanıtı eksik; Gün19 sayfası main'de değil. ONAY BEKLİYOR.
