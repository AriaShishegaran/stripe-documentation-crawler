# MobilePay payments

MobilePay is a single-use card wallet payment method used in Denmark and Finland. It allows customers to authenticate and approve payments using the MobilePay app.

[single-use](/payments/payment-methods#usage)

[authenticate and approve](/payments/payment-methods#customer-actions)

During the processing of a MobilePay payment, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and you can only see the outcome of the transaction.

Stripe immediately notifies you when the payment succeeded or failed.

[immediately notifies you](/payments/payment-methods#payment-notification)

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Use this guide to enable MobilePay on Checkout, our hosted checkout form, and learn the differences between accepting a card payment and a MobilePay payment.

[Checkout](/payments/checkout)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: EEA

Supported currencies: eur, dkk, sek, nok

Presentment currencies: eur, dkk, sek, nok

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support MobilePay payments:

- Prices for all line items must be expressed in Euro, Danish Krona, Swedish Krona or Norwegian Krona (currency codes eur, dkk, sek or nok).

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

- Add mobilepay to the list of payment_method_types

- Make sure all your line_items use the eur, dkk, sek or nok currency

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

After accepting a payment, learn how to fulfill orders.

[fulfill orders](/payments/checkout/fulfill-orders)

[OptionalHandle post-payment events](#post-payment-events)

## OptionalHandle post-payment events

[OptionalTest the integration](#direct-api-test-integration)

## OptionalTest the integration

[Failed payments](#failed-payments)

## Failed payments

MobilePay transactions can fail if the underlying card transaction is declined. Learn more about card declines.

[card declines](/declines/card)

In these cases, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

[PaymentMethod](/api/payment_methods/object)

[PaymentIntent](/api/payment_intents/object)

Other than a payment being declined, for a MobilePay PaymentIntent with a status of requires_action, customers must complete the payment within 5 minutes. If no action is taken after 5 minutes, the PaymentMethod detaches and the PaymentIntent object’s status automatically transitions to requires_payment_method.

[PaymentIntent](/api/payment_intents/object)

[PaymentMethod](/api/payment_methods/object)

[PaymentIntent](/api/payment_intents/object)

[Handle refunds and disputes](#refunds-and-disputes)

## Handle refunds and disputes

Stripe performs a card transaction using standard card rails as part of a MobilePay transaction. Refunds and disputes are subject to the Visa and Mastercard network rules.

[Refunds](/refunds)

[disputes](/disputes/how-disputes-work)

## See also

- More about MobilePay

[More about MobilePay](/payments/mobilepay)

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
