htmlThe Card object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Card object

### Attributes

- idstringUnique identifier for the object.


- cancellation_reasonnullableenumThe reason why the card was canceled.

Possible enum values`design_rejected`The design of this card was rejected by Stripe for violating our partner guidelines.

`lost`The card was lost.

`stolen`The card was stolen.


- cardholderobjectThe Cardholder object to which the card belongs.

Show child attributes
- currencyenumThree-letter ISO currency code, in lowercase. Supported currencies are usd in the US, eur in the EU, and gbp in the UK.


- exp_monthintegerThe expiration month of the card.


- exp_yearintegerThe expiration year of the card.


- last4stringThe last 4 digits of the card number.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- statusenumWhether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive.

Possible enum values`active`The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

`canceled`The card will decline authorizations, and no authorization object will be recorded. This status is permanent.

`inactive`The card will decline authorizations with the card_inactive reason.


- typeenumThe type of the card.

Possible enum values`physical`A physical card will be printed and shipped. It can be used at physical terminals.

`virtual`No physical card will be printed. The card can be used online and can be added to digital wallets.



### More attributesExpand all

- objectstring
- brandstring
- createdtimestamp
- cvcnullablestringExpandable
- livemodeboolean
- numbernullablestringExpandable
- personalization_designnullablestringPreview featureExpandable
- replaced_bynullablestringExpandable
- replacement_fornullablestringExpandable
- replacement_reasonnullableenum
- shippingnullableobject
- spending_controlsobject
- walletsnullableobject

The Card object`{  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",  "object": "issuing.card",  "brand": "Visa",  "cancellation_reason": null,  "cardholder": {    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",    "object": "issuing.cardholder",    "billing": {      "address": {        "city": "Anytown",        "country": "US",        "line1": "123 Main Street",        "line2": null,        "postal_code": "12345",        "state": "CA"      }    },    "company": null,    "created": 1680415995,    "email": null,    "individual": null,    "livemode": false,    "metadata": {},    "name": "John Doe",    "phone_number": null,    "requirements": {      "disabled_reason": "requirements.past_due",      "past_due": [        "individual.card_issuing.user_terms_acceptance.ip",        "individual.card_issuing.user_terms_acceptance.date",        "individual.first_name",        "individual.last_name"      ]    },    "spending_controls": {      "allowed_categories": [],      "blocked_categories": [],      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "individual"  },  "created": 1681163868,  "currency": "usd",  "exp_month": 8,  "exp_year": 2024,  "last4": "4242",  "livemode": false,  "metadata": {},  "replaced_by": null,  "replacement_for": null,  "replacement_reason": null,  "shipping": null,  "spending_controls": {    "allowed_categories": null,    "blocked_categories": null,    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "virtual",  "wallets": {    "apple_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "google_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "primary_account_identifier": null  }}`# Create a card

Creates an Issuing Card object.

### Parameters

- currencystringRequiredThe currency for the card.


- typeenumRequiredThe type of card to issue. Possible values are physical or virtual.

Possible enum values`physical`A physical card will be printed and shipped. It can be used at physical terminals.

`virtual`No physical card will be printed. The card can be used online and can be added to digital wallets.


- cardholderstringRequiredThe Cardholder object with which the card will be associated.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statusenumWhether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive.

Possible enum values`active`The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

`inactive`The card will decline authorizations with the card_inactive reason.



### More parametersExpand all

- personalization_designstringPreview feature
- pinobject
- replacement_forstring
- replacement_reasonenum
- second_linestring
- shippingobject
- spending_controlsobject

### Returns

Returns an Issuing Card object if creation succeeds.

