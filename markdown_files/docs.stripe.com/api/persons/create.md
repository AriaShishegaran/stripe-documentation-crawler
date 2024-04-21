htmlCreate a person | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a person

Creates a new person.

### Parameters

- addressobjectThe person’s address.

Show child parameters
- dobobjectThe person’s date of birth.

Show child parameters
- emailstringThe person’s email address.


- first_namestringThe person’s first name.


- id_numberstringThe person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a PII token provided by Stripe.js.


- last_namestringThe person’s last name.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- phonestringThe person’s phone number.


- relationshipobjectThe relationship that this person has with the account’s legal entity.

Show child parameters
- ssn_last_4stringThe last four digits of the person’s Social Security number (U.S. only).



### More parametersExpand all

- additional_tos_acceptancesobject
- address_kanaobject
- address_kanjiobject
- documentsobject
- first_name_kanastring
- first_name_kanjistring
- full_name_aliasesarray of strings
- genderenum
- id_number_secondarystring
- last_name_kanastring
- last_name_kanjistring
- maiden_namestring
- nationalitystring
- person_tokenstring
- political_exposurestring
- registered_addressobject
- verificationobject

### Returns

Returns a person object.

POST/v1/accounts/:id/personsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "person_1N9XNb2eZvKYlo2CjPX7xF6F",  "object": "person",  "account": "acct_1032D82eZvKYlo2C",  "created": 1684518375,  "dob": {    "day": null,    "month": null,    "year": null  },  "first_name": null,  "future_requirements": {    "alternatives": [],    "currently_due": [],    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "id_number_provided": false,  "last_name": null,  "metadata": {},  "relationship": {    "director": false,    "executive": false,    "owner": false,    "percent_ownership": null,    "representative": false,    "title": null  },  "requirements": {    "alternatives": [],    "currently_due": [],    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "ssn_last_4_provided": false,  "verification": {    "additional_document": {      "back": null,      "details": null,      "details_code": null,      "front": null    },    "details": null,    "details_code": null,    "document": {      "back": null,      "details": null,      "details_code": null,      "front": null    },    "status": "unverified"  }}`# Update a person

Updates an existing person.

### Parameters

- addressobjectThe person’s address.

Show child parameters
- dobobjectThe person’s date of birth.

Show child parameters
- emailstringThe person’s email address.


- first_namestringThe person’s first name.


- id_numberstringThe person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a PII token provided by Stripe.js.


- last_namestringThe person’s last name.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- phonestringThe person’s phone number.


- relationshipobjectThe relationship that this person has with the account’s legal entity.

Show child parameters
- ssn_last_4stringThe last four digits of the person’s Social Security number (U.S. only).



### More parametersExpand all

- additional_tos_acceptancesobject
- address_kanaobject
- address_kanjiobject
- documentsobject
- first_name_kanastring
- first_name_kanjistring
- full_name_aliasesarray of strings
- genderenum
- id_number_secondarystring
- last_name_kanastring
- last_name_kanjistring
- maiden_namestring
- nationalitystring
- person_tokenstring
- political_exposurestring
- registered_addressobject
- verificationobject

### Returns

Returns a person object.

POST/v1/accounts/:id/persons/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",  "person": "person_1MqjB62eZvKYlo2CaeEJzKVR",  "object": "person",  "account": "acct_1032D82eZvKYlo2C",  "created": 1680035496,  "dob": {    "day": null,    "month": null,    "year": null  },  "first_name": "Jane",  "future_requirements": {    "alternatives": [],    "currently_due": [],    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "id_number_provided": false,  "last_name": "Diaz",  "metadata": {    "order_id": "6735"  },  "relationship": {    "director": false,    "executive": false,    "owner": false,    "percent_ownership": null,    "representative": false,    "title": null  },  "requirements": {    "alternatives": [],    "currently_due": [],    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "ssn_last_4_provided": false,  "verification": {    "additional_document": {      "back": null,      "details": null,      "details_code": null,      "front": null    },    "details": null,    "details_code": null,    "document": {      "back": null,      "details": null,      "details_code": null,      "front": null    },    "status": "unverified"  }}`# Retrieve a person

Retrieves an existing person.

### Parameters

No parameters.

### Returns

Returns a person object.

GET/v1/accounts/:id/persons/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "person_1N9XNb2eZvKYlo2CjPX7xF6F",  "object": "person",  "account": "acct_1032D82eZvKYlo2C",  "created": 1684518375,  "dob": {    "day": null,    "month": null,    "year": null  },  "first_name": null,  "future_requirements": {    "alternatives": [],    "currently_due": [],    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "id_number_provided": false,  "last_name": null,  "metadata": {},  "relationship": {    "director": false,    "executive": false,    "owner": false,    "percent_ownership": null,    "representative": false,    "title": null  },  "requirements": {    "alternatives": [],    "currently_due": [],    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "ssn_last_4_provided": false,  "verification": {    "additional_document": {      "back": null,      "details": null,      "details_code": null,      "front": null    },    "details": null,    "details_code": null,    "document": {      "back": null,      "details": null,      "details_code": null,      "front": null    },    "status": "unverified"  }}`# List all persons

Returns a list of people associated with the account’s legal entity. The people are returned sorted by creation date, with the most recent people appearing first.

### Parameters

- relationshipobjectFilters on the list of people returned based on the person’s relationship to the account’s company.

Show child parameters

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit people, starting after person starting_after. Each entry in the array is a separate person object. If no more people are available, the resulting array will be empty.

GET/v1/accounts/:id/personsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/accounts/acct_1032D82eZvKYlo2C/persons",  "has_more": false,  "data": [    {      "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",      "person": "person_1MqjB62eZvKYlo2CaeEJzKVR",      "object": "person",      "account": "acct_1032D82eZvKYlo2C",      "created": 1680035496,      "dob": {        "day": null,        "month": null,        "year": null      },      "first_name": "Jane",      "future_requirements": {        "alternatives": [],        "currently_due": [],        "errors": [],        "eventually_due": [],        "past_due": [],        "pending_verification": []      },      "id_number_provided": false,      "last_name": "Diaz",      "metadata": {},      "relationship": {        "director": false,        "executive": false,        "owner": false,        "percent_ownership": null,        "representative": false,        "title": null      },      "requirements": {        "alternatives": [],        "currently_due": [],        "errors": [],        "eventually_due": [],        "past_due": [],        "pending_verification": []      },      "ssn_last_4_provided": false,      "verification": {        "additional_document": {          "back": null,          "details": null,          "details_code": null,          "front": null        },        "details": null,        "details_code": null,        "document": {          "back": null,          "details": null,          "details_code": null,          "front": null        },        "status": "unverified"      }    }    {...}    {...}  ],}`# Delete a person

Deletes an existing person’s relationship to the account’s legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the account_opener. If your integration is using the executive parameter, you cannot delete the only verified executive on file.

### Parameters

No parameters.

### Returns

Returns the deleted person object.

DELETE/v1/accounts/:id/persons/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",  "object": "person",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`