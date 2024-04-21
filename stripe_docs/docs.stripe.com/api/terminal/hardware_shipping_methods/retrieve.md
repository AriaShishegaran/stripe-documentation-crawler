- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve a Terminal Hardware Shipping MethodPreview feature

[Retrieve a Terminal Hardware Shipping Method](/api/terminal/hardware_shipping_methods/retrieve)

Retrieves a TerminalHardwareShippingMethod object.

No parameters.

Returns a TerminalHardwareShippingMethod object if a valid identifier was provided.

# List all Terminal Hardware Shipping MethodsPreview feature

[List all Terminal Hardware Shipping Methods](/api/terminal/hardware_shipping_methods/list)

List all TerminalHardwareShippingMethod objects.

- countrystringOnly return Shipping Methods that have the given country. If provided, country must be a two-letter country code (ISO 3166-1 alpha-2).

Only return Shipping Methods that have the given country. If provided, country must be a two-letter country code (ISO 3166-1 alpha-2).

[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- nameenumOnly return Shipping Methods that have the given name.Possible enum valuesexpressExpresspriorityPrioritystandardStandard

Only return Shipping Methods that have the given name.

Express

Priority

Standard

- statusenumOnly return Shipping Methods that have the given status. Defaults to Available.Possible enum valuesavailableAvailable for new orders.unavailableCan no longer be used for order creation.

Only return Shipping Methods that have the given status. Defaults to Available.

Available for new orders.

Can no longer be used for order creation.

A dictionary with a data property that contains an array of terminal hardware shipping methods. Each entry in the array is a separate ShippingMethod object.

# Configuration

[Configuration](/api/terminal/configuration)

A Configurations object represents how features should be configured for terminal readers.

[POST/v1/terminal/configurations](/api/terminal/configuration/create)

[POST/v1/terminal/configurations/:id](/api/terminal/configuration/update)

[GET/v1/terminal/configurations/:id](/api/terminal/configuration/retrieve)

[GET/v1/terminal/configurations](/api/terminal/configuration/list)

[DELETE/v1/terminal/configurations/:id](/api/terminal/configuration/delete)

Show

# Financial Accounts

[Financial Accounts](/api/treasury/financial_accounts)

Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance. FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.

[POST/v1/treasury/financial_accounts](/api/treasury/financial_accounts/create)

[POST/v1/treasury/financial_accounts/:id](/api/treasury/financial_accounts/update)

[GET/v1/treasury/financial_accounts/:id](/api/treasury/financial_accounts/retrieve)

[GET/v1/treasury/financial_accounts](/api/treasury/financial_accounts/list)

Show

# Financial Account Features

[Financial Account Features](/api/treasury/financial_account_features)

Encodes whether a FinancialAccount has access to a particular Feature, with a status enum and associated status_details. Stripe or the platform can control Features via the requested field.

[POST/v1/treasury/financial_accounts/:id/features](/api/treasury/financial_account_features/update)

[GET/v1/treasury/financial_accounts/:id/features](/api/treasury/financial_account_features/retrieve)

Show

# Transactions

[Transactions](/api/treasury/transactions)

Transactions represent changes to a FinancialAccount’s balance.

[FinancialAccount’s](#financial_accounts)

[GET/v1/treasury/transactions/:id](/api/treasury/transactions/retrieve)

[GET/v1/treasury/transactions](/api/treasury/transactions/list)

Show

# Transaction Entries

[Transaction Entries](/api/treasury/transaction_entries)

TransactionEntries represent individual units of money movements within a single Transaction.

[Transaction](#transactions)

[GET/v1/treasury/transaction_entries/:id](/api/treasury/transaction_entries/retrieve)

[GET/v1/treasury/transaction_entries](/api/treasury/transaction_entries/list)

Show

# Outbound Transfers

[Outbound Transfers](/api/treasury/outbound_transfers)

Use OutboundTransfers to transfer funds from a FinancialAccount to a PaymentMethod belonging to the same entity. To send funds to a different party, use OutboundPayments instead. You can send funds over ACH rails or through a domestic wire transfer to a user’s own external bank account.

[FinancialAccount](#financial_accounts)

[OutboundPayments](#outbound_payments)

Simulate OutboundTransfer state changes with the /v1/test_helpers/treasury/outbound_transfers endpoints. These methods can only be called on test mode objects.

[POST/v1/treasury/outbound_transfers](/api/treasury/outbound_transfers/create)

[GET/v1/treasury/outbound_transfers/:id](/api/treasury/outbound_transfers/retrieve)

[GET/v1/treasury/outbound_transfers](/api/treasury/outbound_transfers/list)

[POST/v1/treasury/outbound_transfers/:id/cancel](/api/treasury/outbound_transfers/cancel)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/fail](/api/treasury/outbound_transfers/test_mode_fail)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/post](/api/treasury/outbound_transfers/test_mode_post)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/return](/api/treasury/outbound_transfers/test_mode_return)

Show

# Outbound Payments

[Outbound Payments](/api/treasury/outbound_payments)

Use OutboundPayments to send funds to another party’s external bank account or FinancialAccount. To send money to an account belonging to the same user, use an OutboundTransfer.

[FinancialAccount](#financial_accounts)

[OutboundTransfer](#outbound_transfers)

Simulate OutboundPayment state changes with the /v1/test_helpers/treasury/outbound_payments endpoints. These methods can only be called on test mode objects.

[POST/v1/treasury/outbound_payments](/api/treasury/outbound_payments/create)

[GET/v1/treasury/outbound_payments/:id](/api/treasury/outbound_payments/retrieve)

[GET/v1/treasury/outbound_payments](/api/treasury/outbound_payments/list)

[POST/v1/treasury/outbound_payments/:id/cancel](/api/treasury/outbound_payments/cancel)

[POST/v1/test_helpers/treasury/outbound_payments/:id/fail](/api/treasury/outbound_payments/test_mode_fail)

[POST/v1/test_helpers/treasury/outbound_payments/:id/post](/api/treasury/outbound_payments/test_mode_post)

[POST/v1/test_helpers/treasury/outbound_payments/:id/return](/api/treasury/outbound_payments/test_mode_return)

Show

# Inbound Transfers

[Inbound Transfers](/api/treasury/inbound_transfers)

Use InboundTransfers to add funds to your FinancialAccount via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

[InboundTransfers](/treasury/moving-money/financial-accounts/into/inbound-transfers)

[FinancialAccount](#financial_accounts)

[POST/v1/treasury/inbound_transfers](/api/treasury/inbound_transfers/create)

[GET/v1/treasury/inbound_transfers/:id](/api/treasury/inbound_transfers/retrieve)

[GET/v1/treasury/inbound_transfers](/api/treasury/inbound_transfers/list)

[POST/v1/treasury/inbound_transfers/:id/cancel](/api/treasury/inbound_transfers/cancel)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/fail](/api/treasury/inbound_transfers/test_mode_fail)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/return](/api/treasury/inbound_transfers/test_mode_return)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/succeed](/api/treasury/inbound_transfers/test_mode_succeed)

Show

# Received Credits

[Received Credits](/api/treasury/received_credits)

ReceivedCredits represent funds sent to a FinancialAccount (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

[FinancialAccount](#financial_accounts)

[GET/v1/treasury/received_credits/:id](/api/treasury/received_credits/retrieve)

[GET/v1/treasury/received_credits](/api/treasury/received_credits/list)

[POST/v1/test_helpers/treasury/received_credits](/api/treasury/received_credits/test_mode_create)

Show

# Received Debits

[Received Debits](/api/treasury/received_debits)

ReceivedDebits represent funds pulled from a FinancialAccount. These are not initiated from the FinancialAccount.

[FinancialAccount](#financial_accounts)

[GET/v1/treasury/received_debits/:id](/api/treasury/received_debits/retrieve)

[GET/v1/treasury/received_debits](/api/treasury/received_debits/list)

[POST/v1/test_helpers/treasury/received_debits](/api/treasury/received_debits/test_mode_create)

Show

# Credit Reversals

[Credit Reversals](/api/treasury/credit_reversals)

You can reverse some ReceivedCredits depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.

[ReceivedCredits](#received_credits)

[POST/v1/treasury/credit_reversals](/api/treasury/credit_reversals/create)

[GET/v1/treasury/credit_reversals/:id](/api/treasury/credit_reversals/retrieve)

[GET/v1/treasury/credit_reversals](/api/treasury/credit_reversals/list)

Show

# Debit Reversals

[Debit Reversals](/api/treasury/debit_reversals)

You can reverse some ReceivedDebits depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

[ReceivedDebits](#received_debits)

[POST/v1/treasury/debit_reversals](/api/treasury/debit_reversals/create)

[GET/v1/treasury/debit_reversals/:id](/api/treasury/debit_reversals/retrieve)

[GET/v1/treasury/debit_reversals](/api/treasury/debit_reversals/list)

Show

# Feature

[Feature](/api/entitlements/feature)

A feature represents a monetizable ability or functionality in your system. Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.

[POST/v1/entitlements/features](/api/entitlements/feature/create)

[GET/v1/entitlements/features](/api/entitlements/feature/list)

[POST/v1/entitlements/features/:id](/api/entitlements/feature/updates)

Show

# Product Feature

[Product Feature](/api/product-feature)

A product_feature represents an attachment between a feature and a product. When a product is purchased that has a feature attached, Stripe will create an entitlement to the feature for the purchasing customer.

[GET/v1/products/:id/features](/api/product-feature/list)

[POST/v1/products/:id/features](/api/product-feature/attach)

[DELETE/v1/products/:id/features/:id](/api/product-feature/remove)

Show

# Active Entitlement

[Active Entitlement](/api/entitlements/active-entitlement)

An active entitlement describes access to a feature for a customer.

[GET/v1/entitlements/active_entitlements](/api/entitlements/active-entitlement/list)

Show

# Scheduled Queries

[Scheduled Queries](/api/sigma/scheduled_queries)

If you have scheduled a Sigma query, you’ll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.

[scheduled a Sigma query](/sigma/scheduled-queries)

[GET/v1/sigma/scheduled_query_runs/:id](/api/sigma/scheduled_queries/retrieve)

[GET/v1/sigma/scheduled_query_runs](/api/sigma/scheduled_queries/list)

Show

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
