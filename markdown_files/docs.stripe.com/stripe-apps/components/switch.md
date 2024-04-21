htmlSwitch | Stripe Documentation[Skip to content](#main-content)Switch[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fswitch)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fswitch)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Switch

Similar to Checkboxes, you can use Switches to indicate or control boolean values.To add the Switch component to your app:

`import {Switch} from '@stripe/ui-extension-sdk/ui';`A common use of Switches is for settings that you save immediately—in other words, Switch is rarely part of a larger form that needs to be submitted separately.

Here’s a simple example of a Switch.

`<Switch
  label="This is a Switch."
  onChange={(e) => {
    console.log(e.target.checked);
  }}
/>`### Props

PropTypeDescriptionaria-label`string`Text that describes the control. Only visible to screen readers, and is not clickable. Should not be used if `label` is set.autoFocus`boolean`defaultChecked`boolean`description`string`Descriptive text that will be rendered adjacent to the control's label.disabled`boolean`error`string`Error text that will be rendered below the control.form`string`hiddenElements`("label" | "description" | "error")[]`Visually hides the specified elements. The hidden elements will still be present and visible to screen readers.invalid`boolean`label`ReactNode`Text that describes the control. Will be both visible and clickable.name`string`onChange`((e: ChangeEvent<HTMLInputElement>) => void)`readOnly`boolean`required`boolean`tabIndex`number`value`string | number | readonly string[]`## State management

Use the Switch component as an uncontrolled input:

`<Switch
  onChange={(e) => {
    console.log(e.target.checked);
  }}
  defaultChecked
  label="This Switch is uncontrolled."
/>`## Disabled

You can disable a Switch component, which prevents changes.

`<Switch
  label="This Switch is disabled."
  defaultChecked
  disabled
/>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[State management](#state-management)[Disabled](#disabled)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`