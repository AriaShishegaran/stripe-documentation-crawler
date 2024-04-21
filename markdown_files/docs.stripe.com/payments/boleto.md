htmlBoleto payments | Stripe Documentation[Skip to content](#main-content)Boleto[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fboleto)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fboleto)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Vouchers](/docs/payments/vouchers)# Boleto payments

Learn how to accept payments with Boleto.Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil.

To complete a transaction, customers receive a voucher stating the amount to pay for services or goods. Customers then pay the boleto before its expiration date in one of several different methods, including at authorized agencies or banks, ATMs, or online bank portals. You will receive payment confirmation after 1 business day, while funds will be available for payout 2 business days after payment confirmation.

Payment method propertiesSupported countries- Customer locations

Brazil


- Payment method family

Cash-based payment method


- Connect support

Yes


- Presentment currency

BRL


- Recurring Payments

Yes


- Dispute support

No


- Payment confirmation

Customer-initiated


- Payout timing

2 business days


- Refunds/ Partial refunds

No/no



## Payment flow

![](https://b.stripecdn.com/docs-statics-srv/assets/checkout.4af16ecfd4f0a3f4044c56d6100c4a42.svg)

1. Selects Boleto at checkout

![](https://b.stripecdn.com/docs-statics-srv/assets/voucher.23c9ddface4b2e061575d0ef9470ef8e.svg)

2. Receives payment codes and a confirmation number

![](https://b.stripecdn.com/docs-statics-srv/assets/bank_portal.cd5d369eb435691133edeb668c8bf557.svg)

3. Makes a payment at banks or online bank portals.

![](https://b.stripecdn.com/docs-statics-srv/assets/success.1ee3b6d34d944693e654e84f6d1be9f3.svg)

4. Receives notification that payment is complete

## Get started

You don’t actually have to integrate Boleto and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Boleto from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)
- [Subscriptions](/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to manually configure Boleto as a payment.

Check out the Boleto sample on GitHub.

## Disputed payments

Generally Boleto payments cannot be disputed by the customer. However, in rare instances irregularities similar in nature to disputes (by the bank) may arise (for example, due to mishandling). Stripe will need to reach out to you in such cases and ask for your cooperation.

## Refunds

Boleto payments cannot be refunded. You will need to create a separate process to credit customers who require a refund.

## Amount limits

The amount for a single Boleto must be at least R$5.00 and no more than R$49,999.99.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)[Amount limits](#amount-limits)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`