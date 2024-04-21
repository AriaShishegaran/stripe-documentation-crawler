- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Transfer Reversals

[Transfer Reversals](/api/transfer_reversals)

Stripe Connect platforms can reverse transfers made to a connected account, either entirely or partially, and can also specify whether to refund any related application fees. Transfer reversals add to the platform’s balance and subtract from the destination account’s balance.

[Stripe Connect](/connect)

Reversing a transfer that was made for a destination charge is allowed only up to the amount of the charge. It is possible to reverse a transfer_group transfer only if the destination account has enough balance to cover the reversal.

[destination charge](/connect/destination-charges)

[transfer_group](/connect/separate-charges-and-transfers#transfer-options)

Related guide: Reverse transfers

[Reverse transfers](/connect/separate-charges-and-transfers#reverse-transfers)

[POST/v1/transfers/:id/reversals](/api/transfer_reversals/create)

[POST/v1/transfers/:id/reversals/:id](/api/transfer_reversals/update)

[GET/v1/transfers/:id/reversals/:id](/api/transfer_reversals/retrieve)

[GET/v1/transfers/:id/reversals](/api/transfer_reversals/list)

# The Transfer Reversal object

[The Transfer Reversal object](/api/transfer_reversals/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerAmount, in cents.

Amount, in cents.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- transferstringExpandableID of the transfer that was reversed.

ID of the transfer that was reversed.

- objectstring

- balance_transactionnullable stringExpandable

- createdtimestamp

- destination_payment_refundnullable stringExpandable

- source_refundnullable stringExpandable

# Create a transfer reversal

[Create a transfer reversal](/api/transfer_reversals/create)

When you create a new reversal, you must specify a transfer to create it on.

When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.

Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.

- amountintegerA positive integer in cents representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.

A positive integer in cents representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.

- descriptionstringAn arbitrary string which you can attach to a reversal object. It is displayed alongside the reversal in the Dashboard. This will be unset if you POST an empty value.

An arbitrary string which you can attach to a reversal object. It is displayed alongside the reversal in the Dashboard. This will be unset if you POST an empty value.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- refund_application_feeboolean

Returns a transfer reversal object if the reversal succeeded. Raises an error if the transfer has already been reversed or an invalid transfer identifier was provided.

[an error](#errors)

# Update a reversal

[Update a reversal](/api/transfer_reversals/update)

Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata and description as arguments.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the reversal object if the update succeeded. This call will raise an error if update parameters are invalid.

[an error](#errors)

# Retrieve a reversal

[Retrieve a reversal](/api/transfer_reversals/retrieve)

By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.

No parameters.

Returns the reversal object.
