# Accept an FPX payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

FPX is a single-use payment method. Customers pay with FPX by redirecting from your website, sending you payment, then returning to your website where you get immediate notification on whether the payment succeeded or failed.

[single-use](/payments/payment-methods#usage)

[immediate notification](/payments/payment-methods#payment-notification)

[Determine compatibility](#compatibility)

## Determine compatibility

Customer Geography: Malaysia

Supported currencies: myr

Presentment currencies: myr

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support FPX payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- You can only use one-time line items (recurring subscription plans are not supported).

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable FPX—it shows the differences between accepting a card payment and using FPX.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add fpx to the list of payment_method_types

- Make sure all your line_items use the myr currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

FPX requires showing your customer their transaction information after they’ve completed their payment. Follow the custom success page guide to learn how to customize your success page.

[custom success page](/payments/checkout/custom-success-page)

When customizing, you’ll need to retrieve the Charge object directly from the PaymentIntent object using the PaymentIntent ID from your Checkout Session and display the following information on your success_url page.

[PaymentIntent](/api/payment_intents/object#payment_intent_object-latest_charge)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select FPX as the payment method and click the Pay button.

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

The refund period for FPX is up to 60 days after the original payment.

There is no dispute process—customers authenticate with their bank.

## See also

- More about FPX

[More about FPX](/payments/fpx)

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
