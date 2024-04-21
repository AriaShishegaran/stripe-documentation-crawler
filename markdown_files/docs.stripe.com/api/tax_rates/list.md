htmlList all tax rates | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# List all tax rates

Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.

### Parameters

- activebooleanOptional flag to filter by tax rates that are either active or inactive (archived).



### More parametersExpand all

- createdobject
- ending_beforestring
- inclusiveboolean
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit tax rates, starting after tax rate starting_after. Each entry in the array is a separate tax rate object. If no more tax rates are available, the resulting array will be empty.

GET/v1/tax_ratesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/tax_rates \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/tax_rates",  "has_more": false,  "data": [    {      "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",      "object": "tax_rate",      "active": true,      "country": null,      "created": 1682114687,      "description": "VAT Germany",      "display_name": "VAT",      "inclusive": false,      "jurisdiction": "DE",      "livemode": false,      "metadata": {},      "percentage": 16,      "state": null,      "tax_type": null    }    {...}    {...}  ],}`# Retrieves a tax rate

Retrieves a tax rate with the given ID

### Parameters

No parameters.

### Returns

Returns an tax rate if a valid tax rate ID was provided. Raises an error otherwise.

GET/v1/tax_rates/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",  "object": "tax_rate",  "active": true,  "country": null,  "created": 1682114687,  "description": "VAT Germany",  "display_name": "VAT",  "inclusive": false,  "jurisdiction": "DE",  "livemode": false,  "metadata": {},  "percentage": 16,  "state": null,  "tax_type": null}`# Shipping Rates

Shipping rates describe the price of shipping presented to your customers and applied to a purchase. For more information, see Charge for shipping.

Endpoints
Show

# Sessions

A Checkout Session represents your customer’s session as they pay for one-time purchases or subscriptions through Checkout or Payment Links. We recommend creating a new Session each time your customer attempts to pay.

Once payment is successful, the Checkout Session will contain a reference to the Customer, and either the successful PaymentIntent or an active Subscription.

You can create a Checkout Session on your server and redirect to its URL to begin Checkout.

Related guide: Checkout quickstart

Endpoints
Show

# Payment Link

A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.

When a customer opens a payment link it will open a new checkout session to render the payment page. You can use checkout session events to track payments through payment links.

Related guide: Payment Links API

Endpoints
Show

# Credit Note

Issue a credit note to adjust an invoice’s amount after the invoice is finalized.

Related guide: Credit notes

Endpoints
Show

# Customer Balance Transaction

Each customer has a Balance value, which denotes a debit or credit that’s automatically applied to their next invoice upon finalization. You may modify the value directly by using the update customer API, or by creating a Customer Balance Transaction, which increments or decrements the customer’s balance by the specified amount.

Related guide: Customer balance

Endpoints
Show

# Customer Portal Session

The Billing customer portal is a Stripe-hosted UI for subscription and billing management.

A portal configuration describes the functionality and features that you want to provide to your customers through the portal.

A portal session describes the instantiation of the customer portal for a particular customer. By visiting the session’s URL, the customer can manage their subscriptions and billing details. For security reasons, sessions are short-lived and will expire if the customer does not visit the URL. Create sessions on-demand when customers intend to manage their subscriptions and billing details.

Learn more in the integration guide.

Endpoints
Show

# Customer Portal Configuration

A portal configuration describes the functionality and behavior of a portal session.

Endpoints
Show

# Invoices

Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.

They contain invoice items, and proration adjustments that may be caused by subscription upgrades/downgrades (if necessary).

If your invoice is configured to be billed through automatic charges, Stripe automatically finalizes your invoice and attempts payment.  Note that finalizing the invoice, when automatic, does not happen immediately as the invoice is created. Stripe waits until one hour after the last webhook was successfully sent (or the last webhook timed out after failing). If you (and the platforms you may have connected to) have no webhooks configured, Stripe waits one hour after creation to finalize the invoice.

If your invoice is configured to be billed by sending an email, then based on your email settings, Stripe will email the invoice to your customer and await payment. These emails can contain a link to a hosted page to pay the invoice.

Stripe applies any customer credit on the account before determining the amount due for the invoice (i.e., the amount that will be actually charged). If the amount due for the invoice is less than Stripe’s minimum allowed charge per currency, the invoice is automatically marked paid, and we add the amount due to the customer’s credit balance which is applied to the next invoice.

More details on the customer’s credit balance are here.

Related guide: Send invoices to customers

Endpoints
Show

# Invoice Items

