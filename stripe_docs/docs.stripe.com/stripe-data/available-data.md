# Data freshness

Sigma and Data Pipeline provide access to the Stripe data available with the Stripe API. You can also access data such as Stripe financial reports, which isn’t available in the Stripe API.

[Stripe API](/api)

[financial reports](/reports)

## Data freshness

Sigma and Data Pipeline make most of your transaction data available to query within one day.

Sigma makes most of your Stripe transaction data available to query within one day. All API activity for a given day (from 12:00am to 11:59pm UTC) is available to query by 12:00pm UTC the following day. For example, data for the end of day Sunday UTC time is available by Monday at 12:00pm UTC. Similarly, data for the last day of the month is available one day into the following month.

The interface in the Dashboard displays the date and time of the last payments data. You can use data_load_time as a value in your queries to represent when data is most recently processed on your account. For example, if payment tables were last updated on 4/21/2024, the data_load_time is interpreted as 2024-04-18 00:00:00 +0000. At times, Sigma may reflect activity that is more recent than data_load_time. For example, a charge authorized just before midnight, but captured soon after, may show as captured.

Making data available requires additional time. You can use data_load_time as a value in your queries that represents when data is most recently processed on your account. Use this value to dynamically set a date range in your scheduled queries.

For example, consider the following scheduled query that returns a list of balance transactions created one month before data_load_time.

The following timeline illustrates how this works based on data availability.

- data_load_time is interpreted as 2024-04-18

- The scheduled query includes transaction data through EOD 2024-04-17

- Query results are available on 2024-04-18 by 2pm UTC

Now, consider the following scheduled query that returns a list of charge_ids and interchange billing amounts associated with each fee balance debit created one month before data_load_time.

If this query is scheduled to recur daily, the following timeline illustrates when you can expect the results.

- data_load_time is interpreted as 2024-04-18 00:00:00 +0000

- The scheduled query includes transaction data through EOD 2024-04-17

- Query results are available on 2024-04-21 by 2am UTC

## Data freshness for datasets

View the table below for information on data freshness for specific datasets.

## About the schema

Our full-page schema documentation shows the schema in a split-view format and provides more details on table linkages.

[schema documentation](https://dashboard.stripe.com/stripe-schema)

The schema follows our API conventions as closely as possible. Many of the tables correspond to specific API objects, with each column representing a specific attribute that’s reported. For instance, the charges table represents information about Charge objects, which is displayed in the Payments section of the Dashboard.

[Charge](/api#charge_object)

When you write queries, refer to the our API reference for additional content and values.

[API reference](/api)

The Schema tab in Sigma displays all the available data that you can use in your queries, organized by category. Each category contains a set of tables that represents the available data.

[Schema tab](https://dashboard.stripe.com/stripe-schema)

You can select a table to expand it and reveal its available columns, along with a description of the type of data it contains (for example: Boolean , Varchar, Foreign key, and so on). Hover the cursor over any column to reveal a description. Use the search field at the top of the schema to find specific tables and columns.
