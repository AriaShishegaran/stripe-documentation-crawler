# Accept a SEPA Direct Debit payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Accepting SEPA Direct Debit payments on your website consists of creating an object to track a payment, collecting payment method information and mandate acknowledgement, and submitting the payment to Stripe for processing. Stripe uses this payment object, the PaymentIntent, to track and handle all the states of the payment until the payment completes.

SEPA Direct Debit is a delayed notification payment method, which means that funds are not immediately available after payment. A payment typically takes 5 business days to arrive in your account.

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: Europe, US, CA, NZ, SG, HK, JP, AU, MX

Supported currencies: eur

Presentment currencies: eur

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

To support SEPA Direct Debit payments in Checkout, Prices for all line items must be expressed in Euro (currency code eur).

[Prices](/api/prices)

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?ui=stripe-hosted)

Use this guide to learn how to enable SEPA Direct Debit—it shows the differences between accepting a card payment and using SEPA Direct Debit.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add sepa_debit to the list of payment_method_types.

- Make sure all your line_items use the eur currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

Because SEPA Direct Debit is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[handle delayed notification payment methods](/payments/checkout/fulfill-orders#delayed-notification)

[Test your integration](#test-integration)

## Test your integration

Stripe provides several test numbers you can use to make sure your integration is ready for production.

Use the SEPA Direct Debit test numbers when testing your Checkout integration with SEPA Direct Debit.

[SEPA Direct Debit test numbers](#test-integration)

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for SEPA Direct Debit is up to 180 days after the original payment.

Customers can dispute a payment through their bank up to 13 months after the original payment and there’s no appeal process.

[Customers](/api/customers)

Learn more about SEPA Direct Debit disputes.

[SEPA Direct Debit disputes](/payments/sepa-debit#disputed-payments)

## See also

- Save SEPA Direct Debit details for future payments

[Save SEPA Direct Debit details for future payments](/payments/sepa-debit/set-up-payment)

- Connect platforms using the Payment Methods API

[Connect platforms using the Payment Methods API](/payments/payment-methods/connect)
