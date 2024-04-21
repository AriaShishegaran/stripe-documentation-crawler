- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Application Fee Refunds

[Application Fee Refunds](/api/fee_refunds)

Application Fee Refund objects allow you to refund an application fee that has previously been created but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

Related guide: Refunding application fees

[Refunding application fees](/connect/destination-charges#refunding-app-fee)

[POST/v1/application_fees/:id/refunds](/api/fee_refunds/create)

[POST/v1/application_fees/:id/refunds/:id](/api/fee_refunds/update)

[GET/v1/application_fees/:id/refunds/:id](/api/fee_refunds/retrieve)

[GET/v1/application_fees/:id/refunds](/api/fee_refunds/list)

# The Application Fee Refund object

[The Application Fee Refund object](/api/fee_refunds/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerAmount, in cents.

Amount, in cents.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- feestringExpandableID of the application fee that was refunded.

ID of the application fee that was refunded.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- objectstring

- balance_transactionnullable stringExpandable

- createdtimestamp

# Create an application fee refund

[Create an application fee refund](/api/fee_refunds/create)

Refunds an application fee that has previously been collected but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

You can optionally refund only part of an application fee. You can do so multiple times, until the entire fee has been refunded.

Once entirely refunded, an application fee can’t be refunded again. This method will raise an error when called on an already-refunded application fee, or when trying to refund more money than is left on an application fee.

- amountintegerA positive integer, in cents, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.

A positive integer, in cents, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the Application Fee Refund object if the refund succeeded. Raises an error if the fee has already been refunded, or if an invalid fee identifier was provided.

[an error](#errors)

# Update an application fee refund

[Update an application fee refund](/api/fee_refunds/update)

Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata as an argument.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the application fee refund object if the update succeeded. This call will raise an error if update parameters are invalid.

[an error](#errors)

# Retrieve an application fee refund

[Retrieve an application fee refund](/api/fee_refunds/retrieve)

By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.

No parameters.

Returns the application fee refund object.
