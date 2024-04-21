htmlExternal Bank Accounts | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# External Bank Accounts

External bank accounts are financial accounts associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected account’s Stripe balance.

Endpoints
# The External Bank Account object

### Attributes

- idstringUnique identifier for the object.


- accountnullablestringExpandableThe ID of the account that the bank account is associated with.


- bank_namenullablestringName of the bank associated with the routing number (e.g., WELLS FARGO).


- countrystringTwo-letter ISO code representing the country the bank account is located in.


- currencyenumThree-letter ISO code for the currency paid out to the bank account.


- default_for_currencynullablebooleanWhether this bank account is the default external account for its currency.


- last4stringThe last four digits of the bank account number.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- routing_numbernullablestringThe routing transit number for the bank account.


- statusstringFor bank accounts, possible values are new, validated, verified, verification_failed, or errored. A bank account that hasn’t had any activity or validation performed is new. If Stripe can determine that the bank account exists, its status will be validated. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be verified. If the verification failed for any reason, such as microdeposit failure, the status will be verification_failed. If a payout sent to this bank account fails, we’ll set the status to errored and will not continue to send scheduled payouts until the bank details are updated.

For external accounts, possible values are new, errored and verification_failed. If a payout fails, the status is set to errored and scheduled payouts are stopped until account details are updated. In the US and India, if we can’t verify the owner of the bank account, we’ll set the status to verification_failed. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.



### More attributesExpand all

- objectstring
- account_holder_namenullablestring
- account_holder_typenullablestring
- account_typenullablestring
- available_payout_methodsnullablearray of enums
- customernullablestringExpandable
- fingerprintnullablestring
- future_requirementsnullableobject
- requirementsnullableobject

The External Bank Account object`{  "id": "ba_1N9DrD2eZvKYlo2C58f4DaIa",  "object": "bank_account",  "account": "acct_1032D82eZvKYlo2C",  "account_holder_name": "Jane Austen",  "account_holder_type": "individual",  "account_type": null,  "available_payout_methods": [    "standard"  ],  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "fingerprint": "1JWtPxqbdX5Gamtz",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new"}`# Create a bank account

When you create a new bank account, you must specify a Custom account to create it on.

If the bank account’s owner has no other external account in the bank account’s currency, the new bank account will become the default for that currency. However, if the owner already has a bank account for that currency, the new account will become the default only if the default_for_currency parameter is set to true.

### Parameters

- external_accountobject | stringRequiredEither a token, like the ones returned by Stripe.js, or a dictionary containing a user’s bank account details (with the options shown below).

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- default_for_currencyboolean

### Returns

Returns the bank account object

POST/v1/accounts/:id/external_accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d external_account=btok_1NAiJy2eZvKYlo2Cnh6bIs9c`Response`{  "id": "ba_1NAiJy2eZvKYlo2CvChQKz5k",  "object": "bank_account",  "account": "acct_1032D82eZvKYlo2C",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new"}`# Update a bank account

Updates the metadata, account holder name, account holder type of a bank account belonging to a Custom account, and optionally sets it as the default for its currency. Other bank account details are not editable by design. You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.

### Parameters

- default_for_currencybooleanWhen set to true, this becomes the default external account for its currency.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- account_holder_namestring
- account_holder_typestring
- account_typestring
- documentsobject

### Returns

Returns the bank account object.

POST/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAiwl2eZvKYlo2CRdCLZSxO \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "ba_1NAiwl2eZvKYlo2CRdCLZSxO",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {    "order_id": "6735"  },  "routing_number": "110000000",  "status": "new",  "account": "acct_1032D82eZvKYlo2C"}`# Retrieve a bank account

By default, you can see the 10 most recent external accounts stored on a (connected account)[/docs/connect/accounts] directly on the object. You can also retrieve details about a specific bank account stored on the account.

### Parameters

No parameters.

### Returns

Returns the bank account object.

GET/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAinX2eZvKYlo2CpFGcuuEG \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ba_1NAinX2eZvKYlo2CpFGcuuEG",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "customer": null,  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`