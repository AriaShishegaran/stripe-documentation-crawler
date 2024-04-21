htmlQuery transactional data | Stripe Documentation[Skip to content](#main-content)Query transactional data[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-transactions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-transactions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Query transactional data

Create custom reports for charges, refunds, and more.Use the data in the tables within the schema for reporting on your account’s balance activity. The tables in the Payment Tables sections represent funds that flow between your customers and your Stripe account, such as charges or refunds. The Transfer Tables section has information about transfers of your Stripe account balance to your bank account (payouts).

Use the balance_transactions table as a starting point for accounting purposes. Unlike using separate tables (such as charges or refunds), it provides a ledger-style record of every type of transaction that comes into or flows out of your Stripe account balance. Use balance transactions to generate frequently used reports and to simplify how you report on financial activity. Some common types of balance transactions include:

- `charges`
- `refunds`
- `transfers`
- `payouts`
- `adjustments`
- `application_fees`

Each balance transaction row represents an individual balance_transaction object that doesn’t change after it’s created. For example, creating a charge also creates a corresponding balance transaction of type charge. Refunding this charge creates a separate balance transaction of type refund—but it doesn’t modify the original balance transaction. Similarly, receiving a payout in your bank account (represented as a transfer) creates a balance transaction.

The following example query uses this table to retrieve some information about the five most recent balance transactions.

`select
  date_format(created, '%m-%d-%Y') as day,
  id,
  amount,
  currency,
  source_id,
  type
from balance_transactions
order by day desc
limit 5`dayidamountcurrencysource_idtype4/21/2024txn_8EN65uPSPqxvuNz-1,000usdre_vcxoMPD8crx6ki6refund4/21/2024txn_oWUG8WqDOlAsKEI1,000usdch_KTwr6Kur1TQlucccharge4/21/2024txn_lHmQu2xzHVa630e1,000usdch_vCDhfEIS7V0OOx1charge4/21/2024txn_MjolPMz6tSTN71E1,000eurch_Focky0QUsVA2yvzcharge4/21/2024txn_JTg9rdeHftqnUuS-1,000usdre_TfnQ6jphYnG4zV1refundYou can calculate the most common financial summaries by joining the balance_transactions table with other tables containing the appropriate information. Some of our query templates (such as the daily balance and monthly summary and balance) work by joining this table to others.

![](https://b.stripecdn.com/docs-statics-srv/assets/balance-transactions.f272cb17ff065ae1c02b320a235f0b3e.png)

## Balance transaction fee details

The balance_transaction_fee_details table provides fee information about each individual balance transaction. Joining this table to balance_transactions in the manner below allows you to return fee information for each balance transaction.

![](https://b.stripecdn.com/docs-statics-srv/assets/balance_transaction_fee_details.e8c6bba21d6e26ee77157a3fd6b797be.png)

The following query joins the balance_transactions and balance_transaction_fee_details tables together. Each balance transaction item returned includes the amount, fee, type of fee applied, and a description of the fee.

`select
  date_format(date_trunc('day', balance_transactions.created), '%m-%d-%Y') as day,
  balance_transactions.id,
  balance_transactions.amount,
  balance_transactions.fee,
  balance_transaction_fee_details.type
from balance_transactions
inner join balance_transaction_fee_details
  on balance_transaction_fee_details.balance_transaction_id=balance_transactions.id
order by day desc
limit 5`dayidamountfeetype4/21/2024txn_JnOpvHlMxKvkHKl1,00059stripe_fee4/21/2024txn_N7UIVEbusmsHOnu1,00059stripe_fee4/21/2024txn_FrjMpti3zrhnNEz1,00059stripe_fee4/21/2024txn_0tm2USczuWkWynk1,00059stripe_fee4/21/2024txn_SKYZNW6FMD0018F1,00059stripe_fee## Charges

The charges table contains data about Charge objects. Use this table for queries that focus on charge-specific information rather than for accounting or reconciliatory purposes. It also supplements accounting reports with additional customer data. For example, the payment card breakdown template query uses the charges table to report on the different types of cards your customers have used.

You can join the charges table to a number of others to retrieve more information with your queries.

![](https://b.stripecdn.com/docs-statics-srv/assets/charges.6bba866fbd70648f58b7af6bcf425c3e.png)

The following example uses the charges table to report on failed charges, returning the card brand and a failure code and message.

`select
  date_format(date_trunc('day', created), '%m-%d-%Y') as day,
  id,
  card_brand,
  failure_code,
  failure_message
from charges
  where status = 'failed'
order by day desc
limit 5`dayidcard_brandfailure_codefailure_message4/21/2024ch_YBKuWlmugW7fUidVisacard_declinedYour card was declined.4/21/2024ch_7cxb6lOrLxssJrwMasterCardcard_declinedYour card doesn’t support this type of purchase.4/21/2024ch_rXttVGr6XB7goviVisacard_declinedYour card has insufficient funds.4/21/2024ch_XKINQrH3gre49v1Visacard_declinedYour card was declined.4/21/2024ch_LHp2AWHx12pWx3TMasterCardcard_declinedYour card was declined.## Customers

The customers table contains data about Customer objects (this table isn’t part of the Payment Tables group). Use it if you’re creating charges using customers (for example, with saved payment information). It’s also useful if you’re using subscriptions.

![](https://b.stripecdn.com/docs-statics-srv/assets/customers.44a1f795dc4ca7d4df666617f45855e9.png)

The following example retrieves a list of failed charges, with the ID and email address for each customer.

`select
  date_format(date_trunc('day', charges.created), '%m-%d-%Y') as day,
  customers.id,
  customers.email,
  charges.id
from charges
inner join customers
on customers.id=charges.customer_id
where charges.status = 'failed'
order by day desc
limit 5`## Refunds

Charges and refunds are separate objects within the API. Refunding a charge creates a Refund. This data is available in the refunds table and provides in-depth information about completed refunds. Similar to reporting on charges, a best practice is to start with information about balance transactions. If necessary, you can then gather additional details using the refunds table.

You can join the refunds table to the balance_transactions and charges tables to further explore refund data.

![](https://b.stripecdn.com/docs-statics-srv/assets/refunds.aebf78debf4de6e9ee96a477b23fc198.png)

The following example joins the balance_transactions and refunds tables together using the refunds.balance_transaction_id and balance_transactions.id columns. Each balance transaction item returned is a refund, displaying the charge ID and amount. Only balance transactions created after a certain date are returned.

`select
  date_format(date_trunc('day', balance_transactions.created), '%m-%d-%Y') as day,
  balance_transactions.source_id,
  refunds.charge_id,
  balance_transactions.amount
from balance_transactions
inner join refunds
on refunds.balance_transaction_id=balance_transactions.id
  where balance_transactions.type = 'refund'
order by day desc
limit 5`daysource_idcharge_idamount4/21/2024re_7hk6jGsBIimYbjich_ZjlIUC2GjTA8LWP-1,0004/21/2024re_UBsxEIAd50VKYhach_wVFMdB0BxBoK5tg-1,0004/21/2024re_mVvXkg3R26kxvjcch_hNxp9hBmwTyTqIL-1,0004/21/2024re_4vfjtdrlBbjElHfch_lBeuHHYjigIW1Q3-1,0004/21/2024re_HfTJ8dK5LnqNiXKch_TbwGTa0Jmha5WnF-1,000## Partial capture refunds

Using auth and capture and capturing only some of the authorized amount creates both a charge and a refund. An authorized charge creates a charge and an associated balance transaction for the full amount. After a partial capture is complete, the uncaptured amount is released and a refund is created with a reason field of partial_capture along with an associated balance transaction.

For example, authorizing a 10 USD charge but only capturing 7 USD creates a charge for 10 USD. This also creates a refund with the reason partial_capture for the remaining 3 USD.

Take this into account if your business is performing auth and capture charges as you’re creating reports to review customer refund rates. Without consideration, auth and capture can misrepresent the number of refunds on your account. Use the refund’s reason field to filter out partial capture refunds when retrieving payment information.

`select
  balance_transactions.id,
  balance_transactions.amount
from balance_transactions
inner join refunds
on refunds.id=balance_transactions.source_id
where reason != 'partial_capture'
limit 5`## Transfers and payouts

The transfers table contains data about payouts made from your Stripe balance to your bank account. You can use this table to reconcile each payout with the specific charges, refunds, and adjustments that comprise it, as long as you’re using automatic payouts.

For Connect platforms, this table also includes data about transfers of funds to connected Stripe accounts.

![](https://b.stripecdn.com/docs-statics-srv/assets/transfers.f4311836b58c92e30de891a4d124d402.png)

If you’re performing payouts manually, the amount in each payout to your bank account is arbitrary. As such, you can’t reconcile it to specific balance transactions and it only reflects the amount you requested to pay out to your bank account.

The following example joins the balance_transactions and transfers tables together. It returns a list of charges and refunds, the payout they relate to, and the date that the payout is scheduled to arrive into your bank account.

`select
  date_format(date_trunc('day', balance_transactions.created), '%m-%d-%Y') as bt_created,
  balance_transactions.source_id,
  balance_transactions.type,
  balance_transactions.net as net_amount,
  balance_transactions.automatic_transfer_id as transfer_id,
  date_format(date_trunc('day', transfers.date), '%m-%d-%Y') as transfer_date
from balance_transactions
inner join transfers
on balance_transactions.automatic_transfer_id=transfers.id
where balance_transactions.type = 'charge'
and balance_transactions.type != 'refund'
order by bt_created desc
limit 5`daysource_idtypenet_amounttransfer_idtransfer_date05-22-2017ch_GXWFQzMMbXvVmBrcharge941po_wsbVWosVpp6Pdku05-24-201705-22-2017ch_SDq71yJJKBOSKoicharge941po_UgDH4vZVA5CtdP305-24-201705-21-2017ch_HIDF90JtKO77aYEcharge941po_KUEmCrzNzmXji8U05-23-201705-21-2017ch_gpcXD4NmrhqYykpcharge941po_6eqIAhaPdhUW1Nr05-23-201705-21-2017ch_ucSeHPARuW6pOnScharge941po_xVxQjlyLsFvv5mx05-23-2017CautionPayouts before 04-06-2017 have a TRANSFER_ID with a tr_ prefix.

## Transfer reversals

You can reverse a manually created payout (or transfer to a connected Stripe account) if it hasn’t been paid out yet by using funds returned to the available balance in your account. These are represented as Transfer_reversal objects and reside in the transfer_reversals table.

Transfer reversals only apply to payouts and transfers that have been created manually—you can’t reverse automatic payouts.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Balance transaction fee details](#balance-transaction-fee-details)[Charges](#charges)[Customers](#customers)[Refunds](#refunds)[Partial capture refunds](#partial-capture-refunds)[Transfers and payouts](#transfers-and-payouts)[Transfer reversals](#transfer-reversals)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`