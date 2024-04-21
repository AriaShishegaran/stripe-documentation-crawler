htmlStripe LINK Cartridge Operations and Maintenance | Stripe Documentation[Skip to content](#main-content)Operations and Maintenance[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Foperations-and-maintenance)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Foperations-and-maintenance)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce B2C Commerce](/docs/connectors/salesforce-commerce-cloud)# Stripe LINK Cartridge Operations and Maintenance

Learn how to operate and maintain the Stripe LINK cartridge.## Data storage

The Stripe LINK cartridge extends Commerce Cloud to store several data points.

Customer profile: Stripe Customer ID, used to retrieve information about the customer’s record in your Stripe account.

- `stripeCustomerID(string)`- Store Stripe Customer ID

Order/basket custom attributes:

- `stripePaymentIntentID(String)`- Store PaymentIntent ID
- `stripeIsPaymentIntentInReview(Boolean)`- Store PaymentIntent in review

Payment transaction custom attributes:

- `stripeChargeId(string)`- Store Charge ID
- `stripeChargeOutcomeData(text)`- Store Charge outcome data
- `stripeClientSecret(string)`- Store client secret
- `stripeJsonData(text)`- Store webhook JSON data
- `stripeOrderNumber(number)`- Store order number
- `stripeSourceCanCharge(boolean)`- Store if Stripe Source can be charged
- `stripeSourceId(string)`- Store Stripe Source ID

Payment transaction custom attributes:

- `stripeChargeId(string)`- Store Charge ID
- `stripeCardID(string)`- Store card ID
- `stripeCustomerID(string)`- Store Customer ID
- `stripeDefaultCard(boolean)`- Store Stripe default card
- `stripeClientSecret(string)`- Store client secret
- `stripePRUsed(boolean)`- Store payment request button used
- `stripeSavePaymentInstrument(boolean)`- Store save payment instrument
- `stripeSourceID(string)`- Store Stripe Source ID

Custom objects: The custom objects are listed in the Business Manager. Navigate to Merchant Tools > Custom Objects > Custom Objects to see the list of custom objects.

- `StripeWebhookNotifications`

## Availability

Refer to the Stripe service level agreement to determine specific uptimes for the service. In case the service fails, no failover exists to allow transactions to proceed. Users receive a meaningful error message in this case.

## Failover and recovery process

If the Stripe service is unavailable, the user won’t be able to check out. You can track the service availability in SFCC using the Service Status.

## Support

If you experience problems or have recommendations for improvements, please contact Stripe Support.

## Upgrading the LINK cartridge

Before you upgrade, we recommend:

- Backing up your files and any other custom dependencies
- Installing the latest version from[LINK Marketplace](https://www.salesforce.com/products/commerce-cloud/partner-marketplace/partners/stripe/)in your test environment
- Testing the frontend UI and backend data integration
- Keeping a copy of any customizations you made to the module’s original code
- Porting over any customizations you made to the module’s code after upgrading and resolving any potential conflicts

## See also

- [Catridge user guide](/connectors/salesforce-commerce-cloud/user-guide)
- [Testing](/connectors/salesforce-commerce-cloud/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Data storage](#data-storage)[Availability](#availability)[Failover and recovery process](#failover-recovery-process)[Support](#support)[Upgrading the LINK cartridge](#upgrading-the-link-cartridge)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`