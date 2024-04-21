htmlDebit Reversals | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Debit Reversals

You can reverse some ReceivedDebits depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

Endpoints
# The DebitReversal object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- amountintegerAmount (in cents) transferred.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- financial_accountnullablestringThe FinancialAccount to reverse funds from.


- hosted_regulatory_receipt_urlnullablestringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.


- linked_flowsnullableobjectOther flows linked to a DebitReversal.

Show child attributes
- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- networkenumThe rails used to reverse the funds.


- received_debitstringThe ReceivedDebit being reversed.


- statusenumStatus of the DebitReversal

Possible enum values`failed`The network has resolved the DebitReversal against the user.

`processing`The DebitReversal starting state.

`succeeded`The network has resolved the DebitReversal in the users favour. A crediting Transaction is created.


- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.

Show child attributes
- transactionnullablestringExpandableThe Transaction associated with this object.



The DebitReversal object`{  "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",  "object": "treasury.debit_reversal",  "amount": 1000,  "created": 1680755021,  "currency": "usd",  "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",  "linked_flows": null,  "livemode": false,  "metadata": {},  "network": "ach",  "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",  "status": "processing",  "status_transitions": {    "completed_at": null  },  "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}`# Create a DebitReversal

Reverses a ReceivedDebit and creates a DebitReversal object.

### Parameters

- received_debitstringRequiredThe ReceivedDebit to reverse.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a DebitReversal object.

POST/v1/treasury/debit_reversalsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/debit_reversals \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d received_debit=rd_1MtkMLLkdIwHu7ixoiUFN4qd`Response`{  "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",  "object": "treasury.debit_reversal",  "amount": 1000,  "created": 1680755021,  "currency": "usd",  "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",  "linked_flows": null,  "livemode": false,  "metadata": {},  "network": "ach",  "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",  "status": "processing",  "status_transitions": {    "completed_at": null  },  "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}`# Retrieve a DebitReversal

Retrieves a DebitReversal object.

### Parameters

No parameters.

### Returns

Returns a DebitReversal object.

GET/v1/treasury/debit_reversals/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/debit_reversals/debrev_1MtkMLLkdIwHu7ixIcVctOKK \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",  "object": "treasury.debit_reversal",  "amount": 1000,  "created": 1680755021,  "currency": "usd",  "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",  "linked_flows": null,  "livemode": false,  "metadata": {},  "network": "ach",  "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",  "status": "processing",  "status_transitions": {    "completed_at": null  },  "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"}`# List all DebitReversals

Returns a list of DebitReversals.

### Parameters

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.


- received_debitstringOnly return DebitReversals for the ReceivedDebit ID.


- resolutionenumOnly return DebitReversals for a given resolution.

Possible enum values`lost`DebitReversal was lost, and no Transactions will be created.

`won`DebitReversal was won, and a crediting Transaction will be created.


- statusenumOnly return DebitReversals for a given status.

Possible enum values`canceled`The DebitReversal has been canceled before it has been sent to the network and no funds have been returned to the account. (Currently not supported).

`completed`The network has provided a resolution for the DebitReversal. If won, a crediting Transaction is created.

`processing`The DebitReversal starting state.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit DebitReversals, starting after DebitReversal starting_after. Each entry in the array is a separate DebitReversal object. If no more DebitReversals are available, the resulting array will be empty.

GET/v1/treasury/debit_reversalsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/debit_reversals \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d financial_account=fa_1MtkMLLkdIwHu7ixrkGP4bqB \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/debit_reversals",  "has_more": false,  "data": [    {      "id": "debrev_1MtkMLLkdIwHu7ixIcVctOKK",      "object": "treasury.debit_reversal",      "amount": 1000,      "created": 1680755021,      "currency": "usd",      "financial_account": "fa_1MtkMLLkdIwHu7ixrkGP4bqB",      "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KM6SuaEGMgaqNYp8YbE6NpNWYhI1PSbr_jlZwdPHUJHYBRG6-5T1Bmpq4GkpUhVvzLMDWZWkMVIveXHgiVwLUgpMM4Jx8w",      "linked_flows": null,      "livemode": false,      "metadata": {},      "network": "ach",      "received_debit": "rd_1MtkMLLkdIwHu7ixoiUFN4qd",      "status": "processing",      "status_transitions": {        "completed_at": null      },      "transaction": "trxn_1MtkMLLkdIwHu7ix2BG3LwWW"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`