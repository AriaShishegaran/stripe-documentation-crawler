htmlCollect tax in Norway | Stripe Documentation[Skip to content](#main-content)Norway[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Feurope-middle-east-and-africa%2Fnorway)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Feurope-middle-east-and-africa%2Fnorway)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[Europe, Middle East, and Africa](/docs/tax/supported-countries/europe-middle-east-and-africa)# Collect tax in Norway

Learn how to use Stripe Tax to calculate, collect, and report tax in Norway.In Norway, Stripe Tax supports calculation and collection of VAT.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Norway. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

If you’re based outside Norway, you must register in Norway as soon as your taxable sales in Norway reach 50,000 NOK during a period of 12 months and no reverse charge applies. Businesses located in the European Economic Area can register directly with the Norwegian tax administration. Businesses located outside the EEA must appoint a Norwegian VAT representative unless they use the simplified registration procedure (VOEC), which is available for B2C sales of digital services and low-value goods (< ​3,000 NOK).

For example, if you’re based in the US, sell digital services to Norwegian consumers and exceed the threshold during a period of 12 months (from February of the past year to January of the current year), you must register in Norway. However, if you sell digital services only to Norwegian businesses, you don’t need to register because these services are subject to reverse charge.

Threshold: 50,000 NOK

Period: 12 months

Included transactions: Any taxable transactions that reverse charge doesn’t apply to.

## Register to collect tax

Find more information on how to register for VAT in Norway on the government website:

- [General information about VAT in Norway](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/)
- [How to register](https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/)

After you’ve registered to collect tax in Norway, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Norway.

Learn more about how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates VAT for your transactions in Norway.

Generally, most transactions are taxable in the jurisdiction where your customer is. Stripe assumes the sale of most goods or services to be taxable unless specifically exempted.

In Norway, there are some territories outside of the scope of the standard tax system and might have different rules that apply. Stripe won’t calculate tax for customers based there, even if you’ve added a registration for Norway. Learn more about how Stripe handles excluded territories. This applies to the following locations:

- Jan Mayen
- Svalbard

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes to Norway. Stripe doesn’t file taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Collect tax in Europe, Middle East, and Africa](/docs/tax/supported-countries/europe-middle-east-and-africa)[Navigate the VAT registration process in Europe](https://stripe.com/guides/tax-registration-process-europe)[Introduction to indirect tax compliance](https://stripe.com/guides/introduction-to-sales-tax-vat-and-gst-compliance)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`