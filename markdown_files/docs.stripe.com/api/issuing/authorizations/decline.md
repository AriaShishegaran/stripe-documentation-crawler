htmlDecline an authorization | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Decline an authorization

[Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the real time authorization flow. This method is deprecated. Instead, respond directly to the webhook request to decline an authorization.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a declined Issuing Authorization object.

POST/v1/issuing/authorizations/:id/declineServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn/decline \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "iauth_1JVXl82eZvKYlo2CPIiWlzrn",  "object": "issuing.authorization",  "amount": 382,  "amount_details": {    "atm_fee": null  },  "approved": false,  "authorization_method": "online",  "balance_transactions": [],  "card": {    "id": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",    "object": "issuing.card",    "brand": "Visa",    "cancellation_reason": null,    "cardholder": {      "id": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",      "object": "issuing.cardholder",      "billing": {        "address": {          "city": "San Francisco",          "country": "US",          "line1": "123 Main Street",          "line2": null,          "postal_code": "94111",          "state": "CA"        }      },      "company": null,      "created": 1626425119,      "email": "jenny.rosen@example.com",      "individual": null,      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "phone_number": "+18008675309",      "redaction": null,      "requirements": {        "disabled_reason": null,        "past_due": []      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    },    "created": 1626425206,    "currency": "usd",    "exp_month": 6,    "exp_year": 2024,    "last4": "8693",    "livemode": false,    "metadata": {},    "redaction": null,    "replaced_by": null,    "replacement_for": null,    "replacement_reason": null,    "shipping": null,    "spending_controls": {      "allowed_categories": null,      "blocked_categories": null,      "spending_limits": [        {          "amount": 50000,          "categories": [],          "interval": "daily"        }      ],      "spending_limits_currency": "usd"    },    "status": "active",    "type": "virtual",    "wallets": {      "apple_pay": {        "eligible": true,        "ineligible_reason": null      },      "google_pay": {        "eligible": true,        "ineligible_reason": null      },      "primary_account_identifier": null    }  },  "cardholder": "ich_1JDmfb2eZvKYlo2CwHUgaAxU",  "created": 1630657706,  "currency": "usd",  "livemode": false,  "merchant_amount": 382,  "merchant_currency": "usd",  "merchant_data": {    "category": "computer_software_stores",    "category_code": "5734",    "city": "SAN FRANCISCO",    "country": "US",    "name": "STRIPE",    "network_id": "1234567890",    "postal_code": "94103",    "state": "CA"  },  "metadata": {    "order_id": "6735"  },  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [    {      "amount": 382,      "amount_details": {        "atm_fee": null      },      "approved": false,      "created": 1630657706,      "currency": "usd",      "merchant_amount": 382,      "merchant_currency": "usd",      "reason": "verification_failed",      "reason_message": null    }  ],  "status": "closed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "not_provided",    "cvc_check": "mismatch",    "expiry_check": "match"  },  "wallet": null}`# Create a test-mode authorizationTest helper

Create a test-mode authorization.

### Parameters

- amountintegerRequiredThe total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card’s currency, and in the smallest currency unit.


- cardstringRequiredCard associated with this authorization.


- currencyenumThe currency of the authorization. If not provided, defaults to the currency of the card. Three-letter ISO currency code, in lowercase. Must be a supported currency.



### More parametersExpand all

- amount_detailsobject
- authorization_methodenum
- is_amount_controllableboolean
- merchant_dataobject
- network_dataobject
- verification_dataobject
- walletenum

### Returns

An Authorization object

POST/v1/test_helpers/issuing/authorizationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1000 \  -d card=ic_1Nsse72eZvKYlo2CWBGm2WQ5`Response`{  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",  "object": "issuing.authorization",  "amount": 1000,  "amount_details": {    "atm_fee": null,    "cashback_amount": null  },  "approved": true,  "authorization_method": "keyed_in",  "balance_transactions": [],  "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",  "created": 1540586461,  "currency": "usd",  "livemode": false,  "merchant_amount": 0,  "merchant_currency": "usd",  "merchant_data": {    "category": "taxicabs_limousines",    "category_code": "4121",    "city": "San Francisco",    "country": "US",    "name": "Rocket Rides",    "network_id": "1234567890",    "postal_code": "94107",    "state": "CA",    "terminal_id": null  },  "metadata": {},  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [],  "status": "reversed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "match",    "cvc_check": "match",    "expiry_check": "match"  },  "wallet": null}`# Capture a test-mode authorizationTest helper

Capture a test-mode authorization.

### Parameters

- capture_amountintegerThe amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the smallest currency unit.


- close_authorizationbooleanWhether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows.


- purchase_detailsobjectAdditional purchase information that is optionally provided by the merchant.

Show child parameters

### Returns

An Authorization object.

POST/v1/test_helpers/issuing/authorizations/:id/captureServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/authorizations/iauth_1DPc772eZvKYlo2C6avLyZ25/capture \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",  "object": "issuing.authorization",  "amount": 0,  "amount_details": {    "atm_fee": null,    "cashback_amount": null  },  "approved": true,  "authorization_method": "keyed_in",  "balance_transactions": [],  "card": {    "id": "ic_1FEiQC2eZvKYlo2CtahKepKy",    "object": "issuing.card",    "brand": "Visa",    "cancellation_reason": null,    "cardholder": {      "id": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",      "object": "issuing.cardholder",      "billing": {        "address": {          "city": "Beverly Hills",          "country": "US",          "line1": "123 Fake St",          "line2": "Apt 3",          "postal_code": "90210",          "state": "CA"        }      },      "company": null,      "created": 1528992903,      "email": "jenny@example.com",      "individual": null,      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "phone_number": "+18008675309",      "preferred_locales": [],      "redaction": null,      "requirements": {        "disabled_reason": null,        "past_due": []      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    },    "created": 1567541772,    "currency": "usd",    "exp_month": 12,    "exp_year": 2020,    "last4": "4242",    "livemode": false,    "metadata": {      "status": "canceled"    },    "redaction": null,    "replaced_by": null,    "replacement_for": null,    "replacement_reason": null,    "shipping": null,    "spending_controls": {      "allowed_categories": null,      "blocked_categories": null,      "spending_limits": [],      "spending_limits_currency": null    },    "status": "canceled",    "type": "physical",    "wallets": {      "apple_pay": {        "eligible": true,        "ineligible_reason": null      },      "google_pay": {        "eligible": false,        "ineligible_reason": "missing_agreement"      },      "primary_account_identifier": null    }  },  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",  "created": 1540586461,  "currency": "usd",  "livemode": false,  "merchant_amount": 0,  "merchant_currency": "usd",  "merchant_data": {    "category": "taxicabs_limousines",    "category_code": "4121",    "city": "San Francisco",    "country": "US",    "name": "Rocket Rides",    "network_id": "1234567890",    "postal_code": "94107",    "state": "CA",    "terminal_id": null  },  "metadata": {},  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [],  "status": "reversed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "match",    "cvc_check": "match",    "expiry_check": "match"  },  "wallet": null}`# Expire a test-mode authorizationTest helper

