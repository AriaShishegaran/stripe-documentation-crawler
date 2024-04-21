- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve an upcoming invoice

[Retrieve an upcoming invoice](/api/invoices/upcoming)

At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.

Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.

You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the subscription_proration_date parameter when doing the actual subscription update. The recommended way to get only the prorations being previewed is to consider only proration line items where period[start] is equal to the subscription_proration_date value passed in the request.

- customerstringThe identifier of the customer whose upcoming invoice you’d like to retrieve. If automatic_tax is enabled then one of customer, customer_details, subscription, or schedule must be set.

The identifier of the customer whose upcoming invoice you’d like to retrieve. If automatic_tax is enabled then one of customer, customer_details, subscription, or schedule must be set.

- subscriptionstringThe identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but a subscription_items is provided, you will preview creating a subscription with those items. If neither subscription nor subscription_items is provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.

The identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but a subscription_items is provided, you will preview creating a subscription with those items. If neither subscription nor subscription_items is provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.

- automatic_taxobject

- couponstringDeprecated

- currencyenum

- customer_detailsobject

- discountsarray of objects

- invoice_itemsarray of objects

- issuerobjectConnect only

- on_behalf_ofstringConnect only

- schedulestring

- schedule_detailsobject

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

Returns an invoice if valid customer information is provided. Raises an error otherwise.

[an error](#errors)

# Retrieve an invoice's line items

[Retrieve an invoice's line items](/api/invoices/invoice_lines)

When retrieving an invoice, you’ll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

Returns a list of line_item objects.

[line_item objects](#invoice_line_item_object)

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