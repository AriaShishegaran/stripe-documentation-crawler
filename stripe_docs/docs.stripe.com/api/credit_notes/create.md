- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a credit note

[Create a credit note](/api/credit_notes/create)

Issue a credit note to adjust the amount of a finalized invoice. For a status=open invoice, a credit note reduces its amount_due. For a status=paid invoice, a credit note does not affect its amount_due. Instead, it can result in any combination of the following:

- Refund: create a new refund (using refund_amount) or link an existing refund (using refund).

- Customer balance credit: credit the customer’s balance (using credit_amount) which will be automatically applied to their next invoice when it’s finalized.

- Outside of Stripe credit: record the amount that is or will be credited outside of Stripe (using out_of_band_amount).

For post-payment credit notes the sum of the refund, credit and outside of Stripe amounts must equal the credit note total.

You may issue multiple credit notes for an invoice. Each credit note will increment the invoice’s pre_payment_credit_notes_amount or post_payment_credit_notes_amount depending on its status at the time of credit note creation.

- invoicestringRequiredID of the invoice.

ID of the invoice.

- linesarray of objectsLine items that make up the credit note.Show child parameters

Line items that make up the credit note.

- memostringThe credit note’s memo appears on the credit note PDF.

The credit note’s memo appears on the credit note PDF.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- reasonenumReason for issuing this credit note, one of duplicate, fraudulent, order_change, or product_unsatisfactoryPossible enum valuesduplicatefraudulentorder_changeproduct_unsatisfactory

Reason for issuing this credit note, one of duplicate, fraudulent, order_change, or product_unsatisfactory

- amountinteger

- credit_amountinteger

- effective_attimestamp

- out_of_band_amountinteger

- refundstring

- refund_amountinteger

- shipping_costobject

Returns a credit note object if the call succeeded.

# Update a credit note

[Update a credit note](/api/credit_notes/update)

Updates an existing credit note.

- memostringCredit note memo.

Credit note memo.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the updated credit note object if the call succeeded.

# Retrieve a credit note's line items

[Retrieve a credit note's line items](/api/credit_notes/lines)

When retrieving a credit note, you’ll get a lines property containing the the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

Returns a list of line_item objects.

[line_item objects](#credit_note_line_item_object)

# Retrieve a credit note preview's line items

[Retrieve a credit note preview's line items](/api/credit_notes/preview_lines)

When retrieving a credit note preview, you’ll get a lines property containing the first handful of those items. This URL you can retrieve the full (paginated) list of line items.

- invoicestringRequiredID of the invoice.

ID of the invoice.

- linesarray of objectsLine items that make up the credit note.Show child parameters

Line items that make up the credit note.

- memostringThe credit note’s memo appears on the credit note PDF.

The credit note’s memo appears on the credit note PDF.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- reasonenumReason for issuing this credit note, one of duplicate, fraudulent, order_change, or product_unsatisfactoryPossible enum valuesduplicatefraudulentorder_changeproduct_unsatisfactory

Reason for issuing this credit note, one of duplicate, fraudulent, order_change, or product_unsatisfactory

- amountinteger

- credit_amountinteger

- effective_attimestamp

- ending_beforestring

- limitinteger

- out_of_band_amountinteger

- refundstring

- refund_amountinteger

- shipping_costobject

- starting_afterstring

Returns a list of line_item objects.

[line_item objects](#credit_note_line_item_object)

# Retrieve a credit note

[Retrieve a credit note](/api/credit_notes/retrieve)

Retrieves the credit note object with the given identifier.

No parameters.

Returns a credit note object if a valid identifier was provided.
