# Collect a bank account to optimize ACH Direct Debit payments with account data

Not sure about which Financial Connections integration to use? See our overview of integration options.

[overview of integration options](/financial-connections/use-cases)

Stripe offers a number of ways to accept ACH Direct Debit payments from your users. All of these methods require that you verify the user’s account before you can debit their account. Financial Connections is the secure method offered by Stripe to perform instant bank account verification, that’s also extensible to more powerful features such as balance or ownership checks. When using Financial Connections to power your ACH flows, you can:

[verify](/payments/ach-debit#verification)

- Reduce payment failure rate from closed or inactive accounts

- Improve payments conversion by keeping users on session, instead of forcing them to leave your payments flow to locate their account and routing numbers

- Save development time by eliminating the need to create a custom bank account collection form

- Enable the collection of additional bank account data, such as balances and ownership information, to further optimize your integration

## Before you begin

Financial Connections is the default verification method for all hosted ACH payment flows, such as Checkout or the Payment Element. If you use a hosted flow, skip directly to accessing additional account data. If you’re not already set up to collect ACH payments, set that up first.

[accessing additional account data](#access)

[set that up](/payments/ach-debit/accept-a-payment?platform=web&ui=stripe-hosted)

[Enable Financial Connections](#enable)

## Enable Financial Connections

The verification_method parameter on various API resources controls whether Financial Connections is enabled for bank account verification. Financial Connections with microdeposit fallback is the default.

Bank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.

This option is available on the following APIs:

Additional steps might be required for non-hosted integrations. See this section of the ACH guide.

[this section of the ACH guide](/payments/ach-debit/accept-a-payment?platform=web&ui=direct-api#web-collect-details)

- PaymentIntent

[PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method_options-us_bank_account-verification_method)

- SetupIntent

[SetupIntent](/api/setup_intents/create#create_setup_intent-payment_method_options-us_bank_account-verification_method)

- CheckoutSession

[CheckoutSession](/api/checkout/sessions/create#create_checkout_session-payment_method_options-us_bank_account-verification_method)

- Invoice

[Invoice](/api/invoices/create#create_invoice-payment_settings-payment_method_options-us_bank_account-verification_method)

- Subscription

[Subscription](/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-us_bank_account-verification_method)

- Payment Element

[Payment Element](/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method)

[Create a customerRecommended](#customer)

## Create a customerRecommended

We recommend that you create a Customer with an email address to represent your user, that you then attach to your payment. Attaching a Customer object allows you to list previously linked accounts  later. By providing an email address on the Customer object, Financial Connections can improve the authentication flow by streamlining sign-in or sign-up for your user, depending on whether they’re a returning Link user.

[Customer](/api/customers)

[list previously linked accounts](/api/financial_connections/accounts/list)

[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)

[Request access to additional account data](#access)

## Request access to additional account data

To access additional account data on Financial Connections Accounts, first make sure you’ve submitted your Financial Connections application by checking Financial Connections settings in the Dashboard. To view this page, activate your account. How you configure which types of account data you have access to depends on your integration.

[Financial Connections settings in the Dashboard](https://dashboard.stripe.com/settings/financial-connections)

If you use Stripe’s dynamic payment method feature to collect ACH payments for non-Connect use cases, you can configure requested Financial Connections data directly from the ACH Dashboard settings page. Account and routing number is always required for ACH debits; other data types are optional.

[dynamic payment method feature](/payments/payment-methods/dynamic-payment-methods)

[ACH Dashboard settings page](https://dashboard.stripe.com/settings/payment_methods/us_bank_account)

We recommend configuring permissions in the Dashboard because it allows you to change which data you collect without any code changes.

To override the Dashboard configuration, specify Financial Connections permissions directly in the API. To do this for PaymentIntents:

[Use data to optimize ACH integration](#optimize)

## Use data to optimize ACH integration

After you have been approved for additional bank account data access like balances or ownership, you can use this data to optimize ACH payments performance. For example, you can use balance data to reduce the risk of insufficient funds failures. See related data guides for examples:

- Balances: check account balance prior to payment initiation to reduce NSFs.

[Balances](/financial-connections/balances)

- Ownership: pull account owners and compare against your internal data models to catch potential fraud.

[Ownership](/financial-connections/ownership)

- Transactions: pull an account’s transaction history to check when the customer’s paycheck might land.

[Transactions](/financial-connections/transactions)

To initiate data refreshes and retrieve data on a Financial Connections Account, you first need to get the account’s ID from the linked Payment Method by expanding the Payment Intent’s payment_method property:

The Financial Connections Account ID is on the expanded Payment Method’s us_bank_account hash. If you allow manual entry fallback and the user manually entered their account information, this field is null.

[us_bank_account hash](/api/payment_methods/object#payment_method_object-us_bank_account)

[manual entry fallback](/financial-connections/ach-direct-debit-payments#enable)
