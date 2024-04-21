# Enable post-install actions and configurations

After a user installs your app, you might require them to perform additional actions or configurations. For example, your app might require that the user supply separate credentials to access an external service. Stripe Apps refer to these additional steps as post-install actions. You can configure one of several types of post-install actions:

- Within the app itself, using a SettingsView component

[SettingsView](/stripe-apps/components/settingsview)

- Externally, using a link to an external website

If you don’t define a post-install action, the Dashboard displays the app after installation.

## Add a post-install action

To add a post-install action:

- Open your app manifest file.

Open your app manifest file.

[app manifest](/stripe-apps/reference/app-manifest)

- Add a new field, post_install_action.stripe-app.json{
  "id": "com.invoicing.[YOUR_APP]",
  "version": "1.2.3",
  "name": "[YOUR APP] Shipment Invoicing",
  "icon": "./[YOUR_APP]_icon_32.png",
  "permissions": [],
  "app_backend": {},
  "ui_extension": {},
  "post_install_action": {}
}

Add a new field, post_install_action.

- Add the configuration option for the post_install_action that meets the needs of your application setup.

Add the configuration option for the post_install_action that meets the needs of your application setup.

[configuration option](#configuration-options)

- Upload your app to Stripe.

Upload your app to Stripe.

[Upload](/stripe-apps/upload-install-app)

- Make a new release of your app.

Make a new release of your app.

[Make a new release](/stripe-apps/versions-and-releases)

- Publish your app to the marketplace.

Publish your app to the marketplace.

[Publish](/stripe-apps/publish-app)

## Configuration options

Stripe Apps support the following post-install actions:

- Link to app

[Link to app](#link-to-app)

- Link to settings

[Link to settings](#link-to-settings)

- Link to external URL

[Link to external URL](#link-external)

The default action after the user installs your app is to redirect that user to your application interface, if one is available.

This behavior requires no additional configuration to implement.

If you need the user to visit an external site to configure their app, update the post_install_action parameter in your app manifest file as follows:

[https://[YOUR-URL]](https://[YOUR-URL])

Replace [YOUR-URL] with the URL to the external site.

When the user installs your app, the application displays a button that redirects the user to the URL specified in the app manifest file.

This URL includes an account_id query string parameter that you can use to identify the user. For example:

If your app contains a SettingsView component, you can configure a post_install_action to open it after installation. To enable this action, update your app manifest file as follows:

[SettingsView](/stripe-apps/components/settingsview)

When the user installs your app, the application displays a button that redirects them to your applications SettingsView component.
