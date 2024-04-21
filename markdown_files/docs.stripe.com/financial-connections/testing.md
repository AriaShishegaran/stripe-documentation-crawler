htmlTest Financial Connections | Stripe Documentation[Skip to content](#main-content)Testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Test Financial Connections

Learn how to test your integration with simulated Financial Connections accounts.[Get started with test mode](#get-started)### Testing other Stripe APIs

Refer to the testing documentation to learn more about testing your Stripe integration.

To use the test mode features of Financial Connections, follow the relevant use case guide using a test API key. Accounts and customers that you make in test mode are invisible to your live mode integration.

NoteThe Financial Connections authentication flow is subject to change, so we don’t recommend automated client-side testing. Stripe’s test mode API is also strictly rate limited, which you must account for in your tests.

[How to use test accounts and institutionsServer-side](#web-how-to-use-test-accounts)When you provide Stripe.js with a Financial Connections Session token created using test keys, the authentication flow exclusively shows a selection of test institutions managed by Stripe. The client can link accounts from any of these institutions without providing credentials.

Features like balances, account ownership, and transactions work the same way as they do in live mode, except they return testing data instead of real account data.

Test mode webhooks are separate from live webhooks. Learn about testing your webhook integrations.

[Testing different user authentication scenariosClient-side](#web-test-institutions)Stripe provides a set of test institutions exercising different success and failure scenarios, each represented as a bank in the list of featured institutions.

Simulating successful authentication![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Test Institution: Simulates the user successfully logging into their institution and contains a basic set of test accounts.
- Test OAuth Institution: Contains the same test accounts as Test Institution, but instead of authenticating directly with the modal, it opens an OAuth popup for authentication.
- Ownership Accounts: Contains test accounts representing different ownership states.
- Invalid Payment Accounts: Contains test accounts that are unusable for ACH payments.

Simulating failed authentication![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Down bank (scheduled): The institution’s login API is unavailable for a known time period that the institution communicated to Stripe.
- Down bank (unscheduled): The institution’s login API is unavailable without any information about the downtime communicated to Stripe.
- Down bank (error): Stripe is experiencing an unknown error communicating with the institution.

NoteWe recommend manually testing OAuth and non-OAuth institutions to make sure that both UI flows work within the context your application. See additional documentation about the differences between OAuth and non-OAuth connections.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started with test mode](#get-started)[How to use test accounts and institutions](#web-how-to-use-test-accounts)[Testing different user authentication scenarios](#web-test-institutions)Products Used[Financial Connections](/financial-connections)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`