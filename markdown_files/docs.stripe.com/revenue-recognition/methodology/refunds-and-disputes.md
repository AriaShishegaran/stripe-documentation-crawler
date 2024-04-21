htmlRevenue Recognition with refunds and disputes | Stripe Documentation[Skip to content](#main-content)Refunds and disputes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology%2Frefunds-and-disputes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology%2Frefunds-and-disputes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)[How revenue recognition works](/docs/revenue-recognition/methodology)# Revenue Recognition with refunds and disputes

Learn how Revenue Recognition works with refunds and disputes.Refunds and disputes can happen to any transaction on Stripe, which affects your revenue numbers.

## Handling a refund or dispute

Stripe handles refunds and disputes in a similar manner, but the contra revenue generated go to the refunds and disputes accounts respectively.

When a refund or dispute is made,

- Cash is returned to the customer.
- Prior recognized revenue is offset by contra revenue in the refund or dispute account.
- Deferred revenue that hasn’t been recognized is cleared.

This next example is a one-time payment refund.

- On January 1, a customer made a one-time payment for 90 USD.
- On February 1, the transaction was refunded.

In this situation, the full amount of 90 USD is recognized as revenue, and subsequently the full amount of 90 USD is added to the refunds contra revenue account.

AccountJanFebRevenue+90.00Refunds+90.00In this example, the invoice for a subscription was disputed.

- On January 1, a customer starts a three month subscription for 90 USD, which generates and finalizes an invoice.
- The customer pays 90 USD.
- On February 1, the customer disputes the transaction.

In this case, the customer received 31 days worth of service, so 31 USD is placed in the disputes account. The dispute also reduces the cash by 90 USD, and the remaining 59 USD of deferred revenue is cleared. At the end of February, the account balances looks like the following:

AccountJanFebRevenue+31.00DeferredRevenue+59.00-59.00Cash+90.00-90.00Disputes+31.00## Winning a dispute

Disputes are different from refunds in one way—you can win disputes.

When you win a dispute,

- Cash is returned to you.
- Recognized and deferred revenue don’t change.
- Cash is offset by an increase in the recoverables account.

In the previous example, assume that you win the dispute on March 1. If you then looked at the account balances at the end of March, you’d see that cash increased by 90 USD, which is offset by recoverables.

AccountJanFebMarRevenue+31.00DeferredRevenue+59.00-59.00Cash+90.00-90.00+90.00Disputes+31.00Recoverables+90.00Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Handling a refund or dispute](#handling-a-refund-or-dispute)[Winning a dispute](#winning-a-dispute)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`