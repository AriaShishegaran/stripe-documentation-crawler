htmlStripe Connector for Mirakl | Stripe Documentation[Skip to content](#main-content)Mirakl[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)# Stripe Connector for Mirakl

Leverage the power of Stripe on Mirakl-built marketplaces.Connect is the perfect fit for Mirakl marketplaces:

- Compatible with all the[payment methods](https://stripe.com/payments/features#payment-options)offered by Stripe.
- Works for B2C and B2B marketplaces.
- Supports multi-seller and hybrid orders.
- Automated[payouts](/payouts)based on your configuration.

## Integration steps

The main tasks to set up payments for your marketplace using Mirakl are:

1. First, you need a Stripe account.[Register](https://dashboard.stripe.com/register).
2. Implement the relevant payment methods. Use one of our[existing plugins](/connectors)or[build your own integration](/payments).
3. [Activate Connect](https://dashboard.stripe.com/connect/accounts/overview)in your Dashboard. ChoosePlatform or marketplaceas your integration type.
4. Configure your[Connect branding settings](https://dashboard.stripe.com/settings/connect).
5. [Configure](/connectors/mirakl/configuration)and[install](/connectors/mirakl/install)the connector on your test environment.
6. Adapt your communication to sellers as described in the[onboarding workflow](/connectors/mirakl/onboarding-sellers#communication).
7. Adapt your payments requests as described in the[payment split workflow](/connectors/mirakl/payments#payment-validation)
8. Test the different workflows: onboarding, payments, refunds, and payouts.
9. [Activate](https://dashboard.stripe.com/account/onboarding)your Stripe account.
10. Complete your[Platform profile](https://dashboard.stripe.com/connect/profile).
11. [Configure](/connectors/mirakl/configuration)and[install](/connectors/mirakl/install)the connector on your live environment.
12. Go live.

Optionally, you can use Radar for fraud protection or Stripe Billing to create and manage invoices and recurring payments.

## Workflows

Learn more about each workflow:

- [Onboarding sellers](/connectors/mirakl/onboarding-sellers)
- [Payments](/connectors/mirakl/payments)
- [Payouts](/connectors/mirakl/payouts)

## Alerting

The workflows supported by the connector don’t require any manual intervention or operational supervision. In case an operation fails, the alerting job sends you an email.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Integration steps](#integration-steps)[Workflows](#workflows)[Alerting](#alerting)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`