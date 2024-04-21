# iOS basic integrationDeprecated

We created an improved payments UI for mobile apps with features such as additional payment methods and SwiftUI support. We recommend using it for your integration instead of this one.

[payments UI](/payments/accept-a-payment?platform=ios)

If you want to migrate but are unable to, please let us know.

[let us know](https://github.com/stripe/stripe-ios/issues)

Use this integration if you want a prebuilt UI that:

- Accepts credit cards and Apple Pay

- Saves and displays cards for reuse

- Supports limited customization of fonts and colors

[limited customization](#theming)

- Displays full-screen view controllers to collect payment details, shipping address, and shipping method:

STPPaymentOptionsViewController

[STPPaymentOptionsViewController](https://stripe.dev/stripe-ios/docs/Classes/STPPaymentOptionsViewController.html)

STPAddCardViewController

[STPAddCardViewController](https://stripe.dev/stripe-ios/docs/Classes/STPAddCardViewController.html)

STPShippingAddressViewController

[STPShippingAddressViewController](https://stripe.dev/stripe-ios/docs/Classes/STPShippingAddressViewController.html)

These view controllers are also available to use individually—see the steps below for more details. This integration requires both server and client-side steps to implement.

Check out the example Basic Integration app and backend for a full implementation of this guide.

[Basic Integration app](https://github.com/stripe/stripe-ios/tree/master/Example)

[backend](https://github.com/stripe/example-mobile-backend/blob/master/web.rb)

[Set up StripeClient-sideServer-side](#setup-ios)

## Set up StripeClient-sideServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

The Stripe iOS SDK is open source, fully documented, and compatible with apps supporting iOS 13 or above.

[Stripe iOS SDK](https://github.com/stripe/stripe-ios)

[fully documented](https://stripe.dev/stripe-ios/index.html)

To install the SDK, follow these steps:

- In Xcode, select File > Add Packages… and enter https://github.com/stripe/stripe-ios-spm as the repository URL.

- Select the latest version number from our releases page.

[releases page](https://github.com/stripe/stripe-ios/releases)

- Add the Stripe product to the target of your app.

[target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app)

For details on the latest SDK release and past versions, see the Releases page on GitHub. To receive notifications when a new release is published, watch releases for the repository.

[Releases](https://github.com/stripe/stripe-ios/releases)

[watch releases for the repository](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository)

Configure the SDK with your Stripe publishable key on app start. This enables your app to make requests to the Stripe API.

[publishable key](https://dashboard.stripe.com/test/apikeys)

Use your test mode keys while you test and develop, and your live mode keys when you publish your app.

[test mode](/keys#obtain-api-keys)

[live mode](/keys#test-live-modes)

[Set up an ephemeral keyClient-sideServer-side](#ephemeral-key)

## Set up an ephemeral keyClient-sideServer-side

In order for the SDK to save and retrieve credit cards for later use, create a single Stripe Customer object for each of your users. When you create a new user or account on your server, create a corresponding Customer object at the same time, even if you don’t collect payment information from your users when they sign up. This ensures that your application has a matching Customer for each user.

[Customer](/api/customers)

For security, the Customer API is not directly accessible from the client. Instead, your server provides the SDK with an ephemeral key—a short-lived API key with restricted access to the Customer API. You can think of an ephemeral key as a session, authorizing the SDK to retrieve and update a specific Customer object for the duration of the session.

To provide an ephemeral key to the SDK, you’ll need to expose a new API endpoint on your backend. This endpoint should create an ephemeral key for the current Stripe customer, and return the key’s unmodified response as JSON. When the SDK requests an ephemeral key, it will specify the version of the Stripe API that it expects the response to come from. Your endpoint must accept an api_version parameter, and use the specified API version when creating the ephemeral key. This ensures that the SDK always receives the correct ephemeral key response from your backend. Consult our Example Backend to see this in practice.

[Example Backend](https://github.com/stripe/example-mobile-backend/blob/9ac448f8b5d49175d26c7b77fd6bd3c88703e838/web.rb#L25-L40)

In your app, conform to the STPCustomerEphemeralKeyProvider protocol by implementing its createCustomerKeyWithAPIVersion method. This method requests an ephemeral key from the endpoint you created on the backend.

[STPCustomerEphemeralKeyProvider](https://stripe.dev/stripe-ios/docs/Protocols/STPCustomerEphemeralKeyProvider.html)

[createCustomerKeyWithAPIVersion](https://stripe.dev/stripe-ios/docs/Protocols/STPCustomerEphemeralKeyProvider.html#/c:objc(pl)STPCustomerEphemeralKeyProvider(im)createCustomerKeyWithAPIVersion:completion:)

When implementing this method, be sure to pass the apiVersion parameter along to your ephemeral keys endpoint. Consult the API client in our example app to see this in practice.

[API client](https://github.com/stripe/stripe-ios/tree/master/Example/Basic%20Integration/Basic%20Integration/MyAPIClient.swift)

[View full sample](https://github.com/stripe/stripe-ios/blob/21.4.0/Example/Basic%20Integration/Basic%20Integration/MyAPIClient.swift#L77-L101)

[Set up an STPCustomerContextClient-side](#set-up-customer-context)

## Set up an STPCustomerContextClient-side

Next, initialize an STPCustomerContext with the STPCustomerEphemeralKeyProvider you created in the previous step.

[STPCustomerContext](http://stripe.dev/stripe-ios/docs/Classes/STPCustomerContext.html)

A CustomerSession talks to your backend to retrieve an ephemeral key for your Customer with its STPCustomerEphemeralKeyProvider, and uses that key to manage retrieving and updating the Customer’s payment methods on your behalf.

To reduce load times, preload your customer’s information by initializing STPCustomerContext before they enter your payment flow.

If your current user logs out of the app and a new user logs in, create a new instance of STPCustomerContext or clear the cached customer using the provided clearCachedCustomer method. On your backend, create and return a new ephemeral key for the Customer object associated with the new user.

[clearCachedCustomer](https://stripe.dev/stripe-ios/docs/Classes/STPCustomerContext.html#/c:objc(cs)STPCustomerContext(im)clearCache)

[Set up an STPPaymentContextClient-side](#initialize-payment-context)

## Set up an STPPaymentContextClient-side

Once you’ve set up your customer context, you can use it to initialize STPPaymentContext, the core class of the integration. Conform a class to STPPaymentContextDelegate and assign it to the payment context’s delegate and hostViewController properties. We recommend using your app’s checkout screen UIViewController. In the next steps, you will implement the STPPaymentContext delegate methods.

[STPPaymentContext](https://stripe.dev/stripe-ios/docs/Classes/STPPaymentContext.html)

[STPPaymentContextDelegate](https://stripe.dev/stripe-ios/docs/Protocols/STPPaymentContextDelegate.html)

You should also set the payment context’s paymentAmount property, which will be displayed to your user in the Apple Pay dialog (you can change this later, if the amount of the user’s purchase changes).

[Handle the user's payment methodClient-side](#handle-payment-method)

## Handle the user's payment methodClient-side

In your checkout screen, add a button to let the customer enter or change their payment method. When tapped, use STPPaymentContext to push or present an STPPaymentOptionsViewController on the payment context’s hostViewController.

[STPPaymentOptionsViewController](https://stripe.dev/stripe-ios/docs/Classes/STPPaymentOptionsViewController.html)

STPPaymentOptionsViewController

[STPPaymentOptionsViewController](https://stripe.dev/stripe-ios/docs/Classes/STPPaymentOptionsViewController.html)

STPAddCardViewController

[STPAddCardViewController](https://stripe.dev/stripe-ios/docs/Classes/STPAddCardViewController.html)

STPPaymentOptionsViewController uses STPCustomerContext to display a Customer’s payment methods. If there are no stored payment methods or the Add New Card button is tapped, STPAddCardViewController is displayed. You can also initialize and display these view controllers without using STPPaymentContext.

This STPPaymentContext delegate method triggers when the content of the payment context changes, like when the user selects a new payment method or enters shipping information. This is a good place to update your UI:

[STPPaymentContext delegate method](https://stripe.dev/stripe-ios/docs/Protocols/STPPaymentContextDelegate.html#/c:objc(pl)STPPaymentContextDelegate(im)paymentContextDidChange:)

[Handle the user's shipping infoClient-side](#handle-shipping-info)

## Handle the user's shipping infoClient-side

If your user needs to enter or change their shipping address and shipping method, STPPaymentContext can do this for you automatically. STPPaymentContext will save shipping info to the Stripe customer when your user updates their information, and automatically prefill the shipping view controller for future purchases. Note that you should not rely on the shipping information stored on the Stripe customer for order fulfillment, as your user may change this information if they make multiple purchases. We recommend adding shipping information when you create a PaymentIntent object (which can also help prevent fraud), or when saving it to your own database. When presenting the shipping view controller, you can specify whether you’d like it presented modally, or pushed onto a UINavigationController stack:

[PaymentIntent](/api/payment_intents/create#create_payment_intent-shipping)

This sets up and presents an STPShippingAddressViewController on the payment context’s hostViewController. Once the user enters a valid shipping address, they’re taken to an STPShippingMethodsViewController. After they select a shipping method, both view controllers are dismissed or popped off the hostViewController’s stack.

[STPShippingAddressViewController](http://stripe.dev/stripe-ios/docs/Classes/STPShippingAddressViewController.html)

[STPShippingMethodsViewController](http://stripe.dev/stripe-ios/docs/Classes/STPShippingMethodsViewController.html)

STPShippingAddressViewController

[STPShippingAddressViewController](https://stripe.dev/stripe-ios/docs/Classes/STPShippingAddressViewController.html)

STPShippingMethodsViewController

[STPShippingMethodsViewController](https://stripe.dev/stripe-ios/docs/Classes/STPShippingMethodsViewController.html)

This method is called after your user enters a shipping address. Validate the returned address and determine the shipping methods available for that address.

If the address is valid, call the provided completion block with a status of STPShippingStatusValid, nil for the error argument, an array of shipping methods, and a selected shipping method. If you don’t need to collect a shipping method, pass nil for the shipping methods and selected shipping method. If the address is invalid, call the completion block with a status of STPShippingStatusInvalid, an error object describing the issue with the address, and nil for the shipping methods and selected shipping method. Note that providing an error object is optional—if you omit it, the user sees an alert with the message “Invalid Shipping Address.”

[Submit the paymentClient-sideServer-side](#submit-payment)

## Submit the paymentClient-sideServer-side

When your user is ready to pay (for example, they tap the Buy button) call requestPayment on your payment context. It displays any required UI (such as the Apple Pay dialog) and calls the appropriate methods on its delegate as your user finishes their payment.

This method is called when the customer has successfully selected a payment method. Submit the payment to Stripe using a Payment Intent. Stripe uses this payment object to track and handle all the states of the payment until the payment completes.

[Payment Intent](/payments/payment-intents)

On your server, make an endpoint that creates a PaymentIntent with an amount and currency and returns its client secret to your client.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

On the client, implement this delegate method to:

- Request a PaymentIntent from your server.

- Assemble a STPPaymentIntentParams object with the PaymentIntent client secret from your server and the paymentMethod provided by the delegate method.

[STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html)

[paymentMethod](https://stripe.dev/stripe-ios/docs/Classes/STPPaymentResult.html#/c:objc(cs)STPPaymentResult(py)paymentMethod)

- Call the STPPaymentHandler confirmPayment method to confirm the payment, passing the STPPaymentContext as the authenticationContext.

[STPPaymentHandler confirmPayment](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:)

[confirm](/api/payment_intents/confirm)

[authenticationContext](https://stripe.dev/stripe-ios/stripe-payments/Protocols/STPAuthenticationContext.html)

You must call the provided completion block with the appropriate STPPaymentStatus (.success, .error, or .userCancellation) when the customer’s payment is finished.

This method is called after the previous method, when any auxiliary UI that has been displayed (such as the Apple Pay dialog) has been dismissed. You should inspect the returned status and show an appropriate message to your user. For example:

This method is called in the rare case that the payment context’s initial loading call fails, usually due to lack of internet connectivity. You should dismiss your checkout page when this occurs and invite the user to try again. You can also optionally attempt to try again by calling retryLoading on the payment context.

[Test the integration](#test)

## Test the integration

​​Several test cards are available for you to use in test mode to make sure this integration is ready. Use them with any CVC and an expiration date in the future.

For the full list of test cards see our guide on testing.

[testing](/testing)

[OptionalHandle post-payment events](#fulfillment)

## OptionalHandle post-payment events

[OptionalSet up Apple PayClient-side](#set-up-apple-pay)

## OptionalSet up Apple PayClient-side

[OptionalCustomize the UIClient-side](#theming)

## OptionalCustomize the UIClient-side

## See also

- After the payment

[After the payment](/payments/after-the-payment)

- The Payment Intents API

[The Payment Intents API](/payments/payment-intents)

- Stripe iOS SDK Reference

[Stripe iOS SDK Reference](https://stripe.dev/stripe-ios/)
