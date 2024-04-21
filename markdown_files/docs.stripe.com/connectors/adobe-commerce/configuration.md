htmlConfiguring the Stripe Connector for Adobe Commerce | Stripe Documentation[Skip to content](#main-content)Configuration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce%2Fconfiguration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce%2Fconfiguration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Adobe Commerce](/docs/connectors/adobe-commerce)# Configuring the Stripe Connector for Adobe Commerce

Learn how to configure the Stripe Connector for Adobe Commerce to choose payment methods. for your Adobe Commerce site and other options.## Find the module configuration options

To configure the Stripe Connector for Adobe Commerce navigate to the configuration section for it (Stores > Configuration > Sales > Payment Methods):

![](https://b.stripecdn.com/docs-statics-srv/assets/configure-module.7bf695b8cd83fe02e952a9fc5bc008fa.png)

Configuring the Stripe module

Stripe appears on your checkout page only after you configure your API keys. If you don’t have a Stripe account yet, register online.

## Install the Stripe Adobe Commerce app

Use Stripe Apps to bolster security and simplify the use of distinct restricted keys for each integration with your Stripe account. The process of installing the Stripe App and acquiring the newly generated secret and publishable keys is essential for your integration with the Adobe Commerce connector. This approach eliminates the need to manually create your own restricted key or use a secret key. To integrate the Adobe Commerce app and reinforce your account’s security infrastructure:

1. Navigate to the[Stripe App Marketplace](https://marketplace.stripe.com/), then click[Install the Adobe Commerce app](https://marketplace.stripe.com/apps/install/link/com.stripe.AdobeCommerce).
2. Select the Stripe account where you want to install the app.
3. Review and approve the app permissions, install the app in test mode or live mode, then clickInstall.
4. After you install the app, store the keys in a safe place where you won’t lose them. To help yourself remember where you stored it, you can[leave a note on the key in the Dashboard](/keys#reveal-an-api-secret-key-live-mode).
5. Use the newly generated publishable key and secret key to finish the Connector configuration.
6. To manage the app or generate new security keys after installation, navigate to the application settings page in[test mode](https://dashboard.stripe.com/test/settings/apps/com.stripe.AdobeCommerce)or[live mode](https://dashboard.stripe.com/settings/apps/com.stripe.AdobeCommerce).

## General settings

- Mode:We recommend that you start by testing the integration in[test mode](/test-mode). Switch to live mode when you’re ready to accept live transactions. You can learn more about[testing payments](/testing)on Stripe.
- API keys:Fill in the test and live keys that Stripe provides to you in the[Adobe Commerce app](https://dashboard.stripe.com/test/settings/apps/com.stripe.AdobeCommerce).
- Hold Elevated Risk Orders:If Stripe[Radar](/radar)marks a payment with an`Elevated Risk`status, the module places the order`On Hold`until you review the payment. See the section[Enabling fraud prevention features with Stripe Radar](/connectors/adobe-commerce#radar)for additional details.
- Receipt Emails:When enabled, Stripe sends a payment receipt email to the customer after the payment succeeds. You can customize the styles and brand of emails from your Stripe account settings.

## Payments

- Enabled:Enable or disable Stripe as an available payment method for the standard checkout page, for the multi-shipping checkout page, and for the admin area.
- Payment flow:Select your preferred payment flow for the standard checkout page. With the embedded payment flow, we embed an iframe-based Payment Element directly in the checkout page. With the redirect payment flow, we redirect customers to Stripe Checkout to complete their payment.
- Form layout:Display the payment method selector in Horizontal layout (tabs), or Vertical layout (accordion). We recommend the Vertical layout for narrow sections, such as on mobile or 3-column checkout pages. You can test the two layouts in the PaymentElement’s interactive[UI component](/payments/payment-element).
- Title:The label you want to display to the customer on the checkout page.
- Payment method configuration:Stripe supports[multiple configurations](/payments/payment-method-configurations)of payment methods. After you[configure the payment methods](https://dashboard.stripe.com/settings/payment_methods), they immediately become available in the dropdown field. You can select a different configuration for each of your store views, based on business requirements.
- Payment Action:SelectAuthorize and Captureif you want to charge customer cards immediately after a purchase. This is the default option and doesn’t require you to do anything after the customer has placed the order. If you prefer to finalize the payment later, you can chooseAuthorize Only, which authorizes and holds the order amount on the customer’s card so you can capture the amount later by issuing an invoice. You can read more about[capturing payments using invoices](/connectors/adobe-commerce/admin#capturing-later)with this module.
- Expired authorizations:For card payments that you don’t capture immediately, you must do so within seven days. Any attempt to capture the amount after that returns an error. By enabling this option, the module attempts to recreate the original payment with the original card used for that order. The module saves cards automatically inAuthorize Onlymode and the customer can’t delete them from their account section until you either invoice or cancel the order.
- Automatic Invoicing:The Authorize Only option creates a new invoice with a Pending status on checkout. After capturing the charge, the invoice status transitions to Paid. This option is useful when Payment Action is set to Authorize Only: no invoice results from completing the checkout flow. If enabled, the module automatically generates an invoice on checkout completion so you can email it to a customer before charging them.
- Save customer payment methodEnable this option to allow customers to save their last used payment method in the Stripe vault and reuse it later for quicker checkout.
- Card Icons:Display card icons based on the card brands your Stripe account supports.
- Optional Statement Descriptor:This is an optional short description for the source of the payment, shown in the customer’s bank statements. If left empty, the default descriptor configured from your Stripe Dashboard applies. This option isn’t available for Multibanco, SEPA Direct Debit, or Sofort.
- Sort Order:If you’ve enabled multiple payment methods, this setting determines the order of payment methods presented on the checkout page.

## Wallet Button

If your customer is using a compatible device, they can use Apple Pay or Google Pay during the checkout process. Use the dedicated configuration section in the Adobe Commerce admin panel to set your preferences:

![](https://b.stripecdn.com/docs-statics-srv/assets/configure-wallet-button.dbc0da4d8f6bdfaaf937946325725378.png)

Configuration options for Apple Pay and Google Pay

- Enabled:Enable or disable the wallet button as an available payment method for the locations selected. You can enable the wallet button even if you disable regular payments.
- Locations:Choose where to display the wallet button. If you’re using the embedded payment flow, we recommend against selecting the checkout page, because the Payment Element already displays its own version of the wallet button. If you still choose to enable it on the checkout page, the module hides the wallet button in the Payment Element to avoid displaying it twice.
- Button Type:Choose between three types of payment buttons to display (Default, Buy, and Donate).
- Button Theme:Choose between three types of button themes (Dark, Light, and Light-Outline).
- Button Height:Adjust the button height to match your theme’sAdd to CartandProceed to Checkoutbuttons.
- Seller Name:The name of your business that appears in the modal at the time of the payment.

See the troubleshooting section if the button doesn’t appear after enabling it.

## Webhooks

Stripe uses webhooks to notify your application when an event happens in your account. Webhooks are particularly useful for updating Magento orders when a customer’s bank confirms or declines a payment, or when collecting subscription payments. These events allow the module to mark Magento orders as ready for fulfilment, record refunds against them, or add comments about payment failure reasons.

Starting from version 3 of the module, you no longer need to manually configure webhooks. The module checks and potentially configures webhooks automatically in the following cases:

- When you install or upgrade the module and trigger the`setup:upgrade`command.
- Every time you update the API keys in the Magento admin.
- Every time you change the URL of a store in the Magento admin.
- When the module detects a change in the database during one of the hourly automated checks. This prevents webhooks from being broken due to a manual change to the database, a migration from a different server, or a backup restoration.

When updating webhooks, the module creates a single webhook endpoint per Stripe account. For example, if you have five store views, four are using a Stripe account and the last one is using a different Stripe account, the module creates two webhook endpoints.

This also applies if you use different domain names for your store views. In this case, the module uses one of the store view domains and not your base URL. This is to prevent issues with base URLs often being behind a firewall for security reasons.

The module uses webhook signatures to verify that the events were sent by Stripe, not by a third party. You can disable this protection only when your Magento instance is using developer mode.

## See also

- [Using Subscriptions](/connectors/adobe-commerce/subscriptions)
- [Using the Adobe Commerce admin panel](/connectors/adobe-commerce/admin)
- [Troubleshooting](/connectors/adobe-commerce/troubleshooting)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Find the module configuration options](#find-the-module-configuration-options)[Install the Stripe Adobe Commerce app](#install-the-stripe-adobe-commerce-app)[General settings](#general-settings)[Payments](#payments)[Wallet Button](#wallet-button)[Webhooks](#webhooks)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`