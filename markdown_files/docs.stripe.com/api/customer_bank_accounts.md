htmlBank Accounts | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Bank Accounts

These bank accounts are payment methods on Customer objects.

On the other hand External Accounts are transfer destinations on Account objects for Custom accounts. They can be bank accounts or debit cards as well, and are documented in the links above.

Related guide: Bank debits and transfers

Endpoints
# The Bank Account object

### Attributes

- idstringUnique identifier for the object.


- account_holder_namenullablestringThe name of the person or business that owns the bank account.


- account_holder_typenullablestringThe type of entity that holds the account. This can be either individual or company.


- bank_namenullablestringName of the bank associated with the routing number (e.g., WELLS FARGO).


- countrystringTwo-letter ISO code representing the country the bank account is located in.


- currencyenumThree-letter ISO code for the currency paid out to the bank account.


- customernullablestringExpandableThe ID of the customer that the bank account is associated with.


- fingerprintnullablestringUniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.


- last4stringThe last four digits of the bank account number.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- routing_numbernullablestringThe routing transit number for the bank account.



### More attributesExpand all

- objectstring
- accountnullablestringExpandable
- account_typenullablestring
- available_payout_methodsnullablearray of enums
- statusstring

The Bank Account object`{  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "customer": "cus_9s6XI9OFIdpjIg",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new"}`# Create a bank account

When you create a new bank account, you must specify a Customer object on which to create it.

### Parameters

- sourceobject | stringRequiredEither a token, like the ones returned by Stripe.js, or a dictionary containing a user’s bank account details (with the options shown below).

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the bank account object.

POST/v1/customers/:id/sourcesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/ba_1MvoIJ2eZvKYlo2CO9f0MabO/sources \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d source=btok_1MvoS32eZvKYlo2CDhGTErAe`Response`{  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "customer": "cus_9s6XI9OFIdpjIg",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new"}`# Update a bank account

Updates the account_holder_name, account_holder_type, and metadata of a bank account belonging to a customer. Other bank account details are not editable, by design.

### Parameters

- account_holder_namestringThe name of the person or business that owns the bank account.


- account_holder_typestringThe type of entity that holds the account. This can be either individual or company.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the bank account object.

POST/v1/customers/:id/sources/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources/ba_1MvoIJ2eZvKYlo2CO9f0MabO \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "customer": "cus_9s6XI9OFIdpjIg",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {    "order_id": "6735"  },  "routing_number": "110000000",  "status": "new"}`# Retrieve a bank account

By default, you can see the 10 most recent sources stored on a Customer directly on the object, but you can also retrieve details about a specific bank account stored on the Stripe account.

### Parameters

No parameters.

### Returns

Returns the bank account object.

GET/v1/customers/:id/bank_accounts/:idcURL[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts/ba_1MvoIJ2eZvKYlo2CO9f0MabO \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "customer": "cus_9s6XI9OFIdpjIg",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`