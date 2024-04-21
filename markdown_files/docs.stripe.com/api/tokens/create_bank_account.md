htmlCreate a bank account token | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a bank account token

Creates a single-use token that represents a bank account’s details. You can use this token with any API method in place of a bank account dictionary. You can only use this token once. To do so, attach it to a Custom account.

### Parameters

- bank_accountobjectThe bank account this token will represent.

Show child parameters

### More parametersExpand all

- customerstringConnect only

### Returns

Returns the created bank account token if it’s successful. Otherwise, this call raises an error.

POST/v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tokens \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "bank_account[country]"=US \  -d "bank_account[currency]"=usd \  -d "bank_account[account_holder_name]"="Jenny Rosen" \  -d "bank_account[account_holder_type]"=individual \  -d "bank_account[routing_number]"=110000000 \  -d "bank_account[account_number]"=000123456789`Response`{  "id": "tok_1N3T00LkdIwHu7ixt44h1F8k",  "object": "token",  "bank_account": {    "id": "ba_1NWScr2eZvKYlo2C8MgV5Cwn",    "object": "bank_account",    "account_holder_name": "Jenny Rosen",    "account_holder_type": "individual",    "account_type": null,    "bank_name": "STRIPE TEST BANK",    "country": "US",    "currency": "usd",    "fingerprint": "1JWtPxqbdX5Gamtz",    "last4": "6789",    "routing_number": "110000000",    "status": "new"  },  "client_ip": null,  "created": 1689981645,  "livemode": false,  "redaction": null,  "type": "bank_account",  "used": false}`# Create a card token

Creates a single-use token that represents a credit card’s details. You can use this token in place of a credit card dictionary with any API method. You can only use these tokens once by creating a new Charge object or by attaching them to a Customer object.

In most cases, you can use our recommended payments integrations instead of using the API.

### Parameters

- cardobject | stringThe card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user’s credit card details, with the options described below.

Show child parameters

### Returns

Returns the created card token if it’s successful. Otherwise, this call raises an error.

POST/v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tokens \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "card[number]"=4242424242424242 \  -d "card[exp_month]"=5 \  -d "card[exp_year]"=2024 \  -d "card[cvc]"=314`Response`{  "id": "tok_1N3T00LkdIwHu7ixt44h1F8k",  "object": "token",  "card": {    "id": "card_1N3T00LkdIwHu7ixRdxpVI1Q",    "object": "card",    "address_city": null,    "address_country": null,    "address_line1": null,    "address_line1_check": null,    "address_line2": null,    "address_state": null,    "address_zip": null,    "address_zip_check": null,    "brand": "Visa",    "country": "US",    "cvc_check": "unchecked",    "dynamic_last4": null,    "exp_month": 5,    "exp_year": 2024,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "last4": "4242",    "metadata": {},    "name": null,    "tokenization_method": null,    "wallet": null  },  "client_ip": "52.35.78.6",  "created": 1683071568,  "livemode": false,  "type": "card",  "used": false}`# Create a CVC update token

Creates a single-use token that represents an updated CVC value that you can use for CVC re-collection. Use this token when you confirm a card payment or use a saved card on a PaymentIntent with confirmation_method: manual.

For most cases, use our JavaScript library instead of using the API. For a PaymentIntent with confirmation_method: automatic, use our recommended payments integration without tokenizing the CVC value.

### Parameters

- cvc_updateobjectRequiredThe updated CVC value this token represents.

Show child parameters

### Returns

Returns the created CVC update token if it’s successful. Otherwise, this call raises an error.

POST/v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tokens \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "cvc_update[cvc]"=123`Response`{  "id": "cvctok_1NkWsu2eZvKYlo2CFDm6ab7X",  "object": "token",  "client_ip": null,  "created": 1693334608,  "livemode": false,  "redaction": null,  "type": "cvc_update",  "used": false}`# Create a person token

Creates a single-use token that represents the details for a person. Use this when you create or update persons associated with a Connect account. Learn more about account tokens.

You can only create person tokens with your application’s publishable key and in live mode. You can use your application’s secret key to create person tokens only in test mode.

### Parameters

- personobjectRequiredInformation for the person this token represents.

Show child parameters

### Returns

Returns the created person token if it’s successful. Otherwise, this call raises an error.

POST/v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tokens \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "person[first_name]"=Jane \  -d "person[last_name]"=Doe \  -d "person[relationship][owner]"=true`Response`{  "id": "cpt_1EDww82eZvKYlo2CsdelTHFu",  "object": "token",  "client_ip": "8.21.168.117",  "created": 1552582904,  "livemode": false,  "redaction": null,  "type": "person",  "used": false}`# Create a PII token

Creates a single-use token that represents the details of personally identifiable information (PII). You can use this token in place of an id_number or id_number_secondary in Account or Person Update API methods. You can only use a PII token once.

### Parameters

- piiobjectRequiredThe PII this token represents.

Show child parameters

### Returns

Returns the created PII token if it’s successful. Otherwise, this call raises an error.

POST/v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tokens \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "pii[id_number]"=000000000`Response`{  "id": "pii_18PwbX2eZvKYlo2CzRXgwN3J",  "object": "token",  "client_ip": "124.123.76.134",  "created": 1466783547,  "livemode": false,  "redaction": null,  "type": "pii",  "used": false}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`