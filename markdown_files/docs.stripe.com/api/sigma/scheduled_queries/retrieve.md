htmlRetrieve a scheduled query run | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a scheduled query run

Retrieves the details of an scheduled query run.

### Parameters

No parameters.

### Returns

Returns the scheduled query run object if a valid identifier was provided.

GET/v1/sigma/scheduled_query_runs/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/sigma/scheduled_query_runs/sqr_1NpIuH2eZvKYlo2CP72f3rLR \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "object": "list",  "url": "/v1/sigma/scheduled_query_runs",  "has_more": false,  "data": [    {      "id": "sqr_1NpIuH2eZvKYlo2CP72f3rLR",      "object": "scheduled_query_run",      "created": 1694472517,      "data_load_time": 1694217600,      "file": {        "id": "file_1BE4yZ2eZvKYlo2C9MeXgqcB",        "object": "file",        "created": 1508284799,        "expires_at": null,        "filename": "path",        "links": {          "object": "list",          "data": [],          "has_more": false,          "url": "/v1/file_links?file=file_1BE4yZ2eZvKYlo2C9MeXgqcB"        },        "purpose": "sigma_scheduled_query",        "size": 500,        "title": null,        "type": "csv",        "url": "https://files.stripe.com/v1/files/file_1BE4yZ2eZvKYlo2C9MeXgqcB/contents"      },      "livemode": false,      "result_available_until": 1726012800,      "sql": "SELECT count(*) from charges",      "status": "completed",      "title": "Count all charges"    }  ]}`# List all scheduled query runs

Returns a list of scheduled query runs.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A paginated list of all scheduled query runs.

GET/v1/sigma/scheduled_query_runsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/sigma/scheduled_query_runs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/sigma/scheduled_query_runs",  "has_more": false,  "data": [    {      "object": "list",      "url": "/v1/sigma/scheduled_query_runs",      "has_more": false,      "data": [        {          "id": "sqr_1NpIuH2eZvKYlo2CP72f3rLR",          "object": "scheduled_query_run",          "created": 1694472517,          "data_load_time": 1694217600,          "file": {            "id": "file_1BE4yZ2eZvKYlo2C9MeXgqcB",            "object": "file",            "created": 1508284799,            "expires_at": null,            "filename": "path",            "links": {              "object": "list",              "data": [],              "has_more": false,              "url": "/v1/file_links?file=file_1BE4yZ2eZvKYlo2C9MeXgqcB"            },            "purpose": "sigma_scheduled_query",            "size": 500,            "title": null,            "type": "csv",            "url": "https://files.stripe.com/v1/files/file_1BE4yZ2eZvKYlo2C9MeXgqcB/contents"          },          "livemode": false,          "result_available_until": 1726012800,          "sql": "SELECT count(*) from charges",          "status": "completed",          "title": "Count all charges"        }      ]    }    {...}    {...}  ],}`# Report Runs

The Report Run object represents an instance of a report type generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to a file where you can retrieve your results. For an overview, see API Access to Reports.

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

Endpoints
Show

# Report Types

The Report Type resource corresponds to a particular type of report, such as the “Activity summary” or “Itemized payouts” reports. These objects are identified by an ID belonging to a set of enumerated values. See API Access to Reports documentation for those Report Type IDs, along with required and optional parameters.

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

Endpoints
Show

# Accounts

A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

Endpoints
Show

# Account Owner

Describes an owner of an account.

Endpoints
Show

# Session

A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.

Endpoints
Show

# Transactions

A Transaction represents a real transaction that affects a Financial Connections Account balance.

Endpoints
Show

# Tax Calculations

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