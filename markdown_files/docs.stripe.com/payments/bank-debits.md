htmlBank Debits | Stripe Documentation[Skip to content](#main-content)Bank debits[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-debits)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-debits)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Bank Debits

Learn how to accept bank debits with Stripe.With bank debits, you can pull funds directly from your customer’s bank account for both one-time and recurring purchases. Bank debits are often used by:

- Businesses collecting recurring payments from other businesses.
- Retail and services businesses that want a low-cost alternative to cards for large consumer payments, like rent or tuition.

Bank debits might not be a good fit for your business if:

- You deliver goods immediately after checkout because payment confirmation takes 3-7 days.
- Your business is sensitive to disputes—consider other payment methods because some bank debit methods favor the customer during disputes.

## Payment experience

To initiate a bank debit, a customer enters their bank account details during checkout and gives you permission to debit the account. This permission is called a mandate. View a sample mandate.

![Flow chart of the three step process the customer experiences. First, they select bank debit at checkout. Next the customer provides banking details and authorizes mandate. Finally, the customer gets notification that the payment is complete.](https://b.stripecdn.com/docs-statics-srv/assets/payment_flow.e4fcc05342cae882b39c41b497e5a24d.svg)

To reduce fraud with some bank debits, verify the bank account before the payment by confirming microdeposits or bank login. Verifying bank login can improve the user experience because customers pay by logging into their bank rather than entering bank account details.

## Product support

You can use a single integration for all bank debits that works across Stripe products. With Stripe Checkout, Payment Element, and Payment Links, you can enable bank debits right from the Dashboard with no integration work.

Payment methodCustomer countryPaymentIntentsCheckoutInvoicingConnectSubscriptionsPayment ElementPayment LinksMobile Payment Element[ACH Direct Debit](/payments/ach-debit)US[Bacs Direct Debit](/payments/payment-methods/bacs-debit)UK[BECS Debit](/payments/au-becs-debit)AU[Pre-authorized debit in Canada](/payments/acss-debit)CA1[SEPA Direct Debit](/payments/sepa-debit)EU1 Subscription mode isn’t supported.

Contact us to request a new bank debit method.

## Migrating from the Sources, Tokens, or Charges APIs

If your current bank debit integration uses the Sources, Tokens, or Bank Accounts API, we recommend following the appropriate migration guide to transition to Payment Intents API:

- [ACH migration guide](/payments/ach-debit/migrations)
- For all other bank debit payment methods, follow the general[migration guide](/payments/payment-intents/migration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`