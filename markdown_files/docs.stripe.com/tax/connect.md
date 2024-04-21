htmlUse Stripe Tax with Connect | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fconnect)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fconnect)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Use Stripe Tax with Connect

Understand how Stripe Tax can help your platform and your connected accounts comply with tax obligations.Stripe Tax supports Connect by helping you calculate and collect taxes. It provides transactional reports to help with tax reporting and filing for your platform or your connected accounts.

## Who is liable?

The first step for using Stripe Tax with Connect requires you to determine which entity has the obligation to collect and report taxes. The entity that’s liable for tax might be you or your connected account, depending on your business model, regulations (for example, marketplace laws in the US and EU), or the transaction details, such as the order amount or the type of goods being sold.

Consult with a tax advisor who understands your business model to determine the tax obligations for both your platform and your connected accounts.

## Tax for software platforms (non-marketplaces)

SaaS platforms enable other businesses with software services to reach their customers. In these configurations, the connected accounts typically assume responsibility for collecting and remitting taxes. Stripe Tax supports the following charge types and integrations for platforms:

Charge typeLiable for tax?Support- [Direct charges](/connect/direct-charges)
- [Destination charges](/connect/destination-charges)
- [Destination charges with on_behalf_of](/connect/destination-charges#settlement-merchant)
- [Separate charges and transfers](/connect/separate-charges-and-transfers)
- [Separate charges and transfers with on_behalf_of](/connect/separate-charges-and-transfers#settlement-merchant)

Connected Account- Payment Intents (using the Stripe[Tax API](/tax/custom))
- [Checkout](/tax/checkout)
- [Billing](/tax/subscriptions)
- [Invoicing](/tax/invoicing)
- [Payment Links](/tax/paymentlinks)

- Off-Stripe payments

Connected Account- Stripe[Tax API](/tax/custom)

## Tax for marketplaces

Stripe Tax supports the following charges and integrations for marketplaces:

Charge typeLiable for tax?Support- [Direct charges](/connect/direct-charges)

Platform- Payment Intents (using the Stripe[Tax API](/tax/custom))

- [Destination charges](/connect/destination-charges)
- [Destination charges with on_behalf_of](/connect/destination-charges#settlement-merchant)
- [Separate charges and transfers](/connect/separate-charges-and-transfers)
- [Separate charges and transfers with on_behalf_of](/connect/separate-charges-and-transfers#settlement-merchant)

Platform- Payment Intents (using the Stripe[Tax API](/tax/custom))
- [Checkout](/tax/checkout)
- [Billing](/tax/subscriptions)
- [Invoicing](/tax/invoicing)
- [Payment Links](/tax/paymentlinks)

- Off-Stripe payments

Platform- Stripe[Tax API](/tax/custom)

## What is a marketplace?

Marketplaces connect buyers and sellers on a single platform, and are websites or apps where products are listed by multiple third-party vendors. In some jurisdictions, marketplaces might be responsible for tax collection on transactions that they facilitate. The terminology used by the local tax authorities to refer to marketplaces that are responsible for tax collection varies by jurisdiction. Some examples include:

JurisdictionNaming convention for marketplacesUSMarketplace facilitatorCanadaMultiple terms in use.Digital platform operator(divided intodistribution platform operatorsandaccommodation platform operators);online sales platforms;marketplace facilitators; etcAustraliaElectronic distribution platform(EDP)operatorsEUDeemed supplier(Intermediariesis used to refer to platforms that are not marketplaces)Stripe Connect’s distinction between platforms and marketplaces doesn’t strictly correspond to the tax definition of marketplaces. We recommend you consult with a tax advisor to confirm if your business qualifies as a marketplace for tax purposes.

## See also

- [Tax for platforms](/tax/tax-for-platforms)
- [Tax for marketplaces](/tax/tax-for-marketplaces)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Who is liable?](#who-is-liable)[Tax for software platforms (non-marketplaces)](#tax-for-software-platforms)[Tax for marketplaces](#tax-for-marketplaces)[What is a marketplace?](#what-is-a-marketplace)[See also](#see-also)Products Used[Tax](/tax)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`