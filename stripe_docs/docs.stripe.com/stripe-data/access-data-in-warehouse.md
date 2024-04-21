# Access data in your data warehouse with Data Pipeline

Data Pipeline is a no-code product that sends all your Stripe data and reports to Snowflake or Amazon Redshift. This allows you to centralize your Stripe data with other business data to close your books faster and get more detailed business insights.

[Data Pipeline](https://dashboard.stripe.com/settings/stripe-data-pipeline)

With Data Pipeline, you can:

- Automatically export your complete Stripe data in a fast and reliable manner.

- Stop relying on third-party extract, transform, and load (ETL) pipelines or home-built API integrations.

- Combine data from all your Stripe accounts into one data warehouse.

- Integrate Stripe data with your other business data for more complete business insights.

Data Pipeline currently supports Snowflake (deployed on AWS) and Amazon Redshift data regions. For additional information on supported instances, view the table below.

[Snowflake](https://docs.snowflake.com/en/user-guide/intro-regions.html)

[Amazon Redshift](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html)

If you’re using another data warehouse besides Snowflake or Amazon Redshift, or if your warehouse region isn’t listed above, let us know at data-pipeline@stripe.com.

[data-pipeline@stripe.com](mailto:data-pipeline@stripe.com)

Data Pipeline doesn’t support any non-AWS instances yet, such as Google Cloud Storage (GCS) or Microsoft Azure.

Because of data localization requirements, Stripe doesn’t offer Data Pipeline services to customers, merchants, or users in India.

## Get started

When you sign up for Data Pipeline, Stripe sends a data share to your Snowflake or Amazon Redshift account. After you accept the data share, you can access your core Stripe data in Snowflake or Amazon Redshift within 12 hours. After the initial load, your Stripe data refreshes regularly.

[refreshes regularly](/stripe-data/available-data)

You can only have one warehouse account connected to your Stripe account.

First, send all your up-to-date Stripe data and reports through the Dashboard:

- In the Data Pipeline settings page in the Dashboard, click Sign up.

[Data Pipeline settings](https://dashboard.stripe.com/settings/stripe-data-pipeline)

- From the drawer, select Snowflake, then click Continue.

- Enter your Snowflake Account Identifier and your AWS region, then click Next.

[Account Identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html)

- Copy the SQL from the code block and insert it in a SQL worksheet in Snowflake warehouse and run the query to retrieve the unique value. Enter the value in the text box and click Subscribe.

Next, after 48 hours, access your data share from your Snowflake account:

- Navigate to your Snowflake account to accept the Stripe data share.

- In Snowflake, have an ACCOUNTADMIN navigate to Data > Shared Data. In the Ready to Get section, navigate to a share entitled SHARE_[ACCOUNT_IDENTIFIER] from one of three Stripe accounts, depending on your data warehouse region:GSWUDFY_STRIPE_AWS_US_EAST_1: data warehouses in us-east-1JZA07263: data warehouses in us-west-2VM70738: data warehouses in us-east-2Then, click Get shared data to accept the share.

- GSWUDFY_STRIPE_AWS_US_EAST_1: data warehouses in us-east-1

- JZA07263: data warehouses in us-west-2

- VM70738: data warehouses in us-east-2

- In the modal that opens, give the database a name (for example, Stripe), select the roles to grant access to (for example, SYSADMIN), then click Get Data.

- Confirm that you can view your Stripe data in Data From Direct Shares and Databases. You can now query your Stripe data directly in Snowflake.

To change the warehouse account your Stripe account is connected to:

- Turn off Data Pipeline from the Dashboard settings page.

[settings page](https://dashboard.stripe.com/settings/stripe-data-pipeline)

- Sign up for Data Pipeline again using the steps detailed above for the new warehouse account you want to connect to.

To add another Stripe account to your warehouse account:

- Follow the sign up steps above for your new Stripe account.

[sign up](/stripe-data/access-data-in-warehouse#get-started)

- Use the same account identifier as above for the respective warehouse. To find your Account ID, navigate to the Dashboard settings page and locate ID under the Connected data warehouse section.

[settings page](https://dashboard.stripe.com/settings/stripe-data-pipeline)

## Query Stripe data in your data warehouse

In Snowflake and Amazon Redshift, your data is available as secure views. To query your data, follow the steps below.

View your available Stripe data by navigating to Views in the database you created. For each table, you can also see the available columns by clicking on the table and navigating to Columns.

Your warehouse data is split into two database schemas based on the API mode used to create the data.

[test mode](/test-mode)

If you share data from multiple Stripe accounts with the same data warehouse, you can identify these separately. Every table has a merchant_id column, which allows you to filter the data by merchant and account.

In some cases, you might want to combine information from your proprietary data with Stripe data. The following schema shows an orders table that lists data about an order for a company:

The table above doesn’t contain data regarding transaction fees or payouts because that data is contained solely within Stripe. In Stripe, the balance_transactions table contains the following information, but lacks proprietary data regarding customer names and items purchased:

[payouts](/payouts)

To access your proprietary data alongside your Stripe data, combine the orders table with Stripe’s balance_transactions table:

After it completes, the following information is available:

You can see a list of available datasets under Datasets in the schema documentation page in the Dashboard. Available datasets might vary by region, subject to local product availability and regulations. Each dataset contains one or more warehouse tables, and is shared by Data Pipeline separately as data becomes available. Data Pipeline updates some tables on different schedules based on the availability of new data. See data freshness for more information on available datasets and refresh schedules.

[schema documentation](https://dashboard.stripe.com/stripe-schema)

[data freshness](/stripe-data/available-data)

You can also subscribe to email notifications for critical updates in the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/stripe-data-pipeline)

## Financial reports in Data Pipeline

To speed up your financial close, you can access Stripe’s financial reports directly in your data warehouse.

[financial reports](/reports)

At this time, financial reports aren’t available for Amazon Redshift.

Financial report templates have a FINANCIAL_REPORT prefix and are available as views in your data warehouse.

You can format your dates with varying levels of precision:

START_DATE = ‘2021-09-01’;

START_DATE = ‘2021-09-01 00:00:00’;

START_DATE = ‘2021-09-01 00:00:00.000’;

Generating financial reports from Data Pipeline requires setting a few custom variables. These are the same variables you set when generating the report through the Dashboard or API:

- START_DATE (varchar)—The starting date of the report (inclusive).

- END_DATE (varchar)—The ending date of the report (exclusive).

- TIMEZONE (varchar)—The time zone of non-UTC datetime columns.

To set these variables and run the report query:

- Create a new worksheet.

Create a new worksheet.

- Set the database schema and required variables to your desired values.-- set schema based on the name you gave your Stripe database
use schema db_name.stripe;
-- set financial report template variables
set (TIMEZONE, START_DATE, END_DATE) = ('UTC', '2021-09-01', '2021-10-01');CautionRun these lines of code separately before attempting to query tables that require them. Otherwise, you might receive an error that a session variable doesn’t exist.If you’re using the Snowflake Connector for Python, set the session parameter TIMEZONE with the ALTER SESSION SET TIMEZONE = 'UTC' command.

Set the database schema and required variables to your desired values.

Run these lines of code separately before attempting to query tables that require them. Otherwise, you might receive an error that a session variable doesn’t exist.

If you’re using the Snowflake Connector for Python, set the session parameter TIMEZONE with the ALTER SESSION SET TIMEZONE = 'UTC' command.

[Snowflake Connector for Python](https://docs.snowflake.com/en/user-guide/python-connector.html)

- After running the code that sets the necessary variables, query the view of the report you want to generate. For example, running:select * from FINANCIAL_REPORT_BALANCE_CHANGE_FROM_ACTIVITY_ITEMIZED;Returns the same results that the itemized balance change from the activity report displays in the Dashboard or through the API:

After running the code that sets the necessary variables, query the view of the report you want to generate. For example, running:

Returns the same results that the itemized balance change from the activity report displays in the Dashboard or through the API:

## Turn off Data Pipeline

You can turn off Data Pipeline in the Dashboard settings page by clicking Turn off. After you disconnect, you lose access to your data share immediately.

[settings page](https://dashboard.stripe.com/settings/stripe-data-pipeline)

[privacy policy](https://stripe.com/privacy)

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
