- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Verification Report

[Verification Report](/api/identity/verification_reports)

A VerificationReport is the result of an attempt to collect and verify data from a user. The collection of verification checks performed is determined from the type and options parameters used. You can find the result of each verification check performed in the appropriate sub-resource: document, id_number, selfie.

Each VerificationReport contains a copy of any data collected by the user as well as reference IDs which can be used to access collected images through the FileUpload API. To configure and create VerificationReports, use the VerificationSession API.

[FileUpload](/api/files)

[VerificationSession](/api/identity/verification_sessions)

Related guides: Accessing verification results.

[Accessing verification results](/identity/verification-sessions#results)

[GET/v1/identity/verification_reports/:id](/api/identity/verification_reports/retrieve)

[GET/v1/identity/verification_reports](/api/identity/verification_reports/list)

# The VerificationReport object

[The VerificationReport object](/api/identity/verification_reports/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- client_reference_idnullable stringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- documentnullable objectResult of the document check for this report.Show child attributes

Result of the document check for this report.

- id_numbernullable objectResult of the id number check for this report.Show child attributes

Result of the id number check for this report.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- optionsnullable objectConfiguration options for this report.Show child attributes

Configuration options for this report.

- selfienullable objectResult of the selfie check for this report.Show child attributes

Result of the selfie check for this report.

- typeenumType of report.Possible enum valuesdocumentPerform a document check.id_numberPerform an ID number check.

Type of report.

Perform a document check.

Perform an ID number check.

- verification_sessionnullable stringID of the VerificationSession that created this report.

ID of the VerificationSession that created this report.

# Retrieve a VerificationReport

[Retrieve a VerificationReport](/api/identity/verification_reports/retrieve)

Retrieves an existing VerificationReport

No parameters.

Returns a VerificationReport object

# List VerificationReports

[List VerificationReports](/api/identity/verification_reports/list)

List all verification reports.

- client_reference_idstringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- createdobjectOnly return VerificationReports that were created during the given date interval.Show child parameters

Only return VerificationReports that were created during the given date interval.

- typeenumOnly return VerificationReports of this typePossible enum valuesdocumentPerform a document check.id_numberPerform an ID number check.

Only return VerificationReports of this type

Perform a document check.

Perform an ID number check.

- verification_sessionstringOnly return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.

Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.

- ending_beforestring

- limitinteger

- starting_afterstring

List of VerificationInent objects that match the provided filter criteria.

# Crypto Onramp Session

[Crypto Onramp Session](/api/crypto/onramp_sessions)

A Crypto Onramp Session represents your customer’s session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user’s wallet and contain a reference to the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

Related guide: Integrate the onramp

[Integrate the onramp](/crypto/integrate-the-onramp)

[POST/v1/crypto/onramp_sessions](/api/crypto/onramp_sessions/create)

[GET/v1/crypto/onramp_sessions/:id](/api/crypto/onramp_sessions/retrieve)

[GET/v1/crypto/onramp_sessions](/api/crypto/onramp_sessions/list)

Show

# Crypto Onramp Quotes

[Crypto Onramp Quotes](/api/crypto/onramp_quotes)

Crypto Onramp Quotes are estimated quotes for onramp conversions into all the different cryptocurrencies on different networks. The Quotes API allows you to display quotes in your product UI before directing the user to the onramp widget.

Related guide: Quotes API

[Quotes API](/crypto/quotes-api)

[GET/v1/crypto/onramp/quotes](/api/crypto/onramp_quotes/retrieve)

Show

# Climate Order

[Climate Order](/api/climate/order)

Orders represent your intent to purchase a particular Climate product. When you create an order, the payment is deducted from your merchant balance.

[POST/v1/climate/orders](/api/climate/order/create)

[POST/v1/climate/orders/:id](/api/climate/order/update)

[GET/v1/climate/orders/:id](/api/climate/order/retrieve)

[GET/v1/climate/orders](/api/climate/order/list)

[POST/v1/climate/orders/:id/cancel](/api/climate/order/cancel)

Show

# Climate Product

[Climate Product](/api/climate/product)

A Climate product represents a type of carbon removal unit available for reservation. You can retrieve it to see the current price and availability.

[GET/v1/climate/products/:id](/api/climate/product/retrieve)

[GET/v1/climate/products](/api/climate/product/list)

Show

# Climate Supplier

[Climate Supplier](/api/climate/supplier)

A supplier of carbon removal.

[GET/v1/climate/suppliers/:id](/api/climate/supplier/retrieve)

[GET/v1/climate/suppliers](/api/climate/supplier/list)

Show

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

Show

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
