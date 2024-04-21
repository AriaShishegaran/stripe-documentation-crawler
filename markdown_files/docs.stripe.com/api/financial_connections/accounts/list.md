htmlList Accounts | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# List Accounts

Returns a list of Financial Connections Account objects.

### Parameters

- account_holderobjectIf present, only return accounts that belong to the specified account holder. account_holder[customer] and account_holder[account] are mutually exclusive.

Show child parameters
- sessionstringIf present, only return accounts that were collected as part of the given session.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit Account objects, starting after account starting_after. Each entry in the array is a separate Account object. If no more accounts are available, the resulting array will be empty. This request will raise an error if more than one of account_holder[account], account_holder[customer], or session is specified.

GET/v1/financial_connections/accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/financial_connections/accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/financial_connections/accounts",  "has_more": false,  "data": [    {      "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",      "object": "linked_account",      "account_holder": {        "customer": "cus_9s6XI9OFIdpjIg",        "type": "customer"      },      "balance": null,      "balance_refresh": null,      "category": "cash",      "created": 1681412208,      "display_name": "Sample Checking Account",      "institution_name": "StripeBank",      "last4": "6789",      "livemode": false,      "ownership": null,      "ownership_refresh": null,      "permissions": [],      "status": "active",      "subcategory": "checking",      "subscriptions": [],      "supported_payment_method_types": [        "us_bank_account"      ],      "transaction_refresh": null    }    {...}    {...}  ],}`# Disconnect an Account

Disables your access to a Financial Connections Account. You will no longer be able to access data associated with the account (e.g. balances, transactions).

### Parameters

No parameters.

### Returns

Returns an Account object if a valid identifier was provided, and raises an error otherwise.

POST/v1/financial_connections/accounts/:id/disconnectServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf/disconnect \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "disconnected",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`# Refresh Account data

Refreshes the data associated with a Financial Connections Account.

### Parameters

- featuresarray of enumsRequiredThe list of account features that you would like to refresh.

Possible enum values`balance`Balance data from the account

`ownership`Ownership data from the account

`transactions`Transactions data from the account



### Returns

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

POST/v1/financial_connections/accounts/:id/refreshServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf/refresh \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "features[]"=balance`Response`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": {    "status": "pending",    "last_attempted_at": 1681422295  },  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "pending",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`# Subscribe to data refreshes for an Account

Subscribes to periodic refreshes of data associated with a Financial Connections Account.

### Parameters

- featuresarray of enumsRequiredThe list of account features to which you would like to subscribe.

Possible enum values`transactions`Transactions data from the account



### Returns

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

POST/v1/financial_connections/accounts/:id/subscribeServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/financial_connections/accounts/fca_1NQay62eZvKYlo2C8dflHjWB/subscribe \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "features[]"=transactions`Response`{  "id": "fca_1NQay62eZvKYlo2C8dflHjWB",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XKzkNRiz8i3",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1688583746,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [    "transactions"  ],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": {    "id": "fctxnref_OD10iHSd7eaheDkeabbQfnJ7",    "status": "pending",    "last_attempted_at": 1625337296  }}`# Unsubscribe from data refreshes for an Account

Unsubscribes from periodic refreshes of data associated with a Financial Connections Account.

### Parameters

- featuresarray of enumsRequiredThe list of account features from which you would like to unsubscribe.

Possible enum values`transactions`Transactions data from the account



### Returns

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

POST/v1/financial_connections/accounts/:id/unsubscribeServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/financial_connections/accounts/fca_1NQayH2eZvKYlo2CMBkU6Y9s/unsubscribe \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "features[]"=transactions`Response`{  "id": "fca_1NQayH2eZvKYlo2CMBkU6Y9s",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XKzkNRiz8i3",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1688583757,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": {    "id": "fctxnref_OD10EqMBikeOrWm7JW44fdpo",    "status": "succeeded",    "last_attempted_at": 1625337296  }}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`