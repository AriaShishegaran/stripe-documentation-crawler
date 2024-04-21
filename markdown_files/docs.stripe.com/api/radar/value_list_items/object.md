htmlThe Value List Item object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Value List Item object

### Attributes

- idstringUnique identifier for the object.


- valuestringThe value of the item.


- value_liststringThe identifier of the value list this item belongs to.



### More attributesExpand all

- objectstring
- createdtimestamp
- created_bystring
- livemodeboolean

The Value List Item object`{  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",  "object": "radar.value_list_item",  "created": 1681760074,  "created_by": "API",  "livemode": false,  "value": "1.2.3.4",  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj"}`# Create a value list item

Creates a new ValueListItem object, which is added to the specified parent value list.

### Parameters

- valuestringRequiredThe value of the item (whose type must match the type of the parent value list).


- value_liststringRequiredThe identifier of the value list which the created item will be added to.



### Returns

Returns a ValueListItem object if creation succeeds.

POST/v1/radar/value_list_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/radar/value_list_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj \  -d value="1.2.3.4"`Response`{  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",  "object": "radar.value_list_item",  "created": 1681760074,  "created_by": "API",  "livemode": false,  "value": "1.2.3.4",  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj"}`# Retrieve a value list item

Retrieves a ValueListItem object.

### Parameters

No parameters.

### Returns

Returns a ValueListItem object if a valid identifier was provided.

GET/v1/radar/value_list_items/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",  "object": "radar.value_list_item",  "created": 1681760074,  "created_by": "API",  "livemode": false,  "value": "1.2.3.4",  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj"}`# List all value list items

Returns a list of ValueListItem objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

- value_liststringRequiredIdentifier for the parent value list this item belongs to.


- valuestringReturn items belonging to the parent list whose value matches the specified value (using an “is like” match).



### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit items, starting after item starting_after. Each entry in the array is a separate ValueListItem object. If no more items are available, the resulting array will be empty.

GET/v1/radar/value_list_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/radar/value_list_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj`Response`{  "object": "list",  "url": "/v1/radar/value_list_items",  "has_more": false,  "data": [    {      "id": "rsl_1MxxosLkdIwHu7ixNiiD01Kj",      "object": "radar.value_list",      "alias": "custom_ip_blocklist",      "created": 1681760074,      "created_by": "API",      "item_type": "ip_address",      "list_items": {        "object": "list",        "data": [],        "has_more": false,        "total_count": 0,        "url": "/v1/radar/value_list_items?value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj"      },      "livemode": false,      "metadata": {},      "name": "Custom IP Blocklist"    }    {...}    {...}  ],}`# Delete a value list item

Deletes a ValueListItem object, removing it from its parent value list.

### Parameters

No parameters.

### Returns

Returns an object with the deleted ValueListItem object’s ID and a deleted parameter on success. Otherwise, this call raises an error.

DELETE/v1/radar/value_list_items/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",  "object": "radar.value_list_item",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`