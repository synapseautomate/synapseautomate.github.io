# Kinetra Studios Opportunity Scorecard

This scorecard is an evidence-gated portfolio screen. A concept is not accepted because it sounds useful; it must have representative pain evidence, revenue proximity, a realistic distribution path, a safe human-approval boundary, and a 30-case bakeoff before build.

## Decision rules

- `BAKEOFF`: enough external evidence to justify a 3-prompt x 10-case synthetic test. Not a build approval.
- `SANDBOX`: useful signal exists, but regulatory or decision-risk boundaries require a narrower prototype.
- `HOLD`: evidence or operating boundary is too weak for a build decision.
- No unsupported user-count, GMV, competitor-revenue, ROI or market-size number is treated as fact.

## Portfolio scorecard

| Rank | Concept | Category | Representative evidence | Revenue proximity | Distribution hypothesis | Risk | Decision |
|---|---|---|---|---|---|---|---|
| 1 | ReturnOps Exception Copilot | E-commerce & Retail | NRF projects $849.9B in US retail returns for 2025; 19.3% of online sales returned; 64% of merchants say updating returns is a near-term priority. | High: return handling cost, retention and fraud are directly operational. | Shopify/marketplace operators, agencies, 3PL/returns partners. | Medium: fraud signals and refund exceptions need human gates. | BAKEOFF |
| 2 | Maintenance Intake Triage | B2B SaaS & Services / Property Ops | Buildium reports maintenance remained rental owners' top pain point; 38% selected it among top pain points and more than half hired a property manager for maintenance help. | High: maintenance coordination is recurring paid operational work. | Property managers, maintenance coordinators, owner communities. | Medium: emergencies and vendor spend require human escalation. | BAKEOFF |
| 3 | Accounts Receivable Follow-up Coordinator | Finance & Fintech / SMB Ops | QuickBooks reports 56% of surveyed US small businesses were owed money from unpaid invoices, averaging $17.5K; 47% reported invoices overdue 30+ days. | High: cash collection is close to revenue. | Accounting partners, SMB finance teams, invoicing-platform ecosystems. | High: no autonomous money movement or financial advice. | BAKEOFF |
| 4 | Contract Intake Classifier | B2B SaaS & Services / Legal Ops | Thomson Reuters reports legal GenAI usage rose from 14% in 2024 to 26% in 2025; document review (74%), research (73%) and summarization (72%) are leading use cases. | Medium-high: review time is billable/operationally expensive. | Legal ops teams, contract managers, law-firm innovation groups. | High: no legal advice or binding interpretation. | SANDBOX |
| 5 | Appointment No-show Recovery Assistant | Health & Wellness / Admin Ops | MGMA reports 27% of responding practices saw no-shows increase in 2025; the issue remains operationally significant across practices. | Medium-high: unused appointment capacity has direct operating impact. | Clinics and practice managers. | High: patient data, messaging consent and medical context. | HOLD |

## Three opportunity briefs

### 1. ReturnOps Exception Copilot - BAKEOFF

**Problem:** return requests combine policy checks, order facts, customer context, refund/exchange routing and fraud/exception handling. High-volume teams need consistent triage without turning the system into an autonomous refund authority.

**Why now:** NRF's 2025 research estimates 19.3% of online sales are returned and says 64% of merchants prioritize updating returns processes in the next six months.

**First paid wedge:** exception triage for one store/workflow: classify standard return vs human review vs exception approval, with reason and source fields.

**Success signal:** lower human triage time without an increase in wrongly auto-progressed exceptions. Measure human edit rate and critical false-auto rate.

**Human gate:** refund exceptions, fraud suspicion, policy override, high-value return and customer compensation remain human-approved.

### 2. Maintenance Intake Triage - BAKEOFF

**Problem:** property managers receive maintenance requests through multiple channels, then manually identify urgency, missing details, property/unit context, vendor category and owner approval requirements.

**Why now:** Buildium's 2025 survey data cited in its 2026 maintenance report says 38% of rental owners selected maintenance among their top pain points, with the next-highest stressor at 22%; more than half say maintenance expertise is a reason they hired a property manager.

**First paid wedge:** intake normalization and routing for one property portfolio, with emergency escalation and missing-information requests.

**Success signal:** faster complete-ticket creation and lower coordinator edit time; zero automated downgrade of emergency indicators.

**Human gate:** emergency severity, tenant safety, vendor commitment and spend approval.

### 3. Accounts Receivable Follow-up Coordinator - BAKEOFF

**Problem:** teams repeatedly review invoice age, status, contact history and account notes before deciding the next reminder/escalation step.

**Why now:** QuickBooks' 2025 US survey reports 56% of small businesses were owed unpaid invoices, averaging $17.5K; 47% had invoices overdue by more than 30 days.

**First paid wedge:** prepare a follow-up queue and draft reminder context from verified invoice records; no payment execution.

**Success signal:** less manual queue-preparation time and higher completion of scheduled follow-ups, without incorrect amounts or unauthorized customer contact.

**Human gate:** discounts, payment plans, disputes, account holds, collections/legal escalation and any money movement.

## First five product briefs

