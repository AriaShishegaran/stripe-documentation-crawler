- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Quote object

[The Quote object](/api/quotes/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- line_itemsobjectExpandableA list of items the customer is being quoted for.Show child attributes

A list of items the customer is being quoted for.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- objectstring

- amount_subtotalinteger

- amount_totalinteger

- applicationnullable stringExpandableConnect only

- application_fee_amountnullable integerConnect only

- application_fee_percentnullable floatConnect only

- automatic_taxobject

- collection_methodenum

- computedobject

- createdtimestamp

- currencynullable string

- customernullable stringExpandable

- default_tax_ratesarray of stringsExpandable

- descriptionnullable string

- discountsarray of stringsExpandable

- expires_attimestamp

- footernullable string

- from_quotenullable object

- headernullable string

- invoicenullable stringExpandable

- invoice_settingsobject

- livemodeboolean

- numbernullable string

- on_behalf_ofnullable stringExpandableConnect only

- statusenum

- status_transitionsobject

- subscriptionnullable stringExpandable

- subscription_dataobject

- subscription_schedulenullable stringExpandable

- test_clocknullable stringExpandable

- total_detailsobject

- transfer_datanullable objectConnect only

# Create a quote

[Create a quote](/api/quotes/create)

A quote models prices and services for a customer. Default options for header, description, footer, and expires_at can be set in the dashboard via the quote template.

[quote template](https://dashboard.stripe.com/settings/billing/quote)

- line_itemsarray of objectsA list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.Show child parameters

A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- application_fee_amountintegerConnect only

- application_fee_percentfloatConnect only

- automatic_taxobject

- collection_methodenum

- customerstring

- default_tax_ratesarray of strings

- descriptionstring

- discountsarray of objects

- expires_attimestamp

- footerstring

- from_quoteobject

- headerstring

- invoice_settingsobject

- on_behalf_ofstringConnect only

- subscription_dataobject

- test_clockstring

- transfer_dataobjectConnect only

Returns the quote object.

# Update a quote

[Update a quote](/api/quotes/update)

A quote models prices and services for a customer.

- line_itemsarray of objectsA list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.Show child parameters

A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- application_fee_amountintegerConnect only

- application_fee_percentfloatConnect only

- automatic_taxobject

- collection_methodenum

- customerstring

- default_tax_ratesarray of strings

- descriptionstring

- discountsarray of objects

- expires_attimestamp

- footerstring

- headerstring

- invoice_settingsobject

- on_behalf_ofstringConnect only

- subscription_dataobject

- transfer_dataobjectConnect only

Returns the updated quote object.

# Retrieve a quote's line items

[Retrieve a quote's line items](/api/quotes/line_items/list)

When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit quote line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more line items are available, the resulting array will be empty.

# Retrieve a quote's upfront line items

[Retrieve a quote's upfront line items](/api/quotes/line_items/upfront/list)

When retrieving a quote, there is an includable computed.upfront.line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.

[computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items)

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit upfront line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more upfront line items are available, the resulting array will be empty.
