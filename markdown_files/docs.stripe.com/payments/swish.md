htmlSwish payments | Stripe Documentation[Skip to content](#main-content)Swish[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fswish)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fswish)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Real-time payments](/docs/payments/real-time)# Swish payments

Learn about Swish, a popular payment method in Sweden.Swish is a single-use payment method used in Sweden. It allows customers to authenticate and approve payments using the Swish mobile app and the Swedish BankID mobile app.

You get immediate notification on whether the payment succeeded or failed.

Payment method propertiesCountry availability- Customer locations

Sweden


- Presentment currency

SEK


- Payment confirmation

Customer-initiated


- Payment method family

Real-time payments


- Recurring payments

No


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Refunds/Partial refunds

Yes/yes


- Dispute support

No



## Payment flows

MobileDesktop![The customer follows a mobile redirect flow to pay with Swish.](https://b.stripecdn.com/docs-statics-srv/assets/swish-docs-mobile.25c41dc77ede2f9e54f2c7cf769b9645.png)

The customer follows a mobile redirect flow to pay with Swish.

Customers pay with Swish by using one of the following methods:

- Mobile: Customers follow a mobile redirect from your website or mobile app to the Swish app, where they authorize the payment, then return to your website or mobile app.


- Desktop: Customers scan a QR code you present on your website using the Swish app, which allows them to authorize the payment.



## Get started

Learn how to manually configure Swish as a payment method.

You don’t actually have to integrate Swish and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Swish from the Dashboard:

- [Payment Links](/payment-links)

## Merchant of record

For Swish payments, Stripe operates as the merchant of record. Therefore, Stripe’s name appears as the recipient of payments in the Swish app and as the statement descriptor in the customer’s bank statements. Your business name appears in the message field in the Swish app.

## Prohibited business categories

In addition to the industry and business categories listed in Prohibited and Restricted Businesses, the following categories aren’t allowed to use Swish:

- Precious stones and metals, watches and jewelry
- Digital wallet top-ups

## Refunds

You can refund Swish charges up to 365 days after the payment completes. Refunds usually take a few minutes to complete. Swish supports full and partial refunds. You can also issue multiple partial refunds up to the amount of the original charge.

## Swish with Connect

You can use Stripe Connect with Swish to process payments on behalf of a connected account. Connect users can use Swish with the following charge types:

Charge types- [Direct](/connect/direct-charges)
- [Destination](/connect/destination-charges)
- [Separate charges and transfers](/connect/separate-charges-and-transfers)

### Enable Swish for connected accounts that use the Stripe Dashboard

Connected accounts that use the Stripe dashboard can enable Swish in their Payment methods settings in the Dashboard. To check which accounts have enabled Swish, use the capabilities hash in our accounts webhooks or APIs to see if the swish_payments capability is set to active.

### Enable Swish for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

Follow the instructions to enable payment methods for your connected accounts. The name of your connected account is the name customers see during checkout and in the Swish app.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flows](#payment-flows)[Get started](#get-started)[Merchant of record](#merchant-of-record)[Prohibited business categories](#prohibited-business-categories)[Refunds](#refunds)[Swish with Connect](#connect)Products Used[Payments](/payments)[Connect](/connect)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`