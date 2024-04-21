# API and advanced usage

You can create a test clock separately from a subscription for running advanced simulations. In this scenario you create the test clock first and then add different test cases to it.

Not ready for a full integration? See our guide for running simulations on subscriptions.

[our guide](/billing/testing/test-clocks/simulate-subscriptions)

Test clock lifecycle

Follow these steps to start using test clocks:

- Create a test clock

[Create a test clock](#create-clock)

- Set up your testing simulation

[Set up your testing simulation](#setup-simulation)

- Advance the clock’s time

[Advance the clock’s time](#advance-clock)

- Monitor and handle the changes

[Monitor and handle the changes](#monitor-changes)

- Update the simulation

[Update the simulation](#update-simulation)

- Delete the clock

[Delete the clock](#delete-clock)

You can advance the clock’s time, monitor changes, and update the simulation as often as you need to test different cases.

[Create a clock and set its time](#create-clock)

## Create a clock and set its time

To start a simulation, create a clock and set its frozen time. The temporal starting point for all subscriptions associated with this clock. You can set this to a time in the future or in the past to test different simulations, but you can only move it forward in time after you set it.

[subscriptions](/billing/subscriptions/creating)

To create a test clock in the Dashboard, follow the steps below. Set the Dashboard to Test mode to use test clocks.

- Go to the Subscriptions section under the Billing tab.

[section](https://dashboard.stripe.com/test/subscriptions)

- Click the test clocks link in the banner.

[test clocks](https://dashboard.stripe.com/test/test-clocks)

- Click New simulation.

- In the Create new simulation modal, enter a name for the simulation. You can use this to describe the simulation you’re testing, like Annual renewal or Free trial.

- Set the frozen time of the clock. This is the starting point for your simulation. You can set this to a time in the future or in the past, but you can only move it forward in time after you set it.

[Set up your simulation](#setup-simulation)

## Set up your simulation

Next, set up the test case for your simulation. You need to create a customer first, then a subscription for them.

To create a customer for your simulation through the Dashboard:

- Go to the test clocks page and find your test clock.

[test clocks](https://dashboard.stripe.com/test/test-clocks)

- Click Add > Add customer.

You can’t choose existing customers during test clock simulations. You can add up to three new customers to each simulation.

You can optionally enter other available properties for the customer, like their name, email, and billing information, but none are required. For some simulations, like testing free trials, you might not want to collect any billing information up front.

[available properties](/billing/customer#properties-uses)

Next, you can create up to three subscriptions or subscription schedules for your customer. To create a subscription for the customer through the Dashboard:

- Go to the test clocks page and find your test clock.

Go to the test clocks page and find your test clock.

[test clocks](https://dashboard.stripe.com/test/test-clocks)

- Click Add > Add subscription. Select or search for your customer from the drop-down menu. You can also add the customer to a subscription through the customer page, by clicking Actions > Create subscription.

Click Add > Add subscription. Select or search for your customer from the drop-down menu. You can also add the customer to a subscription through the customer page, by clicking Actions > Create subscription.

- Select a recurring product and price in the Pricing section.

Select a recurring product and price in the Pricing section.

- For the Subscription schedule, define the start and end date for the subscription and when to start the billing cycle.

For the Subscription schedule, define the start and end date for the subscription and when to start the billing cycle.

- Choose a payment collection method:Select Automatically charge a payment method on file if you want to charge your customer when the billing cycle starts.Select Email invoice to the customer to pay manually if you want to invoice your customer in arrears.

Choose a payment collection method:

- Select Automatically charge a payment method on file if you want to charge your customer when the billing cycle starts.

- Select Email invoice to the customer to pay manually if you want to invoice your customer in arrears.

- Click Start test subscription to start the subscription and billing cycle. Learn more about all of the options for creating subscriptions in Subscriptions.

Click Start test subscription to start the subscription and billing cycle. Learn more about all of the options for creating subscriptions in Subscriptions.

[Subscriptions](/billing/subscription-resource?dashboard-or-api=dashboard#create-subscriptions)

Both the customer and subscription objects are associated with the clock object you created in the first step. In the Dashboard, the  icon indicates that an object is associated with a clock.

[first step](#create-clock)

[Advance the simulated time](#advance-clock)

## Advance the simulated time

After you’ve created the test clock and set up your test case, advance the simulated time of the clock. The first time you do this, you’ll advance the time from the initial frozen time you set at the creation of the clock. As you advance time, you can see how your integration works when subscriptions end, renew, or undergo other changes (like upgrading from a free trial to a paid subscription).

[creation of the clock](#create-clock)

You can advance test clocks by any increment, but you can only advance them two intervals at a time from their initial frozen time. The length of the interval is based on the shortest subscription interval associated with the test clock, which is determined by the recurring price. For example, if you have a monthly subscription, you can only advance the clock up to two months at a time. If the test clock has no subscriptions or subscription schedules, you can advance it up to two years from the initial frozen time.

To advance time through the Dashboard:

- Go to the test clocks page and find your test clock.

Go to the test clocks page and find your test clock.

[test clocks](https://dashboard.stripe.com/test/test-clocks)

- Click Advance time.

Click Advance time.

- Use the calendar modal to select the date you want to advance the clock to.

Use the calendar modal to select the date you want to advance the clock to.

- Click Advance.

Click Advance.

When the clock is done advancing, the banner updates and displays the clock’s current time.

[Monitor and handle changes](#monitor-changes)

## Monitor and handle changes

After a successful API request or Dashboard operation, the clock takes a few seconds to advance to the specified time. To know when the clock has changed state, you can use webhooks to listen for event notifications or you can poll the clock. The Dashboard also reflects the changes. For example, you can go to the invoices page to check whether an invoice was created or paid for your subscription.

[invoices page](https://dashboard.stripe.com/test/invoices)

If you use webhooks, listen to the following event notifications. Before production, make sure your integration correctly handles the other billing-specific event notifications in addition to the ones listed below.

[webhooks](/webhooks)

[billing-specific event notifications](/billing/subscriptions/webhooks)

To poll the state of the clock, retrieve it by ID to examine its status.

[retrieve](/api/test_clocks/retrieve)

[Update the simulation](#update-simulation)

## Update the simulation

You can continue to make changes to your simulation and advance the clock for simulations like:

[advance the clock](#advance-clock)

- Adding a customer balance.

[customer balance](/billing/customer/balance)

- Making a mid-cycle upgrade.

- Adding one-off invoice items.

[Adding one-off invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items)

After each update, monitor the changes again. Repeat as many times as you need to satisfy your test case.

[monitor the changes](#monitor-changes)

[Delete the clock](#delete-clock)

## Delete the clock

Test clocks are automatically deleted 30 days after you create them, but you can delete them when you’re done testing to ensure a clean test environment.

To delete the clock and all of its associated test objects through the Dashboard:

- Go to the test clocks page and find your test clock.

[test clocks](https://dashboard.stripe.com/test/test-clocks)

- Click Finish simulation.

- In the confirmation modal, click Finish.

Deleting the clock also deletes the test customers associated with the clock and cancels their subscriptions. Test clocks are only available in test mode, so you can’t delete any production objects when you delete a clock.

[Use cases](#use-cases)

## Use cases

First, follow these steps to start using test clocks:

- Create a test clock

[Create a test clock](#create-clock)

- Set up your testing simulation

[Set up your testing simulation](#setup-simulation)

- Advance the clock’s time

[Advance the clock’s time](#advance-clock)

- Monitor and handle the changes

[Monitor and handle the changes](#monitor-changes)

- Update the simulation

[Update the simulation](#update-simulation)

Next, you can test certain subscription renewals using test clocks. Let’s say that you’d like to test that a 50 EUR/month subscription renews correctly. To simulate this situation using test clocks:

- Create a new test clock and set its frozen_time to January 1.

- Add a customer and add a payment method for the customer:

To add a payment method for a customer in the Dashboard:

- From the customer account page, click Add > Add card from the Payment methods section.

- Enter payment information. In this case, use the 4242424242424242 test card.

[test card](/testing#cards)

- Click Add card in the modal.

- After adding a payment method for the customer, create a subscription for the new customer set at 50 EUR/month. In doing so, the invoice of 50 EUR is paid automatically and the subscription is active.

After adding a payment method for the customer, create a subscription for the new customer set at 50 EUR/month. In doing so, the invoice of 50 EUR is paid automatically and the subscription is active.

- Advance the date to February 1 to see that an invoice of 50 EUR is created. By default, the invoice appears in a draft state for one hour.

Advance the date to February 1 to see that an invoice of 50 EUR is created. By default, the invoice appears in a draft state for one hour.

[one hour](/billing/invoices/subscription#adding-draft-invoice-items)

- Advance the time by one hour to see that the invoice is finalized and paid automatically.

Advance the time by one hour to see that the invoice is finalized and paid automatically.

First, follow these steps to start using test clocks:

- Create a test clock

[Create a test clock](#create-clock)

- Set up your testing simulation

[Set up your testing simulation](#setup-simulation)

- Advance the clock’s time

[Advance the clock’s time](#advance-clock)

- Monitor and handle the changes

[Monitor and handle the changes](#monitor-changes)

- Update the simulation

[Update the simulation](#update-simulation)

Next, you can test prorations for customers who upgrade their plans in the middle of a billing cycle. Let’s say that you have two products. One product is 50 EUR/month (‘basic plan’) and the other is 100 EUR/month (‘premium plan’). In this case, you may want to test prorations for a customer who upgrades their ‘basic plan’ to the ‘premium plan’ in the middle of a billing cycle. To simulate this situation using test clocks:

- Create a new test clock and set its frozen_time to January 1.

- Create a customer and add their payment method. In this case, use the 4242424242424242 test card.

[test card](/testing#cards)

- Create a subscription for the ‘basic plan’ at 50 EUR/month. After this is done, you’ll see that the 50 EUR/month invoice is created, finalized, and automatically paid.

- Advance the date by two weeks. In this case, we’ll set the date to January 16.

- Upgrade the subscription to a ‘premium plan’ at 100 EUR/month:

To upgrade a subscription using the Dashboard:

- From the customer account page or the subscription details page, click the overflow menu () associated with a subscription, then select Update subscription.

- Make your desired modifications.

- Click Update subscription in the top right corner to apply the changes.

- After upgrading the subscription, the customer.subscription.updated webhook event is created.

After upgrading the subscription, the customer.subscription.updated webhook event is created.

[customer.subscription.updated](/api/events/types#event_types-customer.subscription.updated)

- Pending invoice items are also created for the prorations. You’ll see a negative proration of -25 EUR for the unused time with the ‘basic plan’ and a positive proration of 50 EUR for using the ‘premium plan’ for half of the remaining month. At this point, no invoice has been generated.

Pending invoice items are also created for the prorations. You’ll see a negative proration of -25 EUR for the unused time with the ‘basic plan’ and a positive proration of 50 EUR for using the ‘premium plan’ for half of the remaining month. At this point, no invoice has been generated.

- Advance the date by two weeks. In this case, we’ll set the date to February 1. You’ll see that the subscription has cycled. An invoice has been generated in a draft state and has incorporated the pending invoice items, including a negative proration, a positive proration, and the total payment for the month of February, resulting in 125 EUR. By default, the invoice appears in a draft state for around one hour.

Advance the date by two weeks. In this case, we’ll set the date to February 1. You’ll see that the subscription has cycled. An invoice has been generated in a draft state and has incorporated the pending invoice items, including a negative proration, a positive proration, and the total payment for the month of February, resulting in 125 EUR. By default, the invoice appears in a draft state for around one hour.

[one hour](/billing/invoices/subscription#adding-draft-invoice-items)

- To finalize the invoice, advance the time by one hour.

To finalize the invoice, advance the time by one hour.

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

## Limitations

For efficient advancement of test clocks, Stripe limits the complexity of each simulation to:

- three customers

- three subscriptions, including scheduled subscriptions, per customer

[scheduled subscriptions](/billing/subscriptions/subscription-schedules)

- ten quotes that aren’t attached to customers

Test clock advancement currently doesn’t support collecting payments through bank debits (for example, us_bank_account payment method types). Stripe collects payments after the test clock advances. To test payment failures:

- Choose the Cancel subscription after all payment retries fail setting.

Choose the Cancel subscription after all payment retries fail setting.

- Attach a us_bank_account payment method type to a customer that fails payments.

Attach a us_bank_account payment method type to a customer that fails payments.

- Create a subscription under the customer.

Create a subscription under the customer.

- Advance the test clock to cycle and collect payment on a subscription.

Advance the test clock to cycle and collect payment on a subscription.

After the Test Clock advances, the subscription remains in the active state. This indicates that the payment collection hasn’t be attempted during test clock advancement, and the subscription has yet to enter the canceled state due to payment_failed.

Listen to the invoice.payment_failed event to monitor the delayed subscription state and invoice payment. The customer.subscription.deleted event indicates that the subscription state is set to canceled.
