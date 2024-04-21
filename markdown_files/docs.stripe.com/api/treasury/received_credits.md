htmlReceived Credits | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Received Credits

ReceivedCredits represent funds sent to a FinancialAccount (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

Endpoints
# The ReceivedCredit object

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

POST/v1/test_helpers/treasury/received_creditsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/treasury/received_credits \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1000 \  -d currency=usd \  -d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \  -d network=ach`Response`{  "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",  "object": "treasury.received_credit",  "amount": 1000,  "created": 1680755425,  "currency": "usd",  "description": "Stripe Test",  "failure_code": null,  "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",  "initiating_payment_method_details": {    "billing_details": {      "address": {        "city": null,        "country": null,        "line1": null,        "line2": null,        "postal_code": null,        "state": null      },      "email": null,      "name": "Jane Austen"    },    "type": "us_bank_account",    "us_bank_account": {      "bank_name": "STRIPE TEST BANK",      "last4": "6789",      "routing_number": "110000000"    }  },  "linked_flows": {    "credit_reversal": null,    "issuing_authorization": null,    "issuing_transaction": null,    "source_flow": null,    "source_flow_type": null  },  "livemode": false,  "network": "ach",  "reversal_details": {    "deadline": 1681084800,    "restricted_reason": null  },  "status": "succeeded",  "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`