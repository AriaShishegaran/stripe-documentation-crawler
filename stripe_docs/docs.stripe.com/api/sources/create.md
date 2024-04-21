- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Attach a source

[Attach a source](/api/sources/attach)

Attaches a Source object to a Customer. The source must be in a chargeable or pending state.

- sourcestringRequiredThe identifier of the source to be attached.

The identifier of the source to be attached.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the attached Source object.

# Detach a source

[Detach a source](/api/sources/detach)

Detaches a Source object from a Customer. The status of a source is changed to consumed when it is detached and it can no longer be used to create a charge.

No parameters.

Returns the detached Source object.
