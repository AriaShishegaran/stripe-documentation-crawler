# Invoices page

Invoices move through a series of statuses as they’re created and processed. You can track the status of an invoice on the Invoices page.

[invoice](/api/invoices)

[Invoices page](https://dashboard.stripe.com/invoices)

You can remove the header on the Invoices page by closing all of the items in the task list. After you remove the header, you can’t make it reappear.

Invoices in open status can display a different badge, such as Past due or Retrying. In some scenarios, you can hover over the badge to view an explanatory tooltip.

If an open non-subscription invoice is waiting for a payment that’s initiated but still pending, it shows the Pending badge in the list of invoices. However, its details page shows the Open badge.

Invoices page

## Filter invoices

On the Invoices page, you can filter the view using the buttons above the list. The Outstanding button shows invoices with open status. To further refine the list, click Filter. You can filter by frequency, status, creation date, due date, and so on.

You can also configure the information displayed in the Customer column. Click the gear icon next to that column’s heading and select the customer description, customer email, list of line items, or a metadata attribute.

Filter invoices

## Invoice actions

You see a Download PDF button when you hover over the overflow menu (). Depending on the invoice status, clicking the button downloads either a PDF of the invoice or a receipt. If the customer has paid the invoice, Stripe generates a PDF of the receipt. For all other statuses, Stripe generates a PDF of the invoice. The overflow menu also provides additional actions, which allow you to duplicate an invoice, delete a draft, or view the customer details associated with an invoice.

If you need the original invoice for a paid invoice, click through to the Invoice details page.

[Invoice details page](#invoice-details-page)

## Export invoices

You can export all of your invoices, or a subset of them (as a CSV file) by using the Export feature.

Export invoices

## Invoice details page

When you click an invoice on the Invoices page, its details page opens. If the invoice is in draft status and isn’t associated with a subscription, the edit invoice form opens automatically. You can perform a variety of actions on the details page, such as editing it, adding a note, resending it, or downloading a receipt. The available actions depend on the status of the invoice.

After Stripe finalizes an invoice, you can’t change its due date. If you need to change the due date, you must void (cancel) the original invoice and send a new one.

[void](/invoicing/overview#void)

Invoice details page

## Pending invoice items

You can see a customer’s pending invoice items by navigating to the Customers page, and clicking on their name. If the customer has a pending invoice item, it appears under Pending invoice items. An invoice item appears as pending if it’s not attached to any invoice.

[Customers page](https://dashboard.stripe.com/customers)

Under Pending invoice items, you can also choose to create a new invoice item, or instantly invoice everything listed. When you click Invoice now, a dialog appears that lets you select whether to charge the default source or email the invoice to the customer. Additionally, the dialog gives you the option to calculate tax automatically. To learn about how invoice items fit within a subscription, see Add invoice items to a draft subscription invoice.

[Add invoice items to a draft subscription invoice](/billing/invoices/subscription#adding-draft-invoice-items)

## See also

- Use the Dashboard

[Use the Dashboard](/invoicing/dashboard)

- Hosted Invoice Page

[Hosted Invoice Page](/invoicing/hosted-invoice-page)