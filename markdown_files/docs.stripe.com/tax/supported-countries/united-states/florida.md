htmlCollect tax in Florida | Stripe Documentation[Skip to content](#main-content)Florida[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Fflorida)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Fflorida)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[United States](/docs/tax/supported-countries/united-states)# Collect tax in Florida

Learn how to use Stripe Tax to calculate, collect, and report tax in Florida.In Florida, Stripe Tax supports calculation and collection of sales tax.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Florida. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

### Sales tax

Sellers that meet both the state’s sales threshold must register for a Florida sales tax permit, collect sales tax on sales that ship into Florida, and remit that sales tax to the state.

Threshold: 100,000 USD

Period: Previous year

Included transactions: Taxable sales

Effective date: July 1, 2021

### Other taxes

We also support:

- [Florida Communications Services tax](https://floridarevenue.com/taxes/taxesfees/Pages/cst.aspx)—for businesses selling video or audio streaming to customers in Florida. This includes the Communications Services Tax, Communications Services Gross Receipts Tax and Local Communications Services Tax. These taxes only apply when your business has physical presence in Florida. This means there isn’t a revenue threshold for when remote sellers need to pay this tax. Transactions for these taxes aren’t included in Stripe monitoring for Florida.

## Register to collect tax

Register for tax in Florida at the tax authority. Read more about registering for sales tax in the US in our guide.

After you’ve registered to collect tax in Florida, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Florida.

Learn how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates the taxes that apply to your customer’s location.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

### Exports

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

### Location reports

Location reports offer a summary of transaction and refund data for specific US locations and align with Florida filing requirements. You have the option to report on an annual, semiannual, quarterly, or monthly basis.

Reporting-specific considerations:

- Certain areas in Florida can impose an extra sales surtax, but there is a set limit on how much tax will be applied based on the transaction amount. You won’t see a location report for Florida if you had these transactions. Use the[exports](/tax/reports#exports)instead for a detailed tax breakdown of each transaction.
- The location reports don’t include transactions with the Florida Communications Services tax as these are filed to the state using a different report. To see transactions with these taxes, you can use the[exports](/tax/reports#exports).

### Filing

You are responsible for filing and remitting your taxes to Florida. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Introduction to US sales tax and economic nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)[Navigate the sales tax registration process in the US](https://stripe.com/guides/sales-tax-registration-process-us)[How to file sales tax returns in the US](https://stripe.com/guides/how-to-file-sales-tax-us)[Collect tax in the United States using Stripe](/docs/tax/supported-countries/united-states)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`