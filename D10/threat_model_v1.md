# Threat Model v1 — Human-Controlled AI Workflows

This operating model uses the NIST AI RMF functions **Govern, Map, Measure, Manage** as organizing headings and focuses on the agentic risks required by the Day 10 plan. It is not a certification or legal-compliance claim.

## GOVERN
- **Purpose owner:** process owner names what the system may and may not do.
- **Data owner:** approves sources, retention and access.
- **Control owner:** approves authority boundaries and rollback.
- **Release owner:** accepts test evidence before production.

## MAP
Primary risk scenarios:
1. **Prompt / instruction injection** — untrusted input attempts to override workflow rules.
2. **Tool misuse** — a model invokes a tool outside the intended business purpose.
3. **Privilege expansion** — an agent gains broader read/write authority than required.
4. **Memory / context poisoning** — persistent context carries attacker-controlled or stale information forward.
5. **Cascading failure** — one bad state propagates across downstream tools or agents.

## MEASURE
For each critical workflow track: blocked injection tests, unauthorized-action attempts, source/provenance failures, human-approval bypass attempts, rollback success, duplicate/late-change handling, and critical incident count.

## MANAGE
- High-impact external writes default to **human approval**.
- Unverified source, missing input or conflict defaults to **human review**.
- Adversarial / privilege violation defaults to **block and escalate**.
- Every external write has an accountable owner and rollback path before production.

## Production red lines
- No autonomous payment, contract acceptance, final price publication or binding customer promise in the first release.
- No secret/raw customer dataset in public proof.
- No automatic expansion of permissions based on model request.
- No persistent memory from untrusted input without validation and scope controls.

## Reference anchors
- NIST AI RMF / Playbook: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
- NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- OWASP GenAI / Agentic Applications incident alignment: https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/
- OWASP memory/context poisoning discussion: https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface/
