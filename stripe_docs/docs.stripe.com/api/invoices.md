- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Invoices

[Invoices](/api/invoices)

Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.

They contain invoice items, and proration adjustments that may be caused by subscription upgrades/downgrades (if necessary).

[invoice items](#invoiceitems)

If your invoice is configured to be billed through automatic charges, Stripe automatically finalizes your invoice and attempts payment.  Note that finalizing the invoice, when automatic, does not happen immediately as the invoice is created. Stripe waits until one hour after the last webhook was successfully sent (or the last webhook timed out after failing). If you (and the platforms you may have connected to) have no webhooks configured, Stripe waits one hour after creation to finalize the invoice.

[when automatic](/invoicing/integration/automatic-advancement-collection)

If your invoice is configured to be billed by sending an email, then based on your email settings, Stripe will email the invoice to your customer and await payment. These emails can contain a link to a hosted page to pay the invoice.

[email settings](https://dashboard.stripe.com/account/billing/automatic)

Stripe applies any customer credit on the account before determining the amount due for the invoice (i.e., the amount that will be actually charged). If the amount due for the invoice is less than Stripe’s minimum allowed charge per currency, the invoice is automatically marked paid, and we add the amount due to the customer’s credit balance which is applied to the next invoice.

[minimum allowed charge per currency](/currencies#minimum-and-maximum-charge-amounts)

More details on the customer’s credit balance are here.

[here](/billing/customer/balance)

Related guide: Send invoices to customers

[Send invoices to customers](/billing/invoices/sending)

[POST/v1/invoices](/api/invoices/create)

[POST/v1/invoices/create_preview](/api/invoices/create_preview)

[POST/v1/invoices/:id](/api/invoices/update)

[POST/v1/invoices/:id/lines/:id](/api/invoices/update_line)

[GET/v1/invoices/:id](/api/invoices/retrieve)

[GET/v1/invoices/upcoming](/api/invoices/upcoming)

[GET/v1/invoices/:id/lines](/api/invoices/invoice_lines)

[GET/v1/invoices/upcoming/lines](/api/invoices/upcoming_invoice_lines)

[GET/v1/invoices](/api/invoices/list)

[DELETE/v1/invoices/:id](/api/invoices/delete)

[POST/v1/invoices/:id/finalize](/api/invoices/finalize)

[POST/v1/invoices/:id/mark_uncollectible](/api/invoices/mark_uncollectible)

[POST/v1/invoices/:id/pay](/api/invoices/pay)

[GET/v1/invoices/search](/api/invoices/search)

[POST/v1/invoices/:id/send](/api/invoices/send)

[POST/v1/invoices/:id/void](/api/invoices/void)

# The Invoice object

[The Invoice object](/api/invoices/object)

- idstringUnique identifier for the object. This property is always present unless the invoice is an upcoming invoice. See Retrieve an upcoming invoice for more details.

Unique identifier for the object. This property is always present unless the invoice is an upcoming invoice. See Retrieve an upcoming invoice for more details.

[Retrieve an upcoming invoice](https://stripe.com/docs/api/invoices/upcoming)

- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

Controls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

- chargenullable stringExpandableID of the latest charge generated for this invoice, if any.

ID of the latest charge generated for this invoice, if any.

- collection_methodenumEither charge_automatically, or send_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.Possible enum valuescharge_automaticallyAttempt payment using the default source attached to the customer.send_invoiceEmail payment instructions to the customer.

Either charge_automatically, or send_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.

Attempt payment using the default source attached to the customer.

Email payment instructions to the customer.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customerstringExpandableThe ID of the customer who will be billed.

The ID of the customer who will be billed.

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.

An arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.

- hosted_invoice_urlnullable stringThe URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null.

The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null.

- linesobjectThe individual line items that make up the invoice. lines is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.Show child attributes

The individual line items that make up the invoice. lines is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- payment_intentnullable stringExpandableThe PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice. Note that voiding an invoice will cancel the PaymentIntent.

The PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice. Note that voiding an invoice will cancel the PaymentIntent.

- period_endtimestampEnd of the usage period during which invoice items were added to this invoice.

End of the usage period during which invoice items were added to this invoice.

- period_starttimestampStart of the usage period during which invoice items were added to this invoice.

Start of the usage period during which invoice items were added to this invoice.

- statusnullable enumThe status of the invoice, one of draft, open, paid, uncollectible, or void. Learn more

The status of the invoice, one of draft, open, paid, uncollectible, or void. Learn more

[Learn more](/billing/invoices/workflow#workflow-overview)

- subscriptionnullable stringExpandableThe subscription that this invoice was prepared for, if any.

The subscription that this invoice was prepared for, if any.

- totalintegerTotal after discounts and taxes.

Total after discounts and taxes.

- objectstring

- account_countrynullable string

- account_namenullable string

- account_tax_idsnullable array of stringsExpandable

- amount_dueinteger

- amount_paidinteger

- amount_remaininginteger

- amount_shippinginteger

- applicationnullable stringExpandableConnect only

- application_fee_amountnullable integerConnect only

- attempt_countinteger

- attemptedboolean

- automatic_taxobject

- billing_reasonnullable enum

- createdtimestamp

- custom_fieldsnullable array of objects

- customer_addressnullable object

- customer_emailnullable string

- customer_namenullable string

- customer_phonenullable string

- customer_shippingnullable object

- customer_tax_exemptnullable enum

- customer_tax_idsnullable array of objects

- default_payment_methodnullable stringExpandable

- default_sourcenullable stringExpandable

- default_tax_ratesarray of objects

- discountnullable objectDeprecated

- discountsarray of stringsExpandable

- due_datenullable timestamp

- effective_atnullable timestamp

- ending_balancenullable integer

- footernullable string

- from_invoicenullable object

- invoice_pdfnullable string

- issuerobjectConnect only

- last_finalization_errornullable object

- latest_revisionnullable stringExpandable

- livemodeboolean

- next_payment_attemptnullable timestamp

- numbernullable string

- on_behalf_ofnullable stringExpandableConnect only

- paidboolean

- paid_out_of_bandboolean

- payment_settingsobject

- post_payment_credit_notes_amountinteger

- pre_payment_credit_notes_amountinteger

- quotenullable stringExpandable

- receipt_numbernullable string

- renderingnullable object

- shipping_costnullable object

- shipping_detailsnullable object

- starting_balanceinteger

- statement_descriptornullable string

- status_transitionsobject

- subscription_detailsnullable object

- subscription_proration_datenullable integer

- subtotalinteger

- subtotal_excluding_taxnullable integer

- taxnullable integer

- test_clocknullable stringExpandable

- threshold_reasonnullable object

- total_discount_amountsnullable array of objects

- total_excluding_taxnullable integer

- total_tax_amountsarray of objects

- transfer_datanullable objectConnect only

- webhooks_delivered_atnullable timestamp

# The Invoice Line Item object

[The Invoice Line Item object](/api/invoices/line_item)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerThe amount, in cents.

The amount, in cents.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- invoicenullable stringThe ID of the invoice that contains this line item.

The ID of the invoice that contains this line item.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with type=subscription, metadata reflects the current metadata from the subscription associated with the line item, unless the invoice line was directly updated with different metadata after creation.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with type=subscription, metadata reflects the current metadata from the subscription associated with the line item, unless the invoice line was directly updated with different metadata after creation.

[key-value pairs](/api/metadata)

- periodobjectThe period this line_item covers. For subscription line items, this is the subscription period. For prorations, this starts when the proration was calculated, and ends at the period end of the subscription. For invoice items, this is the time at which the invoice item was created or the period of the item. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.Show child attributes

The period this line_item covers. For subscription line items, this is the subscription period. For prorations, this starts when the proration was calculated, and ends at the period end of the subscription. For invoice items, this is the time at which the invoice item was created or the period of the item. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

[Stripe Revenue Recognition](/revenue-recognition)

[Revenue Recognition documentation](/revenue-recognition/methodology/subscriptions-and-invoicing)

- pricenullable objectThe price of the line item.Show child attributes

The price of the line item.

- prorationbooleanWhether this is a proration.

Whether this is a proration.

- quantitynullable integerThe quantity of the subscription, if the line item is a subscription or a proration.

The quantity of the subscription, if the line item is a subscription or a proration.

- typeenumA string identifying the type of the source of this line item, either an invoiceitem or a subscription.Possible enum valuesinvoiceitemsubscription

A string identifying the type of the source of this line item, either an invoiceitem or a subscription.

- objectstring

- amount_excluding_taxnullable integer

- discount_amountsnullable array of objects

- discountableboolean

- discountsarray of stringsExpandable

- invoice_itemnullable stringExpandable

- livemodeboolean

- proration_detailsnullable object

- subscriptionnullable stringExpandable

- subscription_itemnullable stringExpandable

- tax_amountsarray of objects

- tax_ratesarray of objects

- unit_amount_excluding_taxnullable decimal string

# Create an invoice

[Create an invoice](/api/invoices/create)

This endpoint creates a draft invoice for a given customer. The invoice remains a draft until you finalize the invoice, which allows you to pay or send the invoice to your customers.

[finalize](#finalize_invoice)

[pay](#pay_invoice)

[send](#send_invoice)

- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

Controls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

- collection_methodenumEither charge_automatically, or send_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to charge_automatically.Possible enum valuescharge_automaticallysend_invoice

Either charge_automatically, or send_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to charge_automatically.

- customerstringThe ID of the customer who will be billed.

The ID of the customer who will be billed.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.

An arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- subscriptionstringThe ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription’s billing cycle and regular subscription events won’t be affected.

The ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription’s billing cycle and regular subscription events won’t be affected.

- account_tax_idsarray of strings

- application_fee_amountintegerConnect only

- automatic_taxobject

- currencyenum

- custom_fieldsarray of objects

- days_until_dueinteger

- default_payment_methodstring

- default_sourcestring

- default_tax_ratesarray of strings

- discountsarray of objects

- due_datetimestamp

- effective_attimestamp

- footerstring

- from_invoiceobject

- issuerobjectConnect only

- numberstring

- on_behalf_ofstringConnect only

- payment_settingsobject

- pending_invoice_items_behaviorenum

- renderingobject

- shipping_costobject

- shipping_detailsobject

- statement_descriptorstring

- transfer_dataobjectConnect only

Returns the invoice object. Raises an error if the customer ID provided is invalid.

[an error](#errors)

# Create a preview invoice

[Create a preview invoice](/api/invoices/create_preview)

At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.

Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.

You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the subscription_details.proration_date parameter when doing the actual subscription update. The recommended way to get only the prorations being previewed is to consider only proration line items where period[start] is equal to the subscription_details.proration_date value passed in the request.

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

- subscription_detailsobject

Returns an invoice if valid customer information is provided. Raises an error otherwise.

[an error](#errors)
