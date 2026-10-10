# Day 28 — Unit economics stress test (INTERNAL ONLY)

**Status: illustrative planning inputs, NOT observed customer cost or profit.** No customer payments have been verified. Adjust assumptions from signed vendor invoices and actual timesheets; do not use these as public success claims.

## Independent price lists

- Process Analysis: TRY 4,900 / separate USD $149
- Controlled Pilot: TRY 24,900 / separate USD $750
- Monthly Management: TRY 14,900 / separate USD $449

No FX mapping between the lists.

## Monthly Management sensitivity (TRY 14,900 starting price)

Assume an **illustrative** internal fully loaded labor cost of TRY 850/hour and an illustrative monthly direct software cost of TRY 1,800. Exclude taxes, account acquisition, overhead, incident escalation, and unpriced hosting/connector bills; therefore the true margin may be lower.

| Monthly delivery + revision effort | Illustrative cost | Illustrative contribution | Contribution margin |
| --- | ---: | ---: | ---: |
| 8 hours | TRY 8,600 | TRY 6,300 | 42.3% |
| 12 hours | TRY 12,000 | TRY 2,900 | 19.5% |
| 16 hours | TRY 15,400 | **TRY -500** | **-3.4%** |
| 20 hours | TRY 18,800 | **TRY -3,900** | **-26.2%** |

Formula: contribution = monthly fee - (total support hours × 850 + direct software cost). Break-even before overhead: (14,900 - 1,800) / 850 ≈ 15.4 hours/month.

**Stop-loss:** A contract estimated above the break-even hours is not sold at the starting price with unlimited work. Reduce scope and explicit support hours, obtain buyer consent to a separately priced tier, or decline. Do not claim real margins from assumed costs.

## Required observed-data fields

For each genuine signed order, privately track invoiced fee, vendor cost, labor time, human review, revisions, incidents, refunds, taxes excluded/included, retention, and delivery dates. Until data exists, mark outcomes UNMEASURED, not 0% ROI or success.

## Scenario source reconciliation

The old `public-proof/pilot-v1/monthly_service_economics.csv` contains scenario revenue TRY 24,900 and should NOT be used as a claim about the current TRY 14,900 Monthly Management offer. It is a synthetic sensitivity artifact under a different fee assumption.
