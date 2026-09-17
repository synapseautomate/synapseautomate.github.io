# Reliable Workflow Architecture v0

## Goal
Turn an inbound business input into a structured, source-traceable draft without fabricating missing fields or executing a consequential external action.

## Flow
`input → parse → context → structured extraction → deterministic validate → draft → human approval → log`

| Component | Single responsibility | Failure output |
|---|---|---|
| Input gate | Type, size, duplicate, corruption checks | `REJECT_INPUT` |
| Parser | Produce derived text + metadata; never mutate raw | `PARSE_FAILED` |
| Context builder | Attach allowed reference context only | `CONTEXT_INCOMPLETE` |
| Structured extractor | Fill declared schema; unknown stays null | `EXTRACTION_UNCERTAIN` |
| Deterministic validator | Apply explicit rules independent of model prose | `VALIDATION_FAILED` |
| Draft builder | Create non-binding draft/recommendation | `DRAFT_BLOCKED` |
| Human gate | Approve/reject consequential action | `AWAITING_APPROVAL` |
| Audit log | Record source refs, version, route, reviewer | `LOG_FAILED` |

## Disabled by default
Email sending, refund/payment, final pricing, contract acceptance, diagnosis/treatment, deletion, publication, or any external write.

## Vendor boundary
Model/provider calls must sit behind an adapter. Schema, deterministic rules, audit format and tests remain provider-independent.

## Public proof
See `public-proof/structured-extraction-v1/` for a reproducible synthetic validator and fail-closed ingestion examples.
