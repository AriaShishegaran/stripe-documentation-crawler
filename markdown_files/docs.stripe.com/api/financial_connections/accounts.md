htmlAccounts | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Accounts

A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

Endpoints
# The Account object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- account_holdernullableobjectThe account holder that this account belongs to.

Show child attributes
- balancenullableobjectThe most recent information about the account’s balance.

Show child attributes
- balance_refreshnullableobjectThe state of the most recent attempt to refresh the account balance.

Show child attributes
- categoryenumThe type of the account. Account category is further divided in subcategory.

Possible enum values`cash`The account represents real funds held by the institution (e.g. a checking or savings account).

`credit`The account represents credit extended by the institution (e.g. a credit card or mortgage).

`investment`The account represents investments, or any account where there are funds of unknown liquidity.

`other`The account does not fall under the other categories.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- display_namenullablestringA human-readable name that has been assigned to this account, either by the account holder or by the institution.


- institution_namestringThe name of the institution that holds this account.


- last4nullablestringThe last 4 digits of the account number. If present, this will be 4 numeric characters.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- ownershipnullablestringExpandableThe most recent information about the account’s owners.


- ownership_refreshnullableobjectThe state of the most recent attempt to refresh the account owners.

Show child attributes
- permissionsnullablearray of enumsThe list of permissions granted by this account.

Possible enum values`balances`Allows accessing balance data from the account.

`ownership`Allows accessing ownership data from the account.

`payment_method`Allows the creation of a payment method from the account.

`transactions`Allows accessing transactions data from the account.


- statusenumThe status of the link to the account.

Possible enum values`active`Stripe is able to retrieve data from the Account without issues.

`disconnected`Account connection has been terminated.

`inactive`Stripe cannot retrieve data from the Account.


- subcategoryenumIf category is cash, one of:

  - `checking`
  - `savings`
  - `other`

If category is credit, one of:

  - `mortgage`
  - `line_of_credit`
  - `credit_card`
  - `other`

If category is investment or other, this will be other.

Possible enum values`checking`The account is a checking account.

`credit_card`The account represents a credit card.

`line_of_credit`The account represents a line of credit.

`mortgage`The account represents a mortgage.

`other`The account does not fall under any of the other subcategories.

`savings`The account is a savings account.


- subscriptionsnullablearray of enumsThe list of data refresh subscriptions requested on this account.

Possible enum values`transactions`Subscribes to periodic transactions data refreshes from the account.


- supported_payment_method_typesarray of enumsThe PaymentMethod type(s) that can be created from this account.

Possible enum values`link`A link PaymentMethod can be created.

`us_bank_account`A us_bank_account PaymentMethod can be created.


- transaction_refreshnullableobjectThe state of the most recent attempt to refresh the account transactions.

Show child attributes

The Account object`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`# Retrieve an Account

Retrieves the details of an Financial Connections Account.

### Parameters

No parameters.

### Returns

Returns an Account object if a valid identifier was provided, and raises an error otherwise.

GET/v1/financial_connections/accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`# List Accounts

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

POST/v1/financial_connections/accounts/:id/disconnectServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf/disconnect \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "disconnected",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`