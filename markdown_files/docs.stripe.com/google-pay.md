htmlGoogle Pay | Stripe Documentation[Skip to content](#main-content)Google Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fgoogle-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fgoogle-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)# Google Pay

Learn how to accept payments using Google Pay.NoteAs of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Google Pay fully supports SCA as it already handles payment flows with a built-in layer of authentication (biometric or password).

Learn more about SCA and how it might impact your business.

### Google Pay terms

By integrating Google Pay, you agree to Google’s terms of service.

Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer’s Google account.

Google Pay is fully compatible with Stripe’s products and features (for example, recurring payments), allowing you to use it in place of a traditional payment form whenever possible. Use it to accept payments for physical goods, donations, subscriptions, and so on.

## Using Stripe and Google Pay versus the Google Play billing system

For sales of physical goods and services, your app can accept Google Pay or any other Stripe-supported payment method. Those payments are processed through Stripe, and you only need to pay Stripe’s processing fees. However, in-app purchases of digital products and content must use the Google Play billing system. Those payments are processed by Google and are subject to their transaction fees.

For more information about which purchases must use the Google Play billing system, see Google Play’s developer terms.

AndroidReact NativeWeb## Accept a payment using Google Pay in your Android app

GooglePayLauncher, part of the Stripe Android SDK, is the fastest and easiest way to start accepting Google Pay in your Android apps.

[Prerequisites](#html-js-prerequisites)To support Google Pay in Android, you need the following:

- A`minSdkVersion`of`19`or higher.
- A`compileSdkVersion`of`28`or higher.

Additionally, if you wish to test with your own device, you need to add a payment method to your Google Account.

[Set up your integration](#setup)To use Google Pay, first enable the Google Pay API by adding the following to the <application> tag of your AndroidManifest.xml:

AndroidManifest.xml`<application>
  ...
  <meta-data
    android:name="com.google.android.gms.wallet.api.enabled"
    android:value="true" />
</application>`This guide assumes you’re using the latest version of the Stripe Android SDK.

build.gradle[Groovy](#)`dependencies {
    implementation 'com.stripe:stripe-android:20.41.0'
}`For more details, see Google Pay’s Set up Google Pay API for Android.

[Instantiate GooglePayLauncher](#instantiate)Next, create an instance of GooglePayLauncher in your Activity or Fragment. This must be done in Activity#onCreate().

GooglePayLauncher.Config exposes both required and optional properties that configure GooglePayLauncher. See GooglePayLauncher.Config for more details on the configuration options.

[Kotlin](#)`class CheckoutActivity : AppCompatActivity() {
    // fetch client_secret from backend
    private lateinit var clientSecret: String

    private lateinit var googlePayButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.checkout_activity)

        PaymentConfiguration.init(this, PUBLISHABLE_KEY)

        googlePayButton = findViewById<Button>(R.id.google_pay_button)

        val googlePayLauncher = GooglePayLauncher(
            activity = this,
            config = GooglePayLauncher.Config(
                environment = GooglePayEnvironment.Test,
                merchantCountryCode = "US",
                merchantName = "Widget Store"
            ),
            readyCallback = ::onGooglePayReady,
            resultCallback = ::onGooglePayResult
        )

        googlePayButton.setOnClickListener {
            // launch `GooglePayLauncher` to confirm a Payment Intent
            googlePayLauncher.presentForPaymentIntent(clientSecret)
        }
    }

    private fun onGooglePayReady(isReady: Boolean) {
        // implemented below
    }

    private fun onGooglePayResult(result: GooglePayLauncher.Result) {
        // implemented below
    }
}`After instantiating GooglePayLauncher, the GooglePayLauncher.ReadyCallback instance is called with a flag indicating whether Google Pay is available and ready to use. This flag can be used to update your UI to indicate to your customer that Google Pay is ready to be used.

[Kotlin](#)`class CheckoutActivity : AppCompatActivity() {
    // continued from above

    private lateinit var googlePayButton: Button

    private fun onGooglePayReady(isReady: Boolean) {
        googlePayButton.isEnabled = isReady
    }
}`[Launch GooglePayLauncher](#launch-google-pay)After Google Pay is available and your app has obtained a PaymentIntent or SetupIntent client secret, launch GooglePayLauncher using the appropriate method. When confirming a PaymentIntent, use GooglePayLauncher#presentForPaymentIntent(clientSecret). When confirming a SetupIntent, use GooglePayLauncher#presentForSetupIntent(clientSecret).

[Kotlin](#)`class CheckoutActivity : AppCompatActivity() {
    // fetch client_secret from backend
    private lateinit var clientSecret: String

    private lateinit var googlePayButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // instantiate `googlePayLauncher`

        googlePayButton.setOnClickListener {
            // launch `GooglePayLauncher` to confirm a Payment Intent
            googlePayLauncher.presentForPaymentIntent(clientSecret)
        }
    }
}`[Handle the result](#handle-result)Finally, implement GooglePayLauncher.ResultCallback to handle the result of the GooglePayLauncher operation.

The result can be GooglePayLauncher.Result.Completed, GooglePayLauncher.Result.Canceled, or GooglePayLauncher.Result.Failed.

[Kotlin](#)`class CheckoutActivity : AppCompatActivity() {
    // continued from above

    private fun onGooglePayResult(result: GooglePayLauncher.Result) {
        when (result) {
            GooglePayLauncher.Result.Completed -> {
                // Payment succeeded, show a receipt view
            }
            GooglePayLauncher.Result.Canceled -> {
                // User canceled the operation
            }
            is GooglePayLauncher.Result.Failed -> {
                // Operation failed; inspect `result.error` for the exception
            }
        }
    }
}`[Going live with Google Pay](#going-live)Follow Google’s instructions to request production access for your app. Choose the integration type Gateway when prompted, and provide screenshots of your app for review.

After your app has been approved, test your integration in production by setting the environment to GooglePayEnvironment.Production, and launching Google Pay from a signed, release build of your app. Remember to use your live mode API keys. You can use a PaymentIntent with capture_method = manual to process a transaction without capturing the payment.

## Creating a PaymentMethod

If you confirm your payment on your server, you can use GooglePayPaymentMethodLauncher to only collect a PaymentMethod instead of confirm payment.

[Kotlin](#)`class CheckoutActivity : AppCompatActivity() {
    private lateinit var googlePayButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.checkout_activity)

        PaymentConfiguration.init(this, PUBLISHABLE_KEY)

        googlePayButton = findViewById<Button>(R.id.google_pay_button)

        val googlePayLauncher = GooglePayPaymentMethodLauncher(
            activity = this,
            config = GooglePayPaymentMethodLauncher.Config(
                environment = GooglePayEnvironment.Test,
                merchantCountryCode = "FR",
                merchantName = "Widget Store"
            ),
            readyCallback = ::onGooglePayReady,
            resultCallback = ::onGooglePayResult
        )

        googlePayButton.setOnClickListener {
            googlePayLauncher.present(
                currencyCode = "EUR",
                amount = 2500
            )
        }
    }

    private fun onGooglePayReady(isReady: Boolean) {
        googlePayButton.isEnabled = isReady
    }

    private fun onGooglePayResult(
        result: GooglePayPaymentMethodLauncher.Result
    ) {
        when (result) {
            is GooglePayPaymentMethodLauncher.Result.Completed -> {
                // Payment details successfully captured.
                // Send the paymentMethodId to your server to finalize payment.
                val paymentMethodId = result.paymentMethod.id
            }
            GooglePayPaymentMethodLauncher.Result.Canceled -> {
                // User canceled the operation
            }
            is GooglePayPaymentMethodLauncher.Result.Failed -> {
                // Operation failed; inspect `result.error` for the exception
            }
        }
    }
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Using Stripe and Google Pay versus the Google Play billing system](#using-stripe-and-google-pay-versus-the-google-play-billing-system)[Accept a payment using Google Pay in your Android app](#native)[Prerequisites](#html-js-prerequisites)[Set up your integration](#setup)[Instantiate GooglePayLauncher](#instantiate)[Launch GooglePayLauncher](#launch-google-pay)[Handle the result](#handle-result)[Going live with Google Pay](#going-live)[Creating a PaymentMethod](#creating-a-paymentmethod)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`