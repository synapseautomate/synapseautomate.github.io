# Contributing

## Small-change workflow
1. State the customer/revenue or proof problem in one sentence.
2. Identify the smallest file set that can solve it.
3. Add or update tests before expanding scope.
4. Run UTF-8, secret, link, schema/FAQ, mobile overflow, and regression checks.
5. Explain the diff in customer terms: what changed, what did not, risk, rollback.

## Do not commit
- Secrets or personal/customer data.
- Unverified claims or fake cases.
- Hidden medical/legal/financial decision logic presented as authoritative advice.
- New integrations or external writes without an explicit approval design.
- Low-value scaled pages created only for search volume.

## Test expectations
A malformed file, unsupported type, duplicate, or ambiguous high-impact decision must fail closed or route to human review. Public examples remain synthetic/redacted.
