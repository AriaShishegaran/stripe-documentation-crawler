htmlOutbound Payments | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Outbound Payments

Use OutboundPayments to send funds to another party’s external bank account or FinancialAccount. To send money to an account belonging to the same user, use an OutboundTransfer.

Simulate OutboundPayment state changes with the /v1/test_helpers/treasury/outbound_payments endpoints. These methods can only be called on test mode objects.

Endpoints
# The Outbound Payment object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- amountintegerAmount (in cents) transferred.


- cancelablebooleanReturns true if the object can be canceled, and false otherwise.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customernullablestringID of the customer to whom an OutboundPayment is sent.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- destination_payment_methodnullablestringThe PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using destination_payment_method_data.


- destination_payment_method_detailsnullableobjectDetails about the PaymentMethod for an OutboundPayment.

Show child attributes
- end_user_detailsnullableobjectDetails about the end user.

Show child attributes
- expected_arrival_datetimestampThe date when funds are expected to arrive in the destination account.


- financial_accountstringThe FinancialAccount that funds were pulled from.


- hosted_regulatory_receipt_urlnullablestringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- returned_detailsnullableobjectDetails about a returned OutboundPayment. Only set when the status is returned.

Show child attributes
- statement_descriptorstringThe description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).


- statusenumCurrent status of the OutboundPayment: processing, failed, posted, returned, canceled. An OutboundPayment is processing if it has been created and is pending. The status changes to posted once the OutboundPayment has been “confirmed” and funds have left the account, or to failed or canceled. If an OutboundPayment fails to arrive at its destination, its status will change to returned.


- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.

Show child attributes
- transactionstringExpandableThe Transaction associated with this object.



The Outbound Payment object`{  "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",  "object": "treasury.outbound_payment",  "amount": 10000,  "cancelable": false,  "created": 1680716009,  "currency": "usd",  "customer": "cus_4QFOF3xrvBT2nU",  "description": "OutboundPayment to a 3rd party",  "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",  "destination_payment_method_details": {    "type": "us_bank_account",    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"  },  "end_user_details": {    "ip_address": null,    "present": false  },  "expected_arrival_date": 1680716009,  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",  "livemode": false,  "metadata": {},  "returned_details": null,  "statement_descriptor": "payment",  "status": "processing",  "status_transitions": {    "canceled_at": null,    "failed_at": null,    "posted_at": null,    "returned_at": null  },  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"}`# Create an OutboundPayment

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

GET/v1/treasury/outbound_paymentsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/outbound_payments \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtaD72eZvKYlo2CYKM3DnUI \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/outbound_payments",  "has_more": false,  "data": [    {      "id": "obp_1MtaD72eZvKYlo2Cu5d5S1kX",      "object": "treasury.outbound_payment",      "amount": 10000,      "cancelable": false,      "created": 1680716009,      "currency": "usd",      "customer": "cus_4QFOF3xrvBT2nU",      "description": "OutboundPayment to a 3rd party",      "destination_payment_method": "pm_1MtaD82eZvKYlo2CtGr4OxTt",      "destination_payment_method_details": {        "type": "us_bank_account",        "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"      },      "end_user_details": {        "ip_address": null,        "present": false      },      "expected_arrival_date": 1680716009,      "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYgdA-GrKk6NZNsf-FXPEqqbHm44fwJ57pNybbkweviYUDJGYFOw4f9cAqpfvPKQZ6y0S2C5DYyRwmDs_36",      "livemode": false,      "metadata": {},      "returned_details": null,      "statement_descriptor": "payment",      "status": "processing",      "status_transitions": {        "canceled_at": null,        "failed_at": null,        "posted_at": null,        "returned_at": null      },      "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`