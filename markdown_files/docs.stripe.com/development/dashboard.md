htmlDevelopers Dashboard | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdevelopment%2Fdashboard)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdevelopment%2Fdashboard)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)
[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Developer Dashboard# Developers Dashboard

Use the Developers Dashboard to view API request and event activity.The Developers Dashboard collects information about each request in your account—use the Dashboard to view common integration errors, requests that failed, webhook events, and so on.

## Start with a guide

[View request logsLearn how to filter API request logs and view log entries in the Developers Dashboard.](/docs/development/dashboard/request-logs)[View events and event object payloadsView events triggered by your account and their event object payload in the Developers Dashboard.](/docs/development/dashboard/events)## Key features

### Determine the reason a request failed

Manage your Stripe integration from the Developers Dashboard. Find your default API version and all versions used by your account, or filter API request logs and view log entries.

### Setup local webhook event listeners

Events are our way of letting you know when something interesting happens in your account. Use the Developers Dashboard and the Stripe CLI to setup a webhooks listener on your local machine, then trigger events to test your setup.

### Manage access to your application

All accounts have a total of four keys: a publishable and secret key pair for test mode and live mode. Use the Developers Dashboard to expire an existing key, restrict traffic to an IP address, or create a restricted API key for microservices used by your application.

### Monitor a webhooks integration

When you send an API request, we log one or more events for your account. Use the Developers Dashboard to view events triggered by your account so you know which events to monitor in your webhooks integration.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Start with a guide](#start-with-a-guide)[Key features](#key-features)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`