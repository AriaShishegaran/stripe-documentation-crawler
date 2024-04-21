# Using trial periods on subscriptions

You can start a customer’s subscription with a free trial period by providing a trial_end argument when creating the subscription:

[subscription](/billing/subscriptions/creating)

[creating the subscription](/api#create_subscription)

The trial_end parameter takes a timestamp indicating the exact moment the trial ends. When creating a subscription, you can alternatively use the trial_period_days parameter: an integer representing the number of days the trial lasts, from the current moment.

[trial_period_days](/api#create_subscription-trial_period_days)

When creating a subscription with a trial period, no payment method is required for the customer. An immediate invoice is still created, but for $0.

[invoice](/api/invoices)

Trial periods are normally applied at the start of a subscription, but you can also use a trial period on an existing subscription to change the subscription’s billing cycle.

[change the subscription’s billing cycle](/billing/subscriptions/billing-cycle)

When the trial ends, if the subscription status isn’t paused, we generate an invoice and send an invoice.created event notification. Approximately 1 hour later, we attempt to charge that invoice. A new billing cycle also begins for the customer when the trial ends.

To end a trial early, make an update subscription API call, setting the trial_end value to a new timestamp, or now to end immediately:

[update subscription](/api#update_subscription)

## Combining trials with billing cycle anchor

As of API version 2018-02-05, you can also combine trials with billing_cycle_anchor, resulting in a free period followed by a prorated period, leading into a fixed billing cycle.

[2018-02-05](/upgrades#2018-02-05)

For example, suppose it’s the 15th of the month and you want to give your customer a free 7 day trial (until the 22nd), and then start normal billing on the 1st. You can do this through the API by combining trials with billing_cycle_anchor. (This isn’t currently available through the Dashboard.)

[Dashboard](https://dashboard.stripe.com/test/subscriptions)

In this example, the customer gets an invoice for a prorated amount on the 22nd (for the period until the 1st). Then, on the 1st, they’ll be invoiced again for the full amount, and again on the 1st of the following month, and so on.

## Combining trials with usage-based billing

You can use trial periods for subscriptions with usage-based billing. During the trial period, any usage accrued doesn’t count toward the total charged to the customer at the end of the billing cycle. After the trial period ends, usage accrues and is billed at the end of the next billing cycle.

[usage-based billing](/products-prices/pricing-models#usage-based-pricing)

If you use the aggregate_usage parameter and set the behavior to last_ever, your customer will be billed for the last usage record if it falls within the trial period, even if the usage occurred during the trial period.

[parameter](/api/prices/create#create_price-recurring-aggregate_usage)

For example, if you provide file storage you might want to offer a month of free storage, but then charge for the first month if the customer continues to store files with your service.

Subscriptions that have subscription items with metered pricing bill in arrears because we need the total usage to determine the amount to bill. Paused subscriptions won’t allow usage events to be created for attached subscription items. Because it’s possible for you to resume a subscription in the middle of a billing period while leaving the billing cycle anchor unchanged, we support invoicing for the usage events with a timestamp after the subscription resumes.

## Combining trials with add_invoice_items

Trial periods for subscriptions can be combined with one time prices and add_invoice_items. This may happen if you want to charge a one time fee or add on at the same time as starting a trial. Note that doing this will cause an invoice to be cut immediately for the amount of the one time item at the beginning of the trial.

## Compliance requirements for trials and promotions

You must comply with card network requirements when offering trials, whether they’re free or not. This includes scenarios like free trials or charging customers a reduced price for the first few months and then automatically charging them your normal rate. When using our trials features, you can enable messaging settings in the Stripe Dashboard to help you meet the requirements.

[requirements](https://support.stripe.com/questions/2020-visa-trial-subscription-requirement-changes-guide)

[messaging settings](https://dashboard.stripe.com/settings/billing/automatic)

If you notify users of successful payments, Stripe automatically displays information about the trial and the cancellation URL in those notifications.

[successful payments](https://dashboard.stripe.com/settings/emails)

If you don’t use these settings, you’re still responsible for complying with the requirements.

When customer emails are enabled, a reminder is sent seven days before a trial ends. If a trial is shorter than seven days, the reminder email is sent as soon as the trial begins. If trials are renewed, a reminder email is resent.

If both trial reminders and subscription renewal reminders are enabled during a trial, customers only receive the trial ending reminder. Renewal emails are then sent for subsequent billing periods.

The cancellation policy link is a URL that is displayed on customer receipts, along with other trial information. This information is included for all card payments. The cancellation URL is also included in the reminder email that is sent to customers seven days before their trial ends.

For statement descriptors, if you manually set the statement descriptor on the invoice, the trial text isn’t appended so you need to add it. If you use product statement descriptors, the trial text is appended automatically. If your statement descriptor is greater than 10 characters, make sure it still makes sense to your customers with the trial text appended. There is a 22 character limit so anything after the 10th character is overwritten with * TRIAL OVER.

[statement descriptor](/api/invoices/object#invoice_object-statement_descriptor)

[product statement descriptors](/api/products/object#product_object-statement_descriptor)

[limit](/get-started/account/statement-descriptors#requirements)

If you don’t manually set the statement descriptor or use product statement descriptors, the trial text is appended to your account’s statement descriptor. If needed, you can set up a shortened descriptor to ensure the trial text displays correctly.

[shortened descriptor](https://dashboard.stripe.com/settings/public)

If you offer trials or promotions without using our trials features, you still need to comply with the requirements. You can listen for the invoice.upcoming event to determine when to send email notifications. To add text to your statement descriptor that indicates the promotion is over:

[requirements](https://support.stripe.com/questions/2020-visa-trial-subscription-requirement-changes-guide)

[invoice.upcoming](/api/events/types#event_types-invoice.upcoming)

- Listen for the customer.subscription.updated event

- Check to see if a trial or promotion has ended

- Update the statement descriptor on the subscription’s latest_invoice

[statement descriptor](/api/invoices/update#update_invoice-statement_descriptor)

You need to update the latest invoice within an hour of its creation while it’s still in draft status.

## Create free trials without collecting payment method

You can sign customers up for a free trial of a subscription without collecting their payment details in the Dashboard, the API, and Checkout. When you create the subscription, you can specify whether to cancel or pause the subscription if the customer didn’t provide a payment method during the trial period. To cancel or pause the subscription, set the trial_settings.end_behavior.missing_payment_method parameter when you create or update the subscription:

- Cancel subscription-If the free trial subscription ends without a payment method, it cancels immediately. You can create another subscription if the customer decides to subscribe to a paid plan in the future. Set missing_payment_method=cancel to cancel the subscription when it reaches the end of a trial without an available payment method.

- Pause subscription-If the free trial subscription ends without a payment method, it pauses and doesn’t cycle until it’s resumed. When a subscription is paused, it doesn’t generate invoices (unlike when a subscription’s payment collection is paused). When your customer adds their payment method after the subscription has paused, you can resume the same subscription. The subscription can remain paused indefinitely. Set missing_payment_method=pause to pause the subscription when it reaches the end of a trial without an available payment method.

[payment collection](/billing/subscriptions/pause-payment)

Alternatively, set missing_payment_method=create_invoice to invoice at the end of the trial if no payment method is present. If a payment method isn’t provided when the invoice finalizes, the subscription moves into past_due.

Configure reminder emails to collect customer’s payment details in your free trial messaging settings.

[free trial messaging settings](https://dashboard.stripe.com/settings/billing/automatic)

Use the Dashboard, the API, or Checkout to create free trials of a subscription without collecting payment details from your customers, and to configure your subscription to cancel if the trial ends without a payment method.

You can use the Dashboard to sign customers up for a free trial of a subscription without collecting their payment details:

- From the Subscriptions settings of the Dashboard, select +Create subscription.

- After adding your customer and product information, select +Add free trial, then input how many days the free trial lasts.

- Select the Pause or cancel if free trial ends without a payment method option, then select Cancel immediately. If you’re using test clocks, advance to the end of the trial. You won’t see an upcoming invoice for the subscription.

[test clocks](/billing/testing/test-clocks)

- Listen to the customer.subscription.deleted event that informs you when a subscription cancels at the end of trials without a payment method.

If you provide a payment method or select the Email invoice to customer with link to payment page option, the Pause or cancel if free trial ends without a payment method option won’t be visible.

Use the Dashboard, the API, or Checkout to create free trials of a subscription without collecting payment details from your customers, and to configure your subscription to pause if the trial ends without a payment method.

You can use the Dashboard to sign customers up for a free trial of a subscription without collecting their payment details:

- From the Subscriptions settings of the Dashboard, select +Create subscription.

- After adding your customer and product information, select +Add free trial, then input how many days the free trial lasts.

- Select the Pause or cancel if free trial ends without a payment method option, then select Pause. If you’re using test clocks, advance to the end of the trial. You won’t see an upcoming invoice for the subscription.

[test clocks](/billing/testing/test-clocks)

- Listen to the customer.subscription.paused event that informs you when a subscription pauses at the end of trials without a payment method.

If you provide a payment method or select the Email invoice to customer with link to payment page option, the Pause or cancel if free trial ends without a payment method option won’t be visible.

Configure your subscription to automatically send a reminder email when the customer’s trial is about to expire. You must comply with the card network requirements when offering trials. Learn more about compliance requirements for trials and promotion.

[compliance requirements for trials and promotion](#compliance)

Events are triggered every time a free trial changes. Make sure that your integration properly handles the events. For example, you might want to email a customer before a free trial ends. Learn more about subscription webhook events.

[Events](/api#event_types)

[subscription webhook events](/billing/subscriptions/webhooks#events)

The following table describes the events that trigger before a free trial ends, when a trial subscription pauses or cancels, and when a subscription is resumed and becomes active.

After you create a subscription for a customer without collecting a payment method, you can redirect them to the Billing customer portal to add their payment details.

First, configure the Billing customer portal to enable your customers to manage their subscriptions.

[Billing customer portal](/customer-management)

Next, collect billing information from your customers:

- Listen to the customer.subscription.trial_will_end event.

[customer.subscription.trial_will_end event](/api/events/types#event_types-customer.subscription.trial_will_end)

- If the subscription doesn’t have a default payment method, get the customer’s email using the Customers API and send them a message with a link to your site. It’s helpful to embed the customer ID in the email. For example: https://example.com?...&customer={{CUSTOMER_ID}}.

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

[Customers API](/api/customers/retrieve)

- When the customer enters your site, create a customer portal session using the customer ID from the previous step.

- Redirect the customer to the customer portal, where they can update their subscription with payment details.

To enable the subscription of a customer whose trial ended in a paused subscription through the customer portal, enable the free trial without payment method feature when creating a new subscription in the Dashboard.

To send a reminder email prior to the end of the trial, select the Link to a Stripe-hosted page option in the Subscriptions and emails setting. The reminder email contains a link for the customer to add or update their payment details. We don’t send free trial reminder emails in test mode. Learn more about how to setup free trial reminders.

[Subscriptions and emails setting](https://dashboard.stripe.com/settings/billing/automatic)

[test mode](/test-mode)

[setup free trial reminders](/billing/revenue-recovery/customer-emails#trial-ending-reminders)

Use the customer.subscription.trial_will_end event to send your own hosted emails to customers. After you see the event in the Dashboard, it’s confirmed that your email has been sent.

Subscriptions and upcoming invoices are created at the start of the trial and become active at the end of the trial if the customer provides a payment method.

After a free trial ends, you can configure subscriptions to pause if no default payment method is available for a subscription on a per-subscription basis.

You can update subscriptions while they’re paused. Updates that typically generate prorations (adding items, changing price or plan, changing quantity, and so on) won’t generate proration line items because the customer isn’t being charged while the subscription is paused. If you want to extend a trial after a subscription transitions into a paused status, you must resume the subscription before configuring a trial.

We check default_source and default_payment_method on the subscription and customer to determine whether a subscription is missing a payment method at the end of a trial.

Use the Dashboard, API, customer portal, or Hosted Invoice Page to resume a paused subscription.

To resume a paused subscription in the Dashboard, navigate to the subscription, then select Resume Subscription under the Actions menu. Select Reset billing cycle or Always invoice (if you’re not resetting the billing cycle) from the Resume subscription modal to charge the customer immediately.

While paused, a subscription won’t create an invoice. If you want to continue creating invoices, use pause_collection to stop collecting payments while continuing to invoice and advance billing periods.

To preview the invoice that’s generated when a paused subscription is resumed, specify a subscription_resume_at.

[subscription_resume_at](/api/invoices/upcoming#upcoming_invoice-subscription_resume_at)

## See also

- Products and prices

[Products and prices](/products-prices/overview)

- Prices

[Prices](/api#prices)

- Subscriptions

[Subscriptions](/api#subscriptions)

- Managing subscription billing cycles

[Managing subscription billing cycles](/billing/subscriptions/billing-cycle)
