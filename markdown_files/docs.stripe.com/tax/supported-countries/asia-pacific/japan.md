htmlCollect tax in Japan | Stripe Documentation[Skip to content](#main-content)Japan[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Fjapan)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Fjapan)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[Asia Pacific](/docs/tax/supported-countries/asia-pacific)# Collect tax in Japan

Learn how to use Stripe Tax to calculate, collect, and report tax in Japan.In Japan, Stripe Tax supports calculation and collection of Consumption Tax (CT).

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Japan. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

Remote sellers must register in Japan if:

- Their taxable sales in Japan exceed the registration threshold of 10 million JPY in the base period.
- Their taxable sales or salaries paid exceed 10 million JPY in the specified period.

The base period refers to:

- The calendar year two years prior to the current one (for example, the base period for the year of 2021 is 2019). This applies to sole proprietors.
- The business year two years prior to the current one. This applies to corporations.

The specified period refers to the first 6 months of the previous calendar year (for sole proprietors) or the first 6 months of a fiscal year (for corporations).

Registered remote sellers must have an office located in Japan or have a tax representative in Japan. Remote sellers that provide electronic services to Japanese consumers can use a simplified registration procedure.

Threshold: 10 million JPY

Time frame: Japanese base period and specified period as defined above.

Included transactions: Any taxable transactions that reverse charge doesn’t apply to.

## Register to collect tax

To collect Consumption Tax, any business must either have an office located in Japan or have a tax representative in Japan. This also applies to remote sellers of electronic services, however there is a simplified registration process for these businesses.

Find more information on how to register for CT in Japan on the government website:

- [General information about Consumption Tax in Japan](https://www.nta.go.jp/english/taxes/consumption_tax/01.htm)
- [Registration for remote sellers of electronic services](https://www.nta.go.jp/english/taxes/consumption_tax/04.htm)

After you’ve registered to collect tax in Japan, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Japan.

Learn more about how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates CT for your transactions in Japan.

Generally, most transactions are taxable in the jurisdiction where your customer is. Stripe assumes the sale of most goods or services to be taxable unless specifically exempted.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes to Japan. Stripe doesn’t file taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`