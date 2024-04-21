htmlExport Bacs data from Stripe | Stripe Documentation[Skip to content](#main-content)Export Bacs data from Stripe[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fexport-data)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fexport-data)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[Bacs Direct Debit](/docs/payments/payment-methods/bacs-debit)# Export Bacs data from Stripe

Learn how to export your Bacs data from Stripe to another payment processor.You can migrate your data from your Stripe account to a new payment processor using the Bacs bulk change process. We work with other payment processors and Bacs sponsor banks throughout the migration to securely migrate your Bacs data. A Bacs migration takes at least 6 weeks to complete.

To import Bacs data from another payment processor to Stripe, see Import Bacs data from Stripe.

[Submit your Bacs export migration request](#submit-bacs-request)Start the migration process by submitting a data migration request.

1. Navigate to the[Stripe Support form for data migrations](https://support.stripe.com/contact/email?topic=migrations). If you’re not signed in, selectSign inand enter the credentials of the account that you want to migrate your data from.
2. SelectExport data out of Stripe to a third party.
3. SelectBacsas the data type you want to export.
4. Complete the remaining fields and selectSend email.

Our data migrations team emails you within 3 business days of receiving your request.

[Print, sign, and send your Bulk Change Deed](#sign-bulk-change-deed)Your new Bacs provider must print and sign a bulk change deed. This agreement authorizes the transfer of your mandates from Stripe to your new payment processor.

CautionSign in to download the bulk change deed.

[Determine your switch date](#determine-switch-date)After we receive your bulk change deed, our Data Migrations team works with you, your new payment processor, and their sponsor bank to agree on a switch date.

[Wait for your data export](#wait-for-export)Our Data Migrations team exports your data and cancels your existing Bacs mandates on the agreed-upon date. This step is irreversible and removes the ability to create charges on these mandates through Stripe.

We control the timing of the export of data from Stripe. There are other tasks that your new processor and their sponsor bank must complete when importing the data.

See Bacs Direct Debit payments in the UK for more information.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Submit your Bacs export migration request](#submit-bacs-request)[Print, sign, and send your Bulk Change Deed](#sign-bulk-change-deed)[Determine your switch date](#determine-switch-date)[Wait for your data export](#wait-for-export)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`