htmlPricing | Stripe Documentation[Skip to content](#main-content)Pricing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fpricing)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fpricing)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)# Pricing

Learn about fees and pricing tiers for Revenue Recognition.Stripe charges a fee for every payment that we process. To see what fees we charged, read the fees report, which Stripe updates daily. Some fees for line items might take a few days to appear in the report.

The following table explains Revenue Recognition fees.

SituationRevenue Recognition fees chargedSuccessful transactionsStripe applies the fee only when a payment succeeds (for example, when an invoice is paid or when a one-time payment is made).Transactions processed by StripeStripe calculates the fee based on the volume processed, rather than the volume recognized. If a user paid 120 USD for an annual subscription on December 1, Stripe calculates the fee based on the 120 USD volume in December, rather than the 10 USD recognized in December.Refunded transactionsIf you refund the corresponding payment, Stripe won’t refund the Revenue Recognition fee.Excluded transactionsStripe charges a fee for all transactions we process, which means you incur a fee even if you exclude a transaction from Revenue Recognition using[custom rules](/revenue-recognition/rules). The transaction still counts toward your volume because Stripe successfully processed the transaction.Voided transactionsIf you void an invoice, it won’t appear in your monthly volume and Stripe won’t charge the Revenue Recognition fee.## Fees for multiple settlement currencies

Each currency has an equivalent threshold. If you have multiple settlement currencies, the combined percentage of thresholds met determines the final fee tier. For each currency, Stripe computes the percentage of volume to the currency’s volume threshold. We call this percentage-to-threshold volume. If the total percentage-to-threshold-volume is more than 100, you qualify for a lower-priced tier.

To demonstrate, see the following two example scenarios.

Scenario 1![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The total percentage-to-threshold-volume is 82%, which means you don’t qualify for the discount.

CurrencyMerchant volumeThreshold volumePercentage-to-threshold volumeUSD80,000100,00080%GBP1,00050,0002%Scenario 2![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The total percentage-to-threshold-volume is 120%, which means you qualify for the discount.

CurrencyMerchant volumeThreshold volumePercentage-to-threshold volumeUSD80,000100,00080%GBP20,00050,00040%## Features without fees

Stripe doesn’t charge fees for:

- [Rules](/revenue-recognition/rules)
- [Reports](/revenue-recognition/reports)
- [Accounting period controls](/revenue-recognition/accounting-period-control)
- [Data export](/revenue-recognition/api)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Fees for multiple settlement currencies](#fees-for-multiple-settlement-currencies)[Features without fees](#features-without-fees)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`