htmlInstall the Stripe Connector for Shopware 6 | Stripe Documentation[Skip to content](#main-content)Install the connector[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fshopware6%2Finstallation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fshopware6%2Finstallation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Shopware 6](/docs/connectors/shopware6)# Install the Stripe Connector for Shopware 6

Learn how to install and update the Stripe Connector for Shopware 6.Use the Stripe Connector for Shopware 6 to integrate Stripe Elements and accept more than 25 payment methods with a single integration.

## Install the connector

Use the Shopware administration panel to install the connector.

1. In the admin panel sidebar, under Extensions, select My extensions.


2. On the My extensions page, on the Shopware Account tab, enter your credentials, then click Login.


3. In the admin panel sidebar, under Extensions, select Store.


4. In the search bar, type Stripe.


5. On the Apps tab, do the following to add the Stripe connector:

  - For the Stripe app, clickAdd extension.
  - Accept the terms and conditions, and then clickAdd extension for free.
  - ClickInstall extension.



## Add Stripe as a payment method

When the installation completes, view the connector on your extensions page in the Shopware administration panel.

1. In the admin panel sidebar, under Sales Channels, select your sales channel to add Stripe as a payment method.


2. Under Payment and shipping, select Pay with Stripe from the Payment methods drop-down.


3. (Optional) To display Stripe first at checkout, select Pay with Stripe from the Default payment method drop-down.


4. Click Save.



## Update the connector

Use the Shopware administration panel to update the connector when a new version is available. Under Extensions, select My extensions. To initialize the update process, select Update on the Apps tab for the Stripe connector.

## See also

- [Overview](/connectors/shopware6)
- [Configure the connector](/connectors/shopware6/configuration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Install the connector](#install-the-connector)[Add Stripe as a payment method](#add-stripe-as-a-payment-method)[Update the connector](#update-connector)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`