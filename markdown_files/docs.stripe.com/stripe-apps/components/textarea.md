htmlTextArea | Stripe Documentation[Skip to content](#main-content)TextArea[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftextarea)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftextarea)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# TextArea

Use TextArea to create an input field for multiple lines of text.To add the TextArea component to your app:

`import {TextArea} from '@stripe/ui-extension-sdk/ui';``<TextArea
  label="Description"
  placeholder="Acme Inc was founded in…"
  defaultValue="Stripe Apps lets you embed custom…"
  onChange={(e) => {
    console.log(e.target.value);
  }}
/>`### Props

PropTypeDescriptionaria-label`string`Text that describes the control. Only visible to screen readers, and is not clickable. Should not be used if `label` is set.autoComplete`string`autoFocus`boolean`cols`number`defaultValue`string | number | readonly string[]`description`string`Descriptive text that will be rendered adjacent to the control's label.disabled`boolean`error`string`Error text that will be rendered below the control.form`string`hiddenElements`("label" | "description" | "error")[]`Visually hides the specified elements. The hidden elements will still be present and visible to screen readers.invalid`boolean`Programmatically mark the value as invalidlabel`ReactNode`Text that describes the control. Will be both visible and clickable.maxLength`number`minLength`number`name`string`onChange`ChangeEventHandler<HTMLTextAreaElement>`onKeyDown`KeyboardEventHandler<HTMLTextAreaElement>`onKeyUp`KeyboardEventHandler<HTMLTextAreaElement>`placeholder`string`readOnly`boolean`required`boolean`resizeable`boolean`Allow the user to resize the textarearows`number`Rows of text that are visible in the inputsize`"small" | "medium" | "large"`The size of the inputspellCheck`Booleanish`tabIndex`number`wrap`string`onKeyPressDeprecated`KeyboardEventHandler<HTMLTextAreaElement>`### CSS

TextArea components support these CSS properties:

PropertyTypeExamplewidth[fractional sizing token](/stripe-apps/style#sizing)2/3Text area width. See[Sizing](/stripe-apps/style#sizing)for details.TextArea components don’t support other CSS. Style them using their props instead.

## Invalid

You can mark a TextArea as invalid by setting the invalid prop on the element. This is purely visual. It defaults to false.

`<TextArea label="Favorite word" defaultValue="Stripe Apps lets you embed custom…" invalid />`## Resizeable

By default, TextArea is vertically resizable. Users who need more space typically prefer this. If you need to prevent the element from resizing, set resizeable to false.

`<TextArea label="Resizable bio" defaultValue="Stripe Apps lets you embed custom…" />
<TextArea
  label="Unresizable bio"
  resizeable={false}
  defaultValue="Stripe Apps lets you embed custom…"
/>`## Size

Changing the size allows you to choose variants with slightly more or slightly less room than the default. In general you don’t want to mix and match different sizes within the same form. The default is medium.

`<TextArea
  label="Description (large)"
  size="large"
  defaultValue="Stripe Apps lets you embed custom…"
/>
<TextArea
  label="Description (medium, default)"
  size="medium"
  defaultValue="Stripe Apps lets you embed custom…"
/>
<TextArea
  label="Description (small)"
  size="small"
  defaultValue="Stripe Apps lets you embed custom…"
/>`## Disable and read only

You can mark a field as disabled, which prevents any interaction and changes the styling. Disabled means that no data from that form element is submitted when the form is submitted.

You can also make a field as readOnly. Read-only means any data from within the element is submitted, but the user can’t change it.

`<TextArea label="Disabled" defaultValue="Stripe Apps lets you embed custom…" disabled />
<TextArea label="Readonly" defaultValue="Stripe Apps lets you embed custom…" readOnly />`## Rows

A TextArea uses rows to control its height rather than using a traditional height in pixels, just like a regular <TextArea />. This allows the element to size itself based on multiples of the font size, rather than a raw pixel value. It prevents text from being partially obscured by default.

The vertical height of your TextArea component also changes depending on what size value you set, because that changes the line height of the text inside the input.

`<TextArea label="Description (3 rows, default)" defaultValue="Stripe Apps lets you embed custom…" />
<TextArea label="Description (6 rows)" rows={6} defaultValue="Stripe Apps lets you embed custom…" />`## State management

Use the TextArea component as an uncontrolled input:

`<TextArea
  onChange={(e) => {
    console.log(e);
  }}
  label="About your business"
  placeholder="Our business is…"
/>`## Width

Set the width of a TexaArea component using the available values with the css prop:

`<TextArea css={{width: 'fill'}} />`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Invalid](#invalid)[Resizeable](#resizeable)[Size](#size)[Disable and read only](#disable-and-read-only)[Rows](#rows)[State management](#state-management)[Width](#width)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`