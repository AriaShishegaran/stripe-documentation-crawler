htmlPayouts | Stripe Documentation[Skip to content](#main-content)Payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fpayouts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fpayouts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Mirakl](/docs/connectors/mirakl)# Payouts

The amount and frequency of each payout to your sellers is controlled by Mirakl based on your settings.

You can customize your billing cycles under Settings > Shops > Billing Cycles. By default, your sellers receive their payouts on the 1st, 11th, and 21st of each month.

## Seller settlement

The workflow starts when Mirakl generates a new invoice.

1. The[payout job](/connectors/mirakl/reference#payout)fetches newly created Mirakl invoices.
2. The connector performs the following actions based on the invoice attributes:

Invoice attributeAction takentotal_other_credits_incl_taxTransfer from the operator to the seller.total_other_invoices_incl_taxTransfer from the seller to the operator.total_subscription_incl_taxTransfer from the seller to the operator.amount_transferredPayout to the Seller.NoteCommissions are already handled during the payment split workflow.

![](https://b.stripecdn.com/docs-statics-srv/assets/payout.514743e5e90d9862245e84cc1c9d3ea2.svg)

## See also

- [Integration steps](/connectors/mirakl#integration-steps).

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Seller settlement](#seller-settlement)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`