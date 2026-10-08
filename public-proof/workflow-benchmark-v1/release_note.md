# Release note — Workflow Decision Benchmark 1.1.0

Date: **2026-10-08**  
Evidence status: **synthetic, deterministic control-policy benchmark**  
Change type: **packaging and discoverability only**

## What changed

This release adds version metadata, a machine-readable artifact manifest and clearer discovery paths for the existing Workflow Decision Benchmark.

The benchmark dataset, decision rules and pinned summary values are unchanged from the 1.0.0 benchmark published on 2026-09-09. No new evaluation run is presented as part of this packaging update.

## What the benchmark shows

On the pinned 100-case synthetic test set:

- the always-proceed baseline matches 36/100 predefined policy labels;
- the risk-gated deterministic policy matches 100/100 predefined policy labels;
- 64/64 expected human/safety gates are captured by the risk-gated policy;
- 15/15 adversarial synthetic cases are routed to block/escalate by that policy.

These values describe agreement with predefined synthetic policy labels. They do not establish production accuracy or business impact.

## What it does not show

This release does not claim:

- customer outcomes;
- production accuracy;
- latency or inference cost;
- ROI or savings;
- uptime or SLA performance;
- legal, medical, financial or regulatory compliance;
- external expert review.

## Start here

- Live technical evidence index: https://synapseautomate.github.io/kanit/teknik-kanit-indeksi.html
- Benchmark summary: benchmark_summary.csv
- Failure taxonomy: failure_taxonomy_v1.csv
- Synthetic before/after examples: before_after_examples.md
- Machine-readable manifest: manifest.json
