htmlAccess ownership details for a Financial Connections account | Stripe Documentation[Skip to content](#main-content)Ownership[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fownership)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fownership)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Access ownership details for a Financial Connections accountBeta

Learn how to access an account's ownership details with your user's permission.The Financial Connections API allows you to retrieve the ownership details of a Financial Connections account. Ownership data is useful for a variety of applications, including reducing the risk of fraud when onboarding users or underwriting.

## Before you begin

You must have a completed Financial Connections registration to access ownership in live mode. Check your Dashboard settings to check the state of your registration or begin the registration process. Test mode Financial Connections data is always available.

[Create a customerRecommendedServer-side](#customer)We recommend that you create a Customer with an email address to represent your user, that you then attach to your payment. Attaching a Customer object allows you to list previously linked accounts  later. By providing an email address on the Customer object, Financial Connections can improve the authentication flow by streamlining sign-in or sign-up for your user, depending on whether they’re a returning Link user.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}}`[Request access to an account's ownership dataServer-side](#request-account-ownership)You must collect an account before you can access its ownership data. To learn more about how to collect Financial Connections Accounts, read the integration guide most relevant to your use case (for example, accept payments, facilitate Connect payouts, or build other-data powered products).

If you use Connect Onboarding for Custom Accounts to collect Financial Connections Accounts, configure which data you want access to in the Dashboard.

If you use an API integration to collect accounts, specify the data you need access to with the permissions parameter. The set of requested data permissions are viewable by the user in the authentication flow. Financial Connections Accounts are collectible through various integration paths, and how you specify the parameter varies slightly by API.

Setup IntentsPayment IntentsSessionsCheckoutInvoicesSubscriptionsCommand Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method`When using dynamic payment methods for certain payments APIs, you can also configure requested permissions in the Dashboard. Learn how to access additional account data on Financial Connections accounts.

[Initiate an ownership refreshServer-side](#initiate-ownership-refresh)All Financial Connections data retrievals are asynchronous. You initiate an ownership refresh and wait for it to complete, then retrieve the results. You can initiate ownership refreshes with the prefetch API parameter or the Refresh API.

### Prefetch ownership data

Specify whether you want to prefetch account ownership details before account collection. This initiates the refresh process as soon as your user connects their account in the authentication flow. Set prefetch when you require ownership data for every linked account, to make sure you receive it with minimal delay. The prefetch parameter is available on all APIs that support Financial Connections.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][prefetch][]"=ownership \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=ownership`### Initiate an on-demand refresh

Use the Refresh API to initiate on-demand ownership refreshes after account collection, and fetch ownership information for a specific account at your convenience, allowing you to defer the decision until a later time. Although account ownership data can change, it generally doesn’t change as frequently as balance or transaction data.

Use the Financial Connections account ID to initiate a refresh. If you’re integrating through a payments flow, find the account ID on the associated Payment Method. When using a Financial Connections Session, retrieve it through the session.

Command Line[curl](#)`curl https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}}/refresh \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "features[]"=ownership`NoteRefreshes aren’t allowed on inactive accounts.

### Wait for the ownership refresh to complete

The ownership_refresh field on a Financial Connections account represents the ownership refresh state. This field remains null until you request the ownership permission and initiate a refresh. After you start an ownership refresh, the state changes to pending, and after completion, it moves to either succeeded or failed. We send the financial_connections.account.refreshed_ownership event when the ownership refresh completes. To determine the success of the ownership refresh, check the ownership_refresh.status field while handling the webhook.

After an ownership refresh completes, Stripe sets the availability of future refreshes through the ownership_refresh.next_refresh_available_at field. Check this field before initiating a new ownership refresh to make sure that refreshes are currently available. If you attempt a refresh while the value is null (as is always the case when the refresh is pending or the account is inactive) or the current time is less than the next_refresh_available_at timestamp, the refresh won’t be initiated.

BetaIn the unlikely event that a refresh fails, the error field on the refresh hash is a beta feature that provides the cause of the failure and recommended next steps. If you’d like to use it, email us for access.

[Retrieve an account's ownership dataServer-side](#retrieve-account-ownership)After the ownership refresh completes, retrieve the Financial Connections account from the API and expand the ownership field to see ownership details.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=ownership`This returns the Financial Connections account with the ownership field expanded to list the account’s owners:

`{
  "id": "fca_zbyrdjTrwcYZJZc6WBs6GPid",
  "object": "financial_connections.account",
  "ownership": {
    "id": "fcaowns_1MzTG4IG1CZuezXppfPbUpXb",
    "object": "financial_connections.account_ownership",
    "created": 1651784999,
    "owners": {
      "object": "list",
      "data": [
        {
          "name": "Jenny Rosen",
          "email": "jenny.rosen@example.com",
          "phone": "+1 555-555-5555",
          "ownership": "fcaowns_1MzTG4IG1CZuezXppfPbUpXb",
          "raw_address": "510 Townsend San Francisco, CA 94103",
          "refreshed_at": 1651784999
        }
      ],
      "has_more": false,
      "url": "/v1/financial_connections/accounts/fca_zbyrdjTrwcYZJZc6WBs6GPid/owners?ownership=fcaowns_1MzTG4IG1CZuezXppfPbUpXb"
    }
  },
  "ownership_refresh": {
    "status": "succeeded",
    "last_attempted_at": 1651784999,
    "next_refresh_available_at": 1651785000
  },
  // ...
}`Stripe returns the ownership information made available by a financial institution, and the availability of ownership details varies. We return all available fields and owners provided by the bank. Ownership details can include account owner name, address, email, and phone number.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Create a customer](#customer)[Request access to an account's ownership data](#request-account-ownership)[Initiate an ownership refresh](#initiate-ownership-refresh)[Retrieve an account's ownership data](#retrieve-account-ownership)Products Used[Financial Connections](/financial-connections)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`