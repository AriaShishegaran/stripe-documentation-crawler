htmlService agreement types | Stripe Documentation[Skip to content](#main-content)Service agreement types[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fservice-agreement-types)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fservice-agreement-types)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Service agreement types

A service agreement establishes the relationship between Stripe and the platform's users.The connected account’s service agreement type determines what capabilities the account has access to, and which service agreement applies to the platform’s users.

### Account types

Connect platforms can work with three different account types.

The content on this page applies only to Express and Custom accounts.

## Supported agreement types

Connected accounts can be under one of the following service agreement types: full or recipient. After the connected account’s service agreement is accepted, the type of service agreement can’t be modified.

### Full service agreement

A full service agreement creates a service relationship between Stripe and the connected account holder. Connected accounts under the full service agreement can process card payments and request the card_payments capability.

For the legal language, see the Stripe Connected Account Agreement.

### Recipient service agreement

A recipient service agreement clarifies that there is no service relationship between Stripe and the recipient, and that the recipient’s relationship is with the platform. Connected accounts under the recipient service agreement can’t process payments or request the card_payments capability.

Transfers to recipient accounts take an extra 24 hours to become available in the connected account’s balance. To learn more about pending balances, see the account balances page.

Cross-border payouts only work with accounts under the recipient service agreement. You must explicitly pass in the country code if it differs from the platform country.

Stripe isn’t responsible for providing direct support for accounts on the recipient service agreement. However, the platform can reach out to Stripe for support for these accounts.

For the legal language, see the Stripe Recipient Agreement.

## Choosing the agreement type

You can specify the agreement type through the Accounts API.

### Accounts API

To choose a recipient service agreement when creating an account, specify the agreement type with tos_acceptance[service_agreement]:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d country=US \
  -d type=custom \
  -d "capabilities[transfers][requested]"=true \
  -d "tos_acceptance[service_agreement]"=recipient`The same principle applies when updating an account:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "tos_acceptance[service_agreement]"=recipient`CautionChanging the service agreement type fails if the service agreement has already been accepted; in those cases, create a new account with the desired service agreement.

### Connect Configuration settings

To choose a recipient service agreement for all new Express accounts, select the Transfers option with the Restricted Capability Access icon in the Configuration settings section of the Stripe Dashboard.

You can override the Configuration settings for an individual account by specifying its capabilities and service agreement type with the Accounts API.

## Accepting the correct agreement

For Express and Connect Onboarding for Custom accounts, Stripe handles the service agreement acceptance.

For other Custom accounts, the platform must attest that their user has seen and accepted the service agreement. See service agreement acceptance for more information.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Supported agreement types](#supported-types)[Choosing the agreement type](#choosing-type)[Accepting the correct agreement](#accepting-the-correct-agreement)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`