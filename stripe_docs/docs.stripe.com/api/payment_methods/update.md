- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Update a PaymentMethod

[Update a PaymentMethod](/api/payment_methods/update)

Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.

- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.Show child parameters

Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- allow_redisplayenum

- cardobject

- linkobject

- us_bank_accountobject

Returns a PaymentMethod object.

# Retrieve a Customer's PaymentMethod

[Retrieve a Customer's PaymentMethod](/api/payment_methods/customer)

Retrieves a PaymentMethod object for a given Customer.

No parameters.

Returns a PaymentMethod object.

# Retrieve a PaymentMethod

[Retrieve a PaymentMethod](/api/payment_methods/retrieve)

Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use Retrieve a Customer’s PaymentMethods

[Retrieve a Customer’s PaymentMethods](/api/payment_methods/customer)

No parameters.

Returns a PaymentMethod object.

# List a Customer's PaymentMethods

[List a Customer's PaymentMethods](/api/payment_methods/customer_list)

Returns a list of PaymentMethods for a given Customer

- typeenumAn optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

An optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

- allow_redisplayenum

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit PaymentMethods of type type, starting after PaymentMethods starting_after. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.

# List PaymentMethods

[List PaymentMethods](/api/payment_methods/list)

Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the List a Customer’s PaymentMethods API instead.

[List a Customer’s PaymentMethods](/api/payment_methods/customer_list)

- typeenumAn optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

An optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

- customerstring

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit PaymentMethods of type type, starting after PaymentMethods starting_after. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.
