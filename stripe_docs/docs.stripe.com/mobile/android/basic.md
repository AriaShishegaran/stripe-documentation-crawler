# Android basic integrationDeprecated

We created an improved payments UI for mobile apps with support for additional payment methods. We recommend using it for your integration instead of this one.

[payments UI](/payments/accept-a-payment?platform=android)

If you want to migrate but are unable to, please let us know.

[let us know](https://github.com/stripe/stripe-android/issues)

Use this integration if you want a prebuilt UI that:

- Accepts credit cards and other payment methods

- Saves and displays cards for reuse

- Can be customized to fit your app’s look and feel using an Android theme

[customized to fit your app’s look and feel](#customize-ui)

- Launches full-screen activities to collect payment details, shipping address, and shipping method

- Allows your customer to choose Google Pay as a payment method

PaymentMethodsActivity

[PaymentMethodsActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-methods-activity/index.html)

AddPaymentMethodActivity

[AddPaymentMethodActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-add-payment-method-activity/index.html)

PaymentFlowActivity

[PaymentFlowActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-flow-activity/index.html)

These activities can also be used individually. This integration requires both server and client-side steps to implement.

[can also be used individually](#use-individual-activities)

Check out the example Basic Integration app and backend for a full implementation of this guide.

[Basic Integration app](https://github.com/stripe-samples/sample-store-android)

[backend](https://github.com/stripe/example-mobile-backend/blob/master/web.rb)

[Set up StripeClient-sideServer-side](#setup)

## Set up StripeClient-sideServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

The Stripe Android SDK is open source and fully documented.

[Stripe Android SDK](https://github.com/stripe/stripe-android)

[fully documented](https://stripe.dev/stripe-android/)

To install the SDK, add stripe-android to the dependencies block of your app/build.gradle file:

[app/build.gradle](https://developer.android.com/studio/build/dependencies)

For details on the latest SDK release and past versions, see the Releases page on GitHub. To receive notifications when a new release is published, watch releases for the repository.

[Releases](https://github.com/stripe/stripe-android/releases)

[watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository)

Configure the SDK with your Stripe publishable key so that it can make requests to the Stripe API, such as in your Application subclass:

[publishable key](https://dashboard.stripe.com/apikeys)

Use your test mode keys while you test and develop, and your live mode keys when you publish your app.

[test mode](/keys#obtain-api-keys)

[live mode](/keys#test-live-modes)

[Set up an ephemeral keyClient-sideServer-side](#set-up-ephemeral-key)

## Set up an ephemeral keyClient-sideServer-side

In order for the SDK to save and retrieve credit cards for later use, create a single Stripe Customer object for each of your users. When you create a new user or account on your server, create a corresponding Customer object at the same time, even if you don’t collect payment information from your users when they sign up. This ensures that your application has a matching Customer for each user.

[Customer](/api/customers)

For security, the Customer API is not directly accessible from the client. Instead, your server provides the SDK with an ephemeral key—a short-lived API key with restricted access to the Customer API. You can think of an ephemeral key as a session, authorizing the SDK to retrieve and update a specific Customer object s for the duration of the session.

To provide an ephemeral key to the SDK, expose a new API endpoint on your backend. This endpoint should create an ephemeral key for the current Stripe customer, and return the key’s unmodified response as JSON. When the SDK requests an ephemeral key, it will specify the version of the Stripe API that it expects the response to come from. Your endpoint must accept an api_version parameter, and use the specified API version when creating the ephemeral key. This ensures that the SDK always receives the correct ephemeral key response from your backend. Consult our Example Backend to see this in practice.

[Example Backend](https://github.com/stripe/example-mobile-backend/blob/9ac448f8b5d49175d26c7b77fd6bd3c88703e838/web.rb#L25-L40)

After you’ve added an ephemeral key endpoint to your backend, you’ll need a way for your Android app to communicate with this endpoint. In your app, make your API client class implement the EphemeralKeyProvider interface, which defines a single method, createEphemeralKey(). When implementing this method, pass the apiVersion parameter along to your ephemeral keys endpoint. Consult our Example App to see this in practice.

[EphemeralKeyProvider](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-ephemeral-key-provider/index.html)

[createEphemeralKey()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-ephemeral-key-provider/create-ephemeral-key.html)

[Example App](https://github.com/stripe/stripe-android/blob/master/example/src/main/java/com/stripe/example/service/ExampleEphemeralKeyProvider.kt)

[Set up a CustomerSessionClient-side](#set-up-customer-session)

## Set up a CustomerSessionClient-side

After creating an EphemeralKeyProvider, initialize a CustomerSession. A CustomerSession talks to your backend to retrieve an ephemeral key for your Customer with its EphemeralKeyProvider, and uses that key to manage retrieving and updating the Customer’s payment methods on your behalf.

[CustomerSession](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/index.html)

You can also use CustomerSession with your own custom UI to retrieve or refresh the Customer, and list their payment methods, attach a payment method, or detach a payment method.

[retrieve](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/retrieve-current-customer.html)

[refresh](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/update-current-customer.html)

[list](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/get-payment-methods.html)

[attach](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/attach-payment-method.html)

[detach](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-customer-session/detach-payment-method.html)

To reduce load times, preload your customer’s information by initializing CustomerSession before they enter your payment flow.

If your current user logs out of the app, clear the current CustomerSession singleton by calling CustomerSession.endCustomerSession(). When a new user logs in, re-initialize the instance. On your backend, create and return a new ephemeral key for the Customer object associated with the new user.

[Set up a PaymentSessionClient-side](#set-up-payment-session)

## Set up a PaymentSessionClient-side

The core of this integration is the PaymentSession class. It uses CustomerSession to launch full-screen activities to collect and store payment information, and can also be used to collect shipping info. Think of it as the data source for your checkout activity—it handles asynchronously retrieving the data you need, and notifies its PaymentSessionListener when your UI should change.

[PaymentSession](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/index.html)

To work with PaymentSession, you’ll need to:

- Create a PaymentSessionConfig object

- Implement a PaymentSessionListener

The PaymentSessionConfig object is created using a Builder. All of the Builder’s fields are optional. See the API reference for details on each method.

[Builder](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session-config/-builder/index.html)

[API reference](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session-config/-builder/index.html)

After creating the PaymentSessionConfig, you’ll need to implement PaymentSessionListener.

This method should also check for whether or not the payment data is complete, according to the PaymentSessionConfig specified. If you receive an update for which PaymentSessionData#isPaymentReadyToCharge() returns true, you can immediately send a message to your server to complete the charge.

This method is called whenever the network communication state has changed. We recommend showing a spinner or infinite progress bar when it is set to true

This method is called whenever an error occurs when connecting to the Stripe API. Make sure users can see the error messages, so display them in an alert dialog.

Having created your PaymentSessionConfig and PaymentSessionListener, you can now initialize the PaymentSession. In the below example, we use anonymous classes to create our listener and config for simplicity.

[initialize](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/init.html)

[Collect the customer's payment and shipping detailsClient-side](#collect-details)

## Collect the customer's payment and shipping detailsClient-side

Once the PaymentSession has been initialized, you can use it to make the following calls.

PaymentMethodsActivity

[PaymentMethodsActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-methods-activity/index.html)

AddPaymentMethodActivity

[AddPaymentMethodActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-add-payment-method-activity/index.html)

This method starts the PaymentMethodsActivity to allow the customer to choose a saved payment method, using CustomerSession as its data source. If the Add new card button is tapped, or there are no existing payment methods, AddPaymentMethodActivity is launched to add a credit card.

PaymentFlowActivity

[PaymentFlowActivity](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-payment-flow-activity/index.html)

This method presents the PaymentFlowActivity to allow the user to enter shipping information, if such information is required according to your PaymentSessionConfig.

[Complete the paymentClient-sideServer-side](#complete-the-payment)

## Complete the paymentClient-sideServer-side

Once PaymentSession#isPaymentReadyToCharge() returns true, submit the payment to Stripe using a Payment Intent. Stripe uses this payment object to track and handle all the states of the payment—even when the bank requires customer intervention, like additional card authentication—until the payment completes.

[Payment Intent](/payments/payment-intents)

On your server, make an endpoint that creates a PaymentIntent with an amount and currency and returns its client secret to your client.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

- Request a PaymentIntent from your server

- Assemble a ConfirmPaymentIntentParams object with the PaymentIntent client secret from your server and the id of PaymentSessionData#paymentMethod obtained from PaymentSessionListenerImpl#onPaymentSessionDataChanged().

[ConfirmPaymentIntentParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirm-payment-intent-params/index.html)

- Call the Stripe confirmPayment method to confirm the payment.

[Stripe confirmPayment](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-payment.html)

When the payment completes, onSuccess is called and the value of the returned PaymentIntent’s status is Succeeded. Any other value indicates the payment was not successful. Inspect lastPaymentError to determine the cause. End the payment session by calling PaymentSession#onCompleted().

[lastPaymentError](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-payment-intent/index.html#com.stripe.android.model/PaymentIntent/lastPaymentError/#/PointingToDeclaration/)

[Manage PaymentSession in a host ActivityClient-side](#manage)

## Manage PaymentSession in a host ActivityClient-side

In order to get updates for the PaymentSessionData object and to handle state during Activity lifecycle, you’ll need to hook up your PaymentSession instance to a few key parts of your host Activity lifecycle. The first is in onActivityResult()

This is all you need to do to get updates from the various activities launched by PaymentSession. Any updates to the data are reported to the PaymentSessionListener argument to PaymentSession#init().

[PaymentSessionListener](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/-payment-session-listener/index.html)

[PaymentSession#init()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-session/init.html)

[Test the integration](#test)

## Test the integration

​​Several test cards are available for you to use in test mode to make sure this integration is ready. Use them with any CVC and an expiration date in the future.

For the full list of test cards see our guide on testing.

[testing](/testing)

[OptionalHandle post-payment events](#fulfillment)

## OptionalHandle post-payment events

[OptionalUse individual activitiesClient-side](#use-individual-activities)

## OptionalUse individual activitiesClient-side

[OptionalCustomize the UIClient-side](#customize-ui)

## OptionalCustomize the UIClient-side

## See also

- After the payment

[After the payment](/payments/after-the-payment)

- The Payment Intents API

[The Payment Intents API](/payments/payment-intents)

- Stripe Android SDK Reference

[Stripe Android SDK Reference](https://stripe.dev/stripe-android)
