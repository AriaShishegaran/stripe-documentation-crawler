htmlTransition to the Payment Intents and Payment Methods APIs | Stripe Documentation[Skip to content](#main-content)Transition to the new APIs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Ftransitioning)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Ftransitioning)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Sources](/docs/sources)# Transition to the Payment Intents and Payment Methods APIs

Learn about transitioning from using the Sources and Tokens APIs to using the Payment Methods API.The Payment Methods API replaces the existing Tokens and Sources APIs as the recommended way for integrations to collect and store payment information. It works with the Payment Intents API to create payments for a wide range of payment methods.

We plan to turn off Sources API support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

While we don’t plan to turn off support for card payment methods, we still recommend that you migrate them to the Payment Methods and Payment Intents APIs. For more information about migrating card payment methods, see Migrating to the Payment Intents API.

## Migrate local payment methods from the Sources API to the Payment Intents API

To migrate your integration for local payment methods, update your server and front end to use the PaymentIntents API. There are three typical integration options:

- Redirect to[Stripe Checkout](/payments/checkout)for your payment flow.
- Use the Stripe[Payment Element](/payments/payment-element)on your own payment page.
- Build your own form and use the Stripe JS SDK to complete the payment.

If you use Stripe Checkout or the Payment Element, you can add and manage most payment methods from the Stripe Dashboard without making code changes.

For specific information about integrating a local payment method using the Payment Methods API, see the instructions for that payment method in the payment methods documentation. The following table provides a high-level comparison of the different payment types.

Old integrationStripe CheckoutPayment ElementOwn formLow complexity

Medium complexity

High complexity

Create a Source on the front end or on the serverCreate a Checkout Session on the serverCreate a PaymentIntent on the serverCreate a PaymentIntent on the serverAuthorize payment by loading a widget or redirecting to a third partyNot neededPass the client secret to the front end and use the Stripe JS SDK to render a Payment Element to complete the paymentPass the client secret to the front end, use your own form to collect details from your customer, and complete the payment according to the payment methodConfirm the source is chargeable and charge the SourceNot neededNot neededNot neededConfirm the Charge succeeded asynchronously with the`charge.succeeded`webhookConfirm the Checkout session succeeded with the`payment_intent.succeeded`webhookConfirm the PaymentIntent succeeded with the`payment_intent.succeeded`webhookConfirm the PaymentIntent succeeded with the`payment_intent.succeeded`webhookCautionA PaymentIntent object represents a payment in the new integration, and it creates a Charge when you confirm the payment on the front end. If you previously stored references to the Charge, you can continue to do so by fetching the Charge ID from the PaymentIntent after the customer completes the payment. However, we also recommend that you store the PaymentIntent ID.

### Mapping fields

If you use the Payment Element or your own form, you must remap Source fields to PaymentIntent fields. The specific fields depend on the payment method.

### Checking payment status

Previously, your integration should have checked both the status of the Source and the status of the Charge after each API call. You no longer need to check two statuses—you only need to check the status of the PaymentIntent or the Checkout Session after you confirm it on the front end.

payment_intent.statusMeaningNote`succeeded`The payment succeeded.`requires_payment_method`The payment failed.`requires_action`The customer hasn’t completed authorizing the payment.If the customer doesn’t complete the payment within 48 hours, then the PaymentIntent transitions to`requires_payment_method`and you can retry the confirmation.Always confirm the status of the PaymentIntent by fetching it on your server or listening for the webhooks on your server. Don’t rely solely on the user returning to the return_url that’s provided when you confirm the PaymentIntent.

### Refunds

You can continue to call the Refunds API with a Charge that the PaymentIntent creates. The ID of the Charge is accessible on the latest_charge parameter.

Alternatively, you can provide the PaymentIntent ID to the Refunds API instead of the Charge.

### Error handling

Previously, you had to handle errors on the Sources. With PaymentIntents, instead of checking for errors on a Source, you check for errors on the PaymentIntent when it’s created and after the customer has authorized the payment. Most errors on the PaymentIntent are of invalid_request_error type, returned in an invalid request.

When you migrate your integration, keep in mind that PaymentIntent error codes can differ from the corresponding error codes for Sources.

### Webhooks

If you previously listened to Source events, you might need to update your integration to listen to new event types. The following table shows some examples.

Old webhookNew webhook on CheckoutNew webhook on PaymentIntentsNote`source.chargeable`Not applicableNot applicable`source.failed`Not applicableNot applicable`source.canceled`Not applicableNot applicable`charge.succeeded``checkout.session.completed``payment_intent.succeeded`The`charge.succeeded`webhook is also sent, so you don’t have to update your integration to listen to the new webhook.`charge.failed`Not applicable - The customer can re-attempt the payment on the same Checkout Session until it[expires](/api/checkout/sessions/create#create_checkout_session-expires_at), at which point you receive a`checkout.session.expired`event.`payment_intent.payment_failed`The`charge.failed`webhook is also sent, so you don’t have to update your integration to listen to the new webhook.`charge.dispute.created``charge.dispute.created``charge.dispute.created`## Transitioning to the Payment Methods API

The main difference between the Payment Methods and Sources APIs is that Sources describes transaction state through the status property. That means that each Source object must transition to a chargeable state before it can be used for a payment. In contrast, a PaymentMethod is stateless, relying on the PaymentIntent object to represent payment state.

NoteThe following table isn’t a comprehensive list of payment methods. If you integrate other payment methods with the Sources API, migrate them to the Payment Methods API as well.

FlowsIntegrate Payment Method with Payment Intents APITokens or Sources with Charges APICards[Card payments](/payments/cards)[Supported on Tokens](/payments/charges-api); Not recommended on SourcesACH Direct Debit[US bank account direct debits](/payments/ach-debit)[Supported on Tokens](/ach-deprecated)Not supported on SourcesAlipay[Alipay payments](/payments/alipay)[Deprecated](/sources/alipay)Bancontact[Bancontact payments](/payments/bancontact)[Deprecated](/sources/bancontact)EPS[EPS payments](/payments/eps)Deprecatedgiropay[giropay payments](/payments/giropay)[Deprecated](/sources/giropay)iDEAL[iDEAL payments](/payments/ideal)[Deprecated](/sources/ideal)Klarna[Klarna payments](/payments/klarna)DeprecatedMultibanco[Planned](https://support.stripe.com/questions/when-will-multibanco-be-available-on-payment-intents)[Deprecated Beta](/sources/multibanco)Przelewy24[Przelewy24 payments](/payments/p24)[Deprecated](/sources/p24)SEPA Direct Debit[Single Euro Payments Area direct debits](/payments/sepa-debit)[Deprecated](/sources/sepa-debit)Sofort[Sofort payments](/payments/sofort)DeprecatedWeChat Pay[WeChat Pay payments](/payments/wechat-pay)[Deprecated](/sources/wechat-pay)After you choose the API to integrate with, our guide to payment methods can help you determine the right payment method types to support for your customers.

This guide includes detailed descriptions of each payment method and describes the differences in the customer-facing flows, along with the geographic regions where they are most relevant. You can enable any payment method available to you within the Dashboard. Activation is generally instantaneous and does not require additional contracts nor include a lengthy process.

## Compatibility with legacy reusable payment methods

If you previously processed any of the following reusable payment methods using Sources, the existing saved sources don’t migrate automatically. To preserve your existing customers’ saved payment methods, you must convert those sources to payment methods using a data migration tool in the Stripe Dashboard. For instructions on how to convert them, see the support page.

- Alipay
- Bacs Direct Debit
- SEPA Direct Debit

## Compatibility with legacy card objects

If you previously collected card customer payment details with Stripe using cards or Sources, you can start using the Payment Methods API immediately without migrating any payment information.

Compatible payment instruments that have been saved to a Customer are usable in any API that accepts a PaymentMethod object. For example, you can use a saved card as a PaymentMethod when creating a PaymentIntent:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "payment_method_types[]"=card \
  -d amount=1099 \
  -d currency=usd \
  -d customer={{CUSTOMER_ID}} \
  -d payment_method={{CARD_ID}}`Remember to provide the customer ID that your compatible payment instrument is saved to when attaching the object to a PaymentIntent.

You can retrieve all saved compatible payment instruments through the Payment Methods API.

CardCard Source`{
  "id": "card_1EBXBSDuWL9wT9brGOaALeD2",
  "object": "card",
  "address_city": "San Francisco",
  "address_country": "US",
  "address_line1": "1234 Fake Street",
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,`See all 26 lines`{
  "id": "card_1EBXBSDuWL9wT9brGOaALeD2",
  "object": "payment_method",
  "billing_details": {
    "address": {
      "city": "San Francisco",
      "country": "US",
      "line1": "1234 Fake Street",
      "line2": null,
      "postal_code": null,`See all 41 linesNote that with this compatibility, no new objects are created; the Payment Methods API provides a different view of the same underlying object. For example, updates to a compatible payment instrument through the Payment Methods API is visible through the Sources API and vice versa.

## See also

- [Guide to payment methods](https://stripe.com/payments/payment-methods-guide)
- [Connect platforms using the Payment Methods API](/payments/payment-methods/connect)
- [Payment Methods API reference](/api/payment_methods)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Migrate local payment methods from the Sources API to the Payment Intents API](#migrate-local-payment-methods)[Transitioning to the Payment Methods API](#transitioning)[Compatibility with legacy reusable payment methods](#compatibility-reusable)[Compatibility with legacy card objects](#compatibility)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`