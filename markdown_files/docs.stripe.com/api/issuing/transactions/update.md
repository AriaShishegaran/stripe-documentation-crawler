htmlUpdate a transaction | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a transaction

Updates the specified Issuing Transaction object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns an updated Issuing Transaction object if a valid identifier was provided.

POST/v1/issuing/transactions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",  "object": "issuing.transaction",  "amount": -100,  "amount_details": {    "atm_fee": null  },  "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",  "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",  "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",  "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",  "created": 1682065867,  "currency": "usd",  "dispute": null,  "livemode": false,  "merchant_amount": -100,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "WWWW.BROWSEBUG.BIZ",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA"  },  "metadata": {    "order_id": "6735"  },  "type": "capture",  "wallet": null}`# Retrieve a transaction

Retrieves an Issuing Transaction object.

### Parameters

No parameters.

### Returns

Returns an Issuing Transaction object if a valid identifier was provided.

GET/v1/issuing/transactions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/transactions/ipi_1MzFN1K8F4fqH0lBmFq8CjbU \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",  "object": "issuing.transaction",  "amount": -100,  "amount_details": {    "atm_fee": null  },  "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",  "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",  "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",  "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",  "created": 1682065867,  "currency": "usd",  "dispute": null,  "livemode": false,  "merchant_amount": -100,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "WWWW.BROWSEBUG.BIZ",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA"  },  "metadata": {},  "type": "capture",  "wallet": null}`# List all transactions

Returns a list of Issuing Transaction objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

- cardstringOnly return transactions that belong to the given card.


- cardholderstringOnly return transactions that belong to the given cardholder.



### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring
- typeenum

### Returns

A dictionary with a data property that contains an array of up to limit transactions, starting after transaction starting_after. Each entry in the array is a separate Issuing Transaction object. If no more transactions are available, the resulting array will be empty.

GET/v1/issuing/transactionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/transactions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/transactions",  "has_more": false,  "data": [    {      "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",      "object": "issuing.transaction",      "amount": -100,      "amount_details": {        "atm_fee": null      },      "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",      "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",      "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",      "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",      "created": 1682065867,      "currency": "usd",      "dispute": null,      "livemode": false,      "merchant_amount": -100,      "merchant_currency": "usd",      "merchant_data": {        "category": "computer_software_stores",        "category_code": "5734",        "city": "SAN FRANCISCO",        "country": "US",        "name": "WWWW.BROWSEBUG.BIZ",        "network_id": "1234567890",        "postal_code": "94103",        "state": "CA"      },      "metadata": {},      "type": "capture",      "wallet": null    }    {...}    {...}  ],}`# Create a test-mode force captureTest helper

Allows the user to capture an arbitrary amount, also known as a forced capture.

### Parameters

- amountintegerRequiredThe total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the smallest currency unit.


- cardstringRequiredCard associated with this transaction.


- currencyenumThe currency of the capture. If not provided, defaults to the currency of the card. Three-letter ISO currency code, in lowercase. Must be a supported currency.



### More parametersExpand all

- merchant_dataobject
- purchase_detailsobject

### Returns

A Transaction object

POST/v1/test_helpers/issuing/transactions/create_force_captureServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/issuing/transactions/create_force_capture \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1000 \  -d card=ic_1Gswa82eZvKYlo2CP2jveFil`Response`{  "id": "ipi_1GswaK2eZvKYlo2Co7wmNJhD",  "object": "issuing.transaction",  "amount": -1000,  "amount_details": {    "atm_fee": null,    "cashback_amount": null  },  "authorization": "iauth_1GswaJ2eZvKYlo2Ct9mFMJ4S",  "balance_transaction": "txn_1GswaK2eZvKYlo2CJAFFIuHg",  "card": "ic_1Gswa82eZvKYlo2CP2jveFil",  "cardholder": "ich_1Gswa82eZvKYlo2CvobneLSo",  "created": 1591905672,  "currency": "usd",  "dispute": null,  "livemode": false,  "merchant_amount": -1000,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "STRIPE.COM",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA",    "terminal_id": null  },  "metadata": {    "order_id": "6735"  },  "redaction": null,  "type": "capture",  "wallet": null}`# Create a test-mode unlinked refundTest helper

Allows the user to refund an arbitrary amount, also known as a unlinked refund.

### Parameters

- amountintegerRequiredThe total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the smallest currency unit.


- cardstringRequiredCard associated with this unlinked refund transaction.


- currencyenumThe currency of the unlinked refund. If not provided, defaults to the currency of the card. Three-letter ISO currency code, in lowercase. Must be a supported currency.



### More parametersExpand all

- merchant_dataobject
- purchase_detailsobject

### Returns

A Transaction object

POST/v1/test_helpers/issuing/transactions/create_unlinked_refundServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/issuing/transactions/create_unlinked_refund \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1000 \  -d card=ic_1Gswa82eZvKYlo2CP2jveFil`Response`{  "id": "ipi_1GswaK2eZvKYlo2Co7wmNJhD",  "object": "issuing.transaction",  "amount": -1000,  "amount_details": {    "atm_fee": null,    "cashback_amount": null  },  "authorization": "iauth_1GswaJ2eZvKYlo2Ct9mFMJ4S",  "balance_transaction": "txn_1GswaK2eZvKYlo2CJAFFIuHg",  "card": "ic_1Gswa82eZvKYlo2CP2jveFil",  "cardholder": "ich_1Gswa82eZvKYlo2CvobneLSo",  "created": 1591905672,  "currency": "usd",  "dispute": null,  "livemode": false,  "merchant_amount": -1000,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "STRIPE.COM",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA",    "terminal_id": null  },  "metadata": {    "order_id": "6735"  },  "redaction": null,  "type": "capture",  "wallet": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`