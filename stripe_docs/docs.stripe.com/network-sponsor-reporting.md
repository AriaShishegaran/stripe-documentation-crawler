# Network Sponsor Reporting

## Stripe Reports

All reports are provided as CSV files over SFTP. The available reports are:

- Daily Settlement Report: a same-day summary report of transaction volume

- Clearing Transaction Detail Report: a daily transaction-level report of cleared transactions

- Dispute Event Report: a daily transaction-level report of events related to disputes

- Transaction Summary Report: a periodic per-merchant summary of processed volume

- Merchant Report: a list of events related to merchant metadata

Filenames are customizable.

CSV files are as described in RFC 4180:

[RFC 4180](https://tools.ietf.org/html/rfc4180)

- Fields are optionally delimited by " quotes.When they are, "" inside is used to represent a single quote and fields can contain commasIn the example below, the first value is "quoted, field"

- When they are, "" inside is used to represent a single quote and fields can contain commas

- In the example below, the first value is "quoted, field"

- Dates will always be in YYYY-MM-DD format and in UTC time.

- Headers will always be present

- Blank fields will either be an empty delimited field ("") or just nothing between commas. Both the example_header and a_date_field values in the second row of the below sample are empty.

Amounts are always:

- provided as an integer

- accompanied by a three-letter currency code

- in the smallest unit for the currency (cents, pence, centavos, etc)

For example 12345,usd is USD $123.45 and 12345,jpy is JPY ¥12345

In the same vein as our API Backwards-Compatibility Guidelines, we consider the following changes to be backwards compatible:

[API Backwards-Compatibility Guidelines](/upgrades#what-changes-does-stripe-consider-to-be-backwards-compatible)

- Adding new rightmost columns to the CSV reports

- Adding new values to type fields

## Daily Settlement Report

Each line of this report is a summary of transactions for one reconciliation window for Visa and Mastercard.

- brand: either visa or mastercard

- network_numeric: for Visa, the BIN; for Mastercard, the ICA.

- settlement_service: an identifier for the settlement service used for the transactionsFor Visa, see the full list of possible values belowFor Mastercard, the identifier from the Settlement Manual is used

- For Visa, see the full list of possible values below

- For Mastercard, the identifier from the Settlement Manual is used

- reconciliation_date: the processing date in YYYY-MM-DD format.

- reconciliation_cycle: which cycle is summarized

- type: which transactions are included in the aggregation. Valid values are:first_presentmentfirst_chargebacksecond_presentmentsecond_chargeback(includes prearbitration withdrawals for Visa)interchange (interchange reimbursement fees)scheme_feemiscellaneous

- first_presentment

- first_chargeback

- second_presentment

- second_chargeback(includes prearbitration withdrawals for Visa)

- interchange (interchange reimbursement fees)

- scheme_fee

- miscellaneous

- amount: the amount as an integer number of minor units, possibly with a leading - to denote a negative amount. Amounts in this report are relative to Stripe, so a positive amount means money flowing to Stripe.

- currency: the three-letter currency code

## Clearing Transaction Detail Report

This report contains records for cleared charges and refunds. It has a number of limitations:

- Some of the listed transactions may later fail in clearing. This means that this report cannot be reconciled against other reports counting successfully settled transactions.

- The clearing date in this report reflects the date the clearing attempt was created internally within Stripe, and may not be the same as the date the transaction is eventually processed.

- The amount is in the presentment currency of the transaction, so cannot be used to reconcile to cash.

- date: the date this transaction was submitted for clearing

- brand: either visa or mastercard

- merchant: the unique identifier assigned by Stripe

- card_number: the first six and last four digits of the card number, separated with an asterisk *

- acquirer_reference_number: the acquirer reference number sent with clearing

- type: the type of transaction. One of:chargerefund

- charge

- refund

- amount: the transaction amount

- currency: the three-letter transaction currency code

- raw__visa_moto: the raw Visa MOTO/ECI value. Only populated for Visa transactions

- raw__mastercard_sli: the raw Mastercard Security Level Indicator value. Only populated for Mastercard transactions

## Dispute Events Report

This report contains records of events related to transaction Disputes.

- date: the date of the incoming record

- brand: either visa or mastercard

- merchant: the unique identifier assigned by Stripe

- card_number: the first six and last four digits of the card number, separated with an asterisk *

- acquirer_reference_number: the acquirer reference number sent with clearing

- type: the type of event. One of:retrievalfirst_chargebackfirst_chargeback_reversalrepresentmentrepresentment_reversalsecond_chargebacksecond_chargeback_reversalprearbitration

- retrieval

- first_chargeback

- first_chargeback_reversal

- representment

- representment_reversal

- second_chargeback

- second_chargeback_reversal

- prearbitration

- amount: the chargeback amount

- currency: the three-letter currency code

- reason_code: the raw Visa or Mastercard reason code

## Transaction Summary Report

This report breaks down transactions by merchant for a given period of time. It is available on a daily, weekly, or monthly basis. Rows are aggregated by:

- Merchant

- Transaction Type

- Presentment Currency

Chargebacks and refunds are counted in the time period that they themselves occur, not the one in which the original transaction did.

- merchant: the unique identifier assigned by Stripe

- range_start: the first date included in this aggregation, in YYYY-MM-DD format

- range_end: the last date included in this aggregation, in YYYY-MM-DD format

- brand: either visa or mastercard

- type: what type of transaction is being aggregatedchargefull_refundpartial_refundchargeback

- charge

- full_refund

- partial_refund

- chargeback

- count: the number of transactions

- amount: the sum of the transaction amounts

- currency: the three-letter currency code of the transaction

## Merchant Report

This report provides information about the merchants transacting on Stripe.

- It can be provided daily, weekly, monthly, or quarterly. Monthly or quarterly reports will be a full copy of the portfolio each time, whereas weekly or daily ones will be just changes.

It can be provided daily, weekly, monthly, or quarterly. Monthly or quarterly reports will be a full copy of the portfolio each time, whereas weekly or daily ones will be just changes.

- The exact selection and ordering of fields in this report can be configured depending on the details of the Network Sponsor’s requirements and the country of operation.

The exact selection and ordering of fields in this report can be configured depending on the details of the Network Sponsor’s requirements and the country of operation.

- Merchants are included in this report when they have settled three live transactions.

Merchants are included in this report when they have settled three live transactions.

- report_date: the date of the report and event, in YYYY-MM-DD format

- event: what happened to this merchant?onboarded: this is a new merchantupdated: the merchant has updated information. When a merchant is updated, the row for them in this report will still include all of their information.offboarded: the merchant is no longer processing with Stripe

- onboarded: this is a new merchant

- updated: the merchant has updated information. When a merchant is updated, the row for them in this report will still include all of their information.

- offboarded: the merchant is no longer processing with Stripe

- merchant: the unique identifier assigned by Stripe

- business_dba: the merchant’s business name

- business_type: the merchant’s business type

- tax_id: a tax identification number for this merchant. It will be blank if it does not apply

- address_line1: merchant’s address line 1

- address_line2: merchant’s address line 2

- city: merchant city

- region: merchant region, meaning depends on country

- postal_code: merchant postal code, meaning depends on country, might be blank

- country: merchant country

- representative_first_name: the first name of the merchant’s legal representative

- representative_last_name: the first name of the merchant’s legal representative

- representative_dob: the Date of Birth for a representative, in YYYY-MM-DD format.

- merchant_url: the merchant’s website

- mcc: the MCC the merchant will be using

- email: the MCC the merchant will be using

- bank_account_last4: the last four digits of the merchant’s attached bank account. Will be blank if the merchant hasn’t yet attached a bank account.
