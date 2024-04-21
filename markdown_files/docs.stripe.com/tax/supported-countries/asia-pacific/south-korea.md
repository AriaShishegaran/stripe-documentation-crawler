htmlCollect tax in South Korea | Stripe Documentation[Skip to content](#main-content)South Korea[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Fsouth-korea)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fasia-pacific%2Fsouth-korea)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[Asia Pacific](/docs/tax/supported-countries/asia-pacific)# Collect tax in South Korea

Learn how to use Stripe Tax to calculate, collect, and report tax in South Korea.In South Korea, Stripe only supports collecting VAT for digital services. In Stripe, these are referred to as “digital products.” To collect this tax on Stripe, you must be a remote seller without a physical presence in the country.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in South Korea. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

Remote sellers providing digital goods or electronically supplied services (digital products) to consumers in South Korea must register for VAT purposes as from the first sale. There are no registration thresholds for non-resident service providers. Sales to business customers in South Korea do not trigger any tax registration obligations as remote sellers are not required to collect tax on such sales.

Threshold: 1 transaction

Included transactions: Business-to-consumer (B2C) sales of digital goods and services

## Register to collect tax

You must be a remote seller with no physical presence in South Korea to collect this tax on Stripe.

Find more information on how to register for VAT in South Korea on the government website.

After you’ve registered to collect tax in South Korea, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in South Korea.

Learn more about how to add your registration in the Dashboard.

## How we calculate taxes

We only support calculations for digital products (non-physical items or services that are delivered, given, or rendered electronically) in South Korea. Stripe doesn’t calculate tax for products that don’t use a digital product tax code.

View the list of supported digital product tax codes. To calculate taxes in South Korea, make sure that you assign a tax code to each of your products.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes to South Korea. Stripe doesn’t file taxes on your behalf.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`