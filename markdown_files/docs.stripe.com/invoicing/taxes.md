htmlTaxes | Stripe Documentation[Skip to content](#main-content)Taxes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)# Taxes

Learn about Stripe Tax and how to use it with invoices.On an invoice, Stripe Tax calculates sales tax, VAT, and GST. To calculate these for each line item, Stripe uses:

- Your[tax settings](https://dashboard.stripe.com/settings/tax)
- The customer’s tax settings and location
- The product tax code and price tax behavior

NoteLog in or sign up for Stripe to activate Stripe Tax.

## Set up the customer

We use the customer’s location to determine the relevant taxes to collect. Customers outside of the US need at least a country-level address, while customers in the US require a 5-digit postal code. For Canada, we need at least the province or postal code.

DashboardAPIYou can add customer location information in the Customer details page by clicking Edit next to Details. To add a customer’s location from the Invoice Editor, click the overflow menu () next to the customer. Select Edit customer information, click Add additional details, and scroll down to Billing details.

After you update the location, click Update customer. Stripe applies the new location to all of your customer’s future invoices unless you update it. For more information, see Determine customer locations.

## Set up line items

To calculate tax on each line item on an invoice, you need to set a tax behavior and optionally a tax code.

### Customize tax settings for one-off line items

Customize line items in the Invoice Editor by selecting the tax behavior from the Include tax in price drop-down menu.

![Customize tax settings for one-off line items](https://b.stripecdn.com/docs-statics-srv/assets/invoicing_price.faa90fb6b3cb833b900e06cb2187d339.png)

Customize tax settings for one-off line items

### Customize tax settings for product-based line items

You can use both the Dashboard and the API to customize tax settings for product-based line items.

DashboardAPIOn the Products page, you can select both the tax behavior for a particular price and the optional tax code for the product. The tax behavior is per price. You can’t change the tax behavior after you select it, but you can create new prices or archive old ones. To set up a tax behavior, click Add a price (or Add another price if you already have one) and select it from the Tax behavior drop-down menu.

To set up a tax code, select it from the Tax code drop-down menu when you create a new product or edit the details of an existing one.

![Customize tax settings for one-off line items](https://b.stripecdn.com/docs-statics-srv/assets/invoicing_new_price.517f186f27925e52e501019b9aecc94b.png)

Customize tax settings for one-off line items

## Enable automatic tax

After specifying a tax behavior and tax code, you can add the price to the customer as an invoice item:

Command Line[curl](#)`curl https://api.stripe.com/v1/invoiceitems \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer=cus_13729he8947269 \
  -d price=price_1K6mzG2eZvKYlo2CK7kcBICl`Set the toggle in the Invoice Editor. In the API, you need to pass the automatic_tax field to enable or disable automatic tax calculation. Both steps are required to start calculating tax automatically.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="cus_13729he8947269" \
  -d "automatic_tax[enabled]"="true"`To enable automatic tax calculation when you update an invoice, add the invoice parameter alongside automatic_tax:

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "invoice"="inv_12345" \
  -d "automatic_tax[enabled]"="true"`For more information on automatic tax calculation, see Automatically collect tax on invoices.

## Net prices and taxes

You can issue invoices with line item prices that exclude inclusive tax. Tax-exclusive prices are only shown in the invoice PDF. That means, when using inclusive tax, the Hosted Invoice Page and invoice emails show tax-inclusive prices. You can define the settings for net prices in the Dashboard or API.

- Include inclusive tax—The invoice PDF displays line item prices including the inclusive tax. (This is the default.)
- Exclude tax—The invoice PDF displays line item prices excluding tax.

Order precedenceIf you set a default for line item prices at the customer level, it takes precedence over account-level settings.

DashboardAPITo set a default for item prices, go to Default item prices in the Invoice template. Your chosen setting applies to all of the invoices you create through the Dashboard or API. For one-off invoices, use the Invoice Editor to set tax exclusivity. Go to Advanced options and choose to Include inclusive tax or Exclude tax. To learn more, see Create an invoice.

## See also

- [Determine customer locations](/tax/customer-locations)
- [Understand zero tax amounts](/tax/zero-tax)
- [Reporting and filing](/tax/reports)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up the customer](#set-up-customer)[Set up line items](#set-up-line-items)[Enable automatic tax](#enable)[Net prices and taxes](#net-price-taxes)[See also](#see-also)Products Used[Invoicing](/invoicing)[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`