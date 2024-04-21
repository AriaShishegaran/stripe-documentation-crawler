htmlTooltip | Stripe Documentation[Skip to content](#main-content)Tooltip[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftooltip)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftooltip)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Tooltip

Use Tooltips to provide additional contextual information about a particular element or subject.To add the Tooltip component to your app:

`import {Tooltip} from '@stripe/ui-extension-sdk/ui';`This is a preview of two Tooltip components with each type of label:

`<Tooltip
  type="description"
  trigger={
    <Button type="primary" disabled onPress={undefined}>
      Pay out to bank
    </Button>
  }
>
  You have no available balance to pay out. You can create payouts when
  you've accumulated a positive balance again.
</Tooltip>

<Tooltip
  type="label"
  trigger={
    <Button onPress={undefined}>
      <Icon name="notifications" />
    </Button>
  }
>
  Notifications
</Tooltip>`Tooltips are overlays that appear when a user hovers or focuses a target element. Use Tooltips to provide additional contextual information about a particular element or subject. You can use tooltips as either descriptions or labels.

Avoid putting any interactive content such as links within a Tooltip, because keyboard users won’t be able to access it.

### Props

PropTypeDescriptiontriggerRequired`RefObject<HTMLElement> | ReactElement<any, string | JSXElementConstructor<any>>`The target element that should be used as the Tooltip trigger.delay`number`How much time in milliseconds to wait before showing the Tooltip on hoverplacement`Placement`How the Tooltip should be placed relative to the trigger elementtype`"label" | "description"`The style variant of the Tooltip## Placement

You can place tooltips in one of 4 primary directions and further align them along a secondary axis, resulting in a total of 12 possible placement options relative to the trigger. The placement automatically adjusts as necessary to ensure the Tooltip remains visible within the viewport.

`<Tooltip placement="top left" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "top left"
</Tooltip>
<Tooltip placement="top" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "top"
</Tooltip>
<Tooltip placement="top right" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "top right"
</Tooltip>
<Tooltip placement="right top" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "right top"
</Tooltip>
<Tooltip placement="right" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "right"
</Tooltip>
<Tooltip placement="right bottom" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "right bottom"
</Tooltip>
<Tooltip placement="bottom right" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "bottom right"
</Tooltip>
<Tooltip placement="bottom" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "bottom"
</Tooltip>
<Tooltip placement="bottom left" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "bottom left"
</Tooltip>
<Tooltip placement="left bottom" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "left bottom"
</Tooltip>
<Tooltip placement="left" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "left"
</Tooltip>
<Tooltip placement="left top" trigger={<Button onPress={undefined}><Icon name="info" /></Button>}>
  "left top"
</Tooltip>`## Delay

Tooltips have a short delay for when they appear after hovering over their trigger element. You can control the amount of time it takes for a Tooltip to become active on hover using the delay prop. Tooltips always appear immediately when their trigger element receives keyboard focus.

`<Tooltip delay={0} trigger={<Button onPress={undefined}>Immediate</Button>}>
  I showed up immediately.
</Tooltip>`Tooltips appear immediately on hover while another Tooltip is already active.

`<Tooltip trigger={<Button onPress={undefined}>Hover me</Button>}>
  I showed up after a delay.
</Tooltip>

<Tooltip trigger={<Button onPress={undefined}>Then me</Button>}>
  I showed up immediately.
</Tooltip>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Placement](#placement)[Delay](#delay)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`