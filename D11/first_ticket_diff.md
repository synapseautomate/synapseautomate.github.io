# First AI ticket — diff explanation

## Ticket
Publish a provider-independent structured-extraction proof that treats missing evidence as `unknown`, validates high-impact routes deterministically, and fails closed on malformed local input.

## Files added
- `public-proof/structured-extraction-v1/schema.json` — fixed public output contract.
- `validate.py` + `test_cases.json` — 10 synthetic extraction/routing tests.
- `ingest.py` + `test_ingest.py` — PDF/XLSX/EML/CSV/TXT ingestion, size/type/duplicate/corruption checks, 5 normal + 5 broken tests.
- `README.md` — limitations and reproducible commands.

## Customer/public effect
No customer data is required. The proof shows how a workflow can expose missing sources and human approval instead of fabricating completeness.

## Risk
Public readers could mistake synthetic tests for production accuracy. Mitigation: README and canonical guide explicitly state synthetic scope and no production/ROI/compliance claim.

## Rollback
Delete the public-proof directory and the canonical guide/internal links. No runtime integration depends on it.
