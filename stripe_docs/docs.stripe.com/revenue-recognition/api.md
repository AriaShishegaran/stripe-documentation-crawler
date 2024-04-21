# Revenue Recognition APIBeta

For accrual accounting, Stripe Revenue Recognition provides downloadable reports, such as a monthly summary and a revenue waterfall. You can download these reports in CSV format through the Dashboard or you can programmatically access them through the API.

[downloadable reports](/revenue-recognition/reports)

[monthly summary](/revenue-recognition/reports/monthly-summary)

[revenue waterfall](/revenue-recognition/reports/waterfall)

[Dashboard](https://dashboard.stripe.com/revenue-recognition)

Revenue Recognition has six supported report types:

- revenue_recognition.debit_credit_summary.1

- revenue_recognition.debit_credit_by_price.1

- revenue_recognition.debit_credit_by_product.1

- revenue_recognition.debit_credit_by_customer.1

- revenue_recognition.debit_credit_by_invoice.1

- revenue_recognition.debit_credit_by_invoice_line_item.1

Because this feature is in beta, the data fields might change.

## Download a report

The following example downloads the debits and credits by summary for May 2021.

First, create a report run using Create a Report Run.

[Create a Report Run](/api/reporting/report_run/create)

To get a report for May 2023, set parameters[interval_start] to 1 May 2023 and parameters[interval_end] to 1 Jun 2023.

Next, check whether the Report Run object succeeds by fetching the report run object:

[Report Run](/api/reporting/report_run/object)

The report run object ID starts with frr_.

When the object’s status is succeeded, you can download the CSV using its result.id value, as in the following example:

The report run result ID starts with file_.

## Report Run Parameters

- interval_start

- interval_end

- decimal_format

- interval_start

- interval_end

- customer

- decimal_format

- interval_start

- interval_end

- customer

- decimal_format

- interval_start

- interval_end

- decimal_format

- interval_start

- interval_end

- customer

- invoice

- invoice_line_item

- decimal_format

- interval_start

- interval_end

- customer

- invoice

- invoice_line_item

- decimal_format

## Report Run Columns

By default, reports are run with the default set of columns. You can customize the selection and ordering of columns in the output by including the optional columns parameter with a list of column names. You can find the supported columns for each report type below.

[list of column names](/reports/api#report-runs)

API report type: revenue_recognition.debit_credit_summary.1

[ISO code for the currency](/currencies)

API report type: revenue_recognition.debit_credit_by_price.1

[ISO code for the currency](/currencies)

API report type: revenue_recognition.debit_credit_by_product.1

[ISO code for the currency](/currencies)

API report type: revenue_recognition.debit_credit_by_customer.1

[ISO code for the currency](/currencies)

API report type: revenue_recognition.debit_credit_by_invoice.1

[ISO code for the currency](/currencies)

API report type: revenue_recognition.debit_credit_by_invoice_line_item.1

[ISO code for the currency](/currencies)

If you encounter any issues, you can contact revenue-recognition-api-beta@stripe.com.

[revenue-recognition-api-beta@stripe.com](mailto:revenue-recognition-api-beta@stripe.com)