Expire a test-mode Authorization.

### Parameters

No parameters.

### Returns

An Authorization object

POST/v1/test_helpers/issuing/authorizations/:id/expireServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/authorizations/iauth_1DPc772eZvKYlo2C6avLyZ25/expire \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",  "object": "issuing.authorization",  "amount": 0,  "amount_details": {    "atm_fee": null,    "cashback_amount": null  },  "approved": true,  "authorization_method": "keyed_in",  "balance_transactions": [],  "card": {    "id": "ic_1FEiQC2eZvKYlo2CtahKepKy",    "object": "issuing.card",    "brand": "Visa",    "cancellation_reason": null,    "cardholder": {      "id": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",      "object": "issuing.cardholder",      "billing": {        "address": {          "city": "Beverly Hills",          "country": "US",          "line1": "123 Fake St",          "line2": "Apt 3",          "postal_code": "90210",          "state": "CA"        }      },      "company": null,      "created": 1528992903,      "email": "jenny@example.com",      "individual": null,      "livemode": false,      "metadata": {},      "name": "Jenny Rosen",      "phone_number": "+18008675309",      "preferred_locales": [],      "redaction": null,      "requirements": {        "disabled_reason": null,        "past_due": []      },      "spending_controls": {        "allowed_categories": [],        "blocked_categories": [],        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "individual"    },    "created": 1567541772,    "currency": "usd",    "exp_month": 12,    "exp_year": 2020,    "last4": "4242",    "livemode": false,    "metadata": {      "status": "canceled"    },    "redaction": null,    "replaced_by": null,    "replacement_for": null,    "replacement_reason": null,    "shipping": null,    "spending_controls": {      "allowed_categories": null,      "blocked_categories": null,      "spending_limits": [],      "spending_limits_currency": null    },    "status": "canceled",    "type": "physical",    "wallets": {      "apple_pay": {        "eligible": true,        "ineligible_reason": null      },      "google_pay": {        "eligible": false,        "ineligible_reason": "missing_agreement"      },      "primary_account_identifier": null    }  },  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",  "created": 1540586461,  "currency": "usd",  "livemode": false,  "merchant_amount": 0,  "merchant_currency": "usd",  "merchant_data": {    "category": "taxicabs_limousines",    "category_code": "4121",    "city": "San Francisco",    "country": "US",    "name": "Rocket Rides",    "network_id": "1234567890",    "postal_code": "94107",    "state": "CA",    "terminal_id": null  },  "metadata": {},  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [],  "status": "reversed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "match",    "cvc_check": "match",    "expiry_check": "match"  },  "wallet": null}`# Increment a test-mode authorizationTest helper

Increment a test-mode Authorization.

### Parameters

- increment_amountintegerRequiredThe amount to increment the authorization by. This amount is in the authorization currency and in the smallest currency unit.


- is_amount_controllablebooleanIf set true, you may provide amount to control how much to hold for the authorization.



### Returns

An Authorization object

POST/v1/test_helpers/issuing/authorizations/:id/incrementServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/issuing/authorizations/iauth_1DPc772eZvKYlo2C6avLyZ25/increment \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d increment_amount=1000`Response`{  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",  "object": "issuing.authorization",  "amount": 1000,  "amount_details": {    "atm_fee": null,    "cashback_amount": null  },  "approved": true,  "authorization_method": "keyed_in",  "balance_transactions": [],  "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",  "created": 1540586461,  "currency": "usd",  "livemode": false,  "merchant_amount": 0,  "merchant_currency": "usd",  "merchant_data": {    "category": "taxicabs_limousines",    "category_code": "4121",    "city": "San Francisco",    "country": "US",    "name": "Rocket Rides",    "network_id": "1234567890",    "postal_code": "94107",    "state": "CA",    "terminal_id": null  },  "metadata": {},  "network_data": null,  "pending_request": null,  "redaction": null,  "request_history": [],  "status": "reversed",  "transactions": [],  "verification_data": {    "address_line1_check": "not_provided",    "address_postal_code_check": "match",    "cvc_check": "match",    "expiry_check": "match"  },  "wallet": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`