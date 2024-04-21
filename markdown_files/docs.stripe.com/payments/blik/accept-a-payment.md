htmlBLIK payments | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fblik%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fblik%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)[BLIK](/docs/payments/blik)# BLIK payments

Learn how to accept BLIK, a common payment method in Poland.WebMobilePrebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

BLIK is a single use payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

[Determine compatibility](#compatibility)Supported business locations: AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, US

Supported currencies: pln

Presentment currencies: pln

Payment mode: Yes

Setup mode: Not yet

Subscription mode: Not yet

A Checkout Session must satisfy all of the following conditions to support BLIK payments:

- [Prices](/api/prices)for all line items must be expressed in Złoty (currency code`pln`).

[Accept a payment](#accept-a-payment)NoteThis guide builds on the foundational accept a payment Checkout integration.

Use this guide to learn how to enable BLIK—it shows the differences between accepting a card payment and using BLIK.

### Enable BLIK as a payment method

When creating a new Checkout Session, you need to:

1. Add`blik`to the list of`payment_method_types`.
2. Make sure all your`line_items`use the`pln`currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'blik'],
  line_items: [{
    price_data: {
      currency: 'usd',
      # To accept `blik`, all line items must have currency: pln
      currency: 'pln',
      product_data: {
        name: 'T-shirt',
      },
      unit_amount: 2000,
    },
    quantity: 1,
  }],
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`### What customers see

Inside their Banking app, customers see four lines related to each BLIK transaction:

- If you provided a value for`description`when creating the PaymentIntent, the first two lines display it (max 70 characters).
- If you provided a value for`statement_descriptor`(typically, an order ID), line 3 displays it (max 22 characters).
- The fourth line automatically populates with the URL of your website.

### Fulfill your orders

After accepting a payment, learn how to fulfill orders.

[Test your integration](#test-integration)When testing your Checkout integration, select BLIK as the payment method and click the Pay button.

Use test mode to test a successful payment by entering any 6-digit code (such as 123456) in the payment form.

[Handle refunds and disputes](#refunds-and-disputes)The refund period for BLIK is up to 13 months after the original payment.

Customers can dispute a payment through their bank up to 13 months after the original payment and there’s no appeal process.

Learn more about BLIK disputes.

[OptionalSimulate failures in test mode](#simulate-failures)## See also

- [More about BLIK](/payments/blik)
- [After the Payment](/payments/checkout/fulfill-orders)
- [Customizing Checkout](/payments/checkout/customization)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Handle refunds and disputes](#refunds-and-disputes)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`