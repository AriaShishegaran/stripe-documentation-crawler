# Migrate to billing meters

Stripe is deprecating usage-records billing. Moving forward, you can migrate to billing meters, our only solution for usage-based billing. Billing meters provide the following advantages:

- High-throughput usage reporting

- One-hour reporting grace period for generating invoices

[grace period](/billing/subscriptions/usage-based/pricing-models#grace-periods)

- Collect usage before creating a subscription

[Collect usage](/billing/subscriptions/usage-based/recording-usage#recording-usage)

However, we don’t support the following features:

- max, last_ever, and last_during_period aggregation

[aggregation](/api/prices/object#price_object-recurring)

- Reporting usage in the Dashboard

You can continue to use usage records as you adopt billing meters.

## Billing meter overview

Billing meters allow you to track usage of a particular event. It supports high-throughput event ingestion and aggregation.

Unlike usage records, billing meters don’t require customers to have subscriptions before reporting usage and a single meter can track usage across multiple customers.

Learn more about billing meters in our implementation guide.

[implementation guide](/billing/subscriptions/usage-based/implementation-guide)

[Create a meter](#create-meter)

## Create a meter

Create a billing meter. Learn more about configuring meters.

[billing meter](/api/billing/meter)

[configuring meters](/billing/subscriptions/usage-based/recording-usage#configuring-meter)

[Create a new price](#create-price)

## Create a new price

Create a new price associated with the billing meter. Make sure that the new price is on the same product as your old price.

[Start recording usage](#start-recording-usage)

## Start recording usage

You must continue to send usage records to Stripe until the migration is completed.

[usage records](/billing/subscriptions/usage-based-legacy/recording-usage)

Start reporting usage to the Billing Meter API. Stripe doesn’t reflect this usage on customer invoices until they’re subscribed to the new price.

Learn more about recording usage.

[recording usage](/billing/subscriptions/usage-based/recording-usage#recording-usage)

[OptionalQuery reported usage](#query-reported-usage)

## OptionalQuery reported usage

[Plan subscription schedules](#plan-subscription-schedules)

## Plan subscription schedules

Use subscription schedules to automatically migrate to the new price at the end of the billing cycle. Learn more about subscription schedules.

[subscription schedules](/billing/subscriptions/subscription-schedules)

List the subscriptions associated with the old price.

Stripe returns a list of subscriptions associated with the old price. For example:

If a subscription has a schedule, you must update the existing subscription schedule to migrate to the new price at the end of a billing cycle. If no schedule exists for a subscription, create a new one.

[schedule](/api/subscriptions/object#subscription_object-schedule)

[subscription schedule](/api/subscription_schedules)

Create a subscription schedule for each subscription associated with the old price.

Stripe returns a new subscription schedule object:

Update the subscription schedule to add a phase with the new price.

## Test the migration

Create a test customer with a subscription associated with the old price.

- Navigate to the Customers tab.

[Customers tab](https://dashboard.stripe.com/test/customers)

- Click + Add customer.

- Enter the name of the customer.

- Navigate to the new customer.

- Next to the Subscriptions header, click + to open the subscription drawer.

- Select the old price.

- Click Create test subscription.

Create a subscription schedule from the subscription.

Add a phase to the subscription schedule to migrate to the new price.

Simulate the subscription change with a test clock.

[Simulate the subscription change](/billing/testing/test-clocks/simulate-subscriptions)

Learn more about testing subscriptions integrations. You can use test clocks to test different scenarios, including mock usage reporting. Learn more about test clocks.

[testing subscriptions integrations](/billing/testing)

[test clocks](/billing/testing/test-clocks)
