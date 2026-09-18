# Human Approval + Deterministic Rules

Synthetic proof of four explicit workflow states:

- `AUTO_PROCEED`: low-risk, source-backed, deterministic checks pass.
- `HUMAN_REVIEW`: ambiguity or non-consequential exception needs review.
- `HUMAN_APPROVAL`: a consequential action is prepared but cannot execute without an authorized human.
- `STOP_ESCALATE`: missing/conflicting critical evidence or unsupported condition blocks progression.

The commercial success metric is **time to approved result + critical-error rate**, not automation percentage.

All examples are synthetic. No production accuracy, compliance, investment, legal, medical or financial advice is claimed.

Run: `python validate_rules.py`
