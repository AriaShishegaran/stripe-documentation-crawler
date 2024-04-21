htmlMirakl reference | Stripe Documentation[Skip to content](#main-content)Reference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Freference)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Freference)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Mirakl](/docs/connectors/mirakl)# Mirakl reference

## Scheduled jobs

### Onboarding

Command Line`php bin/console connector:sync:onboarding -q 2>&1`- Default setting: every minute.
- Recommended setting: as often as possible.
- Description: fetch newly created Mirakl shops and add the onboarding link to their Mirakl back office.
- Documentation:[Onboarding workflow](/connectors/mirakl/onboarding-sellers).

### Payment validation

Command Line`php bin/console connector:validate:pending-debit -q 2>&1`- Default setting: every 5 minutes.
- Recommended setting: < 1 hour.
- Description: fetch newly accepted Mirakl orders, validate the payment on Mirakl, and capture it on Stripe.
- Documentation:[Payment validation workflow](/connectors/mirakl/payments#payment-validation).

### Payment split

Command Line`php bin/console connector:dispatch:process-transfer -q 2>&1`- Default setting: every 5 minutes.
- Recommended setting: < 1 hour.
- Description: fetch newly debited Mirakl orders and create Stripe Transfers from the operator to the seller.
- Documentation:[Payment split workflow](/connectors/mirakl/payments#payment-split).

### Payment refund

Command Line`php bin/console connector:dispatch:process-refund -q 2>&1`- Default setting: every 5 minutes.
- Recommended setting: < 1 hour.
- Description: fetch pending Mirakl refunds, create the refund on Stripe, validate it on Mirakl, and reverse the initial transfer.
- Documentation:[Payment refund workflow](/connectors/mirakl/payments#payment-refund).

### Payout

Command Line`php bin/console connector:dispatch:process-payout -q 2>&1`- Default setting: every day at 1am.
- Recommended setting: synchronized with your Mirakl billing cycles.
- Description: fetch newly created Mirakl[invoices](/api/invoices)and create Stripe Transfers and[Payouts](/payouts).
- Documentation:[Payouts workflow](/connectors/mirakl/payouts#seller-settlement).

### Alerting

Command Line`php bin/console connector:notify:failed-operation -q 2>&1`- Default setting: every day at 8am.
- Recommended setting: according to your preference.
- Description: if[enabled](/connectors/mirakl/configuration#alerting), send an email with all the failed transfers, refunds, and payouts.

## Notification

If enabled, the connector sends server to server notifications in the following events.

NoteIf your endpoint is unreachable or returns an error, an email is sent to your TECHNICAL_ALERT_EMAIL.

### Account updated

A Stripe connected account was updated by the seller or Stripe.

`{
  "type": "account.updated",
  "payload": {
    "miraklShopId": 2000,
    "stripeUserId": "acct_1032D82eZvKYlo2C"
  }
}`### Transfer failed

A transfer failed during the payment split job or the payout job.

`{
  "type": "transfer.failed",
  "payload": {
    "internalId": 5,
    "miraklId": 123,
    "type": "TRANSFER_ORDER",
    "stripeAccountId": "acct_1032D82eZvKYlo2C",
    "miraklShopId": 2003,
    "transferId": null,
    "transactionId": null,
    "amount": 3400,
    "status": "TRANSFER_FAILED",
    "failedReason": "Reason message",
    "currency": "EUR"
  }
}`### Refund failed

A refund failed during the payment refund job job.

`{
  "type": "refund.failed",
  "payload": {
    "internalId": 5,
    "miraklOrderId": "order_refunded_5",
    "miraklRefundId": "1100",
    "stripeRefundId": null,
    "stripeReversalId": "trr_10",
    "amount": 3400,
    "status": "REFUND_FAILED",
    "failedReason": "Reason message",
    "currency": "EUR"
  }
}`### Payout failed

A payout failed during the payout job.

`{
  "type": "payout.failed",
  "payload": {
    "internalId": 12,
    "amount": 2300,
    "currency": "EUR",
    "miraklInvoiceId": 2000,
    "stripePayoutId": null,
    "status": "PAYOUT_FAILED",
    "failedReason": "Reason message",
  }
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Scheduled jobs](#scheduled-jobs)[Notification](#notification)Products Used[Connect](/connect)[Invoicing](/invoicing)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`