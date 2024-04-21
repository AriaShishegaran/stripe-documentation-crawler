htmlTesting Stripe Radar | Stripe Documentation[Skip to content](#main-content)Testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)# Testing Stripe Radar

Use the following information to test your fraud prevention strategy.Use the following test credit card numbers to create payments in test mode with a specific risk level. Create test payments in either the Stripe Dashboard (in test mode) or by calling create a charge with your test API key.

Card numbersTokensPaymentMethodsNumberDescription4000000000004954Results in a charge with a risk level of`highest`, but could be blocked depending on the rules you have in place (for example, payments made with this card aren’t blocked if the`Block if :risk_level: = 'highest'`rule is disabled).4100000000000019Results in a charge with a risk level of`highest`, and is always blocked regardless of your rules.4000000000009235Results in a charge with a risk level of`elevated`.## Rules

Before you add or update a rule, we’ll search for historical live mode payments that match the rule criteria. You can inspect that list of payments to verify the criterion’s intended behavior, and we also summarize those search results to help you estimate its future impact.

For each rule you test, the summary includes the volume and number of payments that fall into the following categories:

- Disputed & EFW: Payments that received a dispute or an[early fraud warning (EFW)](/disputes/how-disputes-work#early-fraud-warnings).
- Refunded: Payments that were refunded.
- Failed & Blocked: Payments that were either blocked by Radar, blocked by Stripe, or declined by issuers.
- Legitimate: Payments that are successfully processed and haven’t yet been identified as fraudulent nor refunded.

Additionally, when you test allow rules, you can also see Overrides. This refers to payments that Radar blocks due to high risk of fraud or a custom block rule, but now will be allowed by your proposed rule. In the Dashboard, you can see further breakdowns of these summary metrics. For example, you can see refunds that are classified as fraudulent.

![Screenshot that shows the potential impact a custom rule could have](https://b.stripecdn.com/docs-statics-srv/assets/backtesting-review-new-rule.6f8037bd10a5877e60a6237ebdbd414d.png)

Review the sample questions in the following table to help you decide if you can implement your rule.

CautionIt’s uncommon to find a perfect rule that only blocks fraudulent payments or only allows good payments. Thus, your decision to implement a rule is typically based on a trade-off. Consider if this rule will block enough fraudulent payments to be worthwhile compared to any valid payments it might incorrectly block. The trade-off that’s right for you depends on the particulars of your business. For more information, see our fraud detection primer.

Rule typeImplement this rule if…Block- It matches payments that were disputed, received an EFW, or refunded as fraud at the cost of an acceptable amount of legitimate payments for your business.
- It matches refunds and you’re trying to save operational burden and prevent refund abuse.
- It matches payments that failed because issuers declined the payment. Sometimes, issuers might decrease auth rates for you if you send a[high number of transactions that fail](/disputes/prevention/card-testing#consequences)(For example, if a business experiences a large amount of Card Testing).

Review- It matches payments that were disputed, received an EFW, or refunded as fraud. It prompts your team to closely evaluate potential fraudulent transactions or other suspicious payment activities.

Request 3DS- It matches payments that were disputed, received an EFW, or refunded as fraud at the cost of an acceptable amount of legitimate payments for your business. Note: 3DS does not always guarantee that your user will receive a challenge. This means while you might get liability shift if a fraudster passes frictionless 3DS and commits fraud, you might still receive an EFW (which ultimately can lead to identification in VFMP).

Allow- It matches an acceptable amount of previously blocked payments that you have a high degree of certainty should be safe for your business. Allow rules are somewhat trickier to evaluate because there’s no way of knowing which previously-blocked charges would, if allowed, have turned out to be fraudulent. So, with these rules, it’s particularly important to review the list of matching historical payments to ensure these are payments you’d like to allow.
- It doesn’t match a lot of Overrides. This indicates that you are letting through high risk payments.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`