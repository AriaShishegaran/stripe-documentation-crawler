htmlList all InboundTransfers | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# List all InboundTransfers

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

GET/v1/treasury/inbound_transfersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/inbound_transfers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtaDM2eZvKYlo2CvXrQknN4 \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/inbound_transfers",  "has_more": false,  "data": [    {      "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",      "object": "treasury.inbound_transfer",      "amount": 10000,      "cancelable": true,      "created": 1680716025,      "currency": "usd",      "description": "InboundTransfer from my bank account",      "failure_details": null,      "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYYdf7K2aE6NpN7tVDs9F1hxjKU9i3In9yfJWRBNJycDGlZZ22xgY_IuRs_jih19J4q6c4yUsv0SimaA57pww",      "linked_flows": {        "received_debit": null      },      "livemode": false,      "metadata": {},      "origin_payment_method": "pm_1KMDdkGPnV27VyGeAgGz8bsi",      "origin_payment_method_details": {        "billing_details": {          "address": {            "city": "San Francisco",            "country": "US",            "line1": "1234 Fake Street",            "line2": null,            "postal_code": "94102",            "state": "CA"          },          "email": null,          "name": "Jane Austen"        },        "type": "us_bank_account",        "us_bank_account": {          "account_holder_type": "company",          "account_type": "checking",          "bank_name": "STRIPE TEST BANK",          "fingerprint": "AP24Iso0btGp4N10",          "last4": "6789",          "network": "ach",          "routing_number": "110000000"        }      },      "returned": false,      "statement_descriptor": "transfer",      "status": "processing",      "status_transitions": {        "failed_at": null,        "succeeded_at": null      },      "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"    }    {...}    {...}  ],}`# Cancel an InboundTransfer

Cancels an InboundTransfer.

### Parameters

No parameters.

### Returns

Returns the InboundTransfer object if the cancellation succeeded. Returns an error if the InboundTransfer has already been canceled or cannot be canceled.

POST/v1/treasury/inbound_transfers/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",  "object": "treasury.inbound_transfer",  "amount": 10000,  "cancelable": false,  "created": 1680716025,  "currency": "usd",  "description": "InboundTransfer from my external bank account",  "failure_details": null,  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgZDF2WUT346NpP69bYKokqfNLTOb3qE8__DQL-vkc_p012AyYJYihh7UHvcsjvgXTDDkgEdUmHTimDXsAT0qA",  "linked_flows": {    "received_debit": null  },  "livemode": false,  "metadata": {},  "origin_payment_method": "pm_1MtaDN2eZvKYlo2CObQW5Wkv",  "origin_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "returned": false,  "statement_descriptor": "transfer",  "status": "canceled",  "status_transitions": {    "posted_at": null,    "failed_at": null,    "canceled_at": 1680716025,    "returned_at": null  },  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}`# Test mode: Fail an InboundTransferTest helper

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

POST/v1/test_helpers/treasury/inbound_transfers/:id/succeedServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/succeed \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",  "object": "treasury.inbound_transfer",  "amount": 10000,  "cancelable": true,  "created": 1680716025,  "currency": "usd",  "description": "InboundTransfer from my external bank account",  "failure_details": null,  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgYVxjWLYpw6NpP6LLdBjWjsgc_5Q68S_eJDtpmsSgc_rHslxhpX2qqP0Xqb3fb3uLR2h-INgqgg7E81-mu1FQ",  "linked_flows": {    "received_debit": null  },  "livemode": false,  "metadata": {},  "origin_payment_method": "pm_1MtaDN2eZvKYlo2CObQW5Wkv",  "origin_payment_method_details": {    "billing_details": {      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Fake Street",        "line2": null,        "postal_code": "94102",        "state": "CA"      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "account_holder_type": "company",      "account_type": "checking",      "bank_name": "STRIPE TEST BANK",      "fingerprint": "AP24Iso0btGp4N10",      "last4": "6789",      "network": "ach",      "routing_number": "110000000"    }  },  "returned": false,  "statement_descriptor": "transfer",  "status": "succeeded",  "status_transitions": {    "failed_at": null,    "succeeded_at": 1680716025  },  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`