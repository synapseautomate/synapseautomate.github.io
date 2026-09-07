# Synapse Automate - Day 5 Reliability Regression v1

**Run date:** 2026-09-07  
**Data:** 100 synthetic, non-sensitive cases  
**Purpose:** Turn the Day 5 reliability standard into a public, rerunnable proof artifact.

## What this proves

This suite checks whether a deterministic decision policy keeps four behaviors separate:

1. **AUTO_PROCEED** - verified source, sufficient input, low-risk/non-external work.
2. **HUMAN_REVIEW** - missing/unverified source, missing/conflicting input, or medium-risk recommendation support.
3. **HUMAN_APPROVAL** - high-risk cases or any external action.
4. **BLOCK_AND_ESCALATE** - adversarial attempts such as prompt injection, approval bypass, or source fabrication.

It does **not** prove production accuracy, regulatory compliance, business ROI, or domain advice quality.

## Public result

| Metric | Result |
|---|---:|
| Synthetic regression cases | 100 |
| Passed | 100 |
| Failed | 0 |
| Human-gated cases | 64 |
| Auto-proceed cases | 36 |
| Human review | 29 |
| Human approval | 20 |
| Block & escalate | 15 |
| Deliberate integrity mutations detected | 5 / 5 |

## Failure handling

The baseline run has 0 policy mismatches. To avoid a misleading "all green" proof, the package also includes `mutation_checks.csv`, which deliberately corrupts five expected outputs. `run_mutation_checks.py` must detect all five. Current result: **5/5 detected**.

If a future baseline case fails, the failure must remain visible in the public summary until the policy, test, or case is corrected and the change is documented.

## High-risk boundaries

- **Finance:** no autonomous financial advice or final money movement.
- **Health:** no medical advice, diagnosis, or treatment decision.
- **Legal:** no legal advice or final legal judgment.
- **External actions:** require human approval.
- **Unknown or conflicting source:** do not invent; stop and escalate.

## Re-run

```bash
python run_regression.py test_cases.csv
python run_mutation_checks.py mutation_checks.csv
```

Expected exit code for both commands: `0`.

## Files

- `test_cases.csv` - 100 synthetic cases and expected policy outcomes.
- `run_regression.py` - deterministic regression runner.
- `mutation_checks.csv` - five deliberately corrupted expectations.
- `run_mutation_checks.py` - verifies all deliberate corruptions are caught.
- `scoreboard.json` - machine-readable public summary.

## Commercial boundary

This proof is designed to answer a buyer question: **"How do you stop an automation from confidently doing the wrong thing?"**

The answer is not a promise of perfection. It is a testable control system: verified source, explicit failure modes, human gates, adversarial blocking, and a visible regression record.

For a real workflow, start with the free process map and then request the fixed-scope Process Analysis: **4,900 TL / $149 starting price**, subject to scope and payment/invoicing verification before purchase.

- Free process map: https://synapseautomate.github.io/araclar/surecini-20-dakikada-haritala.html
- Process Analysis: https://synapseautomate.github.io/surec-analizi.html
