htmlView API request logs | Stripe Documentation[Skip to content](#main-content)View request logs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdevelopment%2Fdashboard%2Frequest-logs)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdevelopment%2Fdashboard%2Frequest-logs)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)
[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Developer Dashboard# View API request logs

Filter API request logs and view log entries in the Developers Dashboard.When you send an API request, Stripe creates an object and logs the request for your account. This page describes how to filter API request logs and view log entries for your account in the Developers Dashboard.

## How requests are logged

This table describes the different ways Stripe logs an API request for your account.

SourceAPI callLogsAPIWhen you manually trigger an event with the Stripe CLI.Logs the API call on the[Logs](https://dashboard.stripe.com/logs)page.APIWhen user actions in your app or website result in an API call.Logs the API call on the[Logs](https://dashboard.stripe.com/logs)page.APIWhen you call an API directly with the Stripe CLI.Logs the API call on the[Logs](https://dashboard.stripe.com/logs)page.DashboardWhen you call an API by modifying your Stripe resources in the Dashboard.Logs the API call on the[Logs](https://dashboard.stripe.com/logs)page.## View your default API version

When you send requests to Stripe, you may specify an API version with the Stripe-Version header. If you don’t specify an API version, Stripe uses your account’s default API version. Use these steps to find all of the API versions used by your account within the last week. If you’re using the latest API version, the version is labeled Latest.

1. Open the[Developers Dashboard](https://dashboard.stripe.com/developers).
2. Your account’s defaultAPI versionis labeled`Default`.

To view a list of versions, see the API changelog.

## View API requests by source

Use these steps to filter requests by an API call source.

1. Open the[Logs](https://dashboard.stripe.com/logs)page.
2. ClickMore.
3. InSource, selectDashboardorAPIto filter requests by source.
4. ClickApply.

## Find common integration errors

Use this filter to discover common integration errors by error code and API endpoint.

1. Open the[Developers Dashboard](https://dashboard.stripe.com/).
2. InRecent errors, select the filter button ().
3. Select an error type.
4. Click an error to view the request payload that failed and the reason.

## Filter by resource ID

When you create, update, or delete a Stripe resource using Stripe APIs, Stripe returns a resource ID in the response payload. For example, when you Create a customer, Stripe returns a customer ID (in id), such as cus_ImZZa3EEvvQQQU. Use these steps to filter API requests by resource ID.

1. Open the[Logs](https://dashboard.stripe.com/logs)page.
2. Enter the resource ID in theFilter by resourceID text field.

## Apply advanced filters

You can use the inline navigation to filter API requests by Date, Status, Method and API endpoint, or apply additional filters to troubleshoot requests. Use these steps to filter API requests by API version, error type, error code, and other filters, such as an IP address.

1. Open the[Logs](https://dashboard.stripe.com/logs)page.
2. ClickMore.  - To filter by version, select an option in theAPI versiondropdown menu. For example,`2024-04-10`.
  - To filter by error type, select an option in theError typedropdown menu. For example,`card_error`.
  - To filter by error message, select an option in theError codedropdown menu. For example,`bank_account_unverified`.


3. ClickApply.

![Filter by API version](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-api-version.2db0c042c6ecb829a34870d93a452aa1.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How requests are logged](#how-requests-are-logged)[View your default API version](#view-your-default-api-version)[View API requests by source](#view-api-requests-by-source)[Find common integration errors](#find-common-integration-errors)[Filter by resource ID](#filter-by-resource-id)[Apply advanced filters](#apply-advanced-filters)Products Used[Sigma](/stripe-data/access-data-in-dashboard)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`