htmlOAuth changes for platform-controlled Standard accounts | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Foauth-changes-for-standard-platforms)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Foauth-changes-for-standard-platforms)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# OAuth changes for platform-controlled Standard accounts

Learn about the changes Stripe has made to OAuth for Connect.### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies to Custom and Express accounts, and Standard accounts with[platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts)enabled.We’ve updated OAuth to isolate platforms’ processing activity on platform-controlled Standard accounts. Platforms using OAuth with read_write scope can’t connect to Standard accounts that are controlled by another platform. Prior to June 2021, multiple platforms could connect to the same Standard account.

This change ensures that in the rare case that a Connect user with access to the Stripe Dashboard interacts with two platforms, each platform’s activity is kept distinct in separate Standard accounts.

When a user of a Standard account controlled by another platform connects to your platform, the Connect onboarding flow directs them to create a separate Standard account to use with your platform. The new account automatically connects to your platform.

If you registered your Connect application as an Extension integration, it can still connect to accounts that are connected to another platform. Extensions need to connect to existing Standard accounts that might also be connected to another Platform or Extension. Only Extensions can use read_only, which ensures that platforms can’t read other applications’ data.

However, if you had previously selected ‘Platform’ for your Connect application, and find that you need Extension functionality, then you will need to contact us to modify your integration selection. Your selection can be found at the Connect Settings page in the ‘Availability’ section.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`