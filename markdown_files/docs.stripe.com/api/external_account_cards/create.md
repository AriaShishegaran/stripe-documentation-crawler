htmlCreate a card | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a card

When you create a new debit card, you must specify a Custom account to create it on.

If the account has no default destination card, then the new card will become the default. However, if the owner already has a default then it will not change. To change the default, you should set default_for_currency to true when creating a card for a Custom account.

### Parameters

- external_accountobject | stringRequiredA token, like the ones returned by Stripe.js or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- default_for_currencyboolean

### Returns

Returns the card object

POST/v1/accounts/:id/external_accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d external_account=tok_visa_debit`Response`{  "id": "card_1NAiaG2eZvKYlo2CDXvcMb6m",  "object": "card",  "account": "acct_1032D82eZvKYlo2C",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "redaction": null,  "tokenization_method": null,  "wallet": null}`# Update a card

If you need to update only some card details, like the billing address or expiration date, you can do so without having to re-enter the full card details. Stripe also works directly with card networks so that your customers can continue using your service without interruption.

### Parameters

- default_for_currencybooleanWhen set to true, this becomes the default external account for its currency.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- address_citystring
- address_countrystring
- address_line1string
- address_line2string
- address_statestring
- address_zipstring
- exp_monthstring
- exp_yearstring
- namestring

### Returns

Returns the card object.

POST/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NBLeN2eZvKYlo2CIq1o7Pzs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "card_1NBLeN2eZvKYlo2CIq1o7Pzs",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {    "order_id": "6735"  },  "name": "Jenny Rosen",  "redaction": null,  "tokenization_method": null,  "wallet": null,  "account": "acct_1032D82eZvKYlo2C"}`# Retrieve a card

By default, you can see the 10 most recent external accounts stored on a connected account directly on the object. You can also retrieve details about a specific card stored on the account.

### Parameters

No parameters.

### Returns

Returns the card object.

GET/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAinb2eZvKYlo2C1Fm9mZsu \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "card_1NAinb2eZvKYlo2C1Fm9mZsu",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "redaction": null,  "tokenization_method": null,  "wallet": null,  "account": "acct_1032D82eZvKYlo2C"}`# List all cards

You can see a list of the cards that belong to a connected account. The 10 most recent external accounts are available on the account object. If you need more than 10, you can use this API method and the limit and starting_after parameters to page through additional cards.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- objectstring
- starting_afterstring

### Returns

Returns a list of the cards stored on the account.

GET/v1/accounts/:id/external_accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d object=card`Response`{  "object": "list",  "url": "/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts",  "has_more": false,  "data": [    {      "id": "card_1NAz2x2eZvKYlo2C75wJ1YUs",      "object": "card",      "address_city": null,      "address_country": null,      "address_line1": null,      "address_line1_check": null,      "address_line2": null,      "address_state": null,      "address_zip": null,      "address_zip_check": null,      "brand": "Visa",      "country": "US",      "cvc_check": "pass",      "dynamic_last4": null,      "exp_month": 8,      "exp_year": 2024,      "fingerprint": "Xt5EWLLDS7FJjR1c",      "funding": "credit",      "last4": "4242",      "metadata": {},      "name": null,      "redaction": null,      "tokenization_method": null,      "wallet": null,      "account": "acct_1032D82eZvKYlo2C"    }    {...}    {...}  ],}`# Delete a card

You can delete cards from a Custom account.

There are restrictions for deleting a card with default_for_currency set to true. You cannot delete a card if any of the following apply:

- The card’s`currency`is the same as the connected account’s[default_currency](/api/accounts/object#account_object-default_currency).
- There is another external account (card or bank account) with the same currency as the card.

To delete a card, you must first replace the default external account by setting default_for_currency with another external account in the same currency.

### Parameters

No parameters.

### Returns

Returns the deleted card object.

DELETE/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAz2x2eZvKYlo2C75wJ1YUs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "card_1NAz2x2eZvKYlo2C75wJ1YUs",  "object": "card",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`