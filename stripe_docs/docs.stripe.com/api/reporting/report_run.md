- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Report Runs

[Report Runs](/api/reporting/report_run)

The Report Run object represents an instance of a report type generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to a file where you can retrieve your results. For an overview, see API Access to Reports.

[API Access to Reports](/reporting/statements/api)

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

[live-mode API key](/keys#test-live-modes)

[POST/v1/reporting/report_runs](/api/reporting/report_run/create)

[GET/v1/reporting/report_runs/:id](/api/reporting/report_run/retrieve)

[GET/v1/reporting/report_runs](/api/reporting/report_run/list)

# The Report Run object

[The Report Run object](/api/reporting/report_run/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- parametersobjectParameters of this report run.Show child attributes

Parameters of this report run.

- report_typestringThe ID of the report type to run, such as "balance.summary.1".

The ID of the report type to run, such as "balance.summary.1".

[report type](/reports/report-types)

- resultnullable objectThe file object representing the result of the report run (populated when status=succeeded).Show child attributes

The file object representing the result of the report run (populated when status=succeeded).

- statusstringStatus of this report run. This will be pending when the run is initially created. When the run finishes, this will be set to succeeded and the result field will be populated. Rarely, we may encounter an error, at which point this will be set to failed and the error field will be populated.

Status of this report run. This will be pending when the run is initially created. When the run finishes, this will be set to succeeded and the result field will be populated. Rarely, we may encounter an error, at which point this will be set to failed and the error field will be populated.

- objectstring

- createdtimestamp

- errornullable string

- livemodeboolean

- succeeded_atnullable timestamp

# Create a Report Run

[Create a Report Run](/api/reporting/report_run/create)

Creates a new object and begin running the report. (Certain report types require a live-mode API key.)

[live-mode API key](https://stripe.com/docs/keys#test-live-modes)

- report_typestringRequiredThe ID of the report type to run, such as "balance.summary.1".

The ID of the report type to run, such as "balance.summary.1".

[report type](/reporting/statements/api#report-types)

- parametersobjectParameters specifying how the report should be run. Different Report Types have different required and optional parameters, listed in the API Access to Reports documentation.Show child parameters

Parameters specifying how the report should be run. Different Report Types have different required and optional parameters, listed in the API Access to Reports documentation.

[API Access to Reports](/reporting/statements/api)

Returns the new ReportRun object.

# Retrieve a Report Run

[Retrieve a Report Run](/api/reporting/report_run/retrieve)

Retrieves the details of an existing Report Run.

No parameters.

Returns the specified ReportRun object if found, and raises an error otherwise.

[an error](#errors)

# List all Report Runs

[List all Report Runs](/api/reporting/report_run/list)

Returns a list of Report Runs, with the most recent appearing first.

- createdobjectOnly return Report Runs that were created during the given date interval.Show child parameters

Only return Report Runs that were created during the given date interval.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit Report Runs, starting after the argument starting_after if it is provided. Each entry in the array is a separate ReportRun object. If no more Report Runs are available, the resulting array will be empty.
