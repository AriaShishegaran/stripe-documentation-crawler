- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# List all invoice items

[List all invoice items](/api/invoiceitems/list)

Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.

- customerstringThe identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.

The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.

- createdobject

- ending_beforestring

- invoicestring

- limitinteger

- pendingboolean

- starting_afterstring

A dictionary with a data property that contains an array of up to limit invoice items, starting after invoice item starting_after. Each entry in the array is a separate invoice item object. If no more invoice items are available, the resulting array will be empty.

# Delete an invoice item

[Delete an invoice item](/api/invoiceitems/delete)

Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.

No parameters.

An object with the deleted invoice item’s ID and a deleted flag upon success. Otherwise, this call raises an error, such as if the invoice item has already been deleted.

[an error](#errors)
