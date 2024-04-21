# Accept a PayPal payment

PayPal is a reusable, immediate notification payment method where customers are required to authenticate their payment. To make a payment using PayPal, customers are redirected from your website to PayPal where they choose a funding source (for example, PayPal wallet, linked card, or buy-now-pay-later, provided by PayPal) and authenticate the payment. Upon completion of the authorization process, the customer is redirected back to your website.

[reusable](/payments/payment-methods#usage)

[immediate notification](/payments/payment-methods#payment-notification)

Stripe Checkout and the Express Checkout Element both support the standalone PayPal button. This button allows a customer to reuse their shipping and billing information previously saved at PayPal so that they don’t have to enter it again at the time of a purchase. If they click this button, a customer can approve the payment from a pop-up (?window/modal/redirected/embedded) so they remain on your website throughout the entire checkout process. Stripe only supports one-off (non-recurring payments) PayPal payments through this button.

[Express Checkout Element](/elements/express-checkout-element)



Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Stripe Checkout shows PayPal either as a standard payment method or as a standalone button, depending on which option is more likely to increase the conversion rate.

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: Europe, GB

Supported currencies: eur, gbp, usd, aud, cad, hkd, czk, dkk, nok, pln, sek, chf, sgd, nzd

Presentment currencies: eur, gbp, usd, aud, cad, hkd, czk, dkk, nok, pln, sek, chf, sgd, nzd

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support PayPal payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable PayPal—it shows the differences between accepting a card payment and using PayPal.

When creating a new Checkout Session, do the following:

[Checkout Session](/api/checkout/sessions)

- Add paypal to the list of payment_method_types.

- Make sure all your line_items use the same currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

You don’t need to connect your PayPal business account to test the integration. However, make sure to connect your PayPal and Stripe accounts when you’re ready to activate live mode payments.

[activate live mode payments](/payments/paypal/connect-your-paypal-account)

When testing your Checkout integration, select PayPal as the payment method and click Pay.

To simulate the most common integration and failure scenarios for PayPal payments, pass email values that match the patterns described in these test scenarios.

[test scenarios](/payments/paypal/accept-a-payment?platform=web&ui=stripe-hosted#test-scenarios)

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

Learn more about PayPal disputes and refunds.

[disputes](/payments/paypal#disputed-payments)

[refunds](/payments/paypal#refunds)
