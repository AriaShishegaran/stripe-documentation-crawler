htmlRevenue Recognition with one-time payments | Stripe Documentation[Skip to content](#main-content)One-time payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology%2Fone-time-payments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology%2Fone-time-payments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)[How revenue recognition works](/docs/revenue-recognition/methodology)# Revenue Recognition with one-time payments

Learn how Revenue Recognition works with one-time payments.With one-time payments created in the Dashboard or through the Charges or Payment Intents APIs, Stripe has data on the transaction amount and payment time, but no explicit service period data. By default, Revenue Recognition immediately recognizes the revenue from one-time payments, but you can override this behavior by importing a custom service period.

This example is for a one time payment of 10 USD.

The journal entries generated might look like the following:

DebitCreditAmountAccountsReceivablesDeferredRevenue+10.00CashAccountsReceivables+10.00DeferredRevenueRevenue+10.00This nets out to leave the following end state:

AccountAmountCash+10.00Revenue+10.00CautionTo incorporate a fulfillment schedule into your revenue recognition reports, you must first import the data.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`