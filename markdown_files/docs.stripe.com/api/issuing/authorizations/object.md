htmlThe Authorization object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Authorization object

### Attributes

- idstringUnique identifier for the object.


- amountintegerThe total amount that was authorized or rejected. This amount is in currency and in the smallest currency unit. amount should be the same as merchant_amount, unless currency and merchant_currency are different.


- approvedbooleanWhether the authorization has been approved.


- cardobjectCard associated with this authorization.

Show child attributes
- cardholdernullablestringExpandableThe cardholder to whom this authorization belongs.


- currencyenumThe currency of the cardholder. This currency can be different from the currency presented at authorization and the merchant_currency field on this authorization. Three-letter ISO currency code, in lowercase. Must be a supported currency.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- statusenumThe current status of the authorization in its lifecycle.

Possible enum values`closed`The authorization was declined or captured through one or more transactions.

`pending`The authorization was created and is awaiting approval or was approved and is awaiting capture.

`reversed`The authorization was reversed by the merchant or expired without capture.



### More attributesExpand all

- objectstring
- amount_detailsnullableobject
- authorization_methodenum
- balance_transactionsarray of objects
- createdtimestamp
- livemodeboolean
- merchant_amountinteger
- merchant_currencyenum
- merchant_dataobject
- network_datanullableobject
- pending_requestnullableobject
- request_historyarray of objects
- tokennullablestringPreview featureExpandable
- transactionsarray of objects
- verification_dataobject
- walletnullablestring

The Authorization object`{  "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",  "object": "issuing.authorization",  "amount": 382,  "amount_details": {    "atm_fee": null  },  "approved": false,  "authorization_method": "online",  "balance_transactions": [],  "card": {    "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",    "object": "issuing.card",    "brand": "Visa",    "cancellation_reason": null,    "cardholder": {      "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",      "object": "issuing.cardholder",      "billing": {        "address": {          "city": "San Francisco",          "country": "US",          "line1": "123 Main Street",          "line2": null,          "postal_code": "94111",          "state": "CA"        }      },      "company": null,      "created": 1626425119,      "email": "jenny.rosen@example.com",      "individual": null,      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "phone_number": "+18008675309",      "redaction": null,      "requirements": {        "disabled_reason": null,        "past_due": []      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    },    "created": 1626425206,    "currency": "usd",    "exp_month": 6,    "exp_year": 2024,    "last4": "8693",    "livemode": false,    "metadata": {},    "redaction": null,    "replaced_by": null,    "replacement_for": null,    "replacement_reason": null,    "shipping": null,    "spending_controls": {      "allowed_categories": null,      "blocked_categories": null,      "spending_limits": [        {          "amount": 50000,          "categories": [],          "interval": "daily"        }      ],      "spending_limits_currency": "usd"    },    "status": "active",    "type": "virtual",    "wallets": {      "apple_pay": {        "eligible": true,        "ineligible_reason": null      },      "google_pay": {        "eligible": true,        "ineligible_reason": null      },      "primary_account_identifier": null    }  },  "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",  "created": 1630657706,  "currency": "usd",  "livemode": false,  "merchant_amount": 382,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "STRIPE",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA"  },  "metadata": {    "order_id": "6735"  },  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [    {      "amount": 382,      "amount_details": {        "atm_fee": null      },      "approved": false,      "created": 1630657706,      "currency": "usd",      "merchant_amount": 382,      "merchant_currency": "usd",      "reason": "verification_failed",      "reason_message": null    }  ],  "status": "closed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "not_provided",    "cvc_check": "mismatch",    "expiry_check": "match"  },  "wallet": null}`# Update an authorization

Updates the specified Issuing Authorization object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns an updated Issuing Authorization object if a valid identifier was provided.

POST/v1/issuing/authorizations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",  "object": "issuing.authorization",  "amount": 382,  "amount_details": {    "atm_fee": null  },  "approved": false,  "authorization_method": "online",  "balance_transactions": [],  "card": {    "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",    "object": "issuing.card",    "brand": "Visa",    "cancellation_reason": null,    "cardholder": {      "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",      "object": "issuing.cardholder",      "billing": {        "address": {          "city": "San Francisco",          "country": "US",          "line1": "123 Main Street",          "line2": null,          "postal_code": "94111",          "state": "CA"        }      },      "company": null,      "created": 1626425119,      "email": "jenny.rosen@example.com",      "individual": null,      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "phone_number": "+18008675309",      "redaction": null,      "requirements": {        "disabled_reason": null,        "past_due": []      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    },    "created": 1626425206,    "currency": "usd",    "exp_month": 6,    "exp_year": 2024,    "last4": "8693",    "livemode": false,    "metadata": {},    "redaction": null,    "replaced_by": null,    "replacement_for": null,    "replacement_reason": null,    "shipping": null,    "spending_controls": {      "allowed_categories": null,      "blocked_categories": null,      "spending_limits": [        {          "amount": 50000,          "categories": [],          "interval": "daily"        }      ],      "spending_limits_currency": "usd"    },    "status": "active",    "type": "virtual",    "wallets": {      "apple_pay": {        "eligible": true,        "ineligible_reason": null      },      "google_pay": {        "eligible": true,        "ineligible_reason": null      },      "primary_account_identifier": null    }  },  "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",  "created": 1630657706,  "currency": "usd",  "livemode": false,  "merchant_amount": 382,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "STRIPE",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA"  },  "metadata": {    "order_id": "6735"  },  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [    {      "amount": 382,      "amount_details": {        "atm_fee": null      },      "approved": false,      "created": 1630657706,      "currency": "usd",      "merchant_amount": 382,      "merchant_currency": "usd",      "reason": "verification_failed",      "reason_message": null    }  ],  "status": "closed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "not_provided",    "cvc_check": "mismatch",    "expiry_check": "match"  },  "wallet": null}`# Retrieve an authorization

