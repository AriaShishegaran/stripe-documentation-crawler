htmlThe VerificationReport object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The VerificationReport object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- client_reference_idnullablestringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- documentnullableobjectResult of the document check for this report.

Show child attributes
- id_numbernullableobjectResult of the id number check for this report.

Show child attributes
- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- optionsnullableobjectConfiguration options for this report.

Show child attributes
- selfienullableobjectResult of the selfie check for this report.

Show child attributes
- typeenumType of report.

Possible enum values`document`Perform a document check.

`id_number`Perform an ID number check.


- verification_sessionnullablestringID of the VerificationSession that created this report.



The VerificationReport object`{  "id": "vr_1MwBlH2eZvKYlo2C91hOpFMf",  "object": "identity.verification_report",  "created": 1681337011,  "livemode": false,  "options": {    "document": {}  },  "type": "document",  "verification_session": "vs_NhaxYCqOE27AqaUTxbIZOnHw",  "document": {    "status": "verified",    "error": null,    "first_name": "Jenny",    "last_name": "Rosen",    "address": {      "line1": "1234 Main St.",      "city": "San Francisco",      "state": "CA",      "zip": "94111",      "country": "US"    },    "type": "driving_license",    "files": [      "file_NhaxRCXT8Iuu8apSuci00UC4",      "file_NhaxDeWKGAOTc8Uec7UY9Ljj"    ],    "expiration_date": {      "month": 12,      "day": 1,      "year": 2025    },    "issued_date": {      "month": 12,      "day": 1,      "year": 2020    },    "issuing_country": "US"  }}`# Retrieve a VerificationReport

Retrieves an existing VerificationReport

### Parameters

No parameters.

### Returns

Returns a VerificationReport object

GET/v1/identity/verification_reports/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/identity/verification_reports/vr_1MwBlH2eZvKYlo2C91hOpFMf \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "vr_1MwBlH2eZvKYlo2C91hOpFMf",  "object": "identity.verification_report",  "created": 1681337011,  "livemode": false,  "options": {    "document": {}  },  "type": "document",  "verification_session": "vs_NhaxYCqOE27AqaUTxbIZOnHw",  "document": {    "status": "verified",    "error": null,    "first_name": "Jenny",    "last_name": "Rosen",    "address": {      "line1": "1234 Main St.",      "city": "San Francisco",      "state": "CA",      "zip": "94111",      "country": "US"    },    "type": "driving_license",    "files": [      "file_NhaxRCXT8Iuu8apSuci00UC4",      "file_NhaxDeWKGAOTc8Uec7UY9Ljj"    ],    "expiration_date": {      "month": 12,      "day": 1,      "year": 2025    },    "issued_date": {      "month": 12,      "day": 1,      "year": 2020    },    "issuing_country": "US"  }}`# List VerificationReports

List all verification reports.

### Parameters

- client_reference_idstringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.


- createdobjectOnly return VerificationReports that were created during the given date interval.

Show child parameters
- typeenumOnly return VerificationReports of this type

Possible enum values`document`Perform a document check.

`id_number`Perform an ID number check.


- verification_sessionstringOnly return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

List of VerificationInent objects that match the provided filter criteria.

GET/v1/identity/verification_reportsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/identity/verification_reports \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/identity/verification_reports",  "has_more": false,  "data": [    {      "id": "vr_1MwBlH2eZvKYlo2C91hOpFMf",      "object": "identity.verification_report",      "created": 1681337011,      "livemode": false,      "options": {        "document": {}      },      "type": "document",      "verification_session": "vs_NhaxYCqOE27AqaUTxbIZOnHw",      "document": {        "status": "verified",        "error": null,        "first_name": "Jenny",        "last_name": "Rosen",        "address": {          "line1": "1234 Main St.",          "city": "San Francisco",          "state": "CA",          "zip": "94111",          "country": "US"        },        "type": "driving_license",        "files": [          "file_NhaxRCXT8Iuu8apSuci00UC4",          "file_NhaxDeWKGAOTc8Uec7UY9Ljj"        ],        "expiration_date": {          "month": 12,          "day": 1,          "year": 2025        },        "issued_date": {          "month": 12,          "day": 1,          "year": 2020        },        "issuing_country": "US"      }    }    {...}    {...}  ],}`# Crypto Onramp Session

A Crypto Onramp Session represents your customer’s session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user’s wallet and contain a reference to the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

Related guide: Integrate the onramp

Endpoints
Show

# Crypto Onramp Quotes

Crypto Onramp Quotes are estimated quotes for onramp conversions into all the different cryptocurrencies on different networks. The Quotes API allows you to display quotes in your product UI before directing the user to the onramp widget.

Related guide: Quotes API

Endpoints
Show

# Climate Order

Orders represent your intent to purchase a particular Climate product. When you create an order, the payment is deducted from your merchant balance.

Endpoints
Show

# Climate Product

A Climate product represents a type of carbon removal unit available for reservation. You can retrieve it to see the current price and availability.

Endpoints
Show

# Climate Supplier

A supplier of carbon removal.

Endpoints
Show

# Forwarding RequestPreview feature

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

Endpoints
Show

# Webhook Endpoints

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

Related guide: Setting up webhooks

Endpoints
Show

Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`