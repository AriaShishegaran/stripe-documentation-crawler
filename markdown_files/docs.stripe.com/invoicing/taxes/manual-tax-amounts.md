htmlUse tax amounts calculated outside of Stripe with Stripe Billing | Stripe Documentation[Skip to content](#main-content)Manual tax amounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes%2Fmanual-tax-amounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Ftaxes%2Fmanual-tax-amounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Taxes](/docs/invoicing/taxes)# Use tax amounts calculated outside of Stripe with Stripe Billing

Use taxes calculated from an external system with Stripe Invoices.To accommodate a wide range of billing scenarios, Stripe allows tax amounts to be set directly on invoices, which helps you to integrate with other tax calculation systems (such as a third-party tax tool such as Avalara or your own tax engine). This guide goes through various billing scenarios to show how to use the tax_amounts field.

## Create an invoice with manual tax amounts

This section describes adding manual tax amounts to invoice line items.

### Create an invoice with an invoice item

The first step is to create an invoice. We assume you already have a customer created, but if you don’t, please reference the customers guide.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}}`Manual tax amounts can only be added to invoice line items, so add an invoice item to the invoice.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoiceitems \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d invoice={{INVOICE_ID}} \
  -d amount=100 \
  -d currency=usd`### Update the invoice line item with tax_amounts

The update invoice line item endpoint accepts the tax_amounts parameter. This field gives merchants the ability to directly set the tax amounts on invoice line items. The field also requires tax rate data to make sure relevant information is displayed to the customer. The example below updates an invoice line item with the tax_amounts field.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/lines/il_0O4tNe589O8KAxCGYD7OyXPP \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "tax_amounts[0][amount]"=10 \
  -d "tax_amounts[0][taxable_amount]"=100 \
  -d "tax_amounts[0][tax_rate_data][percentage]"=10 \
  -d "tax_amounts[0][tax_rate_data][inclusive]"=false \
  -d "tax_amounts[0][tax_rate_data][tax_type]"=sales_tax \
  -d "tax_amounts[0][tax_rate_data][display_name]"="Sales Tax" \
  -d "tax_amounts[0][tax_rate_data][description]"="Texas Sales Tax" \
  -d "tax_amounts[0][tax_rate_data][jurisdiction]"=Texas \
  -d "tax_amounts[0][tax_rate_data][country]"=US \
  -d "tax_amounts[0][tax_rate_data][state]"=TX`All of the fields under tax_amounts are required except for description, jurisdiction, country, state, and tax_type. The invoice line item object returns a tax_amounts field.

`{
  id: "il_0O4tNe589O8KAxCGYD7OyXPP",
  object: "line_item",
  amount: 100,
  amount_excluding_tax: 100,
  currency: "usd",
  ...
  tax_amounts: [
    {
      amount: 10,
      inclusive: false,
      tax_rate: "txr_0Ns7kW589O8KAxCGXoi7EAuS",
      taxability_reason: null,
      taxable_amount: 100
    }
  ],
  tax_rates: [],
  ...
}`NoteStripe automatically creates or reuses an existing tax rate based on tax_rate_data. However, Stripe calculates tax amounts on the invoice based only on the amount parameter. Other values, such as tax rate, are only used for rendering purposes to be shown on the invoice. No validations are run on these fields to make sure they’re consistent with the tax amounts specified.

### Finalize the invoice

After all of the invoice line items are updated with tax amounts, you need to finalize the invoice. Tax amounts can’t change after the invoice is finalized. Refer to the edit invoice guide if you need to modify the invoice after finalization.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/finalize \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`## Stripe automatically creates tax-rates

For manual tax amounts, Stripe requires information about the corresponding tax rate. The tax rate is only used to display information to customers. It isn’t used in any calculations.

