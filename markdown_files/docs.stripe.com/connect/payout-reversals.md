htmlPayout reversals | Stripe Documentation[Skip to content](#main-content)Payout reversals[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayout-reversals)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayout-reversals)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Payout reversals

Learn how to reverse a payout sent to a connected account.When the platform is responsible for risk and negative balances, you can make a payout reversal from an external bank account back to the connected account’s balance.

You can make payout reversals from the Dashboard payout details page or by calling reverse payout.

![Reverse payouts in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/reverse_payout_button.cb224dbe2ceae893b5a0ecef855f8f7b.png)

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/payouts/{{PAYOUT_ID}}/reverse \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`## Requirements

To be reversed, a payout:

- Must be to a bank account in the US.
- Must be expected to arrive less than 90 days ago.
- Can’t be a debit or an[Instant Payout](/connect/instant-payouts).

## Webhooks

Payout reversals are considered debits and have the same webhooks as other payouts. For example, when a payout reversal is first requested, a payout.updated event is sent for the original payout. Then, events for the payout reversal are sent, including payout.created, payout.updated, payout.paid, and possibly a payout.failed event.

## Failures

If the original payout fails while the payout reversal is in a pending state, Stripe cancels the reversing payout. A payout reversal in the paid state can later be refused by the associated bank and transition to the failed state. This results in a payout.failed event. Failed payout reversals aren’t retried.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Requirements](#requirements)[Webhooks](#webhooks)[Failures](#failures)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`