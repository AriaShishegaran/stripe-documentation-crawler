htmlRun a report from the API | Stripe Documentation[Skip to content](#main-content)Reports API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fapi)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fapi)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Basic financial reports](/docs/reports)# Run a report from the API

Access Stripe's financial reports programmatically to automate your reconciliation workflow.NoteYou can now automatically send your Stripe data and reports to Snowflake or Amazon Redshift in a few clicks with Stripe Data Pipeline. Learn more.

The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can schedule them to run automatically or run them whenever you need to receive the associated report files for accounting purposes.

## Report types

Each financial report in the Dashboard provides several different CSV downloads. All of the available downloads for the following reports are also available from the API:

- [Balance](/reports/report-types/balance)
- [Payout reconciliation](/reports/report-types/payout-reconciliation)
- [Tax](/reports/report-types/tax)
- [Connect platforms](/reports/report-types/connect)

CSV and API monetary formats differThe CSV reports format monetary amounts in major currency units as a decimal number. For example, The CSV formats 10 USD as dollars-and-cents (10.00). This differs from the Stripe API, where you specify amounts in the currency’s minor unit (US cents) as an integer. In the API, you format 10 USD as cents (1000).

### Run parameters

Each report has both required and optional parameters you provide when creating a report run. Consider the following when running reports:

- Nearly every report type requires providing the run parameters`interval_start`(inclusive) and`interval_end`(exclusive) as Unix timestamps.
- Each corresponding report type resource has`data_available_start`and`data_available_end`fields. The API returns an invalid request error (status code`400`) if your run doesn’t meet the following contraints:  - The`interval_start`and`interval_end`values must be between`data_available_start`and`data_available_end`(inclusive).
  - The`interval_start`value must bebefore(and not equal to)`interval_end`.


- You can only download a report in a time zone for a`ReportType`with a`timezone`parameter. To do so, create a`ReportRun`object and supply the desired TZ database time zone name.  The`timezone`parameter is optional and defaults to UTC if not supplied. See[IANA Time Zone Database](https://www.iana.org/time-zones)for a list of valid timezone values.
- The optional parameters`currency`and`report_category`filter results to just those rows matching the provided values.
- Reports return a default set of columns, but most report types allow you to customize the selection and ordering of columns in the output by including the optional`columns`parameter with a list of column names.

## Data availability

Stripe prepares data for your reports on a semi-daily basis. Report options provides details on expected processing time and data availability for each report.

To programmatically determine the time range of data available for a given report type, retrieve the ReportType object of interest.  For example, the Balance summary report has the ID balance.summary.1, so you can retrieve the object as follows:

Command Line[curl](#)`curl https://api.stripe.com/v1/reporting/report_types/balance.summary.1 \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:`In the example response below, the fields data_available_start and data_available_end reflect the full range of valid times for this report type. However, you’ll most often be running reports for a smaller interval within that range:

`{
  "id": "balance.summary.1",
  "name": "Balance summary",
  "version": "1",
  "object": "reporting.report_type",
  "data_available_start": 1519862400,
  "data_available_end": 1517356800,
  "updated": 1517382720,
}`Timestamps, such as date_available_start, are measured in seconds since the Unix epoch. For example, 1519862400 represents the timestamp, 2018-03-01 00:00.

### New data notifications

As soon as a report type has new data available, Stripe publishes a reporting.report_type.updated event with the updated ReportType object. To access these events, you must have a webhook configured that explicitly selects to receive reporting.report_type.updated events; webhooks that listen for ‘all events’ won’t receive them. After you receive such an event, you can then run the report. For details, see the recommended integration pattern.

## Creating and accessing report runs

The ReportRun API object represents an instance of a ReportType generated with specific parameters. Review the documentation for the report type for the list of required and optional parameters for that type. For example, you can create a Balance change from activity summary report for April 2020 as follows:

Command Line[curl](#)`curl https://api.stripe.com/v1/reporting/report_runs \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "report_type"="balance_change_from_activity.itemized.3" \
  -d "parameters[interval_start]"=1577865600 \
  -d "parameters[interval_end]"=1580544000 \
  -d "parameters[timezone]"="America/Los_Angeles" \
  -d "parameters[columns][]"="created" \
  -d "parameters[columns][]"="reporting_category" \
  -d "parameters[columns][]"="net"

# Timestamps are for 2020-01-01 00:00 PST and 2020-02-01 00:00 PST.
# The columns parameter is optional. A default set of columns will be provided if you don't specify a value.
# Note that a live-mode API key is required.`When first created, the object appears with status="pending":

`{
  "id": "frr_123",
  "object": "reporting.report_run",
  "livemode": true,
  "report_type": "balance_change_from_activity.itemized.3",
  "parameters": {
    "columns": [ "created", "reporting_category", "net" ],
    "interval_start": 1577865600,
    "interval_end": 1580544000,
    "timezone": "America/Los_Angeles"
  },
  "created": 1580832900,
  "status": "pending",
  "result": null
}`When the run completes, Stripe updates the object, and it has a status of succeeded. It also has a nested result object, containing a URL that you can use to access the file with your API key. For example, if you were to retrieve the above report run after it completes, the response would be:

`{
  "id": "frr_123",
  "object": "reporting.report_run",
  "livemode": true,
  "report_type": "balance_change_from_activity.itemized.3",
  "parameters": {
    "columns": [ "created", "reporting_category", "net" ],
    "interval_start": 1577865600,
    "interval_end": 1580544000,
    "timezone": "America/Los_Angeles"
  },
  "created": 1580832900,
  "status": "succeeded",
  "succeeded_at": 1580832960,
  "result": {
    "id": "file_xs8vrJzC",
    "object": "file",
    "url": "https://files.stripe.com/v1/files/file_xs8vrJzC/contents",
    "created": 1580832960,
    "purpose": "report_run",
    "size": 53075,
    "type": "csv"
  }
}`To retrieve the file contents, use your API key to access the file specified by result.url:

Command Line[curl](#)`curl https://files.stripe.com/v1/files/file_xs8vrJzC/contents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:`Notification of report run completion![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Most runs complete within a few minutes. However, some runs could take longer—depending on the size of your total data set, and on the time range your report covers.

When a requested report run completes, Stripe sends one of two webhooks:

- A`reporting.report_run.succeeded`webhook will be sent if the run completes successfully.
- A`reporting.report_run.failed`webhook will be sent if the run fails. (This should be rare, but we recommend that integrations be prepared to handle this case in the same manner as catching a`500`response.)

In both cases, the webhook payload includes the updated ReportRun object, which includes status succeeded or failed, respectively.

## Recommended integration pattern for automated reporting

Configure a webhook that explicitly selects to receive reporting.report_type.updated events; webhooks that listen for ‘all events’ won’t receive them.

1. A`reporting.report_type.updated`webhook is sent as soon as a new day’s data is available for a given report type. The payload includes the updated`ReportType`object. You’ll typically receive 20-30 webhooks each day, two for each report type. (Different users are eligible for different reports.)
2. Upon receiving the`reporting.report_type.updated`webhook for the desired report type and range of data availability,[create a report run](/api/reporting/report_run/create). The response contains a new`ReportRun`object, initialized with`status=pending`.
3. When the run completes, a`reporting.report_run.succeeded`webhook is sent. This webhook includes the nested field`result.url`. (As mentioned above, in the rare case of a failure, we’ll send a`reporting.report_run.failed`event instead.)
4. Access the file contents at`result.url`, using your API key.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Report types](#report-types)[Data availability](#data-availability)[Creating and accessing report runs](#report-runs)[Recommended integration pattern for automated reporting](#integration-pattern)Products Used[Sigma](/stripe-data/access-data-in-dashboard)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`