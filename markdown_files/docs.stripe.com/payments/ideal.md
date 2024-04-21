htmliDEAL payments | Stripe Documentation[Skip to content](#main-content)iDEAL[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fideal)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fideal)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)# iDEAL payments

Learn about iDEAL, a common payment method in the Netherlands.iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%.

iDEAL redirects customers to their online banking environment to authenticate a payment using a second factor of authentication and there is immediate notification about the success or failure of a payment. The exact customer experience depends on their bank.

Payment method propertiesCountry availability- Customer locations

Netherlands


- Presentment currency

EUR


- Payment confirmation

Customer-initiated


- Payment method family

Authenticated bank debit


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

This demo shows the customer experience when using Ideal.

## Get started

You don’t actually have to integrate iDEAL and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding iDEAL from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)

If you prefer to manually list payment methods or want to save iDEAL details for future payments, see the following guides:

- [Manually configure iDEAL as a payment method](/payments/ideal/accept-a-payment)
- [Save iDEAL details for future payments](/payments/ideal/set-up-payment)

Check out the iDEAL sample on GitHub.

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

iDEAL payments can be refunded up to 180 days after the original payment.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)Products Used[Payments](/payments)[Invoicing](/invoicing)[Payment Links](/payments/payment-links)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`