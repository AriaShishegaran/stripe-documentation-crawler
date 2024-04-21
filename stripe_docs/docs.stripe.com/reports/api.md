# Run a report from the API

You can now automatically send your Stripe data and reports to Snowflake or Amazon Redshift in a few clicks with Stripe Data Pipeline. Learn more.

[Learn more](https://stripe.com/data-pipeline)

The financial reports in the Dashboard provide downloadable reports in CSV format for a variety of accounting and reconciliation tasks. These reports are also available through the API, so you can schedule them to run automatically or run them whenever you need to receive the associated report files for accounting purposes.

[financial reports](https://dashboard.stripe.com/reports)

## Report types

Each financial report in the Dashboard provides several different CSV downloads. All of the available downloads for the following reports are also available from the API:

- Balance

[Balance](/reports/report-types/balance)

- Payout reconciliation

[Payout reconciliation](/reports/report-types/payout-reconciliation)

- Tax

[Tax](/reports/report-types/tax)

- Connect platforms

[Connect platforms](/reports/report-types/connect)

The CSV reports format monetary amounts in major currency units as a decimal number. For example, The CSV formats 10 USD as dollars-and-cents (10.00). This differs from the Stripe API, where you specify amounts in the currency’s minor unit (US cents) as an integer. In the API, you format 10 USD as cents (1000).

Each report has both required and optional parameters you provide when creating a report run. Consider the following when running reports:

- Nearly every report type requires providing the run parameters interval_start (inclusive) and interval_end (exclusive) as Unix timestamps.

- Each corresponding report type resource has data_available_start and data_available_end fields. The API returns an invalid request error (status code 400) if your run doesn’t meet the following contraints:The interval_start and interval_end values must be between data_available_start and data_available_end (inclusive).The interval_start value must be before (and not equal to) interval_end.

- The interval_start and interval_end values must be between data_available_start and data_available_end (inclusive).

- The interval_start value must be before (and not equal to) interval_end.

- You can only download a report in a time zone for a ReportType with a timezone parameter. To do so, create a ReportRun object and supply the desired TZ database time zone name.  The timezone parameter is optional and defaults to UTC if not supplied. See IANA Time Zone Database for a list of valid timezone values.

[IANA Time Zone Database](https://www.iana.org/time-zones)

- The optional parameters currency and report_category filter results to just those rows matching the provided values.

- Reports return a default set of columns, but most report types allow you to customize the selection and ordering of columns in the output by including the optional columns parameter with a list of column names.

## Data availability

Stripe prepares data for your reports on a semi-daily basis. Report options provides details on expected processing time and data availability for each report.

[Report options](/reports/options#data-availability)

To programmatically determine the time range of data available for a given report type, retrieve the ReportType object of interest.  For example, the Balance summary report has the ID balance.summary.1, so you can retrieve the object as follows:

[retrieve](/api#retrieve_reporting_report_type)

In the example response below, the fields data_available_start and data_available_end reflect the full range of valid times for this report type. However, you’ll most often be running reports for a smaller interval within that range:

Timestamps, such as date_available_start, are measured in seconds since the Unix epoch. For example, 1519862400 represents the timestamp, 2018-03-01 00:00.

As soon as a report type has new data available, Stripe publishes a reporting.report_type.updated event with the updated ReportType object. To access these events, you must have a webhook configured that explicitly selects to receive reporting.report_type.updated events; webhooks that listen for ‘all events’ won’t receive them. After you receive such an event, you can then run the report. For details, see the recommended integration pattern.

[webhook configured](/webhooks#register-webhook)

[recommended integration pattern](#integration-pattern)

## Creating and accessing report runs

The ReportRun API object represents an instance of a ReportType generated with specific parameters. Review the documentation for the report type for the list of required and optional parameters for that type. For example, you can create a Balance change from activity summary report for April 2020 as follows:

[report type](#report-types)

[create](/api/reporting/report_run/create)

When first created, the object appears with status="pending":

When the run completes, Stripe updates the object, and it has a status of succeeded. It also has a nested result object, containing a URL that you can use to access the file with your API key. For example, if you were to retrieve the above report run after it completes, the response would be:

[retrieve](/api/reporting/report_run/retrieve)

[https://files.stripe.com/v1/files/file_xs8vrJzC/contents](https://files.stripe.com/v1/files/file_xs8vrJzC/contents)

To retrieve the file contents, use your API key to access the file specified by result.url:

Most runs complete within a few minutes. However, some runs could take longer—depending on the size of your total data set, and on the time range your report covers.

When a requested report run completes, Stripe sends one of two webhooks:

- A reporting.report_run.succeeded webhook will be sent if the run completes successfully.

- A reporting.report_run.failed webhook will be sent if the run fails. (This should be rare, but we recommend that integrations be prepared to handle this case in the same manner as catching a 500 response.)

In both cases, the webhook payload includes the updated ReportRun object, which includes status succeeded or failed, respectively.

## Recommended integration pattern for automated reporting

Configure a webhook that explicitly selects to receive reporting.report_type.updated events; webhooks that listen for ‘all events’ won’t receive them.

- A reporting.report_type.updated webhook is sent as soon as a new day’s data is available for a given report type. The payload includes the updated ReportType object. You’ll typically receive 20-30 webhooks each day, two for each report type. (Different users are eligible for different reports.)

- Upon receiving the reporting.report_type.updated webhook for the desired report type and range of data availability, create a report run. The response contains a new ReportRun object, initialized with status=pending.

[create a report run](/api/reporting/report_run/create)

- When the run completes, a reporting.report_run.succeeded webhook is sent. This webhook includes the nested field result.url. (As mentioned above, in the rare case of a failure, we’ll send a reporting.report_run.failed event instead.)

- Access the file contents at result.url, using your API key.
