# Accept an iDEAL payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

iDEAL is a single use payment method where customers are required to authenticate their payment. Customers pay with iDEAL by redirecting from your website, authorizing the payment, then returning to your website where you get immediate notification on whether the payment succeeded or failed.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[Customers](/api/customers)

[immediate notification](/payments/payment-methods#payment-notification)

To accept iDEAL, you must comply with our iDEAL Terms of Service.

[iDEAL Terms of Service](https://stripe.com/ideal/legal)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: Europe, US, CA, NZ, SG, HK, JP, AU, MX

Supported currencies: eur

Presentment currencies: eur

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support iDEAL payments:

- Prices for all line items must be expressed in Euro (currency code eur).

[Prices](/api/prices)

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?ui=stripe-hosted)

Use this guide to learn how to enable iDEAL—it shows the differences between accepting a card payment and using iDEAL.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add ideal to the list of payment_method_types

- Make sure all your line_items use the eur currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select iDEAL as the payment method and click the Pay button.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for iDEAL is up to 180 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- More about iDEAL

[More about iDEAL](/payments/ideal)

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
