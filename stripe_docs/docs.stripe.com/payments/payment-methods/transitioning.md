# Transition to the Payment Intents and Payment Methods APIs

The Payment Methods API replaces the existing Tokens and Sources APIs as the recommended way for integrations to collect and store payment information. It works with the Payment Intents API to create payments for a wide range of payment methods.

[Payment Methods API](/api/payment_methods)

[Tokens](/api/tokens)

[Sources](/api/sources)

[Payment Intents API](/payments/payment-intents)

We plan to turn off Sources API support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate them to the Payment Methods API](#migrate-local-payment-methods)

While we don’t plan to turn off support for card payment methods, we still recommend that you migrate them to the Payment Methods and Payment Intents APIs. For more information about migrating card payment methods, see Migrating to the Payment Intents API.

[Migrating to the Payment Intents API](/payments/payment-intents/migration)

## Migrate local payment methods from the Sources API to the Payment Intents API

To migrate your integration for local payment methods, update your server and front end to use the PaymentIntents API. There are three typical integration options:

[PaymentIntents API](/api/payment_intents)

- Redirect to Stripe Checkout for your payment flow.

[Stripe Checkout](/payments/checkout)

- Use the Stripe Payment Element on your own payment page.

[Payment Element](/payments/payment-element)

- Build your own form and use the Stripe JS SDK to complete the payment.

If you use Stripe Checkout or the Payment Element, you can add and manage most payment methods from the Stripe Dashboard without making code changes.

For specific information about integrating a local payment method using the Payment Methods API, see the instructions for that payment method in the payment methods documentation. The following table provides a high-level comparison of the different payment types.

[the payment methods documentation](/payments/payment-methods/overview)

Low complexity

Medium complexity

High complexity

A PaymentIntent object represents a payment in the new integration, and it creates a Charge when you confirm the payment on the front end. If you previously stored references to the Charge, you can continue to do so by fetching the Charge ID from the PaymentIntent after the customer completes the payment. However, we also recommend that you store the PaymentIntent ID.

If you use the Payment Element or your own form, you must remap Source fields to PaymentIntent fields. The specific fields depend on the payment method.

Previously, your integration should have checked both the status of the Source and the status of the Charge after each API call. You no longer need to check two statuses—you only need to check the status of the PaymentIntent or the Checkout Session after you confirm it on the front end.

Always confirm the status of the PaymentIntent by fetching it on your server or listening for the webhooks on your server. Don’t rely solely on the user returning to the return_url that’s provided when you confirm the PaymentIntent.

You can continue to call the Refunds API with a Charge that the PaymentIntent creates. The ID of the Charge is accessible on the latest_charge parameter.

Alternatively, you can provide the PaymentIntent ID to the Refunds API instead of the Charge.

Previously, you had to handle errors on the Sources. With PaymentIntents, instead of checking for errors on a Source, you check for errors on the PaymentIntent when it’s created and after the customer has authorized the payment. Most errors on the PaymentIntent are of invalid_request_error type, returned in an invalid request.

When you migrate your integration, keep in mind that PaymentIntent error codes can differ from the corresponding error codes for Sources.

If you previously listened to Source events, you might need to update your integration to listen to new event types. The following table shows some examples.

[expires](/api/checkout/sessions/create#create_checkout_session-expires_at)

## Transitioning to the Payment Methods API

The main difference between the Payment Methods and Sources APIs is that Sources describes transaction state through the status property. That means that each Source object must transition to a chargeable state before it can be used for a payment. In contrast, a PaymentMethod is stateless, relying on the PaymentIntent object to represent payment state.

[status](/api/sources/object#source_object-status)

[PaymentIntent](/payments/payment-intents)

The following table isn’t a comprehensive list of payment methods. If you integrate other payment methods with the Sources API, migrate them to the Payment Methods API as well.

[Card payments](/payments/cards)

[Supported on Tokens](/payments/charges-api)

[US bank account direct debits](/payments/ach-debit)

[Supported on Tokens](/ach-deprecated)

[Alipay payments](/payments/alipay)

[Deprecated](/sources/alipay)

[Bancontact payments](/payments/bancontact)

[Deprecated](/sources/bancontact)

[EPS payments](/payments/eps)

[giropay payments](/payments/giropay)

[Deprecated](/sources/giropay)

[iDEAL payments](/payments/ideal)

[Deprecated](/sources/ideal)

[Klarna payments](/payments/klarna)

[Planned](https://support.stripe.com/questions/when-will-multibanco-be-available-on-payment-intents)

[Deprecated Beta](/sources/multibanco)

[Przelewy24 payments](/payments/p24)

[Deprecated](/sources/p24)

[Single Euro Payments Area direct debits](/payments/sepa-debit)

[Deprecated](/sources/sepa-debit)

[Sofort payments](/payments/sofort)

[WeChat Pay payments](/payments/wechat-pay)

[Deprecated](/sources/wechat-pay)

After you choose the API to integrate with, our guide to payment methods can help you determine the right payment method types to support for your customers.

[guide to payment methods](https://stripe.com/payments/payment-methods-guide)

This guide includes detailed descriptions of each payment method and describes the differences in the customer-facing flows, along with the geographic regions where they are most relevant. You can enable any payment method available to you within the Dashboard. Activation is generally instantaneous and does not require additional contracts nor include a lengthy process.

[geographic regions](https://stripe.com/payments/payment-methods-guide#payment-methods-fact-sheets)

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

## Compatibility with legacy reusable payment methods

If you previously processed any of the following reusable payment methods using Sources, the existing saved sources don’t migrate automatically. To preserve your existing customers’ saved payment methods, you must convert those sources to payment methods using a data migration tool in the Stripe Dashboard. For instructions on how to convert them, see the support page.

[Sources](/sources)

[the support page](https://support.stripe.com/questions/reusable-object-migration)

- Alipay

- Bacs Direct Debit

- SEPA Direct Debit

## Compatibility with legacy card objects

If you previously collected card customer payment details with Stripe using cards or Sources, you can start using the Payment Methods API immediately without migrating any payment information.

[cards](/saving-cards)

[Sources](/sources)

Compatible payment instruments that have been saved to a Customer are usable in any API that accepts a PaymentMethod object. For example, you can use a saved card as a PaymentMethod when creating a PaymentIntent:

[Customer](/api/customers)

[PaymentMethod](/api/payment_methods)

Remember to provide the customer ID that your compatible payment instrument is saved to when attaching the object to a PaymentIntent.

You can retrieve all saved compatible payment instruments through the Payment Methods API.

[retrieve](/api/payment_methods/retrieve)

Note that with this compatibility, no new objects are created; the Payment Methods API provides a different view of the same underlying object. For example, updates to a compatible payment instrument through the Payment Methods API is visible through the Sources API and vice versa.

## See also

- Guide to payment methods

[Guide to payment methods](https://stripe.com/payments/payment-methods-guide)

- Connect platforms using the Payment Methods API

[Connect platforms using the Payment Methods API](/payments/payment-methods/connect)

- Payment Methods API reference

[Payment Methods API reference](/api/payment_methods)
