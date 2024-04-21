# Send Stripe events to Amazon EventBridgeBeta

Use Event Destinations to send events directly to different destination types, including webhook endpoints, a local development machine, and now, Amazon EventBridge. With Amazon EventBridge support, your systems can consume Stripe events from EventBridge to enable business workflows, such as:

- Trigger the shipment of goods to a customer upon successful payment events

- Grant users access to specialized content when they upgrade their subscription plan

- Email your Connect account holders to update their bank account during a failed payout

[privacy policy](https://stripe.com/privacy)

## Benefits of sending events to Amazon EventBridge

Use Amazon EventBridge as an event destination to integrate events with existing AWS infrastructure, increase business automation, and access event management tools:

- Integrate with existing infrastructure: Receive events from Stripe using Amazon Simple Queue Service (SQS) and Amazon Simple Notification Service (SNS). This removes the need to operate additional infrastructure as necessary for a webhook endpoint while leveraging AWS’s service availability.

- Create serverless orchestration workflows for business automation: Send your Stripe events from Amazon EventBridge to a Step Functions workflow to enable the creation of unique financial workflows with minimal development. Automate user notifications for failed payments, expired payment methods, or generate unique referral code coupons for new users.

- Access AWS enterprise-grade event management tools: Use Amazon EventBridge’s native tools to simplify event management and debugging. Amazon EventBridge allows the replay, archiving, batch processing, and monitoring of events without additional tooling.

## Enable event-driven architecture with Stripe events and Amazon EventBridge

An event-driven architecture is a software system pattern that provides near real-time responses to events. After Stripe events are delivered to Amazon EventBridge, they can be natively routed to over 20 supported targets that can process these events, including other AWS services, custom applications, and third-party services. This functionality enables you to scale, update, and deploy event consumer services independently, creating a robust architecture for your business logic.

[20 supported targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html)

Possible architectural patterns you can implement using Amazon EventBridge include:

- Trigger serverless functions with Lambda: Send Stripe events from EventBridge to Lambda to trigger serverless compute functions, such as creating a shipping label after a payment succeeds.

[Lambda](https://aws.amazon.com/lambda/)

- Enable event monitoring with CloudWatch: Send events from EventBridge to CloudWatch Logs to store events as log data that you can interactively search and analyze.

[CloudWatch](https://aws.amazon.com/cloudwatch/)

- Trigger low and no code workflows with Step Functions: Send events to a StepFunction workflow that trigger your business scenarios, such as notifying your customers that their trial is about to end.

[Step Functions](https://aws.amazon.com/step-functions/)

- Fan out events to internal systems with SNS or SQS: Send Stripe events to SNS or SQS to fan out Stripe event data to your internal teams so they can own and process them.

[SNS](https://aws.amazon.com/sns/)

[SQS](https://aws.amazon.com/sqs/)

## Access new developer tooling to manage your event destinations

During the private beta, you also gain access to the following tools:

- Workbench: Replacing the Developer Dashboard, Workbench becomes your central hub for all developer tools. Use these features to debug, create, test, and manage both your integration and event destinations.

[Workbench](https://workbench.stripe.dev/)

- Sandboxes: Create multiple isolated environments for testing your integration and event destinations.
