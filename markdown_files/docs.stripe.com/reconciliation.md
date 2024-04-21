htmlReconciliation | Stripe Documentation[Skip to content](#main-content)Reconciliation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freconciliation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freconciliation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)# ReconciliationBeta

Understand your money movement and automate your payment reconciliation process with Stripe.Use Stripe reconciliation to accurately capture your revenue from the activity on your Stripe account and reconcile it with your system of record and bank statement.

![Overview diagram of reconciliation process on Stripe](https://b.stripecdn.com/docs-statics-srv/assets/reconciliation-overview.1200b3825ccb04aeac7508df80d9c180.png)

How reconciliation works in Stripe.

Stripe reconciliation offers you the capability to perform two types of reconciliations:

[Bank reconciliationBank reconciliation enables you to reconcile Stripe payouts with the cash in your bank account and verify the monthly summary of your revenue to cash breakdown.](/reconciliation/bank-reconciliation)[Transaction reconciliationTransaction reconciliation helps you reconcile your transaction level records with charges and refunds processed on Stripe.](/reconciliation/transaction-reconciliation)Using Stripe reconciliation, you can:

- Track your cash on a daily basis.
- Identify gaps in fund flows or data discrepancies to fix leakages faster.
- Gain visibility into the complete lifecycle of each transaction.
- Implement strong financial controls to protect your business.
- Set up scalable processes for your financial operations that can grow with your business.

Interested in using reconciliation?Enter your email address and our team will be in touch to give you access.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!NoteStripe’s reconciliation features aren’t a substitute for professional services or professional advice.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`