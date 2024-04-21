htmlUse Radar with Connect | Stripe Documentation[Skip to content](#main-content)Use Radar with Connect[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fradar)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fradar)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Use Radar with Connect

Learn how to use Stripe Radar to identify fraud in Connect account charges.Stripe Radar uses machine learning to identify fraudulent payments in real time. When you use Radar with connected accounts, it checks only external charges. It doesn’t check fund transfers between Stripe accounts.

Charges in a Connect integration fall into two categories:

- Direct charges: Paid directly to a connected account; Stripe applies only the collecting account’s Radar configuration and rules
- Transferred charges(for example, destination charges or separate charges and transfers): Paid to the platform account and transferred to a connected account; Stripe applies only the platform account’s Radar configuration and rules

## Radar fees

Stripe charges Radar fees based on the rate for the account that collected the payment. For payments collected by the platform account and transferred to a connected account, you can pass Radar fees to the connected account by reducing the transferred amount.

## Radar configuration for a connected account

The Dashboard you use to configure Radar for a connected account depends on the connected account type. The following table shows which Dashboard to use for each account type.

Dashboard access of the connected accountConnected account DashboardPlatform account Dashboard Connect pageConnected accounts with access to the Stripe DashboardConnected accounts with access to the Express DashboardConnected accounts with no dashboard access## Radar behavior

Radar behavior for connected account payments depends on the charge category and connected account type. The following table describes each scenario.

Charge typeRadar config rules usedCharges visible in connected account DashboardCharges visible in platform account Dashboard Connect pageDirect for connected accounts with access to the Stripe DashboardConnected accountDirect for connected accounts with access to the Express DashboardConnected accountDirect for connected accounts with no dashboard accessConnected accountTransferred from platform accountPlatform account## Radar for Fraud Teams

If you have Radar for Fraud Teams, you can customize your rules to include destination charge attributes. You can either use the destination attribute in the supported rule attributes, or use custom metadata on the destination account.

## See also

- [Choose your connected account type](/connect/accounts)
- [Radar documentation](/radar)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Radar fees](#radar-fees)[Radar configuration for a connected account](#radar-configuration-for-a-connected-account)[Radar behavior](#radar-behavior)[Radar for Fraud Teams](#radar-for-fraud-teams)[See also](#see-also)Products Used[Connect](/connect)[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`