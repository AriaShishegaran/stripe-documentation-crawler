# BLIK payments

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

BLIK is a single use payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, US

Supported currencies: pln

Presentment currencies: pln

Payment mode: Yes

Setup mode: Not yet

Subscription mode: Not yet

A Checkout Session must satisfy all of the following conditions to support BLIK payments:

- Prices for all line items must be expressed in Złoty (currency code pln).

[Prices](/api/prices)

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?ui=stripe-hosted)

Use this guide to learn how to enable BLIK—it shows the differences between accepting a card payment and using BLIK.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add blik to the list of payment_method_types.

- Make sure all your line_items use the pln currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

Inside their Banking app, customers see four lines related to each BLIK transaction:

- If you provided a value for description when creating the PaymentIntent, the first two lines display it (max 70 characters).

- If you provided a value for statement_descriptor (typically, an order ID), line 3 displays it (max 22 characters).

- The fourth line automatically populates with the URL of your website.

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select BLIK as the payment method and click the Pay button.

Use test mode to test a successful payment by entering any 6-digit code (such as 123456) in the payment form.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for BLIK is up to 13 months after the original payment.

Customers can dispute a payment through their bank up to 13 months after the original payment and there’s no appeal process.

[Customers](/api/customers)

Learn more about BLIK disputes.

[BLIK disputes](/payments/blik#disputed-payments)

[OptionalSimulate failures in test mode](#simulate-failures)

## OptionalSimulate failures in test mode

## See also

- More about BLIK

[More about BLIK](/payments/blik)

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
