# Accept a giropay payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

giropay is a single use payment method where customers are required to authenticate their payment. Customers pay with giropay by redirecting from your website, authorizing the payment, then returning to your website where you get immediate notification on whether the payment succeeded or failed. Because giropay is a single use payment method, it isn’t compatible with SetupIntents.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[Customers](/api/customers)

[immediate notification](/payments/payment-methods#payment-notification)

[SetupIntents](/api/setup_intents)

Your use of giropay must be in accordance with the giropay Terms of Service.

[giropay Terms of Service](https://stripe.com/giropay/legal)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: Europe, US, CA, NZ, SG, HK, JP, AU, MX

Supported currencies: eur

Presentment currencies: eur

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support giropay payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- You can only use one-time line items (recurring subscription plans are not supported).

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable giropay—it shows the differences between accepting a card payment and using giropay.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add giropay to the list of payment_method_types

- Make sure all your line_items use the eur currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select giropay as the payment method and click the Pay button.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for giropay is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- After the payment

[After the payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
