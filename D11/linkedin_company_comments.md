# 5 Company Page comment drafts

1. Reliability improves when “unknown” is treated as a legitimate output. If a required field has no source, filling the schema is less important than preserving the evidence gap and routing the decision correctly.

2. Structured output is useful for consistency, but it is not the same as truth. A production workflow still needs provenance, deterministic validation and an explicit owner for exceptions.

3. Human-in-the-loop works best as a workflow state rather than a disclaimer. The reviewer should see the source, proposed action, expected effect and rollback path before approving a consequential step.

4. A practical safeguard is to separate classification from authorization. The system may classify a refund request or flag a pricing exception without owning the final monetary decision.

5. Fail-closed behavior is underrated in document automation. A corrupt, duplicate or unsupported input should be visible as an operational state instead of being silently transformed into a plausible-looking answer.
