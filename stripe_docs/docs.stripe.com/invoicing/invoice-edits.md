# Edit invoices

You can’t revise invoices that are attached to subscriptions after finalization. For these types of invoices, the Edit invoice button is disabled.

[subscriptions](/billing/subscriptions/creating)

Stripe lets you revise a finalized invoice in open or uncollectible status. You can’t, however, revise an invoice in void or paid status. You might want to revise an invoice if you need to:

- Edit the invoice description.

- Edit the customer to update contact information.

- Add, remove, or edit a line item.

- Add a discount or apply taxes.

You can also customize invoices if you need to change their content or branding.

[customize invoices](/invoicing/customize)

The invoice compliance process can vary across countries. For example, if you’re based in the European Union, you might want to void an invoice and issue a credit note instead of revising the original invoice. Learn how to set up invoices in Europe using our best practices guide. Stripe recommends that you consult with your legal counsel for advice specific to your business.

[best practices guide](/invoicing/global-config-guide)

You can use the Dashboard to revise invoices after finalization. Learn how to revise an invoice and notify your customer, update their email address, change the payment collection method, and so on.

[Dashboard](https://dashboard.stripe.com/test/dashboard)

[Revise an invoice and notify your customer](#revision-notification)

## Revise an invoice and notify your customer

To revise an invoice and notify your customer, complete the following steps:

- Go to the Invoice details page and click Edit invoice. This opens up the Invoice Editor and creates a new draft invoice. (If you stop in the middle of a revision, you can come back later to continue editing the draft.) You’ll see a notice at the top of the editor that references the last sent invoice.NoteYou can also go to the Invoices page, click the overflow menu (), then Edit invoice.

Go to the Invoice details page and click Edit invoice. This opens up the Invoice Editor and creates a new draft invoice. (If you stop in the middle of a revision, you can come back later to continue editing the draft.) You’ll see a notice at the top of the editor that references the last sent invoice.

You can also go to the Invoices page, click the overflow menu (), then Edit invoice.

[Invoices page](https://dashboard.stripe.com/test/invoices)

- In the editor, update the field you want to revise. While all of the invoice fields are revisable, you can’t switch the customer or modify the product.

In the editor, update the field you want to revise. While all of the invoice fields are revisable, you can’t switch the customer or modify the product.

- Click Review invoice, and decide whether you want to notify the customer by email.Notify your customer about an updated invoice

Click Review invoice, and decide whether you want to notify the customer by email.

Notify your customer about an updated invoice

- When you click Update invoice, Stripe finalizes the new invoice and voids the old one. The editor closes and redirects you to the details page for the new invoice. The embedded timeline shows all of your revisions.

When you click Update invoice, Stripe finalizes the new invoice and voids the old one. The editor closes and redirects you to the details page for the new invoice. The embedded timeline shows all of your revisions.

In the Invoice details page, navigate down to the History section to see old and new invoices. When you click an invoice that Stripe voided due to a revision, you’re directed to its details page where you can see the revision timeline.

See an invoice’s revision history

[Change your customer's email address](#update-customer-email)

## Change your customer's email address

If you want to update the email address associated with an invoice:

- Click the Edit button () under Customer in the editor.

Click the Edit button () under Customer in the editor.

- Change the email address using the Email field. Previous recipients can still access this invoice through any of the older invoice emails. You can also use the Update customer dialog to change your customer’s email address.Update your customer’s email address

Change the email address using the Email field. Previous recipients can still access this invoice through any of the older invoice emails. You can also use the Update customer dialog to change your customer’s email address.

Update your customer’s email address

- Click Review invoice, followed by Update invoice. The Update invoice dialog displays all of the email addresses associated with the previous invoice including old (and copied) customer emails.

Click Review invoice, followed by Update invoice. The Update invoice dialog displays all of the email addresses associated with the previous invoice including old (and copied) customer emails.

[Update the payment collection method](#change-collection-method)

## Update the payment collection method

If you want to revise an invoice to automatically charge your customer, click Automatically charge a payment method on file, and then review the invoice. Before you proceed to automatically charge the customer, a dialog appears that asks you whether your customer is aware of the change. The dialog also lets you add an internal note for future reference.

[Edit a draft invoice linked to a revision](#edit-draft-invoice)

## Edit a draft invoice linked to a revision

If you want to return to a draft invoice that’s associated with a revision, complete the following steps:

- Exit the editor.

Exit the editor.

- When you’re ready to resume editing, click the draft invoice in the History section of the Invoice details page, or use the Edit invoice button. A dialog appears notifying you that Stripe saved previous, unfinalized changes to a draft.

When you’re ready to resume editing, click the draft invoice in the History section of the Invoice details page, or use the Edit invoice button. A dialog appears notifying you that Stripe saved previous, unfinalized changes to a draft.

- Choose to continue editing the draft or create a new one.

Choose to continue editing the draft or create a new one.

[Customers and revised invoices](#customer-payment)

## Customers and revised invoices

When you revise an invoice and choose to notify your customer:

- Stripe sends them a new email. The subject line of the email indicates that you made an update and also references the old invoice number.

Stripe sends them a new email. The subject line of the email indicates that you made an update and also references the old invoice number.

- When your customer clicks into the email, they see a revised invoice with the new invoice number. Within the revised invoice, there’s an Older versions section that displays older invoices. Your customer can download PDFs of any of the old invoices for their records.Updated invoice email

When your customer clicks into the email, they see a revised invoice with the new invoice number. Within the revised invoice, there’s an Older versions section that displays older invoices. Your customer can download PDFs of any of the old invoices for their records.

Updated invoice email

Stripe lists every invoice version under Older versions. Because the latest email contains all of the relevant invoice information, your customer doesn’t have to search their inbox for previous invoices. If your customer clicks Pay this invoice in an old email, we automatically redirect them to the latest Hosted Invoice Page.

## See also

- Use the Dashboard

[Use the Dashboard](/invoicing/dashboard)

- Integrate with the API

[Integrate with the API](/invoicing/integration)

- Hosted Invoice Page

[Hosted Invoice Page](/invoicing/hosted-invoice-page)
