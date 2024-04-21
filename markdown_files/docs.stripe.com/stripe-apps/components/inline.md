htmlInline | Stripe Documentation[Skip to content](#main-content)Inline[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Finline)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Finline)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Inline

The inline component is used to style inline content such as text.To add the Inline component to your app:

`import {Inline} from '@stripe/ui-extension-sdk/ui';`Inline components are styleable inline elements, equivalent to a span in HTML. They support custom styles. If you’d like to render or style block-level elements, see the Box component.

`<Inline
  css={{
    font: 'body',
    fontWeight: 'semibold',
    color: 'success',
    marginY: 'large',
  }}
>
  This is an example of the inline component.
</Inline>`## Emphasized text

`<Inline css={{font: 'body', color: 'primary', fontWeight: 'semibold'}}>
  This text is emphasized
</Inline>`## Secondary text

`<Inline css={{font: 'caption', color: 'secondary'}}>
  This text is styled using the caption text style and the secondary color.
</Inline>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Emphasized text](#emphasized-text)[Secondary text](#secondary-text)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`