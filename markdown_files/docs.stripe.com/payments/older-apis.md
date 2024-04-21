htmlOlder payment APIs | Stripe Documentation[Skip to content](#main-content)Older APIs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Folder-apis)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Folder-apis)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)# Older payment APIs

Information about our older APIs and the newer APIs that replace them.We’ve replaced some of our older APIs and no longer update their documentation.

## Migrate to current APIs

The older APIs are limited. To get the latest Stripe features, migrate to the Payment Intents, Setup Intents, and Payment Methods APIs. See each individual API’s docs for specifics on migrating.

## Deprecation of the Sources API

We’ve deprecated support for local payment methods in the Sources API and plan to turn it off. If you currently handle any local payment methods using the Sources API, you must migrate them to the current APIs. We’ll communicate more information about this end of support via email.

We’ve also deprecated support for card payments in the Sources API, but don’t currently plan to turn it off.

## Older APIs that remain available

Although unsupported, these APIs aren’t going away. Until you upgrade your integration, you can still use these APIs:

- [Charges](/payments/charges-api)
- [ACH](/ach-deprecated)

## Comparing the APIs

FeaturePayment Intents, Setup Intents, & Payment MethodsCharges, Tokens, & SourcesSupported payment methods[Cards, digital wallets, bank transfers, and so on](/payments/payment-methods/overview)Cards, ACH[SCA-ready](/strong-customer-authentication)Works with[Terminal](/terminal)(in-person payments)Future developmentWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Migrate to current APIs](#migrate-to-current-apis)[Deprecation of the Sources API](#deprecation-of-the-sources-api)[Older APIs that remain available](#older-apis-that-remain-available)[Comparing the APIs](#comparing-the-apis)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`