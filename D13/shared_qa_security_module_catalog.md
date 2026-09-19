# Shared QA / Security Module Catalog — v1

Single source of truth for Synapse and Kinetra Studios prototypes.

| Module | Control | Evidence | Stop condition |
|---|---|---|---|
| SOURCE_PROVENANCE | Critical values carry source/version | source_id + canonical source | missing/conflicting source |
| CONTEXT_FRESHNESS | Price/stock context has freshness policy | last_verified_at | threshold failed |
| UNTRUSTED_CONTENT | Retrieved content cannot grant authority | content_instruction flag | instruction intersects action/tool |
| AUTHORITY_SCOPE | Read/propose/write separated | capability scope | write not granted |
| EGRESS_SCOPE | External destinations allowlisted | destination policy | unapproved target |
| HUMAN_GATE | Consequential action has owner | approve/edit/reject/escalate | owner/approval absent |
| REGRESSION | Frozen cases survive change | suite/version/manifest | critical mismatch > 0 |
| CLAIM_BOUNDARY | Public claim matches evidence | limitation statement | “100% safe/accurate” language |

Studios prototypes use the same four states: AUTO_PROCEED / HUMAN_REVIEW / HUMAN_APPROVAL / STOP_ESCALATE.
