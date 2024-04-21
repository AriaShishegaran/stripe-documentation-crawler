# Getting started with Sources in the Android SDKDeprecated

We deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate them to the Payment Methods API](/payments/payment-methods/transitioning)

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

[PaymentMethods API](/api/payment_methods)

As of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

[Strong Customer Authentication](/strong-customer-authentication)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[accept a payment](/payments/accept-a-payment)

This guide assumes you’ve already installed and configured the Stripe Android SDK and are familiar with Sources.

[installed and configured](/payments/accept-a-payment-charges?platform=android)

Creating a payment using Sources with the Android SDK is a multi-step process:

[Sources](/sources)

- Create a Source object that represents your customer’s payment method.

[Create a Source object](#create-source-object)

- Check if further action is required from your customer.

[Check if further action is required](#check-if-further-action-is-required)

If no further action is required:

- Confirm the source is ready to use.

- Create a charge request on your backend using the source.

If further action is required:

- Present the user with any information they may need to authorize the charge.

- On your backend, listen to Stripe webhooks to create a charge with the source.

[webhooks](/webhooks)

- In your app, display the appropriate confirmation to your customer based on the source’s status.

[Create a Source object](#create-source-object)

## Create a Source object

See the Android SDK reference that documents every method and property of the classes described here.

[Android SDK reference](https://stripe.dev/stripe-android)

To create a Source object, use the appropriate creation method for your Source type.

- SourceParams#createBancontactParams()

[SourceParams#createBancontactParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-bancontact-params.html)

- SourceParams#createCardParams()

[SourceParams#createCardParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-card-params.html)

- SourceParams#createGiropayParams()

[SourceParams#createGiropayParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-giropay-params.html)

- SourceParams#createIdealParams()

[SourceParams#createIdealParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-ideal-params.html)

- SourceParams#createP24Params()

[SourceParams#createP24Params()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-p24-params.html)

- SourceParams#createSepaDebitParams()

[SourceParams#createSepaDebitParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sepa-debit-params.html)

- SourceParams#createSofortParams()

[SourceParams#createSofortParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sofort-params.html)

- SourceParams#createThreeDSecureParams()

[SourceParams#createThreeDSecureParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-three-d-secure-params.html)

Each method requires parameters unique to the payment type. Refer to the appropriate payment methods documentation to find out what these are.

[payment methods](/sources#supported-payment-methods)

Once you have a SourceParams object, create a source with either the Stripe#createSource() or Stripe#createSourceSynchronous(), depending on whether you prefer to manage threading yourself.

[SourceParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/index.html)

[Stripe#createSource()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-source.html)

[Stripe#createSourceSynchronous()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/create-source-synchronous.html)

Do not call Stripe#createSourceSynchronous() on the UI thread as this will crash. All methods labeled “Synchronous” are blocking and meant to be performed on a separate thread. Similarly, you must call createSource on the UI thread, as Android’s AsyncTask must be launched from the main thread.

[Check if further action is required from your customer](#check-if-further-action-is-required)

## Check if further action is required from your customer

Some payment methods require your customer to complete a certain action before the source can be used in a charge request. For instance, customers using giropay must be redirected to their online banking service to authorize the payment.

[giropay](/sources/giropay)

[redirected](#redirecting-your-customer)

For sources that require redirecting your customer, you must specify a return URL when creating the source. This redirect URL should be unique and used consistently for your application. Do not use the same redirect URL in other applications, as it can result in a payment attempt that opens the wrong application after the redirect.

If you would like to accept card payments that are verified with 3D Secure, your integration should use the Payment Intents API instead of sources. Refer to the Payment Methods API documentation to determine if the specific payment methods you wish to use are supported.

[3D Secure](/payments/3d-secure)

[Payment Intents API](/payments/payment-intents)

[Payment Methods API documentation](/payments/payment-methods)

## Redirect your customer to authorize a source

For sources that require your customer to complete an action (for example, verify using 3D Secure), redirect the customer out of your application to complete this step.

Once the customer has completed the required action, they are redirected to the URL that was provided when creating the source.

When declaring your activity that creates redirect-based sources, list an intent-filter item in your AndroidManifest.xml file. This allows you to accept links into your application. Your activity must include android:launchMode="singleTask" or else a new copy of it is opened when your customer comes back from the browser.

To receive information from this event, listen for your activity getting started back up with a new Intent using the onNewIntent lifecycle method.

If you’d like more help, check out the example app on Github that demonstrates creating a payment using several different payment methods.

[example app](https://github.com/stripe/stripe-android/tree/master/example)

## See also

- Using Payment Intents on Android

[Using Payment Intents on Android](/payments/accept-a-payment?integration=elements)

- Supported payment methods

[Supported payment methods](/sources)
