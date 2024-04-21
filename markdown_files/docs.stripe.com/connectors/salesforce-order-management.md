htmlStripe Connector for Salesforce Order Management | Stripe Documentation[Skip to content](#main-content)Salesforce Order Management[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)# Stripe Connector for Salesforce Order Management

Learn about the Stripe Connector for Salesforce Order Management.The Stripe Connector for Salesforce Order Management is a managed package that you install on top of Order Management to enable payment capture and refund for the order servicing supported use cases. It comes with both an asynchronous and synchronous adapter to handle payments and refunds.

## Before you begin

1. A storefront hosted on Salesforce B2C Commerce Cloud and Salesforce Order Management on the Salesforce Core Platform.
2. Salesforce Commerce Cloud cartridge for collecting payments with StripeorSalesforce payments on Commerce Cloud.
3. An integration enabled between SalesforceB2C Commerce Cloud and Salesforce Order Management.
4. Access to CommercePayments API enabled by the PaymentPlatform org permission.
5. Salesforce CommercePayments is only available for orgs with API version 49.0 and later. Commerce Payments is only available in the Lightning Experience.

## Core concepts

### PaymentIntent

A PaymentIntent is a Stripe term that refers to a transaction created at Stripe to track a payment from creation through the checkout process, which might trigger additional authentication steps. You do this by implementing the Payment Intents API. Locate the payment intent in Salesforce Order Management by locating the Gateway Reference Number (GatewayRefNumber) field against the payment authorization record for an order summary.

### Payment authorization

A payment authorization is relevant to both Stripe and the Salesforce OMS. An authorized amount is a sum that a business transmits to a credit or debit card processor to make sure a customer has sufficient funds to complete a purchase—the approved amount of money to be charged.

There are two capture modes in the Stripe LINK cartridge for Salesforce B2C Commerce Cloud—authorize and capture. If the LINK cartridge is set up to authorize a payment during checkout, then Salesforce Order Management creates a payment authorization record. You can view the payment authorization against an order summary using this route:

Order Summary Record > Order Payment Summary Record > Payment Authorizations in Related Tab

If you don’t see Refunds in the Related tab, contact your Salesforce administrator and include the payment authorization related list in the page layout (as shown):

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-payment-auth-sc1.bb4f7cb8c5bce6a76d45fa975c210894.png)

The PaymentIntent ID (pi_XXXXXX) at Stripe is stored in the Gateway Reference Number (GatewayRefNumber) field of the payment authorization record. The Processing Mode (ProcessingMode) is set as External, which implies that the payment authorization was processed outside the Salesforce payment platform.

### Payment

If the capture mode in the Stripe LINK cartridge is set to Capture, then the payment is captured from the customer. In this case, a payment record is created in Salesforce Order Management. You can view the payment against an order summary using this route:

Order Summary Record > Order Payment Summary Record > Payments in Related Tab

If you don’t see Refunds in the Related tab, contact your Salesforce administrator and include the payments related list in the page layout (as shown):

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-payment-sc1.8c48be7fc8849db13914a5f363fba750.png)

### Balance Transaction ID

The Balance Transaction ID (txn_XXXXXXXXX) against the PaymentIntent (pi_XXXXXX) at Stripe is stored in the Gateway Reference Number (GatewayRefNumber) field. The Processing Mode (ProcessingMode) field value is set as External, which means the payment was processed outside the Salesforce payment platform. In the event the payment was authorized in Salesforce B2C Commerce Cloud Storefront, and the amount was captured in Salesforce OMS later, the payment record is represented as shown:

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-baltxn-sc1.7eae0d579cb7f583f4270517d7bd5ab3.png)

The Salesforce Payment Gateway ID (SFXXXXX) against the Payment Intent (pi_XXXXXX) at Stripe is stored in the Gateway Reference Number (GatewayRefNumber) field. The Processing Mode (ProcessingMode) field value is set as Salesforce, which implies that the payment was processed by the Salesforce payment platform.

### Refund

If a refund is initiated from Salesforce OMS, you can trace it to a Refund record by following this route:

Order Summary Record > Order Payment Summary Record > Refunds (in the Related tab)

If you don’t see Refunds in the Related tab, contact your Salesforce administrator and include the Refunds related list in the page layout (as shown):

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-refund-sc1.6ac94b1ed3162b35735ca3bbf0e6bd70.png)

The Salesforce Payment Gateway ID (SFXXXXX) is stored in the Gateway Reference Number (GatewayRefNumber) field. The Processing Mode (ProcessingMode) is set as Salesforce, which implies that the refund was processed by the Salesforce payment platform.

### Payment gateway logs

You can view logs for the transactions made with the Salesforce Platform by navigating to Order Summary Record > Order Payment Summary Record > Gateway Logs in the Related tab. If you don’t see the gateway logs in the Related tab, contact your Salesforce administrator and include the gateway logs in the related page layout, or execute this SOQL in Developer Console or SOQL Builder in VS Code:

`SELECT Id, OrderPaymentSummaryId, ReferencedEntityId, Request, Response, SfRefNumber, SfResultCode, GatewayRefNumber, GatewayAuthCode, GatewayDate, GatewayMessage, GatewayResultCode, GatewayResultCodeDescription, InteractionStatus FROM PaymentGatewayLog`## See also

- [Component Overview](/connectors/salesforce-order-management/overview)
- [Installation Guide](/connectors/salesforce-order-management/installation)
- [Operations and Maintenance](/connectors/salesforce-order-management/operations-and-maintenance)
- [Testing](/connectors/salesforce-order-management/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Core concepts](#core-concepts)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`