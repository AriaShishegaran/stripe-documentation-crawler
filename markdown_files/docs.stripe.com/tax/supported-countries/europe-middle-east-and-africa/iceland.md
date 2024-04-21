htmlCollect tax in Iceland | Stripe Documentation[Skip to content](#main-content)Iceland[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Feurope-middle-east-and-africa%2Ficeland)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Feurope-middle-east-and-africa%2Ficeland)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[Europe, Middle East, and Africa](/docs/tax/supported-countries/europe-middle-east-and-africa)# Collect tax in Iceland

Learn how to use Stripe Tax to calculate, collect, and report tax in Iceland.In Iceland, Stripe Tax supports calculation and collection of VAT for remote sellers. You must have no physical presence in the country to collect this tax on Stripe.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Iceland. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

Remote sellers must register for VAT if their taxable turnover in Iceland exceeds 2,000,000 ISK within any 12-month period, and it requires fiscal representation. Remote sellers who provide electronically supplied services and subscriptions to physical papers and magazines for Icelandic consumers can use a simplified registration procedure (VOES) that doesn’t require fiscal representation. Sales to VAT-registered businesses where the customer pays for the VAT through the reverse charge mechanism don’t count towards the threshold.

Threshold: 2,000,000 ISK

Period: 12 months

Included transactions: Any taxable transactions that reverse charge doesn’t apply to.

## Register to collect tax

Find more information on how to register for VAT in Iceland on the government website:

- [Information about VAT in Iceland](https://www.skatturinn.is/english/companies/value-added-tax/)
- [Start to register](https://voes.rsk.is/)

After you’ve registered to collect tax in Iceland, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Iceland.

Learn more about how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates VAT for your transactions in Iceland.

Generally, most transactions are taxable in the jurisdiction where your customer is. Stripe assumes the sale of most goods or services to be taxable unless specifically exempted.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes to Iceland. Stripe doesn’t file taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Collect tax in Europe, Middle East, and Africa](/docs/tax/supported-countries/europe-middle-east-and-africa)[Navigate the VAT registration process in Europe](https://stripe.com/guides/tax-registration-process-europe)[Introduction to indirect tax compliance](https://stripe.com/guides/introduction-to-sales-tax-vat-and-gst-compliance)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`