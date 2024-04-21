htmlStripe Apps | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)# Stripe Apps

Extend Stripe with third party services or embed custom user experiences directly in the Stripe Dashboard.Stripe Apps are meant to extend Stripe. To learn how to accept payments, see Payments. To accept and send multi-party payments, see Connect. To build a lightweight tool you can test, see Developer Tools.

## What are Stripe Apps?

Stripe Apps provides the opportunity to become a third-party developer for Stripe. You can develop and privately distribute or publish your Stripe app on the global Stripe Apps Marketplace. As a third-party Stripe Apps developer, you can create apps to:

- Authenticate users for third-party services using OAuth 2.0 or a restricted API key (RAK).
- Use the Stripe API to make calls, listen to events, and automate workflows. For example, you can create an app that automatically initiates a billing flow when a customer signs a contract, to streamline tasks and reducing manual account reconciliation.
- Design custom user interfaces that operate directly within the Stripe Dashboard. For example, users can interact with customer records, balance statements, and payment information in their CRM systems.

As a Stripe Apps user, you have access to a range of apps on the Stripe Apps Marketplace to help bolster or expand your business on Stripe. You can also integrate Stripe into existing third-party services or platforms to synchronize data fields, trigger external workflows, or use Stripe as a payment processor.

Create an appBuild a Stripe App for your own team—like a deep integration with proprietary data systems—or publish an app in the Stripe App Marketplace, where Stripe’s global users can discover it.

[Get started](/docs/stripe-apps/create-app)![](https://b.stripecdn.com/docs-statics-srv/assets/stripe-apps-hero.730e1e4e3e7a7bc34f02afbb09aca663.png)

## Get started

[Create an appLearn the basics of app development by building an app in the Stripe Dashboard.](/stripe-apps/create-app)[How Stripe Apps workLearn about different app patterns.](/stripe-apps/how-stripe-apps-work)[Sample appsBrowse examples of Stripe apps.](/stripe-apps/sample-apps)## Build an app

[Store secretsLearn how to use the Secret Store API to persist sensitive data, like authentication credentials.](/stripe-apps/store-secrets)[API authentication methodsSelect the API authentication method that works best for your app’s use case.](/stripe-apps/api-authentication)[Server-side logicValidate and process user actions and data in your app using backend code.](/stripe-apps/build-backend)[App settings pageCreate an app settings page for your users in the Stripe Dashboard.](/stripe-apps/app-settings)[Build a UIBuild, test, and edit a custom UI that extends the functionality of the Stripe Dashboard.](/stripe-apps/build-ui)[OnboardingLearn the best practices for guiding your users through your app’s sign in and initial setup flows.](/stripe-apps/onboarding)## Distribute an app

[Distribution optionsLearn about the options to share or distribute your app.](/stripe-apps/distribution-options)[Upload your appLearn how to make your app privately available.](/stripe-apps/upload-install-app)[Versions and releasesLearn about app versioning and releases to ship new versions of your app.](/stripe-apps/versions-and-releases)[Test your appSet up and distribute test versions of your app before publication.](/stripe-apps/test-app)[Publish your appMake your app discoverable to any user by publishing it on the Stripe App Marketplace.](/stripe-apps/publish-app)[Promote your appLearn how to partner with Stripe to improve the discoverability of your app.](/stripe-apps/promote-app)## Migrate to Stripe Apps

[Migrate or build an extensionLearn why and how to migrate your extensions to Stripe Apps.](/stripe-apps/migrate-extension)[Migrate or build a pluginLearn why and how to migrate your plugin or connector to Stripe Apps.](/stripe-apps/onboarding-plugin)## Reference

[App manifestLearn about the app manifest, an index of all fields, types, and descriptions for your app manifest file.](/stripe-apps/reference/app-manifest)[CLIInstall the Stripe Apps command line interface and use it to manage your app.](/stripe-apps/reference/cli)[Extension SDKReview an index of all fields, types, and descriptions for the Extension SDK API.](/stripe-apps/reference/extensions-sdk-api)[PermissionsA list of available events and their required permissions.](/stripe-apps/reference/permissions)[ViewportsReview a list of available viewports for Stripe Apps and how your end users see them.](/stripe-apps/reference/viewports)[ComponentsUse Stripe’s library of components to quickly build your user interface.](/stripe-apps/components)## Support and troubleshooting

Engage with us on Github to:

- [Receive developer support](https://github.com/stripe/stripe-apps/wiki/Developer-Support)
- [View known issues or submit feedback](https://github.com/stripe/stripe-apps/issues)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`