htmlActivation flow for Stripe Apps | Stripe Documentation[Skip to content](#main-content)Activation flow[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Factivation-flow)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Factivation-flow)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Design patterns](/docs/stripe-apps/patterns)# Activation flow for Stripe Apps

Learn how to build an clear activation flow for your Stripe app.Follow the recommended account activation guidelines on this page to make sign in and authentication secure and easy to follow.

WarningMake sure users never share their full credential set with Stripe.

## Before you begin

Create an app.

## Flow

The ideal sign in flow is:

1. Effortless—Users can onboard quickly and easily, while staying focused on the task in front of them, and providing only necessary information.
2. Customizable—The process can scale up and down according to the user needs—making onboarding versatile, yet focused.
3. Relevant—Users can bypass distractions by seeing short headlines and paragraphs, and only relevant images.

![](https://b.stripecdn.com/docs-statics-srv/assets/activation-flow-02.7760bad10eb8d99537c06690907010fe.png)

## Suggested use

- Your sign in flow must be secure and easy to follow.
- The sign in flow must be the path of least resistance. Avoid unnecessary steps. For example:

![](https://b.stripecdn.com/docs-statics-srv/assets/activation-flow-01.03627e4cf7c6d6f62583c6814248114e.png)

- If users need to sign in to an external site, collect sensitive credentials on that site, not within the Stripe Dashboard to avoid compromising passwords.
- Stick to the recommended set of steps.
- Detect whether a user already has an account for your product and allow them enter a sign in flow. For example:

![](https://b.stripecdn.com/docs-statics-srv/assets/activation-flow-03.4593e0c6fedebac58dce2828163a7b74.png)

- Keep the onboarding flow brief and include authorization to connect your users’ Stripe accounts to your product. For example:

![](https://b.stripecdn.com/docs-statics-srv/assets/activation-flow-04.a680b38bbdfe4e1546ae93f64a37af90.png)

- Always redirect users back to Stripe when sign in is complete. For example:

![](https://b.stripecdn.com/docs-statics-srv/assets/activation-flow-05.6f272ac74689bbaf260607e08119ecd1.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Flow](#flow)[Suggested use](#suggested-use)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`