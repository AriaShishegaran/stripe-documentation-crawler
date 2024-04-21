- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# List all invoices

[List all invoices](/api/invoices/list)

You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.

- customerstringOnly return invoices for the customer specified by this customer ID.

Only return invoices for the customer specified by this customer ID.

- statusenumThe status of the invoice, one of draft, open, paid, uncollectible, or void. Learn more

The status of the invoice, one of draft, open, paid, uncollectible, or void. Learn more

[Learn more](/billing/invoices/workflow#workflow-overview)

- subscriptionstringOnly return invoices for the subscription specified by this subscription ID.

Only return invoices for the subscription specified by this subscription ID.

- collection_methodenum

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array invoice attachments,

# Delete a draft invoice

[Delete a draft invoice](/api/invoices/delete)

Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be voided.

[voided](#void_invoice)

No parameters.

A successfully deleted invoice. Otherwise, this call raises an error, such as if the invoice has already been deleted.

[an error](#errors)

# Finalize an invoice

[Finalize an invoice](/api/invoices/finalize)

Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.

- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

Controls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

Returns an invoice object with status=open.

# Mark an invoice as uncollectible

[Mark an invoice as uncollectible](/api/invoices/mark_uncollectible)

Marking an invoice as uncollectible is useful for keeping track of bad debts that can be written off for accounting purposes.

No parameters.

Returns the invoice object.

# Pay an invoice

[Pay an invoice](/api/invoices/pay)

Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your subscriptions settings. However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.

[subscriptions settings](https://dashboard.stripe.com/account/billing/automatic)

No parameters.

- forgiveboolean

- mandatestring

- off_sessionboolean

- paid_out_of_bandboolean

- payment_methodstring

- sourcestring

Returns the invoice object.
