htmlAccept a PromptPay payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpromptpay%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpromptpay%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Real-time payments](/docs/payments/real-time)[PromptPay](/docs/payments/promptpay)# Accept a PromptPay payment

Learn how to accept payments with PromptPay, an instant funds transfer service popular in Thailand.Prebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

PromptPay is a single-use payment method where customers pay with PromptPay by scanning the QR code that they see during checkout. Completing the payment redirects customers back to your website.

[Determine compatibility](#compatibility)Supported business locations: TH

Supported currencies: thb

Presentment currencies: thb

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support PromptPay payments:

- [Prices](/api/prices)for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (PromptPay Checkout Sessions don’t support recurring[subscription](/billing/subscriptions/creating)plans).

[Accept a payment](#accept-a-payment)NoteThis guide builds on the foundational accept a payment Checkout integration.

This guides you through enabling PromptPay and shows the differences between accepting a card payment and using PromptPay.

### Enable PromptPay as a payment method

When creating a new Checkout Session, you need to:

1. Add`promptpay`to the list of`payment_method_types`
2. Make sure all your`line_items`use the same currency

[Ruby](#)`Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'
Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['promptpay'],

  # or you can take multiple payment methods with
  # payment_method_types: ['card', 'promptpay', ...]
  line_items: [{
    price_data: {
      currency: 'thb',
      product_data: {
        name: 'เสื้อยืด',
      },
      unit_amount: 1000,
    },
    quantity: 1,
  }],
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`### Fulfill your orders

After accepting a payment, learn how to fulfill orders.

[Test your integration](#test-integration)When testing your Checkout integration, select PromptPay as the payment method and click the Generate QR code button, which creates and renders a QR code.

In test mode, scan the QR code with a QR code scanning application on your mobile device. The QR code payload contains a URL which brings you to a Stripe-hosted PromptPay test payment page where you can either authorize or fail the test payment.

In live mode, you will be able to scan the QR code using a preferred banking app or payment app that supports PromptPay.

## See also

- [After the payment](/payments/checkout/fulfill-orders)
- [Customizing Checkout](/payments/checkout/customization)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`