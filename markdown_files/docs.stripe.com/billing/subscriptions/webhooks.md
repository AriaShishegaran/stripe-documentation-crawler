htmlUsing webhooks with subscriptions | Stripe Documentation[Skip to content](#main-content)Subscription webhooks[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fwebhooks)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fwebhooks)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)# Using webhooks with subscriptions

Learn to use webhooks to receive notifications of subscription activity.Stripe sends notifications to your app using webhooks. Webhooks are especially important for subscriptions, where most activity occurs asynchronously.

To use webhooks with your subscriptions:

1. Create a webhook endpoint in your app.
2. Add logic to handle Stripe events. For subscriptions, these include payment failures and subscription state changes (like moving from trial to an active state).
3. Test your webhook endpoint to confirm that it’s working as expected.

Here are some other useful docs about webhooks:

- For more details about[setting up and using incoming webhooks](/webhooks), read the guide.
- Use the[webhook quickstart](/webhooks/quickstart)for an immersive experience where you learn to build a minimal webhook endpoint.

[Subscription webhook events](#events)Stripe triggers events every time a subscription is created or changed. Some events are sent immediately when a subscription is created, while others recur on regular billing intervals.

Make sure that your integration properly handles the events. For example, you may want to email a customer if a payment fails or revoke a customer’s access when a subscription is canceled.

The following table describes the most common events related to subscriptions and, where applicable, suggests actions for handling the events.

EventDescription`customer.created`Sent when a[Customer](/api/customers/object)is successfully created.`customer.subscription.created`Sent when the subscription is created. The subscription`status`might be`incomplete`if customer authentication is required to complete the payment or if you set`payment_behavior`to`default_incomplete`. View[subscription payment behavior](/billing/subscriptions/overview#subscription-payment-behavior)to learn more.`customer.subscription.deleted`Sent when a customer’s subscription ends.`customer.subscription.paused`Sent when a subscription’s`status`changes to`paused`.For example, this is sent when a subscription is[configured](/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)to pause when a[free trial ends without a payment method](/billing/subscriptions/trials#create-free-trials-without-payment).Invoicing won’t occur until the subscription is[resumed](/api/subscriptions/resume).We don’t send this event if[payment collection is paused](/billing/subscriptions/pause-payment)because invoices continue to be created during that time period.`customer.subscription.resumed`Sent when a subscription previously in a`paused`status is resumed. This doesn’t apply when[payment collection is unpaused](/billing/subscriptions/pause-payment#unpausing).`customer.subscription.trial_will_end`Sent three days before the[trial period ends](/billing/subscriptions/trials). If the trial is less than three days, this event is triggered.`customer.subscription.updated`Sent when a subscription starts or[changes](/billing/subscriptions/change). For example, renewing a subscription, adding a coupon, applying a discount, adding an invoice item, and changing plans all trigger this event.`entitlements.active_entitlement_summary.updated`Sent when a customer’s active entitlements are updated. When you receive this event, you can provision or de-provision access to your product’s features. Read more about[integrating with entitlements](/billing/entitlements).`invoice.created`Sent when an invoice is created for a new or renewing subscription. If Stripe fails to receive a successful response to`invoice.created`, then finalizing all invoices with[automatic collection](/invoicing/integration/automatic-advancement-collection)is delayed for up to 72 hours. Read more about[finalizing invoices](/invoicing/integration/workflow-transitions#finalized).- Respond to the notification by sending a request to the[Finalize an invoice](/api/invoices/finalize)API.

`invoice.finalized`Sent when an invoice is successfully finalized and ready to be paid.- You can send the invoice to the customer. View[invoice finalization](/invoicing/integration/workflow-transitions#finalized)to learn more.
- Depending on your settings, we automatically charge the default payment method or attempt collection. View[emails after finalization](/invoicing/integration/workflow-transitions#emails)to learn more.

`invoice.finalization_failed`The invoice couldn’t be finalized. Learn how to[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)by reading the guide. Learn more about[invoice finalization](/invoicing/integration/workflow-transitions#finalized)in the invoices overview guide.- Inspect the Invoice’s[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)field.
- If`automatic_tax[status]=requires_location_inputs`, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required[customer location](/tax/customer-locations).
- If`automatic_tax[status]=failed`, retry the request later.

`invoice.paid`Sent when the invoice is successfully paid. You can provision access to your product when you receive this event and the subscription`status`is`active`.`invoice.payment_action_required`Sent when the invoice requires customer authentication. Learn how to handle the subscription when the invoice[requires action](/billing/subscriptions/overview#requires-action).invoice.payment_failed

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription continues to be incomplete only for the subscription’s first invoice. If a payment fails, there are several possible actions to take:

- Notify the customer. Read about how you can configure[subscription settings](/billing/subscriptions/overview#settings)to enable[Smart Retries](/billing/revenue-recovery/smart-retries)and other revenue recovery features.
- If you’re using PaymentIntents, collect new payment information and[confirm the PaymentIntent](/api/payment_intents/confirm).
- Update the[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)on the subscription.

`invoice.upcoming`Sent a few days prior to the renewal of the subscription. The number of days is based on the number set forUpcoming renewal eventsin the[Dashboard](https://dashboard.stripe.com/settings/billing/automatic). For existing subscriptions, changing the number of days takes effect on the next billing period. You can still add[extra invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items), if needed.`invoice.updated`Sent when a payment succeeds or fails. If payment is successful the`paid`attribute is set to`true`and the`status`is`paid`. If payment fails,`paid`is set to`false`and the`status`remains`open`. Payment failures also trigger  a`invoice.payment_failed`event.`payment_intent.created`Sent when a[PaymentIntent](/api/payment_intents)is created.`payment_intent.succeeded`Sent when a PaymentIntent has successfully completed payment.`subscription_schedule.aborted`Sent when a subscription schedule is canceled because payment delinquency terminated the related subscription.`subscription_schedule.canceled`Sent when a subscription schedule is canceled, which also cancels any active associated subscription.`subscription_schedule.completed`Sent when all[phases](/billing/subscriptions/subscription-schedules#subscription-schedule-phases)of a subscription schedule complete.`subscription_schedule.created`Sent when a new subscription schedule is created.`subscription_schedule.expiring`Sent 7 days before a subscription schedule is set to expire.`subscription_schedule.released`Sent when a subscription schedule is[released](/api/subscription_schedules/release), or stopped and disassociated from the subscription, which remains.`subscription_schedule.updated`Sent when a subscription schedule is updated.[Handle payment failures](#payment-failures)Webhook notifications provide a reliable way for Stripe to notify you of payment failures on subscription invoices. Some payment failures are temporary-for example, a card issuer might decline the initial charge but allow an automatic retry. Other payment failures are final and require action, like not having a usable payment method for the customer.

EventDescriptioninvoice.payment_failed

A payment for an invoice failed. The status of the PaymentIntent changes to requires_payment_method. The status of the subscription changes to incomplete. If a payment fails, there are several possible actions to take:

- Notify the customer.
- If you’re using PaymentIntents, collect new payment information and[confirm the PaymentIntent](/api/payment_intents/confirm).
- Update the[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)on the subscription.
- Consider enabling[Smart Retries](/billing/revenue-recovery/smart-retries).

For more details on how to handle payment failures that require a payment method, see the subscriptions overview guide.

[Handle payments that require additional action](#additional-action)Some payment methods might require additional steps to complete, such as customer authentication. If you receive these events, your app must notify the customer to complete the required action. To learn how to handle events that require additional action, read the subscription overview guide.

EventDescription`invoice.finalization_failed`The invoice couldn’t be finalized. Learn how to[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)by reading the guide. Learn more about[invoice finalization](/invoicing/integration/workflow-transitions#finalized)in the invoices overview guide.- Inspect the Invoice’s[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)field.
- If`automatic_tax[status]=requires_location_inputs`, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required[customer location](/tax/customer-locations).
- If`automatic_tax[status]=failed`, retry the request later.

invoice.payment_failed

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription changes to incomplete. If a payment fails, there are several possible actions to take:

- Notify the customer.
- If you’re using PaymentIntents, collect new payment information and[confirm the PaymentIntent](/api/payment_intents/confirm).
- Update the[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)on the subscription.
- Consider enabling[Smart Retries](/billing/revenue-recovery/smart-retries).

invoice.payment_action_required

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription changes to incomplete. If a payment fails, there are several possible actions to take:

- Notify the customer.
- If you’re using PaymentIntents, collect new payment information and[confirm the PaymentIntent](/api/payment_intents/confirm).
- Update the[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)on the subscription.
- Consider enabling[Smart Retries](/billing/revenue-recovery/smart-retries).

[Track active subscriptions](#active-subscriptions)Subscriptions require coordination between your site and Stripe-the success or failure of a customer’s recurring payments determines whether they can continue to access to your product or service.

For typical integrations, you store customers’ credentials and a mapped timestamp value that represents the access expiration date for that customer on your site when a customer subscribes. When the customer logs in, you check whether the timestamp is still in the future. If the timestamp is in the future when the customer logs in, the account is active and the customer should still have access to the service.

When the subscription renews, Stripe bills the customer and tries to collect payment by either automatically charging the payment method on file, or emailing the invoice to customers. Stripe notifies your site of the invoice status through webhooks:

1. Your site receives an invoice.paid event.

  - When automatically charging a payment method, your site first receives an`invoice.upcoming`event at the webhook endpoint a few days before renewal. You can listen for this event to[add extra invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items)to the upcoming invoice. If`collection_method=send_invoice`, Stripe doesn’t send an`invoice.upcoming`event.


2. Your webhook endpoint finds the customer the payment was made for.


3. Your webhook endpoint updates the customer’s access expiration date in your database to the appropriate date in the future (plus a day or two for leeway).



[Catch subscription status changes](#state-changes)Make sure that your integration properly monitors and handles transitions between the subscription statuses described in the following table.

Some status changes require special attention:

- A few days before a trial ends and the subscription moves from trialing to active, you receive a customer.subscription.trial_will_end event. When you receive this event, verify that you have a payment method on the customer so you can bill them. Optionally, notify the customer that they will be charged.


- When a subscription changes to past_due, notify the customer directly and ask them to update their payment details. Stripe offers several features that help automate this process-read more about revenue recovery.


- When a subscription changes to canceled or unpaid, revoke access to your product.



StatusDescription`trialing`The subscription is currently in a trial period and it’s safe to provision your product for your customer. The subscription transitions automatically to`active`when the first payment is made.`active`The subscription is in good standing and the most recent payment is successful. It’s safe to provision your product for your customer.`incomplete`A successful payment needs to be made within 23 hours to activate the subscription. Or the payment[requires action](#requires-action), like customer authentication. Subscriptions can also be`incomplete`if there’s a pending payment and the PaymentIntent status would be`processing`.`incomplete_expired`The initial payment on the subscription failed and no successful payment was made within 23 hours of creating the subscription. These subscriptions don’t bill customers. This status exists so you can track customers that failed to activate their subscriptions.`past_due`Payment on the latestfinalizedinvoice either failed or wasn’t attempted. The subscription continues to create invoices. Your[subscription settings](/billing/subscriptions/overview#settings)determine the subscription’s next state. If the invoice is still unpaid after all[Smart Retries](/billing/revenue-recovery/smart-retries)have been attempted, you can configure the subscription to move to`canceled`,`unpaid`, or leave it as`past_due`. To move the subscription to`active`, pay the most recent invoice before its due date.`canceled`The subscription has been canceled. During cancellation, automatic collection for all unpaid invoices is disabled (`auto_advance=false`). This is a terminal state that can’t be updated.`unpaid`The latest invoice hasn’t been paid but the subscription remains in place. The latest invoice remains open and invoices continue to be generated but payments aren’t attempted. You should revoke access to your product when the subscription is`unpaid`since payments were already attempted and retried when it was`past_due`. To move the subscription to`active`, pay the most recent invoice before its due date.`paused`The subscription has ended its trial period without a default payment method and the[trial_settings.end_behavior.missing_payment_method](/billing/subscriptions/trials#create-free-trials-without-payment)is set to`pause`. Invoices will no longer be created for the subscription. After a default payment method has been attached to the customer, you can[resume the subscription](/billing/subscriptions/trials#resume-a-paused-subscription).[Webhooks and invoices](#understand)We recommend registering a webhook endpoint to keep track of invoice statuses. Tracking invoice statuses is especially important for subscription-generated invoices.

When you enable automatic collection, Stripe automatically finalizes and begins automatic collection of the invoice.

To ensure that your subscription integration works as expected, including continuing to receive payment on subscription-generated invoices, you must correctly handle the webhooks related to invoice finalization. Successfully finalizing invoices and properly handling invoice finalization failures is critical to a subscriptions integration.

- If Stripe fails to receive a successful response to invoice.created, then finalizing all invoices with automatic collection will be delayed for up to 72 hours.


- Responding properly to invoice.created includes handling all webhook endpoints configured for your account, along with the webhook endpoints of any platforms that you’ve connected to.


- Updating a subscription in a way that synchronously attempts payment (on the initial invoice, and on some kinds of updates) doesn’t cause this delay.


- If the invoice fails to be finalized, payments can’t be collected on the invoice. Ensure that you’re listening for the invoice.finalization_failed event in your webhook endpoint.



### Webhook events related to invoice finalization

EventDescription`invoice.created`The invoice was successfully created and is ready to be finalized. Read the docs to learn more about[finalizing invoices](/invoicing/integration/workflow-transitions#finalized).- Respond to the notification by sending a request to the[Finalize an invoice](/api/invoices/finalize)API.

`invoice.finalized`The invoice was successfully finalized and is ready to be paid.- You can send the invoice to the customer. Read more about[invoice finalization](/invoicing/integration/workflow-transitions#finalized).
- Depending on your settings, Stripe automatically charges the default payment method or attempts collection. Read more about[emails after finalization](/invoicing/integration/workflow-transitions#emails).

`invoice.finalization_failed`The invoice couldn’t be finalized. Learn how to[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)by reading the guide. Learn more about[invoice finalization](/invoicing/integration/workflow-transitions#finalized)in the invoices overview guide.- Inspect the Invoice’s[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)field.
- If`automatic_tax[status]=requires_location_inputs`, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required[customer location](/tax/customer-locations).
- If`automatic_tax[status]=failed`, retry the request later.

### Successful invoice finalization

Stripe waits an hour after receiving a successful response to the invoice.created event before attempting payment. If we don’t receive a successful response within 72 hours, we attempt to finalize and send the invoice.

In case you want to treat one-off invoices differently than subscription invoices, check the subscription property in the webhook body. This indicates whether the invoice was created for a subscription.

In live mode, if your webhook endpoint doesn’t respond properly, Stripe continues retrying the webhook notification for up to 3 days with an exponential back off. In test mode, we retry three times over a few hours. During that time, we won’t attempt to charge the customer unless we receive a successful response. We’ll also send you an email to notify you that the webhook is failing.

This behavior applies to all webhook endpoints defined on your account, including cases where a Connect application or other third-party service is having trouble handling incoming webhooks.

### Invoice finalization failure

If Stripe can’t finalize an invoice, it sends a invoice.finalization_failed event to your webhook endpoint. Subscriptions remain active if invoices can’t be finalized, which means that users may still be able to access your product while you’re not able to collect payments. Make sure to take action on invoices that fail finalization. You can’t collect payments on an invoice that isn’t finalized.

To determine why the invoice finalization failed, look at the Invoice object’s last_finalization_error field, which provides more information about the failure, including how to proceed.

If you’re using Stripe Tax, check the automatic_tax field to determine if the failure is related to customer location validation. If Stripe Tax can’t find a recognized customer location, the invoice can’t be finalized. Learn how to handle invoice finalization failures.

[Testing](#testing)To test webhooks, you have two options:

1. Perform actions in test mode that send legitimate events to your endpoint. For instance, to trigger the[charge.succeeded](/api#event_types-charge.succeeded)event, you can use a[test card that produces a successful charge](#cards).
2. [Trigger events using the Stripe CLI](/webhooks#test-webhook)or[using Stripe for Visual Studio Code](/stripe-vscode#webhooks).

## See also

- [Subscription lifecycle](/billing/subscriptions/overview#subscription-lifecycle)
- [Testing subscriptions](/billing/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Subscription webhook events](#events)[Handle payment failures](#payment-failures)[Handle payments that require additional action](#additional-action)[Track active subscriptions](#active-subscriptions)[Catch subscription status changes](#state-changes)[Webhooks and invoices](#understand)[Testing](#testing)[See also](#see-also)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`