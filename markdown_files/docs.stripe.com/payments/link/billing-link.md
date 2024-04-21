htmlLink with Billing | Stripe Documentation[Skip to content](#main-content)Link with Billing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fbilling-link)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fbilling-link)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)
Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[Faster checkout with Link](/docs/payments/link)# Link with Billing

Speed up invoice payments by using Link with the Hosted Invoice Page.Use Link with the Hosted Invoice Page to let your customers pay invoices faster. Stripe assigns all invoices a unique URL that you can send to your customer. We host these invoices, which means you can securely collect payments without any extra implementation code. Link is compatible with both the Invoices and Subscriptions APIs.

![Link in the Hosted Invoice Page](https://b.stripecdn.com/docs-statics-srv/assets/link-in-hip.a98a2864a383c265c375109b168d62ab.png)

Link in the Hosted Invoice Page

## Enable Link in the Hosted Invoice Page

Your customers can pay invoices faster using Link as a payment method to autofill their payment details. The Hosted Invoice Page provides a secure, private URL where your customers can view, pay, and download copies of the invoice.

To enable Link on the Hosted Invoice page:

1. Go to the[Invoice template](https://dashboard.stripe.com/settings/billing/invoice)in the Dashboard and underPayment methods, clickManage.
2. Find Link, toggle it on, and clickSave.

After you enable Link in the Hosted Invoice Page, all of your customers will be able to pay their invoices faster using Link.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`