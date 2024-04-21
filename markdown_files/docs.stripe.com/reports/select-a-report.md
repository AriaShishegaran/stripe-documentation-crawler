htmlSelect a report | Stripe Documentation[Skip to content](#main-content)Select a report[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fselect-a-report)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fselect-a-report)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Basic financial reports](/docs/reports)# Select a report

Find the right report to fit your financial workflow.Stripe has a variety of different reports that provide information about your transactions. Start with the task you’re looking to perform and use the table below to identify the best report.

TaskSuggested report- Download monthly transaction history
- View monthly totals by transaction category
- [Reconcile](/reports/select-a-report#reconciliation)your Stripe balance like a bank account
- Download a list of your payouts

[Balance](/reports/balance)- Break down the individual transactions included in each payout to your bank account
- Download the detail for multiple payouts at a time

[Payout reconciliation](/reports/payout-reconciliation)## Reconciling your cash

The Balance and Payout reconciliation reports both provide downloadable transaction history including custom metadata, and you can use either to reconcile your cash. The reports group transactions in different ways to facilitate different types of reconciliation.

### The Balance report

The Balance report resembles a bank statement and is optimized for users who treat their Stripe account similar to a bank account in their accounting system. The Balance report helps you to record all activity that occurred in Stripe during a date range. Payouts are recorded as simple transfers between your Stripe account and your bank account, which don’t correspond to any specific payments. Like a bank account, the balance is reconciled at the end of the period to confirm that all transactions have been accounted for.

### The Payout reconciliation report

The Payout reconciliation report is optimized for users on automatic payout plans who model their Stripe balance as a temporary clearing account in their accounting system. This report helps you to reconcile each payout against the transactions included in that batch after it settles.

### Reconciling between the reports

Most reconciliation workflows don’t require using both reports, but it can be helpful to understand how they fit together.

The following table shows an account on a two day rolling schedule with 5 days of activity. The account was opened on the 1st of the month and accepted 10 USD in charges from its customers on its first day. Those funds became available on the 3rd, and the account received its first payout to its bank account because of the 2 day payout schedule.

DAYTRANSACTIONSPAYOUTSBALANCE AT EOD1st10 USD10 USD2nd20 USD30 USD3rd30 USD10 USD50 USD4th50 USD20 USD80 USD5th70 USD30 USD120 USDGiven the above account activity and a date range of 3rd–5th, the Balance summary would include the following data.

BALANCE SUMMARYStarting balance30 USDBalance change from activity150 USDTotal payouts-60 USDEnding balance120 USDThe Balance change from activity section of the Balance report includes all transactions that occurred from the 3rd through the 5th. The total of these transactions matches the Balance change from activity line item in the balance summary of 150 USD.

The Payout reconciliation report includes transactions from the 1st through the 3rd because these transactions were paid out within the selected date range of 3rd–5th. The sum of these transactions matches the Total Payouts line item of the balance summary of -60 USD.

The Ending balance reconciliation section at the bottom of the Payout reconciliation report includes transactions from the 4th and 5th because these transactions weren’t paid out within the selected date range of 3rd–5th. The sum of these transactions matches the Ending balance line item in the balance summary of 120 USD.

## Including transactions in a given date range

When you run a report, you select the reporting period using the controls in the dashboard, or by specifying start and end dates via the API. Each report uses a different type of date to determine which transactions fall within the reporting period.

ReportRelevant DateReport Column[Balance](/reports/balance)Date of change in Stripe balanceBalance transaction`created`(*)[Payout reconciliation](/reports/payout-reconciliation)Date automatic payout is available`automatic_payout_effective_at`(*) except automatic payout transactions, which impact your Stripe balance based on the available_on date

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Reconciling your cash](#reconciliation)[Including transactions in a given date range](#including-transactions-in-a-given-date-range)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`