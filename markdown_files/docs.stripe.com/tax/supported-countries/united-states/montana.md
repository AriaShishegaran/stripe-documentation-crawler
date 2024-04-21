htmlCollect tax from Montana | Stripe Documentation[Skip to content](#main-content)Montana[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Fmontana)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states%2Fmontana)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[United States](/docs/tax/supported-countries/united-states)# Collect tax from Montana

Learn how to use Stripe Tax to calculate, collect, and report tax from Montana.## When to register for tax collection

Montana doesn’t have a general state or local sales tax. This means you won’t see an option to add your registration for Montana to Stripe and collect taxes from your customers based in Montana.

However Montana does impose other taxes on businesses, including corporate income tax and a local resort tax. Learn more about the taxes that apply in Montana at the tax authority.

If you’re a business based in Montana you could still have tax obligations based on sales to customers in other locations. Use the Thresholds tab to get insights about your potential tax registration obligations. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

## Register to collect tax

Read more about registering for sales tax in the US in our guide. You may need to register to collect tax on your sales in other states or countries.

After you’ve registered to collect tax in a location, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in that location.

Learn how to add your registration in the Dashboard.

## How we calculate taxes

Stripe calculates the taxes that apply to your customer’s location.

## Report and file your taxes

Stripe provides reports of your completed tax transactions in locations where you have collected tax. To access these reports, navigate to the Registrations tab of the Dashboard and find the location you want to view your tax reports for. Learn more about the different types of reports.

You are responsible for filing and remitting your taxes. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Introduction to US sales tax and economic nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)[Navigate the sales tax registration process in the US](https://stripe.com/guides/sales-tax-registration-process-us)[How to file sales tax returns in the US](https://stripe.com/guides/how-to-file-sales-tax-us)[Collect tax in the United States using Stripe](/docs/tax/supported-countries/united-states)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`