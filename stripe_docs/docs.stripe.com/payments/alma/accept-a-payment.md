# Accept a payment with AlmaBeta

[privacy policy](https://stripe.com/privacy)

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Alma is a single-use payment method where customers choose to pay between 2, 3, or 4 installments. Customers are redirected from your website or app, authorize the payment with Alma, then return to your website or app. You get immediate notification of whether the payment succeeded or failed.

[single-use](/payments/payment-methods#usage)

[immediate notification](/payments/payment-methods#payment-notification)

[Determine compatibility](#compatibility)

## Determine compatibility

To support Alma payments, a Checkout Session must satisfy all of the following conditions:

- Prices for all line items must be in the same currency.If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

This guide describes how to enable Alma and shows the differences between accepting a card payment and using Alma.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add alma to the list of payment_method_types.

- Make sure all line_items use the same currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Alma as the payment method and click the Pay button.

## See also

- More about Alma

[More about Alma](/payments/alma)

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)