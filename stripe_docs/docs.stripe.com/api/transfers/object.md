- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Transfer object

[The Transfer object](/api/transfers/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerAmount in cents to be transferred.

Amount in cents to be transferred.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- destinationnullable stringExpandableID of the Stripe account the transfer was sent to.

ID of the Stripe account the transfer was sent to.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- objectstring

- amount_reversedinteger

- balance_transactionnullable stringExpandable

- createdtimestamp

- destination_paymentnullable stringExpandable

- livemodeboolean

- reversalsobject

- reversedboolean

- source_transactionnullable stringExpandable

- source_typenullable string

- transfer_groupnullable string

# Create a transfer

[Create a transfer](/api/transfers/create)

To send funds from your Stripe account to a connected account, you create a new transfer object. Your Stripe balance must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.

[Stripe balance](#balance)

- currencyenumRequired3-letter ISO code for currency.

3-letter ISO code for currency.

[ISO code for currency](/payouts)

- destinationstringRequiredThe ID of a connected Stripe account. See the Connect documentation for details.

The ID of a connected Stripe account. See the Connect documentation for details.

[See the Connect documentation](/connect/separate-charges-and-transfers)

- amountintegerRequiredA positive integer in cents representing how much to transfer.

A positive integer in cents representing how much to transfer.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- source_transactionstring

- source_typestring

- transfer_groupstring

Returns a transfer object if there were no initial errors with the transfer creation (e.g., insufficient funds).

# Update a transfer

[Update a transfer](/api/transfers/update)

Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts only metadata as an argument.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the transfer object if the update succeeded. This call will raise an error if update parameters are invalid.

[an error](#errors)

# Retrieve a transfer

[Retrieve a transfer](/api/transfers/retrieve)

Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.

No parameters.

Returns a transfer object if a valid identifier was provided, and raises an error otherwise.

[an error](#errors)

# List all transfers

[List all transfers](/api/transfers/list)

Returns a list of existing transfers sent to connected accounts. The transfers are returned in sorted order, with the most recently created transfers appearing first.

- destinationstringOnly return transfers for the destination specified by this account ID.

Only return transfers for the destination specified by this account ID.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

- transfer_groupstring

A dictionary with a data property that contains an array of up to limit transfers, starting after transfer starting_after. Each entry in the array is a separate transfer object. If no more transfers are available, the resulting array will be empty.