htmlInbound Transfers | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Inbound Transfers

Use InboundTransfers to add funds to your FinancialAccount via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

Endpoints
# The InboundTransfer object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- amountintegerAmount (in cents) transferred.


- cancelablebooleanReturns true if the InboundTransfer is able to be canceled.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- failure_detailsnullableobjectDetails about this InboundTransfer’s failure. Only set when status is failed.

Show child attributes
- financial_accountstringThe FinancialAccount that received the funds.


- hosted_regulatory_receipt_urlnullablestringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.


- linked_flowsobjectOther flows linked to a InboundTransfer.

Show child attributes
- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- origin_payment_methodstringThe origin payment method to be debited for an InboundTransfer.


- origin_payment_method_detailsnullableobjectDetails about the PaymentMethod for an InboundTransfer.

Show child attributes
- returnednullablebooleanReturns true if the funds for an InboundTransfer were returned after the InboundTransfer went to the succeeded state.


- statement_descriptorstringStatement descriptor shown when funds are debited from the source. Not all payment networks support statement_descriptor.


- statusenumStatus of the InboundTransfer: processing, succeeded, failed, and canceled. An InboundTransfer is processing if it is created and pending. The status changes to succeeded once the funds have been “confirmed” and a transaction is created and posted. The status changes to failed if the transfer fails.


- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.

Show child attributes
- transactionnullablestringExpandableThe Transaction associated with this object.



# Create an InboundTransfer

Creates an InboundTransfer.

### Parameters

- amountintegerRequiredAmount (in cents) to be transferred.


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- financial_accountstringRequiredThe FinancialAccount to send funds to.


- origin_payment_methodstringRequiredThe origin payment method to be debited for the InboundTransfer.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statement_descriptorstringThe complete description that appears on your customers’ statements. Maximum 10 characters.



### Returns

Returns an InboundTransfer object if there were no issues with InboundTransfer creation. The status of the created InboundTransfer object is initially marked as processing.

POST/v1/treasury/inbound_transfersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/inbound_transfers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \  -d amount=10000 \  -d currency=usd \  -d origin_payment_method=pm_1KMDdkGPnV27VyGeAgGz8bsi \  -d description="InboundTransfer from my bank account"`Response`{  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",  "object": "treasury.inbound_transfer",  "amount": 10000,  "cancelable": true,  "created": 1680716025,  "currency": "usd",  "description": "InboundTransfer from my bank account",  "failure_details": null,  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww",  "linked_flows": {    "received_debit": null  },  "livemode": false,  "metadata": {},  "origin_payment_method": "pm_1KMDdkGPnV27VyGeAgGz8bsi",  "origin_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "returned": false,  "statement_descriptor": "transfer",  "status": "processing",  "status_transitions": {    "failed_at": null,    "succeeded_at": null  },  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}`# Retrieve an InboundTransfer

Retrieves the details of an existing InboundTransfer.

### Parameters

No parameters.

### Returns

Returns an InboundTransfer object if a valid identifier was provided. Otherwise, returns an error.

GET/v1/treasury/inbound_transfers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",  "object": "treasury.inbound_transfer",  "amount": 10000,  "cancelable": true,  "created": 1680716025,  "currency": "usd",  "description": "InboundTransfer from my bank account",  "failure_details": null,  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww",  "linked_flows": {    "received_debit": null  },  "livemode": false,  "metadata": {},  "origin_payment_method": "pm_1KMDdkGPnV27VyGeAgGz8bsi",  "origin_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "returned": false,  "statement_descriptor": "transfer",  "status": "processing",  "status_transitions": {    "failed_at": null,    "succeeded_at": null  },  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}`# List all InboundTransfers

Returns a list of InboundTransfers sent from the specified FinancialAccount.

### Parameters

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.


- statusenumOnly return InboundTransfers that have the given status: processing, succeeded, failed or canceled.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit InboundTransfers, starting after InboundTransfer starting_after. Each entry in the array is a separate InboundTransfer object. If no more InboundTransfers are available, the resulting array is empty.

GET/v1/treasury/inbound_transfersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/inbound_transfers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtaDM2eZvKYlo2CvXrQknN4 \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/inbound_transfers",  "has_more": false,  "data": [    {      "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",      "object": "treasury.inbound_transfer",      "amount": 10000,      "cancelable": true,      "created": 1680716025,      "currency": "usd",      "description": "InboundTransfer from my bank account",      "failure_details": null,      "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww",      "linked_flows": {        "received_debit": null      },      "livemode": false,      "metadata": {},      "origin_payment_method": "pm_1KMDdkGPnV27VyGeAgGz8bsi",      "origin_payment_method_details": {        "billing_details": {          "address": {            "city": "San Francisco",            "country": "US",            "line1": "1234 Fake Street",            "line2": null,            "postal_code": "94102",            "state": "CA"          },          "email": null,          "name": "Jane Austen"        },        "type": "us_bank_account",        "us_bank_account": {          "account_holder_type": "company",          "account_type": "checking",          "bank_name": "STRIPE TEST BANK",          "fingerprint": "AP24Iso0btGp4N10",          "last4": "6789",          "network": "ach",          "routing_number": "110000000"        }      },      "returned": false,      "statement_descriptor": "transfer",      "status": "processing",      "status_transitions": {        "failed_at": null,        "succeeded_at": null      },      "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`