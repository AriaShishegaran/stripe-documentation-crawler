htmlRetrieve a card | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a card

Retrieves an Issuing Card object.

### Parameters

No parameters.

### Returns

Returns an Issuing Card object if a valid identifier was provided. When requesting the ID of a card that has been deleted, a subset of the card’s information will be returned, including a deleted property, which will be true.

GET/v1/issuing/cards/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",  "object": "issuing.card",  "brand": "Visa",  "cancellation_reason": null,  "cardholder": {    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",    "object": "issuing.cardholder",    "billing": {      "address": {        "city": "Anytown",        "country": "US",        "line1": "123 Main Street",        "line2": null,        "postal_code": "12345",        "state": "CA"      }    },    "company": null,    "created": 1680415995,    "email": null,    "individual": null,    "livemode": false,    "metadata": {},    "name": "John Doe",    "phone_number": null,    "requirements": {      "disabled_reason": "requirements.past_due",      "past_due": [        "individual.card_issuing.user_terms_acceptance.ip",        "individual.card_issuing.user_terms_acceptance.date",        "individual.first_name",        "individual.last_name"      ]    },    "spending_controls": {      "allowed_categories": [],      "blocked_categories": [],      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "individual"  },  "created": 1681163868,  "currency": "usd",  "exp_month": 8,  "exp_year": 2024,  "last4": "4242",  "livemode": false,  "metadata": {},  "replaced_by": null,  "replacement_for": null,  "replacement_reason": null,  "shipping": null,  "spending_controls": {    "allowed_categories": null,    "blocked_categories": null,    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "virtual",  "wallets": {    "apple_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "google_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "primary_account_identifier": null  }}`# List all cards

Returns a list of Issuing Card objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

- cardholderstringOnly return cards belonging to the Cardholder with the provided ID.


- typeenumOnly return cards that have the given type. One of virtual or physical.

Possible enum values`physical`A physical card will be printed and shipped. It can be used at physical terminals.

`virtual`No physical card will be printed. The card can be used online and can be added to digital wallets.



### More parametersExpand all

- createdobject
- ending_beforestring
- exp_monthinteger
- exp_yearinteger
- last4string
- limitinteger
- starting_afterstring
- statusenum

### Returns

A dictionary with a data property that contains an array of up to limit cards, starting after card starting_after. Each entry in the array is a separate Issuing Card object. If no more cards are available, the resulting array will be empty.

GET/v1/issuing/cardsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/cards \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/cards",  "has_more": false,  "data": [    {      "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",      "object": "issuing.card",      "brand": "Visa",      "cancellation_reason": null,      "cardholder": {        "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",        "object": "issuing.cardholder",        "billing": {          "address": {            "city": "Anytown",            "country": "US",            "line1": "123 Main Street",            "line2": null,            "postal_code": "12345",            "state": "CA"          }        },        "company": null,        "created": 1680415995,        "email": null,        "individual": null,        "livemode": false,        "metadata": {},        "name": "John Doe",        "phone_number": null,        "requirements": {          "disabled_reason": "requirements.past_due",          "past_due": [            "individual.card_issuing.user_terms_acceptance.ip",            "individual.card_issuing.user_terms_acceptance.date",            "individual.first_name",            "individual.last_name"          ]        },        "spending_controls": {          "allowed_categories": [],          "blocked_categories": [],          "spending_limits": [],          "spending_limits_currency": null        },        "status": "active",        "type": "individual"      },      "created": 1681163868,      "currency": "usd",      "exp_month": 8,      "exp_year": 2024,      "last4": "4242",      "livemode": false,      "metadata": {},      "replaced_by": null,      "replacement_for": null,      "replacement_reason": null,      "shipping": null,      "spending_controls": {        "allowed_categories": null,        "blocked_categories": null,        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "virtual",      "wallets": {        "apple_pay": {          "eligible": false,          "ineligible_reason": "missing_cardholder_contact"        },        "google_pay": {          "eligible": false,          "ineligible_reason": "missing_cardholder_contact"        },        "primary_account_identifier": null      }    }    {...}    {...}  ],}`# Deliver a testmode cardTest helper

Updates the shipping status of the specified Issuing Card object to delivered.

### Parameters

No parameters.

### Returns

Returns an updated Issuing Card object.

