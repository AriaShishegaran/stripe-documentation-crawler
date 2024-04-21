htmlSofort payments | Stripe Documentation[Skip to content](#main-content)Sofort[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsofort)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsofort)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)# Sofort payments

Learn about Sofort, a common payment method in Europe.WarningOur financial partners are in the process of deprecating Sofort. New businesses can’t accept Sofort payments. For more information read our support page.

Stripe users in Europe and the United States can use the Payment Intents API—a single integration path for creating payments using any supported method—to accept Sofort payments from customers in the following countries:

- Austria
- Belgium
- Germany
- Netherlands
- Spain

Sofort is a single use, delayed notification payment method that requires customers to authenticate their payment. It redirects them to their bank’s portal to authenticate the payment, and it typically takes 2 to 14 days to receive notification of success or failure.

CautionYour use of Sofort must comply with our Sofort Terms of Service.

Payment method propertiesCountry availability- Customer locations

Europe


- Presentment currency

EUR


- Payment confirmation

Customer-initiated


- Payment method family

Bank debit


- Recurring payments

via SEPA Direct Debit


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Refunds / Partial refunds

Yes / yes


- Dispute support

No



## Payment flow

This demo shows the customer experience when using Sofort.

## Get started

You don’t actually have to integrate Sofort and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Sofort from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)

If you prefer to manually list payment methods or want to save Sofort details for future payments, see the following guides:

- [Manually configure Sofort as a payment](/payments/sofort/accept-a-payment)
- [Save Sofort details for future payments](/payments/sofort/set-up-payment)

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Sofort payments can be refunded up to 180 days after the original payment.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`