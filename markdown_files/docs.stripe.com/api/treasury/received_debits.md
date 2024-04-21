htmlReceived Debits | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Received Debits

ReceivedDebits represent funds pulled from a FinancialAccount. These are not initiated from the FinancialAccount.

Endpoints
# The ReceivedDebit object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- amountintegerAmount (in cents) transferred.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- failure_codenullableenumReason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn’t have sufficient funds, is closed, or is frozen.

Possible enum values`account_closed`Funds can’t be pulled from a closed FinancialAccount.

`account_frozen`Funds can’t be pulled from a frozen FinancialAccount.

`insufficient_funds`The FinancialAccount doesn’t have a sufficient balance.

`other`Funds can’t be pulled from the FinancialAccount for other reasons.


- financial_accountnullablestringThe FinancialAccount that funds were pulled from.


- hosted_regulatory_receipt_urlnullablestringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.


- initiating_payment_method_detailsobjectDetails about how a ReceivedDebit was created.

Show child attributes
- linked_flowsobjectOther flows linked to a ReceivedDebit.

Show child attributes
- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- networkenumThe network used for the ReceivedDebit.


- reversal_detailsnullableobjectDetails describing when a ReceivedDebit might be reversed.

Show child attributes
- statusenumStatus of the ReceivedDebit. ReceivedDebits are created with a status of either succeeded (approved) or failed (declined). The failure reason can be found under the failure_code.

Possible enum values`failed`The ReceivedDebit was declined, and no Transaction was created.

`succeeded`The ReceivedDebit was approved.


- transactionnullablestringExpandableThe Transaction associated with this object.



The ReceivedDebit object`{  "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",  "object": "treasury.received_debit",  "amount": 1000,  "created": 1680755530,  "currency": "usd",  "description": "Stripe Test",  "failure_code": null,  "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",  "initiating_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "bank_name": "STRIPE TEST BANK",      "last4": "6789",      "routing_number": "110000000"    }  },  "linked_flows": {    "debit_reversal": null,    "inbound_transfer": null,    "issuing_authorization": null,    "issuing_transaction": null,    "payout": null  },  "livemode": false,  "network": "ach",  "reversal_details": {    "deadline": 1681084800,    "restricted_reason": null  },  "status": "succeeded",  "transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"}`# Retrieve a ReceivedDebit

Retrieves the details of an existing ReceivedDebit by passing the unique ReceivedDebit ID from the ReceivedDebit list

### Parameters

No parameters.

### Returns

Returns a ReceivedDebit object.

GET/v1/treasury/received_debits/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/received_debits/rd_1MtkUY2eZvKYlo2CT9SYD1AF \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",  "object": "treasury.received_debit",  "amount": 1000,  "created": 1680755530,  "currency": "usd",  "description": "Stripe Test",  "failure_code": null,  "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",  "initiating_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "bank_name": "STRIPE TEST BANK",      "last4": "6789",      "routing_number": "110000000"    }  },  "linked_flows": {    "debit_reversal": null,    "inbound_transfer": null,    "issuing_authorization": null,    "issuing_transaction": null,    "payout": null  },  "livemode": false,  "network": "ach",  "reversal_details": {    "deadline": 1681084800,    "restricted_reason": null  },  "status": "succeeded",  "transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"}`# List all ReceivedDebits

Returns a list of ReceivedDebits.

### Parameters

- financial_accountstringRequiredThe FinancialAccount that funds were pulled from.


- statusenumOnly return ReceivedDebits that have the given status: succeeded or failed.

Possible enum values`failed`The ReceivedDebit was declined, and no Transaction was created.

`succeeded`The ReceivedDebit was approved.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit ReceivedDebits, starting after ReceivedDebit starting_after. Each entry in the array is a separate ReceivedDebit object. If no more ReceivedDebits are available, the resulting array will be empty.

GET/v1/treasury/received_debitsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/received_debits \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/received_debits",  "has_more": false,  "data": [    {      "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",      "object": "treasury.received_debit",      "amount": 1000,      "created": 1680755530,      "currency": "usd",      "description": "Stripe Test",      "failure_code": null,      "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",      "initiating_payment_method_details": {        "billing_details": {          "address": {            "city": null,            "country": null,            "line1": null,            "line2": null,            "postal_code": null,            "state": null          },          "email": null,          "name": "Jane Austen"        },        "type": "us_bank_account",        "us_bank_account": {          "bank_name": "STRIPE TEST BANK",          "last4": "6789",          "routing_number": "110000000"        }      },      "linked_flows": {        "debit_reversal": null,        "inbound_transfer": null,        "issuing_authorization": null,        "issuing_transaction": null,        "payout": null      },      "livemode": false,      "network": "ach",      "reversal_details": {        "deadline": 1681084800,        "restricted_reason": null      },      "status": "succeeded",      "transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"    }    {...}    {...}  ],}`# Test mode: Create a ReceivedDebitTest helper

Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.

### Parameters

- amountintegerRequiredAmount (in cents) to be transferred.


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- financial_accountstringRequiredThe FinancialAccount to pull funds from.


- networkenumRequiredSpecifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the docs to learn more about money movement timelines for each network type.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- initiating_payment_method_detailsobjectInitiating payment method details for the object.

Show child parameters

### Returns

A test mode ReceivedDebit object.

POST/v1/test_helpers/treasury/received_debitsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/treasury/received_debits \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1000 \  -d currency=usd \  -d financial_account=fa_1MtkUY2eZvKYlo2CY3s6OQyK \  -d network=ach`Response`{  "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",  "object": "treasury.received_debit",  "amount": 1000,  "created": 1680755530,  "currency": "usd",  "description": "Stripe Test",  "failure_code": null,  "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",  "initiating_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "bank_name": "STRIPE TEST BANK",      "last4": "6789",      "routing_number": "110000000"    }  },  "linked_flows": {    "debit_reversal": null,    "inbound_transfer": null,    "issuing_authorization": null,    "issuing_transaction": null,    "payout": null  },  "livemode": false,  "network": "ach",  "reversal_details": {    "deadline": 1681084800,    "restricted_reason": null  },  "status": "succeeded",  "transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`