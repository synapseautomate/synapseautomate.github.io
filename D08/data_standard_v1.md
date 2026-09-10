# Shared Data Standard v1

Purpose: one common event/data vocabulary across intake, proof, funnel and delivery. No raw customer data is stored in public proof assets.

## Core entities
- `case_id`: unique workflow case identifier
- `source`: system/document/channel that supplied the fact
- `source_verified`: boolean verification state
- `business_id`: pseudonymous/internal business identifier when needed
- `product_or_service`: normalized product/service label
- `revenue_value`: numeric only when legitimately available; otherwise null
- `currency`: ISO currency code when relevant
- `consent_state`: unknown / not_required / granted / denied / expired
- `risk_level`: low / medium / high
- `human_owner_role`: accountable role, not personal name by default
- `expected_route`: auto / review / approval / block
- `actual_route`: measured route after execution
- `status`: current state-machine state
- `created_at`, `updated_at`: ISO-8601 timestamps

## Event names
- `view`
- `tool_start`
- `tool_complete`
- `form_start`
- `form_submit`
- `qualified_inbound`
- `analysis_requested`
- `analysis_paid`
- `pilot_proposed`
- `pilot_accepted`
- `case_received`
- `case_reviewed`
- `case_approved`
- `case_rejected`
- `case_blocked`
- `case_delivered`

## Provenance contract
Every decision-relevant field should carry or be traceable to:
- source type
- source identifier/location where permitted
- verification state
- last-known update time where relevant
- owner role

If a fact is missing or unverified, the normalized value is `unknown`; it is not inferred into a decisive field.

## Privacy / public-proof rule
Public datasets use synthetic records only. Real customer identifiers, secrets, payment details, health data, personal financial data, contract text or confidential attachments are excluded from public proof.

## Measurement rule
Unmeasured business metrics remain null/0 in scoreboards according to the reporting surface. No inferred revenue, ROI, conversion or accuracy value is written as measured fact.
