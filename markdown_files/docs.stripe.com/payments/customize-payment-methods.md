htmlCustomize payment methods | Stripe Documentation[Skip to content](#main-content)Customize payment methods[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomize-payment-methods)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomize-payment-methods)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)[Payment Element](/docs/payments/payment-element)# Customize payment methods

Choose how the Payment Element displays payment methods.The Payment Element supports many payment methods. It displays the payment methods you have enabled, hides any that won’t work for the current transaction, and sorts them dynamically for the best conversion rates.

You can customize its behavior in these ways:

- [Enable different payment methods](#enable-different-payment-methods).
- [Sort payment methods](#sort-payment-methods)differently than the default.

## Enable different payment methods

You can specify Dynamic payment methods to enable different payment methods by selecting them in the Dashboard. Stripe enables this functionality by default in the latest version of the API. This allows Stripe to pull your payment method preferences from the Dashboard to dynamically show the most relevant payment methods to your customers. Alternatively, you can list payment methods manually using payment method types.

There’s one situation where the Payment Element overrides your choice. It hides payment methods that don’t support the current payment. For instance, in a recurring payment for 10 JPY, the Payment Element hides methods that don’t support JPY or recurring payments.

## Sort payment methods

By default, the Payment Element uses dynamic ordering to optimize which payment methods appear for each user. With the paymentMethodOrder parameter, you can override the default order for payment methods in the Payment Element, including Apple Pay and Google Pay.

Payment methods that you specify in paymentMethodOrder are shown first, followed by any additional payment methods. If you specify payment method types that Stripe wouldn’t show, they’re ignored.

`elements.create('payment', {
  paymentMethodOrder: ['apple_pay', 'google_pay', 'card', 'klarna']
});`You can include Apple Pay (apple_pay) and Google Pay (google_pay) when setting the order for payment methods in addition to a full list of payment method types.

Regional considerationsFinlandSwedenRegulations in Finland and Sweden require that debit payment methods must be presented before credit payment methods at checkout in those countries.

## Filter card brands

When your customers pay with a card through the Payment Element, you can control which card brands you accept and which ones you don’t. This applies to both the card input field and Apple Pay or Google Pay.

NoteWant to sign up for our beta? Click here!

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Enable different payment methods](#enable-different-payment-methods)[Sort payment methods](#sort-payment-methods)[Filter card brands](#filter-card-brands)Products Used[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`