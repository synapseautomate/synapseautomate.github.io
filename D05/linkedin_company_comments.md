# Day 5 - 5 Company Page Comments

These are public, sales-free comments for AI quality / reliability conversations. Post from **Synapse Automate Company Page**, not a personal profile. Do not add our link or offer inside the comments.

## 1) Noman Jalal - agent authority boundaries
Target: https://www.linkedin.com/posts/noman-jalaal_aiagents-agenticai-aiengineering-activity-7493282445438423041-99_L

**Comment:**
The authority boundary is the real product boundary. We would add two questions to the three you listed: *what evidence must exist before the agent is allowed to act, and what gets logged after the action?* Clear permission without source verification can still create a confident failure. Clear permission + evidence + audit trail is much harder to break.

## 2) THSKOD - human review workflow
Target: https://www.linkedin.com/posts/thskod_i-want-ai-to-do-almost-all-of-the-work-before-activity-7487150680248516608-lATS

**Comment:**
A useful human gate needs more than an “Approve” button. The reviewer should see the source, the proposed action, the uncertainty, and a real reject/escalate path. Otherwise HITL can become a rubber stamp rather than a control. The quality of the handoff surface matters as much as the model.

## 3) Darshan Bera - production agent reliability
Target: https://www.linkedin.com/posts/darshan-bera_aiengineering-aiagents-llm-activity-7497684270300241920-dQJw

**Comment:**
“What happens when it is wrong?” is the right production question. Evals should also contain cases where the correct output is *not an answer*: stop, ask for a missing source, escalate, or refuse an unsafe action. A benchmark that only rewards successful completion can accidentally train the system to push through uncertainty.

## 4) Shantanu Mittal - oversight modes
Target: https://www.linkedin.com/posts/shantanu-mittal_agenticai-enterpriseai-aiarchitecture-activity-7497510981258895361-yI4h

**Comment:**
Matching oversight to consequence is the key distinction. One additional metric we like is approval behavior itself: if a supposedly high-risk queue gets 100% approvals with no edits or rejects, the gate may be ceremonial. Oversight should be measurable as a control, not just visible on an architecture diagram.

## 5) Rohith Thirunahari - benchmarks and deliberate failure
Target: https://www.linkedin.com/posts/rohith-tofficial-knowey_aiagents-softwareengineering-productionai-activity-7493509984274554881-POq1

**Comment:**
“A benchmark you can’t lose on isn’t measuring anything” is an important principle. Deliberately mutating expected outcomes is a useful companion test: it checks whether the validator itself can detect a bad expectation, not only whether the agent passes the happy-path set. Reliability needs tests that are capable of turning red.

## Rule

Manual publish only. LinkedIn explicitly treats automated comments as inauthentic automation, so these five comments require the user’s physical click from the Company Page.
