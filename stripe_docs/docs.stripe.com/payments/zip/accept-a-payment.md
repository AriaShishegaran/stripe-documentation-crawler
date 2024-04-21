# Accept a Zip payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Zip is an Australia-based BNPL payment method that allows customers to split purchases over a series of payments.

Customers authenticate a payment on Zip website and there is immediate notification about the success or failure of a payment.

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: AU

Supported currencies: aud

Presentment currencies: aud

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Zip payments:

- Prices for all line items must be expressed in Australian Dollar (currency code aud).

[Prices](/api/prices)

[Accept a Zip payment](#accept-a-Zip-payment)

## Accept a Zip payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Make the following updates to your card payment integration to enable Zip.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add zip to the list of payment_method_types

- Make sure all your line_items use the aud currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Zip as the payment method and click Pay.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

Learn more about Zip disputes and refunds.

[disputes](/payments/zip#disputes-and-fraud)

[refunds](/payments/zip#refunds)

## See also

- After the payment

[After the payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
