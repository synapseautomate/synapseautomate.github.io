# Structured Extraction + Validator v1

Synthetic public proof for one principle: **missing evidence must remain missing**. A schema-shaped answer is not automatically trustworthy.

## What this package demonstrates
- explicit `unknowns` instead of fabricated completeness;
- provenance fields tied to a source reference;
- deterministic routing to human review/approval;
- safe local ingestion for PDF/XLSX/email/CSV/text, with JSON support in the parser contract;
- type, size, empty, duplicate and corruption checks;
- raw input is read-only; derived text/metadata is produced separately.

## Run
```bash
python validate.py
python test_ingest.py  # 5 normal + 5 broken inputs
```

## Limitations
All examples are synthetic. This is not a claim of production accuracy, compliance, legal/financial/medical correctness, or ROI. Consequential external actions are intentionally outside this proof and require human approval.
