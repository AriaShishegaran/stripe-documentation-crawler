htmlTesting the Stripe Connector for Salesforce Order Management | Stripe Documentation[Skip to content](#main-content)Testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce Order Management](/docs/connectors/salesforce-order-management)# Testing the Stripe Connector for Salesforce Order Management

Best practices for testing your Stripe Connector and Salesforce B2C Commerce integration.Use the following steps to test your integration:

- In the Stripe Dashboard, toggle from live mode to test mode.
- Raise an order from Salesforce B2C Commerce Cloud.
- After the order is in the Salesforce Order Management environment, complete the required steps based on your mapped business process in SFOMS to fulfill the order or refund an order. Depending on your test case, this translates to triggering either of the flow core actions for order management –[Ensure Funds Async](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_om_actions_ensure_funds_async.htm&type=5)or[Ensure Refunds Async](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_om_actions_ensure_refunds_async.htm&type=5).
- Verify the status of your payment in the Stripe Dashboard, and check the payment gateway logs against the order payment summary.
- If the outcome is as expected, toggle from test mode to live mode. Reauthorize with Stripe, if required.
- If you are experiencing any issues, contact Stripe Support.

If your storefront is hosted on a Salesforce B2C environment, you should have an account.demandware.com login and Business Manager access through the following URL: https://production.demandware.net/on/demandware.store/Sites-Site.

## Verify that  Salesforce Commerce Cloud cartridge can collect payments with Stripe or Salesforce payments on Commerce Cloud

Log in to your Business Manager:

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-verify-sfccb2c-1.213aaa94fd257b4e1c3a7a4e1f371e26.png)

Alternatively:

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-verify-sfccb2c-2.f84e63eb561d5a36669ab0e5bb9e1172.png)

## Verify that your integration is enabled between SalesforceB2C Commerce Cloud and Salesforce Order Management

1. In your Salesforce Order Management org, navigate toSetup > Home > Feature Settings > Order Management![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-verify-sfcc-om-1.2eedd5483a7fae74fc94ebba9667b83a.png)


2. Then use the following route:Setup > Home > Feature Settings > Connect to B2C Commerce > Manage Cloud-to-Cloud Connections![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-verify-sfcc-om-2.fbcb617ab3d23a05ee262a157b1f91c9.png)



## Verify access to the CommercePayments API enabled by the PaymentPlatform org permission

You can validate whether you have access using one of the following methods.

Confirm whether you’ve been assigned any of the following licenses:

- Salesforce Order Management
- Salesforce B2B
- Salesforce B2C

Using the following route in Setup > Home > Company Information > Permission Set Licenses, check for Commerce User (CommerceUserPsl), Lightning Order Management User (LightningOrderManagementUserPsl), B2B Buyer Permission Set One Seat (B2BBuyerPsl), B2B Buyer Manager Permission Set One Seat (B2BBuyerManagerPsl).

## Verify the org API version

Refer to this help document: https://help.salesforce.com/s/articleView?id=000334996&type=1.

## Get logs of payments and refunds in Salesforce

You can view logs for transactions made through the Salesforce Platform by navigating to Order Summary Record > Order Payment Summary Record > Gateway Logs in the Related tab. If you don’t see the gateway logs in the Related tab, contact your Salesforce administrator and include the gateway logs in the page layout.

You can also execute this SOQL in developer console or SOQL Builder in VSCode (Apply filters as required OrderPaymentSummaryId or ReferencedEntityId):

`SELECT Id, OrderPaymentSummaryId, ReferencedEntityId,Request, Response, SfRefNumber, SfResultCode, GatewayRefNumber, GatewayAuthCode, GatewayDate, GatewayMessage, GatewayResultCode, GatewayResultCodeDescription, InteractionStatus FROM PaymentGatewayLog`The ReferencedEntityId is a polymorphic field that points to a payment or refund record.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Verify that  Salesforce Commerce Cloud cartridge can collect payments with Stripe or Salesforce payments on Commerce Cloud](#verify-that-salesforce-commerce-cloud-cartridge-can-collect-payments-with-stripe-or-salesforce-payments-on-commerce-cloud)[Verify that your integration is enabled between SalesforceB2C Commerce Cloud and Salesforce Order Management](#verify-that-your-integration-is-enabled-between-salesforceb2c-commerce-cloud-and-salesforce-order-management)[Verify access to the CommercePayments API enabled by the PaymentPlatform org permission](#verify-access-to-the-commercepayments-api-enabled-by-the-paymentplatform-org-permission)[Verify the org API version](#verify-the-org-api-version)[Get logs of payments and refunds in Salesforce](#get-logs-of-payments-and-refunds-in-salesforce)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`