Invoice Items represent the component lines of an invoice. An invoice item is added to an invoice by creating or updating it with an invoice field, at which point it will be included as an invoice line item within invoice.lines.

Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined with a subscription. Sometimes you want to add a charge or credit to a customer, but actually charge or credit the customer’s card only at the end of a regular billing cycle. This is useful for combining several charges (to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

Related guides: Integrate with the Invoicing API, Subscription Invoices.

Endpoints
Show

# Meters

A billing meter is a resource that allows you to track usage of a particular event. For example, you might create a billing meter to track the number of API calls made by a particular user. You can then attach the billing meter to a price and attach the price to a subscription to charge the user for the number of API calls they make.

Endpoints
Show

# Meter Events

A billing meter event represents a customer’s usage of a product. Meter events are used to bill a customer based on their usage. Meter events are associated with billing meters, which define the shape of the event’s payload and how those events are aggregated for billing.

Endpoints
Show

# Meter Event Adjustment

A billing meter event adjustment is a resource that allows you to cancel a meter event. For example, you might create a billing meter event adjustment to cancel a meter event that was created in error or attached to the wrong customer.

Endpoints
Show

# Meter Event Summary

A billing meter event summary represents an aggregated view of a customer’s billing meter events within a specified timeframe. It indicates how much usage was accrued by a customer for that period.

Endpoints
Show

# Plans

You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.

Plans define the base price, currency, and billing cycle for recurring purchases of products. Products help you track inventory or provisioning, and plans help you track pricing. Different physical goods or levels of service should be represented by products, and pricing options should be represented by plans. This approach lets you change prices without having to change your provisioning scheme.

For example, you might have a single “gold” product that has plans for $10/month, $100/year, €9/month, and €90/year.

Related guides: Set up a subscription and more about products and prices.

Endpoints
Show

# Quote

A Quote is a way to model prices that you’d like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.

Endpoints
Show

# Subscriptions

Subscriptions allow you to charge a customer on a recurring basis.

Related guide: Creating subscriptions

Endpoints
Show

# Subscription Items

Subscription items allow you to create customer subscriptions with more than one plan, making it easy to represent complex billing relationships.

Endpoints
Show

# Subscription Schedule

A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

Related guide: Subscription schedules

Endpoints
Show

# Tax IDs

You can add one or multiple tax IDs to a customer or account. Customer and account tax IDs get displayed on related invoices and credit notes.

Related guides: Customer tax identification numbers, Account tax IDs

Endpoints
Show

# Test ClocksTest helper

A test clock enables deterministic control over objects in testmode. With a test clock, you can create objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances, you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.

Endpoints
Show

# Usage Records

Usage records allow you to report customer usage and metrics to Stripe for metered billing of subscription prices.

Related guide: Metered billing

This is our legacy usage-based billing API. See the updated usage-based billing docs.

Endpoints
Show

# Accounts

This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.

For Custom accounts, the properties below are always returned. For other accounts, some properties are returned until that account has started to go through Connect Onboarding. Once you create an Account Link or Account Session, some properties are only returned for Custom accounts. Learn about the differences between accounts.

Endpoints
Show

# Login Links

Login Links are single-use login link for an Express account to access their Stripe dashboard.

Endpoints
Show

# Account Links

Account Links are the means by which a Connect platform grants a connected account permission to access Stripe-hosted applications, such as Connect Onboarding.

Related guide: Connect Onboarding

Endpoints
Show

# Account Session

An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.

We recommend that you create an AccountSession each time you need to display an embedded component to your user. Do not save AccountSessions to your database as they expire relatively quickly, and cannot be used more than once.

Related guide: Connect embedded components

Endpoints
Show

# Application Fees

When you collect a transaction fee on top of a charge made for your user (using Connect), an Application Fee object is created in your account. You can list, retrieve, and refund application fees.

Related guide: Collecting application fees

Endpoints
Show

# Application Fee Refunds

Application Fee Refund objects allow you to refund an application fee that has previously been created but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

Related guide: Refunding application fees

Endpoints
Show

# Capabilities

This is an object representing a capability for a Stripe account.

Related guide: Account capabilities

Endpoints
Show

# Country Specs

Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account’s country. The Country Specs API makes these rules available to your integration.

You can also view the information from this API call as an online guide.

Endpoints
Show

# External Bank Accounts

External bank accounts are financial accounts associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected account’s Stripe balance.

Endpoints
Show

# External Account Cards

External account cards are debit cards associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected accounts Stripe balance.

Endpoints
Show

# Person

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