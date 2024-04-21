htmlDistribution options | Stripe Documentation[Skip to content](#main-content)Distribution options[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fdistribution-options)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fdistribution-options)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Distribution options

Learn what you need to know to share your Stripe Apps with users.Stripe Apps gives you two ways to distribute your apps. You can make them publicly available or share them only with your team members.

## Publish your app on the Stripe App Marketplace

The Stripe App Marketplace is how you share your application with the Stripe user community.

When you publish an app on the App Marketplace, make sure the app complies with all app review requirements. We also recommend reviewing our app listing guidelines for best practices and recommended coding patterns. Stripe reviews all apps to make sure they comply with the published requirements before listing them in the marketplace.

Stripe can only support English language listings at this time. To support additional languages, reach out to Stripe.

The publishing process consists of these steps:

1. Select the version of the app that you want to publish.
2. Create an app listing that provides prospective users with information about your app and defines how your app appears in the App Marketplace.
3. Submit the application for review.
4. Publish the app to the App Marketplace.

For more information, learn how to publish your app.

## Share your app with team members

With Stripe Apps, you have the option of sharing your app only with team members. For example, you might develop an app that sends sale data into your own custom accounting system. Or you might build an app that connects paid orders with your fulfillment system. For these and other situations, you can make the application only available to team members of your Stripe account.

Unlike apps on the App Marketplace, apps shared with team members don’t go through a review process. However, we recommend reviewing our app review requirements and app listing guidelines when you build your app.

Sharing your app with team members consists of these steps:

1. Specify that you want to share your app only with members of your Stripe account.
2. Select the version of the app that you want to[upload and make available](/stripe-apps/upload-install-app).

If you later decide you want to publish your app on the Stripe App Marketplace, you must uninstall your app in live mode first.

## Setting the distribution type for your app

To set the distribution type for your app, run the following command:

Command Line`stripe apps set distribution public`Command Line`stripe apps set distribution private`This updates the app manifest to reflect the distribution type. The new distribution takes effect after you upload your app. The private distribution type is the default type, which you don’t need to explicitly set.

CautionYou can continue to change the distribution type until you upload an app. After you upload an app with a public distribution, you can’t set a public distribution for another app within the same Stripe account. You can change the distribution type from private to public if there are no other public apps within the same Stripe account.

### Updated app manifest:

## See also

- [Publish your app](/stripe-apps/publish-app)
- [Upload your app](/stripe-apps/upload-install-app)
- [Invite team members or developers to access your Stripe account](https://support.stripe.com/questions/invite-team-members-or-developers-to-access-your-stripe-account)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Publish your app on the Stripe App Marketplace](#publish-app)[Share your app with team members](#share-with-team-members)[Setting the distribution type for your app](#set-distribution-type)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`