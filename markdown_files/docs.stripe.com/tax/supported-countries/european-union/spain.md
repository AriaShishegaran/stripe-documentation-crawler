htmlCollect tax in Spain | Stripe Documentation[Skip to content](#main-content)Spain[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Feuropean-union%2Fspain)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Feuropean-union%2Fspain)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)[European Union](/docs/tax/supported-countries/european-union)# Collect tax in Spain

Learn how to use Stripe Tax to calculate, collect, and report tax in Spain.Spain is part of the EU and applies the EU VAT rules. Read more about those rules on the European Union page. You can also read our guide to VAT.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Spain. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

You can read more about registration obligations in Spain on the European Union page or in our guide to VAT.

## Register to collect tax

Different registration schemes could apply to your business, depending on whether you’re based inside or outside the EU. After you’ve decided which registration scheme is correct for your business, learn how to register in Spain.

- [General information and domestic VAT registration](https://sede.agenciatributaria.gob.es/Sede/en_gb/iva.html)
- [One-Stop Shop registration schemes](https://sede.agenciatributaria.gob.es/Sede/en_gb/iva/iva-comercio-electronico/nuevos-regimenes-especiales-ventanilla-unica.html)

After you’ve registered to collect tax in Spain, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Spain.

Learn more about how to add your registration in the Dashboard.

## How we calculate taxes

Spain applies the EU VAT rules. Learn more about tax calculation in the European Union.

In Spain, there are some territories outside of the scope of the standard tax system and might have different rules that apply. Stripe won’t calculate tax for customers based there, even if you’ve added a registration for Spain. Learn more about how Stripe handles excluded territories. This applies to the following locations:

- Canary Islands
- Ceuta
- Melilla

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab in the Dashboard. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes to Spain. Stripe doesn’t file taxes on your behalf. For Europe, we recommend using our partners Taxually or Marosa, who can help manage your filing and remittance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Calculate, collect, and report tax in the European Union](/docs/tax/supported-countries/european-union)[Introduction to EU VAT and VAT One Stop Shop](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss)[Navigate the VAT registration process in Europe](https://stripe.com/guides/tax-registration-process-europe)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`