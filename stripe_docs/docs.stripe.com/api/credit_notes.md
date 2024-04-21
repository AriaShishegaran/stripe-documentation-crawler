- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Credit Note

[Credit Note](/api/credit_notes)

Issue a credit note to adjust an invoice’s amount after the invoice is finalized.

Related guide: Credit notes

[Credit notes](/billing/invoices/credit-notes)

[POST/v1/credit_notes](/api/credit_notes/create)

[POST/v1/credit_notes/:id](/api/credit_notes/update)

[GET/v1/credit_notes/:id/lines](/api/credit_notes/lines)

[GET/v1/credit_notes/preview/lines](/api/credit_notes/preview_lines)

[GET/v1/credit_notes/:id](/api/credit_notes/retrieve)

[GET/v1/credit_notes](/api/credit_notes/list)

[GET/v1/credit_notes/preview](/api/credit_notes/preview)

[POST/v1/credit_notes/:id/void](/api/credit_notes/void)

# The Credit Note object

[The Credit Note object](/api/credit_notes/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- invoicestringExpandableID of the invoice.

ID of the invoice.

- linesobjectLine items that make up the credit noteShow child attributes

Line items that make up the credit note

- memonullable stringCustomer-facing text that appears on the credit note PDF.

Customer-facing text that appears on the credit note PDF.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- reasonnullable enumReason for issuing this credit note, one of duplicate, fraudulent, order_change, or product_unsatisfactoryPossible enum valuesduplicatefraudulentorder_changeproduct_unsatisfactory

Reason for issuing this credit note, one of duplicate, fraudulent, order_change, or product_unsatisfactory

- statusenumStatus of this credit note, one of issued or void. Learn more about voiding credit notes.Possible enum valuesissuedThe credit note has been issued.voidThe credit note has been voided.

Status of this credit note, one of issued or void. Learn more about voiding credit notes.

[voiding credit notes](/billing/invoices/credit-notes#voiding)

The credit note has been issued.

The credit note has been voided.

- subtotalintegerThe integer amount in cents representing the amount of the credit note, excluding exclusive tax and invoice level discounts.

The integer amount in cents representing the amount of the credit note, excluding exclusive tax and invoice level discounts.

- totalintegerThe integer amount in cents representing the total amount of the credit note, including tax and all discount.

The integer amount in cents representing the total amount of the credit note, including tax and all discount.

- objectstring

- amountinteger

- amount_shippinginteger

- createdtimestamp

- customerstringExpandable

- customer_balance_transactionnullable stringExpandable

- discount_amountintegerDeprecated

- discount_amountsarray of objects

- effective_atnullable timestamp

- livemodeboolean

- numberstring

- out_of_band_amountnullable integer

- pdfstring

- refundnullable stringExpandable

- shipping_costnullable object

- subtotal_excluding_taxnullable integer

- tax_amountsarray of objects

- total_excluding_taxnullable integer

- typeenum

- voided_atnullable timestamp

# The Credit Note Line Item object

[The Credit Note Line Item object](/api/credit_notes/line_item)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- amountintegerThe integer amount in cents representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.

The integer amount in cents representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.

- amount_excluding_taxnullable integerThe integer amount in cents representing the amount being credited for this line item, excluding all tax and discounts.

The integer amount in cents representing the amount being credited for this line item, excluding all tax and discounts.

- descriptionnullable stringDescription of the item being credited.

Description of the item being credited.

- discount_amountintegerDeprecatedThe integer amount in cents representing the discount being credited for this line item.

The integer amount in cents representing the discount being credited for this line item.

- discount_amountsarray of objectsThe amount of discount calculated per discount for this line itemShow child attributes

The amount of discount calculated per discount for this line item

- invoice_line_itemnullable stringID of the invoice line item being credited

ID of the invoice line item being credited

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- quantitynullable integerThe number of units of product being credited.

The number of units of product being credited.

- tax_amountsarray of objectsThe amount of tax calculated per tax rate for this line itemShow child attributes

The amount of tax calculated per tax rate for this line item

- tax_ratesarray of objectsThe tax rates which apply to the line item.Show child attributes

The tax rates which apply to the line item.

- typeenumThe type of the credit note line item, one of invoice_line_item or custom_line_item. When the type is invoice_line_item there is an additional invoice_line_item property on the resource the value of which is the id of the credited line item on the invoice.Possible enum valuescustom_line_iteminvoice_line_item

The type of the credit note line item, one of invoice_line_item or custom_line_item. When the type is invoice_line_item there is an additional invoice_line_item property on the resource the value of which is the id of the credited line item on the invoice.

- unit_amountnullable integerThe cost of each unit of product being credited.

The cost of each unit of product being credited.

- unit_amount_decimalnullable decimal stringSame as unit_amount, but contains a decimal value with at most 12 decimal places.

Same as unit_amount, but contains a decimal value with at most 12 decimal places.

- unit_amount_excluding_taxnullable decimal stringThe amount in cents representing the unit amount being credited for this line item, excluding all tax and discounts.

The amount in cents representing the unit amount being credited for this line item, excluding all tax and discounts.

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
