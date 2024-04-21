htmlRetrieve a file link | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a file link

Retrieves the file link with the given ID.

### Parameters

No parameters.

### Returns

If the identifier you provide is valid, a file link object returns. If not, Stripe raises an error.

GET/v1/file_links/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "link_1Mr23jLkdIwHu7ix65betcoo",  "object": "file_link",  "created": 1680108075,  "expired": false,  "expires_at": null,  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",  "livemode": false,  "metadata": {},  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}`# List all file links

Returns a list of file links.

### Parameters

No parameters.

### More parametersExpand all

- createdobject
- ending_beforestring
- expiredboolean
- filestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit file links, starting after the starting_after file link. Each entry in the array is a separate file link object. If there aren’t additional available file links, the resulting array is empty.

GET/v1/file_linksServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/file_links \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/file_links",  "has_more": false,  "data": [    {      "id": "link_1Mr23jLkdIwHu7ix65betcoo",      "object": "file_link",      "created": 1680108075,      "expired": false,      "expires_at": null,      "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",      "livemode": false,      "metadata": {},      "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"    }    {...}    {...}  ],}`# Mandates

A Mandate is a record of the permission that your customer gives you to debit their payment method.

Endpoints
Show

# Payment Intents

A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.

A PaymentIntent transitions through multiple statuses throughout its lifetime as it interfaces with Stripe.js to perform authentication flows and ultimately creates at most one successful charge.

Related guide: Payment Intents API

Endpoints
Show

# Setup Intents

A SetupIntent guides you through the process of setting up and saving a customer’s payment credentials for future payments. For example, you can use a SetupIntent to set up and save your customer’s card without immediately collecting a payment. Later, you can use PaymentIntents to drive the payment flow.

Create a SetupIntent when you’re ready to collect your customer’s payment credentials. Don’t maintain long-lived, unconfirmed SetupIntents because they might not be valid. The SetupIntent transitions through multiple statuses as it guides you through the setup process.

Successful SetupIntents result in payment credentials that are optimized for future payments. For example, cardholders in certain regions might need to be run through Strong Customer Authentication during payment method collection to streamline later off-session payments. If you use the SetupIntent with a Customer, it automatically attaches the resulting payment method to that Customer after successful setup. We recommend using SetupIntents or setup_future_usage on PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

Related guide: Setup Intents API

Endpoints
Show

# Setup Attempts

A SetupAttempt describes one attempted confirmation of a SetupIntent, whether that confirmation is successful or unsuccessful. You can use SetupAttempts to inspect details of a specific attempt at setting up a payment method using a SetupIntent.

Endpoints
Show

# Payouts

A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, and list all payouts. Payouts are made on varying schedules, depending on your country and industry.

Related guide: Receiving payouts

Endpoints
Show

# Refunds

Refund objects allow you to refund a previously created charge that isn’t refunded yet. Funds are refunded to the credit or debit card that’s initially charged.

Related guide: Refunds

Endpoints
Show

# Confirmation Token

ConfirmationTokens help transport client side data collected by Stripe JS over to your server for confirming a PaymentIntent or SetupIntent. If the confirmation is successful, values present on the ConfirmationToken are written onto the Intent.

To learn more about how to use ConfirmationToken, visit the related guides:

- [Finalize payments on the server](/payments/finalize-payments-on-the-server)
- [Build two-step confirmation](/payments/build-a-two-step-confirmation).

Endpoints
Show

# Tokens

Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token representing this information is returned to your server to use. Use our recommended payments integrations to perform this process on the client-side. This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.

If you can’t use client-side tokenization, you can also create tokens using the API with either your publishable or secret API key. If your integration uses this method, you’re responsible for any PCI compliance that it might require, and you must keep your secret API key safe. Unlike with client-side tokenization, your customer’s information isn’t sent directly to Stripe, so we can’t determine how it’s handled or stored.

You can’t store or use tokens more than once. To store card or bank account information for later use, create Customer objects or Custom accounts. Radar, our integrated solution for automatic fraud protection, performs best with integrations that use client-side tokenization.

Endpoints
Show

# Payment Methods

PaymentMethod objects represent your customer’s payment instruments. You can use them with PaymentIntents to collect payments or save them to Customer objects to store instrument details for future payments.

Related guides: Payment Methods and More Payment Scenarios.

Endpoints
Show

# Payment Method Configurations

PaymentMethodConfigurations control which payment methods are displayed to your customers when you don’t explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

There are two types of PaymentMethodConfigurations. Which is used depends on the charge type:

Direct configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

Child configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

Child configurations have a parent that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations are managed in the dashboard and are not available in this API.

Related guides:

- [Payment Method Configurations API](/connect/payment-method-configurations)
- [Multiple configurations on dynamic payment methods](/payments/multiple-payment-method-configs)
- [Multiple configurations for your Connect accounts](/connect/multiple-payment-method-configurations)

Endpoints
Show

# Payment Method Domains

A payment method domain represents a web domain that you have registered with Stripe. Stripe Elements use registered payment method domains to control where certain payment methods are shown.

Related guides: Payment method domains.

Endpoints
Show

# Bank Accounts

These bank accounts are payment methods on Customer objects.

On the other hand External Accounts are transfer destinations on Account objects for Custom accounts. They can be bank accounts or debit cards as well, and are documented in the links above.

Related guide: Bank debits and transfers

Endpoints
Show

# Cash Balance

A customer’s Cash balance represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.

Endpoints
Show

# Cash Balance Transaction

Customers with certain payments enabled have a cash balance, representing funds that were paid by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions represent when funds are moved into or out of this balance. This includes funding by the customer, allocation to payments, and refunds to the customer.

Endpoints
Show

# Cards

You can store multiple cards on a customer in order to charge the customer later. You can also store multiple debit cards on a recipient in order to transfer to those cards later.

Related guide: Card payments with Sources

Endpoints
Show

# SourcesDeprecated

Source objects allow you to accept a variety of payment methods. They represent a customer’s payment instrument, and can be used with the Stripe API just like a Card object: once chargeable, they can be charged, or can be attached to customers.

Stripe doesn’t recommend using the deprecated Sources API. We recommend that you adopt the PaymentMethods API. This newer API provides access to our latest features and payment method types.

Related guides: Sources API and Sources & Customers.

Endpoints
Show

# Products

Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product. They can be used in conjunction with Prices to configure pricing in Payment Links, Checkout, and Subscriptions.

Related guides: Set up a subscription, share a Payment Link, accept payments with Checkout, and more about Products and Prices

Endpoints
Show

# Prices

Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

For example, you might have a single “gold” product that has prices for $10/month, $100/year, and €9 once.

Related guides: Set up a subscription, create an invoice, and more about products and prices.

Endpoints
Show

# Coupons

A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. Coupons do not work with conventional one-off charges or payment intents.

Endpoints
Show

# Promotion Code

A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.

Endpoints
Show

# Discounts

A discount represents the actual application of a coupon or promotion code. It contains information about when the discount began, when it will end, and what it is applied to.

Related guide: Applying discounts to subscriptions

Endpoints
Show

# Tax Code

Tax codes classify goods and services for tax purposes.

Endpoints
Show

# Tax Rate

Tax rates can be applied to invoices, subscriptions and Checkout Sessions to collect tax.

Related guide: Tax rates

Endpoints
Show

# Shipping Rates

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