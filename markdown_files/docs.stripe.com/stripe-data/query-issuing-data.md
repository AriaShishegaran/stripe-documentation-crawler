htmlQuery Issuing data | Stripe Documentation[Skip to content](#main-content)Query Issuing data[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-issuing-data)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-issuing-data)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Query Issuing data

Use Sigma or Data Pipeline to retrieve information about Issuing.The Issuing objects represented within Sigma or Data Pipeline includes Authorizations, Transactions, Cards, and Cardholders. Issuing-specific tables can be found within the Issuing section of the schema.

Issuing data for your connected accounts can be found within tables prefaced with connected_account_, for example,connected_account_issuing_authorizations. More information about using Connect with Sigma or Data Pipeline can be found in the Connect section of the documentation.

## Authorizations

Whenever an issued card is used to make a purchase, an Authorization object is created. Each row within the issuing_authorizations table represents data about this object. The same information can be retrieved through the API and is available in the Stripe Dashboard. Note that the request history field isn’t currently available. Every authorization that has been created on your account is available in Sigma or Data Pipeline.

The card_id column of this table stores the ID of the card used to make the purchase. You can find additional information about the card that initiated the authorization by joining the column with the issuing_cards table.

To access the transactions associated with a particular authorization, you can join the authorization_id column in the issuing_transactions table.

![](https://b.stripecdn.com/docs-statics-srv/assets/issuing-authorization.a2435f764c18d190f70797814eb62878.svg)

The following query computes counts of authorizations grouped by approval status.

`select
  date_trunc('month', created) as month,
  count(case when approved then 1 end) as num_approved_authorizations,
  count(*) as total_num_authorizations
from issuing_authorizations
where date_trunc('month', created) between date_trunc('month', date_add('month', -13, date(data_load_time)))
                                        and date_trunc('month', date_add('month', -1, date(data_load_time)))
group by 1
order by 1 desc, 2
limit 2`monthapprovednum_authorizations2024-04-01false5062024-04-01true10,045## Transactions

An Issuing Transaction object represents any use of an issued card that results in funds entering or leaving your Stripe account, such as a completed purchase or refund. The issuing_transactions table stores information about these objects. You can retrieve the same information through the API, and it’s also available in the Stripe Dashboard.

For additional details about the transaction, such as the fee, you can access the associated balance transaction. You can do this by joining the balance_transaction_id column with the id column of the balance_transactions table. Balance transactions are not Issuing-specific objects. More information about working with balance transactions in Sigma or Data Pipeline can be found in the Transactions section of the documentation.

The authorization_id column allows you to access the Authorization object associated with the Transaction by joining on the id column of the issuing_authorizations table. This can provide additional details about how the transaction was authorized. The authorization_id column on an Issuing transaction can be empty in the event of force capture and for some instances of refunds.

You can also access both the card and cardholder involved in the transaction via the card_id and cardholder_id columns. Information about the card is stored in the issuing_cards table, and information about the cardholder is stored in the issuing_cardholders table. The Card and Cardholder objects can provide additional details about who initiated the transaction.

![](https://b.stripecdn.com/docs-statics-srv/assets/issuing-transaction.64c38a1e0dfaec61d29a8a967a24efc8.svg)

The following query returns information about the three most recent over captures. It joins the issuing_authorizations table to determine if this transaction is an over capture by comparing the amounts of the two objects.

`select
  date_format(it.created, '%Y-%m-%d') as day,
  it.id,
  ia.amount as authorized_amount,
  -1 * it.amount as captured_amount
from issuing_transactions it
join issuing_authorizations ia
on it.authorization_id=ia.id
where
  it.type='capture' and
  -1 * it.amount > ia.amount --- This checks if this transaction was overcaptured
order by day desc
limit 3`dayidauthorized_amountcaptured_amount2024-04-21ipi_d6Af1AYDO1e4Z921501512024-04-21ipi_IN93Z7JSCy1NrQB01,0002024-04-21ipi_t1X5Aul3qgluWoZ14501050One of the benefits of using Sigma or Data Pipeline with Issuing is the ability to aggregate data. The following example joins the balance_transactions table and aggregates each of the types of fees for Issuing transactions by month.

`select
  date_trunc('month', it.created) as month,
  fd.type as fee_type,
  sum(fd.amount) as net_fees,
  sum(it.amount) as net_amount
from issuing_transactions it
inner join balance_transactions bt
on bt.id=it.balance_transaction_id
inner join balance_transaction_fee_details fd
on fd.balance_transaction_id=bt.id
group by 1,2
order by month desc, fee_type`monthfee_typenet_feesnet_amount2024-04-01stripe-fee59010,0002024-05-01stripe-fee591,0002024-06-01stripe-fee59010,000## Cards

The issuing_cards table contains data about an individual Card object. The same information is available through the API and within the Stripe Dashboard. The spending controls field isn’t currently available.

Every issued card has an associated Cardholder, which can be accessed by joining the issuing_cardholders table on the cardholder_id column.

![](https://b.stripecdn.com/docs-statics-srv/assets/issuing-card.bde34e4a064958836ff7c665a3e71814.svg)

## Cardholders

Cardholder data is stored within the issuing_cardholders table. The same information can be retrieved through the API or with the Stripe Dashboard. The spending controls field isn’t currently available.

This table can be joined to other tables to provide information about the entity that initiated a transaction or owns an issued card.

![](https://b.stripecdn.com/docs-statics-srv/assets/issuing-cardholder.ad6a5836bbdf5b37f497cddace2e1e01.svg)

The following example retrieves information about the three most recently created active cardholders.

`select
  date_format(created, '%Y-%m-%d') as day,
  id,
  email,
  type
from issuing_cardholders
where status='active'
limit 3`dayidemailtype2024-04-01ich_X57DwmzrujO4KJKj.smith@example.comindividual2024-04-01ich_V8vVPYlh7mgAdXqentity@example.combusiness_entity2024-04-01ich_8bdWYryDbHMlfugj.doe@example.comindividual### Metadata

Metadata for each Issuing object is stored in a separate table. The names of these tables is the name of the object’s table with the addition of _metadata to the end, for example, issuing_transactions_metadata. The metadata table contains a foreign key to the corresponding object in the primary table that you can use to join the two tables. For example, every row in the issuing_transactions_metadata table has the column issuing_transaction_id that references the id column of a row in the issuing_transactions table.

The following example creates a dictionary from the issuing_transactions table’s metadata table. It then uses it to access the value of the metadata key 'my_label' for several transactions.

`with transactions_metadata_dictionary as (
  select
    issuing_transaction_id,
    map_agg(key, value) metadata_dictionary
  from issuing_transactions_metadata
  group by 1
)

select
  date_format(it.created, '%Y-%m-%d') as day,
  it.id,
  it.amount,
  metadata_dictionary['my_label'] as my_label_value
from issuing_transactions it
left join transactions_metadata_dictionary
  on it.id = transactions_metadata_dictionary.issuing_transaction_id
where element_at(metadata_dictionary, 'my_label') is not null
order by day desc
limit 3`dayidamountmy_label_value2024-04-01ipi_b8kRbVGSz6NNTem2000true2024-04-01ipi_pIFkjNVXayGSbgd100true2024-04-01ipi_xBashcFTeW5nMlr10000falseWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Authorizations](#authorizations)[Transactions](#transactions)[Cards](#cards)[Cardholders](#cardholders)Products Used[Sigma](/stripe-data/access-data-in-dashboard)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`