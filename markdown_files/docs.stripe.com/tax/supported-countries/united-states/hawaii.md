htmlCollect tax in Hawaii | Stripe Documentation[Skip to content](#main-content)Hawaii[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Fhawaii)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Fhawaii)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[United States](/docs/tax/supported-countries/united-states)# Collect tax in Hawaii

Learn how to use Stripe Tax to calculate, collect, and report tax in Hawaii.## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Hawaii. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

Sellers that meet either the sales or transaction number thresholds must register for a Hawaii sales tax permit, collect sales tax on sales that ship into Hawaii, and remit that sales tax to the state.

Threshold: 100,000 USD or 200 transactions

Period: Previous or current year

Included transactions: Gross sales

Effective date: July 1, 2018

## Register to collect tax

Register for sales tax in Hawaii at the tax authority. Read more about registering for sales tax in the US in our guide.

After you’ve registered to collect tax in Hawaii, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Hawaii.

Learn how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates the taxes that apply to your customer’s location.

Instead of a traditional sales tax paid by consumers, Hawaii has a tax on businesses called General Excise Tax (GET). Businesses can recover GET by passing it on to their customers. Businesses generally display GET as a separate item on receipts, but they are not required to do so.

Because a business must pay GET on the entire amount paid by a customer, it also owes GET on any GET reimbursement it collects from customers. To cover that additional tax amount, Hawaii allows businesses to pass GET on to customers at a higher rate than the base GET rate. Stripe Tax only supports the maximum pass-on rate, which fully covers a business’ GET liability.

For example:

A product sells for 100 USD and is subject to 4% GET, so the seller owes 4 USD GET. If the seller passes that on to the customer and collects 104 USD, the entire amount is subject to 4% GET. As a result, the seller’s GET liability becomes 4.16 USD.

The seller can recover the entire GET amount from the customer by instead using the maximum pass-on rate, which for a 4% GET rate is 4.166%. That lets the seller charge the customer 4.166%, or 4.16 USD, which covers their entire GET liability. GET rates can vary by county and by business type. To learn more about GET and the maximum pass-on rates, see Hawaii’s tax facts page.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

### Exports

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

### Location reports

Location reports offer a summary of transaction and refund data for specific US locations and align with Hawaii filing requirements. You have the option to report on an annual, semiannual, quarterly, or monthly basis.

Reporting-specific considerations:

- In Hawaii, wholesalers are required to identify wholesale sales because they’re subject to a lower tax rate instead of being completely exempt. You won’t see a location report for Hawaii if you have any customer-exempt transactions. Use the[exports](/tax/reports#exports)instead for a detailed tax breakdown of each transaction.

### Filing

You are responsible for filing and remitting your taxes to Hawaii. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Introduction to US sales tax and economic nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)[Navigate the sales tax registration process in the US](https://stripe.com/guides/sales-tax-registration-process-us)[How to file sales tax returns in the US](https://stripe.com/guides/how-to-file-sales-tax-us)[Collect tax in the United States using Stripe](/docs/tax/supported-countries/united-states)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`