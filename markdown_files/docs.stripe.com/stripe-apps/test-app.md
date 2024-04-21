htmlTest your app externally | Stripe Documentation[Skip to content](#main-content)Test your app[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Ftest-app)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Ftest-app)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Test your app externally

Set up and distribute test versions of your app before publication.NoteExternal testing is currently only available for public apps.

You can set up an external test to enable other accounts to install your app before you publish and distribute a new version to the App Marketplace.

## Before you begin

1. [Create your app](/stripe-apps/create-app).
2. Review the mandatory[App review requirements](/stripe-apps/review-requirements).
3. [Upload your app](/stripe-apps/upload-install-app)in test mode.
4. There is a limit of 25 testers per app. Limit the use of external tests for testing purposes only.

[Set up an external test](#set-up-test)1. From the[Developer’s Dashboard](https://dashboard.stripe.com/developers)>[Apps](https://dashboard.stripe.com/apps), select the app you want to test externally.
2. Click theExternal testtab, then clickGet Started.  - If you don’t see theExternal testtab, verify if you’ve selected public distribution fromCreate a release.


3. Complete the following fields to configure external testing (which you can edit at any time):  - Link access: Choose whether anyone can install the app using the link or to restrict to invited users only.
  - Version: Select a version for users to install. If you change the version, all current users will be updated to the new version.


4. Click the invite link to copy it, and send to users for them to install on their account. These users must have administrator rights to install the app.

Result: After a user installs the test version of your app, all members of the account can use it.

![Set up test app](https://b.stripecdn.com/docs-statics-srv/assets/test-app-setup.b1dacf8f5ad162d1a72cb26162cbb12a.png)

Inviting users using the Dashboard

[Update version of test app](#update-test-version)1. From the[Developer’s Dashboard](https://dashboard.stripe.com/developers)>[Apps](https://dashboard.stripe.com/apps), select the app you want to test externally.
2. Click theExternal testtab, then clickEdit.
3. Select a new version of your app from the dropdown, and clickSave.

Result: After you save, all test apps of current users will automatically update to the new version.

[Evaluating your test app](#evaluating-test)You must inform your users that test apps are still in development and haven’t been reviewed by Stripe. Users should only install apps from developers they trust.

### Installing the test app

After the tester opens the invite link, Stripe redirects them to the following page in the Stripe Dashboard:

![Installation invite](https://b.stripecdn.com/docs-statics-srv/assets/test-app-install.2d67f49c8cafcfb964c9d19ff7cf6d30.png)

Installation invite

After the user installs the app, all members on the account can use it. If the published version of the app is already installed on the account, it needs to be uninstalled before the test version can be installed.

### Using the test app

After installation, the app displays in the dock on the right side of the Dashboard. After the tester opens the test app, there is a test version badge next to the app name. They can hover over this badge to learn more about the app and the testing criteria.

![Using test app](https://b.stripecdn.com/docs-statics-srv/assets/test-app-using.49c64bd7d77b4b76e26ebd6852b40485.png)

Test app in dock

### Leaving the test

If users no longer want to evaluate a test app, they must select it from Settings > Installed Apps and uninstall it. If the published version of the app was previously installed on the account, users can reinstall the app from the App Marketplace.

![Uninstall test app](https://b.stripecdn.com/docs-statics-srv/assets/test-app-uninstall.710b89177767cff3a7f53de749558d88.png)

Settings page

### Ending the test

Currently, we don’t support ending external testing with the Stripe Dashboard. Instead, to end a test of an app, you must upload a new version of the app to disable the functionality. After this update, the new test version is available for external testing.

## See also

- [Publish your app](/stripe-apps/publish-app)
- [App review requirements](/stripe-apps/review-requirements)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Set up an external test](#set-up-test)[Update version of test app](#update-test-version)[Evaluating your test app](#evaluating-test)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`