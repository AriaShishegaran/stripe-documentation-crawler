# Simulate subscriptions

To simulate any existing or new subscriptions in test mode:

- Open the Dashboard and enable Test mode.

- In the subscriptions page, click the subscription to test.

[subscriptions](https://dashboard.stripe.com/test/subscriptions)

- Click Run simulation in the banner at the top of the page.Customer ineligible for simulationThe Run simulation button might be disabled if the subscription’s customer:Is attached to more than three subscriptions, including scheduled subscriptionsHas a complex profile, with many quotes, invoices or other related objects

The Run simulation button might be disabled if the subscription’s customer:

- Is attached to more than three subscriptions, including scheduled subscriptions

[scheduled subscriptions](/billing/subscriptions/subscription-schedules)

- Has a complex profile, with many quotes, invoices or other related objects

- In the modal, set the date and time to simulate and click Advance time.

You can advance time by any increment, but you can only advance them two intervals at a time from the initial frozen time. For example, if you have a monthly subscription, you can only advance the clock up to two months at a time.

When the clock is done advancing, the banner updates and displays the clock’s current time.

You can continue to make changes to your simulation and advance the time for simulations like:

- Adding a customer balance.

[customer balance](/billing/customer/balance)

- Making a mid-cycle upgrade.

- Adding one-off invoice items.

[Adding one-off invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items)

Repeat as many times as you need to satisfy your test case.
