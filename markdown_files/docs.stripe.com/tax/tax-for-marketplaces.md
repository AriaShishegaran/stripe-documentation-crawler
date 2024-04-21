htmlTax for marketplaces | Stripe Documentation[Skip to content](#main-content)Tax for marketplaces[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-for-marketplaces)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-for-marketplaces)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Tax for marketplaces

Learn about tax requirements for platforms and marketplaces, and how to enable Stripe Tax to collect tax on transactions when the Connect platform is liable.## Tax requirements for platforms and marketplaces

Many countries and US states require marketplace operators to collect sales tax and VAT on their facilitated sales. The US refers to these businesses as marketplace facilitators, while other regions, such as Europe, might refer to them deemed sellers.

As a marketplace operator, your tax collection requirements differ depending on the country or state. However, if your electronic interface enables transactions between buyers and sellers and you directly or indirectly collect customer payments, you might need to fulfill tax collection responsibilities.

If your businesses operates a marketplace or platform, you must first determine whether they qualify as a marketplace facilitator or a deemed seller, then make sure that they maintain tax compliance. If you’re unsure about your business’s tax requirements, consult a tax advisor.

If your business operates a marketplace and wants to collect tax on sales facilitated through this marketplace, refer to details below to enable Stripe Tax for marketplaces.

## Enable Stripe Tax for marketplaces

Stripe Tax enables businesses to calculate, collect, and file indirect taxes in over 40 countries, across hundreds of product categories.

Use this guide if your platform is responsible for collecting, filing, and reporting taxes.

NoteWe use the platform’s head office location, preset tax code, and tax registrations to calculate taxes. However, we don’t use the connected account information for tax purposes.

1. [Configure your platform account for tax collection](#set-up)
2. (Optional)[Assign tax codes to product catalog](#assign-product-tax-codes)
3. [Integrate tax calculation and collection](#enable-tax-collection)
4. [Withhold the collected tax amount](#tax-withholding)
5. [Access Stripe Tax reports](#access-reports)

[Configure your platform account for tax collection](#set-up)To collect taxes, you need the platform account’s tax settings and registrations.

### Use the Stripe Dashboard

### Use the Stripe API

[Assign tax codes to your product catalog](#assign-product-tax-codes)To calculate taxes, Stripe Tax requires that you classify products into tax codes. You can do so by supplying a preset tax code for the platform account, which might be sufficient if you typically sell a single category of items or services.

Additionally, you can map tax codes to each product to give you more control over tax categorization. You might have to map each product that a seller sets up on your marketplace. You can find a list of supported tax codes from available tax codes or retrieve it from the Stripe Tax Code API.

[Integrate tax calculation and collection](#enable-tax-collection)You need to integrate with Stripe Tax to estimate taxes as part of your checkout flow.

### Payment Links

### Payment Links for one-time payments

### Payment Links for subscriptions

### Checkout

### Checkout Sessions for one-time payments

### Checkout Sessions for subscriptions

### Billing

### Subscriptions

### Invoicing

### Custom flows using the Stripe Tax API

### Payment Intents

### Off-Stripe payments

After you implement it, Stripe automatically starts collecting tax in jurisdictions where you have an active registration.

CautionIndependent of the payment APIs, we credit the transaction amount to the connected account. You need to withhold the collected tax amount on the platform because the platform is liable for tax.

[Withhold collected tax amount](#tax-withholding)You must make sure that the tax collected is transferred to your marketplace account, so that you can then remit the tax to relevant jurisdictions.

### Checkout and Payment Links

### Invoicing

### Subscriptions

### Payment Intents with Stripe Tax API

[Access Stripe Tax Reports](#access-reports)### Use the Stripe Dashboard

### Use the Stripe API

## See also

- [Calculate tax in your custom checkout flow](/tax/custom)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Tax requirements for platforms and marketplaces](#tax-requirements-for-platforms-and-marketplaces)[Enable Stripe Tax for marketplaces](#enable-stripe-tax-for-marketplaces)[Configure your platform account for tax collection](#set-up)[Assign tax codes to your product catalog](#assign-product-tax-codes)[Integrate tax calculation and collection](#enable-tax-collection)[Withhold collected tax amount](#tax-withholding)[Access Stripe Tax Reports](#access-reports)[See also](#see-also)Products Used[Tax](/tax)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`