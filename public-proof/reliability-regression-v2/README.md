# Synapse Automate — Reliability Regression v2

**Version:** 2.0.0  
**Frozen:** 2026-09-19  
**Data:** 100 synthetic, non-sensitive e-commerce workflow cases.

This public artifact tests whether a deterministic workflow policy routes a case to the expected control state: `AUTO_PROCEED`, `HUMAN_REVIEW`, `HUMAN_APPROVAL`, or `STOP_ESCALATE`.

## What changed in v2
A deliberately incomplete candidate baseline was tested against the frozen set. It passed **60/100** and produced **40 critical control mismatches**. Failure Pareto isolated three roots: authority/egress boundary, untrusted instructions embedded in content, and stale price/stock sources. The lowest-complexity reliable controls were added as deterministic gates with escalation. The same frozen suite then passed **100/100 with 0 critical mismatches**.

## Reproduce
```bash
python3 run_regression.py cases.csv
```
Expected: 100 passed, 0 failed.

## Held-out run
`heldout_20.csv` is separated from the 100-case tuning set and executed after the three controls are fixed. `heldout_20_results.json` records pass/fail, correction, error, log integrity, and local policy execution time for each case.

## Claim boundary
**100/100 is not “100% safe” or “100% accurate.”** It means the deterministic control layer conforms to the expected states in this frozen synthetic suite. Production integrations, permissions, model behavior, vendor changes, data drift, and organization-specific risk require separate validation.

## Public files
- `cases.csv` — frozen 100-case suite
- `rubric.json` — severity and pass criteria
- `scoreboard.json` — pre/post control result
- `failure_pareto_v1.csv` — failure concentration
- `root_fix_comparison.md` — prompt/context/rule/human-gate comparison
- `heldout_20.csv` + results — 20-case end-to-end run
- `knowledge_base_template.md` — source/owner/version pattern
- `CHANGELOG.md` — version history
