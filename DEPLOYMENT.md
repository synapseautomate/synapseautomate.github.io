# Deployment

Target repository: `synapseautomate/synapseautomate.github.io`
Target branch: `main`
Publishing source: GitHub Pages from `main` / root.

## Verified package deployment
1. Keep `.github/` from the repository; site packages never overwrite workflow files.
2. Create a rollback branch before replacing public content.
3. Verify package SHA-256 and ZIP integrity.
4. Run `python3 scripts/site_qa.py`, UTF-8 scan, secret scan and `git diff --check` before publish.
5. Replace site files only after all checks pass.
6. Verify desktop + mobile navigation, CTA/contact handoff and the styled/human site directories after Pages updates.

## QA

```bash
python3 scripts/site_qa.py
```

Expected: `SITE QA: PASS — 32 HTML pages`.
