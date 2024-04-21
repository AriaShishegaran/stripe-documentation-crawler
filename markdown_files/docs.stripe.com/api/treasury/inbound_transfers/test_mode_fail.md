htmlTest mode: Fail an InboundTransfer | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Test mode: Fail an InboundTransferTest helper

Transitions a test mode created InboundTransfer to the failed status. The InboundTransfer must already be in the processing state.

### Parameters

- failure_detailsobjectDetails about a failed InboundTransfer.

Show child parameters

### Returns

Returns the InboundTransfer object in the returned state. Returns an error if the InboundTransfer has already failed or cannot be failed.

POST/v1/test_helpers/treasury/inbound_transfers/:id/failServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/fail \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "failure_details[code]"=insufficient_funds`Response`{  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",  "object": "treasury.inbound_transfer",  "amount": 10000,  "cancelable": true,  "created": 1680716025,  "currency": "usd",  "description": "InboundTransfer from my external bank account",  "failure_details": {    "code": "insufficient_funds"  },  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgZ09q__wJA6NpPUfXQX0PUpgdTTpcHXdViKIK3-mEuzKM_CrltWFzRyKdq8OhPb6676H32JwPak4k0jonMLYA",  "linked_flows": {    "received_debit": null  },  "livemode": false,  "metadata": {},  "origin_payment_method": "pm_1MtaDN2eZvKYlo2CObQW5Wkv",  "origin_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "returned": false,  "statement_descriptor": "transfer",  "status": "failed",  "status_transitions": {    "failed_at": 1680716025,    "succeeded_at": null  },  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}`# Test mode: Return an InboundTransferTest helper

Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the succeeded state.

### Parameters

No parameters.

### Returns

Returns the InboundTransfer object with returned set to true. Returns an error if the InboundTransfer has already been returned or cannot be returned.

POST/v1/test_helpers/treasury/inbound_transfers/:id/returnServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/return \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",  "object": "treasury.inbound_transfer",  "amount": 10000,  "cancelable": true,  "created": 1680716025,  "currency": "usd",  "description": "InboundTransfer from my external bank account",  "failure_details": null,  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYvkdeXVp86NpNVlQmJPh28UZzYqO663FQJ4x3nf7tL4goXRt2IONIMvkuzcdxraW__iDMg9Uijq8tP1PcUbA",  "linked_flows": {    "received_debit": "rd_1MtaDN2eZvKYlo2ChwXbpRWa"  },  "livemode": false,  "metadata": {},  "origin_payment_method": "pm_1MtaDN2eZvKYlo2CObQW5Wkv",  "origin_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "returned": true,  "statement_descriptor": "transfer",  "status": "succeeded",  "status_transitions": {    "failed_at": null,    "succeeded_at": 1680716025  },  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}`# Test mode: Succeed an InboundTransferTest helper

Transitions a test mode created InboundTransfer to the succeeded status. The InboundTransfer must already be in the processing state.

### Parameters

No parameters.

### Returns

Returns the InboundTransfer object in the succeeded state. Returns an error if the InboundTransfer has already succeeded or cannot be succeeded.

POST/v1/test_helpers/treasury/inbound_transfers/:id/succeedServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/succeed \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",  "object": "treasury.inbound_transfer",  "amount": 10000,  "cancelable": true,  "created": 1680716025,  "currency": "usd",  "description": "InboundTransfer from my external bank account",  "failure_details": null,  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYVxjWLYpw6NpP6LLdBjWjsgc_5Q68S_eJDtpmsSgc_rHslxhpX2qqP0Xqb3fb3uLR2h-INgqgg7E81-mu1FQ",  "linked_flows": {    "received_debit": null  },  "livemode": false,  "metadata": {},  "origin_payment_method": "pm_1MtaDN2eZvKYlo2CObQW5Wkv",  "origin_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "returned": false,  "statement_descriptor": "transfer",  "status": "succeeded",  "status_transitions": {    "failed_at": null,    "succeeded_at": 1680716025  },  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}`# Received Credits

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