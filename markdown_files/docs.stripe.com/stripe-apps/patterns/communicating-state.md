htmlCommunicating state for Stripe Apps | Stripe Documentation[Skip to content](#main-content)Communicating state[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fcommunicating-state)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fcommunicating-state)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Design patterns](/docs/stripe-apps/patterns)# Communicating state for Stripe Apps

Learn how to guide users to take actions in your app.Keep the user informed by showing them when they need to take a certain action.

## Before you begin

Create an app.

## Suggested use

- Use a[Toast](/stripe-apps/components/toast)component to provide temporary feedback after users take an action.
- Use a[Banner](/stripe-apps/components/banner)component to show users they need to take action on unexpected system-level requirements, changes, or issues. For example:

![On the left, a green check Toast on download. On the right, a red Notice on error.](https://b.stripecdn.com/docs-statics-srv/assets/communicating-state.a613d037f8e0b3bd8a6aa7199e708c8d.png)

## Examples

Consider the following attributes when choosing to deliver a message.

ToastBanner![Green check Toast example with text 'Changes saved'](https://b.stripecdn.com/docs-statics-srv/assets/Toast.e17b36572b25d60725b4bc24098b77b9.png)

![ Banner example with text 'New updates'](https://b.stripecdn.com/docs-statics-srv/assets/Notice.0435a3a4999b7189e67fba5c18dae242.png)

Display

Temporary

All toasts trigger on users’ actions. Toasts dismiss automatically after a short period or when the app closes.

Persistent

You can deliver banners at any time. Dismissing a banner requires an action.

Content

Limited text length

Messages for toasts should be short, and fewer than four words on one line. The maximum character length for a toast is 30.

Medium to long message

Banners contain title and body text. Banners are suitable for providing information with additional details.

Action

Optional

Provide an action as a shortcut for users to quickly enter the related event.

Required

Inform users to take the required action.

PositionBottom of the app drawerUnder app drawer headerWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Suggested use](#suggested-use)[Examples](#examples)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`