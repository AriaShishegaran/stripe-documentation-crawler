- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# SourcesDeprecated

[Sources](/api/sources)

Source objects allow you to accept a variety of payment methods. They represent a customer’s payment instrument, and can be used with the Stripe API just like a Card object: once chargeable, they can be charged, or can be attached to customers.

Stripe doesn’t recommend using the deprecated Sources API. We recommend that you adopt the PaymentMethods API. This newer API provides access to our latest features and payment method types.

[Sources API](/api/sources)

[PaymentMethods API](/api/payment_methods)

Related guides: Sources API and Sources & Customers.

[Sources API](/sources)

[Sources & Customers](/sources/customers)

[POST/v1/sources](/api/sources/create)

[POST/v1/sources/:id](/api/sources/update)

[GET/v1/sources/:id](/api/sources/retrieve)

[POST/v1/customers/:id/sources](/api/sources/attach)

[DELETE/v1/customers/:id/sources/:id](/api/sources/detach)

# The Source objectDeprecated

[The Source object](/api/sources/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountnullable integerA positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for single_use sources.

A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for single_use sources.

- currencynullable enumThree-letter ISO code for the currency associated with the source. This is the currency for which the source will be chargeable once ready. Required for single_use sources.

Three-letter ISO code for the currency associated with the source. This is the currency for which the source will be chargeable once ready. Required for single_use sources.

[ISO code for the currency](https://stripe.com/docs/currencies)

- customernullable stringThe ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.

The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- ownernullable objectInformation about the owner of the payment instrument that may be used or required by particular source types.Show child attributes

Information about the owner of the payment instrument that may be used or required by particular source types.

- redirectnullable objectInformation related to the redirect flow. Present if the source is authenticated by a redirect (flow is redirect).Show child attributes

Information related to the redirect flow. Present if the source is authenticated by a redirect (flow is redirect).

- statement_descriptornullable stringExtra information about a source. This will appear on your customer’s statement every time you charge the source.

Extra information about a source. This will appear on your customer’s statement every time you charge the source.

- statusstringThe status of the source, one of canceled, chargeable, consumed, failed, or pending. Only chargeable sources can be used to create a charge.

The status of the source, one of canceled, chargeable, consumed, failed, or pending. Only chargeable sources can be used to create a charge.

- typeenumThe type of the source. The type is a payment method, one of ach_credit_transfer, ach_debit, alipay, bancontact, card, card_present, eps, giropay, ideal, multibanco, klarna, p24, sepa_debit, sofort, three_d_secure, or wechat. An additional hash is included on the source with a name matching this value. It contains additional information specific to the payment method used.Possible enum valuesach_credit_transferach_debitalipaybancontactcardcard_presentepsgiropayidealklarnaShow 6 more

The type of the source. The type is a payment method, one of ach_credit_transfer, ach_debit, alipay, bancontact, card, card_present, eps, giropay, ideal, multibanco, klarna, p24, sepa_debit, sofort, three_d_secure, or wechat. An additional hash is included on the source with a name matching this value. It contains additional information specific to the payment method used.

[payment method](/sources)

- objectstring

- client_secretstring

- code_verificationnullable object

- createdtimestamp

- flowstring

- livemodeboolean

- receivernullable object

- source_ordernullable object

- usagenullable string

# Create a source

[Create a source](/api/sources/create)

Creates a new source object.

- typestringRequiredThe type of the source to create. Required unless customer and original_source are specified (see the Cloning card Sources guide)

The type of the source to create. Required unless customer and original_source are specified (see the Cloning card Sources guide)

[Cloning card Sources](/sources/connect#cloning-card-sources)

- amountintegerAmount associated with the source. This is the amount for which the source will be chargeable once ready. Required for single_use sources. Not supported for receiver type sources, where charge amount may not be specified until funds land.

Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for single_use sources. Not supported for receiver type sources, where charge amount may not be specified until funds land.

- currencyenumThree-letter ISO code for the currency associated with the source. This is the currency for which the source will be chargeable once ready.

Three-letter ISO code for the currency associated with the source. This is the currency for which the source will be chargeable once ready.

[ISO code for the currency](https://stripe.com/docs/currencies)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- ownerobjectInformation about the owner of the payment instrument that may be used or required by particular source types.Show child parameters

Information about the owner of the payment instrument that may be used or required by particular source types.

- redirectobjectParameters required for the redirect flow. Required if the source is authenticated by a redirect (flow is redirect).Show child parameters

Parameters required for the redirect flow. Required if the source is authenticated by a redirect (flow is redirect).

- statement_descriptorstringAn arbitrary string to be displayed on your customer’s statement. As an example, if your website is RunClub and the item you’re charging for is a race ticket, you may want to specify a statement_descriptor of RunClub 5K race ticket. While many payment types will display this information, some may not display it at all.

An arbitrary string to be displayed on your customer’s statement. As an example, if your website is RunClub and the item you’re charging for is a race ticket, you may want to specify a statement_descriptor of RunClub 5K race ticket. While many payment types will display this information, some may not display it at all.

- flowstring

- mandateobject

- receiverobject

- source_orderobject

- tokenstring

- usagestring

Returns a newly created source.

# Update a source

[Update a source](/api/sources/update)

Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts the metadata and owner as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our payment method guides for more detail.

[payment method guides](/sources)

- amountintegerAmount associated with the source.

Amount associated with the source.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- ownerobjectInformation about the owner of the payment instrument that may be used or required by particular source types.Show child parameters

Information about the owner of the payment instrument that may be used or required by particular source types.

- mandateobject

- source_orderobject

Returns the source object if the update succeeded. This call will raise an error if update parameters are invalid.

[an error](#errors)

# Retrieve a source

[Retrieve a source](/api/sources/retrieve)

Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

No parameters.

- client_secretstring

Returns a source if a valid identifier was provided.
