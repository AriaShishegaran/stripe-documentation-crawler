htmlTransfers | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Transfers

A Transfer object is created when you move funds between Stripe accounts as part of Connect.

Before April 6, 2017, transfers also represented movement of funds from a Stripe account to a card or bank account. This behavior has since been split out into a Payout object, with corresponding payout endpoints. For more information, read about the transfer/payout split.

Related guide: Creating separate charges and transfers

Endpoints
# The Transfer object

### Attributes

- idstringUnique identifier for the object.


- amountintegerAmount in cents to be transferred.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- destinationnullablestringExpandableID of the Stripe account the transfer was sent to.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.



### More attributesExpand all

- objectstring
- amount_reversedinteger
- balance_transactionnullablestringExpandable
- createdtimestamp
- destination_paymentnullablestringExpandable
- livemodeboolean
- reversalsobject
- reversedboolean
- source_transactionnullablestringExpandable
- source_typenullablestring
- transfer_groupnullablestring

The Transfer object`{  "id": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",  "object": "transfer",  "amount": 400,  "amount_reversed": 0,  "balance_transaction": "txn_1MiN3gLkdIwHu7ixxapQrznl",  "created": 1678043844,  "currency": "usd",  "description": null,  "destination": "acct_1MTfjCQ9PRzxEwkZ",  "destination_payment": "py_1MiN3gQ9PRzxEwkZWTPGNq9o",  "livemode": false,  "metadata": {},  "reversals": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"  },  "reversed": false,  "source_transaction": null,  "source_type": "card",  "transfer_group": "ORDER_95"}`# Create a transfer

To send funds from your Stripe account to a connected account, you create a new transfer object. Your Stripe balance must be able to cover the transfer amount, or you’ll receive an “Insufficient Funds” error.

### Parameters

- currencyenumRequired3-letter ISO code for currency.


- destinationstringRequiredThe ID of a connected Stripe account. See the Connect documentation for details.


- amountintegerRequiredA positive integer in cents representing how much to transfer.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- source_transactionstring
- source_typestring
- transfer_groupstring

### Returns

Returns a transfer object if there were no initial errors with the transfer creation (e.g., insufficient funds).

POST/v1/transfersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/transfers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=400 \  -d currency=usd \  -d destination=acct_1MTfjCQ9PRzxEwkZ \  -d transfer_group=ORDER_95`Response`{  "id": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",  "object": "transfer",  "amount": 400,  "amount_reversed": 0,  "balance_transaction": "txn_1MiN3gLkdIwHu7ixxapQrznl",  "created": 1678043844,  "currency": "usd",  "description": null,  "destination": "acct_1MTfjCQ9PRzxEwkZ",  "destination_payment": "py_1MiN3gQ9PRzxEwkZWTPGNq9o",  "livemode": false,  "metadata": {},  "reversals": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"  },  "reversed": false,  "source_transaction": null,  "source_type": "card",  "transfer_group": "ORDER_95"}`# Update a transfer

Updates the specified transfer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts only metadata as an argument.

### Parameters

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the transfer object if the update succeeded. This call will raise an error if update parameters are invalid.

POST/v1/transfers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",  "object": "transfer",  "amount": 400,  "amount_reversed": 0,  "balance_transaction": "txn_1MiN3gLkdIwHu7ixxapQrznl",  "created": 1678043844,  "currency": "usd",  "description": null,  "destination": "acct_1MTfjCQ9PRzxEwkZ",  "destination_payment": "py_1MiN3gQ9PRzxEwkZWTPGNq9o",  "livemode": false,  "metadata": {    "order_id": "6735"  },  "reversals": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"  },  "reversed": false,  "source_transaction": null,  "source_type": "card",  "transfer_group": "ORDER_95"}`# Retrieve a transfer

Retrieves the details of an existing transfer. Supply the unique transfer ID from either a transfer creation request or the transfer list, and Stripe will return the corresponding transfer information.

### Parameters

No parameters.

### Returns

Returns a transfer object if a valid identifier was provided, and raises an error otherwise.

GET/v1/transfers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tr_1MiN3gLkdIwHu7ixNCZvFdgA",  "object": "transfer",  "amount": 400,  "amount_reversed": 0,  "balance_transaction": "txn_1MiN3gLkdIwHu7ixxapQrznl",  "created": 1678043844,  "currency": "usd",  "description": null,  "destination": "acct_1MTfjCQ9PRzxEwkZ",  "destination_payment": "py_1MiN3gQ9PRzxEwkZWTPGNq9o",  "livemode": false,  "metadata": {},  "reversals": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/transfers/tr_1MiN3gLkdIwHu7ixNCZvFdgA/reversals"  },  "reversed": false,  "source_transaction": null,  "source_type": "card",  "transfer_group": "ORDER_95"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`