# Accept a GrabPay payment

Subscriptions and using GrabPay for future payments aren’t currently supported. Reach out to Stripe support for any support queries on these features.

[Subscriptions](/billing/subscriptions/creating)

[Stripe support](https://support.stripe.com/contact)

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

GrabPay is a single-use payment method. Customers pay with GrabPay by redirecting from your website to GrabPay to authorize the payment. After that, they will automatically be redirected back to your website. You will get immediate notification on whether the payment succeeded or failed.

[single-use](/payments/payment-methods#usage)

[immediate notification](/payments/payment-methods#payment-notification)

Assets such as logos and payment buttons are provided in the branding guidelines section.

[branding guidelines](/payments/grabpay#branding-guidelines)

[Determine compatibility](#compatibility)

## Determine compatibility

A Checkout Session must satisfy all of the following conditions to support GrabPay payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- You can only use one-time line items (recurring subscription plans are not supported).

[subscription](/billing/subscriptions/creating)

- The sgd currency is supported for businesses based in Singapore.

- The myr currency is supported for businesses based in Malaysia.

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?integration=checkout)

This guides you through enabling GrabPay and shows the differences between accepting a card payment and using GrabPay.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add grabpay to the list of payment_method_types

- Make sure all your line_items use the same currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select GrabPay as the payment method and click the Pay button.

## See also

- After the payment

[After the payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
