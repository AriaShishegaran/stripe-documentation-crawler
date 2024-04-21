htmlTransactions | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Transactions

Any use of an issued card that results in funds entering or leaving your Stripe account, such as a completed purchase or refund, is represented by an Issuing Transaction object.

Related guide: Issued card transactions

Endpoints
# The Transaction object

### Attributes

- idstringUnique identifier for the object.


- amountintegerThe transaction amount, which will be reflected in your balance. This amount is in your currency and in the smallest currency unit.


- authorizationnullablestringExpandableThe Authorization object that led to this transaction.


- cardstringExpandableThe card used to make this transaction.


- cardholdernullablestringExpandableThe cardholder to whom this transaction belongs.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- typeenumThe nature of the transaction.

Possible enum values`capture`Funds were captured by the acquirer. amount will be negative as funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirers can force capture in some cases.

`refund`An acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions. amount will be positive for refunds and negative for refund reversals (very rare).



### More attributesExpand all

- objectstring
- amount_detailsnullableobject
- balance_transactionnullablestringExpandable
- createdtimestamp
- disputenullablestringExpandable
- livemodeboolean
- merchant_amountinteger
- merchant_currencyenum
- merchant_dataobject
- network_datanullableobject
- purchase_detailsnullableobjectExpandable
- tokennullablestringPreview featureExpandable
- walletnullableenum

The Transaction object`{  "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",  "object": "issuing.transaction",  "amount": -100,  "amount_details": {    "atm_fee": null  },  "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",  "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",  "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",  "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",  "created": 1682065867,  "currency": "usd",  "dispute": null,  "livemode": false,  "merchant_amount": -100,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "WWWW.BROWSEBUG.BIZ",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA"  },  "metadata": {},  "type": "capture",  "wallet": null}`# Update a transaction

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

GET/v1/issuing/transactionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/transactions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/transactions",  "has_more": false,  "data": [    {      "id": "ipi_1MzFN1K8F4fqH0lBmFq8CjbU",      "object": "issuing.transaction",      "amount": -100,      "amount_details": {        "atm_fee": null      },      "authorization": "iauth_1MzFMzK8F4fqH0lBc9VdaZUp",      "balance_transaction": "txn_1MzFN1K8F4fqH0lBQPtqUmJN",      "card": "ic_1MzFMxK8F4fqH0lBjIUITRYi",      "cardholder": "ich_1MzFMxK8F4fqH0lBXnFW0ROG",      "created": 1682065867,      "currency": "usd",      "dispute": null,      "livemode": false,      "merchant_amount": -100,      "merchant_currency": "usd",      "merchant_data": {        "category": "computer_software_stores",        "category_code": "5734",        "city": "SAN FRANCISCO",        "country": "US",        "name": "WWWW.BROWSEBUG.BIZ",        "network_id": "1234567890",        "postal_code": "94103",        "state": "CA"      },      "metadata": {},      "type": "capture",      "wallet": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`