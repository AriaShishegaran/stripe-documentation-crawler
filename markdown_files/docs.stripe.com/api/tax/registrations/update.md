htmlUpdate a registration | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a registration

Updates an existing Tax Registration object.

A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.

### Parameters

- active_fromstring | timestampTime at which the registration becomes active. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.


- expires_atstring | timestampIf set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.



### Returns

A Tax Registration object.

POST/v1/tax/registrations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d expires_at=now`Response`{  "id": "taxreg_NkyGPRPytKq66j",  "object": "tax.registration",  "active_from": 1683036640,  "country": "US",  "country_options": {    "us": {      "state": "CA",      "type": "state_sales_tax"    }  },  "created": 1682006400,  "expires_at": 1684072000,  "livemode": false,  "status": "active",  "state": "CA",  "type": "standard"}`# Retrieve a registration

Returns a Tax Registration object.

### Parameters

No parameters.

### Returns

A Tax Registration object.

GET/v1/tax/registrations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "taxreg_NkyGPRPytKq66j",  "object": "tax.registration",  "active_from": 1682036640,  "country": "US",  "country_options": {    "us": {      "state": "CA",      "type": "state_sales_tax"    }  },  "created": 1682006400,  "expires_at": null,  "livemode": false,  "status": "active",  "state": "CA",  "type": "standard"}`# List registrations

Returns a list of Tax Registration objects.

### Parameters

- statusenumThe status of the Tax Registration.

Possible enum values`active`Return all active Tax Registrations.

`all`Return all Tax Registrations (default).

`expired`Return all expired Tax Registrations.

`scheduled`Return all scheduled Tax Registrations.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A list of Tax Registration objects.

GET/v1/tax/registrationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/tax/registrations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/tax/registrations",  "has_more": false,  "data": [    {      "id": "taxreg_NkyGPRPytKq66j",      "object": "tax.registration",      "active_from": 1682036640,      "country": "US",      "country_options": {        "us": {          "state": "CA",          "type": "state_sales_tax"        }      },      "created": 1682006400,      "expires_at": null,      "livemode": false,      "status": "active",      "state": "CA",      "type": "standard"    }    {...}    {...}  ],}`# Tax Transactions

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: Calculate tax in your custom payment flow

Endpoints
Show

# Tax Settings

You can use Tax Settings to manage configurations used by Stripe Tax calculations.

Related guide: Using the Settings API

Endpoints
Show

# Verification Session

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

Related guide: The Verification Sessions API

Endpoints
Show

# Verification Report

A VerificationReport is the result of an attempt to collect and verify data from a user. The collection of verification checks performed is determined from the type and options parameters used. You can find the result of each verification check performed in the appropriate sub-resource: document, id_number, selfie.

Each VerificationReport contains a copy of any data collected by the user as well as reference IDs which can be used to access collected images through the FileUpload API. To configure and create VerificationReports, use the VerificationSession API.

Related guides: Accessing verification results.

Endpoints
Show

# Crypto Onramp Session

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