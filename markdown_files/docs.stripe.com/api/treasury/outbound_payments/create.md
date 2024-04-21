htmlCreate an OutboundPayment | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create an OutboundPayment

Creates an OutboundPayment.

### Parameters

- amountintegerRequiredAmount (in cents) to be transferred.


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- financial_accountstringRequiredThe FinancialAccount to pull funds from.


- customerstringID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the destination_payment_method passed in.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- destination_payment_methodstringThe PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with destination_payment_method_data.


- destination_payment_method_dataobjectHash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with destination_payment_method.

Show child parameters
- destination_payment_method_optionsobjectPayment method-specific configuration for this OutboundPayment.

Show child parameters
- end_user_detailsobjectEnd user details.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statement_descriptorstringThe description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for ach payments, 140 characters for us_domestic_wire payments, or 500 characters for stripe network transfers. The default value is “payment”.



### Returns

Returns an OutboundPayment object if there were no issues with OutboundPayment creation.

POST/v1/treasury/outbound_paymentsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/outbound_payments \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \  -d amount=10000 \  -d currency=usd \  -d customer=cus_4QFOF3xrvBT2nU \  -d destination_payment_method=pm_1MtaD82eZvKYlo2Cn1XtS23o \  -d description="OutboundPayment to a 3rd party"`Response`{  "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",  "object": "treasury.outbound_payment",  "amount": 10000,  "cancelable": false,  "created": 1680716009,  "currency": "usd",  "customer": "cus_4QFOF3xrvBT2nU",  "description": "OutboundPayment to a 3rd party",  "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",  "destination_payment_method_details": {    "type": "us_bank_account",    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"  },  "end_user_details": {    "ip_address": null,    "present": false  },  "expected_arrival_date": 1680716009,  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "payment",  "status": "processing",  "status_transitions": {    "canceled_at": null,    "failed_at": null,    "posted_at": null,    "returned_at": null  },  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}`# Retrieve an OutboundPayment

Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.

### Parameters

No parameters.

### Returns

Returns an OutboundPayment object if a valid identifier was provided. Otherwise, returns an error.

GET/v1/treasury/outbound_payments/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/outbound_payments/obp_1MtaD72eZvKYlo2Cu5d5S1kX \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",  "object": "treasury.outbound_payment",  "amount": 10000,  "cancelable": false,  "created": 1680716009,  "currency": "usd",  "customer": "cus_4QFOF3xrvBT2nU",  "description": "OutboundPayment to a 3rd party",  "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",  "destination_payment_method_details": {    "type": "us_bank_account",    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"  },  "end_user_details": {    "ip_address": null,    "present": false  },  "expected_arrival_date": 1680716009,  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "payment",  "status": "processing",  "status_transitions": {    "canceled_at": null,    "failed_at": null,    "posted_at": null,    "returned_at": null  },  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}`# List all OutboundPayments

Returns a list of OutboundPayments sent from the specified FinancialAccount.

### Parameters

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.


- createdobjectOnly return OutboundPayments that were created during the given date interval.

Show child parameters
- customerstringOnly return OutboundPayments sent to this customer.


- statusenumOnly return OutboundPayments that have the given status: processing, failed, posted, returned, or canceled.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit OutboundPayments, starting after OutboundPayments starting_after. Each entry in the array is a separate OutboundPayments object. If no more OutboundPayments are available, the resulting array is empty.

GET/v1/treasury/outbound_paymentsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/outbound_payments \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/outbound_payments",  "has_more": false,  "data": [    {      "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",      "object": "treasury.outbound_payment",      "amount": 10000,      "cancelable": false,      "created": 1680716009,      "currency": "usd",      "customer": "cus_4QFOF3xrvBT2nU",      "description": "OutboundPayment to a 3rd party",      "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",      "destination_payment_method_details": {        "type": "us_bank_account",        "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"      },      "end_user_details": {        "ip_address": null,        "present": false      },      "expected_arrival_date": 1680716009,      "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",      "livemode": false,      "metadata": {},      "returned_details": null,      "statement_descriptor": "payment",      "status": "processing",      "status_transitions": {        "canceled_at": null,        "failed_at": null,        "posted_at": null,        "returned_at": null      },      "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"    }    {...}    {...}  ],}`# Cancel an OutboundPayment

Cancel an OutboundPayment.

### Parameters

No parameters.

### Returns

Returns the OutboundPayment object if the cancellation succeeded. Returns an error if the OutboundPayment has already been canceled or cannot be canceled.

POST/v1/treasury/outbound_payments/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/treasury/outbound_payments/obp_1MtaD72eZvKYlo2Cu5d5S1kX/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",  "object": "treasury.outbound_payment",  "amount": 10000,  "cancelable": false,  "created": 1680716009,  "currency": "usd",  "customer": null,  "description": "OutboundPayment to a 3rd party",  "destination_payment_method": null,  "destination_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": null    },    "financial_account": {      "id": "fa_1LpyM72eZvKYlo2CiUmr2kuV",      "network": "stripe"    },    "type": "financial_account"  },  "end_user_details": {    "ip_address": null,    "present": false  },  "expected_arrival_date": 1680716009,  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgakyczTzCY6NZMi6lMnZXTYms--WBYQzUXzaEJ_JwErEK5FXXW8F9Qy7fEzKvsHEOzyjS9AtIuK8sUjgWdU",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "payment",  "status": "canceled",  "status_transitions": {    "posted_at": null,    "failed_at": null,    "canceled_at": 1680716010,    "returned_at": null  },  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}`# Test mode: Fail an OutboundPaymentTest helper

Transitions a test mode created OutboundPayment to the failed status. The OutboundPayment must already be in the processing state.

### Parameters

No parameters.

### Returns

Returns the OutboundPayment object in the failed state. Returns an error if the OutboundPayment has already been failed or cannot be failed.

POST/v1/test_helpers/treasury/outbound_payments/:id/failServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_payments/obp_1MtaD72eZvKYlo2C36lgqC6Y/fail \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "obp_1MtaD72eZvKYlo2C36lgqC6Y",  "object": "treasury.outbound_payment",  "amount": 10000,  "cancelable": false,  "created": 1680716009,  "currency": "usd",  "customer": null,  "description": "OutboundPayment to a 3rd party",  "destination_payment_method": null,  "destination_payment_method_details": {    "type": "us_bank_account",    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"  },  "end_user_details": {    "ip_address": null,    "present": false  },  "expected_arrival_date": 1680716009,  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgbuLATJtPw6NZOxERTeGKynM40SUCL6A1sqeZF9vkrX4q4M0rI4eY7EhfkOVvyileEuRReLgXE2crXLg7sd",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "payment",  "status": "failed",  "status_transitions": {    "failed_at": 1680716010,    "posted_at": null,    "returned_at": null,    "canceled_at": null  },  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`