POST/v1/test_helpers/issuing/cards/:id/shipping/deliverServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu/shipping/deliver \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",  "object": "issuing.card",  "brand": "Visa",  "cancellation_reason": null,  "cardholder": {    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",    "object": "issuing.cardholder",    "billing": {      "address": {        "city": "Anytown",        "country": "US",        "line1": "123 Main Street",        "line2": null,        "postal_code": "12345",        "state": "CA"      }    },    "company": null,    "created": 1680415995,    "email": null,    "individual": null,    "livemode": false,    "metadata": {},    "name": "John Doe",    "phone_number": null,    "requirements": {      "disabled_reason": "requirements.past_due",      "past_due": [        "individual.card_issuing.user_terms_acceptance.ip",        "individual.card_issuing.user_terms_acceptance.date",        "individual.first_name",        "individual.last_name"      ]    },    "spending_controls": {      "allowed_categories": [],      "blocked_categories": [],      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "individual"  },  "created": 1681163868,  "currency": "usd",  "exp_month": 8,  "exp_year": 2024,  "last4": "4242",  "livemode": false,  "metadata": {},  "replaced_by": null,  "replacement_for": null,  "replacement_reason": null,  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "postal_code": "94111",      "state": "CA"    },    "carrier": "usps",    "eta": 1655362799,    "name": "Jenny Rosen",    "service": "standard",    "status": "delivered",    "type": "individual"  },  "spending_controls": {    "allowed_categories": null,    "blocked_categories": null,    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "physical",  "wallets": {    "apple_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "google_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "primary_account_identifier": null  }}`# Fail a testmode cardTest helper

Updates the shipping status of the specified Issuing Card object to failure.

### Parameters

No parameters.

### Returns

Returns an updated Issuing Card object.

POST/v1/test_helpers/issuing/cards/:id/shipping/failServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu/shipping/fail \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",  "object": "issuing.card",  "brand": "Visa",  "cancellation_reason": null,  "cardholder": {    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",    "object": "issuing.cardholder",    "billing": {      "address": {        "city": "Anytown",        "country": "US",        "line1": "123 Main Street",        "line2": null,        "postal_code": "12345",        "state": "CA"      }    },    "company": null,    "created": 1680415995,    "email": null,    "individual": null,    "livemode": false,    "metadata": {},    "name": "John Doe",    "phone_number": null,    "requirements": {      "disabled_reason": "requirements.past_due",      "past_due": [        "individual.card_issuing.user_terms_acceptance.ip",        "individual.card_issuing.user_terms_acceptance.date",        "individual.first_name",        "individual.last_name"      ]    },    "spending_controls": {      "allowed_categories": [],      "blocked_categories": [],      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "individual"  },  "created": 1681163868,  "currency": "usd",  "exp_month": 8,  "exp_year": 2024,  "last4": "4242",  "livemode": false,  "metadata": {},  "replaced_by": null,  "replacement_for": null,  "replacement_reason": null,  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "postal_code": "94111",      "state": "CA"    },    "carrier": "usps",    "eta": 1655362799,    "name": "Jenny Rosen",    "service": "standard",    "status": "failed",    "type": "individual"  },  "spending_controls": {    "allowed_categories": null,    "blocked_categories": null,    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "physical",  "wallets": {    "apple_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "google_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "primary_account_identifier": null  }}`# Return a testmode cardTest helper

Updates the shipping status of the specified Issuing Card object to returned.

### Parameters

No parameters.

### Returns

Returns an updated Issuing Card object.

POST/v1/test_helpers/issuing/cards/:id/shipping/returnServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu/shipping/return \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",  "object": "issuing.card",  "brand": "Visa",  "cancellation_reason": null,  "cardholder": {    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",    "object": "issuing.cardholder",    "billing": {      "address": {        "city": "Anytown",        "country": "US",        "line1": "123 Main Street",        "line2": null,        "postal_code": "12345",        "state": "CA"      }    },    "company": null,    "created": 1680415995,    "email": null,    "individual": null,    "livemode": false,    "metadata": {},    "name": "John Doe",    "phone_number": null,    "requirements": {      "disabled_reason": "requirements.past_due",      "past_due": [        "individual.card_issuing.user_terms_acceptance.ip",        "individual.card_issuing.user_terms_acceptance.date",        "individual.first_name",        "individual.last_name"      ]    },    "spending_controls": {      "allowed_categories": [],      "blocked_categories": [],      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "individual"  },  "created": 1681163868,  "currency": "usd",  "exp_month": 8,  "exp_year": 2024,  "last4": "4242",  "livemode": false,  "metadata": {},  "replaced_by": null,  "replacement_for": null,  "replacement_reason": null,  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "postal_code": "94111",      "state": "CA"    },    "carrier": "usps",    "eta": 1655362799,    "name": "Jenny Rosen",    "service": "standard",    "status": "returned",    "type": "individual"  },  "spending_controls": {    "allowed_categories": null,    "blocked_categories": null,    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "physical",  "wallets": {    "apple_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "google_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "primary_account_identifier": null  }}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`