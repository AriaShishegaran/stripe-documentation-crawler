# Testing Stripe Billing

- Use test cards and account numbers to trigger different scenarios, like payment failures or required authentication.

[cards](/testing#cards)

[account numbers](/testing#test-account-numbers)

- Use test clocks to simulate Billing objects through time and test events at different milestones, like the end of a free trial or annual plan.

[test clocks](/billing/testing/test-clocks)

- Read the general testing doc to learn about fundamental testing common to all of Stripe.

[general testing doc](/testing)

Thoroughly test your integration before you expose it to customers or use it for any live activity. Use the resources on this page in addition to any organizational guidelines (for example, runbooks, quality gates, or development checklists) to help determine whether your integration is production-ready.

## Go-live principles

Before taking your integration live, review these Stripe checklists:

- Account checklist

[Account checklist](/get-started/checklist/account)

- Development checklist

[Development checklist](/get-started/checklist/go-live)

- Website checklist

[Website checklist](/get-started/checklist/website)

Here’s what a typical integration flow looks like.

For subscription and recurring revenue integrations, make sure that, at a minimum, the following components work as expected.

The table lists the event notifications for each component. You can configure your integration to listen for these events with webhooks. Read this guide to learn more about event notifications and testing.

[webhook](/webhooks)

[event notifications](#webhooks)

[Elements](/payments/elements)

[Stripe API](/api)

[manage Customers](/billing/customer#manage-customers)

- customer.created

- customer.subscription.created

[Invoices](/api/invoices)

[invoices for subscriptions](/billing/invoices/subscription)

[use cases](/billing/testing/test-clocks/api-advanced-usage#use-cases)

- invoice.created

- invoice.finalized

- invoice.finalization_failed

- invoice.paid

- invoice.payment_action_required

- invoice.payment_failed

- invoice.upcoming

- invoice.updated

[customer portal](/billing/subscriptions/customer-portal)

[subscriptions](/billing/subscriptions/creating)

[test mode](/test-mode)

[integration guide](/customer-management)

- customer.subscription.deleted

- customer.subscription.paused

- customer.subscription.resumed

- customer.subscription.updated

[Learn how to test trials with test clocks](#trials)

[subscription trials guide](/billing/subscriptions/trials)

- customer.subscription.trial_will_end

- customer.subscription.updated

[Learn how to test payment failures](#payment-failures)

- invoice.finalization_failed

- invoice.payment_failed

- invoice.payment_action_required

## Test clocks

Test clocks allow you to simulate Billing objects, like subscriptions, through time in test mode so you don’t have to wait a year to see how your integration handles a payment failure for an annual renewal. You don’t need to write any code with test clocks: you can create simulations in the Dashboard. You can also access them through the API. Learn more about test clocks and common use cases for them.

[subscriptions](/billing/subscriptions/creating)

[test mode](/test-mode)

[test clocks](/billing/testing/test-clocks)

[use cases](/billing/testing/test-clocks)

## Test subscription trial periods

First, follow these steps to start using test clocks:

- Create a test clock

[Create a test clock](/billing/testing/test-clocks/api-advanced-usage#create-clock)

- Set up your testing simulation

[Set up your testing simulation](/billing/testing/test-clocks/api-advanced-usage#setup-simulation)

- Advance the clock’s time

[Advance the clock’s time](/billing/testing/test-clocks/api-advanced-usage#advance-clock)

- Monitor and handle the changes

[Monitor and handle the changes](/billing/testing/test-clocks/api-advanced-usage#monitor-changes)

- Update the simulation

[Update the simulation](/billing/testing/test-clocks/api-advanced-usage#update-simulation)

Next, you can start testing trials with test clocks. Let’s say that you want customers to try your product for free with a seven-day trial before they start paying and want to collect payment information up front. To simulate this situation using test clocks, follow these steps:

- Create a new test clock and set its frozen_time to January 1.

- Add a customer and include their payment method. In this case, use a 4242424242424242 test card.

[test card](/testing#cards)

- Create a subscription and add a seven-day free trial period:

To add a trial period to an existing subscription using the Dashboard:

Find the subscription you want to change.

- Click Actions.

- Click Update subscription.

- Click Add free trial and enter seven in Free trial days field.

- Click Update subscription.

- After creating a subscription with a seven-day free trial period, a subscription is created in a trialing state. An invoice of $0.00 is generated due to the free trial.

- Advance the date to January 5 to see the customer.subscription.trial_will_end event notification. Stripe sends the notification three days before the trial ends. You can use this webhook event to inform your customers that the trial ends soon.

[customer.subscription.trial_will_end](/api/events/types#event_types-customer.subscription.trial_will_end)

- Advance the date to January 8 to see that the subscription is now paid and an invoice for 50 EUR is created.

- Advance the date by one cycle (for example, to February 8 for a monthly subscription) to see the subscription renew successfully.

## Test subscription webhook notifications

Subscriptions integrations rely heavily on webhooks. You set up a webhook endpoint on your server and specify which event notifications to listen for. Stripe emits notifications for events like a subscription upgrade or cancellation.

[webhooks](/webhooks)

You can test webhooks by either creating actual test subscriptions or by triggering event notifications with the Stripe CLI or through the Dashboard.

[Stripe CLI](/stripe-cli)

[Dashboard](https://dashboard.stripe.com/test/account/webhooks)

After you set up the Stripe CLI and link to your Stripe account, you can trigger events from the subscription lifecycle to test your webhook integration. If you use the Stripe CLI to trigger events, you can see event notifications on your server as they come in, which allows you to check your webhook integration directly without network tunnels or firewalls.

[subscription lifecycle](/billing/subscriptions/overview#subscription-lifecycle)

When you use the Stripe CLI or the Dashboard to trigger events, the event your webhook receives contains fake data that doesn’t correlate to subscription information. The most reliable way to test webhook notifications is to create actual test subscriptions and handle the corresponding events.

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

## Test payment failures

Use specific test credit card numbers to trigger payment failures for subscriptions and invoices.

[test credit card numbers](/testing#cards)

[invoices](/api/invoices)

Some subscription updates cause Stripe to invoice the subscription and attempt payment immediately (this synchronous payment attempt can occur on the initial invoice, or on certain invoice updates). If this attempt fails, the subscription is created in an incomplete status.

To test the effects of payment failure on an active subscription, attach the 4000 0000 0000 0341 card as the customer’s default payment method, but use a trial period to defer the attempt (a trial of a few seconds or minutes is sufficient). The subscription becomes active immediately, with a draft invoice created when the trial period ends. It takes approximately one hour for the invoice status changes to open, at which time payment collection is attempted and fails.

[4000 0000 0000 0341](/testing#cards)

[draft](/invoicing/overview#draft)

Use test clocks to simulate the forward movement of time in test mode, which causes Billing resources, like Subscriptions, to change state and trigger webhook events. This allows you to see how your integration handles a payment failure for a quarterly or annual renewal without waiting a year.

[test clocks](/billing/testing/test-clocks)

[test mode](/test-mode)

[webhook](/webhooks)

## Test payments that require 3D Secure

Use the 4000 0000 0000 3063 card to simulate 3D Secure triggering for subscriptions and invoices. You can also write custom Radar rules in testmode to trigger authentication.

[4000 0000 0000 3063](/testing#three-ds-cards)

[custom Radar rules in testmode](https://dashboard.stripe.com/test/radar/rules)

When a 3D Secure authentication flow is triggered, you can test authenticating or failing the payment attempt in the 3DS dialog that opens. If the payment is authenticated successfully, the invoice is paid. If the invoice belongs to a subscription in an incomplete status, the subscription becomes active. When a payment attempt fails, the authentication attempt is unsuccessful and the invoice remains open.

## Test Bank Transfer payments for invoices

To test manual payments on invoices through Bank Transfer:

- Create a testmode invoice with the collection method set to send_invoice and payment_settings[payment_method_types] array set to [customer_balance].

- Find the invoice in the Dashboard and click Send.

- Your customer has been allocated a unique virtual bank account number that you can retrieve through the funding instructions API. The virtual banking details are also present in the hosted invoice page as well as the PDF.

[funding instructions API](/payments/customer-balance/funding-instructions#create-funding-instructions)

## Test customer tax ID verification

Use these magic tax IDs to trigger certain verification conditions in test mode. The tax ID type must be either the EU VAT Number or Australian Business Number (ABN).
