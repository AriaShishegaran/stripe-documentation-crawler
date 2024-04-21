htmlBalance report | Stripe Documentation[Skip to content](#main-content)Balance[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fbalance)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fbalance)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Basic financial reports](/docs/reports)[Select a report](/docs/reports/select-a-report)# Balance report

Reconcile your Stripe balance and download your categorized transaction history.The Balance report is similar to a bank statement, helping you to reconcile your Stripe balance at the end of the month. It provides an itemized CSV export of your complete transaction history and any custom metadata associated with those transactions. All transactions are shown in your settlement currency (after any foreign currency conversion).

The Balance report is most useful if you treat Stripe like a bank account for accounting purposes, reconciling the balance at the end of each month. If you have automatic payouts enabled and prefer to reconcile the transactions settled in each payout, see the Payout reconciliation report instead. Not sure? Check out our guide to choosing the right report.

To get started, use the controls at the top of the screen to select a date range.

The Balance summary section shows your starting and ending Stripe balance for the selected date range, along with a high level summary of your activity during the period. Your balance includes funds that are available, pending, and any reserved funds, if applicable.

The Balance change from activity section provides a more detailed breakdown of your transactions by reporting category. This section includes all transactions except for payouts that affect your balance, including charges, refunds, disputes, other adjustments, and fees.

The Payouts section provides the quantity and total amount of payouts to your bank account during the period. You can download a list of individual payout transactions by clicking the Download button.

## Downloading data

You can download the data displayed in each section of the report as a CSV file by clicking the Download button in the upper right corner of that section. The Balance change from activity and Payouts sections allow you to download multiple types of reports:

- Summary: This downloads data in CSV format exactly as you see it in the dashboard.
- Itemized: This downloads the full list of individual transactions that are summarized in the dashboard. You can include custom metadata associated with those transactions to speed up the reconciliation process.

In addition, you can quickly download itemized data for a single category of transactions by hovering over that category and clicking the Download button that appears.

## Available columns

You can customize the columns that appear in the reports when downloading them in the dashboard or via the Reporting API. The available columns in each type of report are described below.

- [Balance summary](#schema-balance-summary-1)
- [Balance change from activity summary](#schema-balance-change-from-activity-summary-1)
- [Itemized balance change from activity](#schema-balance-change-from-activity-itemized-3)
- [Payouts summary](#schema-payouts-summary-1)
- [Itemized payouts](#schema-payouts-itemized-3)

### Balance summary

API report type: balance.summary.1

Column nameDefaultDescriptioncategoryOne of starting_balance, ending_balance, activity or payouts.

descriptionOne of Starting balance (YYYY-MM-DD) - the balance at the start of the period, Activity - the net amount of all transactions that affected your balance except for payouts, Total payouts - the amount of payouts to your bank account, or Ending balance (YYYY-MM-DD) - the balance left over at the end of the period after subtracting payouts from the Starting balance and Activity.

net_amountNet amount for the transactions associated with category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

currencyThree-letter ISO code for the currency in which net_amount is defined.

### Balance change from activity summary

API report type: balance_change_from_activity.summary.1

Column nameDefaultDescriptionreporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

countThe number of transactions associated with the reporting_category.

grossSum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeSum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netSum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

### Itemized balance change from activity

API report type: balance_change_from_activity.itemized.3

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

connected_account_idFor Stripe Connect activity related to a connected account, the unique ID for the account.

connected_account_nameFor Stripe Connect activity related to a connected account, the name of the account.

connected_account_countryFor Stripe Connect activity related to a connected account, the two-letter ISO code representing the country of the account.

connected_account_direct_charge_id(Beta) For Stripe Connect activity related to a connected account, charge id of the direct charge that happened on connected account.

payment_metadata[key]Metadata associated with the related PaymentIntent, if any. If no PaymentIntent metadata exists, metadata from any related charge object will be returned. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

refund_metadata[key]Metadata associated with the related refund object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

transfer_metadata[key]Metadata associated with the related transfer object, if any. API requests including this column must specify a metadata key in brackets. This column can be specified multiple times to retrieve data from additional metadata keys.

### Payouts summary

API report type: payouts.summary.1

Column nameDefaultDescriptionreporting_categoryReporting Category is a new categorization of balance transactions, meant to improve on the current type field.

currencyThree-letter ISO code for the currency in which gross, fee and net are defined.

countThe number of transactions associated with the reporting_category.

grossSum of the gross amounts of the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

feeSum of the fees paid for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

netSum of the net amounts for the transactions associated with the reporting_category. Expressed in major units of the currency (e.g. dollars for USD, yen for JPY).

### Itemized payouts

API report type: payouts.itemized.3

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

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Downloading data](#downloading-data)[Available columns](#available-columns)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`