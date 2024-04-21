# Query Stripe fees data

Use the itemized_fees table to get a comprehensive, granular breakdown of every fee charged or deducted from your Stripe balance. For example, if a balance transaction indicates a 2 USD fee for a card payment, you can query this transaction within the itemized_fees table to understand the breakdown. You can also use the table to understand the total fees paid to Stripe in a given period of time.

Here is the list of columns available in the itemized_fees table:

[Charge](/api/charges)

[Refund](/api/refunds)

[Invoice](/api/invoices)

[ISO code for the currency](/currencies)

The following example shows how to extract information about the five most recent fee transactions:

To get a more granular view of your activity, join the itemized_fees table with other tables in the schema . For example, join the balance_transactions table with the itemized_fees table to retrieve fee information for each balance transaction.

Here is an example of how to join these tables together, returning different types of fees applied, and detailed descriptions of the fees:

## Fees paid by connected accounts

If you have a platform account with Stripe Connect, use the connected_account_itemized_fees table to get insight on fees paid by your connected accounts.

Like the itemized_fees table,  the connected_account_itemized_fees table provides a granular record of fee transactions, but from the perspective of your connected accounts. These datasets mostly share common attributes, though the connected_account_itemized_fees dataset has an additional account column. This account column enables platform accounts to track and report on the fees paid by each of their connected accounts.

To identify all fee transactions associated with a specific connected account over a particular time period, use the connected_account_itemized_fees table . Here’s an example of a query that can retrieve the top 10 connected accounts based on the total fees they have paid:

Replace start_date and end_date with the specific dates you want to analyze in the format YYYY-MM-DD. This query sums the total fees paid by each connected account within the specified date range and returns the top 10 accounts with the highest total fees.
