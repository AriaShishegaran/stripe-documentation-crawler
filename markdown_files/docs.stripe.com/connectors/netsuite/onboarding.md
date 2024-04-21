htmlPrepare for onboarding | Stripe Documentation[Skip to content](#main-content)Prepare for onboarding[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fnetsuite%2Fonboarding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fnetsuite%2Fonboarding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[NetSuite](/docs/connectors/netsuite/overview)# Prepare for onboarding

Learn how to prepare your Stripe and NetSuite accounts for onboarding.### Get started

Contact us to get started with your implementation.

If you want to use the Stripe Connector for NetSuite, you must work with an official implementation partner to set up the connector.

Before you begin, make sure to prepare your Stripe and NetSuite accounts for onboarding using the guidance below.

### Prepare for onboarding

1. [Activate your Stripe account](/connectors/netsuite/onboarding#stripe-account)
2. [Set up a NetSuite test account](/connectors/netsuite/onboarding#netsuite-sandbox)
3. [Create a dedicated NetSuite user to operate the connector](/connectors/netsuite/onboarding#netsuite-user)
4. [Provide temporary admin access for the implementation partner](/connectors/netsuite/onboarding#admin-access)
5. (Optional)[Set up Stripe Billing](/connectors/netsuite/onboarding#stripe-billing)

## Activate your Stripe account

If you haven’t already, activate your Stripe account.

## Set up a NetSuite sandbox

We recommend setting up a NetSuite sandbox environment to test the connector. It’s possible to set up the connector to sync Stripe test data to your NetSuite production account. However, you must remember to manually delete the test data from the production instance.

## Create a dedicated NetSuite user

To prevent any settings changes from inadvertently affecting the connector’s ability to operate, we recommend creating a dedicated NetSuite user to operate the connector. With a dedicated user, you can also identify actions taken or changes made by that user in the NetSuite system log.

If you’re unable to provide a dedicated user, you can provide a shared user that isn’t used for other integrations. Any changes to that user can negatively impact the connector. For example, if you use an existing user login and that employee leaves the company, deleting their NetSuite user can break the connector and stop record syncing.

## Prepare to grant admin access

The implementation partner requires temporary admin access during onboarding for the following:

- Testing in the sandbox environment
- Implementing the connector live in production
- Troubleshooting issues specific to your NetSuite account

If you must restrict access, we recommend providing admin and GUI access in the sandbox environment, and then removing permissions before you move to production.

Your implementation partner can provide further instructions for granting access.

## (Optional) Set up Stripe Billing

If you use Stripe Billing and have existing Stripe prices and NetSuite items, you need to do the following to prepare for onboarding:

- Prepare a data sheet to map IDs for existing Stripe and NetSuite customers.
- Prepare a data sheet to map IDs for existing Stripe prices and NetSuite items.
- Determine the rule for the connector to use for NetSuite revenue recognition.
- Determine the start date to sync records.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Activate your Stripe account](#stripe-account)[Set up a NetSuite sandbox](#netsuite-sandbox)[Create a dedicated NetSuite user](#netsuite-user)[Prepare to grant admin access](#admin-access)[(Optional) Set up Stripe Billing](#stripe-billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`