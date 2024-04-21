htmlStripe Connector for Salesforce Platform | Stripe Documentation[Skip to content](#main-content)Stripe Connector for Salesforce Platform[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fstripe-connector-for-salesforce%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fstripe-connector-for-salesforce%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)# Stripe Connector for Salesforce Platform

Access the full Stripe platform from within Salesforce with low and no-code tools.Build integrations between Salesforce and Stripe with the Stripe for Salesforce Platform. This connector enables you to:

- Seamlessly connect your Stripe account to your Salesforce org.
- Automatically map Stripe events to Salesforce events.
- Expose Stripe methods and objects natively in APEX and JavaScript code in Salesforce.
- Support low-code and no-code integrations using[Salesforce Flow](https://www.salesforce.com/products/platform/solutions/automate-business-processes/).

## Event mapping

Map events from Stripe to Salesforce.

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce_event_config.9bddcc789f3279db8ffd840826d17fa4.png)

Configure webhook events with a point and click configuration

## Stripe objects and methods natively available in Salesforce

Access Stripe objects and methods directly from Salesforce Apex and JavaScript. Salesforce Developers can gather data returned from any Stripe API call in a structured, repeatable way.

`public with sharing class CreateCustomerApp {
  public static void createCustomer() {
    List<Customer> customers = Stripe_CreateCustomer_v2020_08_27
  }
}`## Low and no-code integrations

Use Salesforce Flow to create no-code integrations and business workflows.

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce_flow_view.3e2bf3ddbbdb290d96e3f62082cb3079.png)

Build payments and business flows with Stripe and Salesforce

## See also

- [Installation guide](/plugins/stripe-connector-for-salesforce/installation-guide)
- [Enablement videos](/plugins/stripe-connector-for-salesforce/videos)
- [Configure events](/plugins/stripe-connector-for-salesforce/configure-events)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Event mapping](#event-mapping)[Stripe objects and methods natively available in Salesforce](#stripe-objects-and-methods-natively-available-in-salesforce)[Low and no-code integrations](#low-and-no-code-integrations)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`