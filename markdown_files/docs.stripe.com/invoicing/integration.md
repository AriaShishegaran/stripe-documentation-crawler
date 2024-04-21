htmlIntegrate with the Invoicing API | Stripe Documentation[Skip to content](#main-content)Integrate with the API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fintegration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fintegration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)# Integrate with the Invoicing API

Learn how to create and send an invoice with code.The Dashboard is the most common way to create invoices. If you’d like to automate invoice creation, you can integrate with the API. Build a full, working Invoicing integration using our sample integration.

NoteYou don’t need to integrate with the Payments API to integrate with the Invoicing API.

[Set up Stripe](#setup)Use our official libraries for access to the Stripe API:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create a product](#create-product)To create a product, enter its name:

Command Line[curl](#)`curl https://api.stripe.com/v1/products \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d name="Gold Special"`[Create a price](#create-prices)Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the billing interval (when the price is for a subscription). Like products, if you only have a few prices, it’s preferable to manage them in the Dashboard. Use the unit amount to express prices in the lowest unit of the currency—in this case, cents (10 USD is 1,000 cents, so the unit amount is 1000).

NoteAs an alternative, if you don’t need to create a price for your product, you can use the amount parameter during invoice item creation.

To create a price and assign it to the product, pass the product ID, unit amount, and currency. In the following example, the price for the “Gold Special” product is 10 USD:

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d product={{PRODUCT_ID}} \
  -d unit_amount=1000 \
  -d currency=usd`[Create a customer](#create-customer-code)The Customer object represents the customer purchasing your product. It’s required for creating an invoice. To create a customer with a name, email, and description, add the following code replacing the values with your own:

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d name="Jenny Rosen" \
  --data-urlencode email="jenny.rosen@example.com" \
  -d description="My first customer"`After you create the customer, store the customer id in your database so that you can use it later. The next step, for example, uses the customer ID to create an invoice.

NoteSee Create a customer for additional parameters.

[Create an invoice](#create-invoice-code)Set the collection_method attribute to send_invoice. For Stripe to mark an invoice as past due, you must add the days_until_due parameter. When you send an invoice, Stripe emails the invoice to the customer with payment instructions.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d collection_method=send_invoice \
  -d days_until_due=30`Then, create an invoice item by passing in the customer id, product price, and invoice ID invoice.

The maximum number of invoice items is 250.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoiceitems \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d price={{PRICE_ID}} \
  -d invoice={{INVOICE_ID}}`If you set auto_advance to false, you can continue to modify the invoice until you finalize it. To finalize a draft invoice, use the Dashboard, send it to the customer, or pay it. You can also use the Finalize API:

NoteIf you created the invoice in error, void it. You can also mark an invoice as uncollectible.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/finalize \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Accept invoice payment](#accept-invoice-payment)Send an InvoiceStripe ElementsSend the invoice to the email address associated with the customer. As soon as the an invoice is sent, Stripe finalizes it. Many jurisdictions consider finalized invoices a legal document making certain fields unalterable. If you send invoices that have already been paid, there’s no reference to the payment in the email.

NoteWhen you send invoices that have already been paid, the email doesn’t reference the payment. Stripe sends invoices to the email address associated with the customer.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/send \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Handle post-payment events](#handle-payment-events)Stripe sends an invoice.paid event when an invoice payment completes. Listen for this event to ensure reliable fulfillment. If your integration relies on only a client-side callback, the customer could lose connection before the callback executes, which would result in the customer being charged without your server being notified. Setting up your integration to listen for asynchronous events is also what enables you to accept different types of payment methods with a single integration.

NoteSuccessful invoice payments trigger both an invoice.paid and invoice.payment_succeeded event. Both event types contain the same invoice data, so it’s only necessary to listen to one of them to be notified of successful invoice payments. The difference is that invoice.payment_succeeded events are sent for successful invoice payments, but aren’t sent when you mark an invoice as paid_out_of_band. invoice.paid events, on the other hand, are triggered for both successful payments and out of band payments. Because invoice.paid covers both scenarios, we typically recommend listening to invoice.paid rather than invoice.payment_succeeded.

Use the Dashboard webhook tool or follow the webhook quickstart to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

In addition to handling the invoice.paid event, we recommend handling two other events when collecting payments with the Payment Element:

EventDescriptionAction[payment_intent.processing](/api/events/types?lang=php#event_types-payment_intent.processing)Sent when a customer successfully initiated a payment, but the payment has yet to complete. This event is most commonly sent when a bank debit is initiated. It’s followed by either a`invoice.paid`or`invoice.payment_failed`event in the future.Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.[invoice.payment_failed](/api/events/types?lang=php#event_types-payment_intent.payment_failed)Sent when a customer attempted a payment on an invoice, but the payment failed.If a payment transitioned from`processing`to`payment_failed`, offer the customer another attempt to pay.[OptionalCustomize an invoice](#customize-invoices)## See also

- [Post-finalization](/invoicing/integration/workflow-transitions#post-finalized)
- [Use incoming webhooks to get real-time updates](/webhooks)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).[Code quickstart](/docs/invoicing/integration/quickstart)On this page[Set up Stripe](#setup)[Create a product](#create-product)[Create a price](#create-prices)[Create a customer](#create-customer-code)[Create an invoice](#create-invoice-code)[Accept invoice payment](#accept-invoice-payment)[Handle post-payment events](#handle-payment-events)[See also](#see-also)Related Guides[How Invoicing Works](/docs/invoicing/overview)[Invoicing API](/docs/api/invoices)[Hosted Invoice Page](/docs/invoicing/hosted-invoice-page)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`