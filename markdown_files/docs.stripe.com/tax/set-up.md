htmlSet up Stripe Tax | Stripe Documentation[Skip to content](#main-content)Set up[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fset-up)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fset-up)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Set up Stripe Tax

Enable Stripe Tax to automatically calculate and collect tax.NoteIf you’re a platform that wants to set up Stripe Tax for your connected accounts that are responsible for collecting, filing, and reporting taxes, see Tax for software platforms.

To set up Stripe Tax you need to configure your tax settings within the Dashboard and, depending on your integration, add one line of code.

1. [Confirm your origin address](#origin-address). Review and confirm that your details are correct.
2. [Select a preset tax code](#preset-tax-code). We use it to apply the correct tax rate.
3. [Select whether prices include tax](#default-tax-behavior)to have a tax behavior on every price for products.
4. [Add tax registrations](#add-registrations). Add an active tax registration when you’ve exceeded a tax threshold.
5. [Enable Tax in your Stripe integration or use the Stripe Tax API](#integrate)to start collecting tax.

NoteLog in or sign up for Stripe to activate Stripe Tax.

[Confirm your origin addressOptional](#origin-address)The origin address is where your business is located or, if you sell physical goods, the address where you’re shipping goods from. We use your Stripe business address here so you only need to review and confirm that your details are correct.

[Select a preset tax code](#preset-tax-code)- Preset product tax code: A product tax code is a classification of your product or service for Stripe Tax. We use this to make sure that the correct tax rate is applied to your transactions.

You must select the correct product tax code for your product or service. We use this if you don’t explicitly specify a tax_code, which maps to tax codes, on your products or in product_data on your transactions. Learn about products, prices, and tax codes.



- Default shipping tax code: A shipping tax code determines what type of tax treatment to apply when shipping (delivery) fees are added to the price that you charge. In some countries, the tax rate used to calculate the correct amount of tax on your product is the same rate that’s applied to the shipping fees. Some countries have a unique tax rate for shipping fees.

If you’re selling digital goods or services, or if you’re located in the EU, you don’t need to select anything. Otherwise, select the most appropriate tax treatment for your business. We use this if you don’t explicitly specify a tax code on a shipping rate.



[Select whether prices include tax](#default-tax-behavior)To calculate tax, you need to know the tax behavior of a price. The default tax behavior dictates that all prices for products have a tax behavior, in case it isn’t defined on the price itself.

You have three options:

- Exclusive: Tax is excluded from the price and is added on top of the price defined on the product.
- Inclusive: Tax is included in the price and already included in the price defined on the product.
- Automatic: Use currency to determine if tax is included or excluded. Stripe uses the currency of the price to define whether the tax is added on top of the price (excluded) or included in the price. Tax is excluded in USD and CAD, but included in all other currencies.

Learn about tax behavior for products and prices.

[Add registrations](#add-registrations)When your business exceeds a tax threshold (the sales volume or number of transactions where you’re required to start collecting tax), you have to register with the local tax authority before you can add tax to your transactions. If you have existing transactions on Stripe, you’ll see our monitoring tool which helps you understand where you might be registered or need to register.

You need to add any active tax registrations you have in tax settings within the Stripe Dashboard. You can either add a registration manually, or through the Monitor tax thresholds section. Additionally, you can schedule a registration to begin at a date in the future if you’re planning to register. Stripe Tax only calculates and collects tax on transactions in these locations.

We have more information on how to register in different markets. Check our guide.

[Enable Tax in your Stripe integration or use the Stripe Tax API](#integrate)The final step in setting up Stripe Tax is to enable automatic tax on your Stripe integration. Here’s how:

- No-code:If you’re using the Dashboard to create payments, Stripe Tax is enabled automatically unless you switch off the toggle at the bottom of the tax settings page. You can try it out by creating an[invoice](https://dashboard.stripe.com/invoices/create),[subscription](https://dashboard.stripe.com/subscriptions/create),[quote](https://dashboard.stripe.com/quotes/create), or[payment link](https://dashboard.stripe.com/payment-links/create)in the Dashboard.

![Stripe dashboard with the automatic tax toggle set to true](https://b.stripecdn.com/docs-statics-srv/assets/dashboard_automatic_tax.b264e5e6c6f5e836d044e5eee3a29a07.png)

- Low-code: If you’re using any low-code products that are currently integrated with Stripe Tax, you need to add automatic_tax[enabled]=true to each integration. Read our guides for more information:

  - [Invoicing](/tax/invoicing)
  - [Billing](/tax/subscriptions)
  - [Checkout](/tax/checkout)


- Custom flows: To use Tax with PaymentIntents, or to collect tax on payments received outside of Stripe, see our integration guide for Custom Payment Flows.



We also have integration builders for Checkout.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Confirm your origin address](#origin-address)[Select a preset tax code](#preset-tax-code)[Select whether prices include tax](#default-tax-behavior)[Add registrations](#add-registrations)[Enable Tax in your Stripe integration or use the Stripe Tax API](#integrate)Products Used[Tax](/tax)[Checkout](/payments/checkout)[Invoicing](/invoicing)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`