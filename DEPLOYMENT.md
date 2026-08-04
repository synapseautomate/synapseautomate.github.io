# Deployment

Target repository: `synapseautomate/synapseautomate.github.io`
Target branch: `main`
Publishing source: GitHub Pages from `main` / root.

## Replace-site deployment
1. Back up the existing repository or create a release tag.
2. Replace repository root contents with the contents of this package.
3. Commit: `site: launch Synapse Automate corporate platform v2`
4. Verify GitHub Pages deployment.
5. Open desktop and mobile URLs; test navigation, mail, telephone and WhatsApp links.
6. Submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools.

## QA

```bash
python3 scripts/site_qa.py
```

Expected: `SITE QA: PASS — 24 HTML pages`
