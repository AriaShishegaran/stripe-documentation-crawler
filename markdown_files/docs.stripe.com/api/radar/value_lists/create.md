htmlCreate a value list | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a value list

Creates a new ValueList object, which can then be referenced in rules.

### Parameters

- aliasstringRequiredThe name of the value list for use in rules.


- namestringRequiredThe human-readable name of the value list.


- item_typestringType of the items in the value list. One of card_fingerprint, us_bank_account_fingerprint, sepa_debit_fingerprint, card_bin, email, ip_address, country, string, case_sensitive_string, or customer_id. Use string if the item type is unknown or mixed.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a ValueList object if creation succeeds.

POST/v1/radar/value_listsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/radar/value_lists \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name="Custom IP Blocklist" \  -d alias=custom_ip_blocklist \  -d item_type=ip_address`Response`{  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",  "object": "radar.value_list",  "alias": "custom_ip_blocklist",  "created": 1680201894,  "created_by": "API",  "item_type": "ip_address",  "list_items": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"  },  "livemode": false,  "metadata": {},  "name": "Custom IP Blocklist"}`# Update a value list

Updates a ValueList object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Note that item_type is immutable.

### Parameters

- aliasstringThe name of the value list for use in rules.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringThe human-readable name of the value list.



### Returns

Returns an updated ValueList object if a valid identifier was provided.

POST/v1/radar/value_lists/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name="Updated IP Blocklist"`Response`{  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",  "object": "radar.value_list",  "alias": "custom_ip_blocklist",  "created": 1680201894,  "created_by": "API",  "item_type": "ip_address",  "list_items": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"  },  "livemode": false,  "metadata": {},  "name": "Updated IP Blocklist"}`# Retrieve a value list

Retrieves a ValueList object.

### Parameters

No parameters.

### Returns

Returns a ValueList object if a valid identifier was provided.

GET/v1/radar/value_lists/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",  "object": "radar.value_list",  "alias": "custom_ip_blocklist",  "created": 1680201894,  "created_by": "API",  "item_type": "ip_address",  "list_items": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"  },  "livemode": false,  "metadata": {},  "name": "Custom IP Blocklist"}`# List all value lists

Returns a list of ValueList objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

- aliasstringThe alias used to reference the value list when writing rules.



### More parametersExpand all

- containsstring
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit lists, starting after list starting_after. Each entry in the array is a separate ValueList object. If no more lists are available, the resulting array will be empty.

GET/v1/radar/value_listsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/radar/value_lists \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/radar/value_lists",  "has_more": false,  "data": [    {      "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",      "object": "radar.value_list",      "alias": "custom_ip_blocklist",      "created": 1680201894,      "created_by": "API",      "item_type": "ip_address",      "list_items": {        "object": "list",        "data": [],        "has_more": false,        "total_count": 0,        "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"      },      "livemode": false,      "metadata": {},      "name": "Custom IP Blocklist"    }    {...}    {...}  ],}`# Delete a value list

Deletes a ValueList object, also deleting any items contained within the value list. To be deleted, a value list must not be referenced in any rules.

### Parameters

No parameters.

### Returns

Returns an object with the deleted ValueList object’s ID and a deleted parameter on success. Otherwise, this call raises an error.

DELETE/v1/radar/value_lists/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",  "object": "radar.value_list",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`