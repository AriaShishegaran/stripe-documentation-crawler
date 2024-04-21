htmlCancel subscriptions | Stripe Documentation[Skip to content](#main-content)Cancel subscriptions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fcancel)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fcancel)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)# Cancel subscriptions

Learn how to cancel existing subscriptions.### Customer portal

This guide describes how to use the Subscriptions API to manage customer subscriptions through your site.

You can also let customers manage their subscriptions, invoices, and billing information through the Stripe-hosted [customer portal] cancellation page(/docs/customer-management/cancellation-page).

You can manually cancel your customers’ subscriptions through the Subscription API or the Dashboard. If want to keep the subscription active but temporarily stop collecting payment, you can pause payment collection. Pausing payment collection does not affect the status of the subscription, which is what we recommend you use as the trigger for starting or stopping service to your customer.

Subscriptions are canceled automatically after up to four unsuccessful attempts to bill the customer. You can configure this in your subscription lifecycle settings. Read more about revenue recovery settings, like Smart Retries and configurable customer emails, in the guides.

## Cancel subscriptions

Cancel subscriptions through the Dashboard or API:

DashboardAPITo cancel a subscription using the Dashboard:

1. From the customer account page or the subscription details page, click the overflow menu (), then select Cancel subscription.


2. Choose when to end the subscription: immediately, at the end of the period, or on a custom day.


3. Choose to provide a refund for a prorated amount, refund the last payment in full, or provide no refund. Learn more about prorations and refunds.


4. After all settings are finalized, click Cancel subscription.



By default, the cancellation takes effect immediately. As soon the subscription cancels, no further invoices are generated for it.

Common mistakeIf you set a custom cancellation date, you can’t provide a refund. A credit proration is always generated. Prorations are not generated only if the custom cancellation date is within the current billing period and proration_behavior is set to none.

### Prorate for usage-based billing

If the subscription is part of the way through a paid billing period, you can prorate the cancellation by passing the prorate parameter.

When you prorate a cancellation you can optionally invoice for:

- Outstanding prorations
- [Metered usage](/products-prices/pricing-models#usage-based-pricing)

If you don’t prorate the subscription, all metered usage is discarded and the customer does not receive any credit for any potential prorations.

Use the invoice_now parameter to create a final invoice immediately. After canceling, the customer might be owed a credit, which is added to their credit balance to be applied to future invoices. To refund your customer, issue refunds and then adjust their account balance back to zero. Learn more about customer refunds on our dedicated support page.

### Cancel at the end of the current billing cycle

If you want to cancel the subscription at the end of the current billing period (that is, for the duration of time the customer has already paid for), update the subscription with a cancel_at_period_end value of true:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cancel_at_period_end=true`You can reactivate subscriptions scheduled for cancellation (with the cancel_at_period_end parameter) by updating cancel_at_period_end to false. You can reactivate the subscription at any point up to the end of the period.

### Cancel at the end of a future billing cycle

To configure a subscription to end after a specified number of billing cycles, define a schedule for it. Set the schedule length by specifying one or more phases and intervals, and set its end_behavior attribute to cancel.

### Configure automatic cancellation after a dispute

Limited supportThis feature is only supported for disputed credit and debit card payments opened in the full amount.

When a customer disputes a charge for a subscription, the subscription continues to cycle, which can create more disputed charges. You can change this behavior in the Stripe Dashboard so that subscriptions are canceled instead. Under Manage disputed payments, select cancel the subscription immediately without prorating or cancel the subscription at the end of the period. It takes about one hour for changes to the subscription to take effect.

If you choose to cancel immediately, the subscription cancels immediately without any prorating. A canceled subscription can’t be restarted, so you must create a new one for the customer if you want to continue billing them.

If you choose to cancel at the end of the period, cancel_at_period_end is set to true and the subscription cancels at the end of the current billing period. This allows you some time to work through the dispute process before the cancellation occurs.

For subscriptions managed with schedules, the subscription is first released from the schedule and then canceled. This means the rest of the scheduled changes won’t take effect.

## Handle invoice items when canceling subscriptions

When a subscription has pending invoice items you’ve created, the customer may still be billed for those if the cancellation is set to include a final invoice or there is another subscription active on the customer. To avoid this, manually delete the invoice items.

Similarly, any usage reported during the billing period bills at the end of the period. To avoid a final charge for usage, update the subscription and remove the metered price using the clear_usage parameter.

If you set the subscription to cancel at period end, any pending prorations are left in place and still collected at the end of the period. If you cancel the subscription before the end of the period, invoice items will remain—and won’t be processed unless you specifically generate an invoice with them.

Canceling a subscription causes all open and draft invoices for that subscription to have their auto_advance property set to false. This occurs to prevent unexpected automatic payment attempts and reminder emails. This effectively pauses automatic collection for these invoices. You can still manually attempt to collect payment and manually send emails.

## Identify cancellation events

Stripe sends a customer.subscription.deleted event when a customer’s subscription is canceled immediately. If the customer.subscription.deleted event’s request property isn’t null, that indicates the cancellation was made by your request (as opposed to automatically based upon your subscription settings).

If you instead cancel a subscription at the end of the billing period (that is, by setting cancel_at_period_end to true), a customer.subscription.updated event is immediately triggered. That event reflects the change in the subscription’s cancel_at_period_end value. When the subscription is actually canceled at the end of the period, a customer.subscription.deleted event then occurs.

## Stop a pending cancellation

If you schedule a subscription to be canceled by updating cancel_at_period_end to true, and the subscription hasn’t yet reached the end of the billing period, you can stop the cancellation by updating cancel_at_period_end to false.

NotePrior to version 2018-02-28, any parameter sent to the Update Subscription API stops a pending cancellation.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cancel_at_period_end=false`You can also stop a scheduled cancellation by using the Dashboard’s Reactivate Subscription option.

After a subscription has been canceled, you can’t reactivate it.

## See also

- [Using trial periods](/billing/subscriptions/trials)
- [Update subscription](/api#update_subscription)
- [Cancel subscription](/api#cancel_subscription)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Cancel subscriptions](#canceling)[Handle invoice items when canceling subscriptions](#handle-invoice-items-when-canceling-subscriptions)[Identify cancellation events](#events)[Stop a pending cancellation](#reactivating-canceled-subscriptions)[See also](#see-also)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`