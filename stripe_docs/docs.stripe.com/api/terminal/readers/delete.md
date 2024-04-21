- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Delete a Reader

[Delete a Reader](/api/terminal/readers/delete)

Deletes a Reader object.

No parameters.

Returns the Reader object that was deleted.

# Cancel the current reader action

[Cancel the current reader action](/api/terminal/readers/cancel_action)

Cancels the current reader action.

No parameters.

Returns an updated Reader resource.

# Collect inputs using a ReaderPreview feature

[Collect inputs using a Reader](/api/terminal/readers/collect_inputs)

Initiates an input collection flow on a Reader.

- inputsarray of objectsRequiredList of inputs to be collected using the ReaderShow child parameters

List of inputs to be collected using the Reader

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns an updated Reader resource.

# Confirm a PaymentIntent on the ReaderPreview feature

[Confirm a PaymentIntent on the Reader](/api/terminal/readers/confirm_payment_intent)

Finalizes a payment on a Reader.

- payment_intentstringRequiredPaymentIntent ID

PaymentIntent ID

Returns an updated Reader resource.

# Hand-off a PaymentIntent to a Reader and collect card detailsPreview feature

[Hand-off a PaymentIntent to a Reader and collect card details](/api/terminal/readers/collect_payment_method)

Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.

- payment_intentstringRequiredPaymentIntent ID

PaymentIntent ID

- collect_configobject

Returns an updated Reader resource.
