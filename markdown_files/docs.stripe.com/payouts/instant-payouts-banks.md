htmlBank support for Instant Payouts | Stripe Documentation[Skip to content](#main-content)Supported banks[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayouts%2Finstant-payouts-banks)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayouts%2Finstant-payouts-banks)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)
[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[After the payment](/docs/payments/after-the-payment)[Payouts](/docs/payouts)[Instant Payouts](/docs/payouts/instant-payouts)# Bank support for Instant Payouts

Identify whether your account's bank supports Instant Payouts.Regional considerationsUnited StatesCanadaUnited KingdomSingaporeAustraliaStripe supports Instant Payouts for eligible users in the United States, Canada, the United Kingdom, Singapore, and Australia. Instant Payouts in each country must use the local currency. For example, an Instant Payout to a Canadian business must be in CAD.

To see which banks support Instant Payouts, select your country from the dropdown.

Instant Payout support in:United States (US)Canada (CA)Singapore (SG)United Kingdom (GB)Australia (AU)Other countries## Debit cards

Most US banks issue debit cards that can receive Instant Payouts. To see which US banks support Instant Payouts, expand the corresponding section:

### Supports Instant Payouts for all of its debit cards

### Supports Instant Payouts for some of its debit cards

### Does not support Instant Payouts

## Bank accounts

Some US banks also offer Instant Payouts to bank accounts.

### Supports Instant Payouts for its bank accounts

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Debit cards](#debit-cards)[Bank accounts](#bank-accounts)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`