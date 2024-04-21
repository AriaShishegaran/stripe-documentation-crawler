htmlRetrieve a Transaction | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a Transaction

Retrieves the details of a Financial Connections Transaction

### Parameters

No parameters.

### Returns

Returns a Transaction object if a valid identifier was provided, and raises an error otherwise.

GET/v1/financial_connections/transactions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/financial_connections/transactions/fctxn_1MwVKd2eZvKYlo2ChNw2UxSa \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fctxn_1MwVKd2eZvKYlo2ChNw2UxSa",  "object": "financial_connections.transaction",  "account": "fca_1MwVKd2eZvKYlo2CnlgoF3I4",  "amount": 300,  "currency": "usd",  "description": "Rocket Rides",  "livemode": false,  "status": "posted",  "status_transitions": {    "posted_at": 1681412239,    "void_at": null  },  "transacted_at": 1681412239,  "transaction_refresh": "fctxnref_NhvAgiKSFDg9jOe6eIlj41X5",  "updated": 1681412239}`# List Transactions

Returns a list of Financial Connections Transaction objects.

### Parameters

- accountstringRequiredThe ID of the Stripe account whose transactions will be retrieved.


- transacted_atobjectA filter on the list based on the object transacted_at field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options:

Show child parameters
- transaction_refreshobjectA filter on the list based on the object transaction_refresh field. The value can be a dictionary with the following options:

Show child parameters

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit Transaction objects, starting after transaction starting_after. Each entry in the array is a separate Transaction object. If no more transactions are available, the resulting array will be empty.

GET/v1/financial_connections/transactionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/financial_connections/transactions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d account=fca_1NpHiT2eZvKYlo2C6pRwOFjr \  -d limit=3`Response`{  "object": "list",  "url": "/v1/financial_connections/transactions",  "has_more": false,  "data": [    {      "id": "fctxn_1NpHiT2eZvKYlo2CZFvnM3HJ",      "object": "financial_connections.transaction",      "account": "fca_1NpHiT2eZvKYlo2C6pRwOFjr",      "amount": 300,      "currency": "usd",      "description": "Rocket Rides",      "livemode": false,      "status": "posted",      "status_transitions": {        "posted_at": 1694467941,        "void_at": null      },      "transacted_at": 1694467941,      "transaction_refresh": "fctxnref_OcWmGrWptAdJ2bmpYE2P0Hws",      "updated": 1694467941    }    {...}    {...}  ],}`# Tax Calculations

A Tax Calculation allows you to calculate the tax to collect from your customer.

Related guide: Calculate tax in your custom payment flow

Endpoints
Show

# Tax Registrations

A Tax Registration lets us know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax.

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax Registration object. For more information on how to register to collect tax, see our guide.

Related guide: Using the Registrations API

Endpoints
Show

# Tax Transactions

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