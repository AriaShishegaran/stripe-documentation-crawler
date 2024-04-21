htmlSupported Connect embedded components | Stripe Documentation[Skip to content](#main-content)Supported Connect embedded components[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Supported Connect embedded components

Learn about current and upcoming embedded components.Add Connect embedded components to your page as HTML Elements or as React components.

## Available components

[Account management](/connect/supported-embedded-components/account-management)Show account details and allow them to be edited.[Account onboarding](/connect/supported-embedded-components/account-onboarding)Show a localized onboarding form that validates data.[Balances](/connect/supported-embedded-components/balances)Show balance information and allow your connected accounts to perform payouts.[Documents](/connect/supported-embedded-components/documents)Show a list of documents available for download.[Notification banner](/connect/supported-embedded-components/notification-banner)Show a banner that lists required actions for risk interventions and onboarding requirements.[Payments](/connect/supported-embedded-components/payments)Show a list of payments with export, refund, and dispute capabilities.[Payment details](/connect/supported-embedded-components/payment-details)Show details of a given payment and allow users to manage disputes and perform refunds.[Payouts](/connect/supported-embedded-components/payouts)Show payout information and allow your users to perform payouts.[Payouts list](/connect/supported-embedded-components/payouts-list)Show a filterable list of payouts.## Beta components Beta

When using private beta components, use beta versions of the Stripe SDK, as well as beta versions of the @stripe/connect-js and @stripe/react-connect-js SDKs.

To create an account session with private beta components, use the Stripe beta SDKs:

- [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks)`>=11.1.0-beta.1`
- [Python](https://github.com/stripe/stripe-python/#beta-sdks)`>=9.2.0b1`
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks)`>=14.2.0-beta.1`
- [Node](https://github.com/stripe/stripe-node/#beta-sdks)`>=15.2.0-beta.1`
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks)`>=44.2.0-beta.1`
- [Java](https://github.com/stripe/stripe-java#beta-sdks)`>=25.2.0-beta.1`
- [Go](https://github.com/stripe/stripe-go#beta-sdks)`>=78.2.0-beta.1`

Use the client-side libraries for rendering the private beta components:

npmGitHubInstall the library:

`npm install --save @stripe/connect-js@beta`If you’re using React in your application:

`npm install --save @stripe/react-connect-js@beta`### Available beta components

[App install](/connect/supported-embedded-components/app-install)Show a button to install an App.[App viewport](/connect/supported-embedded-components/app-viewport)Show a view from an installed App.[Capital Financing Overview](/connect/supported-embedded-components/capital-overview)Show Capital offers and loan progress details.[Financial Account](/connect/supported-embedded-components/financial-account)Show details of a Financial Account.[Financial Account transactions](/connect/supported-embedded-components/financial-account-transactions)Show a table of all transactions for a Financial Account.[Issuing card](/connect/supported-embedded-components/issuing-card)Show an individual issued card.[Issuing cards list](/connect/supported-embedded-components/issuing-cards-list)Show a table of all issued cards.[Payment method settings](/connect/supported-embedded-components/payment-method-settings)Show a list of payment methods that connected accounts can manage and accept.[Tax settings](/connect/supported-embedded-components/tax-settings)Allow connected accounts to set up Stripe Tax.[Tax registrations](/connect/supported-embedded-components/tax-registrations)Show and manage tax registrations from connected accounts.## Integration guides

[Accounting integrations](/stripe-apps/accounting-software-integrations)Show third-party accounting software integrations.[Fully embedded Connect platform integration](/connect/build-full-embedded-integration)Allow your connected accounts to access Stripe Connect features from your own website, without a Stripe hosted dashboard.[Embedded finance](/baas/start-integration/integration-guides/embedded-finance?integration=embedded)Use prebuilt UI components to embed Issuing and Treasury into your website.[Migrating from the v1 to v2 betaBeta](#migrating-v1-to-v2-beta)1. Update your client library.  - [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks)`>=11.1.0-beta.1`
  - [Python](https://github.com/stripe/stripe-python/#beta-sdks)`>=9.2.0b1`
  - [PHP](https://github.com/stripe/stripe-php/#beta-sdks)`>=14.2.0-beta.1`
  - [Node](https://github.com/stripe/stripe-node/#beta-sdks)`>=15.2.0-beta.1`
  - [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks)`>=44.2.0-beta.1`
  - [Java](https://github.com/stripe/stripe-java#beta-sdks)`>=25.2.0-beta.1`
  - [Go](https://github.com/stripe/stripe-go#beta-sdks)`>=78.2.0-beta.1`


2. Update the beta header used from`embedded_connect_beta=v1`to`embedded_connect_beta=v2`.
3. Specify the list of`components`to enable as a parameter when creating an[Account Session](/api/account_sessions/create).

[Migrating from v2 beta to GA](#migrating-v2-beta-to-ga)If you’re using a beta component that’s now generally available, follow these steps:

1. Update your client library.  - [Ruby](https://github.com/stripe/stripe-ruby)`>=11.1.0`
  - [Python](https://github.com/stripe/stripe-python)`>=9.2.0`
  - [PHP](https://github.com/stripe/stripe-php)`>=14.2.0`
  - [Node](https://github.com/stripe/stripe-node)`>=15.2.0`
  - [.NET](https://github.com/stripe/stripe-dotnet)`>=44.2.0`
  - [Java](https://github.com/stripe/stripe-java)`>=25.2.0`
  - [Go](https://github.com/stripe/stripe-go)`>=78.2.0`


2. Remove the`embedded_connect_beta`header.
3. Use the GA releases of the`@stripe/connect-js`and`@stripe/react-connect-js`npm packages.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Available components](#available-components)[Beta components](#beta-components)[Integration guides](#integration-guides)[Migrating from the v1 to v2 beta](#migrating-v1-to-v2-beta)[Migrating from v2 beta to GA](#migrating-v2-beta-to-ga)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`