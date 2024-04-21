htmlButtonGroup | Stripe Documentation[Skip to content](#main-content)ButtonGroup[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbuttongroup)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbuttongroup)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# ButtonGroup

Use ButtonGroup to handle the layout for multiple buttons and collapse them into an overflow menu when space is limited.To add the ButtonGroup component to your app:

`import {ButtonGroup} from '@stripe/ui-extension-sdk/ui';``<ButtonGroup>
  <Button
    onPress={() => {
      console.log('Filter');
    }}
  >
    Filter
  </Button>
  <Button
    onPress={() => {
      console.log('Export');
    }}
  >
    Export
  </Button>
  <Button type="primary"
    onPress={() => {
      console.log('Save');
    }}
  >
    Save
  </Button>
</ButtonGroup>`### Props

PropTypeDescriptioncollapse`"none" | "auto"`Controls whether or not buttons within the group collapse when there isn't enough space to display them without overflowing.direction`"row" | "column"`Controls which axis the button group should span.menuTrigger`ReactNode`Allows overriding the trigger element used for an overflow menu. Must be a component that supports press events.## Overflow collapsing

Button groups responsively adapt to the space available in their container by collapsing buttons into an overflow menu. Primary buttons collapse after any other buttons, and larger buttons collapse first.

`<ButtonGroup>
  <Button
    onPress={() => {
      console.log('Filter');
    }}
  >
    Filter
  </Button>
  <Button
    onPress={() => {
      console.log('Export');
    }}
  >
    Export
  </Button>
  <Button type="primary"
    onPress={() => {
      console.log('Save');
    }}
  >
    Save
  </Button>
</ButtonGroup>`### Disabling collapse behavior

If you want to turn off collapsing behavior, you can specify the collapse="none" prop value.

`<ButtonGroup collapse="none">
  <Button
    onPress={() => {
      console.log('Filter');
    }}
  >
    Filter
  </Button>
  <Button
    onPress={() => {
      console.log('Export');
    }}
  >
    Export
  </Button>
  <Button type="primary"
    onPress={() => {
      console.log('Save');
    }}
  >
    Save
  </Button>
</ButtonGroup>`## Customizing the overflow menu trigger

You can replace the default overflow menu trigger with any element that supports onPress events. To adhere to best practices, remember to add an appropriate aria-label to your trigger element if it doesn’t contain descriptive text.

`<ButtonGroup
  menuTrigger={
    <Button>More actions</Button>
  }
>
  <Button
    onPress={() => {
      console.log('Filter');
    }}
  >
    Filter
  </Button>
  <Button
    onPress={() => {
      console.log('Export');
    }}
  >
    Export
  </Button>
  <Button
    type="primary"
    onPress={() => {
      console.log('Save');
    }}
  >
    Save
  </Button>
</ButtonGroup>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Overflow collapsing](#collapse-button-groups)[Customizing the overflow menu trigger](#customizing-overflow-trigger)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`