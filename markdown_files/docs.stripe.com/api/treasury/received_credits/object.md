htmlThe ReceivedCredit object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The ReceivedCredit object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- amountintegerAmount (in cents) transferred.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- failure_codenullableenumReason for the failure. A ReceivedCredit might fail because the receiving FinancialAccount is closed or frozen.

Possible enum values`account_closed`Funds can’t be sent to a closed FinancialAccount.

`account_frozen`Funds can’t be sent to a frozen FinancialAccount.

`other`Funds can’t be sent to FinancialAccount for other reasons.


- financial_accountnullablestringThe FinancialAccount that received the funds.


- hosted_regulatory_receipt_urlnullablestringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.


- initiating_payment_method_detailsobjectDetails about the PaymentMethod used to send a ReceivedCredit.

Show child attributes
- linked_flowsobjectOther flows linked to a ReceivedCredit.

Show child attributes
- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- networkenumThe rails used to send the funds.

Possible enum values`ach``card``stripe``us_domestic_wire`
- reversal_detailsnullableobjectDetails describing when a ReceivedCredit may be reversed.

Show child attributes
- statusenumStatus of the ReceivedCredit. ReceivedCredits are created either succeeded (approved) or failed (declined). If a ReceivedCredit is declined, the failure reason can be found in the failure_code field.

Possible enum values`failed`The ReceivedCredit was declined, and no Transaction was created.

`succeeded`The ReceivedCredit was approved.


- transactionnullablestringExpandableThe Transaction associated with this object.



The ReceivedCredit object`{  "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",  "object": "treasury.received_credit",  "amount": 1000,  "created": 1680755425,  "currency": "usd",  "description": "Stripe Test",  "failure_code": null,  "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",  "initiating_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "bank_name": "STRIPE TEST BANK",      "last4": "6789",      "routing_number": "110000000"    }  },  "linked_flows": {    "credit_reversal": null,    "issuing_authorization": null,    "issuing_transaction": null,    "source_flow": null,    "source_flow_type": null  },  "livemode": false,  "network": "ach",  "reversal_details": {    "deadline": 1681084800,    "restricted_reason": null  },  "status": "succeeded",  "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}`# Retrieve a ReceivedCredit

Retrieves the details of an existing ReceivedCredit by passing the unique ReceivedCredit ID from the ReceivedCredit list.

### Parameters

No parameters.

### Returns

Returns a ReceivedCredit object.

GET/v1/treasury/received_credits/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/received_credits/rc_1MtkSr2eZvKYlo2CcysvUbEw \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",  "object": "treasury.received_credit",  "amount": 1000,  "created": 1680755425,  "currency": "usd",  "description": "Stripe Test",  "failure_code": null,  "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",  "initiating_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "bank_name": "STRIPE TEST BANK",      "last4": "6789",      "routing_number": "110000000"    }  },  "linked_flows": {    "credit_reversal": null,    "issuing_authorization": null,    "issuing_transaction": null,    "source_flow": null,    "source_flow_type": null  },  "livemode": false,  "network": "ach",  "reversal_details": {    "deadline": 1681084800,    "restricted_reason": null  },  "status": "succeeded",  "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}`# List all ReceivedCredits

Returns a list of ReceivedCredits.

### Parameters

- financial_accountstringRequiredThe FinancialAccount that received the funds.


- linked_flowsobjectOnly return ReceivedCredits described by the flow.

Show child parameters
- statusenumOnly return ReceivedCredits that have the given status: succeeded or failed.

Possible enum values`failed`The ReceivedCredit was declined, and no Transaction was created.

`succeeded`The ReceivedCredit was approved.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit ReceivedCredits, starting after ReceivedCredit starting_after. Each entry in the array is a separate ReceivedCredit object. If no more ReceivedCredits are available, the resulting array will be empty.

GET/v1/treasury/received_creditsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/received_credits \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/received_credits",  "has_more": false,  "data": [    {      "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",      "object": "treasury.received_credit",      "amount": 1000,      "created": 1680755425,      "currency": "usd",      "description": "Stripe Test",      "failure_code": null,      "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",      "initiating_payment_method_details": {        "billing_details": {          "address": {            "city": null,            "country": null,            "line1": null,            "line2": null,            "postal_code": null,            "state": null          },          "email": null,          "name": "Jane Austen"        },        "type": "us_bank_account",        "us_bank_account": {          "bank_name": "STRIPE TEST BANK",          "last4": "6789",          "routing_number": "110000000"        }      },      "linked_flows": {        "credit_reversal": null,        "issuing_authorization": null,        "issuing_transaction": null,        "source_flow": null,        "source_flow_type": null      },      "livemode": false,      "network": "ach",      "reversal_details": {        "deadline": 1681084800,        "restricted_reason": null      },      "status": "succeeded",      "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"    }    {...}    {...}  ],}`# Test mode: Create a ReceivedCreditTest helper

Use this endpoint to simulate a test mode ReceivedCredit initiated by a third party. In live mode, you can’t directly create ReceivedCredits initiated by third parties.

### Parameters

- amountintegerRequiredAmount (in cents) to be transferred.


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- financial_accountstringRequiredThe FinancialAccount to send funds to.


- networkenumRequiredSpecifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the docs to learn more about money movement timelines for each network type.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- initiating_payment_method_detailsobjectInitiating payment method details for the object.

Show child parameters

### Returns

A test mode ReceivedCredit object.

POST/v1/test_helpers/treasury/received_creditsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/treasury/received_credits \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1000 \  -d currency=usd \  -d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \  -d network=ach`Response`{  "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",  "object": "treasury.received_credit",  "amount": 1000,  "created": 1680755425,  "currency": "usd",  "description": "Stripe Test",  "failure_code": null,  "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",  "initiating_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "bank_name": "STRIPE TEST BANK",      "last4": "6789",      "routing_number": "110000000"    }  },  "linked_flows": {    "credit_reversal": null,    "issuing_authorization": null,    "issuing_transaction": null,    "source_flow": null,    "source_flow_type": null  },  "livemode": false,  "network": "ach",  "reversal_details": {    "deadline": 1681084800,    "restricted_reason": null  },  "status": "succeeded",  "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}`# Received Debits

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