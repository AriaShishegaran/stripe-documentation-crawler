- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Webhook Endpoints

[Webhook Endpoints](/api/webhook_endpoints)

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

[webhook endpoints](/webhooks/)

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

[the dashboard](https://dashboard.stripe.com/webhooks)

Related guide: Setting up webhooks

[Setting up webhooks](/webhooks/configure)

[POST/v1/webhook_endpoints](/api/webhook_endpoints/create)

[POST/v1/webhook_endpoints/:id](/api/webhook_endpoints/update)

[GET/v1/webhook_endpoints/:id](/api/webhook_endpoints/retrieve)

[GET/v1/webhook_endpoints](/api/webhook_endpoints/list)

[DELETE/v1/webhook_endpoints/:id](/api/webhook_endpoints/delete)

Show
