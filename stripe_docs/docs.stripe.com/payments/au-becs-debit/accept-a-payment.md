# Accept a BECS Direct Debit payment

See the BECS Direct Debit overview to learn more about this payment method.

[BECS Direct Debit overview](/payments/au-becs-debit)

Stripe users in Australia can use the Payment Element and a Payment Intent to initiate BECS Direct Debit payments from customers with an AU bank account.

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

[Determine compatibility](#compatibility)

## Determine compatibility

Customer Geography: Australia

Supported currencies: aud

Presentment currencies: aud

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

To support BECS Direct Debit payments in Checkout, Prices for all line items must be expressed in Australian dollars (currency code aud).

[Prices](/api/prices)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable BECS Direct Debit—it shows the differences between accepting a card payment and using BECS Direct Debit.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add au_becs_debit to the list of payment_method_types

- Make sure all your line_items use the aud currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

Because BECS Direct Debit is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[handle delayed notification payment methods](/payments/checkout/fulfill-orders#delayed-notification)

[Test your integration](#test-integration)

## Test your integration

You’ll want to use the BECS Direct Debit test numbers when testing your Checkout integration with BECS Direct Debit.

[BECS Direct Debit test numbers](#test-integration)

There are several test numbers you can use to make sure your integration is ready for production.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for BECS Direct Debit is up to 90 days after the original payment.

Customers can dispute a payment through their bank up to 7 years after the original payment and there is no appeals process.

Learn more about BECS Direct Debit disputes.

[BECS Direct Debit disputes](/payments/au-becs-debit)

## See also

- More about BECS Direct Debit

[More about BECS Direct Debit](/payments/au-becs-debit)

- Managing mandates

[Managing mandates](/payments/au-becs-debit#mandates)

- After the payment

[After the payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)

- Save BECS Direct Debit details for future payments

[Save BECS Direct Debit details for future payments](/payments/au-becs-debit/set-up-payment)

- Connect platforms using the Payment Methods API

[Connect platforms using the Payment Methods API](/payments/payment-methods/connect)
