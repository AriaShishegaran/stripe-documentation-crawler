htmlCreate an account | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create an account

With Connect, you can create Stripe accounts for your users. To do this, you’ll first need to register your platform.

If you’ve already collected information for your connected accounts, you can prefill that information when creating the account. Connect Onboarding won’t ask for the prefilled information during account onboarding. You can prefill any information on the account.

### Parameters

- typeenumRequiredThe type of Stripe account to create. May be one of custom, express or standard.

Possible enum values`custom``express``standard`
- business_typeenumThe business type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

Possible enum values`company``government_entity`US only

`individual``non_profit`
- capabilitiesobjectRequired for custom accountsEach key of the dictionary represents a capability, and each capability maps to its settings (e.g. whether it has been requested or not). Each capability will be inactive until you have provided its specific requirements and Stripe has verified them. An account may have some of its requested capabilities be active and some be inactive.

Show child parameters
- companyobjectInformation about the company or business. This field is available for any business_type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

Show child parameters
- countrystringdefault is your own countryThe country in which the account holder resides, or in which the business is legally established. This should be an ISO 3166-1 alpha-2 country code. For example, if you are in the United States and the business for which you’re creating an account is legally represented in Canada, you would use CA as the country for the account being created. Available countries include Stripe’s global markets as well as countries where cross-border payouts are supported.


- emailstringThe email address of the account holder. This is only to make the account easier to identify to you. Stripe only emails Custom accounts with your consent.


- individualobjectInformation about the person represented by the account. This field is null unless business_type is set to individual. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- tos_acceptanceobjectDetails on the account’s acceptance of the Stripe Services Agreement This property can only be updated for Custom accounts.

Show child parameters

### More parametersExpand all

- account_tokenstring
- business_profileobject
- default_currencyenum
- documentsobject
- external_accountstring
- settingsobject

### Returns

Returns an Account object if the call succeeds.

