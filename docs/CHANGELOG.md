# Public Docs Değişiklik Kaydı

## 1.0.0 — 2026-09-30

- Kurumsal satın alma paketi v1 yayınlandı.
- Kamu veri akışı ve rol referansı yayınlandı.
- Olay yönetimi ve destek sınırı yayınlandı.
- Model ve geri dönüş politikası yayınlandı.
- Türkçe kamu fiyat sunumunda TL ve USD tutarlarının açıklamasız eşdeğer görünmesi kaldırıldı.

Müşteri, üretim doğruluğu, ROI, mevzuat uyumu veya sertifikasyon iddiası eklenmedi.

## 2026-10-06
- Added public-safe reusable template library.
- Added data/template-rights guidance and machine-readable rights registry.
- Explicitly separated customer data/confidential configuration from reusable delivery IP.
- No customer confidential material or customer outcome claims were added.

## 1.1.0 — 2026-10-07

- Added canonical public release notes with “what changed / why / who approves”.
- Added versioning and review policy with explicit internal-vs-external reviewer boundary.
- Added machine-readable public content version/freshness registry and stale-content checker.
- Added 7/14-day value review template for recurring work.
- No external expert review, customer retention, ROI, production performance or renewal outcome is claimed.

## 1.2.0 — 2026-10-07

- Added a single visible Resource Center that connects tools, guides, evidence, trust and templates.
- Rebuilt the Trust Center around authority, human approval, incident handling, rights and review boundaries.
- Replaced the placeholder human sitemap with a categorized public site map and added a technical evidence index.
- Deprecated legacy Synapse product routes from active indexing while preserving backward-compatible URLs.
- Standardized the clean Synapse logo and removed stale product references from current public surfaces.
- Added automatic Pages deployment on main updates with discovery/deprecation QA checks.
- No customer outcome, production accuracy, compliance certification, security guarantee, savings or ROI claim was added.

## 1.3.0 — 2026-10-08

- Reworked the Technical Evidence Index into an open-proof roundup that separates control-policy, regression and workflow-prioritization evidence.
- Added a GitHub-level Public Proof Index for technical readers.
- Versioned the Workflow Decision Benchmark package as 1.1.0 with an explicit packaging-only release note and machine-readable manifest.
- Added Pages artifact checks for the headline public-proof files linked from the live evidence index.
- Benchmark datasets and pinned result values were not changed.
- No customer outcome, production accuracy, ROI, uptime/SLA, compliance certification or external expert-review claim was added.

## 1.3.1 — 2026-10-08

- Made human-readable evidence pages the primary path from the Technical Evidence Index.
- Explicitly labeled Markdown, JSON and CSV destinations as raw technical files with visible extensions.
- Added an explanatory note that raw files can open as plain text/data in the browser.
- Added the 1.1.0 packaging note to the human-readable Workflow Decision Benchmark page.
- Benchmark datasets, rules and pinned result values were not changed.

## 1.4.0 — 2026-10-09

- Consolidated the legacy Finance sector URL into the current Finance & Banking canonical and removed the legacy URL from the sitemap.
- Made the 20-minute workflow map the primary free diagnostic entry point from the Resource Center.
- Added a dedicated Property Management Process Analysis offer and linked sector -> synthetic proof -> offer -> generic intake.
- Added a public-safe 12-month Kinetra portfolio decision framework that separates Synapse commercial validation, Studios portfolio discipline and Kilory product readiness.
- Traffic, form and paid-conversion outcomes remain unmeasured unless observed through connected analytics or authorized payment evidence.

## 1.4.1 — 2026-10-09

- Added confirmed lead measurement for the Process Analysis form.
- The form now marks a short-lived pending lead only after native form validation passes and the submit event fires.
- The thank-you page emits GA4 `generate_lead` only when the matching FormSubmit redirect returns in the same browser session within 30 minutes.
- Direct visits to the thank-you URL do not count as leads, and reloads do not double-count.
- Existing `lead_form_submit` remains a diagnostic submit-attempt event; it is not treated as a confirmed conversion.
- Aligned Process Analysis, pricing-guide and legal-sector price surfaces with the canonical offer ladder: 4,900 TL / $149, 24,900 TL / $750, and 14,900 TL / $449 monthly.
- TRY and USD are explicitly independent list prices, never an FX conversion.
- Hardened offer QA so viewport detection is attribute-order agnostic and the independent-currency boundary is machine-checked.

## 1.5.0 — 2026-10-10

- Consolidated Pages publish behind fail-closed source, canonical, offer, artifact hygiene and real Chromium mobile checks.
- IndexNow now notifies only after the canonical Pages deployment completes successfully; it can no longer mutate main or launch its own deployment.
- Added a static IndexNow ownership file and removed duplicate manual Pages redeploy workflow.
- Added an Ev Hizmetleri / roofing synthetic request-routing example (explicitly not real customer proof) and a dedicated Process Analysis offer.
- Connected existing sector + guide + synthetic example + offer + public site map; updated sitemap and version registry.
- No private GA4/GSC numbers, customer claims, made-up ROI, SLA promises or unverifiable outcomes were published.

