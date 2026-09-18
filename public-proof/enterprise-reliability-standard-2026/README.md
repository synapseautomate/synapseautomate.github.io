# Synapse Automate Enterprise AI Workflow Reliability Standard 2026

**Version:** 1.0 draft for public release  
**Date:** 2026-09-18  
**Publisher:** Synapse Automate  
**Scope:** enterprise AI-assisted workflows that read, extract, classify, recommend, prepare, or execute operational actions.

> This is a Synapse Automate operating standard. It is **not** an ISO/NIST certification, regulatory compliance statement, or guarantee of production accuracy or business outcome.

## Executive principle

A workflow is not reliable because its output looks complete. It is reliable when it can show **what it knows, what it does not know, where critical values came from, which rules were applied, who owns consequential authority, and when the system must stop.**

The standard therefore optimizes for **approved outcome quality**, not maximum automation percentage.

## The four decision states

| State | Trigger | System behavior | Human authority |
|---|---|---|---|
| `AUTO_PROCEED` | low-risk + source-backed + rules pass | continue only within pre-authorized boundary | monitoring, not routine approval |
| `HUMAN_REVIEW` | ambiguity / duplicate / non-consequential exception | hold and expose evidence + proposed correction | inspect, edit, route |
| `HUMAN_APPROVAL` | consequential action | prepare action; external write remains blocked | approve, edit, reject, delegate |
| `STOP_ESCALATE` | missing/conflicting critical evidence or no safe rule | stop progression and expose reason | designated owner resolves evidence/policy gap |

## Ten control domains

### R1 - Source integrity and provenance

**Requirement:** Every critical field must be traceable to an approved source or explicitly marked unknown.

**Minimum evidence:** source identifier, retrieval/observation time where applicable, source status, and field-level provenance for consequential inputs.

**Fail condition:** a critical field is presented as factual without source evidence.

### R2 - Unknown preservation

**Requirement:** Missing evidence must remain missing. The system must not convert absence into a plausible value.

**Minimum evidence:** explicit `unknown`, `missing`, or equivalent state that survives downstream parsing and UI display.

**Fail condition:** unsupported value silently substitutes for missing evidence.

### R3 - Structured output and parse gate

**Requirement:** Machine-consumed model output must pass a declared schema before downstream use.

**Minimum evidence:** schema, parser, failure output, bounded retry policy.

**Fail condition:** invalid output proceeds downstream; retry is unbounded.

### R4 - Deterministic validation

**Requirement:** Rules that can be expressed deterministically must not be delegated to probabilistic model judgment.

**Minimum evidence:** positive + negative tests for critical rule families; examples include quantity, currency, duplicate, mandatory-field and date/term constraints.

**Fail condition:** a rule violation can pass because the model “believes” it is acceptable.

### R5 - Decision authority and human gate

**Requirement:** Consequential actions require explicit authority boundaries.

**Minimum evidence:** owner/approver role, decision state, approve/edit/reject/escalate actions, and external-write control.

**Fail condition:** payment, pricing exception, external message, deletion, publication, legal/medical/financial determination, or other defined consequential action executes without the required gate.

### R6 - Least agency and tool boundary

**Requirement:** AI components receive only the tools, permissions and actions required for the workflow step.

**Minimum evidence:** allow-list of tools/actions, read/write distinction, blocked operations, and owner of permission changes.

**Fail condition:** unnecessary write/delete/broad external capability is available to the AI system.

### R7 - Observability and decision log

**Requirement:** A consequential decision must be reconstructable after the fact.

**Minimum evidence:** source, extracted value, rule result, state, proposed action, human action, timestamp, and final disposition.

**Fail condition:** the team cannot explain why the workflow advanced or stopped.

### R8 - Regression and adversarial testing

**Requirement:** policy changes must be tested against normal, malformed and adversarial cases.

**Minimum evidence:** versioned test set, expected outcomes, visible failures, and mutation/adversarial checks.

**Fail condition:** behavior changes without a rerunnable test record.

### R9 - Incident stop and recovery

**Requirement:** the workflow must define when to stop, who owns the incident, and what evidence is required to resume.

**Minimum evidence:** incident trigger, containment action, escalation owner, recovery criteria, and post-incident test update.

**Fail condition:** the system continues after a known critical evidence or policy failure.

### R10 - Business outcome measurement

**Requirement:** workflow success is measured at the approved result, not at model output or automation rate.

**Primary metrics:**

- Time to Approved Result (TAR)
- Critical Error Rate (CER)
- Evidence Coverage
- Rework Rate
- Escalation Resolution Time
- Cost per Approved Result

**Fail condition:** the only success metric is number/percentage of tasks automated.

## Evidence ladder

| Level | Meaning | Acceptable public claim |
|---|---|---|
| E0 | concept only | no result claim |
| E1 | synthetic demonstration | “synthetic example/demo” |
| E2 | reproducible public test | “re-runnable public test” |
| E3 | controlled pilot | result with scope, period, sample and limitations |
| E4 | production customer result with permission | case result with methodology and permission |

A higher-looking result must never be implied from a lower evidence level.

## Current public proof baseline

The following are synthetic/reproducible controls, **not production accuracy claims**:

- deterministic decision cases: **10/10 PASS**
- critical deterministic rule families: **5/5** with positive + negative coverage
- structured extraction cases: **10/10 PASS**
- ingestion tests: **10/10 PASS** (5 normal + 5 broken)
- provenance cases: **50/50 PASS**
- reliability regression: **100/100 PASS**
- deliberate integrity mutations detected: **5/5**

## Pilot minimum

A Synapse reliability pilot is not a broad transformation program. It begins with:

- one workflow
- one named workflow owner
- one baseline outcome
- one source boundary
- five or fewer critical deterministic rule families where possible
- explicit decision states
- one human authority boundary
- one primary approved-result metric
- a stop/fail rule agreed before implementation

Expansion happens only after the workflow passes both the reliability gate and the business gate.

## Domain boundaries

This standard does not authorize autonomous domain judgment. In finance, health, legal or other high-consequence contexts, the AI workflow may support extraction, classification, anomaly flagging, evidence organization and decision preparation, but final regulated/professional judgment remains with the appropriate authorized human unless a separately validated and legally permitted control model applies.

## External reference alignment

The standard is informed by public risk/governance references, including:

- **NIST AI RMF 1.0** and the **Generative AI Profile (NIST AI 600-1)** - voluntary risk-management guidance, including trustworthiness and provenance considerations.
- **ISO/IEC 42001:2023** - AI management-system requirements and continuous improvement concepts.
- **OWASP Top 10 for LLM/GenAI Applications** - security risks including improper output handling and excessive agency.

These references are alignment inputs only. Synapse does not claim ISO certification, NIST approval, or OWASP endorsement.

## Release rule

A workflow may be called **Synapse Reliability Standard - PASS** only when:

1. all applicable R1-R10 controls have evidence,
2. no critical fail condition is open,
3. human authority and stop conditions are visible,
4. regression tests pass for the release version,
5. limitations are documented,
6. the approved-result business metric is measurable.

Anything less remains **DRAFT**, **DEMO**, or **PILOT - NOT YET PASS**.
