# Baseline Report v1

Same 50 synthetic cases, same expected-route rubric. Prediction functions never read `expected_route`; evaluation compares only after prediction.

| Config | Exact | Corrections | Complexity |
|---|---:|---:|---:|
| A_single_step | 22/50 (44.0%) | 28 | 1 |
| B_structured_context | 47/50 (94.0%) | 3 | 2 |
| C_segmented_validator | 50/50 (100.0%) | 0 | 3 |

**Selected:** `C_segmented_validator`. Selection rule: prefer the simplest configuration that reaches at least 98% exact-route agreement; otherwise choose best accuracy, then lowest complexity.

**Cost caveat:** this is a deterministic local routing harness. External model/API cost was not measured, so no LLM cost claim is made.
