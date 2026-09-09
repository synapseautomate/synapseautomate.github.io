# LinkedIn Company Page - 5 public comments

Rules: post manually as Synapse Automate Company Page. No links, no pitch, no CTA, no DMs.

## 1. Milan Chheda - static benchmark vs production evaluation

Target: https://www.linkedin.com/posts/milanchheda_benchmarks-show-what-should-work-production-activity-7485532831830700032-HXWn

Comment:

A useful distinction is to separate capability evidence from workflow evidence. A model can look strong on a clean benchmark while the actual system still fails on source retrieval, tool choice, approval boundaries or exception handling. Task-specific regression plus production traces makes the trade-off much easier to see than a single model score.

## 2. Borja Marín Rosas - accuracy is not enough

Target: https://www.linkedin.com/posts/borja-marin-rosas_accuracy-is-not-enough-measuring-ai-in-production-activity-7495375550363099136-74JL

Comment:

Error severity is the metric that changes the conversation. A workflow with a high average accuracy can still be unacceptable if the remaining errors cluster in irreversible or high-impact cases. Segmenting errors by consequence, detectability and required human action makes the operational scorecard much more useful.

## 3. Zelin Wan - long-horizon API agent reliability

Target: https://www.linkedin.com/posts/zelinwan_zelin-wan-phd-measuring-api-agent-reliability-activity-7493942971911032832-PbNU

Comment:

The long-chain result is a strong reminder that task success compounds across transitions. One practical design response is to verify state at consequential boundaries rather than only score the final answer: source state, tool result, permission, then human approval before irreversible actions. A correct final sentence cannot repair a wrong state change earlier in the chain.

## 4. Ishika Gupta - evaluate the system, not only the model

Target: https://www.linkedin.com/posts/ishika-gupta-0514241a9_a-production-grade-ai-system-is-not-an-llm-activity-7498458517574410240-pKEE

Comment:

This is why a workflow eval should be able to fail even when the final prose looks good. Wrong source, wrong tool, unauthorized action or a skipped human gate are system failures regardless of answer quality. Making those failure classes explicit also gives each one a clear owner and remediation path.

## 5. Hari R - evaluation engineering

Target: https://www.linkedin.com/posts/hari-r-865934231_aiengineering-aievals-aiagents-activity-7498349103823769600-H9yD

Comment:

The offline / trace / online split is especially useful when paired with stop conditions. Offline tests catch known regressions, traces explain why the workflow failed, and online monitoring shows whether the input distribution changed. The missing piece in many systems is a defined point where uncertainty stops automation and hands control back to a person.
