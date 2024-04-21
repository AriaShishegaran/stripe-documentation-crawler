htmlCreate and send a quote | Stripe Documentation[Skip to content](#main-content)Create a quote[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fquotes%2Fcreate)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fquotes%2Fcreate)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Quotes](/docs/quotes)# Create and send a quote

Learn how to create, send, and accept a quote.NoteYou can use quotes in test mode, but you must upgrade to Invoicing Plus or Billing Scale to unlock full functionality in live mode. See which plan is right for you.

DashboardAPIA quote is a way to show prospective or existing customers the costs for a set of products and services. Quotes show the cost of either a one-off invoice or subscription. When a customer accepts the quote, ​​Stripe automatically creates all relevant invoices and subscriptions. ​​Many sales workflows use this common tool.

[Create a quote](#create-quote-dashboard)To create a quote in the Stripe Dashboard:

1. Go to the[Billing tab](https://dashboard.stripe.com/billing).
2. ClickQuick actions>Create quote(or go directly to the[quote editor](https://dashboard.stripe.com/test/quotes/create)).
3. Select+ Add new customer. At a minimum, enter your customer’sNameandAccount email. ClickAdd customer.
4. UnderItems, add or select a product. (You can also add a coupon.)
5. Choose an expiration date.
6. OptionalWrite a memo, and add a custom header and footer. You can set the future default text for the header and footer in the[quote template](https://dashboard.stripe.com/settings/billing/quote).
7. To preview the quote PDF (which shows the generated quote number) clickDownload preview.
8. ClickFinalize quote.

![Quote editor](https://b.stripecdn.com/docs-statics-srv/assets/create-quote-editor.b0567a67946f35c4844e0979f2bc7019.png)

Quote editor

After you finalize the quote, send it to your customer:

1. To download the quote, go toQuotes details page>Quote PDF.
2. Use an external email address to send the PDF to your customer for review.

[Mark a quote as accepted](#accept-quote-dashboard)After your customer accepts the quote, bill them by converting the quote into an invoice or subscription.

You can only create one-off invoices if a quote only has one-time prices.

If a quote has at least one recurring price, you can only convert it to a subscription.

### Convert a quote to an invoice

1. To mark a quote as accepted and create a draft invoice, go to Convert to invoice > Quotes details.


2. Use the invoice editor to modify the draft invoice as needed.


3. Email the invoice or automatically charge the customer.



### Convert a quote to a subscription

1. In the quote editor, choose a customer and create or select a product with a recurring price.


2. Enter the quote details and choose to either Start the subscription immediately or Schedule a subscription start date.


3. Finalize the quote. This marks the quote as Accepted.


4. Go to Convert to subscription > Quotes details.


5. Enter or modify the subscription details, then click Create subscription.



If you schedule the subscription to start immediately, Stripe creates an active subscription along with a draft invoice for the initial payment. Stripe finalizes the draft invoice automatically in one hour. Otherwise, the subscription begins on the scheduled start date. Depending on the subscription’s payment terms, Stripe collects payment by either charging the customer’s payment method on file or sending them an invoice.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a quote](#create-quote-dashboard)[Mark a quote as accepted](#accept-quote-dashboard)Products Used[Billing](/billing)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`