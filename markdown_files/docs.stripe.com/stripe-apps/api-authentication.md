htmlAPI authentication methods | Stripe Documentation[Skip to content](#main-content)API authentication methods[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fapi-authentication)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fapi-authentication)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# API authentication methods

Select the API authentication method that works best for your app's use case.Your app can use one of three methods to authenticate requests to the Stripe API on behalf of your users.

MethodDescriptionUse cases[Platform key](/stripe-apps/build-backend#using-stripe-apis)DefaultYour account’s secret API key makes requests to the Stripe API on behalf of your user’s account.- You want to manage fewer keys per install.
- BetaYou want to distribute your app through Connect platforms.

[OAuth 2.0](/stripe-apps/api-authentication/oauth)Use industry standard OAuth 2.0 to generate access tokens to interact with the Stripe API. Initialize the Stripe SDK with the access token for the account you’re operating on behalf of.- You already use OAuth to interact with other systems.
- Users need to manage the integration from your software.

[Restricted API key](/stripe-apps/api-authentication/rak)When a user installs your app, Stripe generates a permissioned, restricted API key that users need to copy and paste into your software to interact with Stripe.- Your software can’t support platform or OAuth onboarding.
- Your users run your software on-premise.

## Configure

To configure the API authentication method, edit stripe_api_access_type in the app manifest. For setup instructions, refer to the pages linked in the table above.

stripe-app.json`{
  "id": "com.example.app",
  "version": "0.0.1",
  "name": "Your Stripe App",
  "distribution_type": "public",
  "permissions": [],
  "stripe_api_access_type": "platform" | "oauth" | "restricted_api_key",
}`## See also

- [Set up OAuth 2.0](/stripe-apps/api-authentication/oauth)
- [Set up restricted access key authentication](/stripe-apps/api-authentication/rak)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`