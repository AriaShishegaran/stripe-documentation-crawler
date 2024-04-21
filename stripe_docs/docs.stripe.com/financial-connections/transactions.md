# Access transactions for a Financial Connections account

The Financial Connections API allows you to retrieve transactions on a Financial Connections Account. Use transaction data to build a variety of products and solutions, such as:

[Financial Connections Account](/api/financial_connections/accounts/object)

- Expedite the underwriting process and improve access to credit and other financial services for your users.

- Mitigate fraud and reduce risk during user onboarding by evaluating a user’s transaction history, and understanding cash inflows and outflows from their financial accounts.

- Help your users track expenses, handle bills, and manage their finances.

## Before you begin

You must have a completed Financial Connections registration to access transactions in live mode. Check your Dashboard settings to check the state of your registration or begin the registration process. Test mode Financial Connections data is always available.

[Dashboard settings](https://dashboard.stripe.com/settings/financial-connections)

[Create a customerRecommendedServer-side](#customer)

## Create a customerRecommendedServer-side

We recommend that you create a Customer with an email address to represent your user, that you then attach to your payment. Attaching a Customer object allows you to list previously linked accounts  later. By providing an email address on the Customer object, Financial Connections can improve the authentication flow by streamlining sign-in or sign-up for your user, depending on whether they’re a returning Link user.

[Customer](/api/customers)

[list previously linked accounts](/api/financial_connections/accounts/list)

[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)

[Request access to an account's transactionsServer-side](#request-access-to-transactions)

## Request access to an account's transactionsServer-side

You must collect an account before you can access its transaction data. To learn more about how to collect Financial Connections Accounts consult the integration guide most relevant to your use case: accept payments, facilitate Connect payouts, or build other-data powered products.

[accept payments](/financial-connections/ach-direct-debit-payments)

[facilitate Connect payouts](/financial-connections/connect-payouts)

[build other-data powered products](/financial-connections/other-data-powered-products)

When collecting an account, you specify the data you need access to with the permissions parameter. The set of requested data permissions are viewable by the user in the authentication flow. Financial Connections Accounts are collectible through various integration paths, and how you specify the parameter varies slightly by API.

[permissions](/financial-connections/fundamentals#data-permissions)

[authentication flow](/financial-connections/fundamentals#authentication-flow)

When using dynamic payment methods for certain payments APIs, you can also configure requested permissions in the Dashboard. Learn how to access additional account data on Financial Connections accounts.

[access additional account data on Financial Connections accounts](/financial-connections/ach-direct-debit-payments?dashboard-or-api=dashboard#access)

[Subscribe to transaction dataServer-side](#subscribe-to-transactions)

## Subscribe to transaction dataServer-side

When you subscribe to an account’s transaction data, Stripe automatically retrieves new transactions in the background every day and notifies you when they’re available. Subscribing to daily updates is the easiest way to keep the account’s transaction data up to date.

To get the Financial Connections Account ID you want to subscribe to transactions for, consult the documentation for our payments integrations or check the guide for Financial Connections Sessions.

[payments integrations](/financial-connections/ach-direct-debit-payments#finding-the-financial-connections-account-id)

[Financial Connections Sessions](/financial-connections/other-data-powered-products?platform=web#collect-an-account)

Subscribe to transaction data by calling the subscribe API:

[subscribe API](/api/financial_connections/accounts/subscribe)

Subscriptions aren’t allowed on inactive accounts.

In addition to activating a subscription to future transaction data, this API call automatically initiates a transaction refresh:

As long as you remain subscribed to transaction data, Stripe initiates a new refresh every day.

All Financial Connections data refreshes are asynchronous. After you initiate a transaction refresh, you must wait for it to complete, then retrieve the resulting transactions.

The transaction_refresh field on a Financial Connections account represents the transaction refresh state. This field remains null until you request the transactions permission and initiate a refresh. After you start a transaction refresh, the state changes to pending, and after completion, it moves to either succeeded or failed. We send the financial_connections.account.refreshed_transactions event when the transaction refresh completes. To determine the success of the refresh, check the transaction_refresh.status field while handling the webhook.

[transaction_refresh](/api/financial_connections/accounts/object#financial_connections_account_object-transaction_refresh)

[financial_connections.account.refreshed_transactions](/api/events/types#event_types-financial_connections.account.refreshed_transactions)

[Retrieve transactionsServer-side](#retrieve-transactions)

## Retrieve transactionsServer-side

After Stripe successfully refreshes transactions on the account, you can retrieve them using the transactions list API:

[transactions list API](/api/financial_connections/transactions/list)

Stripe returns a paginated list of up to the last 180 days of transaction history on an account, depending on the account’s financial institution.

[paginated](/api/pagination)

The status of a transaction is one of pending, posted, or void. Information included in the description field varies, but can include metadata such as the business name.

[status](/api/financial_connections/transactions/object#financial_connections_transaction_object-status)

[description](/api/financial_connections/transactions/object#financial_connections_transaction_object-description)

You might wish to retrieve only new transaction data since your last data pull. For example, some users save previously retrieved transaction data to their database, and subsequently merge new or updated data as it becomes available.

To retrieve only new or updated transaction data since your last refresh, pass the transaction_refresh identifier provided by your last observed financial_connections.account.refreshed_transactions webhook event object to the list API:

[financial_connections.account.refreshed_transactions](/api/events/types#event_types-financial_connections.account.refreshed_transactions)

The following is an example webhook integration that only retrieves and records new or updated transaction data:

[webhook](/webhooks#webhook-endpoint-def)

[OptionalUnsubscribe from transaction data](#unsubscribe-from-transaction-data)

## OptionalUnsubscribe from transaction data

[OptionalRefresh transactions on demand](#refresh-transactions-on-demand)

## OptionalRefresh transactions on demand
