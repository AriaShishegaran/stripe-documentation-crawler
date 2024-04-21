htmlSet a Stripe API version | Stripe Documentation[Skip to content](#main-content)Set an API version[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Flibraries%2Fset-version)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Flibraries%2Fset-version)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)
[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[SDKs](/docs/libraries)# Set a Stripe API version

Follow these guidelines to make sure that API versions match throughout your Stripe integration.Your account has a default API version, which defines how you call the API, what functionality you have access to and what you’re guaranteed to get back as part of the response. Webhook event objects are based on your default API version, which might be different from the API version used by the SDK. To make sure these versions match, we recommend registering a webhook endpoint with the same API version used as the SDK. To find your version, see View your default API version.

## Versioning basics

We’ve covered a few fundamental concepts you need to know about API versions used in SDKs. Choose your SDK language to get started.

RubyPythonPHPJavaNodeGo.NET### Setting the API version

The stripe-ruby library allows you to set the API version globally or on a per-request basis. If you don’t set an API version, recent versions of stripe-ruby use the API version that was latest at the time your version of stripe-ruby was released. Versions of stripe-ruby before v9 use your account’s default API version.

To set the API version globally with the SDK, assign the version to the Stripe.api_version property:

`require 'stripe'
Stripe.api_key = sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz
Stripe.api_version = '2024-04-10'`Or set the version per-request:

`require 'stripe'
intent = Stripe::PaymentIntent.retrieve(
  'pi_1DlIVK2eZvKYlo2CW4yj5l2C',
  {
    stripe_version: '2024-04-10',
  }
)
intent.capture`NoteWhen you override the version globally or per-request, the API response objects are also returned in that version.

### Updating your API version

Before updating your API version, carefully review the following resources:

- [Stripe API changelog](/upgrades#api-versions)
- [Upgrading your API version](/upgrades#how-can-i-upgrade-my-api)

You can upgrade your account’s default API version in the Developers Dashboard. Update your code to use the latest version of the Ruby SDK and set the new API version when making your calls.

## See also

Stripe SDKs follow their own versioning policy. See the link below to learn more.

- [Stripe versioning and support policies](/libraries/versioning)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Versioning basics](#versioning-basics)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`