- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a refund

[Create a refund](/api/refunds/create)

When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.

Creating a new refund will refund a charge that has previously been created but not yet refunded. Funds will be refunded to the credit or debit card that was originally charged.

You can optionally refund only part of a charge. You can do so multiple times, until the entire charge has been refunded.

Once entirely refunded, a charge can’t be refunded again. This method will raise an error when called on an already-refunded charge, or when trying to refund more money than is left on a charge.

- amountintegerA positive integer in the smallest currency unit representing how much of this charge to refund. Can refund only up to the remaining, unrefunded amount of the charge.

A positive integer in the smallest currency unit representing how much of this charge to refund. Can refund only up to the remaining, unrefunded amount of the charge.

[smallest currency unit](/currencies#zero-decimal)

- chargestringThe identifier of the charge to refund.

The identifier of the charge to refund.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- payment_intentstringThe identifier of the PaymentIntent to refund.

The identifier of the PaymentIntent to refund.

- reasonstringString indicating the reason for the refund. If set, possible values are duplicate, fraudulent, and requested_by_customer. If you believe the charge to be fraudulent, specifying fraudulent as the reason will add the associated card and email to your block lists, and will also help us improve our fraud detection algorithms.

String indicating the reason for the refund. If set, possible values are duplicate, fraudulent, and requested_by_customer. If you believe the charge to be fraudulent, specifying fraudulent as the reason will add the associated card and email to your block lists, and will also help us improve our fraud detection algorithms.

[block lists](/radar/lists)

- instructions_emailstring

- refund_application_feebooleanConnect only

- reverse_transferbooleanConnect only

Returns the Refund object if the refund succeeded. Raises an error if the Charge/PaymentIntent has already been refunded, or if an invalid identifier was provided.

[an error](#errors)

# Update a refund

[Update a refund](/api/refunds/update)

Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don’t provide remain unchanged.

This request only accepts metadata as an argument.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the refund object if the update succeeds. This call raises an error if update parameters are invalid.

[an error](#errors)

# Retrieve a refund

[Retrieve a refund](/api/refunds/retrieve)

Retrieves the details of an existing refund.

No parameters.

Returns a refund if you provide a valid ID. Raises an error otherwise.

[an error](#errors)

# List all refunds

[List all refunds](/api/refunds/list)

Returns a list of all refunds you created. We return the refunds in sorted order, with the most recent refunds appearing first The 10 most recent refunds are always available by default on the Charge object.

- chargestringOnly return refunds for the charge specified by this charge ID.

Only return refunds for the charge specified by this charge ID.

- payment_intentstringOnly return refunds for the PaymentIntent specified by this ID.

Only return refunds for the PaymentIntent specified by this ID.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit refunds, starting after the starting_after refund. Each entry in the array is a separate Refund object. If no other refunds are available, the resulting array is empty. If you provide a non-existent charge ID, this call raises an error.

[an error](#errors)

# Cancel a refund

[Cancel a refund](/api/refunds/cancel)

Cancels a refund with a status of requires_action.

You can’t cancel refunds in other states. Only refunds for payment methods that require customer action can enter the requires_action state.

No parameters.

Returns the refund object if the cancellation succeeds. This call raises an error if you can’t cancel the refund.

[an error](#errors)
