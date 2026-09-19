# MVP v0 Release Note — Day 13

The working v0 is the deterministic reliability policy runner exposed in `public-proof/reliability-regression-v2/run_regression.py`. It accepts the frozen case schema and returns one of four control states. No model feature is introduced. The value is repeatable control behavior, failure visibility and explicit stop boundaries.

E2E evidence: `heldout_20_results.json` records 20/20 traceable executions.
