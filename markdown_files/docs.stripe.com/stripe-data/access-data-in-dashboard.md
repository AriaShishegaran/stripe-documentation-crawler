htmlAccess data in Stripe with Sigma | Stripe Documentation[Skip to content](#main-content)Access data in your Stripe Dashboard with Sigma[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Faccess-data-in-dashboard)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Faccess-data-in-dashboard)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Access data in Stripe with Sigma

Generate custom reports for charges, refunds, disputes, and more with Sigma.Sigma makes all your transactional data available within an interactive SQL environment in the Stripe Dashboard. Sigma lets you create fully customized reports using information about your payments, subscriptions, customers, payouts, and so on.

With Sigma, you can:

- Get the information you need that best reflects your business and Stripe integration.


- Export in CSV format to import into your tools.


- Fetch the data you need on a schedule of your choosing.



### Read-only queries

The available data within Sigma is read-only. Queries can’t modify existing data or create new transactions.

## Get started

Begin building custom reports using templates. Learn more about writing queries and the broad range of reporting functions.

## Financial reports in Sigma

Financial Reports give you the data you need to complete your accounting and reconciliation workflows. You can use Sigma to create customized versions of these reports tailored to your needs and find queries to generate Stripe’s financial reports in the templates section of the Sigma sidebar. Additionally, you can find the schema for the underlying tables that drive financial reports in the schema section of the sidebar.

You can recreate the following reports and their connected variants in Sigma:

Report groupSigma template nameAPI report typeBalance ReportItemized balance change from activity`balance_change_from_activity.itemized.3`Itemized payouts`payouts.itemized.3`Payout reconciliation reportItemized payout reconciliation`payout_reconciliation.itemized.5`Itemized ending balance reconciliation`ending_balance_reconciliation.itemized.4`Reports follow the same availability rules as the Stripe Dashboard. Payout Reconciliation reports are only available for users with the Automatic payouts setting enabled, and connect variants of reports are only available for users on Stripe Connect.

### Opening a Financial Report in Sigma

To generate a Financial Report in Sigma, navigate to the templates section of your Sigma Dashboard and search for the report you want to generate. Click the template, then click Run in the top right corner.

By default, these reports run on the last completed month that all data is available for. You can change the dates by making a copy of the template and editing the report date intervals.

Descriptions of the columns produced by financial report queries are available in the Financial Reporting documentation.

### Considerations

The Financial Reports you generate from your Sigma Dashboard might slightly differ from those you generate on the Stripe Dashboard.

- Data availability:For Financial Reports, you can find the most recent day of available data by selectingmonth to dateor opening the date picker calendar. In Sigma, the`data_load_time`parameter provides the timestamp that data is available through.
- Time zone:Financial Reports in the Stripe Dashboard filter reports by the local time zone by default, but you can switch them to use the UTC time zone. Sigma filters templates by the UTC time zone.
- Date range:A selected date range for Stripe Dashboard financial reports, such as Jan. 13 to Jan. 14, filters reports from January 13 00:00:00 up to January 14 23:59:59. A chosen date range filter for Sigma templates for January 13 to January 14 filters reports from Jan 13 00:00:00 up to January 13 23:59:59.
- Currency:Financial Reports in the Stripe Dashboard always filter data to a single currency. By default, the Sigma report templates return all currencies. You can add a`WHERE`clause to your Sigma query to restrict your results to a single currency.
- Metadata:Financial reports allow you to include metadata. Sigma templates don’t include it. You can add metadata to your reports by following the`Metadata to column`Sigma template.

## Unsubscribing from Sigma

If you currently have an active Sigma subscription and want to cancel it for any reason, unsubscribe from Sigma in the settings page  of the Stripe Dashboard by clicking Cancel Stripe Sigma subscription. You can continue using Sigma until the end of the billing cycle, at which point the subscription ends.

### See also

- [Query transaction data](/stripe-data/query-transactions)
- [Query Billing data](/stripe-data/query-billing-data)
- [Sigma and Data Pipeline for Connect platforms](/stripe-data/query-connect-data)
- [Query Issuing data](/stripe-data/query-issuing-data)
- [Query Stripe fees data](/stripe-data/query-stripe-fees-data)
- [Schedule queries with Sigma](/stripe-data/schedule-queries)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Financial reports in Sigma](#financial-reports-in-sigma)[Unsubscribing from Sigma](#unsubscribing-from-sigma)Products Used[Sigma](/stripe-data/access-data-in-dashboard)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`