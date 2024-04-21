# Manage bulk invoice line itemsBeta

You can edit multiple line items on an invoice by bulk adding, updating, and removing line items with the Invoices API. You can also use the Invoice and Customer Uploader app to upload new Customers and Invoices from a CSV file.

[Invoices API](/api/invoices)

[Invoice and Customer Uploader app](https://marketplace.stripe.com/apps/invoice-uploader)

[privacy policy](https://stripe.com/privacy)

[Create invoice](#create-invoice)

## Create invoice

To update an invoice, you need to create one first. You can create an invoice in the Dashboard or with the Invoices API. You can only update invoices in a draft state.

[create an invoice in the Dashboard](/invoicing/dashboard#create-invoice)

[Invoices API](/api/invoices/create)

[draft state](/invoicing/overview#invoice-lifecycle)

[Add line items](#add-line-items)

## Add line items

To create multiple line items on the same invoice, reference the invoice ID. You can also assign a preexisting unassigned invoice item with the invoice item ID. Here’s how to create two new line items and assign an existing invoice item to this invoice.

[invoice ID](/api/invoices/object#invoice_object-)

[invoice item ID](/api/invoiceitems/object#invoiceitem_object-)

Ensure that you are using the invoice item ID, using a line item ID here will result in an error.

[Update line items](#update-lines)

## Update line items

From here, you can update multiple line items on the same invoice based on the invoice ID and line item IDs like the following:

The example above updates the description and metadata for line item 1, the price for line item 2, and whether it’s discountable for line item 3.

[Remove line items](#remove-lineitems)

## Remove line items

You can delete or unassign multiple line items on the same invoice by referencing the invoice ID and line item IDs and distinguishing between different removal types with the behavior key. Here’s how to permanently delete LINE_ITEM_1 and unassign LINE_ITEM_2. You can reassign LINE_ITEM_2 to another invoice in another request.

[Restrictions](#restrictions)

## Restrictions

There are some restrictions when using this feature

- The invoice must still be in a draft state

The invoice must still be in a draft state

- There are two types of invoice line itemstype: invoiceitem: Generated when an invoice item is added to an invoicetype: subscription: Automatically generated for a subscription invoice from each subscription item.After you sign up for early access and Stripe gates you into the feature, you can see the full list of available fields to update for each line item.While all fields are supported for invoiceitem line items, you can only update a small subset for subscription line items. Fields that are supported for subscription line items are tax_rates, or discounts.

There are two types of invoice line items

[types of invoice line items](/api/invoices/line_item#invoice_line_item_object-type)

- type: invoiceitem: Generated when an invoice item is added to an invoice

[invoice item](/api/invoiceitems)

- type: subscription: Automatically generated for a subscription invoice from each subscription item.

After you sign up for early access and Stripe gates you into the feature, you can see the full list of available fields to update for each line item.

While all fields are supported for invoiceitem line items, you can only update a small subset for subscription line items. Fields that are supported for subscription line items are tax_rates, or discounts.

- You can update a maximum of 50 line items in one API call. This limit is subject to change and might increase or decrease.

You can update a maximum of 50 line items in one API call. This limit is subject to change and might increase or decrease.

[Invoice metadata](#invoice-metadata)

## Invoice metadata

You can set invoice metadata in the same request for any of the above endpoints. Here’s an example calling update_lines.

[update_lines](/api/invoices)
