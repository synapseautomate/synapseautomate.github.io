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
