htmlUpdate a customer | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a customer

Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.  For example, if you pass the source parameter, that becomes the customer’s active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the source parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the past_due state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the default_source for a customer will not trigger this behavior.

This request accepts mostly the same arguments as the customer creation call.

### Parameters

- addressobjectThe customer’s address.

Show child parameters
- descriptionstringAn arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.


- emailstringCustomer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringThe customer’s full name or business name.


- phonestringThe customer’s phone number.


- shippingobjectThe customer’s shipping information. Appears on invoices emailed to this customer.

Show child parameters

### More parametersExpand all

- balanceinteger
- cash_balanceobject
- couponstring
- default_sourcestring
- invoice_prefixstring
- invoice_settingsobject
- next_invoice_sequenceinteger
- preferred_localesarray of strings
- promotion_codestring
- sourcestring
- taxobject
- tax_exemptenum

### Returns

Returns the customer object if the update succeeded. Raises an error if update parameters are invalid (e.g. specifying an invalid coupon or an invalid source).

POST/v1/customers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "cus_NffrFeUfNV2Hib",  "object": "customer",  "address": null,  "balance": 0,  "created": 1680893993,  "currency": null,  "default_source": null,  "delinquent": false,  "description": null,  "discount": null,  "email": "jennyrosen@example.com",  "invoice_prefix": "0759376C",  "invoice_settings": {    "custom_fields": null,    "default_payment_method": null,    "footer": null,    "rendering_options": null  },  "livemode": false,  "metadata": {    "order_id": "6735"  },  "name": "Jenny Rosen",  "next_invoice_sequence": 1,  "phone": null,  "preferred_locales": [],  "shipping": null,  "tax_exempt": "none",  "test_clock": null}`# Retrieve a customer

Retrieves a Customer object.

### Parameters

No parameters.

### Returns

Returns the Customer object for a valid identifier. If it’s for a deleted Customer, a subset of the customer’s information is returned, including a deleted property that’s set to true.

GET/v1/customers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "cus_NffrFeUfNV2Hib",  "object": "customer",  "address": null,  "balance": 0,  "created": 1680893993,  "currency": null,  "default_source": null,  "delinquent": false,  "description": null,  "discount": null,  "email": "jennyrosen@example.com",  "invoice_prefix": "0759376C",  "invoice_settings": {    "custom_fields": null,    "default_payment_method": null,    "footer": null,    "rendering_options": null  },  "livemode": false,  "metadata": {},  "name": "Jenny Rosen",  "next_invoice_sequence": 1,  "phone": null,  "preferred_locales": [],  "shipping": null,  "tax_exempt": "none",  "test_clock": null}`# List all customers

Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.

### Parameters

- emailstringA case-sensitive filter on the list based on the customer’s email field. The value must be a string.



### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring
- test_clockstring

### Returns

A dictionary with a data property that contains an array of up to limit customers, starting after customer starting_after. Passing an optional email will result in filtering to customers with only that exact email address. Each entry in the array is a separate customer object. If no more customers are available, the resulting array will be empty.

GET/v1/customersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/customers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/customers",  "has_more": false,  "data": [    {      "id": "cus_NffrFeUfNV2Hib",      "object": "customer",      "address": null,      "balance": 0,      "created": 1680893993,      "currency": null,      "default_source": null,      "delinquent": false,      "description": null,      "discount": null,      "email": "jennyrosen@example.com",      "invoice_prefix": "0759376C",      "invoice_settings": {        "custom_fields": null,        "default_payment_method": null,        "footer": null,        "rendering_options": null      },      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "next_invoice_sequence": 1,      "phone": null,      "preferred_locales": [],      "shipping": null,      "tax_exempt": "none",      "test_clock": null    }    {...}    {...}  ],}`# Delete a customer

Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.

### Parameters

No parameters.

### Returns

Returns an object with a deleted parameter on success. If the customer ID does not exist, this call raises an error.

Unlike other objects, deleted customers can still be retrieved through the API in order to be able to track their history. Deleting customers removes all credit card details and prevents any further operations to be performed (such as adding a new subscription).

DELETE/v1/customers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "cus_NffrFeUfNV2Hib",  "object": "customer",  "deleted": true}`# Search customers

Search for customers you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

### Parameters

- querystringRequiredThe search query string. See search query language and the list of supported query fields for customers.


- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.


- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.



### Returns

A dictionary with a data property that contains an array of up to limit customers. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

GET/v1/customers/searchServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/customers/search \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  --data-urlencode query="name:'Jane Doe' AND metadata['foo']:'bar'"`Response`{  "object": "search_result",  "url": "/v1/customers/search",  "has_more": false,  "data": [    {      "id": "cus_NeGfPRiPKxeBi1",      "object": "customer",      "address": null,      "balance": 0,      "created": 1680569616,      "currency": null,      "default_source": null,      "delinquent": false,      "description": null,      "discount": null,      "email": null,      "invoice_prefix": "47D37F8F",      "invoice_settings": {        "custom_fields": null,        "default_payment_method": "pm_1Msy7wLkdIwHu7ixsxmFvcz7",        "footer": null,        "rendering_options": null      },      "livemode": false,      "metadata": {        "foo": "bar"      },      "name": "Jane Doe",      "next_invoice_sequence": 1,      "phone": null,      "preferred_locales": [],      "shipping": null,      "tax_exempt": "none",      "test_clock": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`