htmlDateField | Stripe Documentation[Skip to content](#main-content)DateField[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fdatefield)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fdatefield)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# DateField

Use the DateField component to collect date information from users.To add the DateField component to your app:

`import {DateField} from '@stripe/ui-extension-sdk/ui';`The following shows a preview of a DateField component with a label and a description:

`<DateField
  label="Date of birth"
  description="Enter your birthday"
/>`### Props

PropTypeDescriptionaria-label`string`Text that describes the control. Only visible to screen readers, and is not clickable. Should not be used if `label` is set.defaultValue`string`A default value that a user can changedescription`string`Descriptive text that will be rendered adjacent to the control's labeldisabled`boolean`error`string`Error text that will be rendered below the controlhiddenElements`("label" | "description" | "error")[]`Visually hides the specified elements. The hidden elements will still be present and visible to screen readersinvalid`boolean`Programmatically mark the value as invalidlabel`ReactNode`Text that describes the control. Will be both visible and clickable.onChange`((e: DateInputEvent) => void)`An onChange-alike event that fires only when the change results
in a valid date. Identical behavior to <input type="date" />size`"small" | "medium" | "large"`The size of the input## Size

A DateField at each size will match a TextField at that same size. However, you can’t make a date input wider in the same way that you can TextField.

`<DateField
  label="Date of birth (small)"
  description="Enter your birthday"
  size="small"
/>
<DateField
  label="Date of birth (medium)"
  description="Enter your birthday"
  size="medium"
/>
<DateField
  label="Date of birth (large)"
  description="Enter your birthday"
  size="large"
/>`## Error

You can provide an error message to indicate a problem with the date.

`<DateField
  label="Date of birth"
  description="Enter your birthday"
  defaultValue="2099-02-31"
  invalid
  error="Invalid birthday"
/>`## Disabled

Disable a DateField if the user shouldn’t modify it.

`<DateField
  label="Date of birth"
  description="Enter your birthday"
  defaultValue="2011-09-01"
  disabled
/>`## Hide elements

You can visually hide elements of the DateField component, such as the label or description, while maintaining accessibility for screen readers.

`<DateField
  label="Date of birth"
  description="Enter your birthday"
  defaultValue="2011-09-01"
  hiddenElements={['description', 'label']}
/>`## Events

The onChange prop works similarly to a native <input type="date" /> HTML element. It only returns a value when it’s a valid date. This means that the onChange handler won’t be called on every keystroke, and a DateField can’t be a controlled input.

`<DateField
  label="Date of birth"
  description="Enter your birthday"
  onChange={(e) => {
    console.log(e.target.value);
  }}
/>`Event props (beginning with on) besides onChange fire independently for each of the three sections of the DateField component: year, month, and day.

`<DateField
  label="Date of birth"
  description="Enter your birthday"
  onFocus={(e) => {
    console.log('focus', e);
  }}
  onBlur={(e) => {
    console.log('blur', e);
  }}
  onKeyPress={(e) => {
    console.log('keypress', e);
  }}
  onKeyDown={(e) => {
    console.log('keydown', e);
  }}
  onKeyUp={(e) => {
    console.log('keyup', e);
  }}
/>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Size](#size)[Error](#error)[Disabled](#disabled)[Hide elements](#hide-elements)[Events](#events)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`