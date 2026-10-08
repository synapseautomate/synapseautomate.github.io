# Synapse Automate — Public Proof Index

Status: **public, non-confidential**  
Default evidence boundary: **synthetic, methodology, specification or reusable delivery evidence unless a file explicitly says otherwise**

Start with the live customer-facing index:

**https://synapseautomate.github.io/kanit/teknik-kanit-indeksi.html**

## What this directory is for

This directory exposes reproducible or inspectable artifacts behind Synapse Automate's public methodology pages: frozen test sets, benchmark summaries, schemas, human-approval examples, measurement dictionaries and delivery templates.

It is not a customer-results repository.

## Recommended starting points

| Package | What it demonstrates | What it does not demonstrate |
| --- | --- | --- |
| `reliability-regression-v2/` | Frozen synthetic regression, explicit stop conditions and a held-out deterministic check | Production accuracy, customer performance or compliance |
| `workflow-benchmark-v1/` | Comparison of an always-proceed baseline with a deterministic risk-gated control policy on 100 synthetic cases | Model leaderboard quality, ROI or production impact |
| `workflow-opportunity-benchmark/` | A transparent framework for prioritizing 30 repeatable workflows before technology selection | Sales probability, ROI or automation success |
| `provenance-50-v1/` | Source/provenance structures and public-safe cases | Source truth outside the supplied test context |
| `human-approval/` | Approval-card, action-log and incident-tabletop structures | A claim that a real customer uses these exact artifacts |
| `measurement-v1/` | Event, form and AI-visibility measurement dictionaries | Real customer conversion or retention outcomes |
| `pilot-v1/` | Public-safe SOW, data appendix, handoff and report templates | A live customer contract or delivered customer result |
| `site-catalog-readiness-v1/` | Retrieval, red-team and deletion-test methodology | Universal site readiness or ranking guarantee |
| `structured-extraction-v1/` | Schema, test cases and example output for controlled extraction | Production accuracy outside the test cases |

## Evidence boundary

Unless explicitly supported by separate evidence, these artifacts do **not** claim:

- real customer results;
- production accuracy;
- ROI, savings or revenue lift;
- uptime or SLA performance;
- compliance or security certification;
- external expert review;
- partner or customer endorsement.

## Public website vs GitHub

The live Technical Evidence Index links only to artifacts that are intended to be reachable from the published site.

Some repository files — especially `README*.md` and executable `*.py` files — are intentionally GitHub-only and excluded from the GitHub Pages artifact. This keeps the public website clean while preserving reproducibility and technical inspection in the repository.

## Versioning

Package-level version and release files are used where the evidence set is frozen or materially reviewed. A packaging-only update must say so and must not be presented as a new benchmark result.

Public documentation change history:

**https://synapseautomate.github.io/degisiklikler.html**
