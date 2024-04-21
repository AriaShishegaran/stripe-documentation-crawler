# Best practices for using SourcesDeprecated

We deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate them to the Payment Methods API](/payments/payment-methods/transitioning)

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

[PaymentMethods API](/api/payment_methods)

The flexibility of the Sources API helps you minimize the changes required to support additional payment methods as you add them.

## Typical flow for card payments

In a typical checkout flow for card payments (excluding 3D Secure), your integration collects the card information and creates a source, and uses it to make a charge request. Because it requires no additional action from the customer and card payments provide synchronous confirmation, we can immediately confirm if the payment is successful and that the funds are guaranteed—using webhooks isn’t necessary.

[card payments](/sources/cards)

[webhooks](/webhooks)

## The required use of webhooks

Other payment methods may require your customer to take additional action (for example, a redirect) before a source becomes chargeable and can be used to make a charge request (for example, iDEAL). This transition generally happens asynchronously and may even occur after the customer leaves your website. For these reasons your integration must rely on webhooks to determine when a source becomes chargeable before creating a charge.

[additional action](/sources#flow-for-customer-action)

[iDEAL](/sources/ideal)

Stripe sends the following webhook events to notify you about changes to the status of the source:

Similarly, when creating a charge, certain asynchronous payment methods might require days for the funds to be confirmed and the charge to succeed, requiring webhooks to know when to confirm and eventually fulfill your orders.

[asynchronous](/sources#synchronous-or-asynchronous-confirmation)

Stripe sends the following webhook events to notify you about changes to the status of a charge:

## Building a flexible integration

To ensure that your checkout process is flexible and ready to support multiple payment methods, we recommend the following approach:

When creating Sources, record the source ID on your internal order representation so that you can retrieve the order when you receive and process source.chargeable webhooks. Make sure to index your order objects based on this source attribute for efficient lookup.

[Sources](/api#sources)

Delivery of the source.chargeable webhook charges the Source. When receiving the webhook, retrieve your internal order representation by a look-up based on the received source ID and verify that the order is awaiting a payment.

When making a charge request, use your internal order ID as an idempotency key to avoid any possible race condition. Additionally, if the source is reusable and you want to reuse it, make sure to attach it to a Customer before charging it. Refer to the Single-use or reusable and Sources & Customers guides to learn more about how to handle single-use and reusable Sources and how they interact with Customers.

[idempotency key](/api#idempotent_requests)

[Customer](/api#customers)

[Single-use or reusable](/sources#single-use-or-reusable)

[Sources & Customers](/sources/customers)

[Customers](/api/customers)

Similarly to source creation, record the charge ID on your internal order representation so that you can retrieve the order when you receive and process charge.succeeded webhooks.

After your customer takes the required actions to authorize a payment (for example, they’ve followed a redirect) you should present a confirmation page that shows the state of the order. You can do this by polling the order internally.

Because webhook delivery latency isn’t guaranteed, if want to further streamline your confirmation page, you can poll for the status of the associated Source in your client-side code. When you detect that your Source has become chargeable, you can initiate a Charge creation using that Source without waiting for the source.chargeable webhook to arrive.

Be aware that some types of Sources take minutes (or even days) to become chargeable. If you decide to poll the Source, we recommend that you time out at some point and tell the customer that their order is awaiting payment confirmation, then send them a payment confirmation email asynchronously. You can see our recommended customer-facing messaging for each Source status in the table below.

Client-side polling stops if the customer leaves your page. This means that you must also integrate against the source.chargeable webhook to make sure you don’t lose track of your customer’s order.

[webhook](#the-required-use-of-webhooks)

If you’re using Stripe.js, you can use stripe.retrieveSource() to implement your own polling:

[stripe.retrieveSource()](/js#stripe-retrieve-source)

The table below contains recommendations for potential customer-facing messages you can show based on the Source’s status.

After you create a Charge (and if the user is still on your confirmation page), you can show the following messages based on the status of the Charge:

Only confirm your order after you receive the charge.succeeded webhook (this may happen instantly, but it may not). Send an email to the customer at this stage because the payment confirmation can take days for asynchronous payments.

Listen for the source.canceled and source.failed webhooks and make sure to cancel the order associated with the source concerned. If you follow the best practices above, you should never receive a source.canceled webhook for sources that were previously chargeable (as your source.chargeable handler should have created a charge immediately, preventing the source from getting canceled). You’ll still receive source.canceled webhooks for sources that were never chargeable and remained pending, generally an indication that your customer left your checkout flow early. You can also receive a source.failed webhook whenever the Customer refused the payment or a technical failure happened at the payment scheme level.

You should also listen for the charge.failed webhooks to make sure to cancel the order associated with the received charge.

For each of these events, we recommend that you notify your customer that their order failed and to invite them to re-engage in your payment flow, if desired.

## See also

- Supported payment methods

[Supported payment methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Considerations for Stripe Connect platforms

[Considerations for Stripe Connect platforms](/sources/connect)
