# Cash App Pay payments

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

This guides you through enabling Cash App Pay on Checkout, our hosted checkout form, and shows the differences between accepting a card payment and a Cash App Pay payment.

[Checkout](/payments/checkout)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: US

Supported currencies: usd

Presentment currencies: usd

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support Cash App Pay payments:

- Prices for all line items must be expressed in USD.

[Prices](/api/prices)

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?integration=checkout)

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add cashapp to the list of payment_method_types

- Make sure all your line_items use the usd currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#web-test-integration)

## Test your integration

To test your integration, choose Cash App Pay as the payment method and tap Pay. In test mode, this redirects you to a test payment page where you can approve or decline the payment.

In live mode, tapping Pay redirects you to the Cash App mobile application—you don’t have the option to approve or decline the payment within Cash App. The payment is automatically approved after the redirect.

## See also

- After the payment

[After the payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
