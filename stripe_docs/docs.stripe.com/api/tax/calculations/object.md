- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Tax Calculation object

[The Tax Calculation object](/api/tax/calculations/object)

- idnullable stringUnique identifier for the calculation.

Unique identifier for the calculation.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- amount_totalintegerTotal after taxes.

Total after taxes.

- currencystringThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customer_detailsobjectThe customer’s details, such as address and tax IDs.Show child attributes

The customer’s details, such as address and tax IDs.

- expires_atnullable timestampTimestamp of date at which the tax calculation will expire.

Timestamp of date at which the tax calculation will expire.

- line_itemsnullable objectExpandableThe list of items the customer is purchasing.Show child attributes

The list of items the customer is purchasing.

- shipping_costnullable objectThe shipping cost details for the calculation.Show child attributes

The shipping cost details for the calculation.

- tax_amount_exclusiveintegerThe amount of tax to be collected on top of the line item prices.

The amount of tax to be collected on top of the line item prices.

- tax_amount_inclusiveintegerThe amount of tax already included in the line item prices.

The amount of tax already included in the line item prices.

- tax_breakdownarray of objectsBreakdown of individual tax amounts that add up to the total.Show child attributes

Breakdown of individual tax amounts that add up to the total.

- customernullable string

- livemodeboolean

- tax_datetimestamp

# Retrieve a calculation's line items

[Retrieve a calculation's line items](/api/tax/calculations/line_items)

Retrieves the line items of a persisted tax calculation as a collection.

- ending_beforestringA cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.

A cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- starting_afterstringA cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.

A cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.

A list of Line Item objects if the Tax calculation is found. Otherwise returns a ‘not found’ error.

# Calculate tax

[Calculate tax](/api/tax/calculations/create)

Calculates tax based on input and returns a Tax Calculation object.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- line_itemsarray of objectsRequiredA list of items the customer is purchasing.Show child parameters

A list of items the customer is purchasing.

- customer_detailsobjectRequired unless customer providedDetails about the customer, including address and tax IDs.Show child parameters

Details about the customer, including address and tax IDs.

- shipping_costobjectShipping cost details to be used for the calculation.Show child parameters

Shipping cost details to be used for the calculation.

- customerstringRequired unless customer_details provided

- tax_dateinteger

A Tax Calculation object if calculation succeeds. Otherwise, an error (for example, indicating that the customer address was invalid).

# Tax Registrations

[Tax Registrations](/api/tax/registrations)

A Tax Registration lets us know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax.

[automatically collect tax](/tax)

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax Registration object. For more information on how to register to collect tax, see our guide.

[our guide](/tax/registering)

Related guide: Using the Registrations API

[Using the Registrations API](/tax/registrations-api)

[POST/v1/tax/registrations](/api/tax/registrations/create)

[POST/v1/tax/registrations/:id](/api/tax/registrations/update)

[GET/v1/tax/registrations/:id](/api/tax/registrations/retrieve)

[GET/v1/tax/registrations](/api/tax/registrations/all)

Show

# Tax Transactions

[Tax Transactions](/api/tax/transactions)

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: Calculate tax in your custom payment flow

[Calculate tax in your custom payment flow](/tax/custom#tax-transaction)

[POST/v1/tax/transactions/create_reversal](/api/tax/transactions/create_reversal)

[POST/v1/tax/transactions/create_from_calculation](/api/tax/transactions/create_from_calculation)

[GET/v1/tax/transactions/:id/line_items](/api/tax/transactions/line_items)

[GET/v1/tax/transactions/:id](/api/tax/transactions/retrieve)

Show

# Tax Settings

[Tax Settings](/api/tax/settings)

You can use Tax Settings to manage configurations used by Stripe Tax calculations.

Related guide: Using the Settings API

[Using the Settings API](/tax/settings-api)

[POST/v1/tax/settings](/api/tax/settings/update)

[GET/v1/tax/settings](/api/tax/settings/retrieve)

Show

# Verification Session

[Verification Session](/api/identity/verification_sessions)

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

[verification check](/identity/verification-checks)

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

[multiple statuses](/identity/how-sessions-work)

Related guide: The Verification Sessions API

[The Verification Sessions API](/identity/verification-sessions)

[POST/v1/identity/verification_sessions](/api/identity/verification_sessions/create)

[POST/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/update)

[GET/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/retrieve)

[GET/v1/identity/verification_sessions](/api/identity/verification_sessions/list)

[POST/v1/identity/verification_sessions/:id/cancel](/api/identity/verification_sessions/cancel)

[POST/v1/identity/verification_sessions/:id/redact](/api/identity/verification_sessions/redact)

Show

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

Show

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
