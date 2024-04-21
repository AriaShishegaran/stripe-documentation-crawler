htmlCancel a VerificationSession | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Cancel a VerificationSession

A VerificationSession object can be canceled when it is in requires_input status.

Once canceled, future submission attempts are disabled. This cannot be undone. Learn more.

### Parameters

No parameters.

### Returns

Returns the canceled VerificationSession object

POST/v1/identity/verification_sessions/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN3kLkdIwHu7ixk5OvTq3b/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "vs_1NuN3kLkdIwHu7ixk5OvTq3b",  "object": "identity.verification_session",  "client_secret": null,  "created": 1695680120,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": null,  "status": "canceled",  "type": "document",  "url": null}`# Redact a VerificationSession

Redact a VerificationSession to remove all collected information from Stripe. This will redact the VerificationSession and all objects related to it, including VerificationReports, Events, request logs, etc.

A VerificationSession object can be redacted when it is in requires_input or verified status. Redacting a VerificationSession in requires_action state will automatically cancel it.

The redaction process may take up to four days. When the redaction process is in progress, the VerificationSession’s redaction.status field will be set to processing; when the process is finished, it will change to redacted and an identity.verification_session.redacted event will be emitted.

Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the fields that contain personal data will be replaced by the string [redacted] or a similar placeholder. The metadata field will also be erased. Redacted objects cannot be updated or used for any purpose.

Learn more.

### Parameters

No parameters.

### Returns

Returns the redacted VerificationSession object

POST/v1/identity/verification_sessions/:id/redactServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN3kLkdIwHu7ixk5OvTq3b/redact \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "vs_1NuN3kLkdIwHu7ixk5OvTq3b",  "object": "identity.verification_session",  "client_secret": null,  "created": 1695680120,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": {    "status": "processing"  },  "status": "canceled",  "type": "document",  "url": null}`# Verification Report

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