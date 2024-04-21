htmlCartes Bancaires (CB) | Stripe Documentation[Skip to content](#main-content)Cartes Bancaires[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcartes-bancaires)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcartes-bancaires)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Cards](/docs/payments/cards)# Cartes Bancaires (CB)

Learn about Cartes Bancaires, a common payment method in France.Customer Geography: Europe

Payment Method Type: Credit, Debit, and Prepaid Card

Presentment Currency: EUR

Disputes: Yes

Refunds / Partial Refunds: Yes / Yes

Recurring Payments: Yes

Cartes Bancaires is France’s local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Businesses processing co-badged cards in the EEA must provide customers a choice of which network they prefer at checkout time. See our guide for co-badged cards compliance for more information.

Cartes Bancaires will likely have a positive effect on your acceptance rate in France. If a charge is declined on the Cartes Bancaires network for a technical reason, Stripe automatically retries the charge on Visa or Mastercard’s networks.

As with Visa and Mastercard, cardholders can dispute Cartes Bancaires charges. Because Cartes Bancaires dispute rules are more stringent, there are fewer reasons that a cardholder can dispute a charge, which on average leads to a lower dispute rate compared to Visa and Mastercard for many of our merchants. Merchants cannot contest Cartes Bancaires disputes - the dispute fee is 0 Euro on Cartes Bancaires.

## Availability

Merchants located in these countries have Cartes Bancaires available. If your business isn’t based in France, Cartes Bancaires won’t be fully enabled until your account has processed 50 EUR from Cartes Bancaires eligible cards. French Stripe accounts with the “type of business” set as “Particulier / Micro-entrepreneur / Auto-entrepreneur” are eligible for Cartes Bancaires after providing their business tax ID in the Dashboard settings.

## Integration

If you can already accept card payments, you can accept Cartes Bancaires. See the co-badged cards compliance guide to learn how to best handle customer priority selection, and to find multiple test cards that you can use to test your integration as soon as it’s active. If you require that Cartes Bancaires is never the default network for any payments, please contact support.

Interested in enabling Cartes Bancaires with Apple Pay?Access to Cartes Bancaires with Apple Pay is currently limited to beta users. If you're interested in this feature, enter your email address and we'll respond to you shortly.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Availability](#availability)[Integration](#integration)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`