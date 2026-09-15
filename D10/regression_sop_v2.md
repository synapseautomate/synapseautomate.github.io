# Regression & SOP v2

## 30-case regression
Run before a policy/model/workflow change is promoted. The regression uses 30 fixed synthetic cases from the public provenance set.

## Failing-test loop
1. Reproduce the failing case without changing the gold route.
2. Classify root cause: provenance, missing/conflict, risk/authority, adversarial, or implementation.
3. Make the smallest policy/validator fix.
4. Re-run all 30 cases, not only the failing one.
5. If a fix creates a new critical failure, revert and escalate to human design review.
6. Record the change in the regression log; no free-form retrospective replaces the test result.

## Most repeated manual step
Current synthetic routing set shows **human review of missing/unverified/conflicting inputs** as the largest gated class. Optimization target is faster evidence collection and clearer review context — not bypassing the human gate.
