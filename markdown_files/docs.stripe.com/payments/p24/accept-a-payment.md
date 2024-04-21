htmlAccept a Przelewy24 payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fp24%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fp24%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)[Przelewy24](/docs/payments/p24)# Accept a Przelewy24 payment

Learn how to accept Przelewy24 (P24), the most popular payment method in Poland.WebMobilePrebuilt checkout pageEmbedded ElementCautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Przelewy24 is a single use payment method where customers are required to authenticate their payment. Customers pay with Przelewy24 by redirecting from your website, authorizing the payment, then returning to your website where you get immediate notification on whether the payment succeeded or failed.

[Determine compatibility](#compatibility)Supported business locations: Europe, US, CA, NZ, SG, HK, JP, AU, MX

Supported currencies: eur, pln

Presentment currencies: eur, pln

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Przelewy24 payments:

- [Prices](/api/prices)for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring[subscription](/billing/subscriptions/creating)plans are not supported).

[Accept a payment](#accept-a-payment)NoteThis guide builds on the foundational accept a payment Checkout integration.

Use this guide to learn how to enable Przelewy24—it shows the differences between accepting a card payment and using Przelewy24.

### Enable Przelewy24 as a payment method

When creating a new Checkout Session, you need to:

1. Add`p24`to the list of`payment_method_types`.
2. Make sure all your`line_items`use the same currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'p24'],
  line_items: [{
    price_data: {
      currency: 'usd',
      # To accept `p24`, all line items must have currency: eur, pln
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

[Test your integration](#test-integration)When testing your Checkout integration, select Przelewy24 as the payment method and click the Pay button.

[Handle refunds and disputes](#refunds-and-disputes)The refund period for Przelewy24 is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [After the payment](/payments/checkout/fulfill-orders)
- [Customizing Checkout](/payments/checkout/customization)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Handle refunds and disputes](#refunds-and-disputes)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`