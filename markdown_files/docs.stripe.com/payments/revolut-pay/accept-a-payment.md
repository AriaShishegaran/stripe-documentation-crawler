htmlAccept a payment with Revolut Pay | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Frevolut-pay%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Frevolut-pay%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[Revolut Pay](/docs/payments/revolut-pay)# Accept a payment with Revolut Pay

Learn about Revolut Pay, a digital wallet payment method used in the United Kingdom and the European Union.WebMobilePrebuilt checkout pageCustom payment flowDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Revolut Pay is a reusable payment method where customers are required to authenticate their payment. Customers pay by being redirected from your website or app, authorizing the payment with Revolut Pay, then returning to your website or app. You get immediate notification of whether the payment succeeded or failed.

[Determine compatibility](#compatibility)To support Revolut Pay payments, a Checkout Session must satisfy all of the following conditions:

- [Prices](/api/prices)for all line items must be in the same currency.  - If you have line items in different currencies, create separate Checkout Sessions for each currency.



Recurring subscription plans are supported.

[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

This guide describes how to enable Revolut Pay and shows the differences between accepting a card payment and using Revolut Pay.

### Enable Revolut Pay as a payment method

When creating a new Checkout Session, you need to:

1. Add`revolut_pay`to the list of`payment_method_types`.
2. Make sure all`line_items`use the same currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'revolut_pay'],
  line_items: [{
    price_data: {
      currency: 'usd',
      # To accept `revolut_pay`, all line items must have currency: eur, gbp
      currency: 'gbp',
      product_data: {
        name: 'T-shirt',
      },
      unit_amount: 2000,
    },
    quantity: 1,
  }],
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`### Fulfill your orders

After accepting a payment, learn how to fulfill orders.

[Test your integration](#test-integration)When testing your Checkout integration, select Revolut Pay as the payment method and click the Pay button.

![](https://b.stripecdn.com/docs-statics-srv/assets/merchant_checkout_revolut_pay_visible.de0ad2427b3548dda777da6fc9b421dc.png)

## See also

- [More about Revolut Pay](/payments/revolut-pay)
- [After the Payment](/payments/checkout/fulfill-orders)
- [Customizing Checkout](/payments/checkout/customization)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`