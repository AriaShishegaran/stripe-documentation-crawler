htmlNo-code quickstart guide | Stripe Documentation[Skip to content](#main-content)No-code quickstart guide[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fquickstart-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fquickstart-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)# No-code quickstart guide

Get started with Stripe Invoicing—no code required.Stripe Invoicing can help you get paid and save time using the Dashboard. Automatically charge your customer’s payment method on file, or email them the invoice with or without a link to a payment page. You can also send the invoice or payment page link manually.

NoteIf you’re interested in managing subscriptions and recurring revenue, see Subscriptions.

![Hosted Invoice Page](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page-guide.df3cc5a1e4180c338269aacdfa792180.png)

Hosted Invoice Page

![Invoice PDF](https://b.stripecdn.com/docs-statics-srv/assets/invoice-pdf-guide.d79c407ca08ee4b14dc0519fb3772309.png)

Invoice PDF

[Set up your business brandOptional](#establish-business)Before you start using Stripe Invoicing, help your future customers understand your products and terms of service by establishing your business and customizing how your brand appears.

![Brand your business](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page.79b4c18913fe9fb30f47ad8a5f062b6f.png)

Brand your business

[Choose your payment methodsOptional](#payment-methods)By default, customers can pay invoices with any of the payment methods that you enable in your Invoice template. If you’re a first-time user, Stripe automatically enables card, Link, bank transfers, Cash App Pay, and WeChat Pay payment methods. To enable additional payment methods, you need to activate them in your Payment methods settings.

In some situations, there might be restrictions that prevent payment methods from being used for an invoice. For instance, a payment method might only operate in one currency, or have limitations on the amount that can be paid. Stripe doesn’t automatically select a payment method when these limitations prevent it from being used. To learn more, see Payment methods.

![Choose additional payment methods](https://b.stripecdn.com/docs-statics-srv/assets/supported-payment-methods.194614192ca2c72656bc0587e8e21f46.png)

Choose additional payment methods

[How to get paid](#get-paid)You can create and send an invoice from the Dashboard. Invoices provide an itemized list of goods and services rendered, which includes the cost, quantity, and taxes. You can also use them as a tool to collect payment. Learn more about using the Dashboard.

![Create and send an invoice](https://b.stripecdn.com/docs-statics-srv/assets/create-send-invoices.985a3078348be3c2591f8d5e2d96e21c.png)

Create and send an invoice

[Set up a custom templateOptional](#custom-templates)You can use the Invoice template to customize ​​the content of your invoices. Set a default memo, footer, numbering scheme, and determine your default payment terms. Because you know more about your customers and your business than Stripe does, make sure your invoices include all of the required information. See the full invoice customization guide at Customize invoices.

![Configure the Invoice template](https://b.stripecdn.com/docs-statics-srv/assets/invoice-template.d50c4ba2210f06442b6adbb7279fe7a4.png)

Configure the Invoice template

![Manage tax information](https://b.stripecdn.com/docs-statics-srv/assets/manage-tax-information.3bbd3b8425726dc4ac243bb5bfd707a3.png)

Manage tax information

[Track an invoice](#track-invoice)Invoices move through different statuses from the time they’re created to when they’re paid. You can track the status of an invoice on the Invoices page. To let your customer know that the due date for an invoice is approaching, send them an email reminder. For more information on tracking your invoices, see Manage invoices.

![Track and manage your invoices](https://b.stripecdn.com/docs-statics-srv/assets/track-invoices.647ee840cc77e53c4d8537ec43ba9289.png)

Track and manage your invoices

[Explore advanced features with Invoicing PlusOptional](#invoicing-plus)Invoicing Plus includes advanced features to automate how you collect and reconcile invoice payments.

NoteAre you interested in automatic collection and reconciliation features? Upgrade to Invoicing Plus.

### Automate invoicing and get paid faster

You can automate Stripe Invoicing and get paid faster by choosing to automatically charge your customer’s payment method on file. If you’re a Plus user, let Stripe handle invoice recovery issues.

![Automate invoicing](https://b.stripecdn.com/docs-statics-srv/assets/advanced-invoicing-features.70dfe42ac952e7924876201c06e5902d.png)

Automate invoicing

### Close your books and account for revenue

Using automatic reconciliation means that you don’t need to expose your sensitive bank account details to users or manually reconcile open invoices with your bank. With auto-reconciliation for invoices, Stripe can:

- Match incoming payments with invoice amounts.
- Manage overpayment or underpayment, when the amount paid doesn’t match the invoice.
- Reduce the number of API calls required to transfer funds into Stripe.
- Manage payment retries on open invoices.

![Close your books](https://b.stripecdn.com/docs-statics-srv/assets/invoicing-auto-reconciliation.2d4b2648e4b67e8b2a2c7225a22bec69.png)

Close your books

[Let customers manage their invoicesOptional](#customer-portal)Share a link to your customer portal, where customers can log in with their email to manage invoices, view invoice history, update payment information, and so on. Learn how to create and share your customer portal link.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up your business brand](#establish-business)[Choose your payment methods](#payment-methods)[How to get paid](#get-paid)[Set up a custom template](#custom-templates)[Track an invoice](#track-invoice)[Explore advanced features with Invoicing Plus](#invoicing-plus)[Let customers manage their invoices](#customer-portal)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`