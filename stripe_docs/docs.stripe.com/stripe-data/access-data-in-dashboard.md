# Access data in Stripe with Sigma

Sigma makes all your transactional data available within an interactive SQL environment in the Stripe Dashboard. Sigma lets you create fully customized reports using information about your payments, subscriptions, customers, payouts, and so on.

[Sigma](https://stripe.com/sigma)

With Sigma, you can:

- Get the information you need that best reflects your business and Stripe integration.

Get the information you need that best reflects your business and Stripe integration.

- Export in CSV format to import into your tools.

Export in CSV format to import into your tools.

- Fetch the data you need on a schedule of your choosing.

Fetch the data you need on a schedule of your choosing.

The available data within Sigma is read-only. Queries can’t modify existing data or create new transactions.

## Get started

Begin building custom reports using templates. Learn more about writing queries and the broad range of reporting functions.

[templates](/stripe-data/write-queries#templates)

[writing queries and the broad range of reporting functions](/stripe-data/write-queries)

## Financial reports in Sigma

Financial Reports give you the data you need to complete your accounting and reconciliation workflows. You can use Sigma to create customized versions of these reports tailored to your needs and find queries to generate Stripe’s financial reports in the templates section of the Sigma sidebar. Additionally, you can find the schema for the underlying tables that drive financial reports in the schema section of the sidebar.

[Financial Reports](/reports)

You can recreate the following reports and their connected variants in Sigma:

Reports follow the same availability rules as the Stripe Dashboard. Payout Reconciliation reports are only available for users with the Automatic payouts setting enabled, and connect variants of reports are only available for users on Stripe Connect.

[Stripe Connect](/connect)

To generate a Financial Report in Sigma, navigate to the templates section of your Sigma Dashboard and search for the report you want to generate. Click the template, then click Run in the top right corner.

[templates](/stripe-data/write-queries#templates)

By default, these reports run on the last completed month that all data is available for. You can change the dates by making a copy of the template and editing the report date intervals.

Descriptions of the columns produced by financial report queries are available in the Financial Reporting documentation.

[Financial Reporting documentation](/reports/select-a-report)

The Financial Reports you generate from your Sigma Dashboard might slightly differ from those you generate on the Stripe Dashboard.

- Data availability: For Financial Reports, you can find the most recent day of available data by selecting month to date or opening the date picker calendar. In Sigma, the data_load_time parameter provides the timestamp that data is available through.

- Time zone: Financial Reports in the Stripe Dashboard filter reports by the local time zone by default, but you can switch them to use the UTC time zone. Sigma filters templates by the UTC time zone.

- Date range: A selected date range for Stripe Dashboard financial reports, such as Jan. 13 to Jan. 14, filters reports from January 13 00:00:00 up to January 14 23:59:59. A chosen date range filter for Sigma templates for January 13 to January 14 filters reports from Jan 13 00:00:00 up to January 13 23:59:59.

- Currency: Financial Reports in the Stripe Dashboard always filter data to a single currency. By default, the Sigma report templates return all currencies. You can add a WHERE clause to your Sigma query to restrict your results to a single currency.

- Metadata: Financial reports allow you to include metadata. Sigma templates don’t include it. You can add metadata to your reports by following the Metadata to column Sigma template.

## Unsubscribing from Sigma

If you currently have an active Sigma subscription and want to cancel it for any reason, unsubscribe from Sigma in the settings page  of the Stripe Dashboard by clicking Cancel Stripe Sigma subscription. You can continue using Sigma until the end of the billing cycle, at which point the subscription ends.

[Sigma in the settings page](https://dashboard.stripe.com/settings/sigma)

- Query transaction data

[Query transaction data](/stripe-data/query-transactions)

- Query Billing data

[Query Billing data](/stripe-data/query-billing-data)

- Sigma and Data Pipeline for Connect platforms

[Sigma and Data Pipeline for Connect platforms](/stripe-data/query-connect-data)

- Query Issuing data

[Query Issuing data](/stripe-data/query-issuing-data)

- Query Stripe fees data

[Query Stripe fees data](/stripe-data/query-stripe-fees-data)

- Schedule queries with Sigma

[Schedule queries with Sigma](/stripe-data/schedule-queries)
