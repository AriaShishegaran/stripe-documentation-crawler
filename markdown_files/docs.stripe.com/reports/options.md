htmlReport filters and settings | Stripe Documentation[Skip to content](#main-content)Filters and settings[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Foptions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Foptions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Basic financial reports](/docs/reports)# Report filters and settings

Understand the settings and controls common across all financial reports.This page describes the set of options available on each financial report. These include filters to select the data to view, including date range, currency, and connect accounts.

## Date range

When loading the page, the reports default to displaying data for the prior month. You can select previous months, current month-to-date, or customize the date range to specific dates. Selected dates are inclusive. For example, if you choose a date range of March 22, 2024–March 29, 2024, it includes data from the beginning of the day on March 22, 2024 (12:00am) through the end of the day on March 29, 2024 (11:59pm) in the selected time zone.

### Time zone customization

You can view financial reports based on either your Stripe account’s time zone or Coordinated Universal time (UTC). This selection affects both how the date range setting filters the report, and how dates and times contained within the report are presented.

### Data availability

Stripe computes all your data on a daily basis beginning at 12:00am UTC. The data for each day is defined as account activity that takes place between 12:00am UTC and 11:59pm UTC.

Financial reports tabProcessing timeBalanceWithin 12 hoursPayout reconciliationWithin 12 hoursCautionSLAs indicate when the reports are available for download. Webhook notifications might take additional time.

For example, all account activity on March 22, 2024 (from 12:00 am to 11:59 pm UTC) is available in the Balance financial reports tab by March 23, 2024 at 12:00 pm UTC.

Users who view reports in certain non-UTC timezones might experience an additional day delay. For example, the Balance report for Monday won’t become available until Wednesday morning when viewed in the America/Los_Angeles timezone (PST). This is because data is processed by UTC day, and the last few hours of Monday in PST correspond to Tuesday morning in UTC. As such, the report can’t be made available until Tuesday’s data has finished processing, which occurs by Wednesday at 12:00 pm UTC.

## Currency

Financial reports are based on your account’s settlement currency, which is the currency Stripe uses to send payouts to your bank.

If your account has multiple settlement currencies, you can view reports for each currency separately using the currency selector.

## Connect accounts

Connect platforms often need visibility into funds and transactions within their connected accounts in addition to their platform activity. When viewing a report as the platform account, you can toggle between viewing data:

- For the platform account only
- For all of the platform’s connected accounts (summary reports sum the data across all connected accounts, while itemized reports include relevant rows for all connected accounts)
- For a single connected account

To view reporting for a single connected account:

1. Go to the[Connect Accounts](https://dashboard.stripe.com/connect/accounts/overview)page and search for the account you want.
2. Click on the account’s name to go to the account detail page.
3. Click theView financial reportslink under the Reports section.

![](https://b.stripecdn.com/docs-statics-srv/assets/connected-account-statement.e0e6c62683f5ee3367690b9936bf018b.png)

CautionConnect platforms can’t view the financial reports for connected accounts that can access the full Stripe Dashboard and aren’t controlled by the platform. Holders of such accounts can independently control them if they were created with Stripe directly. Those accounts can contain transactions that originate outside of your platform. Because they have access to the full Stripe Dashboard, they can generate their own financial reports.

## Scheduled reports

To set up a subscription schedule for reports and get notified of new data, read our scheduled reports docs.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Date range](#date-range)[Currency](#currency)[Connect accounts](#connect-accounts)[Scheduled reports](#scheduled-reports)Products Used[Sigma](/stripe-data/access-data-in-dashboard)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`