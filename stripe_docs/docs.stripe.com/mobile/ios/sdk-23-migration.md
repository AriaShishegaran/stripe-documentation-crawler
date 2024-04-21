# Migrating to Stripe iOS SDK 23

The Stripe iOS SDK is now a set of Swift modules, enabling smaller app bundles and better support for Swift APIs.

[Stripe iOS SDK](https://github.com/stripe/stripe-ios)

This move required changes to our public interface. Xcode will offer suggestions to automatically update most of your code, but you’ll also need to make a few changes yourself.

The SDK now requires Xcode 13.2.1 or later. The minimum deployment target is iOS 13.

To use PaymentSheet, you must explicitly import the StripePaymentSheet module.

The SDK is now split into separate modules. You can reduce your app’s bundle size by including only the modules you need.

[prebuilt payment UI](/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)

[Issuing](/issuing/cards/digital-wallets?platform=ios)

[Basic Integration](/mobile/ios/basic)

[STPPaymentCardTextField](/payments/accept-a-payment?platform=ios&mobile-ui=card-element)

[Apple Pay support](/apple-pay)

Add the selected module (e.g. “StripePaymentSheet”) to the target of your app.

[target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)

SDK 23 replaces STPPaymentCardTextField’s .cardParams parameter with .paymentMethodParams, making it easier to collect the customer’s postal code.

In most situations, you can now pass the cardTextField.paymentMethodParams directly to the Stripe API.

To access the STPPaymentMethodCardParams directly, use .paymentMethodParams.card.

cardTextField.paymentMethodParams returns a copy. Never set cardTextField.paymentMethodParams.card directly. If you need to set the card information, set cardTextField.paymentMethodParams to a new instance of STPPaymentMethodParams.
