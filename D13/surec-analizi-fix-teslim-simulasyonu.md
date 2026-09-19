# Synthetic Process Analysis + Fix Delivery Simulation

## Workflow
E-commerce supplier catalog → extraction → price/stock decision support → proposed catalog write.

## Observed candidate failures
1. Embedded content instruction could reach the action planner.
2. Stale commerce state could still reach approval.
3. Proposed write could exist without an explicit capability grant.

## Fix delivery
- Treat retrieved content as data; instruction flag forces STOP_ESCALATE.
- Freshness gate before price/stock write.
- Explicit write/destination scope outside model output.

## Acceptance
- Frozen suite: 100/100 expected states.
- Critical mismatch: 0.
- Held-out: 20/20.
- Production guarantee: none; live permissions and integrations require pilot validation.

## Customer-facing handoff
Deliver source map, policy states, regression artifact, failure Pareto, owner/escalation map and pilot acceptance criteria.
