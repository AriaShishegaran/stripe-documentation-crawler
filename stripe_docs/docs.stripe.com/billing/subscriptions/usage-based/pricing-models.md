# Model usage-based pricing

We updated our usage-based billing process. For information on our previous guidance, refer to our legacy usage-based billing documentation.

[legacy usage-based billing documentation](/billing/subscriptions/usage-based-legacy)

There are various pricing models for usage-based billing: pay as you go, fixed fee and overage (recommended for most users), and credit burndowns.

## Pay as you go

Commonly referred to as “in arrears billing”, the “pay as you go” model lets you track usage incurred over a determined period, then charge the customer at the end of the period. There are four different pricing strategies you can deploy:

- Per unit: Charge the same amount for every single unit.

- Per package: Charge for a package or bundle  of units or usage. This is the model for the fictional Alpaca AI company.

[fictional Alpaca AI company](/billing/subscriptions/usage-based/implementation-guide#what-you-will-build)

- Tiered and volume based pricing: The subscription item is billed at the tier corresponding to the amount of usage at the end of the period. Learn more about volume-based pricing.

[volume-based pricing](/products-prices/pricing-models#volume-based-pricing)

- Tiered and graduated pricing: Similar to volume pricing, graduated pricing charges for the usage in each tier instead of applying a single price to all usage.

[graduated pricing](/products-prices/pricing-models#graduated-pricing)

This model might not be ideal if your business involves customers with low-trust because customers might accumulate significant usage and then have their payment method fail at the end of the month.

## Fixed fee and overage model

In this model, you charge a flat fee per month for your service at the beginning of the period. This flat fee has some included usage entitlement, and any additional usage (overage) is charged at the end of the period.

You can model this with two prices within the same product. For example, Alpaca AI introduces a new advanced model called Llama AI. Priced at 200 USD per month, this model includes 100,000 tokens. Any usage beyond the included tokens is charged at an additional rate of 0.001 USD per token.

To create a product:

- Navigate to the Products tab.

[Products tab](https://dashboard.stripe.com/test/products)

- Click + Add product.

- Enter the name of the product (in this case, Llama AI).

Next, add a recurring flat fee price to the Llama AI product:

- Select Flat rate pricing for the pricing model.

- Set the amount to 200 USD.

Next, add a second recurring price to the product. The first tier is priced at 0 USD because the first 100,000 units are included in the flat rate.

- Select Usage-based, Per Tier and Graduated for the pricing model

Select Usage-based, Per Tier and Graduated for the pricing model

- Create two graduated pricing tiers:First unitLast unitPer unitFlat feeFor the first0100,0000.00 USD0.00 USDFor the next100,001∞0.001 USD0.00 USD

Create two graduated pricing tiers:

- Create a new meter llama_api_tokens to record usage.

Create a new meter llama_api_tokens to record usage.

When you create subscriptions, specify both of the prices you created above.

## Credit burndown model

In this payment model, users pay an initial amount and gradually use up credits for their usage. Currently, Stripe doesn’t support this specific model, but we’re actively developing native support for it. To learn more, please contact us at usage-based-billing@stripe.com

[usage-based-billing@stripe.com](mailto:usage-based-billing@stripe.com)

[Billing thresholds](#billing-thresholds)

## Billing thresholds

Set billing thresholds to issue an invoice and, optionally, to reset a subscription’s billing cycle anchor after a customer’s accrued usage in a subscription cycle reaches a specified monetary threshold. Consider using billing thresholds to add precautions to limit the amount owed or to limit the products consumed between invoices or charges.

[billing thresholds](/api/subscriptions/object#subscription_object-billing_thresholds)

[invoice](/api/invoices)

[billing cycle anchor](/api/subscriptions/create#create_subscription-billing_thresholds-reset_billing_cycle_anchor)

It’s common to set the value of a threshold as a multiple of the cost of one unit of the product being sold.

Setting a lower amount threshold causes your customers to receive an invoice for every unit of usage, which might cause confusion.

The value is a positive integer in the smallest currency unit (for example, 100 cents to charge 1 USD; or 100 to charge 100 JPY, a zero-decimal currency). Set the value to at least 50 currency units.

[smallest currency unit](/currencies#zero-decimal)

You can also set monetary thresholds in the Dashboard when you create or update a subscription.

[Dashboard](https://dashboard.stripe.com/test/subscriptions)

Set usage thresholds to exceed one unit of usage to prevent frequent invoicing. Stripe doesn’t support setting usage thresholds in the Dashboard.

By default, the billing cycle anchor of a subscription remains unchanged after a customer’s usage reaches a threshold. For example, if a threshold is reached in the middle of a month-long subscription, the subscription resets at the end of the month, similar to a subscription without thresholds.

[billing cycle anchor](/billing/subscriptions/billing-cycle)

You can change this behavior by configuring the subscription to reset the billing cycle anchor after it reaches a threshold. Stripe treats the reaching of a threshold as if the subscription had naturally arrived at its rollover point at the end of the month.

Stripe maintains tiers across threshold invoices. Tiers reset at the end of the billing period by default, or if you configure the subscription to reset the billing cycle anchor after it reaches a threshold, similar to a subscription without thresholds.

For example, let’s say you run an ad platform that has the following graduated tiering structure for ad impressions:

Because Stripe bills usage retrospectively, you can set a threshold of 100 USD as a temporary measure for new customers. Under this scheme, your customer is billed every 200 impressions for the first 10,000 impressions (200 * 0.50 USD = 100 USD). When the customer exceeds 10,000 impressions, they’re billed every 250 impressions (250 * 0.40 USD = 100 USD). This continues until the end of the billing period, at which point all un-invoiced usage are invoiced, and the subscription and tiers reset.

To enable the resetting of tiers after reaching a threshold, you must configure the subscription to reset the billing cycle anchor after the usage reaches the thresholds that you set.

Volume tiers define the pricing for all units of usage, as opposed to graduated tiers, which define pricing for a specific amount of usage. Some pricing models use volume tiers that decrease the unit cost at each successive tier. You can use these models to incentivize customers to use more of a product (for example, ad impressions, or GB of storage).

[Volume tiers](#volume-based-pricing)

[graduated tiers](#graduated-pricing)

When combined with thresholds, these pricing models can lead to invoices with line items for negative amounts under the following conditions:

- A threshold invoice has already been issued.

- Subsequent usage bills at a lower unit cost.

For example, consider the following tiered pricing structure:

If a customer uses 10,000 units, the invoice total is 5,000 USD (10,000 * 0.50 USD = 5,000 USD). Any additional usage causes all usage to bill at the lower unit cost of 0.40 USD. If the customer uses one more unit, the invoice total drops to 4,000.40 USD (10,001 * 0.40 USD = 4,000.40 USD).

Without thresholds, Stripe would issue an invoice for 4,000.40 USD at the end of the billing period.

However, to see how negative invoicing can occur, assume that we have a 5,000 USD monetary threshold in place. In this scenario, Stripe issues an invoice when the customer reaches 10,000 units of usage.

If the customer uses one more unit, the invoice total drops to 4,000.40 USD (10,001 * 0.40 USD = 4,000.40 USD). However, if the customer doesn’t consume more units, they’re owed 999.60 USD (5,000 USD - 4,000.40 USD = 999.60 USD). At the end of the billing period, Stripe  credits this amount to the customer’s balance, which we use to pay down future invoices.

Let’s say the customer continues to accrue usage. The cost of this usage reaches 5,000 USD again when the customer uses 12,500 units (5,000 USD / 0.40 USD = 12,500). However, the previous payment of 5,000 USD covers all of this usage. As a result, we don’t issue an invoice.

Stripe won’t issue an invoice until either the total usage reaches 25,000 units (for a total cost of 10,000 USD), or the end of the billing period arrives—whichever occurs first. The tables below show the line items you see for the two invoices issued in the scenario where usage reaches 25,000 units.

Invoice 1:

Invoice 2:

- Thresholds don’t apply to trial subscriptions.

[trial subscriptions](/billing/subscriptions/trials)

- Monetary thresholds must be greater than the sum of any flat fees on metered subscription items.

- Billing thresholds aren’t evaluated during the 24 hours leading up to the end of a subscription. This helps limit confusion for a customer who receives multiple invoices on the same date.

- We only allow subscriptions a single monetary threshold.

- We only allow subscription items a single usage threshold.

- Due to the real-time nature of usage reporting, we might not issue invoices at the exact moment a specified threshold is reached. Invoiced amounts or usage might be slightly higher than the specified thresholds.

- The value used to determine whether a monetary threshold has been reached excludes taxes, but includes discounts.

- Per package per tiering pricing isn’t currently supported

[Free trials](#trials)

## Free trials

You can use trial periods for subscriptions with usage-based billing. During the trial period, any usage accrued doesn’t count toward the total charged to the customer at the end of the billing cycle. After the trial period ends, usage accrues and is billed at the end of the next billing cycle.

[trial periods](/billing/subscriptions/trials)

Learn more about trial periods and subscriptions.

[trial periods and subscriptions](/billing/subscriptions/trials)

Make sure that your integration properly monitors and handles web events related to changes in trial status.

A few days before a trial ends and the subscription moves from trialing to active, you receive a customer.subscription.trial_will_end event. When you receive this event, make sure that you have a payment method on the customer’s account to proceed with billing them. Optionally, notify the customer in advance about the upcoming charge.

[requires action](#requires-action)

[subscription settings](/billing/subscriptions/overview#settings)

[Smart Retries](/billing/revenue-recovery/smart-retries)

[trial_settings.end_behavior.missing_payment_method](/billing/subscriptions/trials#create-free-trials-without-payment)

[resume the subscription](/billing/subscriptions/trials#resume-a-paused-subscription)

Learn more about subscriptions and webhooks.

[subscriptions and webhooks](/billing/subscriptions/webhooks)

[Cancellations](#cancellations)

## Cancellations

With usage-based billing, the bill the customer pays varies based on consumption during the billing cycle. When changing the billing cycle results in ending a subscription interval early, you charge the customer for the usage accrued during the shortened billing cycle. We don’t support proration with usage-based billing.

[proration](/billing/subscriptions/prorations)

After a subscription is canceled, you can’t reactivate it. Instead, you can collect updated billing information from your customer, update their default payment method, and create a new subscription with their existing customer record.

After you schedule the cancellation of a subscription using cancel_at_period_end, you can reactivate it at any point up to the end of the period by updating cancel_at_period_end to false. The final invoice includes any metered usage after the subscription cancels at the end of the billing period.

[cancel_at_period_end](/api/subscriptions/update#update_subscription-cancel_at_period_end)

[Transform quantities](#transform-quantities)

## Transform quantities

Use the transform_quantity option to transform usage before applying the price. This allows you to divide the reported usage by a specific number and round the result either up or down. This is commonly used when pricing on packages of a product instead of individual units. Quantity transformation isn’t compatible with tiered pricing.

[transform_quantity option](/api/prices/create#create_price-transform_quantity)

[tiered pricing](/products-prices/pricing-models#tiered-pricing)

For example, let’s say you have a car rental service. You report usage as a number of minutes, and you want to charge customers for each hour the car is rented.

Next, create a price for the car rental service product, charging 10 USD an hour and rounding up (to charge for a full hour even if only part of the hour is used):

If a car is rented for 150 minutes, that customer is charged 30 USD for 3 hours of renting (2 hours and 30 minutes, rounded up).

[Decimal amounts](#decimal-amounts)

## Decimal amounts

Decimal pricing is useful if you need to create pricing amounts that aren’t whole numbers. For example, if you’re running a cloud storage SaaS business, you can create a price that charges 0.05 cents for each MB used per month. Based on usage, the quantity of MB is then multiplied by 0.05 cents and rounded to the nearest whole cent.

To create prices with decimal amounts, specify unit_amount_decimal instead of unit_amount. unit_amount_decimal allows you to set the amount in the minor unit of the currency that you charge in. For example, you can set unit_amount_decimal = 105.5 in USD to represent 105.5 cents, or 1.055 USD. unit_amount_decimal accepts decimals up to 12 decimal places.

[create prices](/api#create_price)

If you plan to use tiers, you can specify unit_amount_decimal instead of unit_amount. You can also create invoice items with unit_amount_decimal instead of unit_amount.

[tiers](/products-prices/pricing-models#tiered-pricing)

[create invoice items](/api/invoiceitems/create)

In API responses, the integer unit_amount field doesn’t populate if you create the object with a decimal value. For example, if you create a price with unit_amount_decimal = 0.05, the response contains unit_amount = null and unit_amount_decimal = 0.05. You can still pass integer values into unit_amount_decimal, in which case unit_amount is populated in the response. For example, if you create a price with unit_amount_decimal = 5, the response contains unit_amount = 5 and unit_amount_decimal = 5.0.

If your integration has event handling that uses unit_amount values and you begin using decimal amounts, you need to use unit_amount_decimal instead. This is important because unit_amount returns as null if the decimal amounts can’t be converted into integers, which might cause errors in your integration.

[Grace periods](#grace-periods)

## Grace periods

By default, Stripe finalizes subscription invoices one hour after they’re generated. During this one hour grace period, you can continue to report usage for the previous period. When the invoice finalizes, we update it to reflect the latest quantity for its billing period.

[generated](/billing/invoices/subscription#subscription-renewal)

Usage reported after the invoice finalizes aren’t captured in future invoices.

If you’re interested in enabling a longer grace period, contact us at usage-based-billing@stripe.com.

[usage-based-billing@stripe.com](mailto:usage-based-billing@stripe.com)

[Mid-cycle updates](#mid-cycle-updates)

## Mid-cycle updates

You can update a subscription item’s price during a billing cycle. However, we only reflect usage occurring after the update on the invoice. Usage occurring before the change won’t be invoiced.

After the update, we invoice any new usage reported at the new price.

To delete a subscription item:

We don’t reflect any usage from that item on the invoice.

[Backdate subscription creation](#backdating-subscription-creation)

## Backdate subscription creation

You can create backdated subscriptions to start reporting usage before creating a subscription.
