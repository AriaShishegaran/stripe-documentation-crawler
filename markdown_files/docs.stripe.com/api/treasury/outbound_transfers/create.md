htmlCreate an OutboundTransfer | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create an OutboundTransfer

Creates an OutboundTransfer.

### Parameters

- amountintegerRequiredAmount (in cents) to be transferred.


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- financial_accountstringRequiredThe FinancialAccount to pull funds from.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- destination_payment_methodstringThe PaymentMethod to use as the payment instrument for the OutboundTransfer.


- destination_payment_method_optionsobjectHash describing payment method configuration details.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statement_descriptorstringStatement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for ach transfers or 140 characters for us_domestic_wire transfers. The default value is “transfer”.



### Returns

Returns an OutboundTransfer object if there were no issues with OutboundTransfer creation. The status of the created OutboundTransfer object is initially marked as processing.

POST/v1/treasury/outbound_transfersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/outbound_transfers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1 \  -d destination_payment_method=pm_1234567890 \  -d amount=500 \  -d currency=usd \  -d description="OutboundTransfer to my external bank account"`Response`{  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",  "object": "treasury.outbound_transfer",  "amount": 500,  "cancelable": true,  "created": 1680717489,  "currency": "usd",  "description": "OutboundTransfer to my external bank account",  "destination_payment_method": "pm_1234567890",  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "expected_arrival_date": 1680825600,  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "transfer",  "status": "processing",  "status_transitions": {    "canceled_at": null,    "failed_at": null,    "posted_at": null,    "returned_at": null  },  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}`# Retrieve an OutboundTransfer

Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.

### Parameters

No parameters.

### Returns

Returns an OutboundTransfer object if a valid identifier was provided. Otherwise, returns an error.

GET/v1/treasury/outbound_transfers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",  "object": "treasury.outbound_transfer",  "amount": 500,  "cancelable": true,  "created": 1680717489,  "currency": "usd",  "description": "OutboundTransfer to my external bank account",  "destination_payment_method": "pm_1234567890",  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "expected_arrival_date": 1680825600,  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "transfer",  "status": "processing",  "status_transitions": {    "canceled_at": null,    "failed_at": null,    "posted_at": null,    "returned_at": null  },  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}`# List all OutboundTransfers

Returns a list of OutboundTransfers sent from the specified FinancialAccount.

### Parameters

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.


- statusenumOnly return OutboundTransfers that have the given status: processing, canceled, failed, posted, or returned.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit OutboundTransfers, starting after OutboundTransfer starting_after. Each entry in the array is a separate OutboundTransfer object. If no more OutboundTransfers are available, the resulting array is empty.

GET/v1/treasury/outbound_transfersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/outbound_transfers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3 \  -d financial_account=fa_1Mtaaz2eZvKYlo2CUf56sIA1`Response`{  "object": "list",  "url": "/v1/treasury/outbound_transfers",  "has_more": false,  "data": [    {      "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",      "object": "treasury.outbound_transfer",      "amount": 500,      "cancelable": true,      "created": 1680717489,      "currency": "usd",      "description": "OutboundTransfer to my external bank account",      "destination_payment_method": "pm_1234567890",      "destination_payment_method_details": {        "billing_details": {          "address": {            "city": "San Francisco",            "country": "US",            "line1": "1234 Fake Street",            "line2": null,            "postal_code": "94102",            "state": "CA"          },          "email": null,          "name": "Jane Austen"        },        "type": "us_bank_account",        "us_bank_account": {          "account_holder_type": "company",          "account_type": "checking",          "bank_name": "STRIPE TEST BANK",          "fingerprint": "AP24Iso0btGp4N10",          "last4": "6789",          "network": "ach",          "routing_number": "110000000"        }      },      "expected_arrival_date": 1680825600,      "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYCCwVOvUY6NpO8ArWrjrz6Hxk3d8tQ4d_RvOqMTOeq6js5eE94-f-7DwBzjjD1wxIUhOyub1KFYH8QKxj9oA",      "livemode": false,      "metadata": {},      "returned_details": null,      "statement_descriptor": "transfer",      "status": "processing",      "status_transitions": {        "canceled_at": null,        "failed_at": null,        "posted_at": null,        "returned_at": null      },      "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"    }    {...}    {...}  ],}`# Cancel an OutboundTransfer

An OutboundTransfer can be canceled if the funds have not yet been paid out.

### Parameters

No parameters.

### Returns

Returns the OutboundTransfer object if the cancellation succeeded. Returns an error if the object has already been canceled or cannot be canceled.

POST/v1/treasury/outbound_transfers/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",  "object": "treasury.outbound_transfer",  "amount": 10000,  "cancelable": false,  "created": 1680717489,  "currency": "usd",  "description": "OutboundTransfer to my external bank account",  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "expected_arrival_date": 1680825600,  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgbFx5vTNec6NpPKphE93zYcPDgqrHcZhLW_fmKqG9Mu9HUNa_164u93bqkgnPNnYtd3_5Rv_F3YISrR2qg3FQ",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "transfer",  "status": "canceled",  "status_transitions": {    "posted_at": null,    "failed_at": null,    "canceled_at": 1680717489,    "returned_at": null  },  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}`# Test mode: Fail an OutboundTransferTest helper

Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.

### Parameters

No parameters.

### Returns

Returns the OutboundTransfer object in the failed state. Returns an error if the OutboundTransfer has already been failed or cannot be failed.

POST/v1/test_helpers/treasury/outbound_transfers/:id/failServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/fail \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",  "object": "treasury.outbound_transfer",  "amount": 10000,  "cancelable": false,  "created": 1680717489,  "currency": "usd",  "description": "OutboundTransfer to my external bank account",  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "expected_arrival_date": 1680825600,  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYw-nE9MNI6NpOJppCfj7fBzxZ9vepfiOLlViIJsILsSUiUv3teC30OLgOpgL7B0UBbYYtz0t7gi1a1WHo4Ew",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "transfer",  "status": "failed",  "status_transitions": {    "failed_at": 1680717489,    "canceled_at": null,    "posted_at": null,    "returned_at": null  },  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`