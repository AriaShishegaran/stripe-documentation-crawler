htmlList all OutboundTransfers | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# List all OutboundTransfers

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

POST/v1/test_helpers/treasury/outbound_transfers/:id/failServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/fail \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",  "object": "treasury.outbound_transfer",  "amount": 10000,  "cancelable": false,  "created": 1680717489,  "currency": "usd",  "description": "OutboundTransfer to my external bank account",  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "expected_arrival_date": 1680825600,  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYw-nE9MNI6NpOJppCfj7fBzxZ9vepfiOLlViIJsILsSUiUv3teC30OLgOpgL7B0UBbYYtz0t7gi1a1WHo4Ew",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "transfer",  "status": "failed",  "status_transitions": {    "failed_at": 1680717489,    "canceled_at": null,    "posted_at": null,    "returned_at": null  },  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}`# Test mode: Post an OutboundTransferTest helper

Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.

### Parameters

No parameters.

### Returns

Returns the OutboundTransfer object in the posted state. Returns an error if the OutboundTransfer has already been posted or cannot be posted.

POST/v1/test_helpers/treasury/outbound_transfers/:id/postServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/post \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",  "object": "treasury.outbound_transfer",  "amount": 10000,  "cancelable": false,  "created": 1680717489,  "currency": "usd",  "description": "OutboundTransfer to my external bank account",  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "expected_arrival_date": 1680825600,  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYkJOwRj5U6NpOg9L70S_mhPE92VvJUt_P7rrE938uIHfjCSY3Bjn9Dufo8Z1h9709Gm-LmCbzT7a6j9kFN9w",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "transfer",  "status": "posted",  "status_transitions": {    "posted_at": 1680717489,    "failed_at": null,    "canceled_at": null,    "returned_at": null  },  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}`# Test mode: Return an OutboundTransferTest helper

Transitions a test mode created OutboundTransfer to the returned status. The OutboundTransfer must already be in the processing state.

### Parameters

- returned_detailsobjectDetails about a returned OutboundTransfer.

Show child parameters

### Returns

Returns the OutboundTransfer object in the returned state. Returns an error if the OutboundTransfer has already been returned or cannot be returned.

POST/v1/test_helpers/treasury/outbound_transfers/:id/returnServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/return \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",  "object": "treasury.outbound_transfer",  "amount": 10000,  "cancelable": false,  "created": 1680717489,  "currency": "usd",  "description": "OutboundTransfer to my external bank account",  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "expected_arrival_date": 1680825600,  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYdpKbb3Ec6NpO9f9jLUpJTCJGYDld0WR6lbibijEBPoyU4abErSxnN1ZB_JwosN4Krvqn2WLglRwEeAIzg4g",  "livemode": false,  "metadata": {},  "returned_details": {    "code": "declined",    "transaction": "trxn_1Mtaaz2eZvKYlo2CRvn5ac2X"  },  "statement_descriptor": "transfer",  "status": "returned",  "status_transitions": {    "returned_at": 1680717489,    "failed_at": null,    "canceled_at": null,    "posted_at": 1680717489  },  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`