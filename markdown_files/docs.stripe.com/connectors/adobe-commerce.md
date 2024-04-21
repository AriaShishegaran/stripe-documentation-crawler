htmlStripe Connector for Adobe Commerce | Stripe Documentation[Skip to content](#main-content)Adobe Commerce[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)# Stripe Connector for Adobe Commerce

Enable Stripe payments for storefronts built on Adobe Commerce.## Getting started

Install the module and then go to the configuration section to set your preferred checkout flow and other options.

## Accept online payments

The module offers two different flows for accepting payments in Adobe Commerce:

- Embed the[Payment Element](/payments/payment-element)on your website (recommended).
- Redirect to[Stripe Checkout](/payments/checkout), a payment form hosted on Stripe.

Both options are optimized for conversion and SAQ-A eligible, simplifying PCI compliance.

![](https://b.stripecdn.com/docs-statics-srv/assets/embedded-flow.913e34d5ec2bc301dd78f655a69a8565.png)

Embed the Payment Element

![](https://b.stripecdn.com/docs-statics-srv/assets/redirect-flow.9014504efc06073a8b2b06f4831d8778.png)

Redirect to Stripe Checkout

You can individually enable or disable payment methods from your payment methods settings. This applies to both Stripe Checkout and the Payment Element. You don’t need to upgrade your integration after you enable a payment method, even if the payment method became available after you installed the Stripe Connector for Adobe Commerce.

NoteThe full list of supported payment methods is available in the integration options section.

To optimize conversions, Stripe Checkout and the Payment Element display payment methods dynamically to adapt to the current session. The customer device, shipping country, cart currency and even cart contents are taken into consideration to select and sort payment methods for conversion. For logged in customers, we display their saved payment methods first to enable faster checkout.

You can customize the look and feel of the Payment Element by overriding the getElementOptions() PHP method under Model/Ui/ConfigProvider.php. To do this, implement an afterMethod plugin.

### Enabling fraud prevention with Stripe Radar

Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.

If Radar detects a high-risk payment, it might place it under review with an Elevated risk status. If you want to automatically decline charges, you can create a custom rule in your Radar settings. Any orders that go into manual review are automatically placed on hold in Adobe Commerce. You can configure what orders to send to manual review in your Radar rules:

![](https://b.stripecdn.com/docs-statics-srv/assets/radar-result.5124f10f111fecfff231a73522a7a461.png)

Stripe Radar can detect and prevent fraud for orders placed on your site

If you think that an order isn’t fraudulent, you can click Unhold on the order page. This allows you to fulfill the order normally.

To test a fraudulent payment, switch the module to test mode and place an order using the card number 4000 0000 0000 9235.

### Customer Authentication

NoteThe Stripe Connector for Adobe Commerce is SCA-ready and includes 3D Secure 2 support for customer authentication.

By default, customers only see 3D Secure authentication when their bank requires it, so your checkout conversion isn’t negatively affected. In compliance with the Strong Customer Authentication regulation, Stripe displays the 3D Secure authentication flow automatically whenever required by SCA:

![](https://b.stripecdn.com/docs-statics-srv/assets/3d-secure.a876a6e255ef3b0a99d05732fd5eca51.png)

Stripe provides a 3D Secure test payment page in test mode

You can configure your 3DS preferences in your Radar rules.

To test the authentication flow, switch the module to test mode and place an order using any of the test card numbers.

## Grow your recurring revenue with subscriptions

Our module offers a subscription engine for Adobe Commerce that includes the following features:

- Configurable and customer-customizable subscription products in your catalog pages.
- Trial plans or the ability to collect initial fees with each subscription purchase.
- Customer notifications and the collection of new payment details from Stripe Billing when subscription payments fail.
- Reduced churn because Stripe works directly with card networks to automatically update payment details with new card numbers or expiry dates.

## Translations for multi-language websites

CautionIf you configure your locale or currency for the first time, make sure to flush the configuration cache.

The module contains a translation file that you can use to configure a multi-language Adobe Commerce site:

`/app/code/StripeIntegration/Payments/i18n/en_US.csv`To create a translation file for a different language, copy this file to:

`/app/code/StripeIntegration/Payments/i18n/languagecode_COUNTRYCODE.csv`Make sure to replace languagecode_COUNTRYCODE with the locale code for your target language. This is the same language you’ve selected under System > Configuration > General > Locale Options > Locale.

After you copy the file, you can replace the second string on each row with a translation of the first string. You don’t need to do anything else for translations.

## See also

- [Installing the Stripe Connector for Adobe Commerce](/connectors/adobe-commerce/install)
- [Configuring the Stripe Connector for Adobe Commerce](/connectors/adobe-commerce/configuration)
- [Using subscriptions](/connectors/adobe-commerce/subscriptions)
- [Using the Adobe Commerce admin panel](/connectors/adobe-commerce/admin)
- [Building a custom storefront](/connectors/adobe-commerce/custom-storefront)
- [Troubleshooting](/connectors/adobe-commerce/troubleshooting)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Getting started](#getting-started)[Accept online payments](#payments)[Grow your recurring revenue with subscriptions](#subscriptions)[Translations for multi-language websites](#translations-for-multi-language-websites)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)[Billing](/billing)[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`