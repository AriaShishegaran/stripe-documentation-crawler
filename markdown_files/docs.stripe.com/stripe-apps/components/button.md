htmlButton | Stripe Documentation[Skip to content](#main-content)Button[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbutton)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbutton)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Button

Buttons allow users to take actions, and you can use them to direct a user's attention or warn them of outcomes.To add the Button component to your app:

`import {Button} from '@stripe/ui-extension-sdk/ui';`There are multiple button types available:

`<Button type="primary">Primary</Button>
<Button>Secondary</Button>
<Button type="destructive">Destructive</Button>`### Props

PropTypeDescriptionclassName`string`disabled`boolean`Whether the action is disabled.href`string`Native `href` attributeonPress`((e: PressEvent) => void)`Handler that is called when the press is released over the target.size`"small" | "medium" | "large"`The size of the buttontarget`HTMLAttributeAnchorTarget`type`"primary" | "secondary" | "destructive"`The type of the button### CSS

Buttons support these CSS properties:

PropertyTypeExamplealignX‘start’ | ‘center’ | ‘end’ | ‘stretch’‘center’Horizontal alignment. See[Layout properties](/stripe-apps/style#layout-properties)for details.width[fractional sizing token](/stripe-apps/style#sizing)2/3Button width. See[Sizing](/stripe-apps/style#sizing)for details.Buttons don’t support other CSS. Use the size and type props instead.

## Primary buttons

Primary buttons initiate the primary action of any given page or flow. Avoid having more than one primary button available to the user at a given time.

`<Button type="primary" onPress={() => console.log('Button was pressed')}>
  Primary button
</Button>`## Secondary buttons

Secondary buttons are the default and most common buttons in product interfaces. In general, use the secondary style for buttons that aren’t for primary actions.

`<Button onPress={() => console.log('Button was pressed')}>
  Secondary button
</Button>`## Destructive buttons

Use destructive buttons exclusively for actions that result in the destruction of any object or data.

`<Button type="destructive" onPress={() => console.log('Button was pressed')}>
  Destructive button
</Button>`## Button sizes

Buttons are available in three sizes, which determine the height of the element. Buttons can be as wide as needed to fill their container.

- You can use small buttons in contexts where space is limited or to match the size of other, small text such as legal terms, and so on.
- Medium is the default size for buttons.
- You can use large buttons in contexts where a call to action (CTA) needs increased prominence.

`<Button size="small">Small button</Button>
<Button>Medium button</Button>
<Button size="large">Large button</Button>`## Disabled buttons

`<Button type="primary" disabled>Hello!</Button>
<Button disabled>Secondary</Button>
<Button type="destructive" disabled>Destructive</Button>`## Icons in buttons

Use an icon inside of a button:

`<Button type="primary">
  <Icon name="addCircle" />
  Add customer
</Button>`## Content guidelines

### Use the {verb} + {noun} formula for labels

For example, Update customer. It’s acceptable to break this pattern in the case of common actions like Done, Close, Cancel, Add, or Delete.

### Be as descriptive as possible

When a button performs an action or navigates the user to a location, try to name that action or location within the label.

### Use sentence case

This applies for most cases except proper nouns and phrases.

### Avoid punctuation

Avoid periods, exclamation points, and question marks.

### Use second person

When referring to the user within a button or link, always use second person personal pronouns. Example: Post your status.

## Full-width buttons

Create a full-width Button component using the css prop:

`<Button type="primary" css={{width: 'fill', alignX: 'center'}}>
  Full-width button
</Button>`## Opening links in new tabs

`<Button href="https://stripe.com" target="_blank">
  Open link in new tab
</Button>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Primary buttons](#primary-buttons)[Secondary buttons](#secondary-buttons)[Destructive buttons](#destructive-buttons)[Button sizes](#button-sizes)[Disabled buttons](#disabled-buttons)[Icons in buttons](#icons-in-buttons)[Content guidelines](#content-guidelines)[Full-width buttons](#full-width-buttons)[Opening links in new tabs](#opening-links-in-new-tabs)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`