- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Scheduled Query object

[The Scheduled Query object](/api/sigma/scheduled_queries/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- data_load_timetimestampWhen the query was run, Sigma contained a snapshot of your Stripe data at this time.

When the query was run, Sigma contained a snapshot of your Stripe data at this time.

- filenullable objectThe file object representing the results of the query.Show child attributes

The file object representing the results of the query.

- sqlstringSQL for the query.

SQL for the query.

- statusstringThe query’s execution status, which will be completed for successful runs, and canceled, failed, or timed_out otherwise.

The query’s execution status, which will be completed for successful runs, and canceled, failed, or timed_out otherwise.

- titlestringTitle of the query.

Title of the query.

- objectstring

- createdtimestamp

- errornullable object

- livemodeboolean

- result_available_untiltimestamp

# Retrieve a scheduled query run

[Retrieve a scheduled query run](/api/sigma/scheduled_queries/retrieve)

Retrieves the details of an scheduled query run.

No parameters.

Returns the scheduled query run object if a valid identifier was provided.

# List all scheduled query runs

[List all scheduled query runs](/api/sigma/scheduled_queries/list)

Returns a list of scheduled query runs.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A paginated list of all scheduled query runs.

# Report Runs

[Report Runs](/api/reporting/report_run)

The Report Run object represents an instance of a report type generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to a file where you can retrieve your results. For an overview, see API Access to Reports.

[API Access to Reports](/reporting/statements/api)

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

[live-mode API key](/keys#test-live-modes)

[POST/v1/reporting/report_runs](/api/reporting/report_run/create)

[GET/v1/reporting/report_runs/:id](/api/reporting/report_run/retrieve)

[GET/v1/reporting/report_runs](/api/reporting/report_run/list)

Show

# Report Types

[Report Types](/api/reporting/report_type)

The Report Type resource corresponds to a particular type of report, such as the “Activity summary” or “Itemized payouts” reports. These objects are identified by an ID belonging to a set of enumerated values. See API Access to Reports documentation for those Report Type IDs, along with required and optional parameters.

[API Access to Reports documentation](/reporting/statements/api)

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

[live-mode API key](/keys#test-live-modes)

[GET/v1/reporting/report_types/:id](/api/reporting/report_type/retrieve)

[GET/v1/reporting/report_types](/api/reporting/report_type/list)

Show

# Accounts

[Accounts](/api/financial_connections/accounts)

A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

[GET/v1/financial_connections/accounts/:id](/api/financial_connections/accounts/retrieve)

[GET/v1/financial_connections/accounts](/api/financial_connections/accounts/list)

[POST/v1/financial_connections/accounts/:id/disconnect](/api/financial_connections/accounts/disconnect)

[POST/v1/financial_connections/accounts/:id/refresh](/api/financial_connections/accounts/refresh)

[POST/v1/financial_connections/accounts/:id/subscribe](/api/financial_connections/accounts/subscribe)

[POST/v1/financial_connections/accounts/:id/unsubscribe](/api/financial_connections/accounts/unsubscribe)

Show

# Account Owner

[Account Owner](/api/financial_connections/ownership)

Describes an owner of an account.

[GET/v1/financial_connections/accounts/:id/owners](/api/financial_connections/ownership/list)

Show

# Session

[Session](/api/financial_connections/sessions)

A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.

[POST/v1/financial_connections/sessions](/api/financial_connections/sessions/create)

[GET/v1/financial_connections/sessions/:id](/api/financial_connections/sessions/retrieve)

Show

# Transactions

[Transactions](/api/financial_connections/transactions)

A Transaction represents a real transaction that affects a Financial Connections Account balance.

[GET/v1/financial_connections/transactions/:id](/api/financial-connections/transaction/retrieve)

[GET/v1/financial_connections/transactions](/api/financial_connections/transactions/list)

Show

# Tax Calculations

[Tax Calculations](/api/tax/calculations)

A Tax Calculation allows you to calculate the tax to collect from your customer.

Related guide: Calculate tax in your custom payment flow

[Calculate tax in your custom payment flow](/tax/custom)

[GET/v1/tax/calculations/:id/line_items](/api/tax/calculations/line_items)

[POST/v1/tax/calculations](/api/tax/calculations/create)

Show

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
