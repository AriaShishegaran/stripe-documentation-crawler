htmlThe Cardholder object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Cardholder object

### Attributes

- idstringUnique identifier for the object.


- billingobjectThe cardholder’s billing information.

Show child attributes
- emailnullablestringThe cardholder’s email address.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- namestringThe cardholder’s name. This will be printed on cards issued to them.


- phone_numbernullablestringThe cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.



### More attributesExpand all

- objectstring
- companynullableobject
- createdtimestamp
- individualnullableobject
- livemodeboolean
- preferred_localesnullablearray of enums
- requirementsobject
- spending_controlsnullableobject
- statusenum
- typeenum

The Cardholder object`{  "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",  "object": "issuing.cardholder",  "billing": {    "address": {      "line1": "1234 Main Street",      "city": "San Francisco",      "state": "CA",      "country": "US",      "postal_code": "94111"    }  },  "company": null,  "created": 1680415995,  "email": "jenny.rosen@example.com",  "individual": null,  "livemode": false,  "metadata": {},  "name": "Jenny Rosen",  "phone_number": "+18888675309",  "redaction": null,  "requirements": {    "disabled_reason": "requirements.past_due",    "past_due": [      "individual.card_issuing.user_terms_acceptance.ip",      "individual.card_issuing.user_terms_acceptance.date",      "individual.first_name",      "individual.last_name"    ]  },  "spending_controls": {    "allowed_categories": [],    "blocked_categories": [],    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "individual"}`# Create a cardholder

Creates a new Issuing Cardholder object that can be issued cards.

### Parameters

- billingobjectRequiredThe cardholder’s billing address.

Show child parameters
- namestringRequiredThe cardholder’s name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.


- emailstringThe cardholder’s email address.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- phone_numberstringThe cardholder’s phone number. This will be transformed to E.164 if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.



### More parametersExpand all

- companyobject
- individualobject
- preferred_localesarray of enums
- spending_controlsobject
- statusenum
- typeenum

### Returns

Returns an Issuing Cardholder object if creation succeeds.

POST/v1/issuing/cardholdersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/cardholders \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=individual \  -d name="Jenny Rosen" \  --data-urlencode email="jenny.rosen@example.com" \  --data-urlencode phone_number="+18888675309" \  -d "billing[address][line1]"="1234 Main Street" \  -d "billing[address][city]"="San Francisco" \  -d "billing[address][state]"=CA \  -d "billing[address][country]"=US \  -d "billing[address][postal_code]"=94111`Response`{  "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",  "object": "issuing.cardholder",  "billing": {    "address": {      "line1": "1234 Main Street",      "city": "San Francisco",      "state": "CA",      "country": "US",      "postal_code": "94111"    }  },  "company": null,  "created": 1680415995,  "email": "jenny.rosen@example.com",  "individual": null,  "livemode": false,  "metadata": {},  "name": "Jenny Rosen",  "phone_number": "+18888675309",  "redaction": null,  "requirements": {    "disabled_reason": "requirements.past_due",    "past_due": [      "individual.card_issuing.user_terms_acceptance.ip",      "individual.card_issuing.user_terms_acceptance.date",      "individual.first_name",      "individual.last_name"    ]  },  "spending_controls": {    "allowed_categories": [],    "blocked_categories": [],    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "individual"}`# Update a cardholder

Updates the specified Issuing Cardholder object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- billingobjectThe cardholder’s billing address.

Show child parameters
- emailstringThe cardholder’s email address.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- phone_numberstringThe cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.



### More parametersExpand all

- companyobject
- individualobject
- preferred_localesarray of enums
- spending_controlsobject
- statusenum

### Returns

Returns an updated Issuing Cardholder object if a valid identifier was provided.

POST/v1/issuing/cardholders/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/cardholders/ich_1MsKAB2eZvKYlo2C3eZ2BdvK \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",  "object": "issuing.cardholder",  "billing": {    "address": {      "line1": "1234 Main Street",      "city": "San Francisco",      "state": "CA",      "country": "US",      "postal_code": "94111"    }  },  "company": null,  "created": 1680415995,  "email": "jenny.rosen@example.com",  "individual": null,  "livemode": false,  "metadata": {    "order_id": "6735"  },  "name": "Jenny Rosen",  "phone_number": "+18888675309",  "redaction": null,  "requirements": {    "disabled_reason": "requirements.past_due",    "past_due": [      "individual.card_issuing.user_terms_acceptance.ip",      "individual.card_issuing.user_terms_acceptance.date",      "individual.first_name",      "individual.last_name"    ]  },  "spending_controls": {    "allowed_categories": [],    "blocked_categories": [],    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "individual"}`# Retrieve a cardholder

Retrieves an Issuing Cardholder object.

### Parameters

No parameters.

### Returns

Returns an Issuing Cardholder object if a valid identifier was provided.

GET/v1/issuing/cardholders/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/cardholders/ich_1MsKAB2eZvKYlo2C3eZ2BdvK \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",  "object": "issuing.cardholder",  "billing": {    "address": {      "line1": "1234 Main Street",      "city": "San Francisco",      "state": "CA",      "country": "US",      "postal_code": "94111"    }  },  "company": null,  "created": 1680415995,  "email": "jenny.rosen@example.com",  "individual": null,  "livemode": false,  "metadata": {},  "name": "Jenny Rosen",  "phone_number": "+18888675309",  "redaction": null,  "requirements": {    "disabled_reason": "requirements.past_due",    "past_due": [      "individual.card_issuing.user_terms_acceptance.ip",      "individual.card_issuing.user_terms_acceptance.date",      "individual.first_name",      "individual.last_name"    ]  },  "spending_controls": {    "allowed_categories": [],    "blocked_categories": [],    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "individual"}`# List all cardholders

Returns a list of Issuing Cardholder objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

No parameters.

### More parametersExpand all

- createdobject
- emailstring
- ending_beforestring
- limitinteger
- phone_numberstring
- starting_afterstring
- statusenum
- typeenum

### Returns

A dictionary with a data property that contains an array of up to limit cardholders, starting after cardholder starting_after. Each entry in the array is a separate Issuing Cardholder object. If no more cardholders are available, the resulting array will be empty.

GET/v1/issuing/cardholdersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/cardholders \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/cardholders",  "has_more": false,  "data": [    {      "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",      "object": "issuing.cardholder",      "billing": {        "address": {          "line1": "1234 Main Street",          "city": "San Francisco",          "state": "CA",          "country": "US",          "postal_code": "94111"        }      },      "company": null,      "created": 1680415995,      "email": "jenny.rosen@example.com",      "individual": null,      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "phone_number": "+18888675309",      "redaction": null,      "requirements": {        "disabled_reason": "requirements.past_due",        "past_due": [          "individual.card_issuing.user_terms_acceptance.ip",          "individual.card_issuing.user_terms_acceptance.date",          "individual.first_name",          "individual.last_name"        ]      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`