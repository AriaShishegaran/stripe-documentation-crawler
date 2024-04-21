htmlStripe Connector for Shopware 6 | Stripe Documentation[Skip to content](#main-content)Shopware 6[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fshopware6)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fshopware6)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)# Stripe Connector for Shopware 6

Learn how to help your customers check out and accept payments using the Shopware 6 connector.Use the Stripe Connector for Shopware 6 to build an integration that allows you to accept payments in many countries. The connector integrates Stripe Elements, an embedded UI component that lets you accept more than 25 payment methods with a single integration and that comes with the following features:

- Built-in conversion logic: Increase conversion by reducing user friction and errors with features such as address auto-complete, real-time card validation, descriptive error messages, and third-party auto-fill.
- Global payment conversion: Dynamically display the right language, currency, and payment methods most likely to improve conversion. Stripe supports over 25 languages, 135 currencies, and 25 payment methods.
- Authorize payments and capture later: Stripe supports separate card authorization and capture, which lets you collect card information, verify sufficient funds, and then capture the total amount after shipping.
- Works with any device: Provide customers with a responsive checkout across mobile, tablet, and desktop, and offer Apple Pay and Google Pay out of the box.

## Global payment methods

You can turn on payment methods from the Stripe Dashboard. To increase conversion, Stripe dynamically displays the most relevant payment methods based on your customer’s location and device. As Stripe adds new payment methods, you can turn them on without needing additional integrations. Use the connector to enable the following payment methods:

- Credit and debit cards: Visa, Mastercard, American Express, China UnionPay, Discover and Diners, Japan Credit Bureau (JCB), Cartes Bancaires
- Mobile wallets: Apple Pay, Google Pay, WeChat Pay, AliPay, GrabPay
- Buy now, pay later and installments: Klarna, Afterpay (Clearpay)
- Bank debits: ACH, SEPA debit, BECS direct debit, pre-authorized debit in Canada
- Other popular payment methods: Bancontact, EPS, Giropay, iDEAL, Przelewy24, SOFORT, FPX, Boleto, OXXO

## See also

- [Install the connector](/connectors/shopware6/installation)
- [Configure the connector](/connectors/shopware6/configuration)
- [Stripe Connector for Shopware 6 FAQ](https://support.stripe.com/questions/shopware)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Global payment methods](#global-payment-methods)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`