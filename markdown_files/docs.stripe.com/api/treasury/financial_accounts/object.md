htmlThe FinancialAccount object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The FinancialAccount object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- active_featuresarray of enumsThe array of paths to active Features in the Features hash.


- balanceobjectThe single multi-currency balance of the FinancialAccount. Positive values represent money that belongs to the user while negative values represent funds the user owes. Currently, FinancialAccounts can only carry balances in USD.

Show child attributes
- countrystringTwo-letter country code (ISO 3166-1 alpha-2).


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- featuresnullableobjectExpandableThe features and their statuses for this FinancialAccount.

Show child attributes
- financial_addressesarray of objectsThe set of credentials that resolve to a FinancialAccount.

Show child attributes
- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- pending_featuresarray of enumsThe array of paths to pending Features in the Features hash.


- platform_restrictionsnullableobjectThe set of functionalities that the platform can restrict on the FinancialAccount.

Show child attributes
- restricted_featuresarray of enumsThe array of paths to restricted Features in the Features hash.


- statusenumThe enum specifying what state the account is in.


- status_detailsobjectDetails related to the status of this FinancialAccount.

Show child attributes
- supported_currenciesarray of enumsThe currencies the FinancialAccount can hold a balance in. Three-letter ISO currency code, in lowercase.



The FinancialAccount object`{  "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",  "object": "treasury.financial_account",  "active_features": [    "financial_addresses.aba",    "outbound_payments.ach",    "outbound_payments.us_domestic_wire"  ],  "balance": {    "cash": {      "usd": 0    },    "inbound_pending": {      "usd": 0    },    "outbound_pending": {      "usd": 0    }  },  "country": "US",  "created": 1680714349,  "financial_addresses": [    {      "aba": {        "account_holder_name": "Jenny Rosen",        "account_number_last4": "7890",        "bank_name": "STRIPE TEST BANK",        "routing_number": "0000000001"      },      "supported_networks": [        "ach",        "us_domestic_wire"      ],      "type": "aba"    }  ],  "livemode": true,  "metadata": null,  "pending_features": [],  "restricted_features": [],  "status": "open",  "status_details": {    "closed": null  },  "supported_currencies": [    "usd"  ],  "features": {}}`# Create a FinancialAccount

Creates a new FinancialAccount. For now, each connected account can only have one FinancialAccount.

### Parameters

- supported_currenciesarray of stringsRequiredThe currencies the FinancialAccount can hold a balance in.


- featuresobjectEncodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- platform_restrictionsobjectThe set of functionalities that the platform can restrict on the FinancialAccount.

Show child parameters

### Returns

Returns a FinancialAccount object.

POST/v1/treasury/financial_accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/financial_accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "supported_currencies[]"=usd`Response`{  "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",  "object": "treasury.financial_account",  "active_features": [    "financial_addresses.aba",    "outbound_payments.ach",    "outbound_payments.us_domestic_wire"  ],  "balance": {    "cash": {      "usd": 0    },    "inbound_pending": {      "usd": 0    },    "outbound_pending": {      "usd": 0    }  },  "country": "US",  "created": 1680714349,  "financial_addresses": [    {      "aba": {        "account_holder_name": "Jenny Rosen",        "account_number_last4": "7890",        "bank_name": "STRIPE TEST BANK",        "routing_number": "0000000001"      },      "supported_networks": [        "ach",        "us_domestic_wire"      ],      "type": "aba"    }  ],  "livemode": true,  "metadata": null,  "pending_features": [],  "restricted_features": [],  "status": "open",  "status_details": {    "closed": null  },  "supported_currencies": [    "usd"  ],  "features": {}}`# Update a FinancialAccount

Updates the details of a FinancialAccount.

### Parameters

- featuresobjectEncodes whether a FinancialAccount has access to a particular feature, with a status enum and associated status_details. Stripe or the platform may control features via the requested field.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- platform_restrictionsobjectThe set of functionalities that the platform can restrict on the FinancialAccount.

Show child parameters

### Returns

Returns a FinancialAccount object.

POST/v1/treasury/financial_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",  "object": "treasury.financial_account",  "active_features": [    "financial_addresses.aba",    "outbound_payments.ach",    "outbound_payments.us_domestic_wire"  ],  "balance": {    "cash": {      "usd": 0    },    "inbound_pending": {      "usd": 0    },    "outbound_pending": {      "usd": 0    }  },  "country": "US",  "created": 1680714349,  "financial_addresses": [    {      "aba": {        "account_holder_name": "Jenny Rosen",        "account_number_last4": "7890",        "bank_name": "STRIPE TEST BANK",        "routing_number": "0000000001"      },      "supported_networks": [        "ach",        "us_domestic_wire"      ],      "type": "aba"    }  ],  "livemode": true,  "metadata": {    "order_id": "6735"  },  "pending_features": [],  "restricted_features": [],  "status": "open",  "status_details": {    "closed": null  },  "supported_currencies": [    "usd"  ],  "features": {}}`# Retrieve a FinancialAccount

Retrieves the details of a FinancialAccount.

### Parameters

No parameters.

### Returns

Return a FinancialAccount object.

GET/v1/treasury/financial_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",  "object": "treasury.financial_account",  "active_features": [    "financial_addresses.aba",    "outbound_payments.ach",    "outbound_payments.us_domestic_wire"  ],  "balance": {    "cash": {      "usd": 0    },    "inbound_pending": {      "usd": 0    },    "outbound_pending": {      "usd": 0    }  },  "country": "US",  "created": 1680714349,  "financial_addresses": [    {      "aba": {        "account_holder_name": "Jenny Rosen",        "account_number_last4": "7890",        "bank_name": "STRIPE TEST BANK",        "routing_number": "0000000001"      },      "supported_networks": [        "ach",        "us_domestic_wire"      ],      "type": "aba"    }  ],  "livemode": true,  "metadata": null,  "pending_features": [],  "restricted_features": [],  "status": "open",  "status_details": {    "closed": null  },  "supported_currencies": [    "usd"  ],  "features": {}}`# List all FinancialAccounts

Returns a list of FinancialAccounts.

### Parameters

- createdobjectOnly return FinancialAccounts that were created during the given date interval.

Show child parameters

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit FinancialAccounts, starting after FinancialAccount starting_after. Each entry in the array is a separate FinancialAccount object. If no more FinancialAccounts are available, the resulting array is empty.

GET/v1/treasury/financial_accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/treasury/financial_accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/treasury/financial_accounts",  "has_more": false,  "data": [    {      "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",      "object": "treasury.financial_account",      "active_features": [        "financial_addresses.aba",        "outbound_payments.ach",        "outbound_payments.us_domestic_wire"      ],      "balance": {        "cash": {          "usd": 0        },        "inbound_pending": {          "usd": 0        },        "outbound_pending": {          "usd": 0        }      },      "country": "US",      "created": 1680714349,      "financial_addresses": [        {          "aba": {            "account_holder_name": "Jenny Rosen",            "account_number_last4": "7890",            "bank_name": "STRIPE TEST BANK",            "routing_number": "0000000001"          },          "supported_networks": [            "ach",            "us_domestic_wire"          ],          "type": "aba"        }      ],      "livemode": true,      "metadata": null,      "pending_features": [],      "restricted_features": [],      "status": "open",      "status_details": {        "closed": null      },      "supported_currencies": [        "usd"      ],      "features": {}    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`