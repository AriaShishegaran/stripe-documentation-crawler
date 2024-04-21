# Accept a PayNow payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

PayNow is a single-use payment method. Customers pay with PayNow by scanning the QR code that they see during Checkout. Completing the payment redirects customers back to your website.

[single-use](/payments/payment-methods#usage)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: SG

Supported currencies: sgd

Presentment currencies: sgd

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support PayNow payments:

- Prices for all line items must be in the same currency, and must be in sgd.

[Prices](/api/prices)

- You can only use one-time line items (PayNow Checkout Sessions don’t support recurring subscription plans).

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?integration=checkout)

This guides you through enabling PayNow and shows the differences between accepting a card payment and using PayNow.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add paynow to the list of payment_method_types

- Make sure all your line_items use the same currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select PayNow as the payment method and click the Generate QR code button, which creates and renders a QR code.

In test mode, scan the QR code with a QR code scanning application on your mobile device. The QR code payload contains a URL which brings you to a Stripe-hosted PayNow test payment page where you can either authorize or fail the test payment.

In live mode, you will be able to scan the QR code using a preferred banking app or payment app that supports PayNow.

## See also

- After the payment

[After the payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
