htmlMigrate subscriptions to Stripe Billing | Stripe Documentation[Skip to content](#main-content)Migrate subscriptions to Stripe[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fmigrate-subscriptions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fmigrate-subscriptions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)# Migrate subscriptions to Stripe Billing

Learn about migrating subscriptions from other sources to Stripe.You can import subscriptions from third-party billing systems into Stripe Billing.  To import subscriptions programmatically, use Stripe APIs.

Want to get early access to the Billing Migration toolkit?Enter your email address below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## Before you begin

You must know:

- Your current payment processor.
- Your current subscription provider.
- Your[pricing model](/products-prices/pricing-models).
- How you want to charge your customers on a recurring basis.

## Migration stages

A typical migration process consists of the following stages:

1. Set up your[billing integration](/billing/subscriptions/build-subscriptions).
2. Migrate your customer and payment processor information.
3. Import your subscriptions to Stripe Billing.

![example image](https://b.stripecdn.com/docs-statics-srv/assets/billing-migration.f3bae77ee00a04b8d0baf90518a1db2c.png)

## Getting started

[Migrate subscriptions with APIsLearn how to migrate your subscriptions to Stripe using Stripe APIs.](/billing/subscriptions/import-subscriptions)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Migration stages](#migration-stages)[Getting started](#getting-started)Products Used[Billing](/billing)[Tax](/tax)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`