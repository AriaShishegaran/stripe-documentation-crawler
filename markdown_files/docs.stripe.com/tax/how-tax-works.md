htmlHow Tax works | Stripe Documentation[Skip to content](#main-content)How Tax works[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fhow-tax-works)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fhow-tax-works)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# How Tax works

Learn how Stripe Tax helps you automate tax compliance.To be tax compliant, you need to:

1. Understand which locations require you to collect tax
2. Register for tax in those locations
3. Calculate and collect tax
4. Report, file, and remit the tax you collected

# Introduction to indirect taxes with Stripe Tax

Each country handles tax on sold products and services differently, often calling it by a different name. In the US, businesses deal with sales tax. Throughout Europe, it’s called value-added tax (VAT). Canada and most countries in the Asia Pacific region refer to it as goods and services tax (GST).

Taxability and tax rates vary by location and category of products you’re selling. For example, children’s footwear is zero rated in Ireland, but adult footwear isn’t. Digital services are usually taxed at the standard rate in most EU countries. However, e-books are subject to the reduced rate.

Stripe Tax uses your business address, tax registrations, product tax codes, customers’ locations, and customer status to determine the correct tax rates for products you sell, in all supported locations. Read more about tax codes and how we calculate for different jurisdictions.

# Monitor your obligations and register

You need to identify the locations where you have sales tax, VAT, or GST obligations and need to register to collect tax. If you sell into multiple locations, you need to be familiar with the tax laws in those locations because the place where your transaction takes place determines where you’re required to collect tax. This can be the seller’s country, the buyer’s country, or another location.

As your business grows and you sell to more locations, you need to register to collect tax in more locations. Stripe Tax tracks your Stripe transactions and helps you monitor your tax obligations. Read more about tax obligation monitoring.

You must register with the tax authority in a location to collect taxes there. In some countries and states you have to register before your first transaction, while others have a registration threshold (such as the number of sales or sales volume). Take a look at the locations Stripe Tax supports along with the different tax thresholds that apply and links to the tax authority websites.

Stripe Tax tracks your registrations and uses them to calculate and collect taxes. Read more about adding your registrations to Stripe.

After you have registered to collect tax with a tax authority add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions.

# Calculate and collect

After you set up Stripe Tax in the Dashboard, Stripe automatically calculates and collects taxes on your transactions. Alternatively you can use Stripe Tax API to calculate taxes on your own custom payment flows. In either case, to determine which taxes to collect, you or your customers have to provide customer location information. Read more about how Stripe calculates tax.

If you sell to other businesses, your transactions might be subject to reverse charges. This means that the tax liability shifts to the customer and we don’t charge tax on the transaction. Stripe Tax uses customer tax identification numbers to determine whether a transaction is B2B. Adding a tax identification number to the customer might affect the tax calculation result. Stripe Tax doesn’t validate whether the provided tax identification number exists or is valid. Read about supported tax ID formats.

Some individuals or entities might be tax exempt. For example, some US states have a reseller exemption. You can set an exempt status on customers to reflect this. Read more about reverse charges and exempt customers.

# Report, file, and remit

If you’re collecting taxes, you must report, file, and remit (transfer) the taxes collected in every location that you’re registered in. Make sure you understand and comply with obligations of each state or country and consult your tax advisor if you need help. Stripe Tax supports exporting your transactions in an itemized format to aid with tax reporting. Read more about Stripe Tax reports.

Stripe Tax doesn’t currently file or remit taxes on your behalf. Submitting tax returns is key to your tax compliance. You can use TaxJar’s AutoFile solution for filing in the US. In Europe, we recommend Taxually or Marosa. To get started, visit Taxually’s partner page or Marosa’s partner page

Would you like Stripe to file taxes on your behalf?Enter your email address below if you're interested in being an early participant in the upcoming Stripe Tax Filing beta.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Frequently asked questions](/tax/faq)
- [Stripe Tax guides](https://stripe.com/guides/tax-guides)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`