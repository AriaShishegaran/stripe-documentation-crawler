htmlRefund transactions | Stripe Documentation[Skip to content](#main-content)Refund transactions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Frefunds)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Frefunds)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Refund transactions

Cancel or refund Stripe Terminal payments.Stripe Terminal supports both automatic and manual capture.

When the SDK returns a confirmed PaymentIntent to your app, the payment is authorized but not captured. You can cancel payments that are authorized and not captured. If the PaymentIntent has already been captured, you must refund the underlying charge created by the PaymentIntent, using the refunds API or Dashboard.

We recommend reconciling payments on your backend after a day’s activity to prevent unintended authorizations and uncollected funds.

## Availability

Canceling payments is available on Visa, Mastercard, American Express and Discover. For single-message payment methods like Interac and eftpos, PaymentIntents are automatically captured. In lieu of canceling PaymentIntents, make sure your application can allow initiating a refund at the end of the checkout flow.

Online refunds are available on all card networks except for Interac.

In-person refunds are only available on Interac.

## Cancel payments Client-sideServer-side

### SDK reference

- [cancelPaymentIntent (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)cancelPaymentIntent:completion:)
- [cancelPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/cancel-payment-intent.html)
- [cancelPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#cancelPaymentIntent)

You can cancel a card_present PaymentIntent at any time before it has been captured. Canceling a PaymentIntent releases all uncaptured funds, and a canceled PaymentIntent can no longer be used to perform charges.

This can be useful if, for example, your customer decides to use a different payment method or pay with cash after the payment has been processed. In your application’s UI, consider allowing the user to cancel after confirming the payment, before finalizing the payment and notifying your backend to capture.

Client-side

Cancel a PaymentIntent from your client using the iOS, Android, or React Native SDK:

Server-drivenJavaScriptiOSAndroidReact NativeNoteClient-side PaymentIntent cancellation is possible with the iOS, Android, or React Native SDKs. If you’re using server-driven integration, cancel the PaymentIntent server-side.

Server-side

### API Reference

- [Cancel a PaymentIntent](/api/payment_intents/cancel)

The JavaScript SDK and server-driven integration require you to cancel the PaymentIntent on your server. For iOS, Android, or React Native, you can cancel the PaymentIntent on your server if the information required to start a payment isn’t readily available in your app.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/payment_intents/pi_ANipwO3zNfjeWODtRPIg/cancel \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`## Perform refunds Client-sideServer-side

When you use a PaymentIntent to collect payment from a customer, Stripe creates a charge behind the scenes. To refund the customer’s payment after the PaymentIntent has succeeded, create a refund by passing in the PaymentIntent ID or the charge ID. You can also optionally refund part of a payment by specifying an amount.

You can perform refunds with the API or through the Dashboard. For Interac transactions in Canada, the BBPOS WisePOS E reader and Stripe Reader S700 support in-person refunds instead.

Stripe Reader S700Get notified when Stripe Reader S700 is available in your country.

Online refunds don’t require a cardholder to present their card again at the point of sale.  The following example shows how to create a full refund by passing in the PaymentIntent ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d payment_intent=pi_Aabcxyz01aDfoo`To refund part of a PaymentIntent, provide an amount parameter, as an integer in cents (or the charge currency’s smallest currency unit):

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d payment_intent=pi_Aabcxyz01aDfoo \
  -d amount=1000`## See also

- [Cart display](/terminal/features/display)
- [Receipts](/terminal/features/receipts)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Availability](#availability)[Cancel payments](#canceling-payments)[Perform refunds](#refunds)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`