htmlData freshness | Stripe Documentation[Skip to content](#main-content)Data freshness[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Favailable-data)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Favailable-data)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Data freshness

Learn about the data freshness of Stripe data and the schema.Sigma and Data Pipeline provide access to the Stripe data available with the Stripe API. You can also access data such as Stripe financial reports, which isn’t available in the Stripe API.

## Data freshness

Sigma and Data Pipeline make most of your transaction data available to query within one day.

Data freshness for SigmaData freshness for Data PipelineSigma makes most of your Stripe transaction data available to query within one day. All API activity for a given day (from 12:00am to 11:59pm UTC) is available to query by 12:00pm UTC the following day. For example, data for the end of day Sunday UTC time is available by Monday at 12:00pm UTC. Similarly, data for the last day of the month is available one day into the following month.

### Query data load times with Sigma

The interface in the Dashboard displays the date and time of the last payments data. You can use data_load_time as a value in your queries to represent when data is most recently processed on your account. For example, if payment tables were last updated on 4/21/2024, the data_load_time is interpreted as 2024-04-18 00:00:00 +0000. At times, Sigma may reflect activity that is more recent than data_load_time. For example, a charge authorized just before midnight, but captured soon after, may show as captured.

Making data available requires additional time. You can use data_load_time as a value in your queries that represents when data is most recently processed on your account. Use this value to dynamically set a date range in your scheduled queries.

For example, consider the following scheduled query that returns a list of balance transactions created one month before data_load_time.

`select
  id,
  amount,
  fee,
  currency
from balance_transactions -- this table is the canonical record of changes to your Stripe balance
where
  created < data_load_time and
  created >= data_load_time - interval '1' month
order by created desc
limit 10`The following timeline illustrates how this works based on data availability.

DateTimeline for results2024-04-18- `data_load_time`is interpreted as`2024-04-18`
- The scheduled query includes transaction data through EOD2024-04-17
- Query results are available on2024-04-18by 2pm UTC

Now, consider the following scheduled query that returns a list of charge_ids and interchange billing amounts associated with each fee balance debit created one month before data_load_time.

`select
  ic.charge_id,
  ic.billing_currency,
  ic.billing_amount,
  ic.balance_transaction_id,
  ic.balance_transaction_created_at
from icplus_fees as ic
join balance_transactions as bt
  on ic.balance_transaction_id = bt.id
where bt.created >= data_load_time - interval '1' month
  and bt.created < data_load_time`If this query is scheduled to recur daily, the following timeline illustrates when you can expect the results.

DateTimeline for results2024-04-21- `data_load_time`is interpreted as`2024-04-18 00:00:00 +0000`
- The scheduled query includes transaction data through EOD2024-04-17
- Query results are available on2024-04-21by 2am UTC

## Data freshness for datasets

View the table below for information on data freshness for specific datasets.

DatasetExample tablesSigma freshnessData Pipeline freshnessCore API tables (including Connect versions)`balance_transactions`,`charges`,`connected_account_balance_transactions`24 hours9 hoursDaily refreshed tables`exchange_rates_from_usd`,`radar_rules`24 hours28 hours## About the schema

Our full-page schema documentation shows the schema in a split-view format and provides more details on table linkages.

The schema follows our API conventions as closely as possible. Many of the tables correspond to specific API objects, with each column representing a specific attribute that’s reported. For instance, the charges table represents information about Charge objects, which is displayed in the Payments section of the Dashboard.

When you write queries, refer to the our API reference for additional content and values.

### Sigma schema tab

The Schema tab in Sigma displays all the available data that you can use in your queries, organized by category. Each category contains a set of tables that represents the available data.

You can select a table to expand it and reveal its available columns, along with a description of the type of data it contains (for example: Boolean , Varchar, Foreign key, and so on). Hover the cursor over any column to reveal a description. Use the search field at the top of the schema to find specific tables and columns.

![](https://b.stripecdn.com/docs-statics-srv/assets/schema.cbdde995d4375a496852405c9a897123.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Data freshness](#data-freshness)[Data freshness for datasets](#data-freshness-for-datasets)[About the schema](#about-the-schema)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`