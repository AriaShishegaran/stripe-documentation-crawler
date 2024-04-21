# Income statement

The income statement provides a detailed revenue and contra revenue breakdown by month. It shows revenue, contra revenue, expenses, gains, and losses. Contra revenue adjustments are deductions from gross revenue. Applying the contra revenue to your gross revenue results in your net income. Use this report to better understand your net revenue and determine how you want to track contra revenue items.

The report is available to download from our accounting reports page with multiple format options.

[accounting reports](https://dashboard.stripe.com/revenue-recognition/accounting-reports)

## Replication in Sigma

To replicate the income report in Sigma, use the revenue_recognition_debits_and_credits table.

[Sigma](/stripe-data/access-data-in-dashboard)

This sample query generates the report for revenue booked for the accounting period of October 2023 and grouped by account. You can adjust the dates to your desired time frame as well as different grouping parameters.

This sample query generates the report for revenue booked for the accounting period of Feb 2024 and grouped by line item. You can adjust the dates to your desired time frame as well as different grouping parameters.

To retrieve customer address information, join the results of this Sigma query with the invoices Sigma table.

[invoices](/stripe-data/query-billing-data#invoices)

If you’re using our chart of accounts beta feature, be sure to update the unbilled_ar_accounts mapping in the query below to reflect the accounts in your general ledger.

[chart of accounts](/revenue-recognition/chart-of-accounts)
