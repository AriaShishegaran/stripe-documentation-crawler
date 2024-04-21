htmlLink in the Mobile Payment Element | Stripe Documentation[Skip to content](#main-content)Link with Mobile Elements[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fmobile-payment-element-link)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fmobile-payment-element-link)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)
Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[Faster checkout with Link](/docs/payments/link)# Link in the Mobile Payment Element

Add Link to your native iOS, Android, and React Native apps.Let your customer check out faster by using Link in the Mobile Payment Element. You can autofill information for any customer already using Link, regardless of whether they initially saved their information in Link with another business. The default Mobile Payment Element integration includes a Link prompt in the card form.

![Link in iOS](https://b.stripecdn.com/docs-statics-srv/assets/link-in-ios.de526c6199ff89fbaa7b1beb5e8bc3da.png)

Add Link to your iOS integration

## Enable Link

To offer Link in your mobile app:

1. [Integrate the Mobile Payment Element](/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)using the latest version of the Stripe Mobile SDK.
2. Enable Link in your[Payment Method settings](https://dashboard.stripe.com/settings/payment_methods).
3. Enable[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)by using the[latest version of the API](/upgrades)or by adding the[automatic_payment_methods](/api/payment_intents/object#payment_intent_object-automatic_payment_methods)parameter when creating your PaymentIntent.
4. (Optional)[Pass in your customer’s email address](#pass-email).

## Pass in a customer’s email address

Link authenticates a customer using their email address. We recommend prefilling as much information as possible to streamline the checkout process.

iOSAndroidReact NativeTo prefill the customer’s name, email address, and phone number, supply defaultBillingDetails with your customer information after initializing PaymentSheet.Configuration.

`var configuration = PaymentSheet.Configuration()
configuration.defaultBillingDetails.name = "Jenny Rosen"
configuration.defaultBillingDetails.email = "jenny.rosen@example.com"
configuration.defaultBillingDetails.phone = "888-888-8888"`## Test your integration

You can create test mode accounts for Link using any valid email address. When prompted for a one-time passcode, enter 000000.

## See also

- [Stripe Mobile SDKs](/libraries#stripe-mobile-sdks)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Enable Link](#enable-link)[Pass in a customer’s email address](#pass-email)[Test your integration](#test-your-integration)[See also](#see-also)Related Guides[Build an app that accepts payments with Link](/docs/payments/accept-a-payment?platform=ios&ui=payment-sheet)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`