# Google Pay

As of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Google Pay fully supports SCA as it already handles payment flows with a built-in layer of authentication (biometric or password).

[Strong Customer Authentication](/strong-customer-authentication)

Learn more about SCA and how it might impact your business.

[Learn more about SCA and how it might impact your business](/strong-customer-authentication)

By integrating Google Pay, you agree to Google’s terms of service.

[terms of service](https://payments.developers.google.com/terms/sellertos)

Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer’s Google account.

Google Pay is fully compatible with Stripe’s products and features (for example, recurring payments), allowing you to use it in place of a traditional payment form whenever possible. Use it to accept payments for physical goods, donations, subscriptions, and so on.

[subscriptions](/billing/subscriptions/creating)

## Using Stripe and Google Pay versus the Google Play billing system

For sales of physical goods and services, your app can accept Google Pay or any other Stripe-supported payment method. Those payments are processed through Stripe, and you only need to pay Stripe’s processing fees. However, in-app purchases of digital products and content must use the Google Play billing system. Those payments are processed by Google and are subject to their transaction fees.

[processing fees](https://stripe.com/pricing)

[Google Play billing system](https://developer.android.com/google/play/billing)

For more information about which purchases must use the Google Play billing system, see Google Play’s developer terms.

[developer terms](https://support.google.com/googleplay/android-developer/answer/10281818)

## Accept a payment using Google Pay in your Android app

GooglePayLauncher, part of the Stripe Android SDK, is the fastest and easiest way to start accepting Google Pay in your Android apps.

[Prerequisites](#html-js-prerequisites)

## Prerequisites

To support Google Pay in Android, you need the following:

- A minSdkVersion of 19 or higher.

- A compileSdkVersion of 28 or higher.

Additionally, if you wish to test with your own device, you need to add a payment method to your Google Account.

[add a payment method to your Google Account](https://support.google.com/wallet/answer/12058983?visit_id=637947092743186187-653786796&rd=1)

[Set up your integration](#setup)

## Set up your integration

To use Google Pay, first enable the Google Pay API by adding the following to the <application> tag of your AndroidManifest.xml:

This guide assumes you’re using the latest version of the Stripe Android SDK.

For more details, see Google Pay’s Set up Google Pay API for Android.

[Set up Google Pay API](https://developers.google.com/pay/api/android/guides/setup)

[Instantiate GooglePayLauncher](#instantiate)

## Instantiate GooglePayLauncher

Next, create an instance of GooglePayLauncher in your Activity or Fragment. This must be done in Activity#onCreate().

[GooglePayLauncher](https://github.com/stripe/stripe-android/blob/master/payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt)

GooglePayLauncher.Config exposes both required and optional properties that configure GooglePayLauncher. See GooglePayLauncher.Config for more details on the configuration options.

After instantiating GooglePayLauncher, the GooglePayLauncher.ReadyCallback instance is called with a flag indicating whether Google Pay is available and ready to use. This flag can be used to update your UI to indicate to your customer that Google Pay is ready to be used.

[Launch GooglePayLauncher](#launch-google-pay)

## Launch GooglePayLauncher

After Google Pay is available and your app has obtained a PaymentIntent or SetupIntent client secret, launch GooglePayLauncher using the appropriate method. When confirming a PaymentIntent, use GooglePayLauncher#presentForPaymentIntent(clientSecret). When confirming a SetupIntent, use GooglePayLauncher#presentForSetupIntent(clientSecret).

[Handle the result](#handle-result)

## Handle the result

Finally, implement GooglePayLauncher.ResultCallback to handle the result of the GooglePayLauncher operation.

The result can be GooglePayLauncher.Result.Completed, GooglePayLauncher.Result.Canceled, or GooglePayLauncher.Result.Failed.

[Going live with Google Pay](#going-live)

## Going live with Google Pay

Follow Google’s instructions to request production access for your app. Choose the integration type Gateway when prompted, and provide screenshots of your app for review.

[Google’s instructions](https://developers.google.com/pay/api/android/guides/test-and-deploy/request-prod-access)

After your app has been approved, test your integration in production by setting the environment to GooglePayEnvironment.Production, and launching Google Pay from a signed, release build of your app. Remember to use your live mode API keys. You can use a PaymentIntent with capture_method = manual to process a transaction without capturing the payment.

[API keys](/keys)

[capture_method = manual](/api/payment_intents/create#create_payment_intent-capture_method)

## Creating a PaymentMethod

If you confirm your payment on your server, you can use GooglePayPaymentMethodLauncher to only collect a PaymentMethod instead of confirm payment.
