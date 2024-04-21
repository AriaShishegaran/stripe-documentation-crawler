htmlAccept a Sofort payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsofort%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsofort%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)[Sofort](/docs/payments/sofort)# Accept a Sofort payment

Learn how to accept Sofort, a common payment method in Europe.WarningOur financial partners are in the process of deprecating Sofort. New businesses can’t accept Sofort payments. For more information read our support page.

WebMobilePrebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

NoteSOFORT is a delayed notification payment method, which means that funds are not immediately available after payment. A payment typically takes 2 to 14 business days to arrive in your account.

Customers pay with SOFORT by redirecting away from the Checkout Session to their bank, sending you payment, and then returning to Checkout. They are then redirected back to your site.

[Determine compatibility](#compatibility)Supported business locations: Europe, US, CA, NZ, SG, HK, JP, AU, MX

Supported currencies: eur

Presentment currencies: eur

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support SOFORT payments:

- [Prices](/api/prices)for all line items must be expressed in Euro (currency code`eur`).

[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

Use this guide to learn how to enable SOFORT—it shows the differences between accepting a card payment and using SOFORT.

### Enable SOFORT as a payment method

When creating a new Checkout Session, you need to:

1. Add`sofort`to the list of`payment_method_types`.
2. Make sure all your`line_items`use the`eur`currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'sofort'],
  line_items: [{
    price_data: {
      currency: 'usd',
      # To accept `sofort`, all line items must have currency: eur
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

Because SOFORT is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[Test your integration](#test-integration)When testing your Checkout integration, select SOFORT as the payment method and click the Pay button.

[Handle refunds and disputes](#refunds-and-disputes)The refund period for SOFORT is up to 180 days after the original payment.

There is no dispute process–customers authenticate with their bank.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Handle refunds and disputes](#refunds-and-disputes)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`