htmlFinancial Connections use cases | Stripe Documentation[Skip to content](#main-content)Use cases[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fuse-cases)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fuse-cases)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Financial Connections use cases

View options for integrating Financial Connections and common use cases.Financial Connections allows your users to link their financial accounts to collect ACH payments, facilitate Connect payouts, and build financial data products. It also enables your users to connect their accounts in fewer steps with Link, allowing them to save and quickly reuse their bank account details across Stripe merchants. View the following integration paths based on your requirements, and some common use cases for Financial Connections data below.

How you integrate Financial Connections depends on your desired use cases.

Use caseExampleRecommended integration[ACH Direct Debit payments](#ach-direct-debit)- Bank-based payments
- Wallet transfers and top-ups
- Bill payments

An ACH payments integration:- [Setup Intents](/api/setup_intents)
- [Payment Intents](/api/payment_intents)
- [Checkout](/payments/checkout)
- [Invoices](/invoicing)

[Connect payouts](#custom-connect-payouts)- Pay out funds to Connected Accounts

A Connect onboarding integration:- [Hosted onboarding](/connect/payouts-bank-accounts?bank-account-collection-integration=prebuilt-web-form)
- [Setup Intents](/connect/payouts-bank-accounts?bank-account-collection-integration=direct-api#create-a-setup-intent)

[Building financial products](#building-other-products)- Financial management application
- Wealth management application
- Loan underwriting

[Financial Connections Sessions](/api/financial_connections/sessions/object)To process ACH payments or facilitate Connect payouts, use a recommended payments integration in the table above, such as Setup Intents. This makes sure that the collected accounts are compatible with ACH transfers.

The Financial Connections Sessions API provides more flexibility for use cases that won’t use the collected accounts for ACH payments or Connect payouts. It has configuration options that let your users link additional account types that aren’t compatible with ACH, and you can collect multiple accounts in a single session.

Regardless of which API you choose to integrate with, you can request access to additional data on your users’ financial accounts. You can then use this data to optimize your integration or create more complex products. The following sections provide more context on the above use cases, including recommendations on which data to access.

[ACH Direct Debit payments](#ach-direct-debit)### Recommended data

- [Balances](/financial-connections/balances)

In accordance with Nacha regulations, you must verify a user’s account to accept an ACH Direct Debit payment or transfer. With Financial Connections, your customer authenticates their bank account and provides permission to share the details you need to charge their account, such as a tokenized account and routing number.

Collecting bank account details from a customer with Financial Connections can help you:

- Improve payment reliability by verifying that a user’s bank account is open and able to accept ACH direct debits.
- Increase checkout conversion by eliminating the need for your customers to leave your website or application to locate their account and routing numbers.
- Save development time by eliminating the need for you to build bank account form validation when your customer enters account details.

To verify a bank account to accept an ACH Direct Debit payment with Financial Connections, use Stripe’s Payment Intent or Setup Intent APIs. Alternatively, you can use a hosted Stripe payments integration such as Checkout or the Payment Element.

Learn how to collect a bank account to accept an ACH Direct Debit payment.

Optionally, you can request permission from your customers to retrieve additional data on their Financial Connections account. We recommend that you access balances data to perform balance checks prior to processing the payment.

Manual account entry and microdeposit verification are available as a fallback method for this use case. However, accounts that you add through microdeposits won’t have access to additional account data.

[Custom Connect payouts](#custom-connect-payouts)### Recommended data

- [Ownership](/financial-connections/ownership)

Use Financial Connections with Connect to verify bank accounts for Custom connected accounts, thereby facilitating payouts. This allows your connected account to authenticate its own bank account and provide permission to share details you need for payouts, like tokenized account and routing numbers.

Collecting account details from your connected account with Financial Connections can help you:

- Increase onboarding conversion by eliminating the need for your connected account to leave your website or application to locate their account and routing numbers.
- Reduce first payout failure rates by eliminating errors that result from manual entry of account and routing numbers.
- Make sure you don’t need to store sensitive data such as account and routing numbers on your server.
- Save development time by eliminating the need for you to build bank account form validation when your connected account enters their bank account details.

Optionally, you can request permission from your connected account to retrieve additional data on their Financial Connections account. Consider accessing ownership details to optimize your onboarding process. Retrieving ownership data on an account can help you mitigate fraud by verifying an account’s ownership details, such as the name and address of the account holder.

Learn how to collect a bank account to initiate payouts to a US Custom Connect account.

Manual account entry and microdeposit verification are available as a fallback method for this use case (for example, if your connected account can’t find their institution or otherwise authenticate). However, accounts that you add through microdeposits won’t have access to additional account data.

[Building financial products](#building-other-products)### Recommended data

- [Balances](/financial-connections/balances)
- [Ownership](/financial-connections/ownership)
- [Transactions](/financial-connections/transactions)

Use Financial Connections to access external bank account data that you can use to build financial products.

After your user has consented to share data from their financial accounts, you can retrieve data for various use cases, such as:

- Help your user track expenses, handle bills, manage their finances and take control of their financial well-being with[transactions](/financial-connections/transactions)data.
- Speed up underwriting and improve access to credit and other financial services with transactions and balances data.

Learn how to collect an account to access data using Financial Connections’ Sessions API.

Manual account entry and microdeposit verification aren’t available in the authentication flow for this use case because the primary goal of collecting an account is data accessibility.

You can convert most previously linked Financial Connections accounts to Payment Methods. However, if your integration uses the Sessions API, the linked account might not be compatible with ACH.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[ACH Direct Debit payments](#ach-direct-debit)[Custom Connect payouts](#custom-connect-payouts)[Building financial products](#building-other-products)Products Used[Financial Connections](/financial-connections)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`