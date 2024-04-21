htmlGroup invoice line items | Stripe Documentation[Skip to content](#main-content)Group invoice line items[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fgroup-line-items)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fgroup-line-items)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)# Group invoice line items

Dynamically filter and group invoice line items.To help your customers better understand your invoices (including PDFs, Hosted Invoice Page, and invoice emails), you can categorize and display invoice line items under different groups. You can also hide groups of line items. This is helpful if some line items are excessively detailed: you can configure it so that only their group-level subtotal is visible to your customers.

This guide describes how to organize one-time and subscription invoices by creating dynamic filters and groups in the Stripe Dashboard.

Dynamically group invoice line items with CEL expressions.

![Invoice PDF without summary items](https://b.stripecdn.com/docs-statics-srv/assets/summary-items-ungrouped.aebd6d3acceb95a1dcc27f4cb5f0e1ab.png)

Un-grouped line items

![Invoice PDF with summary items](https://b.stripecdn.com/docs-statics-srv/assets/summary-items-grouped.101c38cbe8b978d59a1eb9a59abe5005.png)

Grouped line items using summary items (collapsed “Red items” group)

## Before you begin

To use this feature, you define rules and templates with Common Expression Language (CEL) expressions. To learn more about CEL, read the introduction. This guide provides some examples in the invoice template context, but we recommend reading the official language definition on GitHub. You can also start with a common use case.

Only available with Billing ScaleInvoice line item grouping with CEL requires Billing Scale pricing.

### Limitations

This feature has some limitations:

- You can only apply CEL expressions to invoices created from the Dashboard.
- Each CEL expression has a maximum length of 1024 characters.
- A template has a maximum of 10 line item grouping policies.
- Each CEL expression has a expansion depth limit of 1. For example, we support`line_item.invoice_item.expand().description`but not`line_item.subscription.expand().default_payment_method.expand().type`.
- CEL expressions don’t support every field on the invoice line item object in the public API.
- CEL expressions use the[API Version](/upgrades)`2022-11-15`as its underlying resource. Later API versions and preview features are not supported automatically for the duration of the beta.

[Group invoice line items](#group-invoice-line-items)You can group invoice line items in the Dashboard. If you want to use the API, you can request early access to the beta in the API tab.

DashboardAPI### Create an invoice rendering template

1. Go toSettings > Invoice templatein the Stripe Dashboard.
2. In theTemplatessection, click+ Create template.
3. Name your template. You use the template name when you apply the template to a subscription or a one-time invoice.

### Add a policy to the template

After you create the template, add a line item grouping policy to it. You write these policies in CEL, which allows Stripe to dynamically filter and group line items.

Best practices![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When you create a template, keep in mind:

- The order of the policies matter. For example, if the first policy picks up all the line items that satisfy the filter condition, the second policy picks up all the remaining line items that aren’t yet in a group after the first policy.
- `expand()`is a Stripe-specific macro to expand fields on the API object. See the Stripe-specific CEL expression macros section.

Write a CEL expression![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Invoice template CEL expressions take an invoice line item object as the input. You can use any of that object’s fields in an expression. For example:

`line_item.field_name
line_item.description`You can expand ID fields that point to other Stripe objects, like a subscription or subscription_item, with the  expand() function. For example, to access a subscription’s metadata:

`line_item.subscription.expand().metadata`Common mistakeYou can only expand one level deep. For example, you can’t expand a subscription’s payment method and type fields. This is not currently supported: line_item.subscription.expand().default_payment_method.expand().type

Stripe-specific CEL expression macros![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

In addition to the list of standard CEL expression macros, we currently support these Stripe-specific functions:

- `expand()`: Expands publicly user expandable API fields. For example, in a CEL expression,`line_item.invoice_item`returns the invoice item ID. With`line_item.invoice_item.expand()`, it returns the full invoice item object.

Line item grouping fields![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

A line item grouping has three fields:

FieldTypeDescriptionGroup by

CEL Expression <line_item => string>

Controls the grouping of line items. It’s evaluated against each line item on the invoice that hasn’t been filtered out and returns a string. Line items with the same result string are grouped together under a summary item, where the result string becomes the description of the summary item.

For example, if you want to group together static line item names, like “PO Number”, the CEL expression would be PO Number.

If you want to dynamically group line items using “PO” from a line item’s metadata, the CEL expression would be:

`'PO Number' + line_item.invoice_item.expand().metadata['PO']`With this expression, a line item with metadata['PO'] = 123 evaluates to “PO Number: 123”. If multiple line items evaluate to the exact same string, they’re grouped together under a summary item where the description is “PO Number: 123”.

Filter by

CEL Expression <line_item => boolean>

Filters line items in a policy. This expression is evaluated against each invoice line item on the invoice. If a given invoice line item matches the filter, it’s added to the invoice line item group defined for this policy.

For example, if you want to group line items that have a PO number, use has(line_item.invoice_item.expand().metadata.PO). If the line item’s invoice item resource has a metadata field of PO, the expression returns true. Otherwise, it returns false.

Hide line itemsToggleControls whether to collapse or expand the summary items formed from an invoice line item grouping policy. Summary items are expanded by default.### Apply the invoice rendering template to a one-time invoice or subscription

To use the invoice line item grouping policy, apply the template to an invoice or a subscription.

Use the invoice editor in the Stripe Dashboard to apply invoice rendering templates to new and draft invoices.

Use the subscription editor in the Stripe Dashboard to apply the invoice rendering template to a subscription. All future invoices generated from that subscription use the invoice line item grouping policies of that rendering template. You can apply the template draft to subscription invoices. You can’t apply the template to finalized invoices.

Learn more about invoice transitions and finalization.

[Use cases](#use-cases)The following table provides some common examples of grouping policies.

Use caseDetails and exampleGroup by invoice line item metadata

You might have a sales-led process that ties different purchase order numbers to each of your invoice line items with a metadata named “PO”. In this example, the Group by field creates groups for each purchase order number and lists line items corresponding to that PO number from their metadata field.

Group by:

`'PO - ' + line_item.invoice_item.expand().metadata.purchase_order_number`Filter by:

`has(line_item.invoice_item.expand().metadata.purchase_order_number)`Group by price metadata

You might want to group invoice line items by the price metadata to organize the invoice by the type of price they have purchased. The invoice is sectioned off according to the section string you specify in the price metadata.

Group by:

`line_item.price.metadata.section`Filter by:

`has(line_item.price.metadata.section)`Group by prorations

You might have many proration line items in your subscription invoice and want to simplify your invoice for customers. This example groups line items that have a prorated amount larger than 0 EUR in a group called “Credits” and negative line items in a group called “Debits”.

Group by:

`'Proration ' + (line_item.amount > 0 ? 'Debits' : 'Credits')`Filter by:

`line_item.proration`Group line items by their description

All ungrouped line items are grouped under the Other section of a summary by default. If you want to list otherwise ungrouped line items by their description, you can expand the Other section under a summary. To prevent overriding any other grouping policy, make sure this is the last item in the policy list.

Group by:

`line_item.description`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Group invoice line items](#group-invoice-line-items)[Use cases](#use-cases)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`