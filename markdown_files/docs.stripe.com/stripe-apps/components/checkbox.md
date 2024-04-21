htmlCheckbox | Stripe Documentation[Skip to content](#main-content)Checkbox[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fcheckbox)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fcheckbox)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Checkbox

Use checkboxes to indicate or control boolean values.To add the Checkbox component to your app:

`import {Checkbox} from '@stripe/ui-extension-sdk/ui';``<Checkbox
  label="This is a Checkbox."
  onChange={(e) => {
    console.log(e.target.checked);
  }}
/>`Checkbox takes the following props, in addition to all the appropriate native DOM attributes.

### Props

PropTypeDescriptionaria-label`string`Text that describes the control. Only visible to screen readers, and is not clickable. Should not be used if `label` is set.autoFocus`boolean`defaultChecked`boolean`description`string`Descriptive text that will be rendered adjacent to the control's label.disabled`boolean`error`string`Error text that will be rendered below the control.form`string`hiddenElements`("label" | "description" | "error")[]`Visually hides the specified elements. The hidden elements will still be present and visible to screen readers.indeterminate`boolean`Sets whether the Checkbox should be rendered as indeterminate ("partially checked") or not. Note that this is purely visual, and will not change the actual `checked` state of the Checkbox. If a Checkbox is both `indeterminate` and `checked`, it will display as `indeterminate`.invalid`boolean`label`ReactNode`Text that describes the control. Will be both visible and clickable.name`string`onChange`((e: ChangeEvent<HTMLInputElement>) => void)`readOnly`boolean`required`boolean`tabIndex`number`value`string | number | readonly string[]`You can set a Checkbox component to different states:

- `indeterminate`
- `disabled`
- `invalid`

## Indeterminate

The Checkbox component can be in an indeterminate state. This is useful when it represents the aggregated state of some other set of checkboxes, of which some may be checked and some may not. Note that this property is purely visual, and does not affect the Checkbox’s underlying checked state.

`const [checked1, setChecked1] = React.useState(false);
const [checked2, setChecked2] = React.useState(true);

return (
  <Box
    css={{
      stack: 'x',
    }}
  >
    <Checkbox
      label="This Checkbox is aggregating the state of the Checkboxes below it."
      readOnly
      key={checked1 && checked2}
      defaultChecked={checked1 && checked2}
      indeterminate={checked1 !== checked2}
    />
    <Checkbox
      label="Checkbox 1"
      onChange={(e) => {
        setChecked1(e.target.checked);
      }}
    />
    <Checkbox
      label="Checkbox 2"
      defaultChecked
      onChange={(e) => {
        setChecked2(e.target.checked);
      }}
    />
  </Box>
);`## Disabled

Checkbox can be disabled. This prevents changes.

`<Checkbox
  label="This Checkbox is disabled."
  defaultChecked
  disabled
/>
<Checkbox
  disabled
  invalid
  label="This invalid Checkbox is disabled."
/>`## Invalid

You can mark a Checkbox component as invalid. This is a styling-only prop, useful in form validation. It won’t prevent form submission.

`<Checkbox label="This Checkbox is in an invalid state." invalid />`## State management

Use the Checkbox component as an uncontrolled input:

`<Checkbox
  onChange={(e) => {
    console.log(e.target.checked);
  }}
  defaultChecked
  label="This Checkbox is uncontrolled."
/>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Indeterminate](#indeterminate)[Disabled](#disabled)[Invalid](#invalid)[State management](#state-management)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`