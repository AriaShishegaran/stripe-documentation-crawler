- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve an upcoming invoice's line items

[Retrieve an upcoming invoice's line items](/api/invoices/upcoming_invoice_lines)

When retrieving an upcoming invoice, you’ll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

- customerstringThe identifier of the customer whose upcoming invoice you’d like to retrieve. If automatic_tax is enabled then one of customer, customer_details, subscription, or schedule must be set.

The identifier of the customer whose upcoming invoice you’d like to retrieve. If automatic_tax is enabled then one of customer, customer_details, subscription, or schedule must be set.

- subscriptionstringThe identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but a subscription_items is provided, you will preview creating a subscription with those items. If neither subscription nor subscription_items is provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.

The identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but a subscription_items is provided, you will preview creating a subscription with those items. If neither subscription nor subscription_items is provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.

- automatic_taxobject

- couponstringDeprecated

- currencyenum

- customer_detailsobject

- discountsarray of objects

- ending_beforestring

- invoice_itemsarray of objects

- issuerobjectConnect only

- limitinteger

- on_behalf_ofstringConnect only

- schedulestring

- schedule_detailsobject

- starting_afterstring

- subscription_billing_cycle_anchorstring | timestampDeprecated

- subscription_cancel_attimestampDeprecated

- subscription_cancel_at_period_endbooleanDeprecated

- subscription_cancel_nowbooleanDeprecated

- subscription_default_tax_ratesarray of stringsDeprecated

- subscription_detailsobject

- subscription_itemsarray of objectsDeprecated

- subscription_proration_behaviorenumDeprecated

- subscription_proration_datetimestampDeprecated

- subscription_resume_atstringDeprecated

- subscription_start_datetimestampDeprecated

- subscription_trial_endstring | timestampDeprecated

Returns a list of line_item objects.

[line_item objects](#invoice_line_item_object)

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
