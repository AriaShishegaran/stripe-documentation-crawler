htmlRestricted API key authentication | Stripe Documentation[Skip to content](#main-content)Restricted API key[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fapi-authentication%2Frak)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fapi-authentication%2Frak)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[API authentication methods](/docs/stripe-apps/api-authentication)# Restricted API key authentication

Generate a permissioned restricted API key (RAK) when a user installs your app.![Installing an app to generate a RAK](https://b.stripecdn.com/docs-statics-srv/assets/rak-user-journey.14fda11d13eaeb5cdbebbea71f277126.png)

### RAK user flow

A user authenticating with the RAK follows these steps.

1. On your site, the user clicks a link that redirects them to Stripe.
2. On Stripe, the user selects the appropriate account and accepts permissions for installing the app.
3. After the app is installed, it generates a restricted API key provisioned with the proper permissions.
4. The user copies the generated keys and provides them to your site.

[Develop your app](#develop-app)1. Create your app using our template.

Command Line`stripe apps create <app-name> --template restricted-api-key-app`If you have an existing app, run this command in Stripe CLI:

Command Line`stripe apps set api-access-type restricted_api_key`
2. Add all the permissions that your app requires.


3. Edit your app settings page. If you use the template above, a settings view is automatically created. We recommend adding instructions or links to your own documentation on this page for users to reference when setting up your app.

![The install link page showing app permissions](https://b.stripecdn.com/docs-statics-srv/assets/settingsview.ca0e43bcc311ea9819da61b2949e6ed1.png)

Example app settings page


4. Upload your app to Stripe.

NoteAfter you upload your RAK app, you can’t change the API authentication method.

Command Line`stripe apps upload`

[Test your app](#test-app)You can test the RAK authentication on your own account.

1. [Install your app in test mode](/stripe-apps/versions-and-releases#changing-between-versions)on your account.
2. Go to your[installed apps page](https://dashboard.stripe.com/settings/apps)in settings and click your recently installed app.
3. From the app settings page, clickView API keys. Copy this secret key to test your integration.

To test your app on a different Stripe account than the one used to develop your app, use external testing.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Develop your app](#develop-app)[Test your app](#test-app)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`