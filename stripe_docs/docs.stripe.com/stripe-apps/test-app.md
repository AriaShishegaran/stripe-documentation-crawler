# Test your app externally

External testing is currently only available for public apps.

You can set up an external test to enable other accounts to install your app before you publish and distribute a new version to the App Marketplace.

## Before you begin

- Create your app.

[Create your app](/stripe-apps/create-app)

- Review the mandatory App review requirements.

[App review requirements](/stripe-apps/review-requirements)

- Upload your app in test mode.

[Upload your app](/stripe-apps/upload-install-app)

- There is a limit of 25 testers per app. Limit the use of external tests for testing purposes only.

[Set up an external test](#set-up-test)

## Set up an external test

- From the Developer’s Dashboard > Apps, select the app you want to test externally.

[Developer’s Dashboard](https://dashboard.stripe.com/developers)

[Apps](https://dashboard.stripe.com/apps)

- Click the External test tab, then click Get Started.If you don’t see the External test tab, verify if you’ve selected public distribution from Create a release.

- If you don’t see the External test tab, verify if you’ve selected public distribution from Create a release.

- Complete the following fields to configure external testing (which you can edit at any time):Link access: Choose whether anyone can install the app using the link or to restrict to invited users only.Version: Select a version for users to install. If you change the version, all current users will be updated to the new version.

- Link access: Choose whether anyone can install the app using the link or to restrict to invited users only.

- Version: Select a version for users to install. If you change the version, all current users will be updated to the new version.

- Click the invite link to copy it, and send to users for them to install on their account. These users must have administrator rights to install the app.

Result: After a user installs the test version of your app, all members of the account can use it.

Inviting users using the Dashboard

[Update version of test app](#update-test-version)

## Update version of test app

- From the Developer’s Dashboard > Apps, select the app you want to test externally.

[Developer’s Dashboard](https://dashboard.stripe.com/developers)

[Apps](https://dashboard.stripe.com/apps)

- Click the External test tab, then click Edit.

- Select a new version of your app from the dropdown, and click Save.

Result: After you save, all test apps of current users will automatically update to the new version.

[Evaluating your test app](#evaluating-test)

## Evaluating your test app

You must inform your users that test apps are still in development and haven’t been reviewed by Stripe. Users should only install apps from developers they trust.

After the tester opens the invite link, Stripe redirects them to the following page in the Stripe Dashboard:

Installation invite

After the user installs the app, all members on the account can use it. If the published version of the app is already installed on the account, it needs to be uninstalled before the test version can be installed.

After installation, the app displays in the dock on the right side of the Dashboard. After the tester opens the test app, there is a test version badge next to the app name. They can hover over this badge to learn more about the app and the testing criteria.

Test app in dock

If users no longer want to evaluate a test app, they must select it from Settings > Installed Apps and uninstall it. If the published version of the app was previously installed on the account, users can reinstall the app from the App Marketplace.

[Settings](https://dashboard.stripe.com/settings/apps)

[Installed Apps](https://dashboard.stripe.com/settings/apps)

Settings page

Currently, we don’t support ending external testing with the Stripe Dashboard. Instead, to end a test of an app, you must upload a new version of the app to disable the functionality. After this update, the new test version is available for external testing.

## See also

- Publish your app

[Publish your app](/stripe-apps/publish-app)

- App review requirements

[App review requirements](/stripe-apps/review-requirements)
