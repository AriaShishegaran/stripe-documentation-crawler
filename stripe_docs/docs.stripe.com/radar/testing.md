# Testing Stripe Radar

Use the following test credit card numbers to create payments in test mode with a specific risk level. Create test payments in either the Stripe Dashboard (in test mode) or by calling create a charge with your test API key.

[test mode](/keys#test-live-modes)

[Stripe Dashboard](https://dashboard.stripe.com/test/payments)

[create a charge](/api#create_charge)

[test API key](/keys)

## Rules

Before you add or update a rule, we’ll search for historical live mode payments that match the rule criteria. You can inspect that list of payments to verify the criterion’s intended behavior, and we also summarize those search results to help you estimate its future impact.

[add or update a rule](/radar/rules)

For each rule you test, the summary includes the volume and number of payments that fall into the following categories:

- Disputed & EFW: Payments that received a dispute or an early fraud warning (EFW).

[early fraud warning (EFW)](/disputes/how-disputes-work#early-fraud-warnings)

- Refunded: Payments that were refunded.

- Failed & Blocked: Payments that were either blocked by Radar, blocked by Stripe, or declined by issuers.

- Legitimate: Payments that are successfully processed and haven’t yet been identified as fraudulent nor refunded.

Additionally, when you test allow rules, you can also see Overrides. This refers to payments that Radar blocks due to high risk of fraud or a custom block rule, but now will be allowed by your proposed rule. In the Dashboard, you can see further breakdowns of these summary metrics. For example, you can see refunds that are classified as fraudulent.

Review the sample questions in the following table to help you decide if you can implement your rule.

It’s uncommon to find a perfect rule that only blocks fraudulent payments or only allows good payments. Thus, your decision to implement a rule is typically based on a trade-off. Consider if this rule will block enough fraudulent payments to be worthwhile compared to any valid payments it might incorrectly block. The trade-off that’s right for you depends on the particulars of your business. For more information, see our fraud detection primer.

[fraud detection primer](https://stripe.com/radar/guide#fraud-prevention-performance)

- It matches payments that were disputed, received an EFW, or refunded as fraud at the cost of an acceptable amount of legitimate payments for your business.

- It matches refunds and you’re trying to save operational burden and prevent refund abuse.

- It matches payments that failed because issuers declined the payment. Sometimes, issuers might decrease auth rates for you if you send a high number of transactions that fail (For example, if a business experiences a large amount of Card Testing).

[high number of transactions that fail](/disputes/prevention/card-testing#consequences)

- It matches payments that were disputed, received an EFW, or refunded as fraud. It prompts your team to closely evaluate potential fraudulent transactions or other suspicious payment activities.

- It matches payments that were disputed, received an EFW, or refunded as fraud at the cost of an acceptable amount of legitimate payments for your business. Note: 3DS does not always guarantee that your user will receive a challenge. This means while you might get liability shift if a fraudster passes frictionless 3DS and commits fraud, you might still receive an EFW (which ultimately can lead to identification in VFMP).

- It matches an acceptable amount of previously blocked payments that you have a high degree of certainty should be safe for your business. Allow rules are somewhat trickier to evaluate because there’s no way of knowing which previously-blocked charges would, if allowed, have turned out to be fraudulent. So, with these rules, it’s particularly important to review the list of matching historical payments to ensure these are payments you’d like to allow.

- It doesn’t match a lot of Overrides. This indicates that you are letting through high risk payments.
