htmlTax rates and IDs | Stripe Documentation[Skip to content](#main-content)Tax rates and IDs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes%2Ftax-rates)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes%2Ftax-rates)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Taxes](/docs/invoicing/taxes)# Tax rates and IDs

Assign tax rates to draft invoices for automatic tax calculation.If you’re looking for automated tax calculation where you don’t need to define the rates, use Stripe Tax.

After you create a tax rate, you can assign it:

- On individual[invoice](/api/invoices)items.
- On the entire subtotal of the invoice.

NoteStripe recommends that you assign a tax rate on individual invoice items.

## Set tax rates on individual items

You can set tax rates on individual items using the Dashboard or API. You can add up to five tax rates to each line item.

DashboardAPIIf you’re creating an invoice through the Dashboard, assign tax rates to individual line items.

## Set default tax rates for the entire invoice

If you sell one type of product, or have simple tax needs, you can set a default tax rate on the invoice. Default tax rates apply to all invoice line items. For more complex use cases, you can also set an item-level tax rate that overrides the default tax rate. You can add up to five default tax rates to each invoice.

DashboardAPIIf you’re creating an invoice through the Dashboard, you can assign a default tax rate after you add an item.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set tax rates on individual items](#setting-tax-rates-on-individual-items)[Set default tax rates for the entire invoice](#setting-default-tax-rates)Products Used[Invoicing](/invoicing)[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`