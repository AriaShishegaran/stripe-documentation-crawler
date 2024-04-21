# Migrate to the Payment Element

If your integration still uses the Charges API with tokens, follow the Migrating to the Payment Intents API guide first.

[Migrating to the Payment Intents API](/payments/payment-intents/migration#web)

We’re developing a Payment Element integration that manages subscriptions, tax, discounts, shipping, and currency conversion. Read the Build a checkout page guide to learn more.

[Build a checkout page](/checkout/custom-checkout)

Previously, each payment method (cards, iDEAL, and so on) required a separate Element. By migrating to the Payment Element, you can accept many payment methods with a single Element.

PaymentIntents and SetupIntents each have their own set of migration guidelines. See the appropriate guide for your integration path, including example code.

If your existing integration uses the Payment Intents API to create and track payments or save card details during a payment, follow the steps below to use the Payment Element.

[Payment Intents](/payments/payment-intents)

[Enable payment methods](#enable-payment-methods)

## Enable payment methods

Stripe doesn’t currently support BLIK for this integration path.

View your payment methods settings and enable the payment methods you want to support. You need at least one payment method enabled to create a PaymentIntent.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[PaymentIntent](/payments/payment-intents)

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See Payment method integration options for product and payment method support, and our pricing page for fees.

[Payment method integration options](/payments/payment-methods/integration-options#payment-method-product-support)

[pricing page](https://stripe.com/pricing/local-payment-methods)

[Update Elements instanceClient-side](#one-time-update-elements)

## Update Elements instanceClient-side

Next, update your client-side code to pass mode, currency, and amount when you create the Elements instance. For use with a PaymentIntent, set the mode to 'payment' and the currency and amount to what you’ll charge your customer.

[OptionalSave payment details during a payment](#one-time-save-payment-details)

## OptionalSave payment details during a payment

[OptionalAdditional elements optionsClient-side](#additional-options)

## OptionalAdditional elements optionsClient-side

[Add the Payment ElementClient-side](#one-time-add-payment-element)

## Add the Payment ElementClient-side

If you’re using React Stripe.js, update to the latest package to use the Payment Element.

[React Stripe.js](https://github.com/stripe/react-stripe-js)

You can now replace the Card Element and individual payment methods Elements with the Payment Element. The Payment Element automatically adjusts to collect input fields based on the payment method and country (for example, full billing address collection for SEPA Direct Debit) so you don’t have to maintain customized input fields anymore.

The following example replaces CardElement with PaymentElement:

If your payment flow already always collects details like the customer’s name or email address, you can prevent the Payment Element from collecting this information by passing the fields option when creating the Payment Element. If you disable the collection of a certain field, you must pass that same data back with stripe.confirmPayment.

[fields](/js/elements_object/create_payment_element#payment_element_create-options-fields)

[stripe.confirmPayment](/js/payment_intents/confirm_payment)

[Update your PaymentIntent creation callServer-side](#one-time-payment-intent)

## Update your PaymentIntent creation callServer-side

The Payment Element allows you to accept multiple payment methods. You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. We prioritize payment methods that increase conversion and are most relevant to the customer’s currency and location.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Any of the additional elements options passed when creating the Elements group in the earlier step should also be passed when creating the PaymentIntent.

Each payment method needs to support the currency passed in the PaymentIntent and your business needs to be based in one of the countries each payment method supports. See the Payment method integration options page for more details about what’s supported.

[Payment method integration options](/payments/payment-methods/integration-options)

[Update the submit handlerClient-side](#one-time-update-method)

## Update the submit handlerClient-side

Instead of using individual confirm methods like stripe.confirmCardPayment or stripe.confirmP24Payment, use stripe.confirmPayment to collect payment information and submit it to Stripe.

[stripe.confirmPayment](/js/payment_intents/confirm_payment)

To confirm the PaymentIntent, make the following updates to your submit handler:

- Call elements.submit() to trigger form validation and collect any data required for wallets.

[wallets](/js/elements_object/create_payment_element#payment_element_create-options-wallets)

- Optional: Move PaymentIntent creation to the submit handler. This way you only create the PaymentIntent when you’re sure of the final amount.

- Pass the elements instance you used to create the Payment Element and the clientSecret from the PaymentIntent as parameters to stripe.confirmPayment.

When called, stripe.confirmPayment attempts to complete any required actions, such as authenticating your customers by displaying a 3DS dialog or redirecting them to a bank authorization page. When confirmation is complete, users are directed to the return_url you configured, which normally corresponds to a page on your website that provides the status of the payment.

[required actions](/payments/paymentintents/lifecycle)

[provides the status of the payment](/payments/accept-a-payment#web-post-payment)

If you want to keep the same checkout flow for card payments and only redirect for redirect-based payment methods, you can set redirect to if_required.

[redirect](/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)

The following code example replaces stripe.confirmCardPayment with stripe.confirmPayment:

[https://example.com/order/123/complete](https://example.com/order/123/complete)

[Handle post-payment eventsServer-side](#post-payment)

## Handle post-payment eventsServer-side

Stripe sends a payment_intent.succeeded event when the payment completes. Use the Dashboard webhook tool or follow the webhook guide to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[payment_intent.succeeded](/api/events/types#event_types-payment_intent.succeeded)

[Dashboard webhook tool](https://dashboard.stripe.com/webhooks)

[webhook guide](/webhooks/quickstart)

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept different types of payment methods with a single integration.

[different types of payment methods](https://stripe.com/payments/payment-methods-guide)

In addition to handling the payment_intent.succeeded event, we recommend handling these other events when collecting payments with the Payment Element:

[payment_intent.succeeded](/api/events/types?lang=php#event_types-payment_intent.succeeded)

[payment_intent.processing](/api/events/types?lang=php#event_types-payment_intent.processing)

[payment_intent.payment_failed](/api/events/types?lang=php#event_types-payment_intent.payment_failed)

[Test the integration](#test-the-integration)

## Test the integration

[authentication](/strong-customer-authentication)

See Testing for additional information to test your integration.

[Testing](/testing)
