htmlAPI and advanced usage | Stripe Documentation[Skip to content](#main-content)API and advanced usage[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting%2Ftest-clocks%2Fapi-advanced-usage)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting%2Ftest-clocks%2Fapi-advanced-usage)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Test your integration](/docs/billing/testing)[Test clocks](/docs/billing/testing/test-clocks)# API and advanced usage

Learn advanced strategies for using test clocks in the Dashboard and API.You can create a test clock separately from a subscription for running advanced simulations. In this scenario you create the test clock first and then add different test cases to it.

Not ready for a full integration? See our guide for running simulations on subscriptions.

![How to set a test clock to simulate subscription time elpasing.](https://b.stripecdn.com/docs-statics-srv/assets/test-clock-lifecycle.b711b9cf4feb52351e27958b8b924cb3.png)

Test clock lifecycle

Follow these steps to start using test clocks:

1. [Create a test clock](#create-clock)
2. [Set up your testing simulation](#setup-simulation)
3. [Advance the clock’s time](#advance-clock)
4. [Monitor and handle the changes](#monitor-changes)
5. [Update the simulation](#update-simulation)
6. [Delete the clock](#delete-clock)

You can advance the clock’s time, monitor changes, and update the simulation as often as you need to test different cases.

[Create a clock and set its time](#create-clock)To start a simulation, create a clock and set its frozen time. The temporal starting point for all subscriptions associated with this clock. You can set this to a time in the future or in the past to test different simulations, but you can only move it forward in time after you set it.

DashboardAPITo create a test clock in the Dashboard, follow the steps below. Set the Dashboard to Test mode to use test clocks.

1. Go to theSubscriptions[section](https://dashboard.stripe.com/test/subscriptions)under theBillingtab.
2. Click the[test clocks](https://dashboard.stripe.com/test/test-clocks)link in the banner.
3. ClickNew simulation.
4. In theCreate new simulationmodal, enter a name for the simulation. You can use this to describe the simulation you’re testing, like`Annual renewal`or`Free trial`.
5. Set the frozen time of the clock. This is the starting point for your simulation. You can set this to a time in the future or in the past, but you can only move it forward in time after you set it.

[Set up your simulation](#setup-simulation)Next, set up the test case for your simulation. You need to create a customer first, then a subscription for them.

DashboardAPITo create a customer for your simulation through the Dashboard:

1. Go to the[test clocks](https://dashboard.stripe.com/test/test-clocks)page and find your test clock.
2. ClickAdd>Add customer.

You can’t choose existing customers during test clock simulations. You can add up to three new customers to each simulation.

You can optionally enter other available properties for the customer, like their name, email, and billing information, but none are required. For some simulations, like testing free trials, you might not want to collect any billing information up front.

Next, you can create up to three subscriptions or subscription schedules for your customer. To create a subscription for the customer through the Dashboard:

1. Go to the test clocks page and find your test clock.


2. Click Add > Add subscription. Select or search for your customer from the drop-down menu. You can also add the customer to a subscription through the customer page, by clicking Actions > Create subscription.


3. Select a recurring product and price in the Pricing section.


4. For the Subscription schedule, define the start and end date for the subscription and when to start the billing cycle.


5. Choose a payment collection method:

  - SelectAutomatically charge a payment method on fileif you want to charge your customer when the billing cycle starts.
  - SelectEmail invoice to the customer to pay manuallyif you want to invoice your customer in arrears.


6. Click Start test subscription to start the subscription and billing cycle. Learn more about all of the options for creating subscriptions in Subscriptions.



Both the customer and subscription objects are associated with the clock object you created in the first step. In the Dashboard, the  icon indicates that an object is associated with a clock.

[Advance the simulated time](#advance-clock)After you’ve created the test clock and set up your test case, advance the simulated time of the clock. The first time you do this, you’ll advance the time from the initial frozen time you set at the creation of the clock. As you advance time, you can see how your integration works when subscriptions end, renew, or undergo other changes (like upgrading from a free trial to a paid subscription).

You can advance test clocks by any increment, but you can only advance them two intervals at a time from their initial frozen time. The length of the interval is based on the shortest subscription interval associated with the test clock, which is determined by the recurring price. For example, if you have a monthly subscription, you can only advance the clock up to two months at a time. If the test clock has no subscriptions or subscription schedules, you can advance it up to two years from the initial frozen time.

DashboardAPITo advance time through the Dashboard:

1. Go to the test clocks page and find your test clock.


2. Click Advance time.


3. Use the calendar modal to select the date you want to advance the clock to.


4. Click Advance.



When the clock is done advancing, the banner updates and displays the clock’s current time.

[Monitor and handle changes](#monitor-changes)After a successful API request or Dashboard operation, the clock takes a few seconds to advance to the specified time. To know when the clock has changed state, you can use webhooks to listen for event notifications or you can poll the clock. The Dashboard also reflects the changes. For example, you can go to the invoices page to check whether an invoice was created or paid for your subscription.

If you use webhooks, listen to the following event notifications. Before production, make sure your integration correctly handles the other billing-specific event notifications in addition to the ones listed below.

EventDescription`test_helpers.test_clock.advancing`The clock has started to advance but hasn’t reached the specified time.`test_helpers.test_clock.ready`The clock has completed advancing to the specified time.To poll the state of the clock, retrieve it by ID to examine its status.

Command Line[curl](#)`curl https://api.stripe.com/v1/test_helpers/test_clocks/{{CLOCK_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Update the simulation](#update-simulation)You can continue to make changes to your simulation and advance the clock for simulations like:

- Adding a[customer balance](/billing/customer/balance).
- Making a mid-cycle upgrade.
- [Adding one-off invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items).

After each update, monitor the changes again. Repeat as many times as you need to satisfy your test case.

[Delete the clock](#delete-clock)Test clocks are automatically deleted 30 days after you create them, but you can delete them when you’re done testing to ensure a clean test environment.

DashboardAPITo delete the clock and all of its associated test objects through the Dashboard:

1. Go to the[test clocks](https://dashboard.stripe.com/test/test-clocks)page and find your test clock.
2. ClickFinish simulation.
3. In the confirmation modal, clickFinish.

Deleting the clock also deletes the test customers associated with the clock and cancels their subscriptions. Test clocks are only available in test mode, so you can’t delete any production objects when you delete a clock.

[Use cases](#use-cases)### Test subscription renewals

First, follow these steps to start using test clocks:

1. [Create a test clock](#create-clock)
2. [Set up your testing simulation](#setup-simulation)
3. [Advance the clock’s time](#advance-clock)
4. [Monitor and handle the changes](#monitor-changes)
5. [Update the simulation](#update-simulation)

Next, you can test certain subscription renewals using test clocks. Let’s say that you’d like to test that a 50 EUR/month subscription renews correctly. To simulate this situation using test clocks:

- Create a new test clock and set its`frozen_time`to January 1.
- Add a customer and add a payment method for the customer:

DashboardAPITo add a payment method for a customer in the Dashboard:

1. From the customer account page, clickAdd > Add cardfrom thePayment methodssection.
2. Enter payment information. In this case, use the4242424242424242[test card](/testing#cards).
3. ClickAdd cardin the modal.

- After adding a payment method for the customer, create a subscription for the new customer set at 50 EUR/month. In doing so, the invoice of 50 EUR is paid automatically and the subscription is active.


- Advance the date to February 1 to see that an invoice of 50 EUR is created. By default, the invoice appears in a draft state for one hour.


- Advance the time by one hour to see that the invoice is finalized and paid automatically.



### Test mid-cycle upgrades with prorations

First, follow these steps to start using test clocks:

1. [Create a test clock](#create-clock)
2. [Set up your testing simulation](#setup-simulation)
3. [Advance the clock’s time](#advance-clock)
4. [Monitor and handle the changes](#monitor-changes)
5. [Update the simulation](#update-simulation)

Next, you can test prorations for customers who upgrade their plans in the middle of a billing cycle. Let’s say that you have two products. One product is 50 EUR/month (‘basic plan’) and the other is 100 EUR/month (‘premium plan’). In this case, you may want to test prorations for a customer who upgrades their ‘basic plan’ to the ‘premium plan’ in the middle of a billing cycle. To simulate this situation using test clocks:

- Create a new test clock and set its`frozen_time`to January 1.
- Create a customer and add their payment method. In this case, use the4242424242424242[test card](/testing#cards).
- Create a subscription for the ‘basic plan’ at50EUR/month. After this is done, you’ll see that the50EUR/month invoice is created, finalized, and automatically paid.
- Advance the date by two weeks. In this case, we’ll set the date to January 16.
- Upgrade the subscription to a ‘premium plan’ at100EUR/month:

DashboardAPITo upgrade a subscription using the Dashboard:

1. From the customer account page or the subscription details page, click the overflow menu () associated with a subscription, then selectUpdate subscription.
2. Make your desired modifications.
3. ClickUpdate subscriptionin the top right corner to apply the changes.

- After upgrading the subscription, the customer.subscription.updated webhook event is created.


- Pending invoice items are also created for the prorations. You’ll see a negative proration of -25 EUR for the unused time with the ‘basic plan’ and a positive proration of 50 EUR for using the ‘premium plan’ for half of the remaining month. At this point, no invoice has been generated.


- Advance the date by two weeks. In this case, we’ll set the date to February 1. You’ll see that the subscription has cycled. An invoice has been generated in a draft state and has incorporated the pending invoice items, including a negative proration, a positive proration, and the total payment for the month of February, resulting in 125 EUR. By default, the invoice appears in a draft state for around one hour.


- To finalize the invoice, advance the time by one hour.



### Test trials

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

## Limitations

For efficient advancement of test clocks, Stripe limits the complexity of each simulation to:

- three customers
- three subscriptions, including[scheduled subscriptions](/billing/subscriptions/subscription-schedules), per customer
- ten quotes that aren’t attached to customers

### Caveats with payment processing

Test clock advancement currently doesn’t support collecting payments through bank debits (for example, us_bank_account payment method types). Stripe collects payments after the test clock advances. To test payment failures:

1. Choose the Cancel subscription after all payment retries fail setting.


2. Attach a us_bank_account payment method type to a customer that fails payments.


3. Create a subscription under the customer.


4. Advance the test clock to cycle and collect payment on a subscription.



After the Test Clock advances, the subscription remains in the active state. This indicates that the payment collection hasn’t be attempted during test clock advancement, and the subscription has yet to enter the canceled state due to payment_failed.

Listen to the invoice.payment_failed event to monitor the delayed subscription state and invoice payment. The customer.subscription.deleted event indicates that the subscription state is set to canceled.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a clock and set its time](#create-clock)[Set up your simulation](#setup-simulation)[Advance the simulated time](#advance-clock)[Monitor and handle changes](#monitor-changes)[Update the simulation](#update-simulation)[Delete the clock](#delete-clock)[Use cases](#use-cases)[Limitations](#restrictions)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`