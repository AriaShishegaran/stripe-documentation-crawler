# Upload and install your Stripe App

Some Stripe Apps features also require you to upload your app. For more information, see:

- Store secrets

[Store secrets](/stripe-apps/store-secrets)

- Add server-side functionality

[Add server-side functionality](/stripe-apps/build-backend)

To share your app with your team members, install it on your Stripe account with two steps:

[team members](/dashboard/teams)

- Upload in test mode

[Upload in test mode](#upload-your-app-in-test-mode)

- Install in live mode

[Install in live mode](#install-in-live-mode)

Any team member with access to your Stripe account can run your installed apps. To give other Stripe accounts access, you can publish your app on the Stripe App Marketplace. Your app ID must be globally unique.

[publish your app](/stripe-apps/publish-app)

[app ID](/stripe-apps/reference/app-manifest#schema)

[Upload in test mode](#install-your-app-in-test-mode)

## Upload in test mode

To upload your app, run the following command from your project root directory:

Stripe validates your app manifest, then uploads your app to your Stripe test account. After validation is a complete, a banner is shown with a prompt and button to install the new version into test mode.

[app manifest](/stripe-apps/reference/app-manifest)

You can install previous versions though the Version History list.

- In the version history table, click the overflow menu () of the version you want to install.

- Select Install in test mode and complete the installation.

After this step:

- Any team member can access your app in test mode at https://dashboard.stripe.com/test/.

[test mode](/test-mode)

[https://dashboard.stripe.com/test/](https://dashboard.stripe.com/test/)

- Your app can store secrets in test mode.

[store secrets](/stripe-apps/store-secrets)

- You can access your app’s signing secret to connect it to a backend.

[backend](/stripe-apps/build-backend)

[Install in live mode](#install-in-live-mode)

## Install in live mode

To access real customer data, install your app in live mode.

- Select your app from the Apps page in the Developers Dashboard.

[Apps page in the Developers Dashboard](https://dashboard.stripe.com/apps)

- Select the Private to your account option when choosing how to distribute.

- Choose a version for your app and click Continue.

- Click Continue to open your app in the Dashboard, then click Install.

- Click Done, refresh your browser, and see your app in live mode across the Dashboard in the right-hand side drawer.

After this step:

- Any team member can access your app in live mode in the Dashboard.

- Your app can store secrets in live mode.

[store secrets](/stripe-apps/store-secrets)

- Your app’s signing secret remains available.

To switch between installing your app in live mode to publishing it on the Stripe App Marketplace, uninstall the app in live mode:

- Go to the Installed Apps page in the Dashboard, and find the app you want to uninstall.

[Installed Apps page in the Dashboard](https://dashboard.stripe.com/settings/apps/)

- Click the overflow menu  at the right side of your app, and click View app details.

- Click Uninstall app, and click Uninstall.

After this step, you can publish your app to the Stripe App Marketplace.

[publish your app to the Stripe App Marketplace](/stripe-apps/publish-app)

## See also

- Add deep links

[Add deep links](/stripe-apps/deep-links)

- Versions and releases

[Versions and releases](/stripe-apps/versions-and-releases)
