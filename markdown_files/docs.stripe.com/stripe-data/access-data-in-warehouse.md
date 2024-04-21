htmlAccess data in your data warehouse with Data Pipeline | Stripe Documentation[Skip to content](#main-content)Access data in your data warehouse with Data Pipeline[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Faccess-data-in-warehouse)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Faccess-data-in-warehouse)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Access data in your data warehouse with Data Pipeline

Sync your Stripe account with Snowflake or Amazon Redshift.Data Pipeline is a no-code product that sends all your Stripe data and reports to Snowflake or Amazon Redshift. This allows you to centralize your Stripe data with other business data to close your books faster and get more detailed business insights.

With Data Pipeline, you can:

- Automatically export your complete Stripe data in a fast and reliable manner.
- Stop relying on third-party extract, transform, and load (ETL) pipelines or home-built API integrations.
- Combine data from all your Stripe accounts into one data warehouse.
- Integrate Stripe data with your other business data for more complete business insights.

### Database support

Data Pipeline currently supports Snowflake (deployed on AWS) and Amazon Redshift data regions. For additional information on supported instances, view the table below.

AWS RegionSnowflakeAmazon Redshift RA3 (with encryption)Amazon Redshift DS2/DC2us-west-2 (Oregon)us-east-2 (Ohio)us-east-1 (N. Virginia)us-west-1 (N. California)ca-central-1 (Central Canada)sa-east-1 (São Paulo)eu-central-1 (Frankfurt)eu-west-1 (Ireland)eu-west-2 (London)eu-west-3 (Paris)eu-north-1 (Stockholm)me-south-1 (Bahrain)ap-southeast-1 (Singapore)ap-southeast-2 (Sydney)ap-northeast-1 (Tokyo)ap-northeast-2 (Seoul)ap-east-1 (Hong Kong)NoteIf you’re using another data warehouse besides Snowflake or Amazon Redshift, or if your warehouse region isn’t listed above, let us know at data-pipeline@stripe.com.

Data Pipeline doesn’t support any non-AWS instances yet, such as Google Cloud Storage (GCS) or Microsoft Azure.

Because of data localization requirements, Stripe doesn’t offer Data Pipeline services to customers, merchants, or users in India.

## Get started

When you sign up for Data Pipeline, Stripe sends a data share to your Snowflake or Amazon Redshift account. After you accept the data share, you can access your core Stripe data in Snowflake or Amazon Redshift within 12 hours. After the initial load, your Stripe data refreshes regularly.

NoteYou can only have one warehouse account connected to your Stripe account.

SnowflakeAmazon Redshift RA3Amazon Redshift DC2/DS2### Link your Snowflake account

First, send all your up-to-date Stripe data and reports through the Dashboard:

1. In the[Data Pipeline settings](https://dashboard.stripe.com/settings/stripe-data-pipeline)page in the Dashboard, clickSign up.
2. From the drawer, selectSnowflake, then clickContinue.
3. Enter your Snowflake[Account Identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html)and your AWS region, then clickNext.
4. Copy the SQL from the code block and insert it in a SQL worksheet in Snowflake warehouse and run the query to retrieve the unique value. Enter the value in the text box and clickSubscribe.

### Access your data share in Snowflake

Next, after 48 hours, access your data share from your Snowflake account:

1. Navigate to your Snowflake account to accept the Stripe data share.
2. In Snowflake, have an`ACCOUNTADMIN`navigate toData>Shared Data. In theReady to Getsection, navigate to a share entitled`SHARE_[ACCOUNT_IDENTIFIER]`from one of three Stripe accounts, depending on your data warehouse region:  - `GSWUDFY_STRIPE_AWS_US_EAST_1`: data warehouses in`us-east-1`
  - `JZA07263`: data warehouses in`us-west-2`
  - `VM70738`: data warehouses in`us-east-2`

Then, clickGet shared datato accept the share.
3. In the modal that opens, give the database a name (for example,`Stripe`), select the roles to grant access to (for example,`SYSADMIN`), then clickGet Data.
4. Confirm that you can view your Stripe data inData From Direct SharesandDatabases. You can now query your Stripe data directly in Snowflake.

### Change the warehouse account

To change the warehouse account your Stripe account is connected to:

1. Turn off Data Pipeline from the Dashboard[settings page](https://dashboard.stripe.com/settings/stripe-data-pipeline).
2. Sign up for Data Pipeline again using the steps detailed above for the new warehouse account you want to connect to.

To add another Stripe account to your warehouse account:

1. Follow the[sign up](/stripe-data/access-data-in-warehouse#get-started)steps above for your new Stripe account.
2. Use the same account identifier as above for the respective warehouse. To find your Account ID, navigate to the Dashboard[settings page](https://dashboard.stripe.com/settings/stripe-data-pipeline)and locateIDunder theConnected data warehousesection.

## Query Stripe data in your data warehouse

In Snowflake and Amazon Redshift, your data is available as secure views. To query your data, follow the steps below.

SnowflakeAmazon Redshift RA3Amazon Redshift DC2/DS2View your available Stripe data by navigating to Views in the database you created. For each table, you can also see the available columns by clicking on the table and navigating to Columns.

### Database schemas

Your warehouse data is split into two database schemas based on the API mode used to create the data.

Schema nameDescription`STRIPE`Data populated from live mode`STRIPE_TESTMODE`Data populated from[test mode](/test-mode)### Multiple Stripe accounts with the same data warehouse

If you share data from multiple Stripe accounts with the same data warehouse, you can identify these separately. Every table has a merchant_id column, which allows you to filter the data by merchant and account.

### Example use case

In some cases, you might want to combine information from your proprietary data with Stripe data. The following schema shows an orders table that lists data about an order for a company:

dateorder_noStripe_txn_nocustomer_namepriceitems4/21/20241bt_xcVXgHcBfi83m94John Smith51 bookThe table above doesn’t contain data regarding transaction fees or payouts because that data is contained solely within Stripe. In Stripe, the balance_transactions table contains the following information, but lacks proprietary data regarding customer names and items purchased:

idamountavailable_onfeenetautomatic_transfer_idbt_xcVXgHcBfi83m945004/21/202450450po_rC4ocAkjGy8zl3jTo access your proprietary data alongside your Stripe data, combine the orders table with Stripe’s balance_transactions table:

`select
  orders.date,
  orders.order_no,
  orders.stripe_txn_no,
  bts.amount,
  bts.fee,
  bts.automatic_transfer_id
from mycompany.orders join stripe.balance_transactions bts
on orders.stripe_txn_no = bts.id;`After it completes, the following information is available:

dateorder_noStripe_txn_noamountfeeautomatic_transfer_id4/21/20241bt_xcVXgHcBfi83m9450050po_rC4ocAkjGy8zl3jDatasets![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can see a list of available datasets under Datasets in the schema documentation page in the Dashboard. Available datasets might vary by region, subject to local product availability and regulations. Each dataset contains one or more warehouse tables, and is shared by Data Pipeline separately as data becomes available. Data Pipeline updates some tables on different schedules based on the availability of new data. See data freshness for more information on available datasets and refresh schedules.

### Email notifications

You can also subscribe to email notifications for critical updates in the Dashboard.

## Financial reports in Data Pipeline

To speed up your financial close, you can access Stripe’s financial reports directly in your data warehouse.

NoteAt this time, financial reports aren’t available for Amazon Redshift.

Financial report templates have a FINANCIAL_REPORT prefix and are available as views in your data warehouse.

![](https://b.stripecdn.com/docs-statics-srv/assets/finrep.eb725f745cb57d3e03e813f96b3e8071.png)

### Generating financial reports in Snowflake

You can format your dates with varying levels of precision:

START_DATE = ‘2021-09-01’;

START_DATE = ‘2021-09-01 00:00:00’;

START_DATE = ‘2021-09-01 00:00:00.000’;

Generating financial reports from Data Pipeline requires setting a few custom variables. These are the same variables you set when generating the report through the Dashboard or API:

- `START_DATE`(varchar)—The starting date of the report (inclusive).
- `END_DATE`(varchar)—The ending date of the report (exclusive).
- `TIMEZONE`(varchar)—The time zone of non-UTC datetime columns.

To set these variables and run the report query:

1. Create a new worksheet.


2. Set the database schema and required variables to your desired values.

`-- set schema based on the name you gave your Stripe database
use schema db_name.stripe;
-- set financial report template variables
set (TIMEZONE, START_DATE, END_DATE) = ('UTC', '2021-09-01', '2021-10-01');`CautionRun these lines of code separately before attempting to query tables that require them. Otherwise, you might receive an error that a session variable doesn’t exist.

If you’re using the Snowflake Connector for Python, set the session parameter TIMEZONE with the ALTER SESSION SET TIMEZONE = 'UTC' command.


3. After running the code that sets the necessary variables, query the view of the report you want to generate. For example, running:

`select * from FINANCIAL_REPORT_BALANCE_CHANGE_FROM_ACTIVITY_ITEMIZED;`Returns the same results that the itemized balance change from the activity report displays in the Dashboard or through the API:

![](https://b.stripecdn.com/docs-statics-srv/assets/report.601f8e6f124d2dbf1adc74388fa58025.png)



## Turn off Data Pipeline

You can turn off Data Pipeline in the Dashboard settings page by clicking Turn off. After you disconnect, you lose access to your data share immediately.

Interested in using Data Pipeline for a data warehouse that we don't support yet?We are searching for users to participate in our limited Alpha program for additional data warehouses. If you'd like to join the waitlist, please enter your email address below and our team will be in touch with you soon.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon to understand your data requirements in more detail.### See also

- [Query transaction data](/stripe-data/query-transactions)
- [Query Billing data](/stripe-data/query-billing-data)
- [Sigma and Data Pipeline for Connect platforms](/stripe-data/query-connect-data)
- [Query Issuing data](/stripe-data/query-issuing-data)
- [Query Stripe fees data](/stripe-data/query-stripe-fees-data)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Query Stripe data in your data warehouse](#query-stripe-data-in-your-data-warehouse)[Financial reports in Data Pipeline](#financial-reports-in-data-pipeline)[Turn off Data Pipeline](#turn-off-data-pipeline)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`