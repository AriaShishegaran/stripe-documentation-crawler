# Query transactional data

Use the data in the tables within the schema for reporting on your account’s balance activity. The tables in the Payment Tables sections represent funds that flow between your customers and your Stripe account, such as charges or refunds. The Transfer Tables section has information about transfers of your Stripe account balance to your bank account (payouts).

[schema](/stripe-data/write-queries)

[payouts](/payouts)

Use the balance_transactions table as a starting point for accounting purposes. Unlike using separate tables (such as charges or refunds), it provides a ledger-style record of every type of transaction that comes into or flows out of your Stripe account balance. Use balance transactions to generate frequently used reports and to simplify how you report on financial activity. Some common types of balance transactions include:

[type](/api#balance_transaction_object-type)

- charges

- refunds

- transfers

- payouts

- adjustments

- application_fees

Each balance transaction row represents an individual balance_transaction object that doesn’t change after it’s created. For example, creating a charge also creates a corresponding balance transaction of type charge. Refunding this charge creates a separate balance transaction of type refund—but it doesn’t modify the original balance transaction. Similarly, receiving a payout in your bank account (represented as a transfer) creates a balance transaction.

[balance_transaction](/api#balance_transaction_object)

The following example query uses this table to retrieve some information about the five most recent balance transactions.

You can calculate the most common financial summaries by joining the balance_transactions table with other tables containing the appropriate information. Some of our query templates (such as the daily balance and monthly summary and balance) work by joining this table to others.

[daily balance](https://dashboard.stripe.com/sigma/queries/templates/Daily%20balance)

[monthly summary and balance](https://dashboard.stripe.com/sigma/queries/templates/Monthly%20summary%20and%20balance)

## Balance transaction fee details

The balance_transaction_fee_details table provides fee information about each individual balance transaction. Joining this table to balance_transactions in the manner below allows you to return fee information for each balance transaction.

The following query joins the balance_transactions and balance_transaction_fee_details tables together. Each balance transaction item returned includes the amount, fee, type of fee applied, and a description of the fee.

## Charges

The charges table contains data about Charge objects. Use this table for queries that focus on charge-specific information rather than for accounting or reconciliatory purposes. It also supplements accounting reports with additional customer data. For example, the payment card breakdown template query uses the charges table to report on the different types of cards your customers have used.

[Charge](/api#charge_object)

[payment card breakdown](https://dashboard.stripe.com/sigma/queries/templates/Payment%20card%20breakdown)

You can join the charges table to a number of others to retrieve more information with your queries.

The following example uses the charges table to report on failed charges, returning the card brand and a failure code and message.

## Customers

The customers table contains data about Customer objects (this table isn’t part of the Payment Tables group). Use it if you’re creating charges using customers (for example, with saved payment information). It’s also useful if you’re using subscriptions.

[Customer](/api#customers)

[subscriptions](/stripe-data/query-billing-data)

The following example retrieves a list of failed charges, with the ID and email address for each customer.

## Refunds

Charges and refunds are separate objects within the API. Refunding a charge creates a Refund. This data is available in the refunds table and provides in-depth information about completed refunds. Similar to reporting on charges, a best practice is to start with information about balance transactions. If necessary, you can then gather additional details using the refunds table.

[Refund](/api#refund_object)

You can join the refunds table to the balance_transactions and charges tables to further explore refund data.

The following example joins the balance_transactions and refunds tables together using the refunds.balance_transaction_id and balance_transactions.id columns. Each balance transaction item returned is a refund, displaying the charge ID and amount. Only balance transactions created after a certain date are returned.

## Partial capture refunds

Using auth and capture and capturing only some of the authorized amount creates both a charge and a refund. An authorized charge creates a charge and an associated balance transaction for the full amount. After a partial capture is complete, the uncaptured amount is released and a refund is created with a reason field of partial_capture along with an associated balance transaction.

[auth and capture](/charges/placing-a-hold)

For example, authorizing a 10 USD charge but only capturing 7 USD creates a charge for 10 USD. This also creates a refund with the reason partial_capture for the remaining 3 USD.

Take this into account if your business is performing auth and capture charges as you’re creating reports to review customer refund rates. Without consideration, auth and capture can misrepresent the number of refunds on your account. Use the refund’s reason field to filter out partial capture refunds when retrieving payment information.

## Transfers and payouts

The transfers table contains data about payouts made from your Stripe balance to your bank account. You can use this table to reconcile each payout with the specific charges, refunds, and adjustments that comprise it, as long as you’re using automatic payouts.

[payouts](/payouts)

[automatic payouts](/payouts)

For Connect platforms, this table also includes data about transfers of funds to connected Stripe accounts.

[Connect](/connect)

If you’re performing payouts manually, the amount in each payout to your bank account is arbitrary. As such, you can’t reconcile it to specific balance transactions and it only reflects the amount you requested to pay out to your bank account.

The following example joins the balance_transactions and transfers tables together. It returns a list of charges and refunds, the payout they relate to, and the date that the payout is scheduled to arrive into your bank account.

Payouts before 04-06-2017 have a TRANSFER_ID with a tr_ prefix.

## Transfer reversals

You can reverse a manually created payout (or transfer to a connected Stripe account) if it hasn’t been paid out yet by using funds returned to the available balance in your account. These are represented as Transfer_reversal objects and reside in the transfer_reversals table.

[Transfer_reversal](/api#transfer_reversal_object)

Transfer reversals only apply to payouts and transfers that have been created manually—you can’t reverse automatic payouts.
