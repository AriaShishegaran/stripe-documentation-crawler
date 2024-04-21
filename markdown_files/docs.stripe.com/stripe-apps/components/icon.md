htmlIcon | Stripe Documentation[Skip to content](#main-content)Icon[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ficon)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ficon)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Icon

Display an icon graphic in a compatible format.To add the Icon component to your app:

`import {Icon} from '@stripe/ui-extension-sdk/ui';`This is a preview of an Icon component:

`<Icon name="addCircle" />`### Props

PropTypearia-hidden`boolean`size`iconSize`### CSS

Icons support these CSS properties:

PropertyTypeExamplefill[text and icon color token](/stripe-apps/style#text-&-icons)‘success’Contrasting color. See[Color](/stripe-apps/style#color)for details.If you don’t specify a fill value, the icon gets its color from its parent.

## Size

Icons use the size prop for sizing. They can have one of five sizes:

- `xsmall`:`12px`
- `small`:`16px`
- `medium`:`20px`(default)
- `large`:`32px`
- `xlarge`:`64px`

`<Icon name="konbini" size="xsmall" />
<Icon name="konbini" size="small" />
<Icon name="konbini" size="medium" />
<Icon name="konbini" size="large" />
<Icon name="konbini" size="xlarge" />`## Color and fill

You can give the Icon component color with the fill property of the css prop.

`<Icon name="cancelCircle" css={{fill: 'critical'}} />`### Default color behavior

By default, icons are the same color as the text around them.

`<Inline css={{color: 'attention'}}>
  <Icon name="mobile" /> new messages
</Inline>`## Accessibility

`<Icon icon={add} aria-hidden={false} aria-label="Add another item" />`By default, there is an aria-hidden attribute on icons (read more about ARIA). In the rare situations the icon has semantic value to screen-reader users, you can manually set aria-hidden={false}. In these situations it’s often a good idea to add an aria-label as well. In general, it’s better to have text labels rather than making visual-only icons important for a workflow.

## Icons in Button and Badge components

You can place an Icon component inside of a Button or Badge component.

`<Button>
  <Icon name="mobile" size="xsmall" />
  <Inline>New messages</Inline>
</Button>
<Badge type="positive">
  <Icon name="mobile" size="xsmall" />
  New messages
</Badge>`## Icon reference

## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Size](#size)[Color and fill](#color-and-fill)[Accessibility](#accessibility)[Icons in Button and Badge components](#icons-in-button-and-badge-components)[Icon reference](#icon-reference)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`