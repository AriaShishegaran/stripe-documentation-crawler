- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Forwarding RequestPreview feature

[Forwarding Request](/api/forwarding/request)

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

[Forward card details to third-party API endpoints](https://docs.stripe.com/payments/forwarding)

[POST/v1/forwarding/requests](/api/forwarding/forwarding_requests/create)

[GET/v1/forwarding/requests/:id](/api/forwarding/forwarding_requests/retrieve)

[GET/v1/forwarding/requests](/api/forwarding/forwarding_requests/list)

# The ForwardingRequest objectPreview feature

[The ForwardingRequest object](/api/forwarding/request/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- payment_methodstringThe PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.

The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.

- replacementsarray of enumsThe field kinds to be replaced in the forwarded request.Possible enum valuescard_cvcReplace the card cvc fieldcard_expiryReplace the card expiry fields like month and yearcard_numberReplace the card number fieldcardholder_nameReplace the cardholder name field

The field kinds to be replaced in the forwarded request.

Replace the card cvc field

Replace the card expiry fields like month and year

Replace the card number field

Replace the cardholder name field

- request_contextnullable objectContext about the request from Stripe’s servers to the destination endpoint.Show child attributes

Context about the request from Stripe’s servers to the destination endpoint.

- request_detailsnullable objectThe request that was sent to the destination endpoint. We redact any sensitive fields.Show child attributes

The request that was sent to the destination endpoint. We redact any sensitive fields.

- response_detailsnullable objectThe response that the destination endpoint returned to us. We redact any sensitive fields.Show child attributes

The response that the destination endpoint returned to us. We redact any sensitive fields.

- urlnullable stringThe destination URL for the forwarded request. Must be supported by the config.

The destination URL for the forwarded request. Must be supported by the config.

# Create a ForwardingRequest

[Create a ForwardingRequest](/api/forwarding/forwarding_requests/create)

Creates a ForwardingRequest object.

- payment_methodstringRequiredThe PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.

The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.

- replacementsarray of enumsRequiredThe field kinds to be replaced in the forwarded request.Possible enum valuescard_cvcReplace the card cvc fieldcard_expiryReplace the card expiry fields like month and yearcard_numberReplace the card number fieldcardholder_nameReplace the cardholder name field

The field kinds to be replaced in the forwarded request.

Replace the card cvc field

Replace the card expiry fields like month and year

Replace the card number field

Replace the cardholder name field

- requestobjectRequiredThe request body and headers to be sent to the destination endpoint.Show child parameters

The request body and headers to be sent to the destination endpoint.

- urlstringRequiredThe destination URL for the forwarded request. Must be supported by the config.

The destination URL for the forwarded request. Must be supported by the config.

Returns a ForwardingRequest object.

# Retrieve a ForwardingRequest

[Retrieve a ForwardingRequest](/api/forwarding/forwarding_requests/retrieve)

Retrieves a ForwardingRequest object.

No parameters.

Returns a ForwardingRequest object.

# List all ForwardingRequests

[List all ForwardingRequests](/api/forwarding/forwarding_requests/list)

Lists all ForwardingRequest objects.

- createdobjectSimilar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.Show child parameters

Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.

- ending_beforestringA pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.

A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- starting_afterstringA pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.

A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.

Returns a list of ForwardingRequest objects.
