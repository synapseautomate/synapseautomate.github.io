# Synapse Automate — Repository Rules

These rules protect a revenue-focused, public-facing static site.

## Required before commit
- UTF-8 only; Turkish characters must render correctly.
- No secrets, API keys, passwords, raw customer data, health data, or customer-identifying examples.
- No fabricated customers, testimonials, production accuracy, ROI, compliance, legal, medical, or revenue claims.
- Public examples must be synthetic or explicitly redacted.
- Critical monetary, legal, health, publishing, deletion, and external-write actions require an explicit human approval boundary.
- Keep the primary funnel measurable: impression → click → form → qualified inbound → payment.
- Do not add a new feature when the active problem is messaging, trust, offer, attribution, or distribution.
- Schema/FAQ markup must match visible customer-facing content.
- Mobile overflow, broken links, template residue, and source/provenance errors are release blockers.

## Coding contract
- One responsibility per module; fail closed on malformed input.
- Preserve raw input. Produce derived text/metadata separately.
- Vendor-specific behavior stays behind adapters.
- External send/write, pricing decisions, refunds, payments, diagnosis/treatment, and legal acceptance are disabled by default.
- Tests must pass before commit.
- Scope creep requires a separate task and a clear revenue/proof reason.

## Public proof contract
A public proof must state what was tested, the synthetic/redacted nature of examples, limitations, failure modes, human handoff, and a reproducible validation path.
