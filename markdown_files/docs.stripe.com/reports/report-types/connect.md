htmlConnect report type | Stripe Documentation[Skip to content](#main-content)Connect report type[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Freport-types%2Fconnect)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Freport-types%2Fconnect)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Basic financial reports](/docs/reports)[Reports API](/docs/reports/api)# Connect report type

Retrieve financial reports for your connected accounts using the API.Connect platforms can use most financial reports to view the activity in their platform account, or in one or more of their connected accounts. In the Dashboard, the report setting controls which account’s data the report displays. By default, the API returns report data for your platform account activity. To view data for your connected accounts, use the Connect-specific report types listed below.

The following tables define the required and optional parameters to run the report, as well as the schema of the CSV output.

Report typeRequired run parametersOptional run parameters`connected_account_balance_change_from_activity.itemized.1`[Columns](#schema-connected-account-balance-change-from-activity-itemized-1)- `interval_start`
- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_balance_change_from_activity.itemized.2`[Columns](#schema-connected-account-balance-change-from-activity-itemized-2)- `interval_start`
- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_balance_change_from_activity.itemized.3`[Columns](#schema-connected-account-balance-change-from-activity-itemized-3)- `interval_start`
- `interval_end`

- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_balance_change_from_activity.summary.1`[Columns](#schema-connected-account-balance-change-from-activity-summary-1)- `interval_start`
- `interval_end`

- `currency`
- `connected_account`
- `columns`

`connected_account_payouts.itemized.1`[Columns](#schema-connected-account-payouts-itemized-1)- `interval_start`
- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payouts.itemized.2`[Columns](#schema-connected-account-payouts-itemized-2)- `interval_start`
- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payouts.itemized.3`[Columns](#schema-connected-account-payouts-itemized-3)- `interval_start`
- `interval_end`

- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payouts.summary.1`[Columns](#schema-connected-account-payouts-summary-1)- `interval_start`
- `interval_end`

- `currency`
- `connected_account`
- `columns`

`connected_account_balance.summary.1`[Columns](#schema-connected-account-balance-summary-1)- `interval_start`
- `interval_end`

- `timezone`
- `currency`
- `connected_account`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.1`[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-1)- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.2`[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-2)- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.3`[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-3)- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `timezone`
- `decimal_separator`
- `columns`

`connected_account_ending_balance_reconciliation.summary.1`[Columns](#schema-connected-account-ending-balance-reconciliation-summary-1)- `interval_end`

- `connected_account`
- `currency`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.1`[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-1)- `connected_account`
- `payout`

- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.2`[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-2)- `connected_account`
- `payout`

- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.3`[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-3)- `connected_account`
- `payout`

- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.itemized.4`[Columns](#schema-connected-account-payout-reconciliation-by-id-itemized-4)- `connected_account`
- `payout`

- `timezone`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.by_id.summary.1`[Columns](#schema-connected-account-payout-reconciliation-by-id-summary-1)- `connected_account`
- `payout`

- `columns`

`connected_account_payout_reconciliation.itemized.1`[Columns](#schema-connected-account-payout-reconciliation-itemized-1)- `interval_start`
- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.2`[Columns](#schema-connected-account-payout-reconciliation-itemized-2)- `interval_start`
- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.3`[Columns](#schema-connected-account-payout-reconciliation-itemized-3)- `interval_start`
- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.4`[Columns](#schema-connected-account-payout-reconciliation-itemized-4)- `interval_start`
- `interval_end`

- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.summary.1`[Columns](#schema-connected-account-payout-reconciliation-summary-1)- `interval_start`
- `interval_end`

- `currency`
- `connected_account`
- `columns`

`connected_account_ending_balance_reconciliation.itemized.4`[Columns](#schema-connected-account-ending-balance-reconciliation-itemized-4)- `interval_end`

- `connected_account`
- `currency`
- `reporting_category`
- `timezone`
- `decimal_separator`
- `columns`

`connected_account_payout_reconciliation.itemized.5`[Columns](#schema-connected-account-payout-reconciliation-itemized-5)- `interval_start`
- `interval_end`

- `connected_account`
- `timezone`
- `currency`
- `reporting_category`
- `decimal_separator`
- `columns`

`connect.negative_balance_refunds_disputes_overview.1`[Columns](#schema-connect-negative-balance-refunds-disputes-overview-1)- `interval_end`


### Connected account itemized balance change from activity

API report type: connected_account_balance_change_from_activity.itemized.1

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account itemized balance change from activity

API report type: connected_account_balance_change_from_activity.itemized.2

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

customer_shipping_address_line1First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_cityCity of the customer shipping address associated with this charge, if any

customer_shipping_address_stateState of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_codePostal code of the customer shipping address associated with this charge, if any

customer_shipping_address_countryCountry of the customer shipping address associated with this charge, if any

customer_address_line1First line of the customer address associated with this charge, if any

customer_address_line2Second line of the customer address associated with this charge, if any

customer_address_cityCity of the customer address associated with this charge, if any

customer_address_stateState of the customer address associated with this charge, if any

customer_address_postal_codePostal code of the customer address associated with this charge, if any

customer_address_countryCountry of the customer address associated with this charge, if any

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

card_address_line1First line of the card address associated with this charge, if any

card_address_line2Second line of the card address associated with this charge, if any

card_address_cityCity of the card address associated with this charge, if any

card_address_stateState of the card address associated with this charge, if any

card_address_postal_codePostal code of the card address associated with this charge, if any

card_address_countryCountry of the card address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

invoice_numberUnique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

connected_accountUnique identifier for the Stripe account associated with this line.

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized balance change from activity

API report type: connected_account_balance_change_from_activity.itemized.3

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

createdTime at which the balance transaction was created. Dates in the requested timezone, or UTC if not provided.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

available_onThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested timezone, or UTC if not provided.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_at_utcThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

customer_shipping_address_line1First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_cityCity of the customer shipping address associated with this charge, if any

customer_shipping_address_stateState of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_codePostal code of the customer shipping address associated with this charge, if any

customer_shipping_address_countryCountry of the customer shipping address associated with this charge, if any

customer_address_line1First line of the customer address associated with this charge, if any

customer_address_line2Second line of the customer address associated with this charge, if any

customer_address_cityCity of the customer address associated with this charge, if any

customer_address_stateState of the customer address associated with this charge, if any

customer_address_postal_codePostal code of the customer address associated with this charge, if any

customer_address_countryCountry of the customer address associated with this charge, if any

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

card_address_line1First line of the card address associated with this charge, if any

card_address_line2Second line of the card address associated with this charge, if any

card_address_cityCity of the card address associated with this charge, if any

card_address_stateState of the card address associated with this charge, if any

card_address_postal_codePostal code of the card address associated with this charge, if any

card_address_countryCountry of the card address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

charge_createdCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

invoice_numberNumber for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

connected_accountUnique identifier for the Stripe account associated with this line.

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Connected account balance change from activity summary

API report type: connected_account_balance_change_from_activity.summary.1

Column nameDefaultDescriptionreporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

countThe number of transactions associated with the reporting_category.

grossSum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeSum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netSum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

### Connected account itemized payouts

API report type: connected_account_payouts.itemized.1

Column nameDefaultDescriptionpayout_idThe Stripe object to which this transaction is related.

effective_at_utcFor automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

balance_transaction_idUnique identifier for the balance transaction.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

payout_expected_arrival_dateDate the payout is scheduled to arrive in the bank. This factors in delays like weekends or bank holidays. Dates in UTC.

payout_statusCurrent status of the payout (paid, pending, in_transit, canceled or failed). A payout will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.

payout_reversed_atTypically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status.

payout_typeCan be bank_account or card.

payout_descriptionAn arbitrary string attached to the payout. Often useful for displaying to users.

payout_destination_idID of the bank account or card the payout was sent to.

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account itemized payouts

API report type: connected_account_payouts.itemized.2

Column nameDefaultDescriptionpayout_idThe Stripe object to which this transaction is related.

effective_at_utcFor automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

balance_transaction_idUnique identifier for the balance transaction.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

payout_expected_arrival_dateDate the payout is scheduled to arrive in the bank. This factors in delays like weekends or bank holidays. Dates in UTC.

payout_statusCurrent status of the payout (paid, pending, in_transit, canceled or failed). A payout will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.

payout_reversed_atTypically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status.

payout_typeCan be bank_account or card.

payout_descriptionAn arbitrary string attached to the payout. Often useful for displaying to users.

payout_destination_idID of the bank account or card the payout was sent to.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account itemized payouts

API report type: connected_account_payouts.itemized.3

Column nameDefaultDescriptionpayout_idThe Stripe object to which this transaction is related.

effective_at_utcFor automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in UTC.

effective_atFor automatic payouts, this is the date we expect funds to arrive in your bank account. For manual payouts, this is the date the payout was initiated. In both cases, it’s the date the paid-out funds are deducted from your Stripe balance. All dates in the requested timezone, or UTC if not provided.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

balance_transaction_idUnique identifier for the balance transaction.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

payout_expected_arrival_dateDate the payout is scheduled to arrive in the bank. This factors in delays like weekends or bank holidays.

payout_statusCurrent status of the payout (paid, pending, in_transit, canceled or failed). A payout will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.

payout_reversed_at_utcTypically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status. Times in UTC.

payout_reversed_atTypically this field will be empty. However, if the payout’s status is canceled or failed, this field will reflect the time at which it entered that status. Times in the requested timezone, or UTC if not provided.

payout_typeCan be bank_account or card.

payout_descriptionAn arbitrary string attached to the payout. Often useful for displaying to users.

payout_destination_idID of the bank account or card the payout was sent to.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account payouts summary

API report type: connected_account_payouts.summary.1

Column nameDefaultDescriptionreporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

countThe number of transactions associated with the reporting_category.

grossSum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeSum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netSum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

### Connected account balance summary

API report type: connected_account_balance.summary.1

Column nameDefaultDescriptioncategoryOne of starting_balance, ending_balance, activity or payouts.

descriptionOne of Starting balance (YYYY-MM-DD) - the balance at the start of the period, Activity - the net amount of all transactions that affected your balance except for payouts, Total payouts - the amount of payouts to your bank account, or Ending balance (YYYY-MM-DD) - the balance left over at the end of the period after subtracting payouts from the Starting balance and Activity.

net_amountNet amount for the transactions associated with category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

currencyThree-letter ISO code for the currency in which net_amount is defined.

### Connected account itemized ending balance reconciliation

API report type: connected_account_ending_balance_reconciliation.itemized.1

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account itemized ending balance reconciliation

API report type: connected_account_ending_balance_reconciliation.itemized.2

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

customer_shipping_address_line1First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_cityCity of the customer shipping address associated with this charge, if any

customer_shipping_address_stateState of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_codePostal code of the customer shipping address associated with this charge, if any

customer_shipping_address_countryCountry of the customer shipping address associated with this charge, if any

customer_address_line1First line of the customer address associated with this charge, if any

customer_address_line2Second line of the customer address associated with this charge, if any

customer_address_cityCity of the customer address associated with this charge, if any

customer_address_stateState of the customer address associated with this charge, if any

customer_address_postal_codePostal code of the customer address associated with this charge, if any

customer_address_countryCountry of the customer address associated with this charge, if any

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

card_address_line1First line of the card address associated with this charge, if any

card_address_line2Second line of the card address associated with this charge, if any

card_address_cityCity of the card address associated with this charge, if any

card_address_stateState of the card address associated with this charge, if any

card_address_postal_codePostal code of the card address associated with this charge, if any

card_address_countryCountry of the card address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

invoice_numberUnique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

connected_accountUnique identifier for the Stripe account associated with this line.

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized ending balance reconciliation

API report type: connected_account_ending_balance_reconciliation.itemized.3

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

createdTime at which the balance transaction was created. Dates in the requested timezone, or UTC if not provided.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

available_onThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested timezone, or UTC if not provided.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_at_utcThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

charge_createdCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account ending balance reconciliation summary

API report type: connected_account_ending_balance_reconciliation.summary.1

Column nameDefaultDescriptionreporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

countThe number of transactions associated with the reporting_category.

grossSum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeSum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netSum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

### Connected account itemized single payout reconciliation

API report type: connected_account_payout_reconciliation.by_id.itemized.1

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account itemized single payout reconciliation

API report type: connected_account_payout_reconciliation.by_id.itemized.2

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account itemized single payout reconciliation

API report type: connected_account_payout_reconciliation.by_id.itemized.3

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

connected_accountUnique identifier for the Stripe account associated with this line.

### Connected account itemized single payout reconciliation

API report type: connected_account_payout_reconciliation.by_id.itemized.4

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

createdTime at which the balance transaction was created. Dates in the requested timezone, or UTC if not provided.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

available_onThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested timezone, or UTC if not provided.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_at_utcThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

charge_createdCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

connected_accountUnique identifier for the Stripe account associated with this line.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Connected account single payout reconciliation summary

API report type: connected_account_payout_reconciliation.by_id.summary.1

Column nameDefaultDescriptionreporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

countThe number of transactions associated with the reporting_category.

grossSum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeSum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netSum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

### Connected account itemized date-ranged payout reconciliation

API report type: connected_account_payout_reconciliation.itemized.1

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

connected_accountUnique identifier for the Stripe account associated with this line.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

### Connected account itemized date-ranged payout reconciliation

API report type: connected_account_payout_reconciliation.itemized.2

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

connected_accountUnique identifier for the Stripe account associated with this line.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

### Connected account itemized date-ranged payout reconciliation

API report type: connected_account_payout_reconciliation.itemized.3

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

customer_shipping_address_line1First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_cityCity of the customer shipping address associated with this charge, if any

customer_shipping_address_stateState of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_codePostal code of the customer shipping address associated with this charge, if any

customer_shipping_address_countryCountry of the customer shipping address associated with this charge, if any

customer_address_line1First line of the customer address associated with this charge, if any

customer_address_line2Second line of the customer address associated with this charge, if any

customer_address_cityCity of the customer address associated with this charge, if any

customer_address_stateState of the customer address associated with this charge, if any

customer_address_postal_codePostal code of the customer address associated with this charge, if any

customer_address_countryCountry of the customer address associated with this charge, if any

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

card_address_line1First line of the card address associated with this charge, if any

card_address_line2Second line of the card address associated with this charge, if any

card_address_cityCity of the card address associated with this charge, if any

card_address_stateState of the card address associated with this charge, if any

card_address_postal_codePostal code of the card address associated with this charge, if any

card_address_countryCountry of the card address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

invoice_numberUnique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

connected_accountUnique identifier for the Stripe account associated with this line.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized date-ranged payout reconciliation

API report type: connected_account_payout_reconciliation.itemized.4

Column nameDefaultDescriptionbalance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

createdTime at which the balance transaction was created. Dates in the requested timezone, or UTC if not provided.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

available_onThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested timezone, or UTC if not provided.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

automatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_at_utcThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

charge_createdCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

connected_accountUnique identifier for the Stripe account associated with this line.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

### Connected account date-ranged payouts reconciliation summary

API report type: connected_account_payout_reconciliation.summary.1

Column nameDefaultDescriptionreporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

countThe number of transactions associated with the reporting_category.

grossSum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeSum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netSum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

### Connected account itemized ending balance reconciliation

API report type: connected_account_ending_balance_reconciliation.itemized.4

Column nameDefaultDescriptionautomatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

balance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

createdTime at which the balance transaction was created. Dates in the requested timezone, or UTC if not provided.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

available_onThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested timezone, or UTC if not provided.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_effective_at_utcThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

customer_shipping_address_line1First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_cityCity of the customer shipping address associated with this charge, if any

customer_shipping_address_stateState of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_codePostal code of the customer shipping address associated with this charge, if any

customer_shipping_address_countryCountry of the customer shipping address associated with this charge, if any

customer_address_line1First line of the customer address associated with this charge, if any

customer_address_line2Second line of the customer address associated with this charge, if any

customer_address_cityCity of the customer address associated with this charge, if any

customer_address_stateState of the customer address associated with this charge, if any

customer_address_postal_codePostal code of the customer address associated with this charge, if any

customer_address_countryCountry of the customer address associated with this charge, if any

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

card_address_line1First line of the card address associated with this charge, if any

card_address_line2Second line of the card address associated with this charge, if any

card_address_cityCity of the card address associated with this charge, if any

card_address_stateState of the card address associated with this charge, if any

card_address_postal_codePostal code of the card address associated with this charge, if any

card_address_countryCountry of the card address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

charge_createdCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

invoice_numberNumber for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

connected_accountUnique identifier for the Stripe account associated with this line.

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Connected account itemized date-ranged payout reconciliation

API report type: connected_account_payout_reconciliation.itemized.5

Column nameDefaultDescriptionautomatic_payout_idID of the automatically created payout associated with this balance transaction (only set if your account is on an automatic payout schedule).

automatic_payout_effective_atThe date we expect this automatic payout to arrive in your bank account, in the requested timezone, or UTC if not provided. This is also when the paid-out funds are deducted from your Stripe balance.

balance_transaction_idUnique identifier for the balance transaction.

created_utcTime at which the balance transaction was created. Dates in UTC.

createdTime at which the balance transaction was created. Dates in the requested timezone, or UTC if not provided.

available_on_utcThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in UTC.

available_onThe date the balance transaction’s net funds will become available in the Stripe balance. Dates in the requested timezone, or UTC if not provided.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

grossGross amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeFees paid for this transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netNet amount of the transaction. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

reporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

source_idThe Stripe object to which this transaction is related.

descriptionAn arbitrary string attached to the balance transaction. Often useful for displaying to users.

customer_facing_amountFor transactions associated with charges, refunds, or disputes, the amount of the original charge, refund, or dispute. If the customer was charged in a different currency than your account’s default, this field will reflect the amount as seen by the customer.

customer_facing_currencyFor transactions associated with charges, refunds, or disputes, the three-letter ISO currency code for customer_facing_amount.

regulatory_tag​​An identifier reflecting the classification of this transaction according to local regulations, if applicable. Accounts with automatic payouts enabled receive a separate payout for each regulatory tag. ​​This column is only populated for Brazilian accounts.

automatic_payout_effective_at_utcThe date we expect this automatic payout to arrive in your bank account, in UTC. This is also when the paid-out funds are deducted from your Stripe balance.

customer_idThe unique ID of the related customer, if any.

customer_emailEmail address of the customer, if any, associated with this balance transaction.

customer_nameName of the customer, if any, associated with this balance transaction.

customer_descriptionDescription provided when creating the customer, often used to store the customer name.

customer_shipping_address_line1First line of the customer shipping address associated with this charge, if any

customer_shipping_address_line2Second line of the customer shipping address associated with this charge, if any

customer_shipping_address_cityCity of the customer shipping address associated with this charge, if any

customer_shipping_address_stateState of the customer shipping address associated with this charge, if any

customer_shipping_address_postal_codePostal code of the customer shipping address associated with this charge, if any

customer_shipping_address_countryCountry of the customer shipping address associated with this charge, if any

customer_address_line1First line of the customer address associated with this charge, if any

customer_address_line2Second line of the customer address associated with this charge, if any

customer_address_cityCity of the customer address associated with this charge, if any

customer_address_stateState of the customer address associated with this charge, if any

customer_address_postal_codePostal code of the customer address associated with this charge, if any

customer_address_countryCountry of the customer address associated with this charge, if any

shipping_address_line1First line of the shipping address associated with this charge, if any

shipping_address_line2Second line of the shipping address associated with this charge, if any

shipping_address_cityCity of the shipping address associated with this charge, if any

shipping_address_stateState of the shipping address associated with this charge, if any

shipping_address_postal_codePostal code of the shipping address associated with this charge, if any

shipping_address_countryCountry of the shipping address associated with this charge, if any

card_address_line1First line of the card address associated with this charge, if any

card_address_line2Second line of the card address associated with this charge, if any

card_address_cityCity of the card address associated with this charge, if any

card_address_stateState of the card address associated with this charge, if any

card_address_postal_codePostal code of the card address associated with this charge, if any

card_address_countryCountry of the card address associated with this charge, if any

charge_idUnique identifier for the original charge associated with this balance transaction. Available for charges, refunds and disputes.

payment_intent_idThe unique ID of the related Payment Intent, if any.

charge_created_utcCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in UTC.

charge_createdCreation time of the original charge associated with this balance transaction. Available for charges, refunds and disputes. For charges that were separately authorized and captured, this is the authorization time.  Dates in the requested timezone, or UTC if not provided.

invoice_idUnique ID for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

invoice_numberUnique Number for the invoice associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing invoice.

subscription_idUnique ID for the subscription associated with this balance transaction. Available for charges, refunds, and disputes made in connection with a Stripe Billing subscription.

payment_method_typeThe type of payment method used in the related payment.

is_linkWhether or not the payment was made using Link.

card_brandCard brand, if applicable.

card_fundingCard funding type, if applicable.

card_countryTwo-letter ISO code representing the country of the card.

statement_descriptorThe dynamic statement descriptor or suffix specified when the related charge was created.

dispute_reasonReason given by cardholder for dispute. Read more about dispute reasons.

connected_accountUnique identifier for the Stripe account associated with this line.

source_transaction_idThe source transaction id in case of Separate Charges & Transfers and destination charges

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Connected accounts with negative balances disputes and refunds

API report type: connect.negative_balance_refunds_disputes_overview.1

Column nameDefaultDescriptionaccount_idThe ID of the connected account.

business_nameThe business name of the connected account.

countryTwo-letter ISO code representing the account’s country.

currencyThree-letter ISO code for the currency in which the balance, refunded amount, and disputed amount are defined.

balanceThe balance of the connected account, including both available and pending funds.

pending_debitsThe sum of debits that are currently pending or in transit on the connected account.

balance_excluding_pending_debitsThe balance, excluding pending debits.

balance_24hr_net_changeThe 24 hour net change in balance for the connected account.

refunded_amount_7dThe total amount refunded in the past 7 days related to the connected account.

refunded_amount_7d_prevThe total amount refunded in the past 7 days prior to the most recent 7 days related to the connected account.

refund_pct_changeThe percent change in refunds in the past 7 days compared to the preceding period.

disputed_amount_7dThe total amount disputed in the past 7 days related to the connected account.

disputed_amount_7d_prevThe total amount disputed in the past 7 days prior to the most recent 7 days related to the connected account.

dispute_pct_changeThe percent change in disputes in the past 7 days compared to the preceding period.

has_24hr_negative_balance_changeWhether the account has had their balance go negative in the past 24 hours.

has_high_disputesWhether the account has been tagged as having high disputes.

has_high_refundsWhether the account has been tagged as having high refunds.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`