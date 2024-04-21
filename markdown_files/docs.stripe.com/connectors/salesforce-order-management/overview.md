htmlHow the Connector for Salesforce Order Management works | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-order-management%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce Order Management](/docs/connectors/salesforce-order-management)# How the Connector for Salesforce Order Management works

Learn about the key components of the Stripe Connector for Salesforce Order Management.The managed package contains the following key components needed for a configuration. After installation you can verify this setup by running the queries either through the developer console or SOQL Builder in VS Code.

1. StripeAPI the named credential.

Execute the following query using the developer console or SOQL Builder in VSCode:

`SELECT Id, DeveloperName, Endpoint FROM NamedCredential WHERE DeveloperName = 'StripeAPI'`
2. Use the required Apex classes configured as the bridge between the Payments Platform in Salesforce and the Stripe Payment Gateway: StripeAdapter, StripeAsyncAdapter. These Apex classes for the synchronous and asynchronous adaptors respectively are for processing payments between Salesforce Order Management and Stripe.

Execute the following query using the developer console or SOQL Builder in VS Code:

`SELECT Id, Name, NamespacePrefix FROM ApexClass WHERE Name IN ('StripeAdapter','StripeAsyncAdapter')`
3. Apply any required protected custom settings to store authentication secrets for the transactional calls to the Stripe Payment Gateway.


4. Use an invocable Apex method (getAccesToken) to obtain the OAuth token for integration purposes.


5. Use Lightning Pages required to authorize the Salesforce Connector in the subscribing org and Stripe Payment Gateway.



## Next steps

- [Installation Guide](/connectors/salesforce-order-management/installation)
- [Operations and Maintenance](/connectors/salesforce-order-management/operations-and-maintenance)
- [Testing](/connectors/salesforce-order-management/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`