htmlSimulate subscriptions | Stripe Documentation[Skip to content](#main-content)Simulate subscriptions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting%2Ftest-clocks%2Fsimulate-subscriptions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting%2Ftest-clocks%2Fsimulate-subscriptions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Test your integration](/docs/billing/testing)[Test clocks](/docs/billing/testing/test-clocks)# Simulate subscriptions

Learn how to simulate subscriptions in test mode.To simulate any existing or new subscriptions in test mode:

1. Open the Dashboard and enableTest mode.
2. In the[subscriptions](https://dashboard.stripe.com/test/subscriptions)page, click the subscription to test.
3. ClickRun simulationin the banner at the top of the page.Customer ineligible for simulationThe Run simulation button might be disabled if the subscription’s customer:

  - Is attached to more than three subscriptions, including[scheduled subscriptions](/billing/subscriptions/subscription-schedules)
  - Has a complex profile, with many quotes, invoices or other related objects


4. In the modal, set the date and time to simulate and clickAdvance time.

You can advance time by any increment, but you can only advance them two intervals at a time from the initial frozen time. For example, if you have a monthly subscription, you can only advance the clock up to two months at a time.

When the clock is done advancing, the banner updates and displays the clock’s current time.

You can continue to make changes to your simulation and advance the time for simulations like:

- Adding a[customer balance](/billing/customer/balance).
- Making a mid-cycle upgrade.
- [Adding one-off invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items).

Repeat as many times as you need to satisfy your test case.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`