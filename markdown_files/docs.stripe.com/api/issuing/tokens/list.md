htmlList all issuing tokens for card | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# List all issuing tokens for card

Lists all Issuing Token objects for a given card.

### Parameters

- cardstringRequiredThe Issuing card identifier to list tokens for.


- createdobjectOnly return Issuing tokens that were created during the given date interval.

Show child parameters
- statusenumSelect Issuing tokens with the given status.

Possible enum values`active`Token is provisioned and usable for payments.

`deleted`Terminal state. Token can no longer be used.

`requested`Token has been requested to be provisioned, but has not completed the activation process.

`suspended`Token temporarily cannot be used for payments.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit tokens, starting after token starting_after. Each entry in the array is a separate Issuing Token object. If no more tokens are available, the resulting array will be empty.

GET/v1/issuing/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/tokens \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3 \  -d card=ic_1MytUz2eZvKYlo2CZCn5fuvZ`Response`{  "object": "list",  "url": "/v1/issuing/tokens",  "has_more": false,  "data": [    {      "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",      "object": "issuing.token",      "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",      "created": 1682059060,      "network_updated_at": 1682059060,      "livemode": false,      "status": "suspended",      "last4": "2424",      "token_service_provider": "visa",      "wallet_provider": "apple_pay",      "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"    }    {...}    {...}  ],}`# Transactions

Any use of an issued card that results in funds entering or leaving your Stripe account, such as a completed purchase or refund, is represented by an Issuing Transaction object.

Related guide: Issued card transactions

Endpoints
Show

# Connection Token

A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

Related guide: Fleet management

Endpoints
Show

# Location

A Location represents a grouping of readers.

Related guide: Fleet management

Endpoints
Show

# Reader

A Reader represents a physical device for accepting payment details.

Related guide: Connecting to a reader

Endpoints
Show

# Terminal Hardware OrderPreview feature

A TerminalHardwareOrder represents an order for Terminal hardware, containing information such as the price, shipping information and the items ordered.

Endpoints
Show

# Terminal Hardware ProductPreview feature

A TerminalHardwareProduct is a category of hardware devices that are generally similar, but may have variations depending on the country it’s shipped to.

TerminalHardwareSKUs represent variations within the same Product (for example, a country specific device). For example, WisePOS E is a TerminalHardwareProduct and a WisePOS E - US and WisePOS E - UK are TerminalHardwareSKUs.

Endpoints
Show

# Terminal Hardware SKUPreview feature

A TerminalHardwareSKU represents a SKU for Terminal hardware. A SKU is a representation of a product available for purchase, containing information such as the name, price, and images.

Endpoints
Show

# Terminal Hardware Shipping MethodPreview feature

A TerminalHardwareShipping represents a Shipping Method for Terminal hardware. A Shipping Method is a country-specific representation of a way to ship hardware, containing information such as the country, name, and expected delivery date.

Endpoints
Show

# Configuration

A Configurations object represents how features should be configured for terminal readers.

Endpoints
Show

# Financial Accounts

Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance. FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.

Endpoints
Show

# Financial Account Features

Encodes whether a FinancialAccount has access to a particular Feature, with a status enum and associated status_details. Stripe or the platform can control Features via the requested field.

Endpoints
Show

# Transactions

Transactions represent changes to a FinancialAccount’s balance.

Endpoints
Show

# Transaction Entries

TransactionEntries represent individual units of money movements within a single Transaction.

Endpoints
Show

# Outbound Transfers

Use OutboundTransfers to transfer funds from a FinancialAccount to a PaymentMethod belonging to the same entity. To send funds to a different party, use OutboundPayments instead. You can send funds over ACH rails or through a domestic wire transfer to a user’s own external bank account.

Simulate OutboundTransfer state changes with the /v1/test_helpers/treasury/outbound_transfers endpoints. These methods can only be called on test mode objects.

Endpoints
Show

# Outbound Payments

Use OutboundPayments to send funds to another party’s external bank account or FinancialAccount. To send money to an account belonging to the same user, use an OutboundTransfer.

Simulate OutboundPayment state changes with the /v1/test_helpers/treasury/outbound_payments endpoints. These methods can only be called on test mode objects.

Endpoints
Show

# Inbound Transfers

Use InboundTransfers to add funds to your FinancialAccount via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

Endpoints
Show

# Received Credits

ReceivedCredits represent funds sent to a FinancialAccount (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

Endpoints
Show

# Received Debits

ReceivedDebits represent funds pulled from a FinancialAccount. These are not initiated from the FinancialAccount.

Endpoints
Show

# Credit Reversals

You can reverse some ReceivedCredits depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.

Endpoints
Show

# Debit Reversals

You can reverse some ReceivedDebits depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

Endpoints
Show

# Feature

A feature represents a monetizable ability or functionality in your system. Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.

Endpoints
Show

# Product Feature

A product_feature represents an attachment between a feature and a product. When a product is purchased that has a feature attached, Stripe will create an entitlement to the feature for the purchasing customer.

Endpoints
Show

# Active Entitlement

An active entitlement describes access to a feature for a customer.

Endpoints
Show

# Scheduled Queries

If you have scheduled a Sigma query, you’ll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.

Endpoints
Show

# Report Runs

The Report Run object represents an instance of a report type generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to a file where you can retrieve your results. For an overview, see API Access to Reports.

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

Endpoints
Show

# Report Types

The Report Type resource corresponds to a particular type of report, such as the “Activity summary” or “Itemized payouts” reports. These objects are identified by an ID belonging to a set of enumerated values. See API Access to Reports documentation for those Report Type IDs, along with required and optional parameters.

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

Endpoints
Show

# Accounts

A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

Endpoints
Show

# Account Owner

Describes an owner of an account.

Endpoints
Show

# Session

A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.

Endpoints
Show

# Transactions

A Transaction represents a real transaction that affects a Financial Connections Account balance.

Endpoints
Show

# Tax Calculations

A Tax Calculation allows you to calculate the tax to collect from your customer.

Related guide: Calculate tax in your custom payment flow

Endpoints
Show

# Tax Registrations

A Tax Registration lets us know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax.

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax Registration object. For more information on how to register to collect tax, see our guide.

Related guide: Using the Registrations API

Endpoints
Show

# Tax Transactions

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: Calculate tax in your custom payment flow

Endpoints
Show

# Tax Settings

You can use Tax Settings to manage configurations used by Stripe Tax calculations.

Related guide: Using the Settings API

Endpoints
Show

# Verification Session

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

Related guide: The Verification Sessions API

Endpoints
Show

# Verification Report

A VerificationReport is the result of an attempt to collect and verify data from a user. The collection of verification checks performed is determined from the type and options parameters used. You can find the result of each verification check performed in the appropriate sub-resource: document, id_number, selfie.

Each VerificationReport contains a copy of any data collected by the user as well as reference IDs which can be used to access collected images through the FileUpload API. To configure and create VerificationReports, use the VerificationSession API.

Related guides: Accessing verification results.

Endpoints
Show

# Crypto Onramp Session

A Crypto Onramp Session represents your customer’s session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user’s wallet and contain a reference to the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

Related guide: Integrate the onramp

Endpoints
Show

# Crypto Onramp Quotes

Crypto Onramp Quotes are estimated quotes for onramp conversions into all the different cryptocurrencies on different networks. The Quotes API allows you to display quotes in your product UI before directing the user to the onramp widget.

Related guide: Quotes API

Endpoints
Show

# Climate Order

Orders represent your intent to purchase a particular Climate product. When you create an order, the payment is deducted from your merchant balance.

Endpoints
Show

# Climate Product

A Climate product represents a type of carbon removal unit available for reservation. You can retrieve it to see the current price and availability.

Endpoints
Show

# Climate Supplier

A supplier of carbon removal.

Endpoints
Show

# Forwarding RequestPreview feature

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

Endpoints
Show

# Webhook Endpoints

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

Related guide: Setting up webhooks

Endpoints
Show

Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`