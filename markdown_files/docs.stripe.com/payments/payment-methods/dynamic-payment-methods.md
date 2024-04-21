htmlDynamic payment methods | Stripe Documentation[Skip to content](#main-content)Dynamic payment methods[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fdynamic-payment-methods)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fdynamic-payment-methods)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Dynamic payment methods

Simplify your payment methods code by dynamically ordering and displaying payment methods.Dynamic payment methods is part of the default Stripe integration and enables you to configure payment methods settings from the Dashboard—no code required. When you use dynamic payment methods in a Payment Element or Checkout integration, Stripe handles the logic for dynamically displaying the most relevant eligible payment methods to each customer to maximize conversion. Dynamic payment methods also unlocks customization features to help you customize and experiment with payment methods.

Use dynamic payment methods to:

- Turn on and manage most payment methods in the Dashboard
- Eliminate the need to specify eligibility requirements for individual payment methods
- Dynamically order eligible payment methods to maximize conversion based on factors such as customer device, location, and local currency
- Set rules when payment methods are shown to buyers
- Run A/B Tests for new payment methods before rolling them out to buyers

## Integration options

Use Checkout or Payment Element with dynamic payment methods to have Stripe handle the logic for displaying eligible payment methods in your frontend for each transaction. If you have a platform account, follow our Connect integration.

### Migrate to dynamic payment methods

## Dashboard-based customization features

Access the following features with dynamic payment methods to control how and when payment methods render.

FeatureDescription[Payment method rules](/payments/payment-method-rules)Customize how you display payment methods by setting targeting parameters based on amount or the buyer’s location.[A/B test payment methods](/payments/a-b-testing)Turn on payment methods for a percentage of traffic, run an experiment, and see the resulting impact on conversion rate, average order value, and shift in volume from other payment methods.[Payment method configurations](/payments/payment-method-configurations)Create different sets of payment methods for different checkout scenarios using complex logic, such as only showing specific payment methods for one-time purchases and another set for recurring purchases.[Embed the Payment methods settings component](/connect/embed-payment-method-settings)Embed a payment method settings page directly into your website to allow your users to manage their payment methods.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Integration options](#integrate)[Dashboard-based customization features](#customization-features)Products Used[Payments](/payments)[Elements](/payments/elements)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`