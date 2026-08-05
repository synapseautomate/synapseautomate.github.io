# Synapse Automate Corporate Site v3

Production-oriented static corporate site for `https://synapseautomate.github.io/`.

## Source grounding
- Kinetra Group Investor Presentation — June 2026.
- SYNAPSE Day 1 mobile guide and RevenueOS acceptance rules.
- Public content separates current capabilities, documented implementation patterns, planned group layers and management targets.
- Home Services / Roofing is presented as one sector implementation pattern, not as an exclusive active vertical.
- Financial targets and roadmap figures are labeled as management scenarios, not realized performance or guarantees.

## Information architecture
- Corporate homepage and trust model.
- 12 enterprise AI service areas.
- 8 investor-deck sectors plus Home Services / Roofing as an additional solution pattern.
- RevenueOS + AgentReady + Creative + MagnetFlow + VELA product architecture.
- Kilory, Kinetra Studios and Kinetra Group ecosystem pages.
- Investor relations, guides, privacy, terms, contact, human site directory and AI information profile.
- `robots.txt`, styled `sitemap.xml`, `llms.txt` and structured data for technical discovery.

## QA

```bash
python3 scripts/site_qa.py
```

Expected: `SITE QA: PASS — 32 HTML pages`.
