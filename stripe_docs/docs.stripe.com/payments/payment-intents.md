# The Payment Intents API

Use the Payment Intents API to build an integration that can handle complex payment flows with a status that changes over the PaymentIntent’s lifecycle. It tracks a payment from creation through checkout, and triggers additional authentication steps when required.

[Payment Intents](/api/payment_intents)

[PaymentIntent’s lifecycle](/payments/paymentintents/lifecycle)

Some of the advantages of using the Payment Intents API include:

[Payment Intents](/api/payment_intents)

- Automatic authentication handling

- No double charges

- No idempotency key issues

[idempotency key](/api/idempotent_requests)

- Support for Strong Customer Authentication (SCA) and similar regulatory changes

[Strong Customer Authentication](/strong-customer-authentication)

## A complete set of APIs

Use the Payment Intents API together with the Setup Intents and Payment Methods APIs. These APIs help you handle dynamic payments (for example, additional authentication like 3D Secure) and prepare you for expansion to other countries while allowing you to support new regulations and regional payment methods.

[Payment Intents](/api/payment_intents)

[Setup Intents](/api/setup_intents)

[Payment Methods](/api/payment_methods)

[3D Secure](/payments/3d-secure)

Building an integration with the Payment Intents API involves two actions: creating and confirming a PaymentIntent. Each PaymentIntent typically correlates with a single shopping cart or customer session in your application. The PaymentIntent encapsulates details about the transaction, such as the supported payment methods, the amount to collect, and the desired currency.

[confirming](/api/payment_intents/confirm)

## Creating a PaymentIntent

To get started, see the accept a payment guide. It describes how to create a PaymentIntent on the server and pass its client secret to the client instead of passing the entire PaymentIntent object.

[accept a payment guide](/payments/accept-a-payment?ui=elements)

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

When you create the PaymentIntent, you can specify options like the amount and currency:

[create the PaymentIntent](/api/payment_intents/create)

- We recommend creating a PaymentIntent as soon as you know the amount, such as when the customer begins the checkout process, to help track your purchase funnel. If the amount changes, you can update its amount. For example, if your customer backs out of the checkout process and adds new items to their cart, you may need to update the amount when they start the checkout process again.

We recommend creating a PaymentIntent as soon as you know the amount, such as when the customer begins the checkout process, to help track your purchase funnel. If the amount changes, you can update its amount. For example, if your customer backs out of the checkout process and adds new items to their cart, you may need to update the amount when they start the checkout process again.

