htmlMigrate or build a plugin using Stripe Apps | Stripe Documentation[Skip to content](#main-content)Migrate or build a plugin[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fonboarding-plugin)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fonboarding-plugin)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Migrate or build a plugin using Stripe Apps

Use OAuth 2.0 or RAK to authenticate your plugin's users.Previously, Stripe allowed third-party plugins to request the standard API keys of a user to integrate with their products. Since January 2024, Stripe requires plugins to leverage Stripe Apps. All new and existing plugins must use a Stripe App to authenticate users for their service using Oauth 2.0 or a restricted API key.

If you have an existing plugin, migrate to the standard Stripe Apps integration path for security and compliance purposes. Migrating an existing plugin to a Stripe App integration only requires you to change your plugin’s authentication method.

NoteStripe Apps are meant to extend Stripe. If you want to accept payments, see Payments. If you want to accept and send multi-party payments, see Connect.

### Reasons to migrate

Authentication through a Stripe App is the new default and standard integration path for all new plugins, extensions, and partner connectors. The following are the benefits of the new integration path:

- More efficient onboarding:Your users don’t have to manually create API keys.
- Improved security:Restricted API keys protect users if their keys are exposed.
- Analytics:Get visibility on your app’s adoption and performance.
- Discoverability:Stripe Apps give broad visibility to your product through the Stripe Dashboard, Stripe App Marketplace, and our[partner program](/stripe-apps/promote-app#join-the-stripe-partner-ecosystem).
- Verified Partner:Join the Apps track in[Stripe Partner Ecosystem](/stripe-apps/promote-app#join-the-stripe-partner-ecosystem)to get co-sell, marketing, and technical benefits.

### What happens if you don’t migrate

If you choose not to migrate your authentication to a Stripe App, it will continue to work as it does today, without impact to the user experience until 2024. We’ll continue to support plugins on our backend until the end of 2024.

### Impact on your users after you migrate

If you choose to migrate, your users must re-onboard and re-authenticate their plugin. To migrate or build a plugin, choose either OAuth 2.0 (recommended) or Restricted API Key (RAK) authentication. OAuth is the least complex way for users to securely authenticate a plugin. RAK doesn’t require any additional backend setup from you. However, users must still copy and paste generated Stripe API keys to your third-party plugin. This method increases the complexity of the authentication process for your users.

OAuthRAKThe following is an example of a user re-authenticating with OAuth:

1. From your website, the user wants to integrate with Stripe.
2. They open your app’s[installation link](/stripe-apps/install-links)to view the permissions and install the app.
3. After the user installs your app, authentication is complete, and the user is redirected to your`redirect_uri`.

![The install link page showing an OAuth app](https://b.stripecdn.com/docs-statics-srv/assets/oauth-user-journey.0fd6041638a1cbb305dc88690354a462.png)

## Before you begin

1. Review and complete theBefore you beginsection of[Getting started with Stripe Apps](/stripe-apps/create-app#before-you-begin). Ensure you’ve installed the latest version of the Stripe CLI.
2. Choose your authentication type (OAuth or RAK). After you upload your app, you can’t change the authentication method. For more information about authentication, see[API authentication](/stripe-apps/api-authentication).
3. If you use[Stripe Connect](/connect)and want to migrate an existing plugin through Stripe Apps, you must create a new Stripe account. Currently, a Stripe account with Connect enabled can’t publish an app.
4. You can only create onepublic appper account. If your account already has a public app and you want to publish another one, you must create a new Stripe account. You can still create multiple private apps in tandem with the public app on the same account.

Choose an authentication method to migrate or build your plugin:

[Develop your app](#develop-app-oauth)1. Create your Stripe App by running stripe apps create <app-name> in the CLI.


2. Edit the following fields in the app manifest:

  - Set`stripe_api_access_type`to`oauth`.
  - Set`distribution_type`to`public`.
  - Set your`allowed_redirect_uris`. These are the URLs that users are redirected to after installing your app using OAuth. The first one in the list is used as the default redirect.

Your app manifest should look like this:

stripe-app.json`{
  "id": "com.example.my-app",
  "version": "0.0.1",
  "name": "Your Stripe App",
  "icon": "./[YOUR_APP]_icon_32.png",
  "permissions": [
    // Your app permissions here
  ],
  "stripe_api_access_type": "oauth",
  "distribution_type": "public",
  "allowed_redirect_uris": [
    // Your redirect URIs here
  ]
}`
3. Add all the permissions that your app requires.


4. (Optional) Add UI extensions to your app. We recommend adding a settings view to allow your users to configure settings or to link to your app’s documentation.


5. Upload your app to Stripe.

Command Line`stripe apps upload`

[Test your app](#test-app-oauth)1. Navigate to your app’s details page.
2. Open theExternal testtab and clickGet startedto set up an[external test](/stripe-apps/test-app).
3. Access the authorize links in theTest OAuthsection. You can use this link to test with your own account.

[Configure OAuth 2.0](#configure-oauth)Make sure you’ve configured OAuth 2.0 correctly. To learn how to save and refresh access tokens, see OAuth setup.

[Publish and distribute your app](#publish-app)When you’re ready to distribute your app to users:

1. [Submit your app for review](/stripe-apps/publish-app#submit-app-for-review).
2. After your app is approved,[publish your app](/stripe-apps/publish-app#publish-app)to Stripe App Marketplace.
3. From the app details page, click theSettingstab.
4. Copy theInstall link. Users can use this link to install your app.

[OptionalConfigure payments](#configure-payments)## See also

- [How Stripe Apps work](/stripe-apps/how-stripe-apps-work)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Develop your app](#develop-app-oauth)[Test your app](#test-app-oauth)[Configure OAuth 2.0](#configure-oauth)[Publish and distribute your app](#publish-app)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`