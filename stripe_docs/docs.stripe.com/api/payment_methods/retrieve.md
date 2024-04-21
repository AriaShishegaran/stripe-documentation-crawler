- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Attach a PaymentMethod to a Customer

[Attach a PaymentMethod to a Customer](/api/payment_methods/attach)

Attaches a PaymentMethod object to a Customer.

To attach a new PaymentMethod to a customer for future payments, we recommend you use a SetupIntent or a PaymentIntent with setup_future_usage. These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for future use, which makes later declines and payment friction more likely. See Optimizing cards for future payments for more information about setting up future payments.

[SetupIntent](/api/setup_intents)

[setup_future_usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

[Optimizing cards for future payments](/payments/payment-intents#future-usage)

To use this PaymentMethod as the default for invoice or subscription payments, set invoice_settings.default_payment_method, on the Customer to the PaymentMethod’s ID.

[invoice_settings.default_payment_method](/api/customers/update#update_customer-invoice_settings-default_payment_method)

- customerstringRequiredThe ID of the customer to which to attach the PaymentMethod.

The ID of the customer to which to attach the PaymentMethod.

Returns a PaymentMethod object.

# Detach a PaymentMethod from a Customer

[Detach a PaymentMethod from a Customer](/api/payment_methods/detach)

Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.

No parameters.

Returns a PaymentMethod object.
