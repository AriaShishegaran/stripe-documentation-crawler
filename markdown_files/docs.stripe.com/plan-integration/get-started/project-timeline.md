htmlProject timeline | Stripe Documentation[Skip to content](#main-content)Project timeline[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fplan-integration%2Fget-started%2Fproject-timeline)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fplan-integration%2Fget-started%2Fproject-timeline)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)
[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Plan your integration# Project timeline

Follow our project timeline to successfully integrate Stripe.A Stripe payments integration lets you accept payments, receive payouts, and reconcile your accounts. Use Stripe Elements to create a customized checkout flow with prebuilt UI components. Alternatively, use Checkout to build a payment form and embed it on your site or host it on Stripe.

Stripe’s APIs enable secure processing of payments across various global payment methods and currencies. Our APIs and the Dashboard centralize reporting, providing real-time data on charges, fees, refunds, and transfers. Get started by logging in or registering for a Stripe account.

[Get started](#project-timeline)While you can integrate payments in as little as 1 week, the following timeline assumes that your business has internal systems that add complexity to your Stripe integration. With this in mind, we estimate that the total integration time can range from less than 1 week to up to 3 months. Primary dependencies include engineering resources, internal system integrations, and change management across impacted teams.

PhaseDurationTaskDesign1 weekFinalize decisions outlined in[Planning considerations](/plan-integration/get-started/planning-considerations)in consultation with impacted teams.Setup1-2 daysCreate and[activate your Stripe account](https://dashboard.stripe.com/register)by signing up and completing your business profile.Build1-2 weeksBuild your[frontend integration](/plan-integration/get-started/planning-considerations#how-capture-payment-details)12-4 weeksBuild your[server-side integration](/plan-integration/get-started/server-side-integration)12 weeksBuild your[reporting and reconciliation](/plan-integration/get-started/reporting-reconciliation)pipeline.1Train1 week eachTeam-specific trainings and playbooks for Stripe environment, for example:- Fraud and disputes
- Customer service
- Finance and accounting

Test and go live1 weekTest end-to-end in test and live environments.[Testing](/plan-integration/get-started/testing)for tools to test your integration.Migrate22-4 weeksWhen 100% of new customers are on Stripe, migrate existing customers to Stripe. See[Migrating data to Stripe](/get-started/data-migrations)for more information.1 Tasks in the same phase can be completed in parallel.2 Applicable if you’re migrating customer data from your previous processor.

## Key decisions

Before you start integrating Stripe, review the following:

- [Structure your Stripe account](/plan-integration/get-started/planning-considerations#structure-stripe-accounts)
- [Accept payments](/plan-integration/get-started/planning-considerations#how-accept-payments)
- [Capture customer payment details](/plan-integration/get-started/planning-considerations#how-capture-payment-details)
- [Reconcile your payments and payouts](/plan-integration/get-started/planning-considerations#how-reconcile-payments-payouts)
- [Protect your business from fraud and disputes](/plan-integration/get-started/planning-considerations#how-protect-fraud-disputes)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#project-timeline)[Key decisions](#key-decisions)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`