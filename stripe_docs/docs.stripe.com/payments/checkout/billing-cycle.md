# Set the billing cycle date in Checkout

You can explicitly set a subscription’s billing cycle anchor to a fixed date (for example, the 1st of the next month) in Checkout.

[billing cycle anchor](/api/checkout/sessions/create#create_checkout_session-subscription_data-billing_cycle_anchor)

The billing cycle anchor determines the first full invoice date, when customers are billed the full subscription amount. The billing cycle anchor and the recurring interval of its price also determine a subscription’s future billing dates. For example, a monthly subscription created in Checkout on May 15 with an anchor at June 1 is billed on May 15, then always on the 1st of the month.

[price](/products-prices/overview)

For the initial billing period up until the first full invoice date, you can customize how to handle prorations with the proration_behavior parameter. By default, proration_behavior is set to create_prorations, and customers receive a prorated invoice. If proration_behavior is none, customers receive the initial period up to the first full invoice date for free.

[prorations](/billing/subscriptions/prorations)

[proration_behavior](/api/checkout/sessions/create#create_checkout_session-subscription_data-proration_behavior)

[invoice](/api/invoices)

## Create a Checkout Session with a billing cycle anchor

To configure a billing cycle anchor, set the subscription_data.billing_cycle_anchor parameter when you create a Checkout Session in subscription mode.

The anchor must be a future UNIX timestamp before the next natural subscription billing date.

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

If the billing cycle anchor is during a session’s active period and a customer attempts payment after it has passed, Checkout displays and charges for the full period starting with the billing cycle anchor instead of the prorated period before the billing cycle anchor.

## Disable prorations

To disable prorations, set the subscription_data.proration_behavior parameter to none when creating a Checkout Session.

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

Similar to a free trial, the initial period up to the billing cycle anchor is free. Unlike a trial, no 0 USD invoice is generated. Customers receive an invoice with the full subscription amount on the billing cycle anchor date.

In the Checkout Session response object, amounts attached to the line items and total details are always 0 when prorations are disabled. Additionally, the payment status of the Session is set to no_payment_required to reflect that payment is delayed to a future date.

[line items](/api/checkout/sessions/object#checkout_session_object-line_items)

[total details](/api/checkout/sessions/object#checkout_session_object-total_details)

[payment status](/api/checkout/sessions/object#checkout_session_object-payment_status)

## Current limitations

- You can’t use trials in Checkout with a billing cycle anchor.

- One-time prices can’t be used in Checkout Sessions when proration_behavior is none.

- You can’t apply amount_off coupons to Checkout Sessions with a default proration_behavior of create_prorations.

[amount_off coupons](/api/coupons/create#create_coupon-amount_off)

## See also

- Setting the subscription billing cycle date

[Setting the subscription billing cycle date](/billing/subscriptions/billing-cycle)

- Prorations

[Prorations](/billing/subscriptions/prorations)

- Create Checkout Session

[Create Checkout Session](/api/checkout/sessions/create#create_checkout_session)
