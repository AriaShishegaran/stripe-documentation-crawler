htmlUsage-based billing | Stripe Documentation[Skip to content](#main-content)Usage-based Billing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)# Usage-based billing

Charge customers based on how much they use your product or service.NoteWe updated our usage-based billing process. For information on our previous guidance, refer to our legacy usage-based billing documentation.

[Billing](/billing)Usage-based billing (also known as metered billing or consumption billing) is a common pricing model for SaaS businesses that enables you to charge based on a customer’s usage of your product or service. As a business, you provide access to your service and bill your customer based on their usage. With Stripe Billing, you can set up and integrate different types of usage-based pricing models with your SaaS product.

[Set up usage-based billing](/docs/billing/subscriptions/usage-based/implementation-guide#what-you-will-build)![](https://b.stripecdn.com/docs-statics-srv/assets/usage-based-billing.7815fc3949e9351fd5e39cb2b02e4eca.svg)

## Getting started

[Set up usage-based billingUnderstand the major pieces of a usage-based billing integration.](/billing/subscriptions/usage-based/implementation-guide)[Record usage for billingReport customer usage to Stripe.](/billing/subscriptions/usage-based/recording-usage)[Usage-based billing modelsLearn how to model usage-based pricing on Stripe.](/billing/subscriptions/usage-based/pricing-models)NoteUBB data is accessible only in Stripe Subscriptions and Invoices. We’re striving for full interoperability of UBB data across our product suite.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`