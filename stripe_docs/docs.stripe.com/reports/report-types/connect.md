# Connect report type

Connect platforms can use most financial reports to view the activity in their platform account, or in one or more of their connected accounts. In the Dashboard, the report setting controls which account’s data the report displays. By default, the API returns report data for your platform account activity. To view data for your connected accounts, use the Connect-specific report types listed below.

[Connect](/connect)

[report setting](/reports/options)

The following tables define the required and optional parameters to run the report, as well as the schema of the CSV output.

[Columns](#schema-connected-account-balance-change-from-activity-itemized-1)

- interval_start

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-balance-change-from-activity-itemized-2)

- interval_start

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-balance-change-from-activity-itemized-3)

- interval_start

- interval_end

- connected_account

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-balance-change-from-activity-summary-1)

- interval_start

- interval_end

- currency

- connected_account

- columns

[Columns](#schema-connected-account-payouts-itemized-1)

- interval_start

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payouts-itemized-2)

- interval_start

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payouts-itemized-3)

- interval_start

- interval_end

- connected_account

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payouts-summary-1)

- interval_start

- interval_end

- currency

- connected_account

- columns

[Columns](#schema-connected-account-balance-summary-1)

- interval_start

- interval_end

- timezone

- currency

- connected_account

- columns

[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-1)

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-2)

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-3)

- interval_end

- connected_account

- currency

- reporting_category

- timezone

- decimal_separator

- columns

[Columns](#schema-connected-account-ending-balance-reconciliation-summary-1)

- interval_end

- connected_account

- currency

- columns

[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-1)

- connected_account

- payout

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-2)

- connected_account

- payout

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-3)

- connected_account

- payout

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-4)

- connected_account

- payout

- timezone

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-by-id-summary-1)

- connected_account

- payout

- columns

[Columns](#schema-connected-account-payout-reconciliation-itemized-1)

- interval_start

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-itemized-2)

- interval_start

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-itemized-3)

- interval_start

- interval_end

- connected_account

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-itemized-4)

- interval_start

- interval_end

- connected_account

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-summary-1)

- interval_start

- interval_end

- currency

- connected_account

- columns

[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-4)

- interval_end

- connected_account

- currency

- reporting_category

- timezone

- decimal_separator

- columns

[Columns](#schema-connected-account-payout-reconciliation-itemized-5)

- interval_start

- interval_end

- connected_account

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-connect-negative-balance-refunds-disputes-overview-1)

- interval_end

API report type: connected_account_balance_change_from_activity.itemized.1

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Name of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

The unique ID of the related Payment Intent, if any.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

The type of payment method used in the related payment.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

The dynamic statement descriptor or suffix specified when the related charge was created.

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_balance_change_from_activity.itemized.2

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

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

Unique identifier for the Stripe account associated with this line.

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: connected_account_balance_change_from_activity.itemized.3

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

Unique identifier for the Stripe account associated with this line.

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: connected_account_balance_change_from_activity.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: connected_account_payouts.itemized.1

The Stripe object to which this transaction is related.

For automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in UTC.

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

Date the payout is scheduled to arrive in the bank. This factors in delays like weekends or bank holidays. Dates in UTC.

Current status of the payout (paid, pending, in_transit, canceled or failed). A payout will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.

Typically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status.

Can be bank_account or card.

An arbitrary string attached to the payout. Often useful for displaying to users.

ID of the bank account or card the payout was sent to.

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_payouts.itemized.2

The Stripe object to which this transaction is related.

For automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in UTC.

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

Date the payout is scheduled to arrive in the bank. This factors in delays like weekends or bank holidays. Dates in UTC.

Current status of the payout (paid, pending, in_transit, canceled or failed). A payout will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.

Typically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status.

Can be bank_account or card.

An arbitrary string attached to the payout. Often useful for displaying to users.

ID of the bank account or card the payout was sent to.

​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_payouts.itemized.3

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

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_payouts.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: connected_account_balance.summary.1

One of starting_balance, ending_balance, activity or payouts.

One of Starting balance (YYYY-MM-DD) - the balance at the start of the period, Activity - the net amount of all transactions that affected your balance except for payouts, Total payouts - the amount of payouts to your bank account, or Ending balance (YYYY-MM-DD) - the balance left over at the end of the period after subtracting payouts from the Starting balance and Activity.

