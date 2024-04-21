# Accept a Sofort payment

Our financial partners are in the process of deprecating Sofort. New businesses can’t accept Sofort payments. For more information read our support page.

[support page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

SOFORT is a delayed notification payment method, which means that funds are not immediately available after payment. A payment typically takes 2 to 14 business days to arrive in your account.

Customers pay with SOFORT by redirecting away from the Checkout Session to their bank, sending you payment, and then returning to Checkout. They are then redirected back to your site.

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: Europe, US, CA, NZ, SG, HK, JP, AU, MX

Supported currencies: eur

Presentment currencies: eur

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support SOFORT payments:

- Prices for all line items must be expressed in Euro (currency code eur).

[Prices](/api/prices)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable SOFORT—it shows the differences between accepting a card payment and using SOFORT.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add sofort to the list of payment_method_types.

- Make sure all your line_items use the eur currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

Because SOFORT is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[handle delayed notification payment methods](/payments/checkout/fulfill-orders#delayed-notification)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select SOFORT as the payment method and click the Pay button.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for SOFORT is up to 180 days after the original payment.

There is no dispute process–customers authenticate with their bank.
