htmlConfigure the Stripe Connector for PrestaShop | Stripe Documentation[Skip to content](#main-content)Configure the connector[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fprestashop%2Fconfiguration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fprestashop%2Fconfiguration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[PrestaShop](/docs/connectors/prestashop)# Configure the Stripe Connector for PrestaShop

Learn how to configure the Stripe Connector for PrestaShop.To use Stripe with PrestaShop, you must install and then configure the Stripe connector.

## Configure the connector

Use the PrestaShop dashboard to configure the connector.

1. Under Modules, select Module Manager.


2. On the Modules tab, for the Stripe payment module, click Configure.


3. Configure the Stripe Connector for PrestaShop:

  - [Connect to Stripe to accept payments](/connectors/prestashop/configuration#connect-stripe)
  - [Choose your payment form](/connectors/prestashop/configuration#payment-form)
  - [Customize the payment form](/connectors/prestashop/configuration#customize-payment-form)
  - [Collect your customer’s postal code](/connectors/prestashop/configuration#postal-code)
  - [Choose how to capture funds](/connectors/prestashop/configuration#capture-funds)



## Install the Stripe PrestaShop Commerce app

Use Stripe Apps to bolster security and simplify the use of distinct restricted keys for each integration with your Stripe account. The process of installing the Stripe App and acquiring the newly generated secret and publishable keys is essential for your integration with the PrestaShop Commerce connector. This approach eliminates the need to manually create your own restricted key or use a secret key. To integrate the PrestaShop Commerce app and reinforce your account’s security infrastructure:

1. Navigate to the[Stripe App Marketplace](https://marketplace.stripe.com/), then click[Install the PrestaShop Commerce app](https://marketplace.stripe.com/apps/install/link/com.stripe.PrestaShop.commerce).
2. Select the Stripe account where you want to install the app.
3. Review and approve the app permissions, install the app in test mode or live mode, then clickInstall.
4. After you install the app, store the keys in a safe place where you won’t lose them. To help yourself remember where you stored it, you can[leave a note on the key in the Dashboard](/keys#reveal-an-api-secret-key-live-mode).
5. Use the newly generated publishable key and secret key to finish the Connector configuration.
6. To manage the app or generate new security keys after installation, navigate to the application settings page in[test mode](https://dashboard.stripe.com/test/settings/apps/com.stripe.PrestaShop.commerce)or[live mode](https://dashboard.stripe.com/settings/apps/com.stripe.PrestaShop.commerce).

## Connect to Stripe to accept payments

Connect PrestaShop to your Stripe account to start accepting payments.

1. On theStripe Configurepage, clickConnect with Stripe.
2. Navigate to theStripe Configurepage in the PrestaShop Dashboard, then paste the key from the Stripe PrestaShop app into the appropriate field.

## Choose your payment form

Configure the payment form that displays to your customers during checkout. Under Payment form settings, you can choose from the following:

- Integrated payment form–The[Payment Element](/payments/payment-element)is an embeddable UI component that lets you accept 25+ payment methods with a single integration.

![Integrated payment form with Payment Element](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_element.92e9bda6d112030dee8cd68a9af2a9eb.png)

- Redirect to Stripe–[Stripe Checkout](/payments/checkout)lets you redirect your customers to a Stripe-hosted, customizable checkout page to finalize payment.

![Stripe-hosted checkout page](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_checkout.d40ed334159b3a72be24b0f86bbbb376.png)

## Customize the payment form

You can customize the appearance of the integrated payment form. Under Select a theme for the integrated payment form, choose one of the following: Stripe, Night, Flat, or None.

## Collect your customer’s postal code

You can specify whether or not to collect your customer’s postal code at checkout using the Never collect the postal code field. Stripe recommends collecting and verifying postal code information, which can help decrease the card decline rate.

- (Recommended) Unselect this field if you want to require a postal code at checkout. This applies to cards issued in Canada, the United Kingdom, or the United States.


- Select this field if you don’t want to collect a postal code at checkout.



## Choose how to capture funds

You can specify how you want to authorize and capture funds using the Enable separate authorization and capture field.

- Unselect this field to use simultaneous authorization and capture. The issuing bank confirms that the cardholder can pay, and then transfers the funds automatically after confirmation.


- Select this field to use separate authorization and capture. The authorization occurs first, and the capture occurs later.



You can usually authorize a charge within a 7-day window.

To capture funds, do either of the following:

- In the PrestaShop dashboard, change the order’s payment status from Authorized to the status you specify in the Catch status field. For example, you can use Shipped as the catch status. The capture occurs automatically when the status changes.

If the capture is unsuccessful, the status changes to the specified value in the Transition to the following order status if the authorization expires before being captured field.


- In the Stripe Dashboard, under Payments, select All payments. On the Uncaptured tab, select the order and then click Capture.



## Refunds

To refund a payment, you need the Stripe Payment ID for the order.

1. In the PrestaShop dashboard, under Orders, select Orders.


2. Find the order you want to refund and copy the Payment ID under Stripe.


3. To initiate a full or partial refund, do the following:

  1. Go to the Refund tab on the Stripe payment module.


  2. In the Stripe Payment ID field, paste the payment ID.


  3. Select Full refund or Partial refund. If you want to initiate a partial refund, you must provide the amount to refund.


  4. Click Request Refund.





## See also

- [Overview](/connectors/prestashop)
- [Install the connector](/connectors/prestashop/installation)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Configure the connector](#configure-connector)[Install the Stripe PrestaShop Commerce app](#install-the-stripe-prestashop-commerce-app)[Connect to Stripe to accept payments](#connect-stripe)[Choose your payment form](#payment-form)[Customize the payment form](#customize-payment-form)[Collect your customer’s postal code](#postal-code)[Choose how to capture funds](#capture-funds)[Refunds](#refunds)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`