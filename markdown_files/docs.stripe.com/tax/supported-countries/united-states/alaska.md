htmlCollect tax in Alaska | Stripe Documentation[Skip to content](#main-content)Alaska[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Falaska)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Falaska)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[United States](/docs/tax/supported-countries/united-states)# Collect tax in Alaska

Learn how to use Stripe Tax to calculate, collect, and report tax in Alaska.## When to register for tax collection

Alaska doesn’t have a state sales tax. However local jurisdictions within Alaska may impose a sales and use tax. Each jursidiction can define what it means to be doing business in that location and whether sales tax applies. Many local jurisdictions in Alaska have chosen to adopt the Alaska Remote Seller Sales Tax Commission (ARSSTC) uniform tax code. This includes using state-wide thresholds to determine whether a business needs to pay tax there.

Businesses who are remote sellers or marketplace facilitators need to register with the commission and collect tax on their sales into member Alaska localities if they have 100,000 USD or more in annual gross receipts from sales, or 200 or more sales annually into the state.

Threshold: 100,000 USD or 200 transactions

Period: Previous or current year

Included transactions: Gross sales

Effective date: The state passed The Alaska Remote Seller Sales Tax Code on January 6, 2020. However, local jurisdictions decide whether to adopt the code. After a local jurisdiction adopts the code, businesses have 30 days to begin collecting sales tax from Alaska buyers located in that jurisdiction.

Use the Thresholds tab to get insights about your sales into the state and potential tax registration obligations in Alaska. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

## Register to collect tax

Register for sales tax in Alaska at the tax authority:

- Remote sellers can register with the[Alaska Remote Seller Sales Tax Commission](https://arsstc.munirevs.com/)
- Businesses with a physical presence in the state need to[register in that particular location](https://arsstc.org/business-sellers/).

Read more about registering for sales tax in the US in our guide.

After you’ve registered to collect tax in Alaska, add your registration to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in the local jurisdictions with economic nexus laws.

Learn how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates the taxes that apply to your customer’s location.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

### Exports

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

### Location reports

Alaska doesn’t impose any state sales or use tax. However, local jurisdictions can apply these taxes. A location report isn’t available to view these details. Instead, use the exports to obtain a detailed breakdown of local jurisdiction sales and use tax.

### Filing

You are responsible for filing and remitting your taxes to Alaska. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Introduction to US sales tax and economic nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)[Navigate the sales tax registration process in the US](https://stripe.com/guides/sales-tax-registration-process-us)[How to file sales tax returns in the US](https://stripe.com/guides/how-to-file-sales-tax-us)[Collect tax in the United States using Stripe](/docs/tax/supported-countries/united-states)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`