### A. ReturnOps Exception Copilot
- **One-line promise:** Turn return requests into a sourced, review-ready decision queue without auto-approving risky exceptions.
- **Target user:** e-commerce operations manager / returns specialist.
- **Pain:** repeated policy lookup, missing order context, inconsistent exception routing.
- **Three core screens:** Intake Queue; Case Evidence & Policy; Review / Approve / Escalate.
- **Data/source need:** order ID, item/order facts, return policy/version, customer request, prior actions.
- **Human approval point:** exception refunds, fraud flags, policy overrides, compensation.
- **Revenue model:** B2B monthly SaaS after paid pilot; price not set until evidence and workload are measured.
- **First evidence signal:** 30-case bakeoff critical false-auto rate and human edit time.
- **Sandbox boundary:** synthetic orders/policies only; no real refund execution.

### B. Maintenance Intake Triage
- **One-line promise:** Convert messy maintenance requests into complete, prioritized work orders with explicit emergency escalation.
- **Target user:** property manager / maintenance coordinator.
- **Pain:** incomplete requests, repeated clarification, routing and vendor-category work.
- **Three core screens:** Request Inbox; Triage & Missing Info; Escalation / Work Order Review.
- **Data/source need:** property/unit identifier, request text/media metadata, approved vendor categories, emergency rules.
- **Human approval point:** emergency classification confirmation, vendor commitment and spend.
- **Revenue model:** per-portfolio monthly B2B service/SaaS after pilot.
- **First evidence signal:** complete-ticket rate, coordinator edit time, emergency false-negative rate.
- **Sandbox boundary:** synthetic requests; no vendor dispatch or tenant messaging.

### C. Accounts Receivable Follow-up Coordinator
- **One-line promise:** Build a verified invoice follow-up queue and draft the next step without moving money or making financial decisions.
- **Target user:** SMB finance/admin team.
- **Pain:** manual aging review, status checking, reminder context and escalation tracking.
- **Three core screens:** Aging Queue; Invoice Evidence; Draft / Escalation Review.
- **Data/source need:** invoice ledger, due date, amount, customer contact record, prior communication status.
- **Human approval point:** any external message, discount, plan, dispute/collections escalation, money movement.
- **Revenue model:** monthly B2B after narrow pilot.
- **First evidence signal:** queue-prep time, amount/source error rate, human edit rate.
- **Sandbox boundary:** synthetic invoices; no customer contact or payment action.

### D. Contract Intake Classifier
- **One-line promise:** Classify incoming contracts, extract defined fields and build a review queue while leaving legal judgment to qualified humans.
- **Target user:** legal ops / contract manager.
- **Pain:** manual intake, metadata extraction, routing and repeated checklist setup.
- **Three core screens:** Contract Inbox; Extracted Fields & Sources; Review / Route.
- **Data/source need:** approved document set, clause/field taxonomy, workflow rules, versioned source policy.
- **Human approval point:** legal interpretation, risk acceptance, drafting advice, signature/binding action.
- **Revenue model:** paid process analysis/pilot first; SaaS only after compliance and workflow evidence.
- **First evidence signal:** extraction accuracy by field, human edit time, critical routing errors.
- **Sandbox boundary:** synthetic/redacted documents; no legal advice.

### E. Appointment No-show Recovery Assistant
- **One-line promise:** Surface scheduling gaps and prepare consent-aware recovery tasks without making clinical decisions.
- **Target user:** clinic/practice operations manager.
- **Pain:** missed appointment capacity, inconsistent administrative follow-up, rescheduling workload.
- **Three core screens:** Schedule Gaps; Follow-up Eligibility; Human Review / Reschedule Queue.
- **Data/source need:** appointment metadata, communication consent/status, administrative scheduling rules.
- **Human approval point:** patient contact, exceptions, any clinical context or medical advice.
- **Revenue model:** HOLD until privacy/consent/data handling is validated; no price assumed.
- **First evidence signal:** administrative workload and reschedule completion, not health outcome.
- **Sandbox boundary:** synthetic scheduling metadata only; no patient identifiers or clinical content.

## Kill list

Do not build these as autonomous products:

1. **Medical diagnosis / treatment recommender** - high-impact medical decision; outside the safe automation boundary.
2. **Autonomous payment / collections executor** - money movement, disputes and legal escalation require explicit human authority.
3. **Legal advice / contract-signing bot** - binding legal judgment and signature remain with qualified humans.
4. **Generic 'AI agent for everything'** - no defined workflow, source boundary, owner or measurable outcome.
5. **Unlimited custom automation bundle** - scope cannot be controlled or unit economics measured.

## Evidence sources

- NRF, 2025 Retail Returns Landscape: https://nrf.com/research/2025-retail-returns-landscape
- NRF press release on 2025 returns: https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025
- Buildium, maintenance as competitive advantage / 2025 survey evidence: https://www.buildium.com/blog/how-property-managers-can-turn-maintenance-into-a-competitive-advantage/
- QuickBooks, 2025 US Small Business Late Payments Report: https://quickbooks.intuit.com/r/small-business-data/small-business-late-payments-report-2025/
- Thomson Reuters, 2025 GenAI report for legal professionals: https://legal.thomsonreuters.com/blog/genai-report-executive-summary-for-legal-professionals-tri/
- MGMA, Patient no-shows in 2025: https://www.mgma.com/mgma-stat/patient-no-shows-in-2025
