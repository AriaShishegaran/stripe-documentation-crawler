htmlInstall the Stripe Connector for Salesforce Order Management | Stripe Documentation[Skip to content](#main-content)Install the Stripe Connector for Salesforce Order Management[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management%2Finstallation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management%2Finstallation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce Order Management](/docs/connectors/salesforce-order-management)# Install the Stripe Connector for Salesforce Order Management

Set up and configure the Stripe Connector.## Installation

Use the following links to install the package into your Salesforce org. We recommend that you first install, set up, then test the app in a Salesforce sandbox environment before using it in your production org.

- [Production Package](https://login.salesforce.com/packagingSetupUI/ipLanding.app?apvId=04t6g000008Wod0)
- [Sandbox Package](https://test.salesforce.com/packagingSetupUI/ipLanding.app?apvId=04t6g000008Wod0)

Make sure Install for Admins Only is selected, then click Install.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-install.a95bc450897ae2c8fec49837590ce099.png)

Approve access to and from third-party websites. Check the grant access checkbox and click Continue.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-3p-access.fea0d91a0e164d00b01c288cbe51475e.png)

If the installation takes time, you will receive an email telling you the package is installed.

To verify, navigate to Setup > Apps > Packaging > Installed Packages and make sure the package is installed.

## Configuration

Instructions in the following sections detail how to configure your integration.

### Configure a Stripe Synchronous Payment Gateway Adapter

1. Follow the instructions in step 3 of Set Up a Synchronous Payment Gateway Adapter in Salesforce to create a payment gateway provider. Here’s the set of values we recommend for the payload:

`{
"ApexAdapterId": "Output of this Query: SELECT Id FROM ApexClass WHERE Name IN ('StripeAdapter')",
"DeveloperName": "StripeProvider",
"MasterLabel": " StripeProvider",
"IdempotencySupported": "No",
"Comments": "Stripe Synchronous Payment Gateway Adapter"
}`
2. Follow the instructions in step 4 of Set Up a Synchronous Payment Gateway Adapter in Salesforce to create a payment gateway record.

Recommended values:

Field LabelValueNameSALESFORCE_PAYMENTSMerchant Credential IDOutput of this query:`SELECT Id FROM NamedCredential WHERE DeveloperName = 'StripeAPI'`Payment Gateway ProviderOutput of the query (modify the query accordingly if your Stripe Synchronous Payment Gateway Provider is different than ‘StripeProvider’):`SELECT Id FROM PaymentGatewayProvider WHERE DeveloperName ='StripeProvider'`StatusActive

### Configure a Stripe Asynchronous Payment Gateway Adapter

1. Follow the instructions in Set Up an Asynchronous Payment Gateway Adapter in Salesforce to configure the Stripe Asynchronous Payment Gateway Adapter (skip step 2 and 3 if you’ve already executed the same for the Stripe Synchronous Payment Gateway Adapter). To create an asynchronous Payment Gateway Provider (follow step 4 from the previously linked instruction). Here is the recommended set of values for the payload:

`{
"ApexAdapterId": "Output of this Query: SELECT Id FROM ApexClass WHERE Name IN (‘StripeAsyncAdapter’)",
  "DeveloperName": "StripeAsyncAdapter",
  "MasterLabel": " StripeAsyncAdapterProvider ",
  "IdempotencySupported": "No",
  "Comments": "Stripe Asynchronous Payment Gateway Adapter"
  }`
2. Follow the instruction from step 5 (Create a payment gateway record) in Set Up an Asynchronous Payment Gateway Adapter in Salesforce to register the Stripe Asynchronous Payment Gateway record in Salesforce.

Here are the recommended values for the fields to be inserted (if you’re creating a gateway record for the first time) or updated (if you have already created a gateway record while setting up the synchronous payment gateway adapter)

Field LabelValueNameSALESFORCE_PAYMENTSMerchant Credential IDOutput of this query:`SELECT Id FROM NamedCredential WHERE DeveloperName = 'StripeAPI'`Payment Gateway ProviderOutput of the query (modify the query accordingly if your Stripe Synchronous Payment Gateway Provider is different than ‘StripeProvider’):`SELECT Id FROM PaymentGatewayProvider WHERE DeveloperName ='StripeAsyncAdapter'.`StatusActive
3. Follow the instructions in step 6 to configure the webhook URL for Stripe. The typical format of the webhook URL is a publicly accessible, HTTPS URL. For example: https://mydomainname.my.salesforce-sites.com/subdomain/services/data/v[Replace_ME_version]/commerce/payments/notify%20?provider=<ID>

`SELECT Id FROM PaymentGatewayProvider WHERE DeveloperName = ‘StripeAsyncAdapter’`[Replace_ME_version] with the API version of your org 49.0 and later


4. Use the following steps to register your webhooks URL in Stripe:

  1. Login to the[Stripe Dashboard](https://dashboard.stripe.com/dashboard).
  2. Go to the[Developers Dashboard](https://dashboard.stripe.com/developers).
  3. ClickWebhooks.
  4. ClickAdd Endpoint.
  5. Enter your webhooks URL, then add the following events:`charge.refunded`,`charge.succeeded`,`charge.captured`.


5. Click Add Endpoint.


6. Copy your webhook signing secret and save it for later use.



## Complete the configurations using Stripe OM Setup

Instructions in the following sections detail how to complete the configuration of your integration.

### Authorize the Stripe OMS Connector with your Stripe Account

In your Salesforce Order Management org, go through the Stripe Setup Assistant to connect your org to your Stripe account.

1. Click the App Launcher, then click View All.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-launch-app-launcher.abb6c08a1cde704115918ebaddfe3ff4.png)


2. Click Stripe OM Setup.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-launch-om-setup.d84d6c532e02356ab40073b2bec20f14.png)


3. Click Get Started.


4. Toggle live mode. We recommend leaving live mode disabled to test your Stripe integration without affecting your live data, and activating live mode when you’re ready to start processing real transactions with the Stripe Payment Gateway. Come back to this step and reauthorize your connection to switch between test mode and live mode. If you’re in live mode and you want to switch back to test mode, you don’t need to re-authorize.


5. Click Authorize.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-authorize.d4883cff2b90cce49e6054a05daa9079.png)

