htmlCollect a bank account to optimize ACH Direct Debit payments with account data | Stripe Documentation[Skip to content](#main-content)ACH Direct Debit payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fach-direct-debit-payments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fach-direct-debit-payments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Collect a bank account to optimize ACH Direct Debit payments with account data

Collect a customer's bank account for ACH Direct Debit payments, and use account data such as balances to optimize your payments integration.Not sure about which Financial Connections integration to use? See our overview of integration options.

Stripe offers a number of ways to accept ACH Direct Debit payments from your users. All of these methods require that you verify the user’s account before you can debit their account. Financial Connections is the secure method offered by Stripe to perform instant bank account verification, that’s also extensible to more powerful features such as balance or ownership checks. When using Financial Connections to power your ACH flows, you can:

- Reduce payment failure rate from closed or inactive accounts
- Improve payments conversion by keeping users on session, instead of forcing them to leave your payments flow to locate their account and routing numbers
- Save development time by eliminating the need to create a custom bank account collection form
- Enable the collection of additional bank account data, such as balances and ownership information, to further optimize your integration

## Before you begin

Financial Connections is the default verification method for all hosted ACH payment flows, such as Checkout or the Payment Element. If you use a hosted flow, skip directly to accessing additional account data. If you’re not already set up to collect ACH payments, set that up first.

[Enable Financial Connections](#enable)The verification_method parameter on various API resources controls whether Financial Connections is enabled for bank account verification. Financial Connections with microdeposit fallback is the default.

Common mistakeBank accounts that your customers link through manual entry and microdeposits won’t have access to additional bank account data like balances, ownership, and transactions.

Verification methodDescription`automatic`(default)Financial Connections with the option to manually enter bank account information and use microdeposits`instant`Financial Connections only, with no manual entry + microdeposit fallback`microdeposits`Manual entry and microdeposits onlyThis option is available on the following APIs:

Additional steps might be required for non-hosted integrations. See this section of the ACH guide.

- [PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method_options-us_bank_account-verification_method)
- [SetupIntent](/api/setup_intents/create#create_setup_intent-payment_method_options-us_bank_account-verification_method)
- [CheckoutSession](/api/checkout/sessions/create#create_checkout_session-payment_method_options-us_bank_account-verification_method)
- [Invoice](/api/invoices/create#create_invoice-payment_settings-payment_method_options-us_bank_account-verification_method)
- [Subscription](/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-us_bank_account-verification_method)
- [Payment Element](/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-us_bank_account-verification_method)

[Create a customerRecommended](#customer)We recommend that you create a Customer with an email address to represent your user, that you then attach to your payment. Attaching a Customer object allows you to list previously linked accounts  later. By providing an email address on the Customer object, Financial Connections can improve the authentication flow by streamlining sign-in or sign-up for your user, depending on whether they’re a returning Link user.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}}`[Request access to additional account data](#access)To access additional account data on Financial Connections Accounts, first make sure you’ve submitted your Financial Connections application by checking Financial Connections settings in the Dashboard. To view this page, activate your account. How you configure which types of account data you have access to depends on your integration.

Dynamic payment methodsPayment method typesIf you use Stripe’s dynamic payment method feature to collect ACH payments for non-Connect use cases, you can configure requested Financial Connections data directly from the ACH Dashboard settings page. Account and routing number is always required for ACH debits; other data types are optional.

NoteWe recommend configuring permissions in the Dashboard because it allows you to change which data you collect without any code changes.

To override the Dashboard configuration, specify Financial Connections permissions directly in the API. To do this for PaymentIntents:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=2000 \
  -d currency=usd \
  -d customer={{CUSTOMER_ID}} \
  -d "automatic_payment_methods[enabled]"=true \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=balances \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=transactions`[Use data to optimize ACH integration](#optimize)After you have been approved for additional bank account data access like balances or ownership, you can use this data to optimize ACH payments performance. For example, you can use balance data to reduce the risk of insufficient funds failures. See related data guides for examples:

- [Balances](/financial-connections/balances): check account balance prior to payment initiation to reduceNSFs.
- [Ownership](/financial-connections/ownership): pull account owners and compare against your internal data models to catch potential fraud.
- [Transactions](/financial-connections/transactions): pull an account’s transaction history to check when the customer’s paycheck might land.

### Finding the Financial Connections Account ID

To initiate data refreshes and retrieve data on a Financial Connections Account, you first need to get the account’s ID from the linked Payment Method by expanding the Payment Intent’s payment_method property:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=payment_method`The Financial Connections Account ID is on the expanded Payment Method’s us_bank_account hash. If you allow manual entry fallback and the user manually entered their account information, this field is null.

`{
  "id": "pi_3OK3g4FitzZY8Nvm11121Lhb",
  "object": "payment_intent",
  "payment_method": {
    "us_bank_account": {
      "financial_connections_account": "fca_1OK123bitUAA8SvmruWkck76"
    }
    // ... other fields on the Payment Method
  }
  // ... other fields on the Payment Intent
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Enable Financial Connections](#enable)[Create a customer](#customer)[Request access to additional account data](#access)[Use data to optimize ACH integration](#optimize)Products Used[Financial Connections](/financial-connections)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`