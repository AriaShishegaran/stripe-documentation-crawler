htmlTextField | Stripe Documentation[Skip to content](#main-content)TextField[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftextfield)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftextfield)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# TextField

Use TextField to create a text input field.To add the TextField component to your app:

`import {TextField} from '@stripe/ui-extension-sdk/ui';``<TextField
  label="Business name"
  placeholder="Acme Inc…"
  onChange={(e) => {
    console.log(e.target.value);
  }}
/>`### Props

PropTypeDescriptionaria-label`string`Text that describes the control. Only visible to screen readers, and is not clickable. Should not be used if `label` is set.autoComplete`string`autoFocus`boolean`defaultValue`string | number | readonly string[]`description`string`Descriptive text that will be rendered adjacent to the control's label.disabled`boolean`error`string`Error text that will be rendered below the control.form`string`hiddenElements`("label" | "description" | "error")[]`Visually hides the specified elements. The hidden elements will still be present and visible to screen readers.invalid`boolean`Programmatically mark the value as invalidlabel`ReactNode`Text that describes the control. Will be both visible and clickable.maxLength`number`minLength`number`name`string`onChange`ChangeEventHandler<HTMLInputElement>`onKeyDown`KeyboardEventHandler<HTMLInputElement>`onKeyUp`KeyboardEventHandler<HTMLInputElement>`placeholder`string`readOnly`boolean`required`boolean`size`"small" | "medium" | "large"`The size of the inputspellCheck`Booleanish`tabIndex`number`type`"number" | "text" | "search" | "tel" | "url" | "email" | "password"`Choose between the text-alike types on an inputonKeyPressDeprecated`KeyboardEventHandler<HTMLInputElement>`### CSS

TextField components support these CSS properties:

PropertyTypeExamplewidth[fractional sizing token](/stripe-apps/style#sizing)2/3Field width. See[Sizing](/stripe-apps/style#sizing)for details.TextField components don’t support other CSS. Style them using their props instead.

## Invalid

You can mark a TextField component as invalid by setting the invalid prop on the element. This is purely visual. The default is false.

`<TextField label="Current year" defaultValue="1892" invalid />`## Type

type behaves like the type attribute on an <input />, but is restricted to types that allow text. The default is text.

`<TextField label="Text" type="text" />
<TextField label="Password" type="password" />
<TextField label="Search" type="search" />
<TextField label="Number" type="number" />`## Size

Changing the size allows you to choose variants with slightly more or slightly less room than the default. In general you don’t want to mix and match different sizes within the same form. The default is medium.

`<TextField label="Small" size="small" />
<TextField label="Medium" size="medium" />
<TextField label="Large" size="large" />`## Disabled and read only

You can mark a field as disabled, which prevents any interaction and changes the styling. Disabled means that no data from that form element is submitted when the form is submitted.

You can also make a field as readOnly. Read-only means any data from within the element will be submitted, but the user can’t change it.

`<TextField label="Disabled" defaultValue="Field is disabled" disabled />
<TextField label="Readonly" defaultValue="Field is readonly" readOnly />`## State management

Use the TextField component as an uncontrolled input:

`<TextField
  onChange={(e) => {
    console.log(e);
  }}
  label="First name"
/>`## Width

Set the width of a TextField component using the available values with the css prop:

`<TextField css={{width: 'fill'}} />`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Invalid](#invalid)[Type](#type)[Size](#size)[Disabled and read only](#disabled-and-read-only)[State management](#state-management)[Width](#width)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`