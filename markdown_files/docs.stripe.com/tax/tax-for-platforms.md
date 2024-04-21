htmlTax for software platforms | Stripe Documentation[Skip to content](#main-content)Tax for software platforms[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-for-platforms)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-for-platforms)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Tax for software platforms

Learn how to enable Stripe Tax for your connected accounts, and collect tax when the connected account is liable for paying the tax.Stripe Tax enables businesses to calculate, collect, and report indirect taxes in over 40 countries, across hundreds of product categories. As a platform, you can use Stripe tax to offer pre-integrated tax compliance to your connected accounts.

Use this guide if your connected accounts are responsible for collecting, filing, and reporting taxes.

1. [Set up your connected accounts for tax](#check-set-up)
2. (Optional)[Assign tax codes to the product catalog](#assign-product-tax-codes)
3. [Integrate tax calculation and collection](#enable-tax-collection)
4. [Access Stripe Tax Reports](#access-reports)

[Set up your connected accounts for tax](#set-up)As a platform, you must make sure that a connected account has their tax settings and registrations set up before enabling tax calculations. This can be achieved by:

### Connected account using the Stripe Dashboard

### Creating a tax interface within your platform

### Use Connect embedded components for tax compliance

Your platform must then check whether connected accounts have configured Stripe Tax to enable tax calculations.

### Use the Stripe Dashboard

### Use the Stripe API

[Assign tax codes to the product catalogOptional](#assign-product-tax-codes)To calculate taxes, Stripe Tax requires classifying products into their tax codes. One way to do this is to supply a preset tax code for each connected account, which is probably sufficient if your connected accounts typically sell a single category of items.

However, you might offer your users more control by allowing them to map Tax Codes to each product. You can retrieve a list of supported Product Tax codes from the Stripe Tax Code API. You can also allow a subset of this list if your connected accounts only sell specific types of products.

![](https://b.stripecdn.com/docs-statics-srv/assets/dashboard_product.58429cc20faec07b5fce812d3838d85a.png)

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

After you implement it, Stripe automatically starts collecting tax in jurisdictions where the user has an active registration.

NoteIndependent of the integration, your connected account receives a credit for the collected tax amount by default.

[Access Stripe Tax Reports](#access-reports)Your connected accounts can use Stripe Tax reports to help them correctly file and remit tax.

### Connected account use the Stripe Dashboard

### Use the Stripe API

## See also

- [Calculate tax in your custom checkout flow](/tax/custom)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up your connected accounts for tax](#set-up)[Assign tax codes to the product catalog](#assign-product-tax-codes)[Integrate tax calculation and collection](#enable-tax-collection)[Access Stripe Tax Reports](#access-reports)[See also](#see-also)Products Used[Tax](/tax)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`