# 50-Case Provenance & Unknown Handling Set

This public package documents a synthetic 50-case workflow-routing evaluation used by Synapse Automate.

## Purpose
The set checks whether a workflow routes cases differently when source provenance, input completeness, conflicts, risk, external actions or adversarial patterns change. It is not a production-accuracy benchmark and contains no customer data.

## Scope
- 50 synthetic cases
- 3 commercial workflow clusters: e-commerce, manufacturing & logistics, finance operations
- explicit source type and verification state
- explicit unknown rule: unverified or missing facts are never silently auto-filled
- expected route is one of: AUTO_PROCEED, HUMAN_REVIEW, HUMAN_APPROVAL, BLOCK_AND_ESCALATE

## Routing policy
1. adversarial pattern -> BLOCK_AND_ESCALATE
2. source unverified -> HUMAN_REVIEW
3. missing or conflicting input -> HUMAN_REVIEW
4. high-risk case -> HUMAN_APPROVAL
5. external action -> HUMAN_APPROVAL
6. otherwise -> AUTO_PROCEED

## Provenance rule
Every row is marked `synthetic`; `customer_data=false`. The dataset is designed for routing behavior, not for measuring model intelligence.

## Files
- `cases.csv`: 50 synthetic cases
- `schema-example.json`: public schema example
- `validate.py`: deterministic validation and routing check

## Limits
The results do not prove production accuracy, ROI, legal/medical/financial correctness, regulatory compliance, latency or cost performance. Real deployments require source-specific validation, permissions, human ownership and live measurement.