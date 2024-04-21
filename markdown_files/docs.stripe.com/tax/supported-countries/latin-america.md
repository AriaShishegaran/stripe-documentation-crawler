htmlCollect tax in Latin America | Stripe Documentation[Skip to content](#main-content)Latin America[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Flatin-america)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Flatin-america)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)# Collect tax in Latin America

Learn how to use Stripe Tax to calculate, collect, and report tax in LATAM.In the Latin America (LATAM) region, Stripe supports tax calculation in the following countries. Click the following links to learn about the thresholds in each country and the types of goods and services we support.

- [Chile](/tax/supported-countries/latin-america/chile)
- [Colombia](/tax/supported-countries/latin-america/colombia)
- [Mexico](/tax/supported-countries/latin-america/mexico)

## When and how to register for tax collection

Different rules determine when and how you need to register to collect tax depending on the country. Click the links above to learn about the thresholds for tax collection in each location.

Use the Thresholds tab to get insights about your potential tax registration obligations in each location. Stripe only monitors if you have reached a tax threshold for sales outside of the country your business is based in. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

In Chile, Colombia, and Mexico your business needs to be a remote seller with no physical presence (such as a shop or warehouse) to collect tax on Stripe.

After you’ve registered with a country, add your registration to Stripe in the Registrations tab in the Dashboard to start collecting tax on your transactions in that location.

## How we calculate taxes

Stripe only supports calculation for digital products in Chile, Colombia, and Mexico sold by remote sellers.

### Domestic transactions

A transaction where your business and your customer are in the same country is called a domestic transaction. Stripe doesn’t yet support calculation on domestic transactions in this region.

### Cross border transactions

A cross-border transaction is where your customer is located in a different country to your business or when goods are shipped from one country to another.

Stripe calculates tax on a cross-border transaction taking into account the following factors:

- the location of your business
- the tax registrations you’ve added to Stripe
- the location of the buyer
- the type of the product sold (based on which[product tax code](/tax/tax-codes)you assigned to your product)
- the status of the customer (whether they’re an individual or a business)

Digital products![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Digital products are non-physical items or services that are delivered, given, or rendered electronically. This includes digital goods and electronically supplied services. We determine whether you’re selling digital products or physical goods using the product tax code you assigned to your product.

Digital products are generally taxable in the country where your customer is located. However sales of digital products to businesses in other countries might have reverse charge applied. With reverse charge, your business provides an invoice for the purchase so that your customer can calculate the tax.

Physical goods![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When physical goods are shipped to a customer in a different country to your business, the transaction is referred to as an export. Stripe doesn’t yet support calculation on exports of physical goods in this region.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes. Stripe doesn’t file taxes on your behalf.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When and how to register for tax collection](#when-and-how-to-register-for-tax-collection)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Introduction to indirect tax compliance](https://stripe.com/guides/introduction-to-sales-tax-vat-and-gst-compliance)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`