htmlRevenue Recognition contracts | Stripe Documentation[Skip to content](#main-content)Revenue contracts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Frevenue-contracts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Frevenue-contracts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)# Revenue Recognition contractsBeta

Learn how to configure revenue contracts and model enterprise B2B sales contracts in Stripe Revenue Recognition.Interested in using revenue contracts?Please provide your email address below and our team will be in touch.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.The revenue contracts feature facilitates the representation of enterprise sales-led contracts in Revenue Recognition. It allows you to customize revenue schedules using custom performance obligations that are decoupled from billing periods. Additionally, you can track key metrics at a contract level and improve your financial insights.

## Customize revenue schedules

Revenue contracts enables the creation of custom contract items that dictate how revenue is recognized instead of invoice line items. It allows you to attach billing models (for example, invoices, subscriptions, payments) to the contract used as payment collection containers.

### Example

Given a 2-year B2B contract with monthly billing, you can create a contract item for the 2-year period:

Contract ItemAmount10000[Price](/api/prices)price_1PeriodJan 1, 2022 - Jan 1, 2024You can then attach a transaction/billing model to the contract to be used for payment allocation:

Billing ModelTypesub_sched_1[Subscription Schedule](/api/subscription_schedules)Given this contract setup, Revenue Recognition can augment reports by incorporating non-GAAP accounts like contract assets and deferred revenue. In turn, this enables us to elevate our metrics as the contract undergoes monthly billing.

## Track contract-level metrics

When you open up a revenue contract in Revenue Recognition, you can track high-level metrics across a group of contract items and transactions such as:

- Total contract value
- Annual contract value
- Billing to date
- Revenue to date
- Future schedule billings
- Unbilled deferred revenue

## Integration

### Salesforce CPQ Connector

You can import all your orders and contracts generated in Salesforce using the Stripe Billing Connector for Salesforce CPQ. When this connection is set up, you can manage Stripe Billing subscriptions and revenue contracts associated with your Salesforce orders.

### API

We’re working on a direct API solution for the creation and management of revenue contracts.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Customize revenue schedules](#customize-revenue)[Track contract-level metrics](#contract-level-metrics)[Integration](#integration)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`