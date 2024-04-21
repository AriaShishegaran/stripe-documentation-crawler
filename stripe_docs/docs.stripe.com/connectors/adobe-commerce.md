# Stripe Connector for Adobe Commerce

## Getting started

Install the module and then go to the configuration section to set your preferred checkout flow and other options.

[Install the module](/connectors/adobe-commerce/install)

[configuration](/connectors/adobe-commerce/configuration)

## Accept online payments

The module offers two different flows for accepting payments in Adobe Commerce:

- Embed the Payment Element on your website (recommended).

[Payment Element](/payments/payment-element)

- Redirect to Stripe Checkout, a payment form hosted on Stripe.

[Stripe Checkout](/payments/checkout)

Both options are optimized for conversion and SAQ-A eligible, simplifying PCI compliance.

[PCI compliance](/security/guide#validating-pci-compliance)

Embed the Payment Element

Redirect to Stripe Checkout

You can individually enable or disable payment methods from your payment methods settings. This applies to both Stripe Checkout and the Payment Element. You don’t need to upgrade your integration after you enable a payment method, even if the payment method became available after you installed the Stripe Connector for Adobe Commerce.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

The full list of supported payment methods is available in the integration options section.

[integration options](/payments/payment-methods/integration-options#payment-method-product-support)

To optimize conversions, Stripe Checkout and the Payment Element display payment methods dynamically to adapt to the current session. The customer device, shipping country, cart currency and even cart contents are taken into consideration to select and sort payment methods for conversion. For logged in customers, we display their saved payment methods first to enable faster checkout.

You can customize the look and feel of the Payment Element by overriding the getElementOptions() PHP method under Model/Ui/ConfigProvider.php. To do this, implement an afterMethod plugin.

[afterMethod plugin](https://developer.adobe.com/commerce/php/development/components/plugins/#after-methods)

Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.

[Radar](/radar)

[Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)

If Radar detects a high-risk payment, it might place it under review with an Elevated risk status. If you want to automatically decline charges, you can create a custom rule in your Radar settings. Any orders that go into manual review are automatically placed on hold in Adobe Commerce. You can configure what orders to send to manual review in your Radar rules:

[Radar rules](https://dashboard.stripe.com/test/settings/radar/rules)

Stripe Radar can detect and prevent fraud for orders placed on your site

If you think that an order isn’t fraudulent, you can click Unhold on the order page. This allows you to fulfill the order normally.

To test a fraudulent payment, switch the module to test mode and place an order using the card number 4000 0000 0000 9235.

The Stripe Connector for Adobe Commerce is SCA-ready and includes 3D Secure 2 support for customer authentication.

[SCA-ready](/strong-customer-authentication)

[3D Secure 2](https://stripe.com/guides/3d-secure-2)

By default, customers only see 3D Secure authentication when their bank requires it, so your checkout conversion isn’t negatively affected. In compliance with the Strong Customer Authentication regulation, Stripe displays the 3D Secure authentication flow automatically whenever required by SCA:

[Strong Customer Authentication](/strong-customer-authentication)

Stripe provides a 3D Secure test payment page in test mode

You can configure your 3DS preferences in your Radar rules.

[Radar rules](https://dashboard.stripe.com/test/settings/radar/rules)

To test the authentication flow, switch the module to test mode and place an order using any of the test card numbers.

[test card numbers](/payments/3d-secure/authentication-flow#three-ds-cards)

## Grow your recurring revenue with subscriptions

Our module offers a subscription engine for Adobe Commerce that includes the following features:

- Configurable and customer-customizable subscription products in your catalog pages.

- Trial plans or the ability to collect initial fees with each subscription purchase.

- Customer notifications and the collection of new payment details from Stripe Billing when subscription payments fail.

- Reduced churn because Stripe works directly with card networks to automatically update payment details with new card numbers or expiry dates.

## Translations for multi-language websites

If you configure your locale or currency for the first time, make sure to flush the configuration cache.

[flush the configuration cache](https://devdocs.magento.com/guides/v2.3/config-guide/cli/config-cli-subcommands-cache.html#config-cli-subcommands-cache-clean)

The module contains a translation file that you can use to configure a multi-language Adobe Commerce site:

To create a translation file for a different language, copy this file to:

Make sure to replace languagecode_COUNTRYCODE with the locale code for your target language. This is the same language you’ve selected under System > Configuration > General > Locale Options > Locale.

After you copy the file, you can replace the second string on each row with a translation of the first string. You don’t need to do anything else for translations.

## See also

- Installing the Stripe Connector for Adobe Commerce

[Installing the Stripe Connector for Adobe Commerce](/connectors/adobe-commerce/install)

- Configuring the Stripe Connector for Adobe Commerce

[Configuring the Stripe Connector for Adobe Commerce](/connectors/adobe-commerce/configuration)

- Using subscriptions

[Using subscriptions](/connectors/adobe-commerce/subscriptions)

- Using the Adobe Commerce admin panel

[Using the Adobe Commerce admin panel](/connectors/adobe-commerce/admin)

- Building a custom storefront

[Building a custom storefront](/connectors/adobe-commerce/custom-storefront)

- Troubleshooting

[Troubleshooting](/connectors/adobe-commerce/troubleshooting)