Stripe automatically creates tax rate objects in the background based on tax_rate_data. If the same tax rate data is passed in multiple times, Stripe references the existing tax rate object instead of creating another one. The following fields are used to deduplicate the tax rate: percentage, inclusive, display_name, jurisdiction, country, state, and tax_type. In this example, assume a second invoice line item was updated on the invoice from the previous section with the same tax_rate_data.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/lines/il_0P6nbg589O8KAxCGRWBJAdNV \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "tax_amounts[0][amount]"=50 \
  -d "tax_amounts[0][taxable_amount]"=500 \
  -d "tax_amounts[0][tax_rate_data][percentage]"=10 \
  -d "tax_amounts[0][tax_rate_data][inclusive]"=false \
  -d "tax_amounts[0][tax_rate_data][tax_type]"=sales_tax \
  -d "tax_amounts[0][tax_rate_data][display_name]"="Sales Tax" \
  -d "tax_amounts[0][tax_rate_data][description]"="Texas Sales Tax" \
  -d "tax_amounts[0][tax_rate_data][jurisdiction]"=Texas \
  -d "tax_amounts[0][tax_rate_data][country]"=US \
  -d "tax_amounts[0][tax_rate_data][state]"=TX``{
  id: "il_0P6nbg589O8KAxCGRWBJAdNV",
  object: "line_item",
  amount: 100,
  amount_excluding_tax: 100,
  currency: "usd",
  ...
  tax_amounts: [
    {
      amount: 10,
      inclusive: false,
      tax_rate: "txr_0Ny6QR589O8KAxCGo6MKGPxM",
      taxability_reason: null,
      taxable_amount: 100
    }
  ],
  tax_rates: [],
  ...
}`Both invoice line items have the same tax_rate ID under the tax_amount. Stripe handles the tax rate creation and deduplication to minimize the burden on merchants. While the tax_rate ID maps to a valid tax rate object, the IDs mapped to automatically created tax rates can’t be passed into the tax_rates field on the API. The only exception to that rule is the create credit notes endpoint.

## Issue a credit note

Credit notes allow for adjustments on invoices without needing to void an invoice. When issuing a credit note for an invoice line item with manual tax amounts, the API requires additional information to accurately create it.

### Create credit note

The create credit note endpoint also accepts the tax_amounts parameter. The field is required when the corresponding invoice line item has manual tax amounts. This ensures accurate accounting of the credit note and maintains consistency with your invoices.

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d reason=duplicate \
  -d "lines[0][type]"=invoice_line_item \
  -d "lines[0][invoice_line_item]"=il_0O4tNe589O8KAxCGYD7OyXPP \
  -d "lines[0][tax_amounts][0][amount]"=10 \
  -d "lines[0][tax_amounts][0][taxable_amount]"=100 \
  -d "lines[0][tax_amounts][0][tax_rate]"=txr_0Ns7kW589O8KAxCGXoi7EAuS`## Limitations

Keep in mind the following constraints when working with manual tax amounts.

### Invoice items don’t have tax amounts

Manual tax amounts can only be added to invoice line items.

### taxable_amount and tax_rates are not validated

The taxable amount and tax rate data passed in the request are only used for rendering purposes. They’re not validated against the tax amount in the request.

### Can’t mix tax_amounts and tax_rates

An invoice line item can’t have manual tax amounts if it also has a tax rate, and vice versa. Invoice line items also can’t have manual tax amounts if the invoice has a default tax rate or if any of the other invoice line items on the invoice has a tax rate.

### tax_amounts can grow stale when updating other fields

Existing manual tax amounts persist on the invoice line item unless directly edited. This can lead to stale tax amounts when updating the invoice item with fields relating to its amount, such as amount, discounts, or price.

### Automatically created tax rates can’t be directly used

Stripe automatically creates tax rate objects for manual tax amounts. These tax rates can’t be directly referenced on invoice or payment-related endpoints, except the credit note endpoint. They also can’t be directly updated and won’t be included on the all tax rates endpoint. However, the tax rate’s data is accessible by calling the retrieve tax rate endpoint with its token.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create an invoice with manual tax amounts](#create-invoice-with-manual-tax-amounts)[Stripe automatically creates tax-rates](#stripe-creates-tax-rates)[Issue a credit note](#issue-credit-note)[Limitations](#limitations)Related Guides[Collect taxes automatically with Stripe Tax](/docs/tax)[Collect taxes with manual tax rates](/docs/billing/taxes/tax-rates)Products Used[Invoicing](/invoicing)[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`