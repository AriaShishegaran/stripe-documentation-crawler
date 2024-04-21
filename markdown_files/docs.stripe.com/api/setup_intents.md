htmlSetup Intents | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Setup Intents

A SetupIntent guides you through the process of setting up and saving a customer’s payment credentials for future payments. For example, you can use a SetupIntent to set up and save your customer’s card without immediately collecting a payment. Later, you can use PaymentIntents to drive the payment flow.

Create a SetupIntent when you’re ready to collect your customer’s payment credentials. Don’t maintain long-lived, unconfirmed SetupIntents because they might not be valid. The SetupIntent transitions through multiple statuses as it guides you through the setup process.

Successful SetupIntents result in payment credentials that are optimized for future payments. For example, cardholders in certain regions might need to be run through Strong Customer Authentication during payment method collection to streamline later off-session payments. If you use the SetupIntent with a Customer, it automatically attaches the resulting payment method to that Customer after successful setup. We recommend using SetupIntents or setup_future_usage on PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

Related guide: Setup Intents API

Endpoints
# The SetupIntent object

### Attributes

- idstringretrievable with publishable keyUnique identifier for the object.


- automatic_payment_methodsnullableobjectSettings for dynamic payment methods compatible with this Setup Intent

Show child attributes
- client_secretnullablestringretrievable with publishable keyThe client secret of this SetupIntent. Used for client-side retrieval using a publishable key.

The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.


- customernullablestringExpandableID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.


- descriptionnullablestringretrievable with publishable keyAn arbitrary string attached to the object. Often useful for displaying to users.


- last_setup_errornullableobjectretrievable with publishable keyThe error encountered in the previous SetupIntent confirmation.

Show child attributes
- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- next_actionnullableobjectretrievable with publishable keyIf present, this property tells you what actions you need to take in order for your customer to continue payment setup.

Show child attributes
- payment_methodnullablestringExpandableretrievable with publishable keyID of the payment method used with this SetupIntent.


- statusenumretrievable with publishable keyStatus of this SetupIntent, one of requires_payment_method, requires_confirmation, requires_action, processing, canceled, or succeeded.

Possible enum values`canceled``processing``requires_action``requires_confirmation``requires_payment_method``succeeded`
- usagestringretrievable with publishable keyIndicates how the payment method is intended to be used in the future.

Use on_session if you intend to only reuse the payment method when the customer is in your checkout flow. Use off_session if your customer may or may not be in your checkout flow. If not provided, this value defaults to off_session.



### More attributesExpand all

- objectstringretrievable with publishable key
- applicationnullablestringExpandableConnect only
- attach_to_selfnullableboolean
- cancellation_reasonnullableenumretrievable with publishable key
- createdtimestampretrievable with publishable key
- flow_directionsnullablearray of enums
- latest_attemptnullablestringExpandable
- livemodebooleanretrievable with publishable key
- mandatenullablestringExpandable
- on_behalf_ofnullablestringExpandableConnect only
- payment_method_configuration_detailsnullableobject
- payment_method_optionsnullableobject
- payment_method_typesarray of stringsretrievable with publishable key
- single_use_mandatenullablestringExpandable

The SetupIntent object`{  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",  "object": "setup_intent",  "application": null,  "cancellation_reason": null,  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",  "created": 1678942624,  "customer": null,  "description": null,  "flow_directions": null,  "last_setup_error": null,  "latest_attempt": null,  "livemode": false,  "mandate": null,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "single_use_mandate": null,  "status": "requires_payment_method",  "usage": "off_session"}`# Create a SetupIntent

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

GET/v1/setup_intents/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/setup_intents/seti_1Mm8s8LkdIwHu7ix0OXBfTRG \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG",  "object": "setup_intent",  "application": null,  "cancellation_reason": null,  "client_secret": "seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe",  "created": 1678942624,  "customer": null,  "description": null,  "flow_directions": null,  "last_setup_error": null,  "latest_attempt": null,  "livemode": false,  "mandate": null,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "single_use_mandate": null,  "status": "requires_payment_method",  "usage": "off_session"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`