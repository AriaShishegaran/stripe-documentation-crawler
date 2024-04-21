- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Top-up object

[The Top-up object](/api/topups/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerAmount transferred.

Amount transferred.

- currencystringThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- statusenumThe status of the top-up is either canceled, failed, pending, reversed, or succeeded.Possible enum valuescanceledfailedpendingreversedsucceeded

The status of the top-up is either canceled, failed, pending, reversed, or succeeded.

- objectstring

- balance_transactionnullable stringExpandable

- createdtimestamp

- expected_availability_datenullable integer

- failure_codenullable string

- failure_messagenullable string

- livemodeboolean

- sourcenullable objectDeprecated

- statement_descriptornullable string

- transfer_groupnullable string

# Create a top-up

[Create a top-up](/api/topups/create)

Top up the balance of an account

- amountintegerRequiredA positive integer representing how much to transfer.

A positive integer representing how much to transfer.

- currencystringRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- sourcestring

- statement_descriptorstring

- transfer_groupstring

Returns the top-up object.

# Update a top-up

[Update a top-up](/api/topups/update)

Updates the metadata of a top-up. Other top-up details are not editable by design.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

The newly updated top-up object if the call succeeded. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve a top-up

[Retrieve a top-up](/api/topups/retrieve)

Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.

No parameters.

Returns a top-up if a valid identifier was provided, and raises an error otherwise.

[an error](#errors)

# List all top-ups

[List all top-ups](/api/topups/list)

Returns a list of top-ups.

- statusstringOnly return top-ups that have the given status. One of canceled, failed, pending or succeeded.

Only return top-ups that have the given status. One of canceled, failed, pending or succeeded.

- amountobject

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary containing the data property, which is an array of separate top-up objects. The number of top-ups in the array is limited to the number designated in limit. If no more top-ups are available, the resulting array will be empty.
