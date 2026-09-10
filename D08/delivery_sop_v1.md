# Delivery SOP v1 - Five Productized Steps

These SOPs describe the working delivery standard. Durations are operational targets, not guarantees; live customer scope can change them.

## SOP 1 - Intake & Scope
Input: redacted workflow description, source systems, volume, current pain, accountable owner.
Steps: confirm scope -> identify missing facts -> mark unknowns -> define one workflow boundary.
QA: no hidden assumptions; no sensitive data unless necessary and authorized.
Output: scoped workflow brief + missing-information list.

## SOP 2 - Baseline & Measurement
Input: scoped workflow.
Steps: choose 1-3 measurable baseline metrics -> define critical error -> define stop condition -> record measurement method.
QA: metric must be observable and attributable; no fabricated baseline.
Output: baseline/evidence plan.

## SOP 3 - Workflow Build / Configuration
Input: approved brief + verified sources.
Steps: map states -> implement deterministic gates -> add source/unknown handling -> add human handoff -> create logs.
QA: missing/conflicting source does not silently pass; external high-impact action requires explicit permission.
Output: controlled workflow candidate.

## SOP 4 - Eval & Human Review
Input: candidate workflow + synthetic/redacted cases.
Steps: run normal + exception cases -> classify failures -> run mutation/adversarial checks where relevant -> review human approval surface.
QA: critical transitions have deterministic or human control; failed examples are not hidden.
Output: eval report + known limits + fix list.

## SOP 5 - Delivery & Handoff
Input: approved workflow/eval.
Steps: document owner/permissions -> define rollback -> verify measurement events -> confirm support boundary -> deliver evidence pack.
QA: no autonomous action beyond approved scope; all customer-facing claims supported by measurement or explicitly labeled assumption.
Output: release package + owner map + measurement/incident instructions.
