# Swish payments

Swish is a single-use payment method used in Sweden. It allows customers to authenticate and approve payments using the Swish mobile app and the Swedish BankID mobile app.

[single-use](/payments/payment-methods#usage)

[authenticate and approve](/payments/payment-methods#customer-actions)

You get immediate notification on whether the payment succeeded or failed.

[immediate notification](/payments/payment-methods#payment-notification)

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Use this guide to enable Swish on Checkout, our hosted checkout form, and learn the differences between accepting a card payment and a Swish payment.

[Checkout](/payments/checkout)

Swish is a delayed notification payment method, which means that funds are not immediately available after payment. A payment typically takes 2 business days to arrive in your account.

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: Europe

Supported currencies: sek

Presentment currencies: sek

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Swish payments:

- Prices for all line items must be expressed in SEK.

[Prices](/api/prices)

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?integration=checkout)

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add swish to the list of payment_method_types.

- Make sure all your line_items use the sek currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

Because Swish is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[handle delayed notification payment methods](/payments/checkout/fulfill-orders#delayed-notification)

[OptionalHandle post-payment events](#post-payment-events)

## OptionalHandle post-payment events

[OptionalTest the integration](#direct-api-test-integration)

## OptionalTest the integration

[Failed payments](#failed-payments)

## Failed payments

Swish uses multiple data points to decide when to decline a transaction (for example, there aren’t enough funds in the customer’s bank account, or the customer has clicked Cancel in the app).

In these cases, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

[PaymentMethod](/api/payment_methods/object)

[PaymentIntent](/api/payment_intents/object)

Other than a payment being declined, for a Swish PaymentIntent with a status of requires_action, customers must complete the payment within 3 minutes. If no action is taken after 3 minutes, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

[PaymentIntent](/api/payment_intents/object)

[PaymentMethod](/api/payment_methods/object)

[PaymentIntent](/api/payment_intents/object)

## See also

- After the payment

[After the payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