Retrieves an Issuing Authorization object.

### Parameters

No parameters.

### Returns

Returns an Issuing Authorization object if a valid identifier was provided.

GET/v1/issuing/authorizations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",  "object": "issuing.authorization",  "amount": 382,  "amount_details": {    "atm_fee": null  },  "approved": false,  "authorization_method": "online",  "balance_transactions": [],  "card": {    "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",    "object": "issuing.card",    "brand": "Visa",    "cancellation_reason": null,    "cardholder": {      "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",      "object": "issuing.cardholder",      "billing": {        "address": {          "city": "San Francisco",          "country": "US",          "line1": "123 Main Street",          "line2": null,          "postal_code": "94111",          "state": "CA"        }      },      "company": null,      "created": 1626425119,      "email": "jenny.rosen@example.com",      "individual": null,      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "phone_number": "+18008675309",      "redaction": null,      "requirements": {        "disabled_reason": null,        "past_due": []      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    },    "created": 1626425206,    "currency": "usd",    "exp_month": 6,    "exp_year": 2024,    "last4": "8693",    "livemode": false,    "metadata": {},    "redaction": null,    "replaced_by": null,    "replacement_for": null,    "replacement_reason": null,    "shipping": null,    "spending_controls": {      "allowed_categories": null,      "blocked_categories": null,      "spending_limits": [        {          "amount": 50000,          "categories": [],          "interval": "daily"        }      ],      "spending_limits_currency": "usd"    },    "status": "active",    "type": "virtual",    "wallets": {      "apple_pay": {        "eligible": true,        "ineligible_reason": null      },      "google_pay": {        "eligible": true,        "ineligible_reason": null      },      "primary_account_identifier": null    }  },  "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",  "created": 1630657706,  "currency": "usd",  "livemode": false,  "merchant_amount": 382,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "STRIPE",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA"  },  "metadata": {    "order_id": "6735"  },  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [    {      "amount": 382,      "amount_details": {        "atm_fee": null      },      "approved": false,      "created": 1630657706,      "currency": "usd",      "merchant_amount": 382,      "merchant_currency": "usd",      "reason": "verification_failed",      "reason_message": null    }  ],  "status": "closed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "not_provided",    "cvc_check": "mismatch",    "expiry_check": "match"  },  "wallet": null}`# List all authorizations

Returns a list of Issuing Authorization objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

- cardstringOnly return authorizations that belong to the given card.


- cardholderstringOnly return authorizations that belong to the given cardholder.


- statusenumOnly return authorizations with the given status. One of pending, closed, or reversed.

Possible enum values`closed``pending``reversed`

### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit authorizations, starting after authorization starting_after. Each entry in the array is a separate Issuing Authorization object. If no more authorizations are available, the resulting array will be empty.