This allows Salesforce to access your Stripe data so you can capture and refund payments. The Stripe website opens to complete the authorization process, which might require you to enter login information or activate your Stripe account. When done, you’re redirected to this page to finish the setup process. After authorization is complete and successful, the following message displays:

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-authorize-complete.8ff6523255d2652a3dacaa56304c0090.png)

Store the webhook signing secret for Stripe asynchronous payment processing.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-store-wh-secret.9918a70a19d3886755228a68102c1979.png)

  1. Add the webhook signing secret value inSigning secret.
  2. ClickUpdate.
  3. A message appears on top to confirm successful insertion. ClickFinish.



### Modify existing order management flows

The authentication with Stripe is using OAuth, where Stripe is the OAuth provider. Salesforce doesn’t support Stripe as an OAuth provider, therefore the OAuth token is obtained using a custom integration, leveraging an invocable action getAccesToken. This is packaged as part of the Stripe OM Connector Managed Package.

Identify the flow that initiates the payment or refund to Stripe and include the getAccessToken invocable method in an action just before the Ensure Funds action in the flow (as shown in the following example). The flows that you need to modify varies from the one shown in the following example.

1. Navigate toSetup > Process Automation > Flows.
2. Select the activeFlowto use to capture funds.
3. Create a newActionthat calls the`getAccessToken`invocable method.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-generate-token.4e707e9311288fd5e7f6e93a47dc638d.png)

1. Make sure that theGet Access Tokenaction occurs before theCapture Fundsaction. After it completes, save a new version of thisFlowto make sure that your processes use the new version.

![](https://b.stripecdn.com/docs-statics-srv/assets/sfom-flowbuilder.22b239ea431eca499ef4cddd690ade94.png)

1. You can now use Stripe Payment as a payment method in your Order Management org. You can now place orders from Salesforce B2C Commerce Cloud and complete transactions, such as capture and refund transactions for payment methods that are associated with Salesforce commerce payments.

## Next steps

- [Operations and Maintenance](/connectors/salesforce-order-management/operations-and-maintenance)
- [Testing](/connectors/salesforce-order-management/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Installation](#installation)[Configuration](#configuration)[Complete the configurations using Stripe OM Setup](#complete-the-configurations-using-stripe-om-setup)[See also](#next-steps)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`