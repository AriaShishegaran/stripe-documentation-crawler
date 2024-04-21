htmlSubscribe to data refreshes for an Account | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Subscribe to data refreshes for an Account

Subscribes to periodic refreshes of data associated with a Financial Connections Account.

### Parameters

- featuresarray of enumsRequiredThe list of account features to which you would like to subscribe.

Possible enum values`transactions`Transactions data from the account



### Returns

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

POST/v1/financial_connections/accounts/:id/subscribeServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/financial_connections/accounts/fca_1NQay62eZvKYlo2C8dflHjWB/subscribe \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "features[]"=transactions`Response`{  "id": "fca_1NQay62eZvKYlo2C8dflHjWB",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XKzkNRiz8i3",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1688583746,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [    "transactions"  ],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": {    "id": "fctxnref_OD10iHSd7eaheDkeabbQfnJ7",    "status": "pending",    "last_attempted_at": 1625337296  }}`# Unsubscribe from data refreshes for an Account

Unsubscribes from periodic refreshes of data associated with a Financial Connections Account.

### Parameters

- featuresarray of enumsRequiredThe list of account features from which you would like to unsubscribe.

Possible enum values`transactions`Transactions data from the account



### Returns

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

POST/v1/financial_connections/accounts/:id/unsubscribeServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/financial_connections/accounts/fca_1NQayH2eZvKYlo2CMBkU6Y9s/unsubscribe \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "features[]"=transactions`Response`{  "id": "fca_1NQayH2eZvKYlo2CMBkU6Y9s",  "object": "linked_account",  "account_holder": {    "customer": "cus_9s6XKzkNRiz8i3",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1688583757,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": {    "id": "fctxnref_OD10EqMBikeOrWm7JW44fdpo",    "status": "succeeded",    "last_attempted_at": 1625337296  }}`# Account Owner

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