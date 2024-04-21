- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Update an invoice's line item

[Update an invoice's line item](/api/invoices/update_line)

Updates an invoice’s line item. Some fields, such as tax_amounts, only live on the invoice line item, so they can only be updated through this endpoint. Other fields, such as amount, live on both the invoice item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well. Updating an invoice’s line item is only possible before the invoice is finalized.

- invoicestringRequiredInvoice ID of line item

Invoice ID of line item

- line_item_idstringRequiredInvoice line item ID

Invoice line item ID

- amountintegerThe integer amount in cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.

The integer amount in cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.

- descriptionstringAn arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata. For type=recurring line items, the incoming metadata specified on the request is directly used to set this value, in contrast to type=invoiceitem line items, where any existing metadata on the invoice line is merged with the incoming data.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata. For type=recurring line items, the incoming metadata specified on the request is directly used to set this value, in contrast to type=invoiceitem line items, where any existing metadata on the invoice line is merged with the incoming data.

[key-value pairs](/api/metadata)

- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.Show child parameters

The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

[Stripe Revenue Recognition](/revenue-recognition)

[Revenue Recognition documentation](/revenue-recognition/methodology/subscriptions-and-invoicing)

- pricestringThe ID of the price object.

The ID of the price object.

- quantityintegerNon-negative integer. The quantity of units for the line item.

Non-negative integer. The quantity of units for the line item.

- discountableboolean

- discountsarray of objects

- price_dataobject

- tax_amountsarray of objects

- tax_ratesarray of strings

The updated invoice’s line item object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve an invoice

[Retrieve an invoice](/api/invoices/retrieve)

Retrieves the invoice with the given ID.

No parameters.

Returns an invoice object if a valid invoice ID was provided. Raises an error otherwise.

[an error](#errors)

The invoice object contains a lines hash that contains information about the subscriptions and invoice items that have been applied to the invoice, as well as any prorations that Stripe has automatically calculated. Each line on the invoice has an amount attribute that represents the amount actually contributed to the invoice’s total. For invoice items and prorations, the amount attribute is the same as for the invoice item or proration respectively. For subscriptions, the amount may be different from the plan’s regular price depending on whether the invoice covers a trial period or the invoice period differs from the plan’s usual interval.

The invoice object has both a subtotal and a total. The subtotal represents the total before any discounts, while the total is the final amount to be charged to the customer after all coupons have been applied.

The invoice also has a next_payment_attempt attribute that tells you the next time (as a Unix timestamp) payment for the invoice will be automatically attempted. For invoices with manual payment collection, that have been closed, or that have reached the maximum number of retries (specified in your subscriptions settings), the next_payment_attempt will be null.

[subscriptions settings](https://dashboard.stripe.com/account/billing/automatic)

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
