# Sanitized Workflow Decision Summary

Current working default: RFQ intake -> quote/checklist draft -> human approval.

Why this shape is testable:
- the input can be represented with synthetic/redacted request data;
- missing attachment, ambiguous quantity, currency conflict, duplicate request and late change can be evaluated as explicit exceptions;
- the first version does not need autonomous external action;
- human approval can remain the final gate before any binding output;
- delivery quality can be measured with source completeness, correction time, exception rate and human edits.

What this summary does **not** claim:
- validated customer demand;
- a proven revenue lift or ROI;
- production accuracy;
- autonomous authority to quote, contract or commit funds.

The decision changes only when measurable real-world evidence contradicts it. Praise or general interest is not treated as demand.