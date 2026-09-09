# Three synthetic before/after examples

These are **synthetic control examples**, not customer case studies.

## 1. Missing source

**Before / naive behavior**  
The workflow receives a request with no verifiable source and still continues to an answer or action.

**After / risk-gated behavior**  
The workflow stops automatic continuation, labels the source as missing and routes the case to `HUMAN_REVIEW` or requests the missing source.

**Why it matters**  
The improvement is not a prettier answer. It is the prevention of unsupported certainty.

## 2. Conflicting input

**Before / naive behavior**  
A form says 40 weekly transactions while an attached document says 120. The workflow silently picks one number and continues.

**After / risk-gated behavior**  
The conflict is surfaced and the case moves to `HUMAN_REVIEW`. No binding action is taken until the discrepancy is resolved.

**Why it matters**  
Conflicting inputs are a process problem, not a prompt-writing problem.

## 3. External action

**Before / naive behavior**  
A draft output is automatically sent, posted, priced or committed because the model produced a plausible result.

**After / risk-gated behavior**  
The draft is prepared, but the external action is held behind `HUMAN_APPROVAL` with source, uncertainty and reject/escalate options visible.

**Why it matters**  
Automation can prepare high-value work without silently inheriting human authority.