Net amount for the transactions associated with category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Three-letter ISO code for the currency in which net_amount is defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

API report type: connected_account_ending_balance_reconciliation.itemized.1

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Name of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

The unique ID of the related Payment Intent, if any.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

The type of payment method used in the related payment.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

The dynamic statement descriptor or suffix specified when the related charge was created.

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_ending_balance_reconciliation.itemized.2

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

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

Unique identifier for the Stripe account associated with this line.

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: connected_account_ending_balance_reconciliation.itemized.3

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

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

The unique ID of the related Payment Intent, if any.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

The type of payment method used in the related payment.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

The dynamic statement descriptor or suffix specified when the related charge was created.

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_ending_balance_reconciliation.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: connected_account_payout_reconciliation.by_id.itemized.1

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

The source transaction id in case of Separate Charges & Transfers and destination charges

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_payout_reconciliation.by_id.itemized.2

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

The source transaction id in case of Separate Charges & Transfers and destination charges

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_payout_reconciliation.by_id.itemized.3

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Name of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

The unique ID of the related Payment Intent, if any.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

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

The source transaction id in case of Separate Charges & Transfers and destination charges

Unique identifier for the Stripe account associated with this line.

API report type: connected_account_payout_reconciliation.by_id.itemized.4

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

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

The unique ID of the related Payment Intent, if any.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

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

Unique identifier for the Stripe account associated with this line.

The source transaction id in case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: connected_account_payout_reconciliation.by_id.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: connected_account_payout_reconciliation.itemized.1

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

Unique identifier for the Stripe account associated with this line.

The source transaction id in case of Separate Charges & Transfers and destination charges

API report type: connected_account_payout_reconciliation.itemized.2

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

The unique ID of the related customer, if any.

Email address of the customer, if any, associated with this balance transaction.

Description provided when creating the customer, often used to store the customer name.

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

Unique identifier for the Stripe account associated with this line.

The source transaction id in case of Separate Charges & Transfers and destination charges

API report type: connected_account_payout_reconciliation.itemized.3

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

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

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

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

Unique identifier for the Stripe account associated with this line.

The source transaction id in case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: connected_account_payout_reconciliation.itemized.4

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

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

Unique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

The unique ID of the related Payment Intent, if any.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

The type of payment method used in the related payment.

Whether or not the payment was made using Link.

Card brand, if applicable.

[Card brand](https://stripe.com/docs/api#card_object-brand)

Card funding type, if applicable.

[funding type](https://stripe.com/docs/api#account_card_object-funding)

Two-letter ISO code representing the country of the card.

The dynamic statement descriptor or suffix specified when the related charge was created.

Unique identifier for the Stripe account associated with this line.

The source transaction id in case of Separate Charges & Transfers and destination charges

API report type: connected_account_payout_reconciliation.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: connected_account_ending_balance_reconciliation.itemized.4

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

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

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

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

Unique identifier for the Stripe account associated with this line.

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: connected_account_payout_reconciliation.itemized.5

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

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

The date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

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

Unique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

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

Unique identifier for the Stripe account associated with this line.

The source transaction id in case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: connect.negative_balance_refunds_disputes_overview.1

The ID of the connected account.

The business name of the connected account.

Two-letter ISO code representing the account’s country.

Three-letter ISO code for the currency in which the balance, refunded amount, and disputed amount are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The balance of the connected account, including both available and pending funds.

The sum of debits that are currently pending or in transit on the connected account.

[debits](https://stripe.com/docs/connect/account-balances#accounting-for-negative-balances)

The balance, excluding pending debits.

[pending debits](https://stripe.com/docs/connect/account-balances#accounting-for-negative-balances)

The 24 hour net change in balance for the connected account.

The total amount refunded in the past 7 days related to the connected account.

The total amount refunded in the past 7 days prior to the most recent 7 days related to the connected account.

The percent change in refunds in the past 7 days compared to the preceding period.

The total amount disputed in the past 7 days related to the connected account.

The total amount disputed in the past 7 days prior to the most recent 7 days related to the connected account.

The percent change in disputes in the past 7 days compared to the preceding period.

Whether the account has had their balance go negative in the past 24 hours.

Whether the account has been tagged as having high disputes.

Whether the account has been tagged as having high refunds.
