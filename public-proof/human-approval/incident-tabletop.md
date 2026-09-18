# Incident Tabletop - Human Approval

**Scenario (synthetic):** a workflow proposes a refund while a required delivery confirmation is missing.

1. **Detect:** deterministic validator emits `STOP_ESCALATE` for missing critical evidence.
2. **Contain:** external write remains disabled; no payment/refund action is executed.
3. **Explain:** approval card shows source, missing field, proposed action and authority owner.
4. **Human decision:** reviewer may edit, reject or escalate; approval requires source completion.
5. **Log:** state transition, reviewer role, source IDs and reason are logged.
6. **Recover:** after evidence is corrected, validation is rerun; no silent retry on content ambiguity.
7. **Learn:** add a regression case if the failure mode was not already represented.

**Success criterion:** zero consequential external action before authorized approval; critical evidence gap remains visible.
