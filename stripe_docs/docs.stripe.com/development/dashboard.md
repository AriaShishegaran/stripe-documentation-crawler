# Developers Dashboard

The Developers Dashboard collects information about each request in your account—use the Dashboard to view common integration errors, requests that failed, webhook events, and so on.

## Start with a guide

[View request logsLearn how to filter API request logs and view log entries in the Developers Dashboard.](/docs/development/dashboard/request-logs)

Learn how to filter API request logs and view log entries in the Developers Dashboard.

[View events and event object payloadsView events triggered by your account and their event object payload in the Developers Dashboard.](/docs/development/dashboard/events)

View events triggered by your account and their event object payload in the Developers Dashboard.

## Key features

Manage your Stripe integration from the Developers Dashboard. Find your default API version and all versions used by your account, or filter API request logs and view log entries.

Events are our way of letting you know when something interesting happens in your account. Use the Developers Dashboard and the Stripe CLI to setup a webhooks listener on your local machine, then trigger events to test your setup.

All accounts have a total of four keys: a publishable and secret key pair for test mode and live mode. Use the Developers Dashboard to expire an existing key, restrict traffic to an IP address, or create a restricted API key for microservices used by your application.

[test mode](/test-mode)

When you send an API request, we log one or more events for your account. Use the Developers Dashboard to view events triggered by your account so you know which events to monitor in your webhooks integration.
