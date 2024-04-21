# Restricted API key authentication

A user authenticating with the RAK follows these steps.

- On your site, the user clicks a link that redirects them to Stripe.

- On Stripe, the user selects the appropriate account and accepts permissions for installing the app.

- After the app is installed, it generates a restricted API key provisioned with the proper permissions.

- The user copies the generated keys and provides them to your site.

[Develop your app](#develop-app)

## Develop your app

- Create your app using our template.Command Linestripe apps create <app-name> --template restricted-api-key-appIf you have an existing app, run this command in Stripe CLI:Command Linestripe apps set api-access-type restricted_api_key

Create your app using our template.

If you have an existing app, run this command in Stripe CLI:

- Add all the permissions that your app requires.

Add all the permissions that your app requires.

[permissions](/stripe-apps/reference/permissions)

- Edit your app settings page. If you use the template above, a settings view is automatically created. We recommend adding instructions or links to your own documentation on this page for users to reference when setting up your app.Example app settings page

Edit your app settings page. If you use the template above, a settings view is automatically created. We recommend adding instructions or links to your own documentation on this page for users to reference when setting up your app.

[app settings page](/stripe-apps/app-settings)

Example app settings page

- Upload your app to Stripe.NoteAfter you upload your RAK app, you can’t change the API authentication method.Command Linestripe apps upload

Upload your app to Stripe.

[Upload](/stripe-apps/upload-install-app)

After you upload your RAK app, you can’t change the API authentication method.

[API authentication method](/stripe-apps/api-authentication)

[Test your app](#test-app)

## Test your app

You can test the RAK authentication on your own account.

- Install your app in test mode on your account.

[Install your app in test mode](/stripe-apps/versions-and-releases#changing-between-versions)

- Go to your installed apps page in settings and click your recently installed app.

[installed apps page](https://dashboard.stripe.com/settings/apps)

- From the app settings page, click View API keys. Copy this secret key to test your integration.

To test your app on a different Stripe account than the one used to develop your app, use external testing.

[external testing](/stripe-apps/test-app)
