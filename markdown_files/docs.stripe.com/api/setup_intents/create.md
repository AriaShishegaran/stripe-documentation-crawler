htmlCreate a SetupIntent | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a SetupIntent

Creates a SetupIntent object.

After you create the SetupIntent, attach a payment method and confirm it to collect any required permissions to charge the payment method later.

### Parameters

- automatic_payment_methodsobjectWhen you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.

Show child parameters
- confirmbooleanSet to true to attempt to confirm this SetupIntent immediately. This parameter defaults to false. If a card is the attached payment method, you can provide a return_url in case further authentication is necessary.


- customerstringID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- payment_methodstringID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.


- usageenumIndicates how the payment method is intended to be used in the future. If not provided, this value defaults to off_session.

Possible enum values`off_session`Use off_session if your customer may or may not be in your checkout flow.

`on_session`Use on_session if you intend to only reuse the payment method when the customer is in your checkout flow.



### More parametersExpand all

- attach_to_selfboolean
- confirmation_tokenstringonly when confirm=true
- flow_directionsarray of enums
- mandate_dataobjectonly when confirm=true
- on_behalf_ofstringConnect only
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings
- return_urlstringonly when confirm=true
- single_useobject
- use_stripe_sdkboolean

### Returns

Returns a SetupIntent object.

POST/v1/setup_intentsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/setup_intents \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "payment_method_types[]"=card`Response`{  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",  "object": "setup_intent",  "application": null,  "cancellation_reason": null,  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",  "created": 1678942624,  "customer": null,  "description": null,  "flow_directions": null,  "last_setup_error": null,  "latest_attempt": null,  "livemode": false,  "mandate": null,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "single_use_mandate": null,  "status": "requires_payment_method",  "usage": "off_session"}`# Update a SetupIntent

Updates a SetupIntent object.

### Parameters

- customerstringID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- payment_methodstringID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.



### More parametersExpand all

- attach_to_selfboolean
- flow_directionsarray of enums
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings

### Returns

Returns a SetupIntent object.

POST/v1/setup_intents/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",  "object": "setup_intent",  "application": null,  "cancellation_reason": null,  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",  "created": 1678942624,  "customer": null,  "description": null,  "flow_directions": null,  "last_setup_error": null,  "latest_attempt": null,  "livemode": false,  "mandate": null,  "metadata": {    "order_id": "6735"  },  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "single_use_mandate": null,  "status": "requires_payment_method",  "usage": "off_session"}`# Retrieve a SetupIntent

Retrieves the details of a SetupIntent that has previously been created.

Client-side retrieval using a publishable key is allowed when the client_secret is provided in the query string.

When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the SetupIntent object reference for more details.

### Parameters

- client_secretstringRequired if using publishable keyThe client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.



### Returns

Returns a SetupIntent if a valid identifier was provided.

GET/v1/setup_intents/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",  "object": "setup_intent",  "application": null,  "cancellation_reason": null,  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",  "created": 1678942624,  "customer": null,  "description": null,  "flow_directions": null,  "last_setup_error": null,  "latest_attempt": null,  "livemode": false,  "mandate": null,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "single_use_mandate": null,  "status": "requires_payment_method",  "usage": "off_session"}`# List all SetupIntents

Returns a list of SetupIntents.

### Parameters

- customerstringOnly return SetupIntents for the customer specified by this customer ID.


- payment_methodstringOnly return SetupIntents that associate with the specified payment method.



### More parametersExpand all

- attach_to_selfboolean
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit SetupIntents, starting after SetupIntent starting_after. Each entry in the array is a separate SetupIntent object. If no more SetupIntents are available, the resulting array will be empty.

GET/v1/setup_intentsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/setup_intents \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/setup_intents",  "has_more": false,  "data": [    {      "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",      "object": "setup_intent",      "application": null,      "cancellation_reason": null,      "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",      "created": 1678942624,      "customer": null,      "description": null,      "flow_directions": null,      "last_setup_error": null,      "latest_attempt": null,      "livemode": false,      "mandate": null,      "metadata": {},      "next_action": null,      "on_behalf_of": null,      "payment_method": null,      "payment_method_options": {        "card": {          "mandate_options": null,          "network": null,          "request_three_d_secure": "automatic"        }      },      "payment_method_types": [        "card"      ],      "single_use_mandate": null,      "status": "requires_payment_method",      "usage": "off_session"    }    {...}    {...}  ],}`# Cancel a SetupIntent

You can cancel a SetupIntent object when it’s in one of these statuses: requires_payment_method, requires_confirmation, or requires_action.

After you cancel it, setup is abandoned and any operations on the SetupIntent fail with an error.

### Parameters

- cancellation_reasonstringReason for canceling this SetupIntent. Possible values are: abandoned, requested_by_customer, or duplicate



### Returns

Returns a SetupIntent object if the cancellation succeeds. Returns an error if the SetupIntent is already canceled or isn’t in a cancelable state.

POST/v1/setup_intents/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",  "object": "setup_intent",  "application": null,  "cancellation_reason": null,  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",  "created": 1678942624,  "customer": null,  "description": null,  "flow_directions": null,  "last_setup_error": null,  "latest_attempt": null,  "livemode": false,  "mandate": null,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "single_use_mandate": null,  "status": "canceled",  "usage": "off_session"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`