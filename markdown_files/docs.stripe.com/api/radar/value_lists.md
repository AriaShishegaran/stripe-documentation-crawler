htmlValue Lists | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Value Lists

Value lists allow you to group values together which can then be referenced in rules.

Related guide: Default Stripe lists

Endpoints
# The Value List object

### Attributes

- idstringUnique identifier for the object.


- aliasstringThe name of the value list for use in rules.


- item_typeenumThe type of items in the value list. One of card_fingerprint, us_bank_account_fingerprint, sepa_debit_fingerprint, card_bin, email, ip_address, country, string, case_sensitive_string, or customer_id.

Possible enum values`card_bin``card_fingerprint``case_sensitive_string``country``customer_id``email``ip_address``sepa_debit_fingerprint``string``us_bank_account_fingerprint`
- list_itemsobjectList of items contained within this value list.

Show child attributes
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- namestringThe name of the value list.



### More attributesExpand all

- objectstring
- createdtimestamp
- created_bystring
- livemodeboolean

The Value List object`{  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",  "object": "radar.value_list",  "alias": "custom_ip_blocklist",  "created": 1680201894,  "created_by": "API",  "item_type": "ip_address",  "list_items": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"  },  "livemode": false,  "metadata": {},  "name": "Custom IP Blocklist"}`# Create a value list

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

GET/v1/radar/value_lists/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",  "object": "radar.value_list",  "alias": "custom_ip_blocklist",  "created": 1680201894,  "created_by": "API",  "item_type": "ip_address",  "list_items": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"  },  "livemode": false,  "metadata": {},  "name": "Custom IP Blocklist"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`