htmlAccept a payment with Alma | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Falma%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Falma%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)[Alma](/docs/payments/alma)# Accept a payment with AlmaBeta

Learn how to setup your integration with Alma.Interested in getting early access to Alma?To learn more or get early access, enter your email address below. We’ll work with you to determine your eligibility, and from there, add you to the waitlist.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.WebMobilePrebuilt checkout pageCustom payment flowDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Alma is a single-use payment method where customers choose to pay between 2, 3, or 4 installments. Customers are redirected from your website or app, authorize the payment with Alma, then return to your website or app. You get immediate notification of whether the payment succeeded or failed.

[Determine compatibility](#compatibility)To support Alma payments, a Checkout Session must satisfy all of the following conditions:

- [Prices](/api/prices)for all line items must be in the same currency.  - If you have line items in different currencies, create separate Checkout Sessions for each currency.



[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

This guide describes how to enable Alma and shows the differences between accepting a card payment and using Alma.

### Enable Alma as a payment method

When creating a new Checkout Session, you need to:

1. Add`alma`to the list of`payment_method_types`.
2. Make sure all`line_items`use the same currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'alma'],
  line_items: [{
    price_data: {
      currency: 'usd',
      # To accept `alma`, all line items must have currency: eur
      currency: 'eur',
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

[Test your integration](#test-integration)When testing your Checkout integration, select Alma as the payment method and click the Pay button.

![](https://b.stripecdn.com/docs-statics-srv/assets/merchant_checkout_alma_visible.267e88e1e3ef1ac2708a9f5d39292f78.png)

## See also

- [More about Alma](/payments/alma)
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