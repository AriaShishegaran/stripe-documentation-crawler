htmlOnboarding sellers | Stripe Documentation[Skip to content](#main-content)Onboarding sellers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fonboarding-sellers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fonboarding-sellers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Mirakl](/docs/connectors/mirakl)# Onboarding sellers

You can use Express or Custom accounts with the transfers capability to onboard your sellers.

Standard accounts aren’t supported.

## Seller account initiation

The workflow starts when you create a new shop. If you invite the seller via email, the workflow starts when they submit the initial Mirakl form.

1. The[onboarding job](/connectors/mirakl/reference#onboarding)fetches newly created Mirakl shops.
2. The connector adds an onboarding link to each shop.
3. The seller finds the link in their Mirakl back office underMy Account.
4. They complete their KYC/KYB on Stripe.
5. The seller is redirected to the`REDIRECT_ONBOARDING`URL.

Stripe then performs verification, asking for more information when needed. To handle this, see the communication guidelines.

### Initiate the onboarding outside of Mirakl

You can build your own onboarding flow and then use the following API request to map the Stripe account with the Mirakl shop:

Command Line`curl \
	-X POST "https://connector-url/api/mappings" \
	-H "accept: application/json" \
	-H "X-AUTH-TOKEN: $OPERATOR_PASSWORD" \
	-H "Content-Type: application/json" \
	-d "{ \"miraklShopId\": 123, \"stripeUserId\": \"acct_1032D82eZvKYlo2C\"}"`## Seller account update

The workflow starts with the seller intending to update their information on Stripe.

1. The seller finds the link in their Mirakl back office underMy Account.
2. They update their information on Stripe.
3. The shop custom field is updated with a fresh login link to their[Express dashboard](/connect/express-dashboard).
4. The KYC status is updated on Mirakl.

The last two steps are also performed when accounts are updated by the connector during the account initiation workflow or when accounts are updated by Stripe, for example, a new document needs to be provided. You can receive a notification when that happens, see the Account updated notification.

Stripe then performs verification, asking for more information when needed. To handle this, see the communication guidelines.

![](https://b.stripecdn.com/docs-statics-srv/assets/seller-account-update.952e89cdf275dc5c34146b87cd06b603.svg)

## Communication

You can customize the visual appearance of the Stripe form with your brand’s name, color, and icon in your Connect settings page.

Be sure to tell your sellers about the link available in their Mirakl account settings and the need to complete the onboarding on Stripe to receive their payouts. For example, you could customize some of the email templates sent to your sellers by Mirakl under Settings > Notifications.

If we require more information from your sellers, we’ll email them directly for Express accounts. You must inform the sellers yourself if you decided to use Custom accounts.

NoteIn test mode, no emails are sent.

## See also

- [Integration steps](/connectors/mirakl#integration-steps).

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Seller account initiation](#seller-account-initiation)[Seller account update](#seller-account-update)[Communication](#communication)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`