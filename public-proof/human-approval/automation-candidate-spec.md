# Automation Candidate Spec

## Candidate
E-commerce order-exception triage before any refund/payment/external write.

## Input
Order metadata + approved policy/source references. No raw sensitive customer data is required for the synthetic example.

## Automated
1. Parse supported input.
2. Extract schema fields with provenance.
3. Run deterministic rules.
4. Route to AUTO_PROCEED, HUMAN_REVIEW, HUMAN_APPROVAL or STOP_ESCALATE.

## Never autonomous in v1
Refund approval, payment movement, binding price exception, destructive write, external customer promise.

## Success metric
Primary: total minutes to an **approved result**. Secondary: critical error count, reviewer correction count, handoff latency. Automation percentage is not the success metric.

## Stop conditions
Missing source, conflicting critical value, unsupported input, duplicate candidate, consequential action without an authorized approver.
