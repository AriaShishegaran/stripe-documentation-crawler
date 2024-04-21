htmlCollect tax in Australia | Stripe Documentation[Skip to content](#main-content)Australia[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Faustralia)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Faustralia)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[Asia Pacific](/docs/tax/supported-countries/asia-pacific)# Collect tax in Australia

Learn how to use Stripe Tax to calculate, collect, and report tax in Australia.In Australia, Stripe Tax supports calculation and collection of GST.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Australia. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

Remote sellers supplying goods or services in Australia must register if their taxable turnover from these transactions exceeded 75,000 AUD within the past 12-month period or will exceed this amount in the next 12 months.

These rules also apply to businesses supplying remote services such as digital content or low-value goods from outside Australia to customers who are residents of Australia and aren’t registered for GST. Sales to Australian GST-registered businesses that are subject to reverse charge don’t count towards the threshold. The registration threshold for non-resident non-profit organizations is 150,000 AUD.

Stripe doesn’t support the non-profit organization specific threshold.

Threshold: 75,000 AUD (or 150,000 AUD for non-profit organizations)

Time frame: Previous or current year.

Included transactions: Any taxable transactions that reverse charge doesn’t apply to.

## Register to collect tax

Find more information on how to register for GST in Australia on the government website:

- [Registration for businesses with an origin address in Australia](https://www.ato.gov.au/Business/GST/Registering-for-GST/)
- [Registration for remote sellers](https://www.ato.gov.au/Business/International-tax-for-business/Non-resident-businesses-and-GST/)(businesses based outside of Australia selling into Australia)

After you’ve registered to collect tax in Australia, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Australia.

Learn more about how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates GST for your transactions in Australia.

Generally, most transactions are taxable in the jurisdiction where your customer is. Stripe assumes the sale of most goods or services to be taxable unless specifically exempted.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes to Australia. Stripe doesn’t file taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`