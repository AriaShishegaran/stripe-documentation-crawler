htmlMigrate your customer data to Stripe | Stripe Documentation[Skip to content](#main-content)Migrate customer data[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fdata-migrations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fdata-migrations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)# Migrate your customer data to Stripe

Successfully migrate your customers' data to Stripe.Migrating your customer data to Stripe is a multi-step process. After you read through this guide, you’ll:

- Understand the Stripe migration process.
- Be able to scope the timeline for your migration.
- Know the integration elements required for a successful migration.
- Understand how to migrate payment details with minimal disruption to your users.

If you run into issues while trying to migrate customer data, contact Stripe support.

## Build your integration

- Develop your data migration plan, starting with new customers. Your end goal is to migrate 100% of new customers, then migrate existing customers.
- Design a process for customers to update their card information.

## Learn about the migration process

- Review Stripe’s[migration documentation](/get-started/data-migrations/pan-copy-self-serve).
- Contact your previous processor to understand their migrations process.

## Plan a migration and connect with an existing processor

- Identify which payment details you want to migrate.
- Identify which payment methods you want to migrate.
- Find out how many customer records you want to migrate.
- Plan a migration timeline that considers your previous processor, your customer count, and any upcoming deadlines.
- Send the Stripe Migrations team details about your previous processor, Stripe account number, number of records to be migrated, and types of payment methods that you plan to import.

## The Stripe Migrations team

- Introduce your existing processor to Stripe’s Migrations team.
- Complete any action items or provide any additional information requested by Stripe or your existing processors’ migrations team.

## Migrate and update

- Follow communication between Stripe and your previous processor to ensure your team is prepared.
- Respond to any issues identified during migration.
- Look for an email from the Stripe Migration team with the JSON mapping file.
- Parse JSON mapping file and update your database accordingly.
- Implement a process for customers  to update their card information.
- Design your remapping plan, and include[subscription](/billing/subscriptions/creating)remapping where applicable.
- Begin charging existing customers on Stripe.

[PAN data](#migrate-pan-data)If you need to transfer sensitive payment information to or from another payment processor, or even between Stripe accounts, we can help you do so in a secure and PCI-compliant way.

The process differs depending on the type of transfer:

- [Transfer PAN data from one Stripe account to another Stripe account](/get-started/data-migrations/pan-copy-self-serve)
- [Import PAN data to Stripe from another payment processor](/get-started/data-migrations/pan-import)
- [Export PAN data from Stripe to another payment processor](/get-started/data-migrations/pan-export)

For each type of data migration, we can only assist you if your request includes both customer records and the associated payment data. Use Stripe’s Customer API to create, update, or retrieve customer data that doesn’t include payment information.

NoteYou can perform PAN data migrations without using Stripe’s Sigma or Data Pipeline products.

## See also

- [The Customer object](/api/customers/object)
- [The Subscription object](/api/subscriptions/object)
- [Default payment source](/api/customers/object#customer_object-default_source)
- [Products and prices](/products-prices/overview)
- [Billing cycle anchor](/api/subscriptions/create#create_subscription-billing_cycle_anchor)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Build your integration](#build-your-integration)[Learn about the migration process](#familiarize-yourself-with-the-migrations-process)[Plan a migration and connect with an existing processor](#plan-migrations-and-connect-with-existing-processor)[The Stripe Migrations team](#connect-with-the-stripe-migrations-team)[Migrate and update](#migrate-and-update)[PAN data](#migrate-pan-data)[See also](#see-also)Products Used[Billing](/billing)[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`