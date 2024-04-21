htmlBadge | Stripe Documentation[Skip to content](#main-content)Badge[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbadge)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbadge)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Badge

Use badges to indicate the state of an item or object.Unlike buttons, badges are read-only and don’t perform any actions, such as onPress events. Use badges to indicate the state of an item or object in your applications user interface.

To add the Badge component to your app:

`import {Badge} from '@stripe/ui-extension-sdk/ui';`The following types of badges are available:

- Neutral: Neutral label, no action required, everything is working as expected
- Info: Identifies an object or action with an important attribute or a key state
- Positive: Positive, neutral and important outcome or category, no action required
- Negative: Negative, important outcome or category, no action required
- Warning: Needs immediate action, optional to resolve
- Urgent: Needs immediate action, strong requirement to resolve

`<Badge>
  Neutral
</Badge>

<Badge type="info">
  Info
</Badge>

<Badge type="positive">
  Positive
</Badge>

<Badge type="negative">
  Negative
</Badge>

<Badge type="warning">
  Warning
</Badge>

<Badge type="urgent">
  Urgent
</Badge>`### Props

PropTypetype`"urgent" | "warning" | "negative" | "positive" | "info" | "neutral"`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`