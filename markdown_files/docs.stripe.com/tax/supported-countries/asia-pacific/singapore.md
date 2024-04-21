htmlCollect tax in Singapore | Stripe Documentation[Skip to content](#main-content)Singapore[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Fsingapore)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Fsingapore)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[Asia Pacific](/docs/tax/supported-countries/asia-pacific)# Collect tax in Singapore

Learn how to use Stripe Tax to calculate, collect, and report tax in Singapore.In Singapore, Stripe Tax supports calculation and collection of GST.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Singapore. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

Remote sellers must register for GST if the Singaporean taxable turnover exceeded 1 million SGD in the past 12 months (retrospective basis) or is likely to exceed 1 million SGD in the next 12 months (prospective basis).

A special registration rule applies to remote sellers of digital services. As of Jan 1, 2020, non-resident suppliers must register under the Overseas Vendor Registration regime if in a calendar year:

1. They have a global turnover exceeding 1 million SGD.
2. They make B2C supplies of digital services to customers in Singapore exceeding 100,000 SGD. Global turnover refers to all supplies made that would be taxable supplies if made in Singapore.

Stripe only monitors the 100,000 SGD threshold of the Overseas Vendor Registration.

### Domestic Registration

Threshold: 1 million SGD

Time frame: Previous or current year.

Included transactions: Any taxable transactions that reverse charge doesn’t apply to.

### Overseas Vendor Registration

Threshold: 100,000 SGD and 1 million SGD (global turnover)

Time frame: Calendar year.

Included transactions: For the 100,000 SGD threshold, any taxable transactions that:

- Is either a digital good or an electronically supplied service
- Is a B2C transaction

## Register to collect tax

Find more information on how to register for GST in Singapore on the government website:

- [Information about GST](https://www.iras.gov.sg/taxes/goods-services-tax-(gst))
- [How to register](https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-registration-deregistration/applying-for-gst-registration)

After you’ve registered to collect tax in Singapore, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Singapore.

Learn more about how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates GST for your transactions in Singapore.

Generally, most transactions are taxable in the jurisdiction where your customer is. Stripe assumes the sale of most goods or services to be taxable unless specifically exempted.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes to Singapore. Stripe doesn’t file taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`