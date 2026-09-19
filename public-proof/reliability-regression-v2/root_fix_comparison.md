# Root-fix comparison

| Root cause | Prompt-only | More context | Deterministic rule | Human gate | Selected control |
|---|---|---|---|---|---|
| Untrusted instruction inside document | Weak: same model can still be manipulated | Helps but does not establish authority | Strong: treat retrieved content as data; embedded instructions cannot grant authority | Escalate when suspicious content intersects an action | Deterministic instruction/data boundary + STOP_ESCALATE |
| Stale price/stock source | Weak: prompt can ask for freshness but cannot prove it | Useful if timestamp exists | Strong: freshness threshold must pass before consequential write | Human handles stale/ambiguous exceptions | Deterministic freshness gate + escalation |
| Unauthorized write / data egress | Weak: policy in prose can be bypassed | More context does not create permission | Strong: capability allowlist and destination/write scope | Human grants/denies consequential authority | Deterministic authority gate + human approval/escalation |

The selected controls minimize complexity while placing enforcement outside free-form model output. Prompt wording remains supportive, not authoritative.
