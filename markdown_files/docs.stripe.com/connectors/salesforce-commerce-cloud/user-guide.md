htmlStripe Salesforce Commerce Cloud Cartridge user guide | Stripe Documentation[Skip to content](#main-content)User Guide[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Fuser-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Fuser-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce B2C Commerce](/docs/connectors/salesforce-commerce-cloud)# Stripe Salesforce Commerce Cloud Cartridge user guide

Learn how to use the Stripe Salesforce Commerce Cloud Cartridge.## Merchant roles and responsibilities

As soon as configurations and job schedules are set up, the functionality runs on demand—the merchant doesn’t need to perform any ongoing maintenance or other tasks.

## Business Manager

Business Manager settings and configuration notes are described in detail in the implementation guide.

The cartridge comes with two jobs:

- Stripe - Delete Custom Objects
- Stripe - Process Webhook Notifications

Enable the Stripe - Process Webhook Notifications job for the desired site:

![](https://b.stripecdn.com/docs-statics-srv/assets/userguide-siteassignments.6e5f58df010141fb6b2e306dff0d2db0.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/userguide-notifications.e53f68c90c668d89feb1ba7bf4976344.png)

## Storefront functionality

### Saved credit cards

When an authenticated customer selects a saved credit card on the payment page, they can see a list of their Stripe-saved payment sources as radio buttons rather than the default SiteGenesis select options.

![](https://b.stripecdn.com/docs-statics-srv/assets/storefront-payment.b41658955e3b7ea13a0ee9f3e0fd9795.png)

### Payment request button

After a customer saves their address and credit card information in their browser, they see the payment request button (Pay now).

![](https://b.stripecdn.com/docs-statics-srv/assets/storefront-paynow.f5e387d720260d6d4dc1a27faed5a31a.png)

The customer sees Pay now or an Apple Pay button, depending on what their device and browser combination supports.

## See also

- [Testing](/connectors/salesforce-commerce-cloud/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Merchant roles and responsibilities](#merchant-roles-and-responsibilities)[Business Manager](#business-manager)[Storefront functionality](#storefront-functionality)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`