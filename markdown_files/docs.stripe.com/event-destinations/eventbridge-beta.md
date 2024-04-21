htmlSend Stripe events to Amazon EventBridge | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fevent-destinations%2Feventbridge-beta)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fevent-destinations%2Feventbridge-beta)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Send Stripe events to Amazon EventBridgeBeta

Join the private beta to get started consuming events in your existing AWS infrastructure.![Sign up to join the beta for EventBridge Event Destinations](https://b.stripecdn.com/docs-statics-srv/assets/eventbridge-eventdestinations-signup-banner.11418a99e95861ddcef8026ea418d356.png)

Use Event Destinations to send events directly to different destination types, including webhook endpoints, a local development machine, and now, Amazon EventBridge. With Amazon EventBridge support, your systems can consume Stripe events from EventBridge to enable business workflows, such as:

- Trigger the shipment of goods to a customer upon successful payment events
- Grant users access to specialized content when they upgrade their subscription plan
- Email your Connect account holders to update their bank account during a failed payout

Support for Amazon EventBridge is now in private beta. Sign up here to request access to join!By signing up, you're opting in to receive emails from Stripe about Event Destinations and other services that might interest you.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## Benefits of sending events to Amazon EventBridge

Use Amazon EventBridge as an event destination to integrate events with existing AWS infrastructure, increase business automation, and access event management tools:

- Integrate with existing infrastructure: Receive events from Stripe using Amazon Simple Queue Service (SQS) and Amazon Simple Notification Service (SNS). This removes the need to operate additional infrastructure as necessary for a webhook endpoint while leveraging AWS’s service availability.
- Create serverless orchestration workflows for business automation: Send your Stripe events from Amazon EventBridge to a Step Functions workflow to enable the creation of unique financial workflows with minimal development. Automate user notifications for failed payments, expired payment methods, or generate unique referral code coupons for new users.
- Access AWS enterprise-grade event management tools: Use Amazon EventBridge’s native tools to simplify event management and debugging. Amazon EventBridge allows the replay, archiving, batch processing, and monitoring of events without additional tooling.

## Enable event-driven architecture with Stripe events and Amazon EventBridge

An event-driven architecture is a software system pattern that provides near real-time responses to events. After Stripe events are delivered to Amazon EventBridge, they can be natively routed to over 20 supported targets that can process these events, including other AWS services, custom applications, and third-party services. This functionality enables you to scale, update, and deploy event consumer services independently, creating a robust architecture for your business logic.

Possible architectural patterns you can implement using Amazon EventBridge include:

- Trigger serverless functions with[Lambda](https://aws.amazon.com/lambda/): Send Stripe events from EventBridge to Lambda to trigger serverless compute functions, such as creating a shipping label after a payment succeeds.
- Enable event monitoring with[CloudWatch](https://aws.amazon.com/cloudwatch/): Send events from EventBridge to CloudWatch Logs to store events as log data that you can interactively search and analyze.
- Trigger low and no code workflows with[Step Functions](https://aws.amazon.com/step-functions/): Send events to a StepFunction workflow that trigger your business scenarios, such as notifying your customers that their trial is about to end.
- Fan out events to internal systems with[SNS](https://aws.amazon.com/sns/)or[SQS](https://aws.amazon.com/sqs/): Send Stripe events to SNS or SQS to fan out Stripe event data to your internal teams so they can own and process them.

## Access new developer tooling to manage your event destinations

During the private beta, you also gain access to the following tools:

- [Workbench](https://workbench.stripe.dev/): Replacing the Developer Dashboard, Workbench becomes your central hub for all developer tools. Use these features to debug, create, test, and manage both your integration and event destinations.
- Sandboxes: Create multiple isolated environments for testing your integration and event destinations.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Benefits of sending events to Amazon EventBridge](#benefits-of-sending-events-to-amazon-eventbridge)[Enable event-driven architecture with Stripe events and Amazon EventBridge](#enable-event-driven-architecture-with-stripe-events-and-amazon-eventbridge)[Access new developer tooling to manage your event destinations](#access-new-developer-tooling-to-manage-your-event-destinations)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`