POST/v1/issuing/cardsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/cards \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d cardholder=ich_1MsKAB2eZvKYlo2C3eZ2BdvK \  -d currency=usd \  -d type=virtual`Response`{  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",  "object": "issuing.card",  "brand": "Visa",  "cancellation_reason": null,  "cardholder": {    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",    "object": "issuing.cardholder",    "billing": {      "address": {        "city": "Anytown",        "country": "US",        "line1": "123 Main Street",        "line2": null,        "postal_code": "12345",        "state": "CA"      }    },    "company": null,    "created": 1680415995,    "email": null,    "individual": null,    "livemode": false,    "metadata": {},    "name": "John Doe",    "phone_number": null,    "requirements": {      "disabled_reason": "requirements.past_due",      "past_due": [        "individual.card_issuing.user_terms_acceptance.ip",        "individual.card_issuing.user_terms_acceptance.date",        "individual.first_name",        "individual.last_name"      ]    },    "spending_controls": {      "allowed_categories": [],      "blocked_categories": [],      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "individual"  },  "created": 1681163868,  "currency": "usd",  "exp_month": 8,  "exp_year": 2024,  "last4": "4242",  "livemode": false,  "metadata": {},  "replaced_by": null,  "replacement_for": null,  "replacement_reason": null,  "shipping": null,  "spending_controls": {    "allowed_categories": null,    "blocked_categories": null,    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "virtual",  "wallets": {    "apple_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "google_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "primary_account_identifier": null  }}`# Update a card

Updates the specified Issuing Card object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- cancellation_reasonenumReason why the status of this card is canceled.

Possible enum values`lost`The card was lost.

`stolen`The card was stolen.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statusenumDictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive. If this card is being canceled because it was lost or stolen, this information should be provided as cancellation_reason.

Possible enum values`active`The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

`canceled`The card will decline authorizations, and no authorization object will be recorded. This status is permanent.

`inactive`The card will decline authorizations with the card_inactive reason.



### More parametersExpand all

- pinobject
- spending_controlsobject

### Returns

Returns an updated Issuing Card object if a valid identifier was provided.

POST/v1/issuing/cards/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/cards/ic_1MvSieLkdIwHu7ixn6uuO0Xu \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",  "object": "issuing.card",  "brand": "Visa",  "cancellation_reason": null,  "cardholder": {    "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",    "object": "issuing.cardholder",    "billing": {      "address": {        "city": "Anytown",        "country": "US",        "line1": "123 Main Street",        "line2": null,        "postal_code": "12345",        "state": "CA"      }    },    "company": null,    "created": 1680415995,    "email": null,    "individual": null,    "livemode": false,    "metadata": {},    "name": "John Doe",    "phone_number": null,    "requirements": {      "disabled_reason": "requirements.past_due",      "past_due": [        "individual.card_issuing.user_terms_acceptance.ip",        "individual.card_issuing.user_terms_acceptance.date",        "individual.first_name",        "individual.last_name"      ]    },    "spending_controls": {      "allowed_categories": [],      "blocked_categories": [],      "spending_limits": [],      "spending_limits_currency": null    },    "status": "active",    "type": "individual"  },  "created": 1681163868,  "currency": "usd",  "exp_month": 8,  "exp_year": 2024,  "last4": "4242",  "livemode": false,  "metadata": {    "order_id": "6735"  },  "replaced_by": null,  "replacement_for": null,  "replacement_reason": null,  "shipping": null,  "spending_controls": {    "allowed_categories": null,    "blocked_categories": null,    "spending_limits": [],    "spending_limits_currency": null  },  "status": "active",  "type": "virtual",  "wallets": {    "apple_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "google_pay": {      "eligible": false,      "ineligible_reason": "missing_cardholder_contact"    },    "primary_account_identifier": null  }}`# Retrieve a card

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

GET/v1/issuing/cardsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/cards \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/cards",  "has_more": false,  "data": [    {      "id": "ic_1MvSieLkdIwHu7ixn6uuO0Xu",      "object": "issuing.card",      "brand": "Visa",      "cancellation_reason": null,      "cardholder": {        "id": "ich_1MsKAB2eZvKYlo2C3eZ2BdvK",        "object": "issuing.cardholder",        "billing": {          "address": {            "city": "Anytown",            "country": "US",            "line1": "123 Main Street",            "line2": null,            "postal_code": "12345",            "state": "CA"          }        },        "company": null,        "created": 1680415995,        "email": null,        "individual": null,        "livemode": false,        "metadata": {},        "name": "John Doe",        "phone_number": null,        "requirements": {          "disabled_reason": "requirements.past_due",          "past_due": [            "individual.card_issuing.user_terms_acceptance.ip",            "individual.card_issuing.user_terms_acceptance.date",            "individual.first_name",            "individual.last_name"          ]        },        "spending_controls": {          "allowed_categories": [],          "blocked_categories": [],          "spending_limits": [],          "spending_limits_currency": null        },        "status": "active",        "type": "individual"      },      "created": 1681163868,      "currency": "usd",      "exp_month": 8,      "exp_year": 2024,      "last4": "4242",      "livemode": false,      "metadata": {},      "replaced_by": null,      "replacement_for": null,      "replacement_reason": null,      "shipping": null,      "spending_controls": {        "allowed_categories": null,        "blocked_categories": null,        "spending_limits": [],        "spending_limits_currency": null      },      "status": "active",      "type": "virtual",      "wallets": {        "apple_pay": {          "eligible": false,          "ineligible_reason": "missing_cardholder_contact"        },        "google_pay": {          "eligible": false,          "ineligible_reason": "missing_cardholder_contact"        },        "primary_account_identifier": null      }    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`