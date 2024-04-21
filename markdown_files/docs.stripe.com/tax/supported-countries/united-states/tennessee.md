htmlCollect tax in Tennessee | Stripe Documentation[Skip to content](#main-content)Tennessee[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Ftennessee)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Ftennessee)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[United States](/docs/tax/supported-countries/united-states)# Collect tax in Tennessee

Learn how to use Stripe Tax to calculate, collect, and report tax in Tennessee.## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Tennessee. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

Sellers with sales exceeding the threshold must register for a Tennessee sales tax permit, collect sales tax on sales that ship into Tennessee, and remit sales tax back to the state.

Threshold: 100,000 USD

Period: 12 months

Included transactions: Retail sales

Effective date: October 1, 2019

## Register to collect tax

Register for sales tax in Tennessee at the tax authority. Read more about registering for sales tax in the US in our guide.

After you’ve registered to collect tax in Tennessee, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Tennessee.

Learn how to add your registration in the Dashboard.

## How we calculate taxes

If your origin address is in the US and differs from your customer’s state, Stripe always calculates tax based on your customer’s location.

If your customer is in Tennessee and your origin address is also in Tennessee, Stripe applies tax based on your origin address, depending on the type of product or service you sell.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

### Exports

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

### Location reports

Location reports offer a summary of transaction and refund data for specific US locations and align with Tennessee filing requirements. You have the option to report on an annual, fiscal year, quarterly, or monthly basis.

Reporting-specific considerations:

- In most areas of Tennessee, if the price of a single item exceeds the local tax limit for that specific area, the local tax doesn’t apply to that excess amount. You won’t see a location report for Tennessee if you have these transactions. Use the[exports](/tax/reports#exports)instead for a detailed tax breakdown of each transaction.

### Filing

You are responsible for filing and remitting your taxes to Tennessee. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Introduction to US sales tax and economic nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)[Navigate the sales tax registration process in the US](https://stripe.com/guides/sales-tax-registration-process-us)[How to file sales tax returns in the US](https://stripe.com/guides/how-to-file-sales-tax-us)[Collect tax in the United States using Stripe](/docs/tax/supported-countries/united-states)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`