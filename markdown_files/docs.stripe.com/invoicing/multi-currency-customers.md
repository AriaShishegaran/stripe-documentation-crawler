htmlMulti-currency customers | Stripe Documentation[Skip to content](#main-content)Multi-currency customers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fmulti-currency-customers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fmulti-currency-customers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Global invoicing](/docs/invoicing/global-invoicing)# Multi-currency customers

Change the billable currency for any customer to accept multiple currencies.Are you looking for a way to sell in multiple currencies, but each individual customer uses a single currency? Check out multi-currency Prices.

Use the Invoicing API to issue an invoice to a customer in a different currency. With the multi-currency customers feature, you can bill the same Customer using a different currency than what’s set as their default currency, and change the currency for a customer’s subscriptions. You can’t have two active subscriptions with different currencies.

This guide also explains how to create a credit note and inspect a customer’s credit balance in all assigned currencies. For illustrative purposes, we use the Canadian Dollar (CAD).

[Create an invoice](#create-invoice-code)Before you invoice a customer, create an invoice item by passing in the customer id, amount, and currency. Only add invoice items to a single customer at a time to avoid adding them to the wrong one.

The maximum number of invoice items is 250. Creating an invoice adds up to 250 pending invoice items with the remainder to be added on the next invoice. To see your customer’s pending invoice items, see the Customer details page or set the pending attribute to true when you use the API to list all of the invoice items.

NoteA CAD invoice doesn’t apply a customer credit balance denominated in USD or any other currency other than CAD. Additionally, any amount-off coupons you applied to the customer that are denominated in non-CAD currency are ignored.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoiceitems \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d amount=1000 \
  -d currency=cad`You must pass in the currency parameter when you issue a multi-currency invoice. The currency parameter dictates which invoice items get pulled into the invoice. For example, if you were to create two invoice items—one in USD and the other in CAD—for the same customer, setting the currency to CAD would only pull in the CAD invoice item (ignoring the USD invoice item).

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d collection_method=send_invoice \
  -d days_until_due=30 \
  -d pending_invoice_items_behavior=include \
  -d currency=cad`[Create a credit note](#create-credit-note)If there’s an issue with the invoice, you can create a credit note. If you need to apply the credit to the customer’s credit balance (as opposed to back to the original payment method), Stripe allocates the credit amount to the CAD-specific credit balance.

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d reason=duplicate \
  -d amount=1000 \
  -d credit_amount=1000`[Inspect the credit balance](#inspect-credit-balance)To see how much credit a customer has in each currency, use the invoice_credit_balance parameter:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=invoice_credit_balance`The customer’s credit balance is drawn down from the next CAD invoice created for this customer. It won’t, however, be drawn down for invoices created in different currencies.

## See also

- [Integrate with the Invoicing API](/invoicing/integration)
- [Manage customers](/invoicing/customer)
- [Products and prices](/invoicing/products-prices)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create an invoice](#create-invoice-code)[Create a credit note](#create-credit-note)[Inspect the credit balance](#inspect-credit-balance)[See also](#see-also)Products Used[Invoicing](/invoicing)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`