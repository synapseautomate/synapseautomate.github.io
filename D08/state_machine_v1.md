# RFQ State Machine v1

Working default: TradeOps RFQ intake -> quote/checklist draft -> human approval. This is a design default, not customer-validated demand.

## States
1. `RECEIVED` - trigger: inbound RFQ/form/document
2. `SOURCE_CHECK` - verify sender/source and attachment presence
3. `NORMALIZE` - parse customer, item, quantity, currency, delivery and terms fields
4. `EXCEPTION_REVIEW` - route missing/ambiguous/conflicting/duplicate/late-change cases
5. `DRAFT_READY` - quote/checklist draft assembled from verified fields
6. `HUMAN_APPROVAL` - authorized person reviews source, assumptions, warnings and draft
7. `APPROVED_FOR_ACTION` - deterministic permission gate passed
8. `DELIVERED` - approved output sent/exported by permitted action
9. `CLOSED` - outcome, time, edits and reason recorded
10. `BLOCKED` - unsafe/unresolved case stopped and escalated

## Required exception paths
- missing attachment -> `EXCEPTION_REVIEW`
- ambiguous quantity -> `EXCEPTION_REVIEW`
- currency conflict -> `EXCEPTION_REVIEW`
- duplicate RFQ -> `EXCEPTION_REVIEW`
- late change after draft -> return to `SOURCE_CHECK` / `NORMALIZE`
- unverified source -> `EXCEPTION_REVIEW`
- adversarial or unauthorized instruction -> `BLOCKED`

## State contract
| State | Input | Owner | Tool | Output | Timeout | Escalation |
|---|---|---|---|---|---|---|
| RECEIVED | inbound request | ops | intake | raw case | configurable | ops owner |
| SOURCE_CHECK | raw case | ops/system | validator | verified/unverified source | configurable | human review |
| NORMALIZE | verified case | system | parser/rules | structured fields + unknowns | configurable | human review |
| EXCEPTION_REVIEW | exception | human | review surface | corrected/blocked case | configurable | process owner |
| DRAFT_READY | structured case | system | template | quote/checklist draft | configurable | human approval |
| HUMAN_APPROVAL | draft + source + warnings | authorized human | approval UI | approve/edit/reject | configurable | senior owner |
| APPROVED_FOR_ACTION | approved draft | system | deterministic gate | permitted action | immediate | block if permission missing |
| DELIVERED | permitted output | ops/system | delivery adapter | delivery record | configurable | ops owner |
| CLOSED | delivery + outcome | ops | event log | measured case | n/a | n/a |
| BLOCKED | unsafe/unresolved | human | incident/escalation | block record | immediate | designated owner |

## v1 autonomy boundary
No autonomous external action before `HUMAN_APPROVAL` and `APPROVED_FOR_ACTION`. Missing, conflicting or unverified information is never silently auto-filled.
