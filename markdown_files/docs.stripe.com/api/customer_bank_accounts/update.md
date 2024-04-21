htmlUpdate a bank account | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a bank account

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

GET/v1/customers/:id/bank_accounts/:idcURL[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts/ba_1MvoIJ2eZvKYlo2CO9f0MabO \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "customer": "cus_9s6XI9OFIdpjIg",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new"}`# List all bank accounts

You can see a list of the bank accounts belonging to a Customer. Note that the 10 most recent sources are always available by default on the Customer. If you need more than those 10, you can use this API method and the limit and starting_after parameters to page through additional bank accounts.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

Returns a list of the bank accounts stored on the customer.

GET/v1/customers/:id/bank_accountscURL[](#)[](#)`curl -G https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/customers/cus_9s6XI9OFIdpjIg/bank_accounts",  "has_more": false,  "data": [    {      "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",      "object": "bank_account",      "account_holder_name": "Jane Austen",      "account_holder_type": "company",      "account_type": null,      "bank_name": "STRIPE TEST BANK",      "country": "US",      "currency": "usd",      "customer": "cus_9s6XI9OFIdpjIg",      "fingerprint": "1JWtPxqbdX5Gamtc",      "last4": "6789",      "metadata": {},      "routing_number": "110000000",      "status": "new"    }    {...}    {...}  ],}`# Delete a bank account

You can delete bank accounts from a Customer.

### Parameters

No parameters.

### Returns

DELETE/v1/customers/:id/sources/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/sources/ba_1NkxyL2eZvKYlo2CwZgb2mzO \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "customer": "cus_9s6XKzkNRiz8i3",  "id": "ba_1NkxyL2eZvKYlo2CwZgb2mzO",  "object": "bank_account",  "deleted": true}`# Verify a bank account

Verify a specified bank account for a given customer.

### Parameters

- amountsarray of integersTwo positive integers, in cents, equal to the values of the microdeposits sent to the bank account.



### Returns

POST/v1/customers/:id/sources/:id/verifyServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XGDTHzA66Po/sources/ba_1NAiwl2eZvKYlo2CRdCLZSxO/verify \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "amounts[]"=32 \  -d "amounts[]"=45`Response`{  "id": "ba_1NAiwl2eZvKYlo2CRdCLZSxO",  "object": "bank_account",  "account_holder_name": "Jane Austen",  "account_holder_type": "company",  "account_type": null,  "bank_name": "STRIPE TEST BANK",  "country": "US",  "currency": "usd",  "customer": "cus_9s6XGDTHzA66Po",  "fingerprint": "1JWtPxqbdX5Gamtc",  "last4": "6789",  "metadata": {},  "routing_number": "110000000",  "status": "new",  "name": "Jenny Rosen"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`