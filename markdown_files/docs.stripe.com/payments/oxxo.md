htmlOXXO payments | Stripe Documentation[Skip to content](#main-content)OXXO[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Foxxo)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Foxxo)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Vouchers](/docs/payments/vouchers)# OXXO payments

Learn how to accept payments with OXXO.OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash.

To complete a transaction, customers receive a voucher that includes a reference number for the transaction. Customers then bring their voucher to an OXXO store to make a cash payment. You will receive payment confirmation by the next business day along with the settled funds.

Payment method propertiesCountry availability- Customer locations

Mexico


- Presentment currency

MXN


- Payment confirmation

Customer-initiated


- Payment method family

Cash-based payment method


- Recurring payments

No


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Dispute support

No


- Refunds / Partial refunds

No / no



## Payment flow

![](https://b.stripecdn.com/docs-statics-srv/assets/checkout.4af16ecfd4f0a3f4044c56d6100c4a42.svg)

Step 1. Selects OXXO at checkout

![](https://b.stripecdn.com/docs-statics-srv/assets/voucher.192ad10df702bb52ef9601e679d1a670.svg)

Step 2. Receives voucher with transaction reference

![](https://b.stripecdn.com/docs-statics-srv/assets/store.6026ce09a3857d0c5e532b8723c3e371.svg)

Step 3. Provides voucher and cash payment at OXXO store

![](https://b.stripecdn.com/docs-statics-srv/assets/success.1ee3b6d34d944693e654e84f6d1be9f3.svg)

Step 4. Receives notification that payment is complete

## Get started

You don’t actually have to integrate OXXO and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

Payment Links also supports adding OXXO from the Dashboard.

If your integration requires manually listing payment methods, learn how to manually configure OXXO as a payment.

Check out the OXXO sample on GitHub.

## Disputed payments

OXXO payments have a low risk of fraud or unrecognized payments because the customer must provide cash payment in person at an OXXO convenience store. Customers can’t dispute OXXO payments.

## Refunds

OXXO payments can’t be refunded. Some merchants have created a separate process to credit their customers who reach out directly.

## Amount limits

The amount for a single OXXO must be at least 10.00 MXN and no more than 10,000.00 MXN.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)[Amount limits](#amount-limits)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`