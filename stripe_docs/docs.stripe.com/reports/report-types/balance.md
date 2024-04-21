# Balance report type

The Balance report returns your complete transaction history to help with reconciliation. Run this report to use the returned data in your API calls. You can also download the CSV from the Balance report in the Dashboard.

[Balance report](https://dashboard.stripe.com/reports/balance)

The following tables define the required and optional parameters to run the report, as well as the schema of the CSV output.

[Columns](#schema-balance-change-from-activity-itemized-1)

- interval_start

- interval_end

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-balance-change-from-activity-itemized-2)

- interval_start

- interval_end

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-balance-change-from-activity-itemized-3)

- interval_start

- interval_end

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-balance-change-from-activity-summary-1)

- interval_start

- interval_end

- currency

- columns

[Columns](#schema-payouts-itemized-1)

- interval_start

- interval_end

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payouts-itemized-2)

- interval_start

- interval_end

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payouts-itemized-3)

- interval_start

- interval_end

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payouts-summary-1)

- interval_start

- interval_end

- currency

- columns

[Columns](#schema-balance-summary-1)

- interval_start

- interval_end

- timezone

- currency

- columns

API report type: balance_change_from_activity.itemized.1

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

API report type: balance_change_from_activity.itemized.2

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

For Stripe Connect activity related to a connected account, the unique ID for the account.

For Stripe Connect activity related to a connected account, the name of the account.

For Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

(Beta) For Stripe Connect activity related to a connected account, charge id of the direct charge that happened on connected account.

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

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

API report type: balance_change_from_activity.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: payouts.itemized.1

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

API report type: payouts.itemized.2

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

API report type: payouts.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: balance.summary.1

One of starting_balance, ending_balance, activity or payouts.

One of Starting balance (YYYY-MM-DD) - the balance at the start of the period, Activity - the net amount of all transactions that affected your balance except for payouts, Total payouts - the amount of payouts to your bank account, or Ending balance (YYYY-MM-DD) - the balance left over at the end of the period after subtracting payouts from the Starting balance and Activity.

Net amount for the transactions associated with category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Three-letter ISO code for the currency in which net_amount is defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

## See also

- Balance report overview

[Balance report overview](/reports/balance)
