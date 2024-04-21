htmlAccess balances for a Financial Connections account | Stripe Documentation[Skip to content](#main-content)Balances[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fbalances)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fbalances)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Access balances for a Financial Connections account

Learn how to access an account's balances with your user's permission.The Financial Connections API allows you to retrieve up-to-date balances of a Financial Connections Account. Balance data is useful for a variety of applications, including reducing the risk of insufficient funds failures for ACH, underwriting, or building financial management tools.

## Before you begin

You must have a completed Financial Connections registration to access balances in live mode. Check your Dashboard settings to check the state of your registration or begin the registration process. Test mode Financial Connections data is always available.

[Create a customerRecommendedServer-side](#customer)We recommend that you create a Customer with an email address to represent your user, that you then attach to your payment. Attaching a Customer object allows you to list previously linked accounts  later. By providing an email address on the Customer object, Financial Connections can improve the authentication flow by streamlining sign-in or sign-up for your user, depending on whether they’re a returning Link user.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}}`[Request access to an account's balancesServer-side](#request-account-balances)You must collect an account before you can access its balance data. To learn more about how to collect Financial Connections Accounts consult the integration guide most relevant to your use case: accept payments, facilitate Connect payouts, or build other-data powered products.

When collecting an account, you specify the data you need access to with the permissions parameter. The set of requested data permissions are viewable by the user in the authentication flow. Financial Connections Accounts are collectible through various integration paths, and how you specify the parameter varies slightly by API.

Payment IntentsSetup IntentsSessionsCheckoutInvoicesSubscriptionsCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=20000 \
  -d currency=usd \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=balances \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method`When using dynamic payment methods for certain payments APIs, you can also configure requested permissions in the Dashboard. Learn how to access additional account data on Financial Connections accounts.

[Initiate a balance refreshServer-side](#initiate-balance-refresh)All Financial Connections data retrievals are asynchronous. You initiate a balance refresh and wait for it to complete, then retrieve the results. You can initiate balance refreshes with the prefetch API parameter or the Refresh API.

### Prefetch balance data

Specify whether you want to prefetch account balances before account collection. This initiates the refresh process as soon as your user connects their account in the authentication flow. Set prefetch when you require balance data for every linked account, to make sure you receive it with minimal delay. An example of this is if you plan to perform balance checks prior to initiating an ACH payment. The prefetch parameter is available on all APIs that support Financial Connections.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=20000 \
  -d currency=usd \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][prefetch][]"=balances \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=balances`### Initiate an on-demand refresh

Use the Refresh API to initiate on-demand balance refreshes after account collection, and fetch balance information for a specific account at your convenience, allowing you to defer the decision until a later time.

Use the Financial Connections account ID to initiate a refresh. If you’re integrating through a payments flow, find the account ID on the associated Payment Method. When using a Financial Connections Session, retrieve it through the session.

Command Line[curl](#)`curl https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}}/refresh \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "features[]"=balance`NoteRefreshes aren’t allowed on inactive accounts.

### Wait for the balance refresh to complete

The balance_refresh field on a Financial Connections account represents the balance refresh state. This field remains null until you request the balances permission and initiate a refresh. After you start a balance refresh, the state changes to pending, and after completion, it moves to either succeeded or failed. We send the financial_connections.account.refreshed_balance event when the balance refresh completes. To determine the success of the refresh, check the balance_refresh.status field while handling the webhook.

After a balance refresh completes, Stripe sets the availability of future refreshes through the balance_refresh.next_refresh_available_at field. Check this field before initiating a new balance refresh to make sure that refreshes are currently available. If you attempt a refresh while the value is null (as is always the case when the refresh is pending or the account is inactive) or the current time is less than the next_refresh_available_at timestamp, the refresh won’t be initiated.

BetaIn the unlikely event that a refresh fails, the error field on the refresh hash is a beta feature that provides the cause of the failure and recommended next steps. If you’d like to use it, email us for access.

[Retrieve an account's balancesServer-side](#retrieve-account-balances)After the balance refresh has completed, retrieve the Financial Connections Account from the body of the financial_connections.account.refreshed_balance event or through the API.

Command Line[curl](#)`curl https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`If the refresh completed successfully, the account object contains balance data.

`{
  "id": "fca_1Jbry3BAjqvGMUSxCDjFsrLU",
  "object": "financial_connections.account",
  "balance": {
    "as_of": 1651516592,
    "cash": {
      "available": {
        "usd": 6000
      }
    },
    "current": {
      "usd": 6000
    },
    "type": "cash"
  },
  "balance_refresh": {
    "last_attempted_at": 1651516582,
    "next_refresh_available_at": 1651516583,
    "status": "succeeded",
  },
  // ... other fields on the Financial Connections Account
}`Balance data details![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The balance hash describes the different types of balances made available by a financial institution.

Balance TypesDescription`current`The`current`balance is the amount of funds that have posted to the account. This amount ignores events that have yet to post to an account such as incoming transfers, outgoing transfers, and other holds. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.`available`The balance object is polymorphic, with types`cash`and`credit`. If the balance has`type: "cash"`, you’ll see a`cash`sub-object with the`available`property, which is the amount of funds available for use, such as any to be transferred or paid out, after considering incoming and outgoing holds.`used`The balance object is polymorphic, with types`cash`and`credit`. If the balance has`type: "credit"`, you’ll see a`credit`sub-object with the`used`property, which is the amount of funds that have been consumed after taking outgoing holds into account. For credit balances,`current`and`used`amounts use the same sign convention used for cash balances: a positive amount means funds owedtothe account holder, a negative amount means funds owedbythe account holder. In most cases a credit balance has negative amounts.The availability of balances varies by underlying financial institution. We return all balance data that we have access to. In rare cases, most often when dealing with smaller financial institutions, Stripe can’t retrieve balance data from a financial institution or partner of any kind, in which case the balance object is null. The balance object is also null if the account has been disconnected. In some instances only a current balance is returned. See our list of supported institutions for data coverage.

For the cash balance type, use the available sub-object to confirm sufficient funds exist prior to initiating an ACH Direct Debit payment. If an available balance is null, you might want to use the current balance to confirm sufficient funds prior to initiating an ACH Direct Debit, but be mindful that this amount ignores events that have yet to post to an account such as incoming transfers, outgoing transfers, and other holds.

The as_of field on a balance is the date and time that the financial institution calculated this balance. This isn’t the same as the date and time of balance data retrieval. For example, certain institutions only update balance data once per day, while others update more frequently.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Create a customer](#customer)[Request access to an account's balances](#request-account-balances)[Initiate a balance refresh](#initiate-balance-refresh)[Retrieve an account's balances](#retrieve-account-balances)Products Used[Financial Connections](/financial-connections)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`