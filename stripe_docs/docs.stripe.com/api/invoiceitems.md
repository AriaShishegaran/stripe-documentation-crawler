- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Invoice Items

[Invoice Items](/api/invoiceitems)

Invoice Items represent the component lines of an invoice. An invoice item is added to an invoice by creating or updating it with an invoice field, at which point it will be included as an invoice line item within invoice.lines.

[invoice](/api/invoices)

[an invoice line item](/api/invoices/line_item)

[invoice.lines](/api/invoices/object#invoice_object-lines)

Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined with a subscription. Sometimes you want to add a charge or credit to a customer, but actually charge or credit the customer’s card only at the end of a regular billing cycle. This is useful for combining several charges (to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

[subscription](/api/subscriptions)

Related guides: Integrate with the Invoicing API, Subscription Invoices.

[Integrate with the Invoicing API](/invoicing/integration)

[Subscription Invoices](/billing/invoices/subscription#adding-upcoming-invoice-items)

[POST/v1/invoiceitems](/api/invoiceitems/create)

[POST/v1/invoiceitems/:id](/api/invoiceitems/update)

[GET/v1/invoiceitems/:id](/api/invoiceitems/retrieve)

[GET/v1/invoiceitems](/api/invoiceitems/list)

[DELETE/v1/invoiceitems/:id](/api/invoiceitems/delete)

# The Invoice Item object

[The Invoice Item object](/api/invoiceitems/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerAmount (in the currency specified) of the invoice item. This should always be equal to unit_amount * quantity.

Amount (in the currency specified) of the invoice item. This should always be equal to unit_amount * quantity.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customerstringExpandableThe ID of the customer who will be billed when this invoice item is billed.

The ID of the customer who will be billed when this invoice item is billed.

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.Show child attributes

The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

[Stripe Revenue Recognition](/revenue-recognition)

[Revenue Recognition documentation](/revenue-recognition/methodology/subscriptions-and-invoicing)

- pricenullable objectThe price of the invoice item.Show child attributes

The price of the invoice item.

- prorationbooleanWhether the invoice item was created automatically as a proration adjustment when the customer switched plans.

Whether the invoice item was created automatically as a proration adjustment when the customer switched plans.

- objectstring

- datetimestamp

- discountableboolean

- discountsnullable array of stringsExpandable

- invoicenullable stringExpandable

- livemodeboolean

- quantityinteger

- subscriptionnullable stringExpandable

- subscription_itemnullable string

- tax_ratesnullable array of objects

- test_clocknullable stringExpandable

- unit_amountnullable integer

- unit_amount_decimalnullable decimal string

# Create an invoice item

[Create an invoice item](/api/invoiceitems/create)

Creates an item to be added to a draft invoice (up to 250 items per invoice). If no invoice is specified, the item will be on the next invoice created for the customer specified.

- customerstringRequiredThe ID of the customer who will be billed when this invoice item is billed.

The ID of the customer who will be billed when this invoice item is billed.

- amountintegerThe integer amount in cents of the charge to be applied to the upcoming invoice. Passing in a negative amount will reduce the amount_due on the invoice.

The integer amount in cents of the charge to be applied to the upcoming invoice. Passing in a negative amount will reduce the amount_due on the invoice.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionstringAn arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.Show child parameters

The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

[Stripe Revenue Recognition](/revenue-recognition)

[Revenue Recognition documentation](/revenue-recognition/methodology/subscriptions-and-invoicing)

- pricestringThe ID of the price object.

The ID of the price object.

- discountableboolean

- discountsarray of objects

- invoicestring

- price_dataobject

- quantityinteger

- subscriptionstring

- tax_behaviorenum

- tax_codestring

- tax_ratesarray of strings

- unit_amountinteger

- unit_amount_decimalstring

The created invoice item object is returned if successful. Otherwise, this call raises an error.

[an error](#errors)

# Update an invoice item

[Update an invoice item](/api/invoiceitems/update)

Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.

- amountintegerThe integer amount in cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.

The integer amount in cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.

- descriptionstringAn arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.Show child parameters

The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

[Stripe Revenue Recognition](/revenue-recognition)

[Revenue Recognition documentation](/revenue-recognition/methodology/subscriptions-and-invoicing)

- pricestringThe ID of the price object.

The ID of the price object.

- discountableboolean

- discountsarray of objects

- price_dataobject

- quantityinteger

- tax_behaviorenum

- tax_codestring

- tax_ratesarray of strings

- unit_amountinteger

- unit_amount_decimalstring

The updated invoice item object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve an invoice item

[Retrieve an invoice item](/api/invoiceitems/retrieve)

Retrieves the invoice item with the given ID.

No parameters.

Returns an invoice item if a valid invoice item ID was provided. Raises an error otherwise.

[an error](#errors)
