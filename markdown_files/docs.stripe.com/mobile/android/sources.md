htmlGetting started with Sources in the Android SDK | Stripe Documentation[Skip to content](#main-content)Android[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fmobile%2Fandroid%2Fsources)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fmobile%2Fandroid%2Fsources)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Sources](/docs/sources)# Getting started with Sources in the Android SDKDeprecated

Learn how to use Sources in your Android application.WarningWe deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

CautionAs of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

This guide assumes you’ve already installed and configured the Stripe Android SDK and are familiar with Sources.

Creating a payment using Sources with the Android SDK is a multi-step process:

1. [Create a Source object](#create-source-object)that represents your customer’s payment method.
2. [Check if further action is required](#check-if-further-action-is-required)from your customer.

If no further action is required:

1. Confirmthe source is ready to use.
2. Create a charge request on your backend using the source.

If further action is required:

1. Present the user with any information they may need to authorize the charge.
2. On your backend, listen to Stripe[webhooks](/webhooks)to create a charge with the source.
3. In your app, display the appropriate confirmation to your customer based on the source’s status.

[Create a Source object](#create-source-object)### SDK reference

See the Android SDK reference that documents every method and property of the classes described here.

To create a Source object, use the appropriate creation method for your Source type.

- [SourceParams#createBancontactParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-bancontact-params.html)
- [SourceParams#createCardParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-card-params.html)
- [SourceParams#createGiropayParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-giropay-params.html)
- [SourceParams#createIdealParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-ideal-params.html)
- [SourceParams#createP24Params()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-p24-params.html)
- [SourceParams#createSepaDebitParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sepa-debit-params.html)
- [SourceParams#createSofortParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-sofort-params.html)
- [SourceParams#createThreeDSecureParams()](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-source-params/-companion/create-three-d-secure-params.html)

[Java](#)`final Stripe stripe = new Stripe(getContext(),
    "pk_test_VOOyyYjgzqdm8I3SrBqmh9qY");
Card card = cardInputWidget.getCard();
SourceParams cardSourceParams = SourceParams.createCardParams(card);
// The asynchronous way to do it. Call this method on the main thread.
stripe.createSource(
    cardSourceParams,
    new ApiResultCallback<Source>() {
        @Override
        public void onSuccess(@NonNull Source source) {
            // Store the source somewhere, use it, etc
        }
        @Override
        public void onError(@NonNull Exception error) {
            // Tell the user that something went wrong
        }
    });

// The synchronous way to do it (DON'T DO BOTH)
Source source = stripe.createSourceSynchronous(cardSourceParams);`Each method requires parameters unique to the payment type. Refer to the appropriate payment methods documentation to find out what these are.

Once you have a SourceParams object, create a source with either the Stripe#createSource() or Stripe#createSourceSynchronous(), depending on whether you prefer to manage threading yourself.

WarningDo not call Stripe#createSourceSynchronous() on the UI thread as this will crash. All methods labeled “Synchronous” are blocking and meant to be performed on a separate thread. Similarly, you must call createSource on the UI thread, as Android’s AsyncTask must be launched from the main thread.

[Check if further action is required from your customer](#check-if-further-action-is-required)Some payment methods require your customer to complete a certain action before the source can be used in a charge request. For instance, customers using giropay must be redirected to their online banking service to authorize the payment.

[Java](#)`SourceParams giropayParams = SourceParams.createGiropayParams(
        100,
        "Customer Name",
        "yourapp://post-authentication-return-url",
        "a purchase description");
// Note: this is a synchronous method -- you should not run it on the UI thread
Source giropaySource = stripe.createSourceSynchronous(giropayParams);
if (Source.REDIRECT.equals(giropaySource.getFlow())) {
    String redirectUrl = giropaySource.getRedirect().getUrl();
    // then go to this URL, as shown below.
}`For sources that require redirecting your customer, you must specify a return URL when creating the source. This redirect URL should be unique and used consistently for your application. Do not use the same redirect URL in other applications, as it can result in a payment attempt that opens the wrong application after the redirect.

NoteIf you would like to accept card payments that are verified with 3D Secure, your integration should use the Payment Intents API instead of sources. Refer to the Payment Methods API documentation to determine if the specific payment methods you wish to use are supported.

## Redirect your customer to authorize a source

For sources that require your customer to complete an action (for example, verify using 3D Secure), redirect the customer out of your application to complete this step.

[Java](#)`String externalUrl = mThreeDSource.getRedirect().getUrl();
// We suggest popping up a dialog asking the user
// to tap to go to their browser so they are not
// surprised when they leave your application.
Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(externalUrl));
startActivity(browserIntent);`Once the customer has completed the required action, they are redirected to the URL that was provided when creating the source.

When declaring your activity that creates redirect-based sources, list an intent-filter item in your AndroidManifest.xml file. This allows you to accept links into your application. Your activity must include android:launchMode="singleTask" or else a new copy of it is opened when your customer comes back from the browser.

`<activity
    android:name=".activity.PollingActivity"
    android:launchMode="singleTask"
    android:theme="@style/SampleTheme">
    <intent-filter>
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
        <data
            android:scheme="yourapp"
            android:host="post-authentication-return-url"/>
    </intent-filter>
</activity>`To receive information from this event, listen for your activity getting started back up with a new Intent using the onNewIntent lifecycle method.

[Java](#)`@Override
protected void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    if (intent.getData() != null && intent.getData().getQuery() != null) {
        // The client secret and source ID found here is identical to
        // that of the source used to get the redirect URL.

        String host = intent.getData().getHost();
        // Note: you don't have to get the client secret
        // and source ID here. They are the same as the
        // values already in your source.
        String clientSecret = intent.getData().getQueryParameter(QUERY_CLIENT_SECRET);
        String sourceId = intent.getData().getQueryParameter(QUERY_SOURCE_ID);
        if (clientSecret != null
                && sourceId != null
                && clientSecret.equals(redirectSource.getClientSecret())
                && sourceId.equals(redirectSource.getId())) {
            // Then this is a redirect back for the original source.
            // You should poll your own backend to update based on
            // source status change webhook events it may receive, and display the results
            // of that here.
        }
        // If you had a dialog open when your user went elsewhere, remember to close it here.
        mRedirectDialogController.dismissDialog();
    }
}`If you’d like more help, check out the example app on Github that demonstrates creating a payment using several different payment methods.

## See also

- [Using Payment Intents on Android](/payments/accept-a-payment?integration=elements)
- [Supported payment methods](/sources)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a Source object](#create-source-object)[Check if further action is required from your customer](#check-if-further-action-is-required)[Redirect your customer to authorize a source](#redirect-your-customer)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`