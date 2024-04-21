htmlAccept a BECS Direct Debit payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fau-becs-debit%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fau-becs-debit%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[BECS Direct Debit in Australia](/docs/payments/au-becs-debit)# Accept a BECS Direct Debit payment

Learn to accept BECS Direct Debit payments in Australia.WebMobilePrebuilt checkout pageEmbedded Element### How it works

See the BECS Direct Debit overview to learn more about this payment method.

Stripe users in Australia can use the Payment Element and a Payment Intent to initiate BECS Direct Debit payments from customers with an AU bank account.

CautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Determine compatibility](#compatibility)Customer Geography: Australia

Supported currencies: aud

Presentment currencies: aud

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

To support BECS Direct Debit payments in Checkout, Prices for all line items must be expressed in Australian dollars (currency code aud).

[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

Use this guide to learn how to enable BECS Direct Debit—it shows the differences between accepting a card payment and using BECS Direct Debit.

### Enable BECS Direct Debit as a payment method

When creating a new Checkout Session, you need to:

1. Add`au_becs_debit`to the list of`payment_method_types`
2. Make sure all your`line_items`use the`aud`currency

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'au_becs_debit'],
  line_items: [{
    price_data: {
      currency: 'usd',
      # To accept `au_becs_debit`, all line items must have currency: aud
      currency: 'aud',
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

Because BECS Direct Debit is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[Test your integration](#test-integration)NoteYou’ll want to use the BECS Direct Debit test numbers when testing your Checkout integration with BECS Direct Debit.

There are several test numbers you can use to make sure your integration is ready for production.

BSB NumberAccount NumberDescription`000-000``000123456`The PaymentIntent status transitions from`processing`to`succeeded`. The mandate status remains`active`.`000-000``900123456`The PaymentIntent status transitions from`processing`to`succeeded`(with a three-minute delay). The mandate status remains`active`.`000-000``111111113`The PaymentIntent status transitions from`processing`to`requires_payment_method`with an`account_closed`failure code. The mandate status becomes`inactive`.`000-000``111111116`The PaymentIntent status transitions from`processing`to`requires_payment_method`with a`no_account`failure code. The mandate status becomes`inactive`.`000-000``222222227`The PaymentIntent status transitions from`processing`to`requires_payment_method`with a`refer_to_customer`failure code. The mandate status remains`active`.`000-000``922222227`The PaymentIntent status transitions from`processing`to`requires_payment_method`with a`refer_to_customer`failure code (with a three-minute delay). The mandate status remains`active`.`000-000``333333335`The PaymentIntent status transitions from`processing`to`requires_payment_method`with a`debit_not_authorized`failure code. The mandate status becomes`inactive`.`000-000``666666660`The PaymentIntent status transitions from`processing`to`succeeded`, but a dispute is immediately created.[Handle refunds and disputes](#refunds-and-disputes)The refund period for BECS Direct Debit is up to 90 days after the original payment.

Customers can dispute a payment through their bank up to 7 years after the original payment and there is no appeals process.

Learn more about BECS Direct Debit disputes.

## See also

- [More about BECS Direct Debit](/payments/au-becs-debit)
- [Managing mandates](/payments/au-becs-debit#mandates)
- [After the payment](/payments/checkout/fulfill-orders)
- [Customizing Checkout](/payments/checkout/customization)
- [Save BECS Direct Debit details for future payments](/payments/au-becs-debit/set-up-payment)
- [Connect platforms using the Payment Methods API](/payments/payment-methods/connect)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Handle refunds and disputes](#refunds-and-disputes)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`