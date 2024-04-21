htmlCalculate tax | Stripe Documentation[Skip to content](#main-content)Calculate tax[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fcalculating)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fcalculating)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Calculate tax

Learn how to calculate tax with Stripe Tax.The most common forms of indirect taxes for your business are sales tax, VAT, and GST. These taxes apply on the sale of physical goods, digital goods, and services.

Stripe calculates tax on a transaction taking into account some or all of the following factors:

- The location of the seller
- The location of the customer
- The type of the product sold
- Whether the transaction involves a[reverse charge](/tax/zero-tax#reverse-charges)
- The status of the customer (for example, whether they’re a VAT-registered business, private person or an exempt organization)

## How Stripe uses addresses

Stripe uses a single address as the customer’s location, or transaction destination, when calculating taxes. For more information, see which customer address we use.

In certain scenarios, it’s important to identify the origin of a transaction. Stripe generally uses the address where your business is located as the origin of a transaction. This address is defined as your origin address in the Dashboard or as head_office if using the tax settings object.

### How to use ship-from addresses Beta

You can add ship-from addresses that differ from your business address for tax calculation. To add them, use the ship_from_address transaction object. You can add ship-from locations only using the Stripe Tax API. They aren’t available in integrations of Stripe Tax with Payment Links, Checkout, or Billing and Invoicing. If you enter an unrecognized ship-from address, Stripe returns a shipping_address_invalid error.

Stripe Tax can designate only one address as the origin of a transaction even though in some countries the determination of origin can vary by product type. If you provide the ship-from address, Stripe Tax uses it to calculate tax for both services and physical goods. If you don’t provide a ship-from address, Stripe Tax assumes that the origin of the transaction is the address where your business is located. When selling a combination of products that require different origin locations, consider splitting the transaction accordingly.

If you’re interested in participating in this ship-from beta, send an email to: stripe-tax@stripe.com.

[Specify product tax codes and tax behaviorLearn how to set up products and prices to automatically calculate tax.](/tax/products-prices-tax-codes-tax-behavior)[Collect customer addressesLearn how to collect customer addresses to automatically calculate tax.](/tax/customer-locations)[Zero tax amounts and reverse chargesLearn about cases when Stripe calculates zero tax.](/tax/zero-tax)[Override tax behaviorBetaSet up Tax to fit your business needs with tax overrides.](/tax/tax-overrides)[Countries supported by Stripe TaxLearn how to use Stripe to calculate, collect, and report tax in different countries](/tax/supported-countries)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Related Guides[Calculate tax using APIs](/docs/tax/custom)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`