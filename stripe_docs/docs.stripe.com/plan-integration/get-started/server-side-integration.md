# Server-side integration

To set up an optimal backend integration, you must authenticate to Stripe, learn API request best practices, and appropriately configure your webhooks.

## Authenticate to Stripe

Stripe provides authentication through API key. It’s also possible to create restricted access keys to further control access to specific resources. You can use the secret and publishable API keys to create tokens, but need secret keys for any server-side authentication.

[restricted access keys](/keys#limit-access)

[secret and publishable API keys](/keys#obtain-api-keys)

Here’s an example API call:

[API request best practices](#API-requests-best-practices)

## API request best practices

Stripe recommends adding an idempotency key to all POST requests. Make sure that the key is unique, such as a universally unique identifier (UUID) or a combination of customer ID and order ID. These keys allow you to safely retry requests if you encounter a network error.

[idempotency key](/api/idempotent_requests)

To store and reuse PaymentMethods, you must attach them to Customer objects.

[PaymentMethods](/api/payment_methods)

[Customer objects](/payments/save-and-reuse)

After attaching the PaymentMethod to a Customer, store the Customer ID and PaymentMethod ID in your system to use it for payments in the future. Because one Customer object can have a list of multiple payment methods, you must specify both the Customer ID and the PaymentMethod ID when creating a charge later on.

[Customer ID](/api/customers/object#customer_object-id)

[PaymentMethod ID](/api/payment_methods/object#payment_method_object-id)

[list of multiple payment methods](/api/payment_methods/list)

Here’s an example creating a Customer and attaching a PaymentMethod:

Refunds are managed using the Refunds API and can be made for full or partial amounts. To refund a transaction with Stripe, you’ll need either the PaymentIntent ID or the Charge ID for the transaction you need to refund.

[Refunds](/api/refunds)

Refunds use your available Stripe balance, and can’t use your pending balance. If your available balance doesn’t have sufficient funds to cover the amount of the refund, Stripe debits the remaining amount from your bank account. You can issue partial refunds, full refunds, and more than one refund against a charge, but you can’t refund a total greater than the original charge amount.

You can issue refunds using the API or the Dashboard. You can’t cancel a refund after you issue it. It takes 5-10 business days for the refund to appear on the customer’s statement. If a customer is curious about the status of their refund, you can provide the ARN so that they can inquire about the refund with their bank.

[API](/api)

[Dashboard](https://dashboard.stripe.com/test/dashboard)

[5-10 business days](https://support.stripe.com/questions/customer-refund-processing-time)

[provide the ARN](https://support.stripe.com/questions/acquirer-reference-number-(arn)-for-refunds)

Here’s an example refund for a PaymentIntent:

Here’s a partial refund example with an amount specified:

Your business is responsible for managing disputes (also known as chargebacks). We recommend that you actively monitor disputes and collect and submit evidence to support the validity of charges where appropriate. We hold disputed funds and deduct them from your Stripe balance pending a decision. We return the funds if you win the dispute.

[disputes (also known as chargebacks)](/disputes)

You can monitor disputes in two ways:

- Use the Stripe Dashboard and email notifications that you can configure in your Dashboard profile.

[Dashboard profile](https://dashboard.stripe.com/settings/user)

- You can fully automate the dispute response and evidence submission through the Disputes API.

[Disputes](/api/disputes)

[Configure webhooks](#configuring-webhooks)

## Configure webhooks

You can use webhooks to capture events that occur on your account (such as payouts to your bank account, refunds, payments, and so on). They’re helpful when handling Stripe events that occur asynchronously, or for those that you want to trigger additional actions for.

[webhooks](/webhooks)

[events](/api/events)

See our recommended webhook for each type:

- charge.succeeded

- charge.failed

- charge.refunded

- refund.created

- refund.failed

- payout.created

- payout.paid

- payout.failed

- payment_intent.succeeded

- payment_intent.payment_failed

- payment_intent.canceled

- radar.early_fraud_warning.created

- charge.dispute.created

- charge.dispute.closed

Use the following resources to set up your webhooks and validate that they’ve been configured correctly:

- Webhooks

[Webhooks](/webhooks)

- Check the webhook signatures

[Check the webhook signatures](/webhooks#verify-events)

- Types of events

[Types of events](/api/events/types)

- Best practices for using webhooks

[Best practices for using webhooks](/webhooks#best-practices)

- Check your webhook configurations

[Check your webhook configurations](https://dashboard.stripe.com/account/webhooks)
