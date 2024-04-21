htmlAccept a PayPal payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[PayPal](/docs/payments/paypal)# Accept a PayPal payment

Learn how to accept PayPal payment, a digital wallet popular with businesses in Europe.PayPal is a reusable, immediate notification payment method where customers are required to authenticate their payment. To make a payment using PayPal, customers are redirected from your website to PayPal where they choose a funding source (for example, PayPal wallet, linked card, or buy-now-pay-later, provided by PayPal) and authenticate the payment. Upon completion of the authorization process, the customer is redirected back to your website.

Stripe Checkout and the Express Checkout Element both support the standalone PayPal button. This button allows a customer to reuse their shipping and billing information previously saved at PayPal so that they don’t have to enter it again at the time of a purchase. If they click this button, a customer can approve the payment from a pop-up (?window/modal/redirected/embedded) so they remain on your website throughout the entire checkout process. Stripe only supports one-off (non-recurring payments) PayPal payments through this button.



WebMobilePrebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Stripe Checkout shows PayPal either as a standard payment method or as a standalone button, depending on which option is more likely to increase the conversion rate.

[Determine compatibility](#compatibility)Supported business locations: Europe, GB

Supported currencies: eur, gbp, usd, aud, cad, hkd, czk, dkk, nok, pln, sek, chf, sgd, nzd

Presentment currencies: eur, gbp, usd, aud, cad, hkd, czk, dkk, nok, pln, sek, chf, sgd, nzd

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support PayPal payments:

- [Prices](/api/prices)for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

Use this guide to learn how to enable PayPal—it shows the differences between accepting a card payment and using PayPal.

### Enable PayPal as a payment method

When creating a new Checkout Session, do the following:

1. Add`paypal`to the list of`payment_method_types`.
2. Make sure all your`line_items`use the same currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'paypal'],
  line_items: [{
    price_data: {
      currency: 'usd',
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

[Test your integration](#test-integration)You don’t need to connect your PayPal business account to test the integration. However, make sure to connect your PayPal and Stripe accounts when you’re ready to activate live mode payments.

When testing your Checkout integration, select PayPal as the payment method and click Pay.

To simulate the most common integration and failure scenarios for PayPal payments, pass email values that match the patterns described in these test scenarios.

### Test scenarios

Email patternScenarioExplanation`.*payee_account_restricted@.*`Merchant account restrictedCapturing or authorizing a payment fails with a`payment_method_unexpected_state`error if your merchant account is restricted by PayPal. Provide an email matching this pattern at time of authorization to fail the authorization.`.*transaction_refused@.*`Transaction refusedCapturing a payment fails with a`payment_method_provider_decline`error if the transaction is refused by PayPal.`.*instrument_declined@.*`Payment instrument declinedCapturing a payment fails with a`payment_method_provider_decline`error if the instrument presented was either declined by the processor or bank, or it can’t be used for this payment.`.*lost_dispute@.*`Lost disputeOn capture, the payment intent first succeeds only to be disputed. The dispute created is already lost and the merchant can’t submit evidence on the Stripe Dashboard.`.*authorization_expired@.*`Manually capturing an authorized paymentCapturing an authorized payment fails with a`capture_charge_authorization_expired`error if the authorization has already expired.[Handle refunds and disputes](#refunds-and-disputes)Learn more about PayPal disputes and refunds.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Handle refunds and disputes](#refunds-and-disputes)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`