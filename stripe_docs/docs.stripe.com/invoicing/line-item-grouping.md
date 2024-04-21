# Invoice summary itemsBeta

This guide describes how to use the underlying API (Invoice summary items) that enables the grouping of invoice line items. With the summary item feature, you can group invoice line items with the API.

If you want to categorize and display invoice line items dynamically, see Group invoice line items.

[Group invoice line items](/invoicing/group-line-items)

[privacy policy](https://stripe.com/privacy)

[Create summary items](#create-summary-items)

## Create summary items

For an existing draft invoice, create an invoice summary item as described below. The summary item represents a group that you can assign line items to, and the description field of the summary item renders as the group header for these line items.

By default, Stripe renders all the line items assigned to the summary item. You can also hide all line items assigned to the summary item and only display the group header by setting display_items=none as a parameter on the summary item. If you set display_items=none, it hides all line items assigned to the summary item. It is not possible to selectively hide some line items but not others, except for line items with a value of 0 USD (see Hide individual $0 line items section).

Instead of creating the summary items one-by-one, you can also bulk create with the create or update invoice endpoints. The example code below creates a draft invoice with two empty summary items

[create](/api/invoices/create)

[update](/api/invoices/update)

Remember to expand rendering.summary_items so you can see the list of summary items in the response.

[Assign summary item](#assign-summary-items)

## Assign summary item

Now that the invoice contains empty summary items (assuming that the invoice already contains line items), we can assign a summary item to the line item.

You can update the summary item that the line item belongs to, or un-group the line item by using the same endpoint.

[Update summary items](#update-summary-items)

## Update summary items

Using the update invoice endpoint, you can re-order, delete, or update the summary items. For example, in the code below, the order is reversed for the first and second summary item.

[update](/api/invoices/update)

To delete all existing summary items from an invoice, use the same endpoint to unset the rendering[summary_items_data] field like the following:

When you delete the summary items, all associated line items are no longer grouped.

Alternatively, you can delete a single summary item like the following:

[Hide individual $0 line items](#hide-line-items)

## Hide individual $0 line items

The API also supports hiding individual 0 USD line items. For a specific line item on the invoice, you can set rendering[display]=hidden_if_zero like the following:

Then, if the line item is 0 USD, it is automatically hidden anywhere the customer sees the invoice.
