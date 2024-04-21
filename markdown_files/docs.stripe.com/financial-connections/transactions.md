htmlAccess transactions for a Financial Connections account | Stripe Documentation[Skip to content](#main-content)Transactions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Ftransactions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Ftransactions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Access transactions for a Financial Connections account

Learn how to access an account's transactions with your user's permission.The Financial Connections API allows you to retrieve transactions on a Financial Connections Account. Use transaction data to build a variety of products and solutions, such as:

- Expedite the underwriting process and improve access to credit and other financial services for your users.
- Mitigate fraud and reduce risk during user onboarding by evaluating a user’s transaction history, and understanding cash inflows and outflows from their financial accounts.
- Help your users track expenses, handle bills, and manage their finances.

## Before you begin

You must have a completed Financial Connections registration to access transactions in live mode. Check your Dashboard settings to check the state of your registration or begin the registration process. Test mode Financial Connections data is always available.

[Create a customerRecommendedServer-side](#customer)We recommend that you create a Customer with an email address to represent your user, that you then attach to your payment. Attaching a Customer object allows you to list previously linked accounts  later. By providing an email address on the Customer object, Financial Connections can improve the authentication flow by streamlining sign-in or sign-up for your user, depending on whether they’re a returning Link user.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}}`[Request access to an account's transactionsServer-side](#request-access-to-transactions)You must collect an account before you can access its transaction data. To learn more about how to collect Financial Connections Accounts consult the integration guide most relevant to your use case: accept payments, facilitate Connect payouts, or build other-data powered products.

When collecting an account, you specify the data you need access to with the permissions parameter. The set of requested data permissions are viewable by the user in the authentication flow. Financial Connections Accounts are collectible through various integration paths, and how you specify the parameter varies slightly by API.

Payment IntentsSetup IntentsSessionsCheckoutInvoicesSubscriptionsCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=20000 \
  -d currency=usd \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=us_bank_account \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=transactions \
  -d "payment_method_options[us_bank_account][financial_connections][permissions][]"=payment_method`When using dynamic payment methods for certain payments APIs, you can also configure requested permissions in the Dashboard. Learn how to access additional account data on Financial Connections accounts.

[Subscribe to transaction dataServer-side](#subscribe-to-transactions)When you subscribe to an account’s transaction data, Stripe automatically retrieves new transactions in the background every day and notifies you when they’re available. Subscribing to daily updates is the easiest way to keep the account’s transaction data up to date.

To get the Financial Connections Account ID you want to subscribe to transactions for, consult the documentation for our payments integrations or check the guide for Financial Connections Sessions.

Subscribe to transaction data by calling the subscribe API:

Command Line[curl](#)`curl https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}}/subscribe \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "features[]"=transactions`NoteSubscriptions aren’t allowed on inactive accounts.

In addition to activating a subscription to future transaction data, this API call automatically initiates a transaction refresh:

`{
  "id": "fca_1LDYuMGxLVUXRs6HW0lrat9T",
  "object": "financial_connections.account",
  "display_name": "Savings",
  "institution_name": "Test Bank",
  "status": "active",
  "permissions": ["transactions"],
  "subscriptions": ["transactions"],
  "transaction_refresh": {
    "id": "fctxnref_1aaaxqEitUZY8Svm4QdcWZKt",
    "last_attempted_at": 1706742786,
    "next_refresh_available_at": null,
    "status": "pending"
  }
  // ...
}`As long as you remain subscribed to transaction data, Stripe initiates a new refresh every day.

### Wait for the refresh to complete

All Financial Connections data refreshes are asynchronous. After you initiate a transaction refresh, you must wait for it to complete, then retrieve the resulting transactions.

The transaction_refresh field on a Financial Connections account represents the transaction refresh state. This field remains null until you request the transactions permission and initiate a refresh. After you start a transaction refresh, the state changes to pending, and after completion, it moves to either succeeded or failed. We send the financial_connections.account.refreshed_transactions event when the transaction refresh completes. To determine the success of the refresh, check the transaction_refresh.status field while handling the webhook.

[Retrieve transactionsServer-side](#retrieve-transactions)After Stripe successfully refreshes transactions on the account, you can retrieve them using the transactions list API:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/financial_connections/transactions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{ACCOUNT_ID}}`Stripe returns a paginated list of up to the last 180 days of transaction history on an account, depending on the account’s financial institution.

`{
  "object": "list",
  "data": [
    {
      "id": "fctxn_1LXp9RGxLVUXRs6HtTSVfxse",
      "object": "financial_connections.transaction",
      "account": "fca_1LDYuMGxLVUXRs6HW0lrat9T",
      "amount": -1000,
      "currency": "usd",
      "description": "Rocket Rides",
      "livemode": true,
      "status": "posted",
      "status_transitions": {
        "posted_at": 1651784999,
        "void_at": null
      },
      "transacted_at": 1651784999,
      "transaction_refresh": "fctxnref_1LXp8WGxLVUXRs6Hkc5PNUXf",
      "updated": 1651784999
    },
    {...},
    {...}
  ],
  "has_more": false,
  "url": "/v1/financial_connections/transactions"
}`The status of a transaction is one of pending, posted, or void. Information included in the description field varies, but can include metadata such as the business name.

### Retrieving transactions since last refresh

You might wish to retrieve only new transaction data since your last data pull. For example, some users save previously retrieved transaction data to their database, and subsequently merge new or updated data as it becomes available.

To retrieve only new or updated transaction data since your last refresh, pass the transaction_refresh identifier provided by your last observed financial_connections.account.refreshed_transactions webhook event object to the list API:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/financial_connections/transactions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{ACCOUNT_ID}} \
  -d "transaction_refresh[after]"=fctxnref_1LXp8WGxLVUXRs6Hkc5PNUXf`The following is an example webhook integration that only retrieves and records new or updated transaction data:

[Python](#)`import stripe
from flask import Flask
app = Flask(__name__)

@app.route('/stripe_webhooks', methods=['POST'])
def webhook():
    event = None
    try:
        event = stripe.Event.construct_from(json.loads(request.data), stripe.api_key)
    except ValueError as e:
        # Invalid payload
        raise e

    if event.type == "financial_connections.account.refreshed_transactions":
        account = event.data.object
        sync_transactions(account["id"], account["transaction_refresh"]["id"])

    return jsonify(success=True)


def sync_transactions(account_id, current_refresh):
    # Fetches the last transaction_refresh observed for this account from internal database
    last_observed_transaction_refresh = get_previous_transaction_refresh(key=account_id)

    # Get transactions since the last seen transaction_refresh
    response = stripe.financial_connections.Transaction.list(
        account=account_id,
        transaction_refresh={"after": last_observed_transaction_refresh},
    )

    # We know every transaction is either new or updated because of the `transaction_refresh` filter in the list endpoint
    for transaction in response.data:
        record_transaction(transaction)  # Saves the transaction to the DB

    # Updates the last observed transaction_refresh for this account to the current refresh
    set_previous_transaction_refresh(key=account_id, value=current_refresh)`[OptionalUnsubscribe from transaction data](#unsubscribe-from-transaction-data)[OptionalRefresh transactions on demand](#refresh-transactions-on-demand)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Create a customer](#customer)[Request access to an account's transactions](#request-access-to-transactions)[Subscribe to transaction data](#subscribe-to-transactions)[Retrieve transactions](#retrieve-transactions)Products Used[Financial Connections](/financial-connections)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`