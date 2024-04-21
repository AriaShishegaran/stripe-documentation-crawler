htmlTesting Stripe Billing | Stripe Documentation[Skip to content](#main-content)Test your integration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)# Testing Stripe Billing

Learn how to test your Billing integration.### Testing resources

- Use test[cards](/testing#cards)and[account numbers](/testing#test-account-numbers)to trigger different scenarios, like payment failures or required authentication.
- Use[test clocks](/billing/testing/test-clocks)to simulate Billing objects through time and test events at different milestones, like the end of a free trial or annual plan.
- Read the[general testing doc](/testing)to learn about fundamental testing common to all of Stripe.

Thoroughly test your integration before you expose it to customers or use it for any live activity. Use the resources on this page in addition to any organizational guidelines (for example, runbooks, quality gates, or development checklists) to help determine whether your integration is production-ready.

## Go-live principles

Before taking your integration live, review these Stripe checklists:

- [Account checklist](/get-started/checklist/account)
- [Development checklist](/get-started/checklist/go-live)
- [Website checklist](/get-started/checklist/website)

Here’s what a typical integration flow looks like.

For subscription and recurring revenue integrations, make sure that, at a minimum, the following components work as expected.

The table lists the event notifications for each component. You can configure your integration to listen for these events with webhooks. Read this guide to learn more about event notifications and testing.

ComponentDescriptionEventsCustomer sign-upMake sure your integration can successfully collect the information you need to create a Customer record in Stripe. Your customers can enter that information through Payment Links  Checkout,[Elements](/payments/elements), or a completely custom payment form built with the[Stripe API](/api). No matter which form you use, make sure that you see the Customer object stored on Stripe. You can use the Dashboard or API to view and[manage Customers](/billing/customer#manage-customers).- `customer.created`
- `customer.subscription.created`

InvoicingSubscriptions generate[Invoices](/api/invoices)at the end of each billing cycle. Depending on your payment collection method, you may send an invoice to collect payment in arears or to confirm an automatic charge. Make sure that your integration creates and sends invoices as you expect. Read the guide to learn more about creating and managing[invoices for subscriptions](/billing/invoices/subscription). You can use test clocks to simulate billing cycles, which include generating and sending invoices. Read the test clocks guide to learn about specific[use cases](/billing/testing/test-clocks/api-advanced-usage#use-cases)to test.- `invoice.created`
- `invoice.finalized`
- `invoice.finalization_failed`
- `invoice.paid`
- `invoice.payment_action_required`
- `invoice.payment_failed`
- `invoice.upcoming`
- `invoice.updated`

Subscription managementSet up the[customer portal](/billing/subscriptions/customer-portal)to let your customers manage their[subscriptions](/billing/subscriptions/creating)and billing information. To test it, create a subscription in[test mode](/test-mode). Then, log in to the portal as the test user and update the subscription. Check the Dashboard or API to see whether the subscription reflects the customer’s change. Read the[integration guide](/customer-management)to learn how to set up the customer portal.- `customer.subscription.deleted`
- `customer.subscription.paused`
- `customer.subscription.resumed`
- `customer.subscription.updated`

TrialsOffer customers a trial of your service. To test that your trial is set up correctly, you can create a test clock. The subscription should generate a zero-value invoice for the trial period.[Learn how to test trials with test clocks](#trials). For more information about how trials work, read the[subscription trials guide](/billing/subscriptions/trials).- `customer.subscription.trial_will_end`
- `customer.subscription.updated`

Payment failuresPayments from your customers may fail for a number of reasons. Make sure your integration can handle failures, including retrying payments.[Learn how to test payment failures](#payment-failures).- `invoice.finalization_failed`
- `invoice.payment_failed`
- `invoice.payment_action_required`

## Test clocks

Test clocks allow you to simulate Billing objects, like subscriptions, through time in test mode so you don’t have to wait a year to see how your integration handles a payment failure for an annual renewal. You don’t need to write any code with test clocks: you can create simulations in the Dashboard. You can also access them through the API. Learn more about test clocks and common use cases for them.

## Test subscription trial periods

First, follow these steps to start using test clocks:

1. [Create a test clock](/billing/testing/test-clocks/api-advanced-usage#create-clock)
2. [Set up your testing simulation](/billing/testing/test-clocks/api-advanced-usage#setup-simulation)
3. [Advance the clock’s time](/billing/testing/test-clocks/api-advanced-usage#advance-clock)
4. [Monitor and handle the changes](/billing/testing/test-clocks/api-advanced-usage#monitor-changes)
5. [Update the simulation](/billing/testing/test-clocks/api-advanced-usage#update-simulation)

Next, you can start testing trials with test clocks. Let’s say that you want customers to try your product for free with a seven-day trial before they start paying and want to collect payment information up front. To simulate this situation using test clocks, follow these steps:

- Create a new test clock and set its`frozen_time`to January 1.
- Add a customer and include their payment method. In this case, use a4242424242424242[test card](/testing#cards).
- Create a subscription and add a seven-day free trial period:

DashboardAPITo add a trial period to an existing subscription using the Dashboard:

Find the subscription you want to change.

1. ClickActions.
2. ClickUpdate subscription.
3. ClickAdd free trialand enter seven inFree trial daysfield.
4. ClickUpdate subscription.

- After creating a subscription with a seven-day free trial period, a subscription is created in a`trialing`state. An invoice of $0.00 is generated due to the free trial.
- Advance the date to January 5 to see the[customer.subscription.trial_will_end](/api/events/types#event_types-customer.subscription.trial_will_end)event notification. Stripe sends the notification three days before the trial ends. You can use this webhook event to inform your customers that the trial ends soon.
- Advance the date to January 8 to see that the subscription is now`paid`and an invoice for50EURis created.
- Advance the date by one cycle (for example, to February 8 for a monthly subscription) to see the subscription renew successfully.

### Test trial periods without test clocks

## Test subscription webhook notifications

Subscriptions integrations rely heavily on webhooks. You set up a webhook endpoint on your server and specify which event notifications to listen for. Stripe emits notifications for events like a subscription upgrade or cancellation.

You can test webhooks by either creating actual test subscriptions or by triggering event notifications with the Stripe CLI or through the Dashboard.

After you set up the Stripe CLI and link to your Stripe account, you can trigger events from the subscription lifecycle to test your webhook integration. If you use the Stripe CLI to trigger events, you can see event notifications on your server as they come in, which allows you to check your webhook integration directly without network tunnels or firewalls.

When you use the Stripe CLI or the Dashboard to trigger events, the event your webhook receives contains fake data that doesn’t correlate to subscription information. The most reliable way to test webhook notifications is to create actual test subscriptions and handle the corresponding events.

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

`invoice.upcoming`Sent a few days prior to the renewal of the subscription. The number of days is based on the number set forUpcoming renewal eventsin the[Dashboard](https://dashboard.stripe.com/settings/billing/automatic). For existing subscriptions, changing the number of days takes effect on the next billing period. You can still add[extra invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items), if needed.`invoice.updated`Sent when a payment succeeds or fails. If payment is successful the`paid`attribute is set to`true`and the`status`is`paid`. If payment fails,`paid`is set to`false`and the`status`remains`open`. Payment failures also trigger  a`invoice.payment_failed`event.`payment_intent.created`Sent when a[PaymentIntent](/api/payment_intents)is created.`payment_intent.succeeded`Sent when a PaymentIntent has successfully completed payment.`subscription_schedule.aborted`Sent when a subscription schedule is canceled because payment delinquency terminated the related subscription.`subscription_schedule.canceled`Sent when a subscription schedule is canceled, which also cancels any active associated subscription.`subscription_schedule.completed`Sent when all[phases](/billing/subscriptions/subscription-schedules#subscription-schedule-phases)of a subscription schedule complete.`subscription_schedule.created`Sent when a new subscription schedule is created.`subscription_schedule.expiring`Sent 7 days before a subscription schedule is set to expire.`subscription_schedule.released`Sent when a subscription schedule is[released](/api/subscription_schedules/release), or stopped and disassociated from the subscription, which remains.`subscription_schedule.updated`Sent when a subscription schedule is updated.## Test payment failures

Use specific test credit card numbers to trigger payment failures for subscriptions and invoices.

Some subscription updates cause Stripe to invoice the subscription and attempt payment immediately (this synchronous payment attempt can occur on the initial invoice, or on certain invoice updates). If this attempt fails, the subscription is created in an incomplete status.

To test the effects of payment failure on an active subscription, attach the 4000 0000 0000 0341 card as the customer’s default payment method, but use a trial period to defer the attempt (a trial of a few seconds or minutes is sufficient). The subscription becomes active immediately, with a draft invoice created when the trial period ends. It takes approximately one hour for the invoice status changes to open, at which time payment collection is attempted and fails.

Use test clocks to simulate the forward movement of time in test mode, which causes Billing resources, like Subscriptions, to change state and trigger webhook events. This allows you to see how your integration handles a payment failure for a quarterly or annual renewal without waiting a year.

## Test payments that require 3D Secure

Use the 4000 0000 0000 3063 card to simulate 3D Secure triggering for subscriptions and invoices. You can also write custom Radar rules in testmode to trigger authentication.

When a 3D Secure authentication flow is triggered, you can test authenticating or failing the payment attempt in the 3DS dialog that opens. If the payment is authenticated successfully, the invoice is paid. If the invoice belongs to a subscription in an incomplete status, the subscription becomes active. When a payment attempt fails, the authentication attempt is unsuccessful and the invoice remains open.

## Test Bank Transfer payments for invoices

To test manual payments on invoices through Bank Transfer:

1. Create a testmode invoice with the collection method set to`send_invoice`and`payment_settings[payment_method_types]`array set to`[customer_balance]`.
2. Find the invoice in the Dashboard and clickSend.
3. Your customer has been allocated a unique virtual bank account number that you can retrieve through the[funding instructions API](/payments/customer-balance/funding-instructions#create-funding-instructions). The virtual banking details are also present in the hosted invoice page as well as the PDF.

## Test customer tax ID verification

Use these magic tax IDs to trigger certain verification conditions in test mode. The tax ID type must be either the EU VAT Number or Australian Business Number (ABN).

NumberType`000000000`Successful verification`111111111`Unsuccessful verification`222222222`Verification remains pending indefinitelyWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Go-live principles](#go-live-principles)[Test clocks](#test-clocks)[Test subscription trial periods](#trials)[Test subscription webhook notifications](#webhooks)[Test payment failures](#payment-failures)[Test payments that require 3D Secure](#payment-3d-secure)[Test Bank Transfer payments for invoices](#bank-transfer)[Test customer tax ID verification](#customer-tax-id-verfication)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`