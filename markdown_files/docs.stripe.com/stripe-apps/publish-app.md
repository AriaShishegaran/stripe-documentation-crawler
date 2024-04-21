htmlPublish your app to the Stripe App Marketplace | Stripe Documentation[Skip to content](#main-content)Publish your app[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpublish-app)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpublish-app)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Publish your app to the Stripe App Marketplace

Make your app discoverable to any user by publishing it on the Stripe App Marketplace.To share your app beyond your own team, publish it to the Stripe App Marketplace. This makes it available for installation on any Stripe account, not just your own.

Publication comes with some restrictions:

- Your account must be[activated](/get-started/account/activate).
- You can only publish one app per account.
- Stripe can only support English language listings at this time. To support additional languages, reach out to Stripe.
- Published apps must pass a review process. For more information, see the[app review requirements](/stripe-apps/review-requirements)and[app listing guidelines](/stripe-apps/listing-guidelines).
- If you need to remove your app from the Stripe App Marketplace later, you must contact Stripe for removal.

These restrictions only apply to apps that you share with public users in the Stripe App Marketplace. If your app only needs to be available to your own team members, learn to upload and install your app instead.

[Before you begin](#before-you-begin)1. If you’ve already[installed your app in live mode](/stripe-apps/upload-install-app), you must[uninstall it](/stripe-apps/upload-install-app#uninstall-your-live-app)to switch to publishing your app.
2. Choose a Stripe account to associate with your app. You can only publish one app per account.
3. To understand the process for getting your app approved for listing, see[app review requirements](/stripe-apps/review-requirements).

[Update the distribution type](#set-your-distribution-type)1. Set your app to the public distribution.

Command Line`stripe apps set distribution public`This command updates the manifest file with a distribution_type field set to a public value.

stripe-app.json`{
  "id": "com.example.app",
  "version": "1.2.3",
  "name": "Example App",
  "icon": "./example_icon_32.png",
  "distribution_type": "public"
}`[Add permissions](#add-permissions)To add your app’s required permissions:

1. Determine which objects your app calls on the Stripe API.If you’re[migrating an extension to an app](/stripe-apps/migrate-extension), you must determine which objects your extension (not your app) calls on the Stripe API to understand which permissions to include.
2. See the[list of permissions](/stripe-apps/reference/permissions)you can add to your[app manifest](/stripe-apps/reference/app-manifest).
3. You can add a permission to the`permissions`array in your`stripe-app.json`app manifest file using the following command:

Command Line`stripe apps grant permission "PERMISSION_NAME" "EXPLANATION"`Populate the prompts with your permission’s information:

- `PERMISSION_NAME`: The name of the permission you’d like to add. See[possible permission names](/security/permissions).
- `EXPLANATION`: Explanation for enabling access. Users see this explanation when they install your app.

Repeat this step for each new permission that you want to add to your application.

### Your app manifest file should look like this:

To remove a permission, you can also use the CLI:

Command Line`stripe apps revoke permission "PERMISSION_NAME"`[Upload in test mode](#upload-in-test-mode)To upload your app, run the following command from your project root directory:

Command Line`stripe apps upload`Stripe validates your app manifest, then uploads and installs your app to your Stripe test account.

After this step:

- Any team member can access your app in[test mode](/test-mode)at[https://dashboard.stripe.com/test/](https://dashboard.stripe.com/test/).
- Your app can[store secrets](/stripe-apps/store-secrets)in test mode.
- You can access your app’s signing secret to connect it to a[backend](/stripe-apps/build-backend).

[Submit app for review](#submit-app-for-review)1. Upload a new version of your app after setting the distribution type.

After you make your distribution choice, Stripe automatically applies it to all future app versions. To change how to distribute your app after you publish it to all Stripe users, contact Stripe at stripe-apps@stripe.com.


2. In the Stripe Dashboard, navigate to Apps, then select your app to see its details page.


3. If your app has multiple versions, choose the app version you want to publish and click Continue. If you can’t select a version, activate your account first.


4. Create your app listing by clicking Edit listing and providing an overview, features, pricing and support, and resource links to help users evaluate your app. As you complete the listing, you can see its preview on the right side of the Dashboard.

For tips on ensuring app approval and creating a compelling listing, see App listing guidelines.


5. Click Continue to provide the following information before final app submission:

  - Version: If your app has multiple versions, select and verify the version you want to submit for review.
  - Marketplace install URL: This option is required for[OAUTH apps](/stripe-apps/api-authentication/oauth)and optionally available for apps that support[install links](/stripe-apps/install-links). From the Stripe App Marketplace, users are redirected to this URL to install your app.NoteThe URL must link to a page that can initiate the onboarding and installation process with clear instructions.


  - Testing credentials: If your app requires sign in, provide at least one test account to allow Stripe to test and review your app. See the[example testing credentials](/stripe-apps/review-requirements#test-plan-and-credentials).CautionStripe does not permit you to use real (non-test) accounts for the app review process.


  - Testing guidance: Provide user scenarios to allow Stripe to simulate the user’s intended installation and usage of your app. To increase your chances of passing app review, see[example testing guidance](/stripe-apps/review-requirements#test-plan-and-credentials).
  - Contact emails: Provide the email of the recipient for app review updates, and the email of a contact for resolving security incidents.

Any changes you make after starting the review process are subject to an additional review period. To avoid delays, ensure all information is accurate according to App review requirements before final submission.


6. To start the review process, click Submit for review.

After Stripe reviews and approves your app, you have the ability to publish it to the Stripe App Marketplace. If you need to make changes, you can cancel your app in review, and Stripe removes your position in the review queue.

To avoid delays, make sure all information is accurate according to the App review requirements before final submission. After your app is In Review, you won’t be able to withdraw your submission or make changes. After Stripe reviews and approves your app, you can publish it to the Stripe App Marketplace.



[Publish your app](#publish-app)After Stripe verifies that your app meets all app review requirements, we send a notification to the contact email and update your app details page with a review decision. If your app requires additional changes, Stripe provides guidance on the changes you need to address for approval. After you implement the changes, you can resubmit your app for another review.

1. After Stripe approves your app, go to the Apps page in the Stripe Dashboard. Select your app, and preview your listing by clicking Review and publish.

If you decide to make changes, clicking Cancel and edit requires you to resubmit your app for review.


2. To publish and list your app on the Stripe App Marketplace, click Publish.



After this step:

- Any user can discover your app on the Stripe App Marketplace.
- Any Stripe account user can install and use your app.
- You can view[app analytics](/stripe-apps/analytics)as soon as 24 hours after publication.

## See also

- [Add deep links](/stripe-apps/deep-links)
- [Versions and releases](/stripe-apps/versions-and-releases)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Update the distribution type](#set-your-distribution-type)[Add permissions](#add-permissions)[Upload in test mode](#upload-in-test-mode)[Submit app for review](#submit-app-for-review)[Publish your app](#publish-app)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`