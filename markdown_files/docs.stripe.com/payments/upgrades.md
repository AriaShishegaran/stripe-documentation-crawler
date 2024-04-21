htmlUpgrade your integration | Stripe Documentation[Skip to content](#main-content)Upgrade your integration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fupgrades)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fupgrades)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)# Upgrade your integration

Increase conversion and get access to new features by upgrading your integration.Discover the recommended options for upgrading both your entire payments integration, and individual features. For a comprehensive list of changes to the API, see API upgrades.

## Payment integration upgrades

Take advantage of new features by upgrading your existing integration.

Legacy integrationRecommended integrationWhy you should upgradeUpgrade path[Card Element](/payments/payment-card-element-comparison)[Payment Element](/payments/payment-element)- Use a single UI component to present over 100 payment methods and build a customizable checkout.
- Access the latest compatible features.
- Have Stripe handle the presentment logic using various factors, such as location, currency, and success metrics.
- Customize payment method preferences in the Dashboard.

[Migrate to the Payment Element](/payments/payment-element/migration)Legacy Checkout- [Checkout](/payments/checkout/how-checkout-works)
- [Payment Links](/payment-links)

- Checkout:

  - Checkout offers a prebuilt payment form to securely accept online payments.
  - Embed Checkout on your site or redirect to a Stripe-hosted Checkout page.
  - Checkout gives you access to additional features, such as[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)and[Adaptive Pricing](/payments/checkout/adaptive-pricing).


- Payment Links:

  - Accept a payment or sell subscriptions without building additional standalone websites or applications.
  - Share a link as many times as you want on social media, in emails, or on your website.
  - Access[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)from the Dashboard.



[Migrate to Checkout](/payments/checkout/migration)[Client-only Checkout](/payments/checkout/client)- [Create a payment link](/payment-links/create)
- [Create an embeddable buy button](/payment-links/buy-button)
- [Embed a pricing table](/payments/checkout/pricing-table)

- Start accepting payments without writing any code.
- Replace your existing integration by adding a buy button or pricing table onto your website with a simple script tag, or use payment links that you can present to your customers.

[Migrate to a no-code solution](/no-code/get-started#get-retain-subscribers)[Payment request button](/stripe-js/elements/payment-request-button)[Express checkout element](/elements/express-checkout-element)- Accept additional payment method options, such as[Apple pay](/apple-pay),[Amazon Pay](/payments/amazon-pay),[Google Pay](/google-pay),[Link](/payments/link), and[PayPal](/payments/paypal).
- Display multiple payment method buttons at the same time.
- For more details, see the[Express Checkout Element comparison guide](/elements/express-checkout-element/comparison).

[Migrate to the Express Checkout Element](/elements/express-checkout-element/migration)## Feature upgrades

We recommend upgrading these features to enhance your checkout process.

Integration featureFeature upgradeWhy you should upgradeUpgrade path[Manual payment methods](/payments/payment-methods/integration-options#listing-payment-methods-manually)[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)- Manage payment methods from the Dashboard.
- Rely on Stripe to present eligible payment methods for each transaction using factors such as transaction amount, currency, payment flow, and the payment method preferences you set in the Dashboard.

[Payment Links, Checkout, or Payment Element](/payments/payment-methods/dynamic-payment-methods)[Manual payment methods](/payments/payment-methods/integration-options#listing-payment-methods-manually)in a[Connect integration](/connect/creating-a-payments-page)[Dynamic payment methods](/connect/dynamic-payment-methods)- Manage payment methods from the Dashboard.
- Rely on Stripe to present eligible payment methods for each transaction using factors such as transaction amount, currency, payment flow, and the payment method preferences you set in the Dashboard.

[Connect dynamic payment methods](/connect/dynamic-payment-methods)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment integration upgrades](#payment-integration-upgrades)[Feature upgrades](#feature-upgrades)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`