- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Hand-off a PaymentIntent to a Reader and collect card detailsPreview feature

[Hand-off a PaymentIntent to a Reader and collect card details](/api/terminal/readers/collect_payment_method)

Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.

- payment_intentstringRequiredPaymentIntent ID

PaymentIntent ID

- collect_configobject

Returns an updated Reader resource.

# Hand-off a PaymentIntent to a Reader

[Hand-off a PaymentIntent to a Reader](/api/terminal/readers/process_payment_intent)

Initiates a payment flow on a Reader.

- payment_intentstringRequiredPaymentIntent ID

PaymentIntent ID

- process_configobject

Returns an updated Reader resource.

# Hand-off a SetupIntent to a Reader

[Hand-off a SetupIntent to a Reader](/api/terminal/readers/process_setup_intent)

Initiates a setup intent flow on a Reader.

- customer_consent_collectedbooleanRequiredCustomer Consent Collected

Customer Consent Collected

- setup_intentstringRequiredSetupIntent ID

SetupIntent ID

- process_configobject

Returns an updated Reader resource.

# Refund a Charge or a PaymentIntent in-person

[Refund a Charge or a PaymentIntent in-person](/api/terminal/readers/refund_payment)

Initiates a refund on a Reader

- amountintegerA positive integer in cents representing how much of this charge to refund.

A positive integer in cents representing how much of this charge to refund.

- chargestringID of the Charge to refund.

ID of the Charge to refund.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- payment_intentstringID of the PaymentIntent to refund.

ID of the PaymentIntent to refund.

- refund_application_feebooleanConnect onlyBoolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.

Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.

- reverse_transferbooleanConnect onlyBoolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.

Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.

- refund_payment_configobject

Returns an updated Reader resource

# Set reader display

[Set reader display](/api/terminal/readers/set_reader_display)

Sets reader display to show cart details.

- typeenumRequiredType

Type

- cartobjectCartShow child parameters

Cart

Returns an updated Reader resource.
