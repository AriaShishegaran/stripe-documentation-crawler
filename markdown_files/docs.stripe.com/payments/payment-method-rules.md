htmlPayment method rules | Stripe Documentation[Skip to content](#main-content)Payment method rules[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-method-rules)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-method-rules)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Payment method rules

Control when payment methods are available to your buyers.Payment method rules allow you to set conditions on payment methods directly from the Dashboard without any custom logic or code. Rules allow you to:

- Hide or show a payment method if the order amount is over or under a certain amount
- Hide or show a payment method for buyers in certain countries or using certain currencies

## Payment method rules considerations

Non-card payment methods can help offer improved unit economics compared to cards and they often drive higher AOV and conversion rates.

When you turn on these payment methods, you might want to apply specific business logic to control when payment methods are available to your buyers. With payment method rules, you can apply these insights directly in Dashboard—no code required.

Payment method rules is compatible with Stripe A/B Testing. This allows you to run A/B tests using the targeting criteria you select or test additional criteria. For example, you can test the impact of only showing a specific payment method when the price is greater than a certain dollar amount.

## Before you begin

- You must use either the Stripe[Payment Element](/payments/payment-element)or[Checkout](/payments/checkout).
- You must use[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)to enable additional payment methods from the Stripe Dashboard, which won’t require any code changes.  - To set up dynamic payment methods for direct users, see the[payment method integration](/payments/payment-methods/dynamic-payment-methods)guide.
  - ConnectTo set up dynamic payment methods for Connect platforms, see[Upgrading to dynamic payment methods](/connect/dynamic-payment-methods).



[Set rule conditions](#set-rule-conditions)1. In your Dashboard, go to[Payment methods settings](https://dashboard.stripe.com/test/settings/payment_methods).
2. In the payment method row, selectCreate custom rules.![Klarna Row](https://b.stripecdn.com/docs-statics-srv/assets/pmt-klarna-row.931f50a1bd9a4d872657f0372dead2d8.png)


3. Set custom rules (for example, a new minimum of 100 USD for Klarna), then selectApply Overrides.The configured payment method now has aCustomizedtag. A customized payment method appears only in Checkout or Payment Element sessions that meet its targeting criteria.

![A checkout page showing Klarna.](https://b.stripecdn.com/docs-statics-srv/assets/pmt-checkout-klarna-present.fab9fed6ec4dfc1e187b38beb944fc65.png)

Before

![A checkout page with Klarna hidden.](https://b.stripecdn.com/docs-statics-srv/assets/pmt-checkout-klarna-hidden.e1d585ab6318861be8aa813cdde91fb4.png)

After

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment method rules considerations](#payment-method-rules-considerations)[Before you begin](#before-you-begin)[Set rule conditions](#set-rule-conditions)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`