[purchase funnel](https://en.wikipedia.org/wiki/Purchase_funnel)

[update](/api#update_payment_intent)

[amount](/api#payment_intent_object-amount)

- If the checkout process is interrupted and resumes later, attempt to reuse the same PaymentIntent instead of creating a new one. Each PaymentIntent has a unique ID that you can use to retrieve it if you need it again. In the data model of your application, you can store the ID of the PaymentIntent on the customer’s shopping cart or session to facilitate retrieval. The benefit of reusing the PaymentIntent is that the object state helps track any failed payment attempts for a given cart or session.

If the checkout process is interrupted and resumes later, attempt to reuse the same PaymentIntent instead of creating a new one. Each PaymentIntent has a unique ID that you can use to retrieve it if you need it again. In the data model of your application, you can store the ID of the PaymentIntent on the customer’s shopping cart or session to facilitate retrieval. The benefit of reusing the PaymentIntent is that the object state helps track any failed payment attempts for a given cart or session.

[retrieve](/api#retrieve_payment_intent)

[object state](/payments/paymentintents/lifecycle)

- Remember to provide an idempotency key to prevent the creation of duplicate PaymentIntents for the same purchase. This key is typically based on the ID that you associate with the cart or customer session in your application.

Remember to provide an idempotency key to prevent the creation of duplicate PaymentIntents for the same purchase. This key is typically based on the ID that you associate with the cart or customer session in your application.

[idempotency key](/api/idempotent_requests)

## Passing the client secret to the client side

The PaymentIntent contains a client secret, a key that’s unique to the individual PaymentIntent. On the client side of your application, Stripe.js uses the client secret as a parameter when invoking functions (such as stripe.confirmCardPayment or stripe.handleCardAction) to complete the payment.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[stripe.confirmCardPayment](/js#stripe-confirm-card-payment)

[stripe.handleCardAction](/js#stripe-handle-card-action)

The PaymentIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Retrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

You can use the client secret to complete the payment process with the amount specified on the PaymentIntent. Don’t log it, embed it in URLs, or expose it to anyone other than the customer. Make sure that you have TLS on any page that includes the client secret.

[TLS](/security/guide#tls)

## After the payment

After the client confirms the payment, it is a best practice for your server to monitor webhooks to detect when the payment successfully completes or fails.

[monitor webhooks](/payments/payment-intents/verifying-status#webhooks)

A PaymentIntent might have more than one Charge object associated with it if there were multiple payment attempts, for examples retries. For each charge you can inspect the outcome and details of the payment method used.

[Charge](/api/charges)

[outcome](/api/charges/object#charge_object-outcome)

[details of the payment method](/api/charges/object#charge_object-payment_method_details)

## Optimizing payment methods for future payments

The setup_future_usage parameter saves payment methods to use again in the future. For cards, it also optimizes authorization rates in compliance with regional legislation and network rules, such as SCA. To determine which value to use, consider how you want to use this payment method in the future.

[setup_future_usage](/api/payment_intents/object#payment_intent_object-setup_future_usage)

[SCA](/strong-customer-authentication)

You can still accept off-session payments with a card set up for on-session payments, but the bank is more likely to reject the off-session payment and require authentication from the cardholder.

The following example shows how to create a PaymentIntent and specify setup_future_usage:

Setups for off-session payments are more likely to incur additional friction. Use on-session setup if you don’t intend to accept off-session payments with the saved card.

## Dynamic statement descriptor

By default, your Stripe account’s statement descriptor appears on customer statements whenever you charge their card. To provide a different description on a per-payment basis, include the statement_descriptor parameter.

[statement descriptor](/get-started/account/activate#public-business-information)

Statement descriptors are limited to 22 characters, can’t use the special characters <, >, ', ", or *, and must not consist solely of numbers. When using dynamic statement descriptors, the dynamic text is appended to the statement descriptor prefix set in the Stripe Dashboard. An asterisk (*) and an empty space are also added to separate the default statement descriptor from the dynamic portion. These 2 characters count towards the 22 character limit.

[statement descriptor prefix](https://dashboard.stripe.com/settings/public)

## Storing information in metadata

Stripe supports adding metadata to the most common requests you make, such as processing payments. Metadata isn’t shown to customers or factored into whether or not a payment is declined or blocked by our fraud prevention system.

[metadata](/api#metadata)

Through metadata, you can associate information that’s meaningful to you with Stripe activity.

Any metadata you include is viewable in the Dashboard (for example, when looking at the page for an individual payment), and is also available in common reports. As an example, you can attach the order ID for your store to the PaymentIntent for that order. Doing so allows you to easily reconcile payments in Stripe to orders in your system.

If you’re using Radar for Fraud Teams, consider passing additional customer information and order information as metadata. Then you can write Radar rules using metadata attributes and have more information available within the Dashboard, which can expedite your review process.

[Radar for Fraud Teams](/radar)

[Radar rules using metadata attributes](/radar/rules/reference#metadata-attributes)

When a PaymentIntent creates a charge, the PaymentIntent copies its metadata to the charge. Subsequent updates to the PaymentIntent’s metadata won’t modify the metadata of charges previously created by the PaymentIntent.

Don’t store any sensitive information (personally identifiable information, card details, and so on) as metadata or in the description parameter of the PaymentIntent.

## See also

- Accept a payment online

[Accept a payment online](/payments/accept-a-payment?platform=web)

- Accept a payment in an iOS app

[Accept a payment in an iOS app](/payments/accept-a-payment?platform=ios)

- Accept a payment in an Android app

[Accept a payment in an Android app](/payments/accept-a-payment?platform=android)

- Set up future payments

[Set up future payments](/payments/save-and-reuse)
