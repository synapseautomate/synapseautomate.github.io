# Workflow Decision Benchmark v1

Version: **1.1.0**  
Benchmark dataset/result date: **2026-09-09**  
Packaging/review update: **2026-10-08**  
Status: **public, synthetic, non-sensitive**

## Release boundary

Version 1.1.0 does **not** change the dataset, decision rules or pinned summary values from the 1.0.0 benchmark. This packaging update adds explicit version metadata, a machine-readable manifest, a release note and clearer discovery paths.

- Live technical evidence index: https://synapseautomate.github.io/kanit/teknik-kanit-indeksi.html
- Public proof repository index: ../README.md
- Release note: release_note.md
- Manifest: manifest.json

No new model evaluation, customer result, production accuracy, ROI or compliance claim is introduced by this packaging update.

## What this benchmark is

This benchmark compares two **decision strategies** on the same pinned 100-case synthetic test set. It is not an LLM model-quality leaderboard.

The question is practical: when a workflow contains missing sources, conflicting inputs, external actions, high-impact decisions or adversarial attempts, should the system continue automatically or route the case to a safer control path?

### Blind labels

- **Approach A - A_ALWAYS_PROCEED:** a deliberately naive baseline that returns `AUTO_PROCEED` for every case.
- **Approach B - B_RISK_GATED:** a deterministic policy using source verification, input quality, risk, human approval and adversarial blocking.

The public page can present these as **Approach A** and **Approach B** before revealing the implementation details.

## Dataset

Source: `../reliability-regression-v1/test_cases.csv`

- 100 synthetic cases
- no real customer data
- 9 sectors
- expected outcomes: 36 automatic, 29 human review, 20 human approval, 15 block/escalate
- 64 cases require a human or safety gate
- 15 adversarial cases

## Pinned v1 results

| Metric | Approach A | Approach B |
| --- | ---: | ---: |
| Policy match | 36/100 | 100/100 |
| Policy mismatch | 64 | 0 |
| Human/safety gates captured | 0/64 | 64/64 |
| Adversarial cases blocked | 0/15 | 15/15 |
| Automatic continuation | 100 | 36 |
| Human review | 0 | 29 |
| Human approval | 0 | 20 |
| Block/escalate | 0 | 15 |

The result means only that Approach B matches the **predefined policy labels in this synthetic deterministic test set**. It does not establish production accuracy or business impact.

## Reproduce

From this directory:

```bash
python run_benchmark.py
```

The script reads the pinned v1 dataset, evaluates both strategies, checks the expected v1 gates and writes generated CSV/JSON summaries.

## Decision rule for Approach B

1. Adversarial attempt -> `BLOCK_AND_ESCALATE`
2. Missing or unverified source -> `HUMAN_REVIEW`
3. Missing or conflicting input -> `HUMAN_REVIEW`
4. High-risk decision -> `HUMAN_APPROVAL`
5. External action -> `HUMAN_APPROVAL`
6. Medium-risk recommendation support -> `HUMAN_REVIEW`
7. Otherwise -> `AUTO_PROCEED`

## What was not measured

- model latency
- inference cost
- human edit time
- real-world task accuracy
- customer ROI
- legal, medical, financial or regulatory compliance

Those fields must remain **unmeasured**, not estimated, until real instrumentation exists.

## Limits

This is a public proof of a **control policy and test discipline**, not a claim that Synapse Automate, an AI model or a customer workflow is 100% accurate in production. The test set is synthetic and the expected outcomes were defined before evaluation. High-impact decisions remain human-controlled.

## Related proof

- `../reliability-regression-v1/` - 100-case reliability regression and mutation checks
- `failure_taxonomy_v1.csv` - error categories, severity and owners
- `before_after_examples.md` - three synthetic before/after cases
- `CHANGELOG.md` - version history
- `VERSION` - current public package version
- `release_note.md` - scope and claim boundary for the current package
- `manifest.json` - machine-readable package inventory with Git blob identifiers
