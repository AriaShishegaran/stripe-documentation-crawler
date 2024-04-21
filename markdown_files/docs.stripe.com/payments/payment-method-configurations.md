htmlPayment method configurations | Stripe Documentation[Skip to content](#main-content)Payment method configurations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-method-configurations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-method-configurations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Payment method configurations

Create different sets of payment methods to display to customers based on specific checkout scenarios.Payment method configurations allows dynamic payment method users to display different sets of payment methods to customers for specific checkout scenarios.

You can create a configuration to:

- Display a unique set of payment methods for certain products
- Enable a set of payment methods for your one-time payment checkout flow and a different set of payment methods for your subscription checkout flow
- ConnectOffer connected accounts access to additional payment methods for a different subscription fee

After you create a payment method configuration, you can toggle each payment method on or off for a given scenario directly in Dashboard—no code required. Then at checkout, select which configuration you want to use. Stripe ranks the payment methods that are enabled within that configuration to optimize for conversion.

## Before you begin

- You must use either the Stripe[Payment Element](/payments/payment-element)or[Checkout](/payments/checkout).
- You must use[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)to enable additional payment methods from the Stripe Dashboard, which won’t require any code changes.  - To set up dynamic payment methods for direct users, see the[payment method integration](/payments/payment-methods/dynamic-payment-methods)guide.
  - ConnectTo set up dynamic payment methods for Connect platforms, see[Upgrading to dynamic payment methods](/connect/dynamic-payment-methods).



[Create a payment method configuration](#create-payment-method-configuration)By default, you have one payment method configuration called Default Config. You can create additional payment method configurations using both the Stripe Dashboard and the API.

DashboardAPI1. In your Dashboard, go to[Payment methods settings](https://dashboard.stripe.com/test/settings/payment_methods).
2. In theConfiguration Managementsection, click the overflow menu (), then selectCreate a configuration.
3. Give your new configuration a name.
4. ClickSave configuration.

![Payment method configuration page](https://b.stripecdn.com/docs-statics-srv/assets/payment-method-configurations.a766550ad4dd95854a7a9b9f178e1d45.png)

The page displays your new configuration. It has a default set of enabled payment methods.

To switch between configurations, use the Select configuration dropdown near the top of the page.

[Enable payment methods](#enable-payment-methods)In the Dashboard, open the configuration and turn on the payment methods that you want to make available to buyers when using that configuration. A buyer sees only payment methods that are turned on and compatible with the payment location and currency.

NoteSome payment methods don’t show edit controls until you expand them.

[Display available payment methods in checkout](#section-4)Copy the configuration ID in the Dashboard from the configuration you want to use in your checkout flow.

If you’re using the deferred intent creation integration path, pass the payment_method_configuration ID when you create your Payment Element component. The Payment Element automatically pulls the payment methods associated with that configuration and ranks them to best convert buyers.

WebiOSAndroid`const options = {
   mode: 'payment',
   amount: 1099,
   currency: 'usd',
   payment_method_configuration: 'pmc_234'
}`If you aren’t using a Payment Element, pass the payment_method_configuration ID when you create a Checkout session.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=payment \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d currency=usd \
  -d payment_method_configuration=pmc_234`To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

[Create a PaymentIntent with the configuration](#create-payment-intent)Create a PaymentIntent on your server using the payment method configuration.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]"=true \
  -d payment_method_configuration=pmc_123`In the latest version of the API, the automatic_payment_methods parameter is optional because it’s enabled by default.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Create a payment method configuration](#create-payment-method-configuration)[Enable payment methods](#enable-payment-methods)[Display available payment methods in checkout](#section-4)[Create a PaymentIntent with the configuration](#create-payment-intent)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`