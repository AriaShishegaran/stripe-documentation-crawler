htmlSet up a webhook endpoint with Workbench | Stripe Documentation[Skip to content](#main-content)Set up a webhook endpoint[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworkbench%2Fwebhooks)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworkbench%2Fwebhooks)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)
[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Workbench](/docs/workbench)# Set up a webhook endpoint with WorkbenchBeta

Use Workbench to set up a webhook endpoint and receive events from Stripe.Read the complete guide to webhook events for a high-level overview and best practices on receiving events about your Stripe account.

This guide describes how to set up a webhook endpoint using Workbench.

## Register a webhook endpoint with Workbench

To register a webhook endpoint in Workbench:

1. OpenWorkbenchin the[Dashboard](https://dashboard.stripe.com/), then click theWebhookstab.
2. ClickRegister a new webhook endpoint.
3. Select the API version for the[events object](/api/events)you want to consume.
4. If you’re using[Connect](/connect), you can listen forEvents on connected accounts. Otherwise, chooseEvents on your account.
5. Select the[event types](/api/events/types)that you want to send to a webhook endpoint, then clickContinue.
6. Provide theEndpoint URLfor Stripe to send webhooks to and an optional description for the endpoint.
7. ClickCreate destinationto create your webhook endpoint.

![Register a new webhook endpoint in the Webhooks tab](https://b.stripecdn.com/docs-statics-srv/assets/create-webhook-endpoint.92271ebcb6d3c1f936baaeeda36feafc.png)

Register a new webhook endpoint in the Webhooks tab

## Configure an existing webhook endpoint

You can update or delete existing webhook endpoints in the Workbench Webhooks tab. You can also temporarily disable a registered webhook endpoint. Stripe won’t attempt to resend any events generated while the respective webhook endpoint is disabled. You can also manage webhook endpoints programmatically.

## View event deliveries

### Listening with Stripe CLI

You can also use the Stripe CLI to listen for events directly in your terminal.

To view event deliveries, select the webhook endpoint in Webhooks, then select the Event deliveries tab.

The Event deliveries tab provides a list of events and whether they’re Delivered, Pending, or Failed. Click an event to view the Delivery attempts, which includes the HTTP status code of previous delivery attempts and the time of pending future deliveries.

![View event delivery attempts on a webhook endpoint's Event deliveries tab](https://b.stripecdn.com/docs-statics-srv/assets/view-event-deliveries.375483a863ab143a0e92f01fa01c14b0.png)

View event delivery attempts on a webhook endpoint’s Event deliveries tab.

## Retry sending an event

In live mode, Stripe attempts to deliver a given event to your webhook endpoint for up to 3 days with an exponential back off. In the Event deliveries section of your webhook endpoint listed on Workbench, you can view when the next retry will occur.

In test mode, Stripe retries three times over a few hours. You can manually retry transmitting individual events to your webhook endpoint after this time using the Workbench Webhooks tab by navigating to the Event deliveries listed for your desired endpoint. You can also query for missed events to reconcile the data over any time period.

![Retry sending events using a webhook endpoint's Event deliveries tab](https://b.stripecdn.com/docs-statics-srv/assets/retry-failed-event-deliveries.225753ebf217cd1e9d0798f0c6f0a198.png)

Retry sending events using a webhook endpoint’s Event deliveries tab.

## See also

- [Interactive webhook endpoint builder](/webhooks/quickstart)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Register a webhook endpoint with Workbench](#register-webhook-workbench)[Configure an existing webhook endpoint](#manage-webhook)[View event deliveries](#view-events)[Retry sending an event](#retries)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`