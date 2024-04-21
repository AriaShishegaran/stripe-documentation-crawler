# Payout reconciliation report type

The Payout reconciliation report returns data related to the payouts your receive in your bank account to help you match them to the transactions they relate to. Run this report to use the returned data in your API calls. You can also download the CSV from the Payment fees report in the Dashboard.

[Payment fees report](https://dashboard.stripe.com/reports/reconciliation)

The following tables define the required and optional parameters to run the report, as well as the schema of the CSV output.

[Columns](#schema-ending-balance-reconciliation-itemized-1)

- interval_end

- currency

- reporting_category

- columns

[Columns](#schema-ending-balance-reconciliation-itemized-2)

- interval_end

- currency

- reporting_category

- columns

[Columns](#schema-ending-balance-reconciliation-itemized-3)

- interval_end

- currency

- reporting_category

- timezone

- columns

[Columns](#schema-ending-balance-reconciliation-itemized-4)

- interval_end

- currency

- reporting_category

- timezone

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-itemized-5)

- interval_start

- interval_end

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-by-id-itemized-1)

- payout

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-by-id-itemized-2)

- payout

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-by-id-itemized-3)

- payout

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-by-id-itemized-4)

- payout

- reporting_category

- timezone

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-by-id-summary-1)

- payout

- columns

[Columns](#schema-ending-balance-reconciliation-summary-1)

- interval_end

- currency

- columns

[Columns](#schema-payout-reconciliation-itemized-1)

- interval_start

- interval_end

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-itemized-2)

- interval_start

- interval_end

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-itemized-3)

- interval_start

- interval_end

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-itemized-4)

- interval_start

- interval_end

- timezone

- currency

- reporting_category

- decimal_separator

- columns

[Columns](#schema-payout-reconciliation-summary-1)

- interval_start

- interval_end

- currency

- columns

API report type: ending_balance_reconciliation.itemized.1

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

First line of the shipping address associated with this charge, if any

Second line of the shipping address associated with this charge, if any

City of the shipping address associated with this charge, if any

State of the shipping address associated with this charge, if any

Postal code of the shipping address associated with this charge, if any

Country of the shipping address associated with this charge, if any

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

API report type: ending_balance_reconciliation.itemized.2

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

API report type: ending_balance_reconciliation.itemized.3

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

For Stripe Connect activity related to a connected account, the unique ID for the account.

For Stripe Connect activity related to a connected account, the name of the account.

For Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

API report type: ending_balance_reconciliation.itemized.4

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

For Stripe Connect activity related to a connected account, the unique ID for the account.

For Stripe Connect activity related to a connected account, the name of the account.

For Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

(Beta) For Stripe Connect activity related to a connected account, charge id of the direct charge that happened on connected account.

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payout_reconciliation.itemized.5

ID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

[automatic payout schedule](https://stripe.com/docs/payouts#payout-schedule)

The date we expect this automatic payout to arrive in your bank account, in the requested time zone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

[automatic payout](https://stripe.com/docs/payouts#payout-schedule)

Unique identifier for the balance transaction.

Time at which the balance transaction was created. Dates in UTC.

Time at which the balance transaction was created. Dates in the requested time zone, or UTC if not provided.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

The date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested time zone, or UTC if not provided.

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

Creation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested time zone, or UTC if not provided.

Unique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

Unique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

Unique ID for the order associated with this balance transaction.

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

Destination payment id in the case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payout_reconciliation.by_id.itemized.1

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

Destination payment id in the case of Separate Charges & Transfers and destination charges

API report type: payout_reconciliation.by_id.itemized.2

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

Destination payment id in the case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payout_reconciliation.by_id.itemized.3

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

For Stripe Connect activity related to a connected account, the unique ID for the account.

For Stripe Connect activity related to a connected account, the name of the account.

For Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

(Beta) For Stripe Connect activity related to a connected account, charge id of the direct charge that happened on connected account.

Destination payment id in the case of Separate Charges & Transfers and destination charges

API report type: payout_reconciliation.by_id.itemized.4

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

For Stripe Connect activity related to a connected account, the unique ID for the account.

For Stripe Connect activity related to a connected account, the name of the account.

For Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

(Beta) For Stripe Connect activity related to a connected account, charge id of the direct charge that happened on connected account.

Destination payment id in the case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payout_reconciliation.by_id.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: ending_balance_reconciliation.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

API report type: payout_reconciliation.itemized.1

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

Destination payment id in the case of Separate Charges & Transfers and destination charges

API report type: payout_reconciliation.itemized.2

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

Destination payment id in the case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payout_reconciliation.itemized.3

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

Unique ID for the order associated with this balance transaction.

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

Destination payment id in the case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payout_reconciliation.itemized.4

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

For Stripe Connect activity related to a connected account, the unique ID for the account.

For Stripe Connect activity related to a connected account, the name of the account.

For Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

Destination payment id in the case of Separate Charges & Transfers and destination charges

Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

API report type: payout_reconciliation.summary.1

Reporting Category is a new categorization of balance transactions, meant to improve on the current type field.

[Reporting Category](https://stripe.com/docs/reporting/reporting-categories)

Three-letter ISO code for the currency in which gross, fee and net are defined.

[ISO code for the currency](https://stripe.com/docs/currencies)

The number of transactions associated with the reporting_category.

Sum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

Sum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

## See also

- Payout reconciliation report overview

[Payout reconciliation report overview](/reports/payout-reconciliation)
