htmlBilling for a multi-entity business | Stripe Documentation[Skip to content](#main-content)Integrate a multi-entity business[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fmulti-entity-business)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fmulti-entity-business)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Build a subscriptions integration](/docs/billing/subscriptions/build-subscriptions)# Billing for a multi-entity business

Integrate Stripe Billing for a business with more than one legal entity.Stripe requires you to have a separate account for each legal entity. Businesses might need to create different legal entities to accommodate international operations, set up financial isolation for different business units, or handle acquisitions. Use this guide to learn how to set up multiple Stripe accounts for a business that has multiple legal entities.

## Multiple entities architecture

To manage multiple legal entities in a scalable way, we recommend using Stripe Connect with a Standard account, where you have a platform account that serves as a single entry point, and multiple connected accounts for each line of business.

![Organization with multiple accounts setup using Connect](https://b.stripecdn.com/docs-statics-srv/assets/structure_4_before.e35e09f6d8127fb01f240a30834b99b7.png)

A platform account and multiple connected accounts, each representing different business lines.

With this account configuration, each account can maintain its own customers, subscriptions, and product catalog. The platform account provides a single integration point and a single, shared API key that you can use to manage multiple connected Stripe accounts.

You create a service on your app to route customers to the right account when they check out. On the backend, your integration passes in the correct account ID to make a direct charge for the relevant Standard account, which settles funds to that entity’s bank account.

[Metrics and analytics](#monitor)To get a consolidated view of metrics for multiple Stripe accounts, use the Stripe Data Pipeline to sync your Stripe account with an external system. You can export the data for all your accounts to your data warehouse, where you can apply analytic tools to get business insights.

[Accounting reports](#accounting)Use Revenue Recognition to export and consolidate accounting reports. You can also import data into a single account and get a comprehensive view that way.

[Product catalog](#product-catalog)Your product catalog can be part of the platform account or each connected Standard account. Where you maintain your catalog depends on your business needs. For example, a company that operates in the US and in the EU likely wants to keep the catalog with the connected accounts to help them maintain local prices. A company with a global website that serves customers in multiple currencies likely wants to keep the catalog with the platform account and use multi-currency prices.

### Lookup keys

To efficiently manage product catalogs for connected accounts, use lookup keys. Product IDs and lookup key names only need to be unique for each account.

[Entitlements](#entitlements)To correctly associate a customer with a Stripe account, store the customer ID and Stripe account ID in your database so that when you check the statuses of invoices and subscriptions for entitlements, you know you’re referencing the correct Stripe account.

[Tax](#tax)If you want to report taxes as a single entity for two Stripe accounts, you can merge the tax reports of those accounts. Export the data then combine the reports in a spreadsheet or with a partner such as TaxJar or Avalara.

[Revenue recovery](#rev-recovery)To enable revenue recovery, configure invoice templates, subscription lifecycles, and dunning emails for each individual Stripe account.

[Payment methods](#payment-methods)To correctly associate a customer with a Stripe account, store the customer ID and Stripe account ID in your database. Doing so means that when you check the statuses of invoices and subscriptions for entitlements, you know you’re referencing the correct Stripe account.

To transition to multiple Stripe accounts, we recommend setting up a platform account and a connected account when you first get started.

### Limitations

Payment method cloning currently has the following limitations:

- You can only clone payment methods that have the[type](/api/payment_methods/object#payment_method_object-type)set to`card`or`us_bank_account`.
- You can’t clone payment methods from one connected account to another connected account.
- You can’t clone payment methods from a connected account to a platform account.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Multiple entities architecture](#multiple-entities-architecture)[Metrics and analytics](#monitor)[Accounting reports](#accounting)[Product catalog](#product-catalog)[Entitlements](#entitlements)[Tax](#tax)[Revenue recovery](#rev-recovery)[Payment methods](#payment-methods)Related Guides[Usage-based pricing model](/docs/products-prices/pricing-models#usage-based-pricing)[Billing quickstart](/docs/billing/quickstart)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`