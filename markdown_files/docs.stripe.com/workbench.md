htmlWorkbench | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworkbench)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworkbench)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)
[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)# WorkbenchBeta

Use Workbench to build, manage, and debug your Stripe integration.BetaTo use Workbench, enable it for your user login from the Early access features in the Dashboard.

Workbench provides developer tools to help you build, manage, and debug your Stripe integration from your browser, anywhere in the Dashboard. For example, using Workbench you can:

- Review a summary of recent integration errors
- Inspect API objects, request logs, events, and webhook deliveries
- Run API requests using the built-in command-line environment, or build them with the API Explorer
- Create and manage your webhook endpoint configuration

Share your ideas: improve Workbench by clicking Share feedback at the top of the tool with feature requests, bug reports, and feedback.

## Get started

To use Workbench, you need a Stripe account and to enable the beta from Early access features in the Dashboard. Only users with the Administrator or Developer role have full access to all Workbench tools.

1. Sign in to the[Dashboard](https://dashboard.stripe.com/). From theDevelopersmenu, clickWorkbench.
2. You can drag the top handle of the Workbench pane to resize it, or you can click the maximize icon () to leave or enter full-screen mode.
3. Click the minimize icon () to collapse Workbench to a taskbar at the bottom of the page, or the expand icon () to reopen the pane. The taskbar lets you quickly inspect API objects and includes a notification tray that alerts you to critical API errors and event activity.
4. To hide the Workbench taskbar, click the collapse icon () to minimize the taskbar to an icon on the right of the Dashboard. Hover over the icon to display the notification tray. Click the icon to reopen the full Workbench pane.



Workbench includes multiple tools in each tab. Learn more about the functionality of each tab and how to use it below.

NoteTo open or minimize Workbench from anywhere in the Dashboard, press the tilde key (~) on your keyboard.

### Use Workbench tools

While using Workbench, keep these tools in mind:

- ClickCopy linkto generate a shareable URL of the current Workbench view.
- ClickSend feedbackto share ideas or questions with the core development team.

## Overview of your Stripe integration

See an overview of your account’s API activity in the Overview tab.

- TheIntegration statuswidget displays any known service degradations in Stripe’s infrastructure.
- TheAPI keyswidget displays a list of standard and restricted keys on your account. ClickManageto create or update your API keys.
- TheAPI versionswidget displays a breakdown of the API versions that recent API requests to your account used. ClickUpgrade availableto[upgrade the default API version](/upgrades#how-can-i-upgrade-my-api)of your Stripe account.
- TheAPI requestsandWebhooksgraphs visualize recent API activity on your account.
- Integration insightsdisplays actionable improvements you can make to your Stripe account to resolve errors, improve performance, or better use Stripe APIs.

![](https://b.stripecdn.com/docs-statics-srv/assets/workbench-overview.82e64e4151ee0da510e97050956b1a96.png)

The Overview tab shows a quick snapshot of your account’s API activity.

## View recent errors

The Errors tab summarizes recent errors for your Stripe account. You can learn more about how to resolve each type of API error, and review recent API request logs for each error.

![](https://b.stripecdn.com/docs-statics-srv/assets/workbench-errors.f9bc5a18ecacc6f161ebc9cd2a8d9f0a.png)

The Errors tab summarizes recent API errors and highlights related request logs.

## Use the Inspector to learn about API objects

Use the Inspector to explore a JSON view of API objects on your Stripe account. To inspect an object, you can:

- Enter an object ID from theInspectortab.
- Enter an object ID from the Workbench taskbar.
- Visit a Dashboard page for any object (for example, a`Payment`,`Customer`, or`Subscription`) and open theInspectortab.

![](https://b.stripecdn.com/docs-statics-srv/assets/workbench-inspector.132a139ddb20906e606a39d4eaf51af5.png)

The Inspector shows a JSON view of the API object, and any related request logs and events.

The Inspector tab displays all related API objects on the left, and a JSON view in the Overview tab. The Logs and Events tabs show related API activity to this object.

## View API request logs

The Logs tab includes a list of recent API requests and responses for your Stripe account. Workbench highlights recent errors with suggestions on how to resolve them. You can filter API requests by:

- Date of the request
- HTTP status (for example,`200`)
- HTTP method (for example,`POST`or`DELETE`)
- API endpoint (for example,`/v1/checkout/sessions`)
- IP address that created the request
- Source (direct API requests or Dashboard)
- Account (or specifically when using Connect, the platform or connected accounts)
- API version (for example,`2020-08-27`)
- Error code (for example,`resource_missing`)
- Error type (for example,`invalid_request_error`)
- Error parameter (for example,`line_items[*][price]`)

Workbench doesn’t automatically refresh this tab in real-time as your account receives new API requests. Click Refresh logs to fetch the latest request logs from your Stripe account.

![](https://b.stripecdn.com/docs-statics-srv/assets/workbench-logs.eca1ad610d58aa7493eff9d064a659d9.png)

The Logs tool presents a timeline of API activity, with filters for time endpoint, response code, and other properties.

## Review recent events on your Stripe account

The Events tab includes a list of recent events on your Stripe account. Click Refresh events to fetch the latest events from your Stripe account. You can filter events by:

- Date of the event
- Delivery status (delivered or failed)
- Event type (for example,`customer.subscription.created`; you can also use wildcards (for example,`customer.*`)
- API resource (for example,`cus_123`)

Click an event in the list on the left to review the event’s details, payload, and attempted deliveries on the right. Learn more about setting up webhook endpoints with Workbench.

![](https://b.stripecdn.com/docs-statics-srv/assets/workbench-events.45cfc616e1e6b03ac93673581b47b8ba.png)

The Events tab shows recent activity on your Stripe account. Events can be delivered to webhook endpoints.

The Delivery attempts section lists attempted deliveries of the event (for example, to a webhook endpoint). Workbench might list multiple delivery attempts if the initial attempts failed. Stripe automatically retries delivery in live mode several times. Click Retry now to manually attempt to redeliver the event.

## Set up a webhook endpoint

The  Webhooks  tab allows you to create a new  webhook endpoint  for Stripe to deliver events to:

- URL endpoints using webhooks
- Your local machine using the[Stripe CLI](/stripe-cli)

Click Create new endpoint to configure a new webhook endpoint that Stripe sends events to. Select the API version that Stripe uses to generate webhook events and the event types to listen for, and specify an HTTPS URL where your server hosts the webhook endpoint.

On the left, Workbench lists any configured webhook endpoints. The Overview summarizes the activity on that configured endpoint, and Event deliveries provides a complete list of attempts by Stripe to deliver events to that endpoint. Click Retry now next to any delivery attempt so Stripe can redeliver the event to that endpoint.

![](https://b.stripecdn.com/docs-statics-srv/assets/main.a385ccd665e5fbafa035600ecee9021a.png)

Set up a new webhook endpoint or route events to your local development machine.

## Run API commands using Shell and Explorer

Shell provides a command-line interface to manage your Stripe resources within Workbench, similar to the Stripe CLI. See Shell and API Explorer for the full list of available commands.

NoteShell is read-only in live mode. Switch to test mode to run API requests that create, modify, or delete API objects.

When using Workbench, a minimal Shell is always available in the pane, or you can use the Shell tab to launch a full-screen session. From the Shell tab, click New pane to split the pane into multiple shell sessions.

Click API Explorer to reveal the interactive command builder on the right. Choose the API resource and HTTP method to show the required and optional parameters for that request. The Headers tab allows setting some HTTP headers, such as the Stripe-Account header which allows making API requests to a connected account. Click Run to execute the API request.

Filling in parameters in the API Explorer automatically constructs the corresponding Shell command. Select a programming language, then click Print SDK request to see the corresponding SDK code for the API request.

![](https://b.stripecdn.com/docs-statics-srv/assets/workbench-shell.bda499755fff63eadcbcc0c90c7a70f1.png)

Shell and the API Explorer help you experiment with Stripe’s API from Workbench.

## Next steps

- [Set up a webhook endpoint](/workbench/webhooks)
- [Try the Shell and API Explorer](/workbench/shell)
- [Keyboard shortcuts in Workbench](/workbench/keyboard-shortcuts)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Overview of your Stripe integration](#overview-of-your-stripe-integration)[View recent errors](#view-recent-errors)[Use the Inspector to learn about API objects](#use-the-inspector-to-learn-about-api-objects)[View API request logs](#view-api-request-logs)[Review recent events on your Stripe account](#review-recent-events-on-your-stripe-account)[Set up a webhook endpoint](#set-up-a-webhook-endpoint)[Run API commands using Shell and Explorer](#run-api-commands-using-shell-and-explorer)[Next steps](#next-steps)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`