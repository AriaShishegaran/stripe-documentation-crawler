htmlMigrating to Stripe iOS SDK 23 | Stripe Documentation[Skip to content](#main-content)Migrate to iOS SDK 23[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fmobile%2Fios%2Fsdk-23-migration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fmobile%2Fios%2Fsdk-23-migration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)
[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[SDKs](/docs/libraries)# Migrating to Stripe iOS SDK 23

Migrate your Swift and Objective-C apps to our modular Swift SDK.The Stripe iOS SDK is now a set of Swift modules, enabling smaller app bundles and better support for Swift APIs.

This move required changes to our public interface. Xcode will offer suggestions to automatically update most of your code, but you’ll also need to make a few changes yourself.

From SDK 20From SDK 21From SDK 22SwiftObjective-C### Requirements

The SDK now requires Xcode 13.2.1 or later. The minimum deployment target is iOS 13.

### PaymentSheet

To use PaymentSheet, you must explicitly import the StripePaymentSheet module.

BeforeAfter`import Stripe``import StripePaymentSheet`### Modules

The SDK is now split into separate modules. You can reduce your app’s bundle size by including only the modules you need.

ModuleFeaturesCompressed sizeStripePaymentSheetStripe’s[prebuilt payment UI](/payments/accept-a-payment?platform=ios&mobile-ui=payment-element).2.7MBStripeContains all the below frameworks, plus[Issuing](/issuing/cards/digital-wallets?platform=ios)and[Basic Integration](/mobile/ios/basic).2.2MBStripePaymentsBindings for the Stripe Payments API.1.1MBStripePaymentsUIBindings for the Stripe Payments API,[STPPaymentCardTextField](/payments/accept-a-payment?platform=ios&mobile-ui=card-element), STPCardFormView, and other UI elements.1.7MBStripeApplePay[Apple Pay support](/apple-pay), including`STPApplePayContext`.0.4MB### Module installation

Swift Package ManagerCocoapodsCarthageAdd the selected module (e.g. “StripePaymentSheet”) to the target of your app.

### Card field

SDK 23 replaces STPPaymentCardTextField’s .cardParams parameter with .paymentMethodParams, making it easier to collect the customer’s postal code.

In most situations, you can now pass the cardTextField.paymentMethodParams directly to the Stripe API.

BeforeAfter`var cardTextField: STPPaymentCardTextField
// Collect card details
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
let cardParams = cardTextField.cardParams
let paymentMethodParams = STPPaymentMethodParams(card: cardParams, billingDetails: nil, metadata: nil)
paymentIntentParams.paymentMethodParams = paymentMethodParams``var cardTextField: STPPaymentCardTextField
// Collect card details
let paymentIntentParams = STPPaymentIntentParams(clientSecret: paymentIntentClientSecret)
paymentIntentParams.paymentMethodParams = cardTextField.paymentMethodParams`Advanced card field usage![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To access the STPPaymentMethodCardParams directly, use .paymentMethodParams.card.

BeforeAfter`var cardTextField: STPPaymentCardTextField
let cardParams = cardTextField.cardParams``var cardTextField: STPPaymentCardTextField
// STPPaymentCardTextField will never return a nil .card
let cardParams = cardTextField.paymentMethodParams.card!`cardTextField.paymentMethodParams returns a copy. Never set cardTextField.paymentMethodParams.card directly. If you need to set the card information, set cardTextField.paymentMethodParams to a new instance of STPPaymentMethodParams.

BeforeAfter`var cardTextField: STPPaymentCardTextField
cardTextField.cardParams = myCardParams``var cardTextField: STPPaymentCardTextField
let paymentMethodParams = STPPaymentMethodParams(card: myCardParams, billingDetails: nil, metadata: nil)
cardTextField.paymentMethodParams = paymentMethodParams`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`