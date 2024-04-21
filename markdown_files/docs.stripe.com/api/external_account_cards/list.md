htmlList all cards | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# List all cards

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

DELETE/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAz2x2eZvKYlo2C75wJ1YUs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "card_1NAz2x2eZvKYlo2C75wJ1YUs",  "object": "card",  "deleted": true}`# Person

This is an object representing a person associated with a Stripe account.

A platform cannot access a Standard or Express account’s persons after the account starts onboarding, such as after generating an account link for the account. See the Standard onboarding or Express onboarding documentation for information about platform prefilling and account onboarding steps.

Related guide: Handling identity verification with the API

Endpoints
Show

# Top-ups

To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.

Related guide: Topping up your platform account

Endpoints
Show

# Transfers

A Transfer object is created when you move funds between Stripe accounts as part of Connect.

Before April 6, 2017, transfers also represented movement of funds from a Stripe account to a card or bank account. This behavior has since been split out into a Payout object, with corresponding payout endpoints. For more information, read about the transfer/payout split.

Related guide: Creating separate charges and transfers

Endpoints
Show

# Transfer Reversals

Stripe Connect platforms can reverse transfers made to a connected account, either entirely or partially, and can also specify whether to refund any related application fees. Transfer reversals add to the platform’s balance and subtract from the destination account’s balance.

Reversing a transfer that was made for a destination charge is allowed only up to the amount of the charge. It is possible to reverse a transfer_group transfer only if the destination account has enough balance to cover the reversal.

Related guide: Reverse transfers

Endpoints
Show

# Secrets

Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

The primary resource in Secret Store is a secret. Other apps can’t view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

All Dashboard users and the app backend share account scoped secrets. Use the account scope for secrets that don’t change per-user, like a third-party API key.

A user scoped secret is accessible by the app backend and one specific Dashboard user. Use the user scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

Related guide: Store data between page reloads

Endpoints
Show

# Early Fraud Warning

An early fraud warning indicates that the card issuer has notified us that a charge may be fraudulent.

Related guide: Early fraud warnings

Endpoints
Show

# Reviews

Reviews can be used to supplement automated fraud detection with human expertise.

Learn more about Radar and reviewing payments here.

Endpoints
Show

# Value Lists

Value lists allow you to group values together which can then be referenced in rules.

Related guide: Default Stripe lists

Endpoints
Show

# Value List Items

Value list items allow you to add specific values to a given Radar value list, which can then be used in rules.

Related guide: Managing list items

Endpoints
Show

# Authorizations

When an issued card is used to make a purchase, an Issuing Authorization object is created. Authorizations must be approved for the purchase to be completed successfully.

Related guide: Issued card authorizations

Endpoints
Show

# Cardholders

An Issuing Cardholder object represents an individual or business entity who is issued cards.

Related guide: How to create a cardholder

Endpoints
Show

# Cards

You can create physical or virtual cards that are issued to cardholders.

Endpoints
Show

# Disputes

As a card issuer, you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.

Related guide: Issuing disputes

Endpoints
Show

# Funding Instructions

Funding Instructions contain reusable bank account and routing information. Push funds to these addresses via bank transfer to top up Issuing Balances.

Endpoints
Show

# Personalization Designs

A Personalization Design is a logical grouping of a Physical Bundle, card logo, and carrier text that represents a product line.

Endpoints
Show

# Physical Bundles

A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.

Endpoints
Show

# TokensPreview feature

An issuing token object is created when an issued card is added to a digital wallet. As a card issuer, you can view and manage these tokens through Stripe.

Endpoints
Show

# Transactions

Any use of an issued card that results in funds entering or leaving your Stripe account, such as a completed purchase or refund, is represented by an Issuing Transaction object.

Related guide: Issued card transactions

Endpoints
Show

# Connection Token

A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

Related guide: Fleet management

Endpoints
Show

# Location

A Location represents a grouping of readers.

Related guide: Fleet management

Endpoints
Show

# Reader

A Reader represents a physical device for accepting payment details.

Related guide: Connecting to a reader

Endpoints
Show

# Terminal Hardware OrderPreview feature

A TerminalHardwareOrder represents an order for Terminal hardware, containing information such as the price, shipping information and the items ordered.

Endpoints
Show

# Terminal Hardware ProductPreview feature

A TerminalHardwareProduct is a category of hardware devices that are generally similar, but may have variations depending on the country it’s shipped to.

TerminalHardwareSKUs represent variations within the same Product (for example, a country specific device). For example, WisePOS E is a TerminalHardwareProduct and a WisePOS E - US and WisePOS E - UK are TerminalHardwareSKUs.

Endpoints
Show

# Terminal Hardware SKUPreview feature

A TerminalHardwareSKU represents a SKU for Terminal hardware. A SKU is a representation of a product available for purchase, containing information such as the name, price, and images.

Endpoints
Show

# Terminal Hardware Shipping MethodPreview feature

A TerminalHardwareShipping represents a Shipping Method for Terminal hardware. A Shipping Method is a country-specific representation of a way to ship hardware, containing information such as the country, name, and expected delivery date.

Endpoints
Show

# Configuration

A Configurations object represents how features should be configured for terminal readers.

Endpoints
Show

# Financial Accounts

Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance. FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.

Endpoints
Show

# Financial Account Features

Encodes whether a FinancialAccount has access to a particular Feature, with a status enum and associated status_details. Stripe or the platform can control Features via the requested field.

Endpoints
Show

# Transactions

Transactions represent changes to a FinancialAccount’s balance.

Endpoints
Show

# Transaction Entries

TransactionEntries represent individual units of money movements within a single Transaction.

Endpoints
Show

# Outbound Transfers

Use OutboundTransfers to transfer funds from a FinancialAccount to a PaymentMethod belonging to the same entity. To send funds to a different party, use OutboundPayments instead. You can send funds over ACH rails or through a domestic wire transfer to a user’s own external bank account.

Simulate OutboundTransfer state changes with the /v1/test_helpers/treasury/outbound_transfers endpoints. These methods can only be called on test mode objects.

Endpoints
Show

# Outbound Payments

Use OutboundPayments to send funds to another party’s external bank account or FinancialAccount. To send money to an account belonging to the same user, use an OutboundTransfer.

Simulate OutboundPayment state changes with the /v1/test_helpers/treasury/outbound_payments endpoints. These methods can only be called on test mode objects.

Endpoints
Show

# Inbound Transfers

Use InboundTransfers to add funds to your FinancialAccount via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

Endpoints
Show

# Received Credits

ReceivedCredits represent funds sent to a FinancialAccount (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

Endpoints
Show

# Received Debits

ReceivedDebits represent funds pulled from a FinancialAccount. These are not initiated from the FinancialAccount.

Endpoints
Show

# Credit Reversals

You can reverse some ReceivedCredits depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.

Endpoints
Show

# Debit Reversals

You can reverse some ReceivedDebits depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

Endpoints
Show

# Feature

A feature represents a monetizable ability or functionality in your system. Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.

Endpoints
Show

# Product Feature

A product_feature represents an attachment between a feature and a product. When a product is purchased that has a feature attached, Stripe will create an entitlement to the feature for the purchasing customer.

Endpoints
Show

# Active Entitlement

An active entitlement describes access to a feature for a customer.

Endpoints
Show

# Scheduled Queries

If you have scheduled a Sigma query, you’ll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.

Endpoints
Show

# Report Runs

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