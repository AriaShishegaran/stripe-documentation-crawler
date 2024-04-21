# Accept a Klarna payment

To create recurring or off-session payments with Klarna, sign up for the beta.

[sign up for the beta.](#)

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Klarna is a single use, immediate notification payment method that requires customers to authenticate their payment. Customers are redirected to a Klarna page, where they select among multiple payment options (immediate full payment, payment in installments, or deferred payment). When the customer accepts the terms, Klarna guarantees that the funds are available to the customer and transfers the funds to your Stripe account. The customer repays Klarna according to their selected payment option.

[single use](/payments/payment-methods#usage)

[immediate notification](/payments/payment-methods#payment-notification)

[authenticate](/payments/payment-methods#customer-actions)

Before you start the integration, make sure your account is eligible for Klarna by navigating to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: AT, BE, DE, DK, ES, FI, GB, IE, IT, NL, NO, SE, US, FR, CZ, EE, GR, LV, LT, SK, SI, AU, NZ, CA, PL, PT, CH

Supported currencies: eur, dkk, gbp, nok, sek, usd, czk, aud, nzd, cad, pln, chf

Presentment currencies: eur, dkk, gbp, nok, sek, usd, czk, aud, nzd, cad, pln, chf

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Klarna payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- You can only use one-time line items (recurring subscription plans are not supported).

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable Klarna—it shows the differences between accepting a card payment and using Klarna.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add klarna to the list of payment_method_types

- Make sure all your line_items use the same currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Klarna as the payment method and click the Pay button. In test mode, you can then simulate different outcomes within Klarna’s redirect.

Below, we have specially selected test data for the currently supported customer countries. In test mode, Klarna approves or denies a transaction based on the supplied email address.

For production testing, you can use an amount of 3500 in your local currency to test all Klarna payment options besides Financing. For example, if you want to test “Pay in 3” in Italy, you can use a transaction of 35.00 EUR.

Any six digit number is a valid two-step authentication code. Use 999999 for authentication to fail.

Inside the Klarna flow, you can use the following test values to try various repayment types:

- Number: 4111 1111 1111 1111

- CVV: 123

- Expiration: any valid date in the future

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

Learn more about Klarna disputes and refunds.

[disputes](/payments/klarna#disputed-payments)

[refunds](/payments/klarna#refunds)
