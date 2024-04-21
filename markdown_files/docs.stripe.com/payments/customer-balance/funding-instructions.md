htmlFunding instructions | Stripe Documentation[Skip to content](#main-content)Funding instructions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Ffunding-instructions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Ffunding-instructions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank transfers](/docs/payments/bank-transfers)[Customer balance](/docs/payments/customer-balance)# Funding instructions

Provide customer balance funding instructions without creating a PaymentIntent.This guide describes how to retrieve instructions for funding the customer’s cash balance without creating a PaymentIntent. Funding instructions are typically useful if you’re accepting payments from larger companies who require these details before you send them an invoice or request for payment.

Most users rely on this API for a first-time customer signup flow.  If a customer selects bank transfers as their preferred payment method, you can call this endpoint to get the funding instructions right away rather than waiting for the first PaymentIntent or Invoice to be created.

The funding instructions will always be the same for a given customer across both the Customer Balance Funding Instructions API and the PaymentIntents API. As with PaymentIntents, you can request funding instructions using the bank transfer type and currency that best fits your customer.

[Create or retrieve funding instructionsServer-side](#create-funding-instructions)Use the Customer Balance Funding Instructions API to retrieve a set of financial_addresses that can receive funds from the customer. Provide these bank account details to your customer so that they can initiate a bank transfer using any of the supported_networks.

NoteIn live mode, Stripe supplies each customer with a unique set of bank transfer details. In contrast, Stripe offers invalid bank transfer details to all customers in test mode. Unlike live mode, these invalid details might not always be unique.

USUKEUJPMXCommand Line[curl](#)`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}}/funding_instructions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d funding_type=bank_transfer \
  -d "bank_transfer[type]"=us_bank_transfer \
  -d currency=usd`The response contains the following fields:

USUKEUJPMX### Bank transfer hash

FieldValuesDescription`type``us_bank_transfer`The type of bank transfer to use.`currency``usd`The supported currency for the bank transfer.`country``US`The two-letter country code of the bank account to transfer to.`financial_addresses`- `aba`hash
- `swift`hash

The list of financial addresses. Funds sent to any address are routed to the customer balance.### ABA hash

FieldValuesDescription`type``aba`The type of financial address.`supported_networks`- `ach`
- `domestic_wire_us`

The list of networks supported by this address.`aba.account_number`111222333444The ABA account number.`aba.routing_number`444555666The ABA routing number.`aba.bank_name`Wells Fargo Bank, NAThe name of the bank.### SWIFT hash

FieldValuesDescription`type``swift`The type of financial address.`supported_networks``swift`The list of networks supported by this address.`swift.account_number`111222333444The SWIFT account number.`swift.swift_code`AAAA-BB-CC-123The SWIFT code.`swift.bank_name`Wells Fargo Bank, NAThe name of the bank.[Download confirmation of account ownership](#vban-confirmation-letters)Some customers might request additional assurance that the account they’re transferring money into is yours, because the account might be listed as owned by Stripe. To provide this assurance, you can generate a letter confirming your ownership of the account to the customer. In this letter, Stripe confirms that you’re the owner of the virtual bank account corresponding to the account details you have passed to that customer.

To download a letter confirming account ownership:

1. Navigate to the Customers page in the Dashboard.


2. Select the customer who has requested additional verification that you own the account.


3. Navigate to their cash balance details. This page shows the account details that the customer must use to pay you by bank transfer.


4. Click the button to download a confirmation letter in a PDF format with today’s date.



![Button to download confirmation of account ownership](https://b.stripecdn.com/docs-statics-srv/assets/vban-confirmation-letter-button.cfd3f902e44069f96d011b7fb8cba336.png)

Download confirmation of account ownership

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create or retrieve funding instructions](#create-funding-instructions)[Download confirmation of account ownership](#vban-confirmation-letters)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`