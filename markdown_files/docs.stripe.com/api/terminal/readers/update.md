htmlUpdate a Reader | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a Reader

Updates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- labelstringThe new label of the reader.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns an updated Reader object if a valid identifier was provided.

POST/v1/terminal/readers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": null,  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {    "order_id": "6735"  },  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`# Retrieve a Reader

Retrieves a Reader object.

### Parameters

No parameters.

### Returns

Returns a Reader object if a valid identifier was provided.

GET/v1/terminal/readers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": null,  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`# List all Readers

Returns a list of Reader objects.

### Parameters

- device_typeenumFilters readers by device type


- locationstringA location ID to filter the response list to only readers at the specific location


- serial_numberstringFilters readers by serial number


- statusenumA status filter to filter readers to only offline or online readers



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit readers, starting after reader starting_after. Each entry in the array is a separate Terminal Reader object. If no more readers are available, the resulting array will be empty.

GET/v1/terminal/readersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/terminal/readers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/terminal/readers",  "has_more": false,  "data": [    {      "id": "tmr_FDOt2wlRZEdpd7",      "object": "terminal.reader",      "action": null,      "device_sw_version": "",      "device_type": "simulated_wisepos_e",      "ip_address": "0.0.0.0",      "label": "Blue Rabbit",      "last_seen_at": 1681320543815,      "livemode": false,      "location": "tml_FDOtHwxAAdIJOh",      "metadata": {},      "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",      "status": "online"    }    {...}    {...}  ],}`# Delete a Reader

Deletes a Reader object.

### Parameters

No parameters.

### Returns

Returns the Reader object that was deleted.

DELETE/v1/terminal/readers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "deleted": true}`# Cancel the current reader action

Cancels the current reader action.

### Parameters

No parameters.

### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/cancel_actionServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/cancel_action \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": null,  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1695402450407,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`