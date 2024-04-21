# How reconciliation worksBeta

Learn how Stripe helps you reconcile the activity on your Stripe account with your transaction data and bank statement.

Stripe uses the following three datasets in the reconciliation process. To match records between two datasets, Stripe relies on a shared reference key present in both datasets.

- Your transaction data: Your internal record of payments, like orders or sales records that reflect the gross amount for every transaction stored in your system. This could be your internal order management system or the list of invoices stored in your ERP for example, which contains information about all receivable expectations. Stripe uses this data to estimate the gross amount expected for each transaction and to create payment expectations. For example, successfully delivered orders create payment expectations. You can use the Stripe Dashboard to manually import this data using CSV files.

- Stripe transaction: Data produced by Stripe as the confirmation of the money movement. This includes any charges, refunds, or payouts processed by Stripe. This data is fetched into the reconciliation workspace every 12 hours.

- Bank statement: Bank account statements that confirm the money movement claimed by Stripe in your bank account. Stripe fetches this data directly from your bank account through Financial Connections on a daily basis. Link your bank account through Financial Connections if you haven’t already.

Stripe reconciliation enables you set up three types of reconciliations using the above datasets:

[Bank reconciliation](#bank-reconciliation)

## Bank reconciliation

Bank reconciliation enables you to reconcile the payouts paid by Stripe with the cash deposited in your bank account. To enable this, Stripe needs access to your bank statement. Stripe can fetch your bank statement directly from your bank account through Stripe Financial Connections. You need to link your bank account through Financial Connections and provide access for Reconciliation to use this information. You could perform this step during the Bank reconciliation sign up process.

[Stripe Financial Connections](/financial-connections)

After you provide access to your bank statement, Stripe automatically reconciles the Stripe payouts with the corresponding deposit in your bank account to determine the amount received and any outstanding balance. You can access the details of each Stripe payout, the bank deposit, and the corresponding reconciliation statuses.

[Transaction reconciliation](#transaction-reconciliation)

## Transaction reconciliation

Transaction reconciliation enables you to reconcile Stripe transactions with your internal records at an individual transaction level. It enables you to track and make sure that your internal records and Stripe transactions match, and identify any gaps between the two on a regular basis and take corrective action.

You can ingest and map transaction data from your internal records to Stripe and automate the reconciliation between the two datasets. Stripe uses common reference keys present in both data sets to connect and reconcile the data. These references could be Stripe generated references like charge_id, or your own references that you pass into Stripe in the form of metadata.

[Combination of transaction and bank reconciliation](#combined-reconciliation)

## Combination of transaction and bank reconciliation

You can use a combination of transaction and bank reconciliation to track the complete lifecycle of a transaction from its origin (within your internal records) to Stripe transactions and your bank statement. The transaction data is reconciled with Stripe transactions on a one-to-one basis, and payouts from Stripe are reconciled with your bank statements. With the reconciled data, you can verify if:

- A transaction that you have initiated has been processed by Stripe accurately.

- If the payout against the same transaction has been received in your bank account.

By setting up this three way reconciliation between your transaction data, Stripe transactions, and your bank statements, you can accurately track information across systems and validate them before updating your books.
