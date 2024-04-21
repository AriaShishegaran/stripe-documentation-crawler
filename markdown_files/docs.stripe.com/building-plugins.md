htmlLegacy plugins | Stripe Documentation[Skip to content](#main-content)Legacy plugins[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbuilding-plugins)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbuilding-plugins)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Migrate or build a plugin](/docs/stripe-apps/onboarding-plugin)# Legacy pluginsDeprecated

Develop and integrate your own connector following these best practices.DeprecatedYou can no longer request API keys from users. Stripe Apps is the new method for authenticating users and includes support for OAuth 2.0.

View the migration docs

NoteBecome a Stripe Partner to reach businesses on Stripe who are looking to add capabilities to their platforms.

Follow these best practices to make sure your users can safely process on Stripe’s platform without disruption as our API evolves. If you have questions along the way, reach out to plugins@stripe.com.

- Register your plugin by creating a Stripe account or using an existing one
- [Identify your plugin](#identify-plugin)using`setAppInfo`and`registerAppInfo`so we can alert you to any potential issues we notice
- Set[Stripe’s API version](#set-api-version)in your plugin to avoid potentially breaking changes for your users
- Use[client-side tokenization](#tokenization)to securely collect payment details in the browser

You can also take a few steps to improve the quality of your connector:

- Add the[Express Checkout Element](#express-checkout-element)to offer multiple one-click payment buttons to your customers, including[Apple Pay](/apple-pay),[Google Pay](/google-pay),[Link](/payments/link), and[PayPal](/payments/paypal)
- Enable[multiple payment methods](#apms)beyond credit cards to support international users
- Verify your users[have HTTPS enabled](#https)to improve their security
- Subscribe to our[mailing list](#subscribe)to keep up to speed with changes to Stripe’s API

## Identifying your plugin

Provide identifying information so that we can contact you if there’s an issue with your connector or critical update to the API.

### Backend API calls

If you use the APIs to create server-side requests, use setAppInfo with a hash containing the following options:

- `name`(required): your plugin’s name
- `partner_id`(required for[Stripe Verified Partners](https://stripe.com/partner-program), optional otherwise): your Partner ID from the[Partners](https://dashboard.stripe.com/partners/settings)section of the Dashboard
- `version`(optional): your plugin’s version
- `url`(optional): the URL for your plugin’s website with your contact details

[Ruby](#)`Stripe.set_app_info(
  'MyStripePlugin',
  partner_id: '{{PARTNER_ID}}', # Used by Stripe to identify your connector
  version: '1.2.34',
  url: 'https://example.com'
)`CautionIf your connector is designed for a particular platform, include that platform in the name field (for example, WordPress MyStripePlugin or WooCommerce MyStripePlugin).

If you’re building a connector and not using one of our official libraries, set the value of the User-Agent header on requests made to the Stripe API as name/version (url).

The following is an example:

`User-Agent: WordPress MyStripePlugin/1.2.34 (https://example.com)`### Client side / Stripe.js

For frontend libraries that use Stripe.js, use registerAppInfo with the same options as setAppInfo above. For example, using JavaScript:

`stripe.registerAppInfo({
  name: "MyOSSLibrary",
  partner_id: '{{PARTNER_ID}}',   // Used by Stripe to identify your connector
  version: "1.2.34",
  url: "https://example.com",
});`## Setting the API version

Your plugin should use the setApiVersion function, which will set the Stripe-Version HTTP header on all requests. Your users will use their own API keys to access Stripe, but this header will be included with every request. We recommend that you use the most recently published version of the API. The current API version and details on our versioning policy can be found in the API reference.

[Ruby](#)`Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'
Stripe.api_version = '2022-08-01'`New Stripe users automatically default to the latest version of the API. This header ensures that your connector is pinned to a specific API version, which keeps the occasional backwards-incompatible change from breaking your connector’s functionality.

Users can upgrade their own API version through the Stripe Dashboard. If your connector relies on webhook events, their data format and structure depend on the user’s account API version. You should instruct your users to set the version in their Dashboard to match your plugin.

CautionAPI versions can’t be downgraded. You should regularly release new versions of your connector to correctly handle any changes to JSON responses.

## Subscribing to our mailing list for updates

We regularly release new versions of the Stripe API that bring new features and bug fixes. You can subscribe to the api-announce mailing list to be notified of updates that may affect users of your connector.

## Securely collecting payment details

Stripe users are subject to PCI compliance, which specifies how credit card data should be securely stored, processed, and transmitted. Their businesses could face stiff penalties for noncompliance or potential breaches, so it’s important to help them safely process on Stripe.

Since your connector will make API calls on behalf of a Stripe user, you must transmit credit card data securely using client-side tokenization. Customers submit their personal information through their web browser or mobile app directly to Stripe, and in exchange a simple token will be sent to the Stripe user. This allows your users to securely collect card details without sensitive data ever touching their server.

If your connector includes a client-side payment form in the browser, we recommend that you use either Stripe.js and Elements or Checkout:

- Elements provides prebuilt UI components and complete control over the look and feel of payment forms
- Checkout provides a complete checkout experience and can be quickly added to a Stripe user’s website

Both of these options provide client-side tokenization.

If your plugin only operates in a backend environment, please include a note in your connector’s documentation asking users to tokenize payment details using Elements or Checkout. Tokenization helps Stripe users process as safely as possible on our platform.

## Add the Express Checkout Element

The Express Checkout Element gives you a single integration for accepting payments through one-click payment buttons, including Apple Pay, Google Pay, Link, or PayPal.

The Express Checkout Element allows you to display multiple buttons at the same time. Customers see different payment buttons depending on what their device and browser combination supports.

## Enabling multiple payment methods

Stripe supports multiple payment methods, aside from credit cards. We’ve published a guide to payment methods that introduces terminology, key considerations, and how we support each method on our platform.

The Payment Methods API enables your users to collect payments using additional payment methods (for example, Alipay, iDEAL, Sofort). You can add these payment methods using one integration path.

## Verifying that HTTPS is enabled

If your plugin presents a payment form in a web browser, it should check if the form is being served over HTTPS. We require our users to enable HTTPS: you should present a clear error to your user if they’re not properly secured.

Here are a few examples to verify whether your users have HTTPS enabled:

[Ruby](#)`# This example uses Sinatra, but the `request` object is provided by Rack
require 'sinatra'

get '/' do
  if !request.https?
    # Present an error to the user
  end
  # ...
end`If your connector has a front-end component, check whether HTTPS is being used from the browser. For example, using JavaScript:

`// This example checks for HTTPS from the browser
if (window.location.protocol !== "https:") {
  // Present an error to the user
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Identifying your plugin](#identify-plugin)[Setting the API version](#set-api-version)[Subscribing to our mailing list for updates](#subscribe)[Securely collecting payment details](#tokenization)[Add the Express Checkout Element](#express-checkout-element)[Enabling multiple payment methods](#apms)[Verifying that HTTPS is enabled](#https)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`