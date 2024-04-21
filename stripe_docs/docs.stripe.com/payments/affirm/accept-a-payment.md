# Accept an Affirm payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Affirm is a single use, immediate notification payment method that requires customers to authenticate their payment. Customers are redirected to the Affirm site, where they agree to the terms of an installment plan. When the customer accepts the terms, funds are guaranteed and transferred to your Stripe account. The customer repays Affirm directly over time.

[single use](/payments/payment-methods#usage)

[immediate notification](/payments/payment-methods#payment-notification)

[authenticate](/payments/payment-methods#customer-actions)

Before you start the integration, make sure your account is eligible for Affirm by navigating to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[Determine compatibility](#compatibility)

## Determine compatibility

Customer Geography: Canada, US

Supported currencies: cad, usd

Presentment currencies: cad, usd

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Affirm payments:

- You can only use one-time line items. Affirm doesn’t support recurring subscription plans.

[subscription](/billing/subscriptions/creating)

- Express all Prices in your domestic currency.

[Prices](/api/prices)

[Accept a payment](#accept-a-payment)

## Accept a payment

This guide builds on the foundational accept a payment Checkout integration.

[accept a payment](/payments/accept-a-payment?ui=stripe-hosted)

Use this guide to learn how to enable Affirm—it shows the differences between accepting a card payment and using Affirm.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add affirm to the list of payment_method_types.

- Make sure all your line_items use your domestic currency.

- We recommend collecting shipping addresses by adding your country to shipping_address_collection[allowed_countries]. If you don’t want to collect shipping addresses with Checkout, you can also provide the shipping address using payment_intent_data[shipping]. Doing so helps with loan acceptance rates.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

Use a method such as webhooks to handle order fulfillment, instead of relying on your customer to return to the payment status page.

[Use a method such as webhooks](/payments/payment-intents/verifying-status#webhooks)

The following events are sent when the payment status changes:

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[payment_intent.succeeded](/api/events/types#event_types-payment_intent.succeeded)

[payment_intent.payment_failed](/api/events/types#event_types-payment_intent.payment_failed)

Learn more about fulfilling orders.

[fulfilling orders](/payments/checkout/fulfill-orders)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Affirm as the payment method and click the Pay button.

Test your Affirm integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from requires_action to succeeded.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click Fail test payment. The PaymentIntent transitions from requires_action to requires_payment_method.

For manual capture PaymentIntents in testmode, the uncaptured PaymentIntent auto-expires 10 minutes after successful authorization.

[manual capture](#manual-capture)

[Failed payments](#failed-payments)

## Failed payments

Affirm takes into account multiple factors when deciding to accept or decline a transaction (for example, the length of time buyer has used Affirm, the outstanding amount the customer has to repay, and the value of the current order).

Always present additional payment options such as card in your checkout flow, as Affirm payments have a higher rate of decline than many payment methods. In these cases, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

[PaymentMethod](/api/payment_methods/object)

[PaymentIntent](/api/payment_intents/object)

Other than a payment being declined, for an Affirm PaymentIntent with a status of requires_action, customers need to complete the payment within 12 hours after you redirect them to the Affirm site. If the customer takes no action within 12 hours, the PaymentMethod is detached and the PaymentIntent object’s status automatically transitions to requires_payment_method.

[PaymentIntent](/api/payment_intents/object)

[PaymentMethod](/api/payment_methods/object)

[PaymentIntent](/api/payment_intents/object)

In these cases, inform your customer to try again with a different payment option presented in your checkout flow.

[Error codes](#error-codes)

## Error codes

These are the common error codes and corresponding recommended actions:

[default transaction limits](/payments/affirm)

[default transaction limits](/payments/affirm)

[two-letter ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
