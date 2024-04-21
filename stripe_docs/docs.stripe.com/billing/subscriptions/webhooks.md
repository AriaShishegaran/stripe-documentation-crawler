# Using webhooks with subscriptions

Stripe sends notifications to your app using webhooks. Webhooks are especially important for subscriptions, where most activity occurs asynchronously.

[webhooks](/webhooks)

[subscriptions](/billing/subscriptions/creating)

To use webhooks with your subscriptions:

- Create a webhook endpoint in your app.

- Add logic to handle Stripe events. For subscriptions, these include payment failures and subscription state changes (like moving from trial to an active state).

- Test your webhook endpoint to confirm that it’s working as expected.

Here are some other useful docs about webhooks:

- For more details about setting up and using incoming webhooks, read the guide.

[setting up and using incoming webhooks](/webhooks)

- Use the webhook quickstart for an immersive experience where you learn to build a minimal webhook endpoint.

[webhook quickstart](/webhooks/quickstart)

[Subscription webhook events](#events)

## Subscription webhook events

Stripe triggers events every time a subscription is created or changed. Some events are sent immediately when a subscription is created, while others recur on regular billing intervals.

[events](/api#event_types)

Make sure that your integration properly handles the events. For example, you may want to email a customer if a payment fails or revoke a customer’s access when a subscription is canceled.

The following table describes the most common events related to subscriptions and, where applicable, suggests actions for handling the events.

[Customer](/api/customers/object)

[subscription payment behavior](/billing/subscriptions/overview#subscription-payment-behavior)

[configured](/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)

[free trial ends without a payment method](/billing/subscriptions/trials#create-free-trials-without-payment)

[resumed](/api/subscriptions/resume)

[payment collection is paused](/billing/subscriptions/pause-payment)

[payment collection is unpaused](/billing/subscriptions/pause-payment#unpausing)

[trial period ends](/billing/subscriptions/trials)

[changes](/billing/subscriptions/change)

[integrating with entitlements](/billing/entitlements)

[automatic collection](/invoicing/integration/automatic-advancement-collection)

[finalizing invoices](/invoicing/integration/workflow-transitions#finalized)

- Respond to the notification by sending a request to the Finalize an invoice API.

[Finalize an invoice](/api/invoices/finalize)

- You can send the invoice to the customer. View invoice finalization to learn more.

[invoice finalization](/invoicing/integration/workflow-transitions#finalized)

- Depending on your settings, we automatically charge the default payment method or attempt collection. View emails after finalization to learn more.

[emails after finalization](/invoicing/integration/workflow-transitions#emails)

[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)

[invoice finalization](/invoicing/integration/workflow-transitions#finalized)

- Inspect the Invoice’s last_finalization_error to determine the cause of the error.

[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)

- If you’re using Stripe Tax, check the Invoice object’s automatic_tax field.

[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)

- If automatic_tax[status]=requires_location_inputs, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required customer location.

[customer location](/tax/customer-locations)

- If automatic_tax[status]=failed, retry the request later.

[requires action](/billing/subscriptions/overview#requires-action)

invoice.payment_failed

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription continues to be incomplete only for the subscription’s first invoice. If a payment fails, there are several possible actions to take:

- Notify the customer. Read about how you can configure subscription settings to enable Smart Retries and other revenue recovery features.

[subscription settings](/billing/subscriptions/overview#settings)

[Smart Retries](/billing/revenue-recovery/smart-retries)

- If you’re using PaymentIntents, collect new payment information and confirm the PaymentIntent.

[confirm the PaymentIntent](/api/payment_intents/confirm)

- Update the default payment method on the subscription.

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

[Dashboard](https://dashboard.stripe.com/settings/billing/automatic)

[extra invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items)

[PaymentIntent](/api/payment_intents)

[phases](/billing/subscriptions/subscription-schedules#subscription-schedule-phases)

[released](/api/subscription_schedules/release)

[Handle payment failures](#payment-failures)

## Handle payment failures

Webhook notifications provide a reliable way for Stripe to notify you of payment failures on subscription invoices. Some payment failures are temporary-for example, a card issuer might decline the initial charge but allow an automatic retry. Other payment failures are final and require action, like not having a usable payment method for the customer.

invoice.payment_failed

A payment for an invoice failed. The status of the PaymentIntent changes to requires_payment_method. The status of the subscription changes to incomplete. If a payment fails, there are several possible actions to take:

- Notify the customer.

- If you’re using PaymentIntents, collect new payment information and confirm the PaymentIntent.

[confirm the PaymentIntent](/api/payment_intents/confirm)

- Update the default payment method on the subscription.

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

- Consider enabling Smart Retries.

[Smart Retries](/billing/revenue-recovery/smart-retries)

For more details on how to handle payment failures that require a payment method, see the subscriptions overview guide.

[handle payment failures that require a payment method](/billing/subscriptions/overview#requires-payment-method)

[Handle payments that require additional action](#additional-action)

## Handle payments that require additional action

Some payment methods might require additional steps to complete, such as customer authentication. If you receive these events, your app must notify the customer to complete the required action. To learn how to handle events that require additional action, read the subscription overview guide.

[handle events that require additional action](/billing/subscriptions/overview#requires-action)

[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)

[invoice finalization](/invoicing/integration/workflow-transitions#finalized)

- Inspect the Invoice’s last_finalization_error to determine the cause of the error.

[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)

- If you’re using Stripe Tax, check the Invoice object’s automatic_tax field.

[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)

- If automatic_tax[status]=requires_location_inputs, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required customer location.

[customer location](/tax/customer-locations)

- If automatic_tax[status]=failed, retry the request later.

invoice.payment_failed

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription changes to incomplete. If a payment fails, there are several possible actions to take:

- Notify the customer.

- If you’re using PaymentIntents, collect new payment information and confirm the PaymentIntent.

[confirm the PaymentIntent](/api/payment_intents/confirm)

- Update the default payment method on the subscription.

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

- Consider enabling Smart Retries.

[Smart Retries](/billing/revenue-recovery/smart-retries)

invoice.payment_action_required

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription changes to incomplete. If a payment fails, there are several possible actions to take:

- Notify the customer.

- If you’re using PaymentIntents, collect new payment information and confirm the PaymentIntent.

[confirm the PaymentIntent](/api/payment_intents/confirm)

- Update the default payment method on the subscription.

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

- Consider enabling Smart Retries.

[Smart Retries](/billing/revenue-recovery/smart-retries)

[Track active subscriptions](#active-subscriptions)

## Track active subscriptions

Subscriptions require coordination between your site and Stripe-the success or failure of a customer’s recurring payments determines whether they can continue to access to your product or service.

For typical integrations, you store customers’ credentials and a mapped timestamp value that represents the access expiration date for that customer on your site when a customer subscribes. When the customer logs in, you check whether the timestamp is still in the future. If the timestamp is in the future when the customer logs in, the account is active and the customer should still have access to the service.

When the subscription renews, Stripe bills the customer and tries to collect payment by either automatically charging the payment method on file, or emailing the invoice to customers. Stripe notifies your site of the invoice status through webhooks:

[renews](/billing/subscriptions/overview#subscription-lifecycle)

[automatically charging](/invoicing/automatic-charging)

[emailing the invoice](/invoicing/integration#accept-invoice-payment)

- Your site receives an invoice.paid event.When automatically charging a payment method, your site first receives an invoice.upcoming event at the webhook endpoint a few days before renewal. You can listen for this event to add extra invoice items to the upcoming invoice. If collection_method=send_invoice, Stripe doesn’t send an invoice.upcoming event.

Your site receives an invoice.paid event.

- When automatically charging a payment method, your site first receives an invoice.upcoming event at the webhook endpoint a few days before renewal. You can listen for this event to add extra invoice items to the upcoming invoice. If collection_method=send_invoice, Stripe doesn’t send an invoice.upcoming event.

[add extra invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items)

- Your webhook endpoint finds the customer the payment was made for.

Your webhook endpoint finds the customer the payment was made for.

- Your webhook endpoint updates the customer’s access expiration date in your database to the appropriate date in the future (plus a day or two for leeway).

Your webhook endpoint updates the customer’s access expiration date in your database to the appropriate date in the future (plus a day or two for leeway).

[Catch subscription status changes](#state-changes)

## Catch subscription status changes

Make sure that your integration properly monitors and handles transitions between the subscription statuses described in the following table.

Some status changes require special attention:

- A few days before a trial ends and the subscription moves from trialing to active, you receive a customer.subscription.trial_will_end event. When you receive this event, verify that you have a payment method on the customer so you can bill them. Optionally, notify the customer that they will be charged.

A few days before a trial ends and the subscription moves from trialing to active, you receive a customer.subscription.trial_will_end event. When you receive this event, verify that you have a payment method on the customer so you can bill them. Optionally, notify the customer that they will be charged.

- When a subscription changes to past_due, notify the customer directly and ask them to update their payment details. Stripe offers several features that help automate this process-read more about revenue recovery.

When a subscription changes to past_due, notify the customer directly and ask them to update their payment details. Stripe offers several features that help automate this process-read more about revenue recovery.

[revenue recovery](/billing/revenue-recovery)

- When a subscription changes to canceled or unpaid, revoke access to your product.

When a subscription changes to canceled or unpaid, revoke access to your product.

[requires action](#requires-action)

[subscription settings](/billing/subscriptions/overview#settings)

[Smart Retries](/billing/revenue-recovery/smart-retries)

[trial_settings.end_behavior.missing_payment_method](/billing/subscriptions/trials#create-free-trials-without-payment)

[resume the subscription](/billing/subscriptions/trials#resume-a-paused-subscription)

[Webhooks and invoices](#understand)

## Webhooks and invoices

We recommend registering a webhook endpoint to keep track of invoice statuses. Tracking invoice statuses is especially important for subscription-generated invoices.

When you enable automatic collection, Stripe automatically finalizes and begins automatic collection of the invoice.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

[invoice](/billing/invoices/subscription)

To ensure that your subscription integration works as expected, including continuing to receive payment on subscription-generated invoices, you must correctly handle the webhooks related to invoice finalization. Successfully finalizing invoices and properly handling invoice finalization failures is critical to a subscriptions integration.

- If Stripe fails to receive a successful response to invoice.created, then finalizing all invoices with automatic collection will be delayed for up to 72 hours.

If Stripe fails to receive a successful response to invoice.created, then finalizing all invoices with automatic collection will be delayed for up to 72 hours.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

- Responding properly to invoice.created includes handling all webhook endpoints configured for your account, along with the webhook endpoints of any platforms that you’ve connected to.

Responding properly to invoice.created includes handling all webhook endpoints configured for your account, along with the webhook endpoints of any platforms that you’ve connected to.

- Updating a subscription in a way that synchronously attempts payment (on the initial invoice, and on some kinds of updates) doesn’t cause this delay.

Updating a subscription in a way that synchronously attempts payment (on the initial invoice, and on some kinds of updates) doesn’t cause this delay.

- If the invoice fails to be finalized, payments can’t be collected on the invoice. Ensure that you’re listening for the invoice.finalization_failed event in your webhook endpoint.

If the invoice fails to be finalized, payments can’t be collected on the invoice. Ensure that you’re listening for the invoice.finalization_failed event in your webhook endpoint.

[finalizing invoices](/invoicing/integration/workflow-transitions#finalized)

- Respond to the notification by sending a request to the Finalize an invoice API.

[Finalize an invoice](/api/invoices/finalize)

- You can send the invoice to the customer. Read more about invoice finalization.

[invoice finalization](/invoicing/integration/workflow-transitions#finalized)

- Depending on your settings, Stripe automatically charges the default payment method or attempts collection. Read more about emails after finalization.

[emails after finalization](/invoicing/integration/workflow-transitions#emails)

[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)

[invoice finalization](/invoicing/integration/workflow-transitions#finalized)

- Inspect the Invoice’s last_finalization_error to determine the cause of the error.

[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)

- If you’re using Stripe Tax, check the Invoice object’s automatic_tax field.

[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)

- If automatic_tax[status]=requires_location_inputs, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required customer location.

[customer location](/tax/customer-locations)

- If automatic_tax[status]=failed, retry the request later.

Stripe waits an hour after receiving a successful response to the invoice.created event before attempting payment. If we don’t receive a successful response within 72 hours, we attempt to finalize and send the invoice.

In case you want to treat one-off invoices differently than subscription invoices, check the subscription property in the webhook body. This indicates whether the invoice was created for a subscription.

In live mode, if your webhook endpoint doesn’t respond properly, Stripe continues retrying the webhook notification for up to 3 days with an exponential back off. In test mode, we retry three times over a few hours. During that time, we won’t attempt to charge the customer unless we receive a successful response. We’ll also send you an email to notify you that the webhook is failing.

This behavior applies to all webhook endpoints defined on your account, including cases where a Connect application or other third-party service is having trouble handling incoming webhooks.

[Connect application](https://stripe.com/works-with)

If Stripe can’t finalize an invoice, it sends a invoice.finalization_failed event to your webhook endpoint. Subscriptions remain active if invoices can’t be finalized, which means that users may still be able to access your product while you’re not able to collect payments. Make sure to take action on invoices that fail finalization. You can’t collect payments on an invoice that isn’t finalized.

[event](/api/events/types#event_types-invoice.finalization_failed)

To determine why the invoice finalization failed, look at the Invoice object’s last_finalization_error field, which provides more information about the failure, including how to proceed.

[field](/api/invoices/object#invoice_object-last_finalization_error)

If you’re using Stripe Tax, check the automatic_tax field to determine if the failure is related to customer location validation. If Stripe Tax can’t find a recognized customer location, the invoice can’t be finalized. Learn how to handle invoice finalization failures.

[field](/api/invoices/object#invoice_object-automatic_tax)

[customer location validation](/tax/subscriptions#handling-location-validation)

[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)

[Testing](#testing)

## Testing

To test webhooks, you have two options:

[webhooks](/webhooks)

- Perform actions in test mode that send legitimate events to your endpoint. For instance, to trigger the charge.succeeded event, you can use a test card that produces a successful charge.

[charge.succeeded](/api#event_types-charge.succeeded)

[test card that produces a successful charge](#cards)

- Trigger events using the Stripe CLI or using Stripe for Visual Studio Code.

[Trigger events using the Stripe CLI](/webhooks#test-webhook)

[using Stripe for Visual Studio Code](/stripe-vscode#webhooks)

## See also

- Subscription lifecycle

[Subscription lifecycle](/billing/subscriptions/overview#subscription-lifecycle)

- Testing subscriptions

[Testing subscriptions](/billing/testing)
