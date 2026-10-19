# QA A — kaynak, teknik, negatif test ve metrik — 19.10.2026
## İncelenen kod
- Main SHA fb7cbbd77abf2abe5cb0b201cec83799e9338558; taslak yayın PR#28 head be2b2b040f95aeba64d2229984d09eff992a77ab; iç arşiv PR#27.
- FormSubmit HTML POST (süreç), JS FormSubmit (iletişim), teşekkür redirect ve olaylar (`asset_view`, `lead_form_submit`, `generate_lead`) kaynakta kontrol edildi.
- PR#28 JS kapalı iletişimde HTML action POST ile FormSubmit'e gidebiliyor; JS açıkken action/consent görsel açıklaması uyumlu (statik inceleme PASS). E-posta teslimi TEST_EDİLEMEDİ.
- Consent öncesi GA4/localStorage başlangıcı yeni taslakta bloke edildi; kullanıcı izin / ret / iptal tarayıcı testi yapıldı (staged Chromium PASS, hukuk ayrı).
- UTM lower-case/token kuralı; boş/garip parametrelerle kişisel veri sızdırmama hedefi kodda var. Etkin kullanıcı panel doğrulaması yok.
## Gerçek GitHub Actions kanıtı
- Site Integrity QA: **PASS**; orphan/sitemap kontrolü. https://github.com/synapseautomate/synapseautomate.github.io/pull/28
- Day 8 Commercial SEO Quality: **PASS** (yalnız SEO/kanıt taraması).
- Synapse Release Preflight: **PASS** (son komitte), çalıştırma https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/39237109324
- Komutlar: python scripts/site_integrity.py; python scripts/day8_quality_gate.py; node scripts/day28_browser_smoke.mjs; node scripts/qa_consent_local.mjs; node scripts/day1_browser_funnel.mjs
- Son testte önce açık rıza, sonra sentetik FormSubmit POST mock'u kullanıldı; gerçek müşteri formuna veri gönderilmedi. Simüle `generate_lead` gerçek inbox teslimi değildir.
## Sonuç
- PASS (kod/CI): site repo link graph, sitemap, 6 ekran genişliği Chromium responsive, consent sentetik negatif akış, 0/BİLİNMİYOR ayrımı.
- FAIL/AÇIK P0: gerçek KVKK hukuk yorumu, üçüncü taraf FormSubmit tesliminin alıcıda kanıtlanması, GitHub Pages ticari barındırma uygunluğu, satış/fatura P0.
- TEST_EDİLEMEDİ: GA4 DebugView yetkili hesabı, GSC, LinkedIn şirket analitiği, üretim HTTP ve gerçek ziyaret; Lighthouse gerçek prod.
## Kanıtlı hata giderimi
- İlk Release Preflight başarısızlığı: eski sentetik test, izinsiz `generate_lead` istiyordu; event üretimi consent kapısı arkasında doğru olduğu için test opt-in ile yenilendi ve en son CI PASS.
- Bu QA, formun gerçekten teslim edildiğini veya KVKK açısından uygun olduğunu söylemez.

## Son CI artefakt kanıtı / 19.10.2026
- Web PR#28 commit `16a5b533dda256963877c1226d76be1a2dad7d92`; üç GitHub Actions: Site Integrity PASS / Day8 SEO Quality PASS / Release Preflight PASS. https://github.com/synapseautomate/synapseautomate.github.io/actions/runs/39239458222
- `synapse-public-preview-no-internal` 12180681388 indirilip ZIP içeriği açıldı: 280 dosya, kritik 6 rota tamam, operasyon iç dosya 0, devri dosya 0.
- `preflight-mobile-screenshots` artefaktı 12180139149 (6 kritik genişlik dahil gerçek staging Chromium).
- QA A sonucu: source/paket/dependency PASS; PROD network, gerçek GA4/GSC/posta verisi TEST_EDİLEMEDİ.
