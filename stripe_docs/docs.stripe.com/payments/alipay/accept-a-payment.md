# Accept an Alipay payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Alipay is a single-use payment method where customers are required to authenticate their payment. Customers pay by redirecting from your website or app, authorize the payment through Alipay, then return to your website or app where you get immediate notification on whether the payment succeeded or failed.

[single-use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[immediate notification](/payments/payment-methods#payment-notification)

[Determine Compatibility](#compatibility)

## Determine Compatibility

Customer Geography: China

Supported currencies: aud, cad, eur, gbp, hkd, jpy, nzd, sgd, usd, myr

Presentment currencies: aud, cad, cny, eur, gbp, hkd, jpy, nzd, sgd, usd, myr

Payment mode: Yes

Setup mode: No

Subscription mode: No

To support Alipay payments, a Checkout Session must satisfy all of the following conditions:

- Prices for all line items must be in the same currency.If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- If you have line items in different currencies, create separate Checkout Sessions for each currency.

- You can only use one-time line items.

Recurring subscription plans aren’t supported.

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

This guide describes how to enable Alipay and shows the differences between accepting a card payment and using Alipay.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add Alipay to the list of payment_method_types.

- Make sure all line_items use the same currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Alipay as the payment method and click the Pay button.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for Alipay is up to 90 days after the original payment.

Alipay has no dispute process—customers authenticate with their Alipay account.

## See also

- More about Alipay

[More about Alipay](/payments/alipay)

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
