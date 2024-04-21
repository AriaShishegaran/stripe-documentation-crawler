htmlBLIK payments | Stripe Documentation[Skip to content](#main-content)BLIK[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fblik)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fblik)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)# BLIK payments

Learn about BLIK, a common payment method in Poland.BLIK is a single use payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

Payment method propertiesCountry availability- Customer locations

Poland


- Presentment currency

PLN


- Payment confirmation

Customer-initiated


- Payment method family

Authenticated bank debit


- Recurring payments

No


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Refunds / Partial refunds

Yes / yes


- Dispute support

Yes



## Payment flow

![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_1.7e386c77d6410d13caf823130b7ec68a.svg)

Customer selects BLIK at checkout.

![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_2.5caa9f807d50579710cc01b361a2d0fc.svg)

Customer is directed to their mobile banking app to generate a 6-digit code.

![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_3.8e52c5c894b439baae7bec85b96b71b2.svg)

Customer puts the code into the checkout.

![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_4.a93b15c949981d6a0b61463ff201fc53.svg)

Customer is notified that payment is complete.

## Get started

You don’t actually have to integrate BLIK and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

If you prefer to manually list payment methods, learn how to manually configure BLIK as a payment.

## Disputed payments

BLIK has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API`charge.dispute.created`event (if your integration is set up to receive[webhooks](/webhooks))

Stripe holds back the disputed amount from your balance until BLIK resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchase you have already refunded)

To handle disputes programmatically, respond to disputes using the API.

This information helps BLIK determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If BLIK resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If BLIK rules in favor of the customer, the balance charge becomes permanent.

## Refunds

BLIK supports full and partial refunds. Depending on the bank, refunds are processed immediately or within a couple of hours.

## Connect

If you use Connect, you must consider the following before you enable and use BLIK.

### Request BLIK capabilities for your connected accounts

Set the blik_payments capability to active on your platform account, and on any connected accounts you want to enable BLIK for. You can also request more account capabilities.

### Merchant of record and statement descriptors

The charge type of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

Charge typeDescriptor taken fromDirectConnected AccountDestinationPlatformSeparate charge and transferPlatformDestination (with`on_behalf_of`)Connected AccountSeparate charge and transfer (with`on_behalf_of`)Connected AccountWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)[Connect](#connect)Products Used[Payments](/payments)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`