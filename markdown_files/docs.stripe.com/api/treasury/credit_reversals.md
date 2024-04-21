htmlCredit Reversals | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Credit Reversals

You can reverse some ReceivedCredits depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.

Endpoints
# The CreditReversal object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- amountintegerAmount (in cents) transferred.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- financial_accountstringThe FinancialAccount to reverse funds from.


- hosted_regulatory_receipt_urlnullablestringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- networkenumThe rails used to reverse the funds.


- received_creditstringThe ReceivedCredit being reversed.


- statusenumStatus of the CreditReversal

Possible enum values`canceled`The CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).

`posted`The CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)

`processing`The CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).


- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.

Show child attributes
- transactionnullablestringExpandableThe Transaction associated with this object.



The CreditReversal object`{  "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",  "object": "treasury.credit_reversal",  "amount": 1000,  "created": 1680756608,  "currency": "usd",  "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",  "livemode": false,  "metadata": {},  "network": "ach",  "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",  "status": "processing",  "status_transitions": {    "posted_at": null  },  "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}`# Create a CreditReversal

Reverses a ReceivedCredit and creates a CreditReversal object.

### Parameters

- received_creditstringRequiredThe ReceivedCredit to reverse.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a CreditReversal object.

POST/v1/treasury/credit_reversalsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/credit_reversals \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d received_credit=rc_1MtkGJLkdIwHu7ixWPuY9DGn`Response`{  "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",  "object": "treasury.credit_reversal",  "amount": 1000,  "created": 1680756608,  "currency": "usd",  "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",  "livemode": false,  "metadata": {},  "network": "ach",  "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",  "status": "processing",  "status_transitions": {    "posted_at": null  },  "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}`# Retrieve a CreditReversal

Retrieves the details of an existing CreditReversal by passing the unique CreditReversal ID from either the CreditReversal creation request or CreditReversal list

### Parameters

No parameters.

### Returns

Returns a CreditReversal object.

GET/v1/treasury/credit_reversals/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/credit_reversals/credrev_1Mtklw2eZvKYlo2CJG2MWJM7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",  "object": "treasury.credit_reversal",  "amount": 1000,  "created": 1680756608,  "currency": "usd",  "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",  "livemode": false,  "metadata": {},  "network": "ach",  "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",  "status": "processing",  "status_transitions": {    "posted_at": null  },  "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"}`# List all CreditReversals

Returns a list of CreditReversals.

### Parameters

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.


- received_creditstringOnly return CreditReversals for the ReceivedCredit ID.


- statusenumOnly return CreditReversals for a given status.

Possible enum values`canceled`The CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).

`posted`The CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)

`processing`The CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit CreditReversals, starting after CreditReversal starting_after. Each entry in the array is a separate CreditReversal object. If no more CreditReversal are available, the resulting array will be empty.

GET/v1/treasury/credit_reversalsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/credit_reversals \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtkGJLkdIwHu7ix6FAcfxof \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/credit_reversals",  "has_more": false,  "data": [    {      "id": "credrev_1Mtklw2eZvKYlo2CJG2MWJM7",      "object": "treasury.credit_reversal",      "amount": 1000,      "created": 1680756608,      "currency": "usd",      "financial_account": "fa_1Mtklw2eZvKYlo2CNHscZzs2",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKICfuaEGMgYv0T_PcXU6NpP_n6wAfI9LKta3LkDRNQT8oLGdQf7JcXsskGjrq1LICpYVy5a3oOBI5gaVvTy8MtwpT1PTpQ",      "livemode": false,      "metadata": {},      "network": "ach",      "received_credit": "rc_1Mtklw2eZvKYlo2CxuluQFPR",      "status": "processing",      "status_transitions": {        "posted_at": null      },      "transaction": "trxn_1Mtklw2eZvKYlo2CKkbNA2TS"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`