# Day 13 — 5 public comments from Synapse Automate Company Page

No links in the comments. No selling. Comment only as the Company Page.

## 1 — Ernest D. / runtime control & excessive agency
Post: https://www.linkedin.com/posts/ernestdeleon_aigovernance-agenticai-cybersecurity-activity-7503076504969547776-91Mn

Comment:
The blast radius is the useful design unit. A workflow should assume untrusted content can eventually influence model behavior, then constrain what that behavior can actually read, write, transmit or approve. Prompt defenses matter, but capability and egress boundaries determine consequence.

## 2 — Kamal Rupareliya / permissions problem
Post: https://www.linkedin.com/posts/krupareliya_aiagents-aisecurity-promptinjection-activity-7504179795321319425-j8fn

Comment:
This is why “the model got the answer right” is not an authorization test. Read, propose, write and external-send should be separate capabilities. If a workflow cannot show which authority produced an action, the control surface is incomplete even when the output looks correct.

## 3 — Risk AI Council / untrusted data-plane
Post: https://www.linkedin.com/posts/riskaicouncil_aigovernance-agenticai-owasptop10-activity-7499352778444664832-13HS

Comment:
A practical boundary is to make retrieved content incapable of granting authority. Documents, tickets and web pages can supply data; they should not expand tool scope, write permissions or destinations. Suspicious content intersecting a consequential action should become an explicit stop/escalation state.

## 4 — Mohd Sohaib / human approval is not enough
Post: https://www.linkedin.com/posts/sohaibmohd_aisecurity-promptinjection-agenticai-activity-7488852643956543488-WX9e

Comment:
Agreed on the ordering. Human approval is strongest after deterministic policy checks have already constrained the proposal. The reviewer needs source, proposed action, authority, consequence and the exact exception — otherwise “Approve” can become a presentation layer rather than a control.

## 5 — Software Analyst Cyber Research / prompt injection + excessive agency
Post: https://www.linkedin.com/posts/software-analyst_cybersecurity-aisecurity-agenticai-activity-7437576851172118528-fuZq

Comment:
These two risks amplify each other. Prompt injection is the steering problem; excessive agency sets the maximum damage. Testing them separately misses the interaction. A useful regression case combines untrusted content with a real capability boundary and verifies that the workflow stops before consequence.