GET/v1/issuing/authorizationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/authorizations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/authorizations",  "has_more": false,  "data": [    {      "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",      "object": "issuing.authorization",      "amount": 382,      "amount_details": {        "atm_fee": null      },      "approved": false,      "authorization_method": "online",      "balance_transactions": [],      "card": {        "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",        "object": "issuing.card",        "brand": "Visa",        "cancellation_reason": null,        "cardholder": {          "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",          "object": "issuing.cardholder",          "billing": {            "address": {              "city": "San Francisco",              "country": "US",              "line1": "123 Main Street",              "line2": null,              "postal_code": "94111",              "state": "CA"            }          },          "company": null,          "created": 1626425119,          "email": "jenny.rosen@example.com",          "individual": null,          "livemode": false,          "metadata": {},          "name": "Jenny Rosen",          "phone_number": "+18008675309",          "redaction": null,          "requirements": {            "disabled_reason": null,            "past_due": []          },          "spending_controls": {            "allowed_categories": [],            "blocked_categories": [],            "spending_limits": [],            "spending_limits_currency": null          },          "status": "active",          "type": "individual"        },        "created": 1626425206,        "currency": "usd",        "exp_month": 6,        "exp_year": 2024,        "last4": "8693",        "livemode": false,        "metadata": {},        "redaction": null,        "replaced_by": null,        "replacement_for": null,        "replacement_reason": null,        "shipping": null,        "spending_controls": {          "allowed_categories": null,          "blocked_categories": null,          "spending_limits": [            {              "amount": 50000,              "categories": [],              "interval": "daily"            }          ],          "spending_limits_currency": "usd"        },        "status": "active",        "type": "virtual",        "wallets": {          "apple_pay": {            "eligible": true,            "ineligible_reason": null          },          "google_pay": {            "eligible": true,            "ineligible_reason": null          },          "primary_account_identifier": null        }      },      "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",      "created": 1630657706,      "currency": "usd",      "livemode": false,      "merchant_amount": 382,      "merchant_currency": "usd",      "merchant_data": {        "category": "computer_software_stores",        "category_code": "5734",        "city": "SAN FRANCISCO",        "country": "US",        "name": "STRIPE",        "network_id": "1234567890",        "postal_code": "94103",        "state": "CA"      },      "metadata": {        "order_id": "6735"      },      "network_data": null,      "pending_request": null,      "redaction": null,      "request_history": [        {          "amount": 382,          "amount_details": {            "atm_fee": null          },          "approved": false,          "created": 1630657706,          "currency": "usd",          "merchant_amount": 382,          "merchant_currency": "usd",          "reason": "verification_failed",          "reason_message": null        }      ],      "status": "closed",      "transactions": [],      "verification_data": {        "address_line1_check": "not_provided",        "address_postal_code_check": "not_provided",        "cvc_check": "mismatch",        "expiry_check": "match"      },      "wallet": null    }    {...}    {...}  ],}`# Approve an authorization

[Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the real-time authorization flow. This method is deprecated. Instead, respond directly to the webhook request to approve an authorization.

### Parameters

- amountintegerIf the authorization’s pending_request.is_amount_controllable property is true, you may provide this value to control how much to hold for the authorization. Must be positive (use decline to decline an authorization request).


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns an approved Issuing Authorization object.

POST/v1/issuing/authorizations/:id/approveServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/issuing/authorizations/iauth_1MvSKeLkdIwHu7ixKr8rO1HV/approve \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "iauth_1MvSKeLkdIwHu7ixKr8rO1HV",  "object": "issuing.authorization",  "amount": 0,  "amount_details": {    "atm_fee": null  },  "approved": true,  "authorization_method": "keyed_in",  "balance_transactions": [],  "card": {    "id": "ic_1MvSKeLkdIwHu7ixFANTvxgn",    "object": "issuing.card",    "brand": "Visa",    "cancellation_reason": null,    "cardholder": {      "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",      "object": "issuing.cardholder",      "billing": {        "address": {          "city": "Anytown",          "country": "US",          "line1": "123 Main Street",          "line2": null,          "postal_code": "12345",          "state": "CA"        }      },      "company": null,      "created": 1680415995,      "email": null,      "individual": null,      "livemode": false,      "metadata": {},      "name": "John Doe",      "phone_number": null,      "requirements": {        "disabled_reason": "requirements.past_due",        "past_due": [          "individual.card_issuing.user_terms_acceptance.ip",          "individual.card_issuing.user_terms_acceptance.date",          "individual.first_name",          "individual.last_name"        ]      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    },    "created": 1681162380,    "currency": "usd",    "exp_month": 8,    "exp_year": 2024,    "last4": "4242",    "livemode": false,    "metadata": {},    "replaced_by": null,    "replacement_for": null,    "replacement_reason": null,    "shipping": null,    "spending_controls": {      "allowed_categories": null,      "blocked_categories": null,      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "physical",    "wallets": {      "apple_pay": {        "eligible": false,        "ineligible_reason": "missing_cardholder_contact"      },      "google_pay": {        "eligible": false,        "ineligible_reason": "missing_cardholder_contact"      },      "primary_account_identifier": null    }  },  "cardholder": null,  "created": 1681162380,  "currency": "usd",  "livemode": false,  "merchant_amount": 0,  "merchant_currency": "usd",  "merchant_data": {    "category": "taxicabs_limousines",    "category_code": "4121",    "city": "San Francisco",    "country": "US",    "name": "Rocket Rides",    "network_id": "1234567890",    "postal_code": "94107",    "state": "CA"  },  "metadata": {},  "network_data": null,  "pending_request": {    "amount": 700,    "amount_details": {      "atm_fee": null    },    "currency": "usd",    "is_amount_controllable": false,    "merchant_amount": 700,    "merchant_currency": "usd"  },  "request_history": [],  "status": "pending",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "match",    "cvc_check": "match",    "expiry_check": "match"  },  "wallet": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`