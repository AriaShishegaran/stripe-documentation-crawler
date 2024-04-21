htmlRevenue Recognition with multiple currencies | Stripe Documentation[Skip to content](#main-content)Multi-currency[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology%2Fmulti-currency)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology%2Fmulti-currency)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)# Revenue Recognition with multiple currencies

Learn how Revenue Recognition works with multiple currencies.Two types of currencies are important for the purpose of revenue recognition—presentment currencies and settlement currencies. Presentment currencies are the currencies that your customers use to pay, settlement currencies are the currencies that you receive payment in.

For all transactions with presentment currencies matching one of your settlement currencies, Revenue Recognition processes journal entries in that currency directly. In this case, no currency conversion takes place because you can receive payment in that currency directly. Transactions with presentment currencies that aren’t supported as a settlement currency are automatically converted to the default settlement currency for your Stripe account.

Payments and paid invoices use the exchange rate for the actual money movement (that is, what’s reflected on the balance transaction) for revenue recognition. For example, if you collected 10 EUR from a customer that settled in your account as 12 USD, Revenue Recognition uses 12 USD as the transaction amount.

One-time payments and invoices that are paid immediately when they finalize don’t incur exposure to fluctuating exchange rates or foreign exchange gains or losses.

## FX loss

However, sometimes an invoice is finalized first, and paid later. In this case, the exchange rate may have changed between finalization and payment, creating a need to track gains and losses because of foreign exchange.

For revenue recognition purposes (for example, calculating accounts receivable), any activity that gets booked before an invoice is paid uses an estimated exchange rate at the time the invoice finalizes. The difference between the estimated exchange rate and the actual exchange rate, if any, is added to the FxLoss account.

In this example, the exchange rate changes between when the invoice finalizes and when it’s paid—and assumes your account settles in USD, but the customer is paying in EUR.

- On January 1, an invoice finalizes for 30 EUR. The EUR to USD exchange rate is 1.20
- On February 1, the customer pays the invoice for 30 EUR. The EUR to USD exchange rate is 1.10

Because of the change in exchange rate, we expected to receive 36 USD at the time the invoice finalized, but we only received 33 USD when it was paid, resulting in a net FX loss of 3 USD.

AccountJanFebAccountsReceivables+36.00-36.00Revenue+36.00Cash+33.00FxLoss+3.00## FX Loss from refunds and disputes

FxLoss can occur whenever you have a time delay between two operations, which could happen when a payment gets refunded later.

In this example, the exchange rate changes between a one time payment and when it gets refunded—and assume your account settles in USD, and the customer is paying in EUR.

- On January 1, the customer makes a one time payment for 30 EUR. The EUR to USD exchange rate is 1.20.
- On February 1, they receive a refund for 30 EUR. The EUR to USD exchange rate is 1.10

Because of the change in exchange rate, you received 36 USD, but refunded only 33 USD, resulting in a net FX gain of 3 USD.

AccountJanFebRevenue+36.00Cash+36.00-36.00Refunds+33.00FxLoss-3.00Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[FX loss](#fx-loss)[FX Loss from refunds and disputes](#fx-loss-from-refunds-and-disputes)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`