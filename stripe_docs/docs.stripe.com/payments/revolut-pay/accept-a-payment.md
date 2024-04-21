# Accept a payment with Revolut Pay

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Revolut Pay is a reusable payment method where customers are required to authenticate their payment. Customers pay by being redirected from your website or app, authorizing the payment with Revolut Pay, then returning to your website or app. You get immediate notification of whether the payment succeeded or failed.

[reusable](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[immediate notification](/payments/payment-methods#payment-notification)

[Determine compatibility](#compatibility)

## Determine compatibility

To support Revolut Pay payments, a Checkout Session must satisfy all of the following conditions:

- Prices for all line items must be in the same currency.If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- If you have line items in different currencies, create separate Checkout Sessions for each currency.

Recurring subscription plans are supported.

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

This guide describes how to enable Revolut Pay and shows the differences between accepting a card payment and using Revolut Pay.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add revolut_pay to the list of payment_method_types.

- Make sure all line_items use the same currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Revolut Pay as the payment method and click the Pay button.

## See also

- More about Revolut Pay

[More about Revolut Pay](/payments/revolut-pay)

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)