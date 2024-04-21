htmlTest your integration with test clocks | Stripe Documentation[Skip to content](#main-content)Test clocks[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting%2Ftest-clocks)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftesting%2Ftest-clocks)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Test your integration](/docs/billing/testing)# Test your integration with test clocks

Learn how to move Billing objects through time in test mode.## Overview

Test clocks help you test your Billing integration and make sure it behaves as designed. When you use test clocks you simulate the forward movement of time in test mode, which causes Billing resources, like Subscriptions, to change state and trigger webhook events. This means that, for example, you don’t have to wait a year to see how your integration handles a payment failure for a quarterly or annual renewal.

Here are some other things you can do with test clocks:

- Test complex simulations such as upgrading or changing plans mid-cycle.
- Ensure your integration processes Billing lifecycle webhooks correctly.
- Validate that your app handles trials correctly.
- Build and test multi-phase subscription schedules.

## How to use test clocks

[Simulate subscriptionsLearn how to simulate subscriptions in test mode.](/billing/testing/test-clocks/simulate-subscriptions)[API and advanced usageLearn advanced strategies for using test clocks in the Dashboard and API.](/billing/testing/test-clocks/api-advanced-usage)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`