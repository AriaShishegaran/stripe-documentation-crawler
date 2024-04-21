# Accept a bank transfer

The first time you accept a bank transfer payment from a customer, Stripe generates a virtual bank account for them, which you can then share with them directly. All future bank transfer payments from this customer get sent to this bank account. In some countries, Stripe also provides you with a unique transfer reference number that your customer should include with each transfer to make it easier to match the transfer against outstanding payments. Some countries have limits on the number of virtual bank account numbers that you can create for free.

You can find an overview of the common steps when accepting a bank transfer payment in the following sequence diagram:

## Handling underpayments and overpayments

With bank transfer payments, it’s possible that the customer sends you more or less than the expected payment amount. If the customer sends too little, Stripe partially funds an open payment intent. Invoices won’t be partially funded and remain open until incoming funds cover the full invoice amount.

If the customer sends more than the expected amount, Stripe attempts to reconcile the incoming funds against an open payment and keep the remaining excess amount in the customer cash balance. You can find more details on how Stripe handles reconciliation in the reconciliation section of our documentation.

[reconciliation section](/payments/customer-balance/reconciliation)

When a customer underpays:

When a customer overpays:

## Handling multiple open payments or invoices

You might have multiple open payments or invoices which can be paid with a bank transfer. In the default setup, Stripe attempts to automatically reconcile the bank transfer by using information like the transfer’s reference code or the amount transferred.

[automatically reconcile](/payments/customer-balance/reconciliation)

You can disable automatic reconciliation and manually reconcile payments and invoices yourself. You can override the automatic reconciliation behavior on a per-customer basis by setting reconciliation mode to manual.

[manually reconcile](/payments/customer-balance/reconciliation#cash-manual-reconciliation)

[reconciliation mode](/api/customers/create#create_customer-cash_balance-settings-reconciliation_mode)

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create or retrieve a CustomerServer-side](#web-create-a-customer)

## Create or retrieve a CustomerServer-side

You must associate a Customer object to reconcile each bank transfer payment. If you have an existing Customer object, you can skip this step. Otherwise, create a new Customer object.

[Customer](/api/customers)

[Create and confirm a PaymentIntentServer-side](#web-create-and-confirm-payment-intent)

## Create and confirm a PaymentIntentServer-side

A PaymentIntent is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. Create and confirm a PaymentIntent on the server, specifying the amount and currency you want to collect.

[PaymentIntent](/api/payment_intents/object)

Before creating a Payment Intent, make sure to turn Bank transfer on in the payment methods settings page of your Dashboard.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

With Dynamic payment methods, Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

[https://example.com/return_url](https://example.com/return_url)

In the latest version of the API, specifying the automatic_payment_methods parameter is optional because Stripe enables its functionality by default.

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a succeeded status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must reconcile customer balances within a certain period based on your location.

[reconcile customer balances within a certain period based on your location](/payments/customer-balance/reconciliation)

[Instruct the customer to complete a bank transferClient-side](#web-complete-bank-transfer)

## Instruct the customer to complete a bank transferClient-side

If the customer balance isn’t high enough to cover the request amount, the PaymentIntent shows a requires_action status. The response has a next_action field containing a type value of display_bank_transfer_instructions. The next_action[display_bank_transfer_instructions] hash contains information to display to your customer so that they can complete the bank transfer.

In live mode, Stripe supplies each customer with a unique set of bank transfer details. In contrast, Stripe offers invalid bank transfer details to all customers in test mode. Unlike live mode, these invalid details might not always be unique.

[test mode](/test-mode)

[type](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-type)

[reference](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-reference)

[amount_remaining](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-amount_remaining)

[currency](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-currency)

[financial_addresses](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions)

[hosted_instructions_url](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url)

Example of an aba hash:

- ach

- domestic_wire_us

Example of a swift hash:

- swift

After instructing your customer to initiate a transfer with their bank using the information you provide, it can take up to 5 days for the transfer to complete. The settlement timing depends on the banking rails that the transfer arrived through to Stripe:

- ACH transfers arrive within 1-3 business days.

- Domestic wire transfers (Fedwire) arrive on the same day (depending on whether the transfer is sent before the bank’s cut-off time).

- International wire transfers (SWIFT) arrive within 1-5 business days.

[Confirm the PaymentIntent succeeded](#web-confirm-success)

## Confirm the PaymentIntent succeeded

The PaymentIntent stays in a requires_action status until funds arrive in the bank account. When funds are ready, the PaymentIntent status updates from requires_action to succeeded.

You need to set up your webhook endpoint to start receiving the payment_intent.partially_funded event.

[webhook](/webhooks)

You can add a webhook from the Dashboard.

[add a webhook from the Dashboard](https://dashboard.stripe.com/webhooks/create)

Alternatively, you can use the Webhook Endpoints API to start receiving the payment_intent.partially_funded event.

[Webhook Endpoints API](/api/webhook_endpoints)

[payment_intent.partially_funded](/api/events/types#event_types-payment_intent.partially_funded)

Stripe sends the following events during the payment funding flow when we update the PaymentIntent.

[confirm](/api/payment_intents/confirm)

When you change the amount of a partially funded PaymentIntent, the funds are returned to the customer balance. If other PaymentIntents are open, Stripe funds those automatically. If the customer is configured for manual reconciliation, you need to apply the funds again.

[apply the funds](/api/payment_intents/apply_customer_balance)

We recommend using webhooks to confirm the charge has succeeded and to notify the customer that the payment is complete.

[using webhooks](/payments/payment-intents/verifying-status#webhooks)

You can view all pending bank transfer PaymentIntents in the Dashboard by applying the Waiting on funding filter to Status .

[Dashboard](https://dashboard.stripe.com/payments)

[Test your integration](#test-your-integration)

## Test your integration

You can test your integration by simulating an incoming bank transfer using either the Dashboard or an HTTP request.

To simulate a bank transfer using the Dashboard, navigate to the customer’s page in the Dashboard. Under Payment methods, click Add and select Fund cash balance (testmode only).

You can make an API call to simulate a bank transfer.

[Handling temporary availability issues](#handling-temporary-availability-issues)

## Handling temporary availability issues

The following error codes indicate temporary issues with the availability of the payment method:

[API-wide rate limits](/rate-limits)

If you anticipate heavy usage in general or because of an upcoming event, contact us as soon as you know about it.

[OptionalCollecting payment method options from your customer](#collect-payment-method-options)

## OptionalCollecting payment method options from your customer

[OptionalSend payment instruction emails](#instruction-emails)

## OptionalSend payment instruction emails
