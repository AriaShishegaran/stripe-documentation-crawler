htmlTokens | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# TokensPreview feature

An issuing token object is created when an issued card is added to a digital wallet. As a card issuer, you can view and manage these tokens through Stripe.

Endpoints
# The Token objectPreview feature

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- cardstringExpandableCard associated with this token.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- device_fingerprintnullablestringThe hashed ID derived from the device ID from the card network associated with the token.


- last4nullablestringThe last four digits of the token.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- networkenumThe token service provider / card network associated with the token.

Possible enum values`mastercard`MasterCard token service provider.

`visa`Visa token service provider.


- network_datanullableobjectPreview featureExpandableAdditional details obtained from the network about the token, primarily related to the token creation process. For security reasons, this is only available to view in the first 24 hours after token creation, based on the created value, and will be omitted unless you explicitly request it with the expand parameter. Additionally, it’s only available via the “Retrieve a token” endpoint and “Update a token status” endpoint.

Show child attributes
- network_updated_attimestampTime at which the token was last updated by the card network. Measured in seconds since the Unix epoch.


- statusenumThe usage state of the token.

Possible enum values`active`Token is provisioned and usable for payments.

`deleted`Terminal state. Token can no longer be used.

`requested`Token has been requested to be provisioned, but has not completed the activation process.

`suspended`Token temporarily cannot be used for payments.


- wallet_providernullableenumThe digital wallet for this token, if one was used.

Possible enum values`apple_pay`Apple Pay.

`google_pay`Google Pay.

`samsung_pay`Samsung Pay.



The Token object`{  "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",  "object": "issuing.token",  "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",  "created": 1682059060,  "network_updated_at": 1682059060,  "livemode": false,  "status": "active",  "last4": "2424",  "token_service_provider": "visa",  "wallet_provider": "apple_pay",  "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"}`# Update a token status

Attempts to update the specified Issuing Token object to the status specified.

### Parameters

- statusenumRequiredSpecifies which status the token should be updated to.

Possible enum values`active`Token is provisioned and usable for payments.

`deleted`Terminal state. Token can no longer be used.

`suspended`Token temporarily cannot be used for payments.



### Returns

Returns an updated Issuing Token object if a valid identifier was provided.

POST/v1/issuing/tokens/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/tokens/intok_1MzDbE2eZvKYlo2C26a98MDg \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d status=suspended`Response`{  "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",  "object": "issuing.token",  "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",  "created": 1682059060,  "network_updated_at": 1682059060,  "livemode": false,  "status": "suspended",  "last4": "2424",  "token_service_provider": "visa",  "wallet_provider": "apple_pay",  "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"}`# Retrieve an issuing token

Retrieves an Issuing Token object.

### Parameters

No parameters.

### Returns

Returns an Issuing Token object if a valid identifier was provided.

GET/v1/issuing/tokens/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/tokens/intok_1MzDbE2eZvKYlo2C26a98MDg \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",  "object": "issuing.token",  "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",  "created": 1682059060,  "network_updated_at": 1682059060,  "livemode": false,  "status": "active",  "last4": "2424",  "token_service_provider": "visa",  "wallet_provider": "apple_pay",  "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"}`# List all issuing tokens for card

Lists all Issuing Token objects for a given card.

### Parameters

- cardstringRequiredThe Issuing card identifier to list tokens for.


- createdobjectOnly return Issuing tokens that were created during the given date interval.

Show child parameters
- statusenumSelect Issuing tokens with the given status.

Possible enum values`active`Token is provisioned and usable for payments.

`deleted`Terminal state. Token can no longer be used.

`requested`Token has been requested to be provisioned, but has not completed the activation process.

`suspended`Token temporarily cannot be used for payments.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit tokens, starting after token starting_after. Each entry in the array is a separate Issuing Token object. If no more tokens are available, the resulting array will be empty.

GET/v1/issuing/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/tokens \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3 \  -d card=ic_1MytUz2eZvKYlo2CZCn5fuvZ`Response`{  "object": "list",  "url": "/v1/issuing/tokens",  "has_more": false,  "data": [    {      "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",      "object": "issuing.token",      "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",      "created": 1682059060,      "network_updated_at": 1682059060,      "livemode": false,      "status": "suspended",      "last4": "2424",      "token_service_provider": "visa",      "wallet_provider": "apple_pay",      "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`