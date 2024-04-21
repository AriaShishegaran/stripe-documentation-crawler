# Report filters and settings

This page describes the set of options available on each financial report. These include filters to select the data to view, including date range, currency, and connect accounts.

[date range](#date-range)

[currency](#currency)

[connect accounts](#connect-accounts)

## Date range

When loading the page, the reports default to displaying data for the prior month. You can select previous months, current month-to-date, or customize the date range to specific dates. Selected dates are inclusive. For example, if you choose a date range of March 22, 2024–March 29, 2024, it includes data from the beginning of the day on March 22, 2024 (12:00am) through the end of the day on March 29, 2024 (11:59pm) in the selected time zone.

You can view financial reports based on either your Stripe account’s time zone or Coordinated Universal time (UTC). This selection affects both how the date range setting filters the report, and how dates and times contained within the report are presented.

Stripe computes all your data on a daily basis beginning at 12:00am UTC. The data for each day is defined as account activity that takes place between 12:00am UTC and 11:59pm UTC.

SLAs indicate when the reports are available for download. Webhook notifications might take additional time.

For example, all account activity on March 22, 2024 (from 12:00 am to 11:59 pm UTC) is available in the Balance financial reports tab by March 23, 2024 at 12:00 pm UTC.

Users who view reports in certain non-UTC timezones might experience an additional day delay. For example, the Balance report for Monday won’t become available until Wednesday morning when viewed in the America/Los_Angeles timezone (PST). This is because data is processed by UTC day, and the last few hours of Monday in PST correspond to Tuesday morning in UTC. As such, the report can’t be made available until Tuesday’s data has finished processing, which occurs by Wednesday at 12:00 pm UTC.

## Currency

Financial reports are based on your account’s settlement currency, which is the currency Stripe uses to send payouts to your bank.

[settlement currency](/connect/payouts-connected-accounts#supported-settlement)

[payouts](/payouts)

If your account has multiple settlement currencies, you can view reports for each currency separately using the currency selector.

## Connect accounts

Connect platforms often need visibility into funds and transactions within their connected accounts in addition to their platform activity. When viewing a report as the platform account, you can toggle between viewing data:

[Connect](/connect)

- For the platform account only

- For all of the platform’s connected accounts (summary reports sum the data across all connected accounts, while itemized reports include relevant rows for all connected accounts)

- For a single connected account

To view reporting for a single connected account:

- Go to the Connect Accounts page and search for the account you want.

[Connect Accounts](https://dashboard.stripe.com/connect/accounts/overview)

- Click on the account’s name to go to the account detail page.

- Click the View financial reports link under the Reports section.

Connect platforms can’t view the financial reports for connected accounts that can access the full Stripe Dashboard and aren’t controlled by the platform. Holders of such accounts can independently control them if they were created with Stripe directly. Those accounts can contain transactions that originate outside of your platform. Because they have access to the full Stripe Dashboard, they can generate their own financial reports.

[controlled by the platform](/connect/platform-controls-for-stripe-dashboard-accounts)

## Scheduled reports

To set up a subscription schedule for reports and get notified of new data, read our scheduled reports docs.

[scheduled reports](/reports/scheduled-reports)
