# Proof / Offer Change Tracking Protocol

Track only changes that can be tied to the revenue chain.

- `change_id`
- `date`
- `surface`: title / cover / price presentation / FAQ / proof badge / CTA
- `hypothesis`
- `baseline`: impressions / clicks / forms / qualified inbound / payment
- `post_change_window`
- `result`
- `decision`: keep / revert / inconclusive

Stop-loss: no impressions -> distribution/cover; impressions no clicks -> message/CTA; clicks no forms -> trust/offer; forms no payment -> scope/price/proof. Do not change code first.