POST/v1/accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=custom \  -d country=US \  --data-urlencode email="jenny.rosen@example.com" \  -d "capabilities[card_payments][requested]"=true \  -d "capabilities[transfers][requested]"=true`Response`{  "id": "acct_1Nv0FGQ9RKHgCVdK",  "object": "account",  "business_profile": {    "mcc": null,    "name": null,    "product_description": null,    "support_address": null,    "support_email": null,    "support_phone": null,    "support_url": null,    "url": null  },  "business_type": null,  "capabilities": {    "card_payments": "inactive",    "transfers": "inactive"  },  "charges_enabled": false,  "country": "US",  "created": 1695830751,  "default_currency": "usd",  "details_submitted": false,  "email": "jenny.rosen@example.com",  "external_accounts": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"  },  "future_requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "metadata": {},  "payouts_enabled": false,  "requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "disabled_reason": "requirements.past_due",    "errors": [],    "eventually_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "past_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "pending_verification": []  },  "settings": {    "bacs_debit_payments": {},    "branding": {      "icon": null,      "logo": null,      "primary_color": null,      "secondary_color": null    },    "card_issuing": {      "tos_acceptance": {        "date": null,        "ip": null      }    },    "card_payments": {      "decline_on": {        "avs_failure": false,        "cvc_failure": false      },      "statement_descriptor_prefix": null,      "statement_descriptor_prefix_kana": null,      "statement_descriptor_prefix_kanji": null    },    "dashboard": {      "display_name": null,      "timezone": "Etc/UTC"    },    "payments": {      "statement_descriptor": null,      "statement_descriptor_kana": null,      "statement_descriptor_kanji": null    },    "payouts": {      "debit_negative_balances": false,      "schedule": {        "delay_days": 2,        "interval": "daily"      },      "statement_descriptor": null    },    "sepa_debit_payments": {}  },  "tos_acceptance": {    "date": null,    "ip": null,    "user_agent": null  },  "type": "custom"}`# Update an account

Updates a connected account by setting the values of the parameters passed. Any parameters not provided are left unchanged.

For Custom accounts, you can update any information on the account. For other accounts, you can update all information until that account has started to go through Connect Onboarding. Once you create an Account Link or Account Session, some properties can only be changed or updated for Custom accounts.

To update your own account, use the Dashboard. Refer to our Connect documentation to learn more about updating accounts.

### Parameters

- business_typeenumThe business type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

Possible enum values`company``government_entity`US only

`individual``non_profit`
- capabilitiesobjectEach key of the dictionary represents a capability, and each capability maps to its settings (e.g. whether it has been requested or not). Each capability will be inactive until you have provided its specific requirements and Stripe has verified them. An account may have some of its requested capabilities be active and some be inactive.

Show child parameters
- companyobjectInformation about the company or business. This field is available for any business_type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

Show child parameters
- emailstringThe email address of the account holder. This is only to make the account easier to identify to you. Stripe only emails Custom accounts with your consent.


- individualobjectInformation about the person represented by the account. This field is null unless business_type is set to individual. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- tos_acceptanceobjectDetails on the account’s acceptance of the Stripe Services Agreement This property can only be updated for Custom accounts.

Show child parameters

### More parametersExpand all

- account_tokenstring
- business_profileobject
- default_currencyenum
- documentsobject
- external_accountstring
- settingsobject

### Returns

Returns an Account object if the call succeeds. If the account ID does not exist or another issue occurs, this call raises an error.

POST/v1/accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1Nv0FGQ9RKHgCVdK \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "acct_1Nv0FGQ9RKHgCVdK",  "object": "account",  "business_profile": {    "mcc": null,    "name": null,    "product_description": null,    "support_address": null,    "support_email": null,    "support_phone": null,    "support_url": null,    "url": null  },  "business_type": null,  "capabilities": {    "card_payments": "inactive",    "transfers": "inactive"  },  "charges_enabled": false,  "country": "US",  "created": 1695830751,  "default_currency": "usd",  "details_submitted": false,  "email": "jenny.rosen@example.com",  "external_accounts": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"  },  "future_requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "metadata": {    "order_id": "6735"  },  "payouts_enabled": false,  "requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "disabled_reason": "requirements.past_due",    "errors": [],    "eventually_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "past_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "pending_verification": []  },  "settings": {    "bacs_debit_payments": {},    "branding": {      "icon": null,      "logo": null,      "primary_color": null,      "secondary_color": null    },    "card_issuing": {      "tos_acceptance": {        "date": null,        "ip": null      }    },    "card_payments": {      "decline_on": {        "avs_failure": false,        "cvc_failure": false      },      "statement_descriptor_prefix": null,      "statement_descriptor_prefix_kana": null,      "statement_descriptor_prefix_kanji": null    },    "dashboard": {      "display_name": null,      "timezone": "Etc/UTC"    },    "payments": {      "statement_descriptor": null,      "statement_descriptor_kana": null,      "statement_descriptor_kanji": null    },    "payouts": {      "debit_negative_balances": false,      "schedule": {        "delay_days": 2,        "interval": "daily"      },      "statement_descriptor": null    },    "sepa_debit_payments": {}  },  "tos_acceptance": {    "date": null,    "ip": null,    "user_agent": null  },  "type": "custom"}`# Retrieve account

Retrieves the details of an account.

### Parameters

No parameters.

### Returns

Returns an Account object if the call succeeds. If the account ID does not exist, this call raises an error.

GET/v1/accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1Nv0FGQ9RKHgCVdK \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "acct_1Nv0FGQ9RKHgCVdK",  "object": "account",  "business_profile": {    "mcc": null,    "name": null,    "product_description": null,    "support_address": null,    "support_email": null,    "support_phone": null,    "support_url": null,    "url": null  },  "business_type": null,  "capabilities": {    "card_payments": "inactive",    "transfers": "inactive"  },  "charges_enabled": false,  "country": "US",  "created": 1695830751,  "default_currency": "usd",  "details_submitted": false,  "email": "jenny.rosen@example.com",  "external_accounts": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"  },  "future_requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "metadata": {},  "payouts_enabled": false,  "requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "disabled_reason": "requirements.past_due",    "errors": [],    "eventually_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "past_due": [      "business_profile.mcc",      "business_profile.url",      "business_type",      "external_account",      "representative.first_name",      "representative.last_name",      "tos_acceptance.date",      "tos_acceptance.ip"    ],    "pending_verification": []  },  "settings": {    "bacs_debit_payments": {},    "branding": {      "icon": null,      "logo": null,      "primary_color": null,      "secondary_color": null    },    "card_issuing": {      "tos_acceptance": {        "date": null,        "ip": null      }    },    "card_payments": {      "decline_on": {        "avs_failure": false,        "cvc_failure": false      },      "statement_descriptor_prefix": null,      "statement_descriptor_prefix_kana": null,      "statement_descriptor_prefix_kanji": null    },    "dashboard": {      "display_name": null,      "timezone": "Etc/UTC"    },    "payments": {      "statement_descriptor": null,      "statement_descriptor_kana": null,      "statement_descriptor_kanji": null    },    "payouts": {      "debit_negative_balances": false,      "schedule": {        "delay_days": 2,        "interval": "daily"      },      "statement_descriptor": null    },    "sepa_debit_payments": {}  },  "tos_acceptance": {    "date": null,    "ip": null,    "user_agent": null  },  "type": "custom"}`# List all connected accounts

Returns a list of accounts connected to your platform via Connect. If you’re not a platform, the list is empty.

### Parameters

No parameters.

### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit accounts, starting after account starting_after. Each entry in the array is a separate Account object. If no more accounts are available, the resulting array is empty.

GET/v1/accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/accounts",  "has_more": false,  "data": [    {      "id": "acct_1Nv0FGQ9RKHgCVdK",      "object": "account",      "business_profile": {        "mcc": null,        "name": null,        "product_description": null,        "support_address": null,        "support_email": null,        "support_phone": null,        "support_url": null,        "url": null      },      "business_type": null,      "capabilities": {        "card_payments": "inactive",        "transfers": "inactive"      },      "charges_enabled": false,      "country": "US",      "created": 1695830751,      "default_currency": "usd",      "details_submitted": false,      "email": "jenny.rosen@example.com",      "external_accounts": {        "object": "list",        "data": [],        "has_more": false,        "total_count": 0,        "url": "/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"      },      "future_requirements": {        "alternatives": [],        "current_deadline": null,        "currently_due": [],        "disabled_reason": null,        "errors": [],        "eventually_due": [],        "past_due": [],        "pending_verification": []      },      "metadata": {},      "payouts_enabled": false,      "requirements": {        "alternatives": [],        "current_deadline": null,        "currently_due": [          "business_profile.mcc",          "business_profile.url",          "business_type",          "external_account",          "representative.first_name",          "representative.last_name",          "tos_acceptance.date",          "tos_acceptance.ip"        ],        "disabled_reason": "requirements.past_due",        "errors": [],        "eventually_due": [          "business_profile.mcc",          "business_profile.url",          "business_type",          "external_account",          "representative.first_name",          "representative.last_name",          "tos_acceptance.date",          "tos_acceptance.ip"        ],        "past_due": [          "business_profile.mcc",          "business_profile.url",          "business_type",          "external_account",          "representative.first_name",          "representative.last_name",          "tos_acceptance.date",          "tos_acceptance.ip"        ],        "pending_verification": []      },      "settings": {        "bacs_debit_payments": {},        "branding": {          "icon": null,          "logo": null,          "primary_color": null,          "secondary_color": null        },        "card_issuing": {          "tos_acceptance": {            "date": null,            "ip": null          }        },        "card_payments": {          "decline_on": {            "avs_failure": false,            "cvc_failure": false          },          "statement_descriptor_prefix": null,          "statement_descriptor_prefix_kana": null,          "statement_descriptor_prefix_kanji": null        },        "dashboard": {          "display_name": null,          "timezone": "Etc/UTC"        },        "payments": {          "statement_descriptor": null,          "statement_descriptor_kana": null,          "statement_descriptor_kanji": null        },        "payouts": {          "debit_negative_balances": false,          "schedule": {            "delay_days": 2,            "interval": "daily"          },          "statement_descriptor": null        },        "sepa_debit_payments": {}      },      "tos_acceptance": {        "date": null,        "ip": null,        "user_agent": null      },      "type": "custom"    }    {...}    {...}  ],}`# Delete an account

With Connect, you can delete accounts you manage.

Accounts created using test-mode keys can be deleted at any time. Standard accounts created using live-mode keys cannot be deleted. Custom or Express accounts created using live-mode keys can only be deleted once all balances are zero.

If you want to delete your own account, use the account information tab in your account settings instead.

### Parameters

No parameters.

### Returns

Returns an object with a deleted parameter if the call succeeds. If the account ID does not exist, this call raises an error.

DELETE/v1/accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "acct_1032D82eZvKYlo2C",  "object": "account",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`