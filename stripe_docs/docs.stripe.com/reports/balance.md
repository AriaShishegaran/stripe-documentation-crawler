# Balance report

The Balance report is similar to a bank statement, helping you to reconcile your Stripe balance at the end of the month. It provides an itemized CSV export of your complete transaction history and any custom metadata associated with those transactions. All transactions are shown in your settlement currency (after any foreign currency conversion).

[Balance report](https://dashboard.stripe.com/reports/balance)

The Balance report is most useful if you treat Stripe like a bank account for accounting purposes, reconciling the balance at the end of each month. If you have automatic payouts enabled and prefer to reconcile the transactions settled in each payout, see the Payout reconciliation report instead. Not sure? Check out our guide to choosing the right report.

[Payout reconciliation](/reports/payout-reconciliation)

[guide](/reports/select-a-report#reconciliation)

To get started, use the controls at the top of the screen to select a date range.

[controls](/reports/options)

The Balance summary section shows your starting and ending Stripe balance for the selected date range, along with a high level summary of your activity during the period. Your balance includes funds that are available, pending, and any reserved funds, if applicable.

The Balance change from activity section provides a more detailed breakdown of your transactions by reporting category. This section includes all transactions except for payouts that affect your balance, including charges, refunds, disputes, other adjustments, and fees.

[reporting category](/reports/reporting-categories)

The Payouts section provides the quantity and total amount of payouts to your bank account during the period. You can download a list of individual payout transactions by clicking the Download button.

## Downloading data

You can download the data displayed in each section of the report as a CSV file by clicking the Download button in the upper right corner of that section. The Balance change from activity and Payouts sections allow you to download multiple types of reports:

- Summary: This downloads data in CSV format exactly as you see it in the dashboard.

- Itemized: This downloads the full list of individual transactions that are summarized in the dashboard. You can include custom metadata associated with those transactions to speed up the reconciliation process.

In addition, you can quickly download itemized data for a single category of transactions by hovering over that category and clicking the Download button that appears.

## Available columns

You can customize the columns that appear in the reports when downloading them in the dashboard or via the Reporting API. The available columns in each type of report are described below.

[Reporting API](/reports/api)

- Balance summary

[Balance summary](#schema-balance-summary-1)

- Balance change from activity summary

[Balance change from activity summary](#schema-balance-change-from-activity-summary-1)

- Itemized balance change from activity

[Itemized balance change from activity](#schema-balance-change-from-activity-itemized-3)

- Payouts summary

[Payouts summary](#schema-payouts-summary-1)

- Itemized payouts

[Itemized payouts](#schema-payouts-itemized-3)

API report type: balance.summary.1

One of starting_balance, ending_balance, activity or payouts.

One of Starting balance (YYYY-MM-DD) - the balance at the start of the period, Activity - the net amount of all transactions that affected your balance except for payouts, Total payouts - the amount of payouts to your bank account, or Ending balance (YYYY-MM-DD) - the balance left over at the end of the period after subtracting payouts from the Starting balance and Activity.

Net amount for the transactions associated with category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Three-letter ISO code for the currency in which net_amount is defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

API report type: balance_change_from_activity.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: balance_change_from_activity.itemized.3

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

Time at which the balance transaction was created. Dates in the requested timezone, or UTC if not provided.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested timezone, or UTC if not provided.

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

Gross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Fees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Net amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

The Stripe object to which this transaction is related.

An arbitrary string attached to the balance transaction. Often useful for displaying to users.

For transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

For transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

[ISO currency code](https://stripe.com/docs/currencies)

​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Name of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

First line of the customer shipping address associated with this charge, if any

Second line of the customer shipping address associated with this charge, if any

City of the customer shipping address associated with this charge, if any

State of the customer shipping address associated with this charge, if any

Postal code of the customer shipping address associated with this charge, if any

Country of the customer shipping address associated with this charge, if any

First line of the customer address associated with this charge, if any

Second line of the customer address associated with this charge, if any

City of the customer address associated with this charge, if any

State of the customer address associated with this charge, if any

Postal code of the customer address associated with this charge, if any

Country of the customer address associated with this charge, if any

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

First line of the card address associated with this charge, if any

Second line of the card address associated with this charge, if any

City of the card address associated with this charge, if any

State of the card address associated with this charge, if any

Postal code of the card address associated with this charge, if any

Country of the card address associated with this charge, if any

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

The unique ID of the related Payment Intent, if any.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

The type of payment method used in the related payment.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

The dynamic statement descriptor or suffix specified when the related charge was created.

Reason given by cardholder for dispute. Read more about dispute reasons.

[dispute reasons](https://stripe.com/docs/disputes/categories)

For Stripe Connect activity related to a connected account, the unique ID for the account.

For Stripe Connect activity related to a connected account, the name of the account.

For Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

(Beta) For Stripe Connect activity related to a connected account, charge id of the direct charge that happened on connected account.

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payouts.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: payouts.itemized.3

The Stripe object to which this transaction is related.

For automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in UTC.

[automatic payouts](https://stripe.com/docs/payouts#payout-schedule)

[manual payouts](https://stripe.com/docs/payouts#manual-payouts)

For automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in the requested timezone, or UTC if not provided.

[automatic payouts](https://stripe.com/docs/payouts#payout-schedule)

[manual payouts](https://stripe.com/docs/payouts#manual-payouts)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

Gross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Fees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Net amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Unique identifier for the balance transaction.

An arbitrary string attached to the balance transaction. Often useful for displaying to users.

Date the payout is scheduled to arrive in the bank. This factors in delays like weekends or bank holidays.

Current status of the payout (paid, pending, in_transit, canceled or failed). A payout will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.

Typically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status. Times in UTC.

Typically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status. Times in the requested timezone, or UTC if not provided.

Can be bank_account or card.

An arbitrary string attached to the payout. Often useful for displaying to users.

ID of the bank account or card the payout was sent to.

​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.
