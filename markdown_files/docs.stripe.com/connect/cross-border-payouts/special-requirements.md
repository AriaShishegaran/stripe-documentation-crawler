htmlCountry-specific considerations for cross-border payouts | Stripe Documentation[Skip to content](#main-content)Country-specific considerations for cross-border payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcross-border-payouts%2Fspecial-requirements)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcross-border-payouts%2Fspecial-requirements)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Cross-border payouts](/docs/connect/cross-border-payouts)# Country-specific considerations for cross-border payouts

Learn which countries have additional requirements for receiving payments from outside their borders.Connected accounts in certain countries might have additional bank or fund flow restrictions when using cross-border payouts.

## Bank restrictions

Most banks can accept payments from other countries without any special requirements. Some banks in certain countries require more information regarding recipient identity or transaction information for risk and compliance purposes. The receiving bank often has discretion over what they require for cross-border transactions, which can differ between banks, even within the same country.

If a seller or service provider onboards as a connected account to your platform in one of these countries, we send an email to alert your user of the possibility for additional requirements. If the receiving bank requires additional information, they should reach out to your user directly with their requirements.

NoteBanks might have special requirements in certain countries, so your user might pay additional fees for the payout. Stripe might also set a higher minimum payout threshold to account for possible fees charged by certain banks.

The list of possible requirements for the following countries isn’t exhaustive, as Stripe isn’t involved with creating these conditions. If you encounter additional requirements that aren’t listed, please notify Stripe support.

Possible special requirements include:

### Bangladesh

- Submitting a remittance form.
- Providing a receipt or invoice as proof that the recipient is legitimately receiving the payment.
- Paying additional fees.

### Japan

- Visiting a bank location to submit a copy of their ID and additional paperwork, if they haven’t previously done so. Banks require a national ID card number (MyNumber) to be submitted and on file before they can receive or send international transfers.
- Providing a receipt or invoice as proof that the recipient is legitimately receiving the payment.
- Paying additional fees.
- Supporting payouts only to banks participating in the Foreign Exchange Yen Clearing System (FXYCS).

### Serbia

- Providing additional information on the purpose of the payment.
- Providing a receipt or invoice as proof that the recipient is legitimately receiving the payment.
- Submitting a remittance form.

## Fund flow restrictions

The following fund flows are generally supported in countries for cross-border payouts:

- [Separate charges and transfers](/connect/separate-charges-and-transfers)without the`on_behalf_of`parameter
- Top-up and transfers
- [Destination charges](/connect/destination-charges)

Direct charges and destination charges with the on_behalf_of parameter aren’t supported. However, some countries have additional limitations.

For Brazil, India, and Thailand, only the following fund flows are supported:

- [Separate charges and transfers](/connect/separate-charges-and-transfers)without the`on_behalf_of`parameter
- Top-up and transfers

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Bank restrictions](#bank-restrictions)[Fund flow restrictions](#fund-flow-restrictions)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`