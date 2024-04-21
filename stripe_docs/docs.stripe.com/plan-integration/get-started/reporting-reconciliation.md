# Reporting and reconciliation

Learn about the different payout types, balance transactions, and the advanced reporting features within the Sigma platform.

## Reporting and payouts

To simplify reporting and reconciliation, use automatic payouts, because they maintain the association between each transaction and the payout they’re included in.

[payouts](/payouts)

If you’re building custom reporting using the APIs, use the balance transaction endpoint and the payout parameter to list all transactions included in an automatic payout. A best practice is to retrieve payouts automatically and asynchronously when the payout.paid or payout.reconciliation_completed event is received by your webhook handler.

[balance transaction endpoint](/api/balance_transactions/list)

[payout.paid](/api#event_types-payout.paid)

[payout.reconciliation_completed](/api/events/types#event_types-payout.reconciliation_completed)

[webhook](/connect/webhooks)

The number of balance transactions can exceed the maximum limit. In that case, we recommend using the auto pagination feature to fetch the list of all balance transactions without having to manually paginate results and perform subsequent requests.

[auto pagination feature](/api/pagination/auto)

Here’s an example balance history API call to retrieve transactions from a payout:

Automatic payouts supports Instant Payouts that instantly send funds to a supported debit card. You can request Instant Payouts 24/7, including weekends and holidays, and funds typically appear in the associated bank account within 30 minutes. See the Instant Payout documentation to see if it is available in your region.

[Instant Payouts](/payouts#instant-payouts)

[Instant Payout documentation](/payouts/instant-payouts-banks)

You can use manual payouts if desired. However, Stripe does not support transaction-level reporting for the funds that comprise your manual payouts because you specify the amount you want to get paid out.

[manual payouts](/connect/payouts-connected-accounts)

Here’s an example manual payout on your account:

## Financial Reports

Stripe supports many out-of-the-box reports for financial analysis:

[reports](/reports)

- 

- Balance: You can view and download summarized and itemized balance transaction data, helping you to close books on a daily, weekly, or monthly basis. These reports help you understand changes to your Stripe balance.

[Balance](/reports/balance)

- Reconciliation: You can see which transactions have already been paid out and which ones are yet to be paid out using this report. The Reconciliation tab displays the same type of data you see in the Balance tab but grouped in different ways to help you reconcile payouts.

[Reconciliation](/reports/payout-reconciliation)

All reports are available in the Stripe Dashboard, and with the API. You can programmatically request and download any of Stripe’s prebuilt reports using the Reporting API.

[Reporting API](/reports/api)

To fully automate this process, follow our four-step integration pattern, which includes listening for events that tell you when new reporting data becomes available and running your reports at that time.

[four-step integration pattern](/reports/api#integration-pattern)

Here’s an example API call to generate a “Itemized payout reconciliation report for a single payout” (aka “Settlement file”). Make this API call after you’ve been notified that new data is available:

## Balance transactions

Balance transactions are the building blocks of all activity on Stripe. These objects:

[Balance transactions](/reports/balance-transaction-types)

- Represent everything that affected your Stripe balance (credits and debits).

- Are automatically created by Stripe (for example, each successful PaymentIntent generates a separate BalanceTransaction object, as does each payout).

- Are immutable (a refund is associated with a new BalanceTransaction negating the original).

- Can act as your ledger (to understand your balance at any point in time, you can replay all BalanceTransactions up to that point).

BalanceTransactions (txn_*** objects) are also the basis of all of our reporting—in most reports, the line-level data point is a txn_*** object.

## Advanced reporting with Sigma

Sigma makes all of your business data available in an interactive SQL environment in the Dashboard. You can write queries that leverage its extensive schema, allowing you to create fully customized reports using information about your transactions.

[Sigma](/stripe-data)

With Sigma, you have the ability to export data directly to CSV, and schedule queries to deliver results by email or webhook. You can generate datasets for your business intelligence tools, reconcile transactional data, and generate custom reports.

[webhook](/webhooks)

To activate Sigma, navigate to Settings > Sigma from the Dashboard. After you activate it, data takes up to 24 hours to load and be queryable. Sigma uses standard ANSI SQL and a broad range of reporting functions. Anyone on your account with permission to view reports can write and run queries.

[activate Sigma](https://dashboard.stripe.com/test/get-started/sigma)