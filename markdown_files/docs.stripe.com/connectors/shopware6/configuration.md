htmlConfigure the Stripe Connector for Shopware 6 | Stripe Documentation[Skip to content](#main-content)Configure the connector[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fshopware6%2Fconfiguration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fshopware6%2Fconfiguration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Shopware 6](/docs/connectors/shopware6)# Configure the Stripe Connector for Shopware 6

Learn how to configure the Stripe Connector for Shopware 6.To use Stripe with Shopware 6, you must install and then configure the Stripe connector.

## Configure the connector

Use the Shopware administration panel to configure the connector.

1. In the admin panel sidebar, under Extensions, select My extensions.


2. On the Apps tab, for the Stripe connector, click the overflow menu () and select Open extension.


3. Configure the Stripe Connector for Shopware 6:

  - [Connect to Stripe to accept payments](/connectors/shopware6/configuration#connect-stripe)
  - [Choose your payment form](/connectors/shopware6/configuration#payment-form)
  - [Customize the payment form](/connectors/shopware6/configuration#customize-payment-form)
  - [Collect your customer’s postal code](/connectors/shopware6/configuration#postal-code)
  - [Choose how to capture funds](/connectors/shopware6/configuration#capture-funds)



## Connect to Stripe to accept payments

Connect Shopware to your Stripe account to start accepting payments. When you connect to a new account, you must reactivate your preferred payment methods.

1. On the Stripe Configuration page, click Connect with Stripe in Live Mode. If you want to test different app functionality without processing live payments, use Connect with Stripe in Test Mode.


2. Provide your business information to create your Stripe account.


3. After you create your Stripe account, log in to your Stripe Dashboard.


4. In the Stripe Dashboard, do the following:

  - Under Settings > Payment methods, select your Shopware account from the Select your platform drop-down.


  - Turn on your preferred payment methods individually or by using the Turn on all button.





## Choose your payment form

Configure the payment form that displays to your customers during checkout. Under Payment form settings, you can choose from the following:

- Integrated payment form–The[Payment Element](/payments/payment-element)is an embeddable UI component that lets you accept 25+ payment methods with a single integration.

![Integrated payment form with Payment Element](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_element.424e5b7d979120ca7615409e62bb86bc.png)

- Redirect to Stripe–[Stripe Checkout](/payments/checkout)lets you redirect your customers to a Stripe-hosted, customizable checkout page to finalize payment.

![Stripe-hosted checkout page](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_checkout.9846147c723ca1610638c755de28ebc9.png)

## Customize the payment form

You can customize the appearance of your checkout form in the Stripe Dashboard. Under Select a theme for the integrated payment form, choose one of the following: Stripe, Night, Flat, or None.

## Collect your customer’s postal code

You can specify whether or not to collect your customer’s postal code at checkout using the Never collect the postal code field. Stripe recommends collecting and verifying postal code information, which can help decrease the card decline rate.

- (Recommended) Unselect this field if you want to require a postal code at checkout. This applies to cards issued in Canada, the United Kingdom, or the United States.


- Select this field if you don’t want to collect a postal code at checkout.



## Choose how to capture funds

You can specify how you want to authorize and capture funds.

- Simultaneous authorization and capture–The issuing bank confirms that the cardholder can pay, and then transfers the funds automatically after confirmation.


- Separate authorization and capture–The authorization occurs first, and the capture occurs later. To capture funds, change the order’s payment status from Authorized to Paid or Partially paid in the Shopware administration panel.



## Refunds

You can refund any order with a Paid status. To initiate a refund, select the order under Orders > Overview in the Shopware administration panel. Change the order’s payment status from Paid to Refunded.

## See also

- [Overview](/connectors/shopware6)
- [Install the connector](/connectors/shopware6/installation)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Configure the connector](#configure-connector)[Connect to Stripe to accept payments](#connect-stripe)[Choose your payment form](#payment-form)[Customize the payment form](#customize-payment-form)[Collect your customer’s postal code](#postal-code)[Choose how to capture funds](#capture-funds)[Refunds](#refunds)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`