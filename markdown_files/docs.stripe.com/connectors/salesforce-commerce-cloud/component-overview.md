htmlInstall Stripe Connector for Salesforce B2C Commerce Shopfront Reference Architecture | Stripe Documentation[Skip to content](#main-content)Component Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Fcomponent-overview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Fcomponent-overview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce B2C Commerce](/docs/connectors/salesforce-commerce-cloud)# Install Stripe Connector for Salesforce B2C Commerce Shopfront Reference Architecture

Learn about the Stripe Connector for Salesforce Commerce Cloud Shopfront architecture.### Stripe Payment Element

Stripe Payment Element modifies the default Commerce Cloud credit card collection and processing by using Stripe.js, a JavaScript library, to securely tokenize credit card data. Payments are then processed using the tokenized data, instead of raw credit card information.

During checkout, the cartridge creates a PaymentIntent for any new cards or alternate payment methods that a customer enters. This tokenized data generates a Stripe Charge at the point of purchase.

### Stripe.js sources

When customers enter credit card or other payment information on the storefront, Stripe.js tokenizes it in interactions between Stripe and the client (browser). Unmasked credit card data is therefore never sent to the Commerce Cloud servers.

### Stripe PaymentIntent

The PaymentIntent workflow guides you through the process of collecting a payment from your customer. A PaymentIntent transitions through multiple statuses throughout its lifetime as it interfaces with Stripe.js to perform authentication flows and creates, at most, one successful charge.

The system creates a Stripe Charge (authorize or capture, based on Business Manager configuration) from a successfully created and submitted Basket. All Stripe Charges are created against a Stripe payment source.

### AVS auto-fail transactions

Site administrators can select a variety of AVS statuses to auto fail an order for. If the Stripe charge returns any of the selected statuses for either address_line1_check or address_zip_check, the order is auto-failed and the Stripe charge reversed. You can also manage these settings on the Stripe Dashboard. Supported payment methods:

- Cards (Visa, Mastercard, American Express, Discover, Diners Club, JCB, Alipay).
- The Payment Request button element gives you a single integration for Apple Pay, Google Pay, and the browser standard Payment Request API.

## Limitations and constraints

Stripe offers a number of standard services that aren’t supported by the cartridge. These include support for subscriptions, plans, and coupons. There aren’t any known locale specific restrictions in the cartridge.

The included RELAY OCAPI configurations are included as examples only. A RELAY implementation requires additional configuration and testing along with the Stripe team. For any locale specific restrictions, see the Stripe.js documentation.

## Compatibility

Available since Commerce Cloud Platform Release 16.8, SFRA version 4.4.

The cartridge is available for installation on storefronts that support both controller and SFRA SiteGenesis implementations.

## Privacy

Commerce Cloud doesn’t store any unmasked credit card data. The cartridge tokenizes all payment data within direct client-to-Stripe communications and obscures any sensitive credit card data before it arrives on the Commerce Cloud servers. Similarly, all credit card data that Commerce Cloud retrieves from the Stripe servers is either masked, tokenized, or both.

## See also

- [Implementation Guide](/connectors/salesforce-commerce-cloud/implementation-guide)
- [Operations and Maintenance](/connectors/salesforce-commerce-cloud/operations-and-maintenance)
- [User Guide](/connectors/salesforce-commerce-cloud/user-guide)
- [Testing](/connectors/salesforce-commerce-cloud/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Limitations and constraints](#limitations-and-constraints)[Compatibility](#compatibility)[Privacy](#privacy)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`