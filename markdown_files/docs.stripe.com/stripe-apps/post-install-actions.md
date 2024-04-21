htmlEnable post-install actions and configurations | Stripe Documentation[Skip to content](#main-content)Post-install actions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpost-install-actions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpost-install-actions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Enable post-install actions and configurations

Support additional configurations that occur after app installation.After a user installs your app, you might require them to perform additional actions or configurations. For example, your app might require that the user supply separate credentials to access an external service. Stripe Apps refer to these additional steps as post-install actions. You can configure one of several types of post-install actions:

- Within the app itself, using a[SettingsView](/stripe-apps/components/settingsview)component
- Externally, using a link to an external website

If you don’t define a post-install action, the Dashboard displays the app after installation.

## Add a post-install action

To add a post-install action:

1. Open your app manifest file.


2. Add a new field, post_install_action.

stripe-app.json`{
  "id": "com.invoicing.[YOUR_APP]",
  "version": "1.2.3",
  "name": "[YOUR APP] Shipment Invoicing",
  "icon": "./[YOUR_APP]_icon_32.png",
  "permissions": [],
  "app_backend": {},
  "ui_extension": {},
  "post_install_action": {}
}`
3. Add the configuration option for the post_install_action that meets the needs of your application setup.


4. Upload your app to Stripe.


5. Make a new release of your app.


6. Publish your app to the marketplace.



## Configuration options

Stripe Apps support the following post-install actions:

- [Link to app](#link-to-app)
- [Link to settings](#link-to-settings)
- [Link to external URL](#link-external)

### Link to app (default)

The default action after the user installs your app is to redirect that user to your application interface, if one is available.

![Post-install screen with a link to view an app](https://b.stripecdn.com/docs-statics-srv/assets/app.09cbbc38c50cfef0a9aaf9a92f8d1d0e.png)

This behavior requires no additional configuration to implement.

### Link to external URL

If you need the user to visit an external site to configure their app, update the post_install_action parameter in your app manifest file as follows:

stripe-app.json`{
  "id": "com.invoicing.[YOUR_APP]",
  "version": "1.2.3",
  "name": "[YOUR APP] Shipment Invoicing",
  "icon": "./[YOUR_APP]_icon_32.png",
  "permissions": [],
  "app_backend": {},
  "ui_extension": {},
  "post_install_action": {
    "type": "external",
    "url": "https://[YOUR-URL]"
  }
}`Replace [YOUR-URL] with the URL to the external site.

When the user installs your app, the application displays a button that redirects the user to the URL specified in the app manifest file.

This URL includes an account_id query string parameter that you can use to identify the user. For example:

`https://www.company.com/marketplace/stripe?account_id=12345`![Post-install screen with an external link](https://b.stripecdn.com/docs-statics-srv/assets/external.565e55096589e7c7580bc5d534c1ace1.png)

### Link to settings

If your app contains a SettingsView component, you can configure a post_install_action to open it after installation. To enable this action, update your app manifest file as follows:

stripe-app.json`{
  "id": "com.invoicing.[YOUR_APP]",
  "version": "1.2.3",
  "name": "[YOUR APP] Shipment Invoicing",
  "icon": "./[YOUR_APP]_icon_32.png",
  "permissions": [],
  "app_backend": {},
  "ui_extension": {},
  "post_install_action": {
    "type": "settings"
  }
}`When the user installs your app, the application displays a button that redirects them to your applications SettingsView component.

![Post-install screen with a link to view settings](https://b.stripecdn.com/docs-statics-srv/assets/settings.e6bc859871bc657c25d353055497c8ee.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Add a post-install action](#add-a-post-install-action)[Configuration options](#configuration-options)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`