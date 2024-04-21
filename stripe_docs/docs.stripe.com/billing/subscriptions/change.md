# Change subscriptions

In addition to using the API and Dashboard to change subscriptions, you can also implement the customer portal to provide a Stripe-hosted dashboard where customers can manage their subscriptions and billing details.

[customer portal](/customer-management)

Stripe supports changing existing subscriptions without having to cancel and recreate them. Some of the most significant changes you might make are:

- Changing the billing cycle

[billing cycle](/billing/subscriptions/billing-cycle)

- Upgrading or downgrading the subscription price

[Upgrading or downgrading](/billing/subscriptions/upgrade-downgrade)

- Canceling an active subscription

[Canceling](/billing/subscriptions/cancel)

- Pausing payment collection for an active subscription

[Pausing payment collection](/billing/subscriptions/pause-payment)

Some changes automatically create a new invoice. Use the pending updates feature with these changes so that the updates are only applied if the new invoice is successfully paid.

[invoice](/api/invoices)

[pending updates](/billing/subscriptions/pending-updates)

You can also alter subscriptions by updating the parameters normally used when creating the subscription. For example:

- Applying discounts

[discounts](/billing/subscriptions/coupons)

- Using trial periods

[trial periods](/billing/subscriptions/trials)

- Setting quantities

[quantities](/billing/subscriptions/quantities)

- Adding taxes

[taxes](/billing/taxes)

- Setting payment methods

[payment methods](/billing/subscriptions/payment-methods-setting)

The most complex aspect of changing existing subscriptions is proration, where the customer is charged a percentage of a subscription’s cost to reflect partial use. By default, the following actions result in a proration:

[proration](/billing/subscriptions/prorations)

- Changing to a price with a different base cost

- Changing to a price with a different billing interval

- Adding a trial period to an active subscription

- Changing the quantity

Proration ensures that customers are billed accurately, but a proration can result in different payment amounts than you expect, which may be confusing. Also keep in mind that prorations are never automatically refunded to a customer nor immediately billed, although you can do both manually. When applying changes to existing subscriptions, discounts don’t affect the resulting proration line items.

[discounts](/billing/subscriptions/coupons)

Prorations only apply to charges that occur ahead of the billing cycle. Metered billing isn’t subject to proration.

[Metered billing](/products-prices/pricing-models#usage-based-pricing)

You can preview a proration to view the amount before applying the changes.

[preview a proration](/billing/subscriptions/prorations#preview-proration)
