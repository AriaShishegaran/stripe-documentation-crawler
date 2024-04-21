htmlElements Appearance API | Stripe Documentation[Skip to content](#main-content)Elements Appearance API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fappearance-api)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fappearance-api)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)# Elements Appearance API

Customize the look and feel of Elements to match the design of your site.WebiOSAndroidReact NativeStripe Elements supports visual customization, which allows you to match the design of your site with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.

1. Start by picking a[theme](#theme)

Get up and running right away by picking the prebuilt theme that most closely resembles your website.

1. Customize the theme using[variables](#variables)

Set variables like fontFamily and colorPrimary to broadly customize components appearing throughout each Element.

1. If needed, fine-tune individual components and states using[rules](#rules)

For complete control, specify custom CSS properties for individual components appearing in the Element.

NoteThe Elements Appearance API doesn’t support individual payment method Elements (such as CardElement). Use the Style object to customize your Element instead.

USTabs[Themes](#theme)Start customizing Elements by picking from one of the following themes:

- `stripe`
- `night`
- `flat`

`const appearance = {
  theme: 'night'
};

// Pass the appearance object to the Elements instance
const elements = stripe.elements({clientSecret, appearance});`[Variables](#variables)Set variables to affect the appearance of many components appearing throughout each Element.

The variables option works like CSS variables. You can specify CSS values for each variable and reference other variables with the var(--myVariable) syntax. You can even inspect the resulting DOM using the DOM explorer in your browser.

`const appearance = {
  theme: 'stripe',

  variables: {
    colorPrimary: '#0570de',
    colorBackground: '#ffffff',
    colorText: '#30313d',
    colorDanger: '#df1b41',
    fontFamily: 'Ideal Sans, system-ui, sans-serif',
    spacingUnit: '2px',
    borderRadius: '4px',
    // See all possible variables below
  }
};

// Pass the appearance object to the Elements instance
const elements = stripe.elements({clientSecret, appearance});`### Commonly used variables

VariableDescription`fontFamily`The font family used throughout Elements. Elements supports custom fonts by passing the`fonts`option to the[Elements group](/js/elements_object/create#stripe_elements-options-fonts).`fontSizeBase`The font size that’s set on the root of the Element. By default, other font size variables like`fontSizeXs`or`fontSizeSm`are scaled from this value using`rem`units.`spacingUnit`The base spacing unit that all other spacing is derived from. Increase or decrease this value to make your layout more or less spacious.`borderRadius`The border radius used for tabs, inputs, and other components in the Element.`colorPrimary`A primary color used throughout the Element. Set this to your primary brand color.`colorBackground`The color used for the background of inputs, tabs, and other components in the Element.`colorText`The default text color used in the Element.`colorDanger`A color used to indicate errors or destructive actions in the Element.### Less commonly used variables

VariableDescription`fontSmooth`What text anti-aliasing settings to use in the Element. It can be`always`,`auto`, or`never`.`fontVariantLigatures`The[font-variant-ligatures](http://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-ligatures)setting of text in the Element.`fontVariationSettings`The[font-variation-settings](http://developer.mozilla.org/en-US/docs/Web/CSS/font-variation-settings)setting of text in the Element.`fontWeightLight`The font weight used for light text.`fontWeightNormal`The font weight used for normal text.`fontWeightMedium`The font weight used for medium text.`fontWeightBold`The font weight used for bold text.`fontLineHeight`The[line-height](http://developer.mozilla.org/en-US/docs/Web/CSS/line-height)setting of text in the Element.`fontSizeXl`The font size of extra-large text in the Element. By default this is scaled from`var(--fontSizeBase)`using`rem`units.`fontSizeLg`The font size of large text in the Element. By default this is scaled from`var(--fontSizeBase)`using`rem`units.`fontSizeSm`The font size of small text in the Element. By default this is scaled from`var(--fontSizeBase)`using`rem`units.`fontSizeXs`The font size of extra-small text in the Element. By default this is scaled from`var(--fontSizeBase)`using`rem`units.`fontSize2Xs`The font size of double-extra small text in the Element. By default this is scaled from`var(--fontSizeBase)`using`rem`units.`fontSize3Xs`The font size of triple-extra small text in the Element. By default this is scaled from`var(--fontSizeBase)`using`rem`units.`logoColor`A preference for which logo variations to display; either`light`or`dark`.`tabLogoColor`The logo variation to display inside`.Tab`components; either`light`or`dark`.`tabLogoSelectedColor`The logo variation to display inside the`.Tab--selected`component; either`light`or`dark`.`blockLogoColor`The logo variation to display inside`.Block`components; either`light`or`dark`.`colorSuccess`A color used to indicate positive actions or successful results in the Element.`colorWarning`A color used to indicate potentially destructive actions in the Element.`accessibleColorOnColorPrimary`The color of text appearing on top of any`var(--colorPrimary)`background.`accessibleColorOnColorBackground`The color of text appearing on top of any`var(--colorBackground)`background.`accessibleColorOnColorSuccess`The color of text appearing on top of any`var(--colorSuccess)`background.`accessibleColorOnColorDanger`The color of text appearing on top of any`var(--colorDanger)`background.`accessibleColorOnColorWarning`The color of text appearing on top of any`var(--colorWarning)`background.`colorTextSecondary`The color used for text of secondary importance. For example, this color is used for the label of a tab that isn’t currently selected.`colorTextPlaceholder`The color used for input placeholder text in the Element.`iconColor`The default color used for icons in the Element, such as the icon appearing in the card tab.`iconHoverColor`The color of icons when hovered.`iconCardErrorColor`The color of the card icon when it’s in an error state.`iconCardCvcColor`The color of the CVC variant of the card icon.`iconCardCvcErrorColor`The color of the CVC variant of the card icon when the CVC field has invalid input.`iconCheckmarkColor`The color of checkmarks displayed within components like`.Checkbox`.`iconChevronDownColor`The color of arrow icons displayed within select inputs.`iconChevronDownHoverColor`The color of arrow icons when hovered.`iconCloseColor`The color of close icons, used for indicating a dismissal or close action.`iconCloseHoverColor`The color of close icons when hovered.`iconLoadingIndicatorColor`The color of the spinner in loading indicators.`iconMenuColor`The color of menu icons used to indicate a set of additional actions.`iconMenuHoverColor`The color of menu icons when hovered.`iconMenuOpenColor`The color of menu icons when opened.`iconPasscodeDeviceColor`The color of the passcode device icon, used to indicate a message has been sent to the user’s mobile device.`iconPasscodeDeviceHoverColor`The color of the passcode device icon when hovered.`iconPasscodeDeviceNotificationColor`The color of the notification indicator displayed over the passcode device icon.`iconRedirectColor`The color of the redirect icon that appears for redirect-based payment methods.`tabIconColor`The color of icons appearing in a tab.`tabIconHoverColor`The color of icons appearing in a tab when the tab is hovered.`tabIconSelectedColor`The color of icons appearing in a tab when the tab is selected.`tabIconMoreColor`The color of the icon that appears in the trigger for the additional payment methods menu.`tabIconMoreHoverColor`The color of the icon that appears in the trigger for the additional payment methods menu when the trigger is hovered.`accordionItemSpacing`The vertical spacing between`.AccordionItem`components. This is only applicable when[spacedAccordionItems](/js/elements_object/create_payment_element#payment_element_create-options-layout-spacedAccordionItems)is`true`.`gridColumnSpacing`The spacing between columns in the grid used for the Element layout.`gridRowSpacing`The spacing between rows in the grid used for the Element layout.`pickerItemSpacing`The spacing between`.PickerItem`components rendered within the`.Picker`component.`tabSpacing`The horizontal spacing between`.Tab`components.[Rules](#rules)The rules option is a map of CSS-like selectors to CSS properties, allowing granular customization of individual components. After defining your theme and variables, use rules to seamlessly integrate Elements to match the design of your site.

`const appearance = {
    rules: {
      '.Tab': {
        border: '1px solid #E0E6EB',
        boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02)',
      },

      '.Tab:hover': {
        color: 'var(--colorText)',
      },

      '.Tab--selected': {
        borderColor: '#E0E6EB',
        boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02), 0 0 0 2px var(--colorPrimary)',
      },

      '.Input--invalid': {
        boxShadow: '0 1px 1px 0 rgba(0, 0, 0, 0.07), 0 0 0 2px var(--colorDanger)',
      },

      // See all supported class names and selector syntax below
    }
  };

  // Pass the appearance object to the Elements instance
  const elements = stripe.elements({clientSecret, appearance});`### All rules

The selector for a rule can target any of the public class names in the Element, as well as the supported states, pseudo-classes, and pseudo-elements for each class. For example, the following are valid selectors:

- `.Tab, .Label, .Input`
- `.Tab:focus`
- `.Input--invalid, .Label--invalid`
- `.Input::placeholder`

The following are not valid selectors:

- `.p-SomePrivateClass, img`, only public class names can be targeted
- `.Tab .TabLabel`, ancestor-descendant relationships in selectors are unsupported
- `.Tab--invalid`, the`.Tab`class does not support the`--invalid`state

Each class name used in a selector supports an allowlist of CSS properties, that you specify using camel case (for example, boxShadow for the box-shadow property).

The following is the complete list of supported class names and corresponding states, pseudo-classes, and pseudo-elements.

### Tabs

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesTabs@2x.9c36db7ee4c98d7b2d6f00e91e6d4f20.png)

Class nameStatesPseudo-classesPseudo-elements`.Tab``--selected``:hover`,`:focus`,`:active`,`:disabled``.TabIcon``--selected``:hover`,`:focus`,`:active`,`:disabled``.TabLabel``--selected``:hover`,`:focus`,`:active`,`:disabled`### Form Inputs - Labels Above

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesFormInputs@2x.4ed082ee74fcbad043a80e2d4b133b35.png)

Class nameStatesPseudo-classesPseudo-elements`.Label``--empty`,`--invalid``.Input``--empty`,`--invalid``:hover`,`:focus`,`:disabled`,`:autofill``::placeholder`,`::selection``.Error`### Form Inputs - Floating Labels

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesFormInputsFloating@2x.daec4a823ac24cc86d94a44664104eb8.png)

NoteFloating Labels can be enabled as an additional configuration option.

Class nameStatesPseudo-classesPseudo-elements`.Label``--empty`,`--invalid`,`--floating`,`--resting``.Input``--empty`,`--invalid``:hover`,`:focus`,`:disabled`,`:autofill``::placeholder`,`::selection``.Error`### Block

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesBlock@2x.556532f7e919aaf1d775ceb0253f5c22.png)

Class nameStatesPseudo-classesPseudo-elements`.Block``.BlockDivider``.BlockAction``--negative``:hover`,`:focus`,`:active`### Code Input

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesCodeInput@2x.64975e4945d393068a2f207a2d48f25c.png)

Class nameStatesPseudo-classesPseudo-elements`.CodeInput``:hover`,`:focus`,`:disabled`### Checkbox

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesCheckbox@2x.d7bedd38a342344eb06d5bff5dd6ae43.png)

Class nameStatesPseudo-classesPseudo-elements`.Checkbox``--checked``.CheckboxLabel``--checked``:hover`,`:focus`,`:focus-visible``.CheckboxInput``--checked``:hover`,`:focus`,`:focus-visible`### Dropdown

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesDropdown@2x.d635e032d2a254d672c11825a2d3d23d.png)

Class nameStatesPseudo-classesPseudo-elements`.Dropdown``.DropdownItem``--highlight``:active`### Switch

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesSwitch@2x.a263ba8361af937d5228a35d18c63645.png)

Class nameStatesPseudo-classesPseudo-elements`.Switch``--active``:hover``.SwitchControl``:hover`### Picker

![](https://b.stripecdn.com/docs-statics-srv/assets/exampleRulesPicker@2x.aa78c665be0c7e33a62992c8e7e33014.png)

Class nameStatesPseudo-classesPseudo-elements`.PickerItem``--selected`,`--highlight`,`--new`,`--disabled``:hover`,`:focus`,`:active``.PickerAction``:hover`,`:focus`,`:active`User Experience Tip

Make sure your .PickerItem active state stands out amongst the other states.

![](https://b.stripecdn.com/docs-statics-srv/assets/uxTipPickerDo@2x.cc709dc96a8e99e6b020f53216d4d585.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/uxTipPickerDont@2x.b31bc4b51910a6eece59d44fa92c5b4d.png)

DO

Use a noticeable, high-contrast primary color, weight, and/or outline to distinguish the active state your customer has already selected.

DON’T

Don’t use two equally weighted options or low-contrast colors for your .PickerItem states because it makes distinguishing which one is active more difficult.

### Menu

Class nameStatesPseudo-classesPseudo-elements`.Menu``.MenuIcon``--open``:hover``.MenuAction``--negative``:hover`,`:focus`,`:active`### Accordion

Class nameStatesPseudo-classesPseudo-elements`.AccordionItem``--selected``:hover`,`:focus-visible`### Supported CSS properties

CSS PropertySupported classes`-moz-osx-font-smoothing``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``-webkit-font-smoothing``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``-webkit-text-fill-color``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``backgroundColor``AccordionItem`,`Action`,`Block`,`BlockAction`,`BlockDivider`,`Button`,`CheckboxInput`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`InputDivider`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`Switch`,`Tab``border``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderBottom``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderBottomColor``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderBottomLeftRadius``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderBottomRightRadius``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderBottomStyle``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderBottomWidth``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderColor``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderLeft``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderLeftColor``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderLeftStyle``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderLeftWidth``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderRadius``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`InputCloseIcon`,`Link`,`MenuAction`,`MenuIcon`,`PasscodeCloseIcon`,`PasscodeShowIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Switch`,`SwitchControl`,`Tab`,`TermsLink`,`TermsText`,`Text``borderRight``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderRightColor``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderRightStyle``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderRightWidth``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderStyle``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderTop``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderTopColor``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderTopLeftRadius``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderTopRightRadius``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderTopStyle``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderTopWidth``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``borderWidth``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Switch`,`SwitchControl`,`Tab`,`TermsText`,`Text``boxShadow``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`InputCloseIcon`,`Link`,`MenuAction`,`MenuIcon`,`PasscodeCloseIcon`,`PasscodeShowIcon`,`PickerAction`,`PickerItem`,`SecondaryLink`,`Switch`,`SwitchControl`,`Tab`,`TermsLink``color``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabIcon`,`TabLabel`,`TermsLink`,`TermsText`,`Text``fill``Action`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`SwitchControl`,`Tab`,`TabIcon``fontFamily``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``fontSize``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Switch`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``fontVariant``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``fontWeight``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``letterSpacing``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``lineHeight``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``margin``Action`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`MenuAction`,`PickerAction`,`PickerItem`,`Tab``marginBottom``Action`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`MenuAction`,`PickerAction`,`PickerItem`,`Tab``marginLeft``Action`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`MenuAction`,`PickerAction`,`PickerItem`,`Tab``marginRight``Action`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`MenuAction`,`PickerAction`,`PickerItem`,`Tab``marginTop``Action`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`MenuAction`,`PickerAction`,`PickerItem`,`Tab``opacity``Label``outline``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`InputCloseIcon`,`Link`,`MenuAction`,`MenuIcon`,`PasscodeCloseIcon`,`PasscodeShowIcon`,`PickerAction`,`PickerItem`,`SecondaryLink`,`Switch`,`SwitchControl`,`Tab`,`TermsLink``outlineOffset``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Input`,`InputCloseIcon`,`Link`,`MenuAction`,`MenuIcon`,`PasscodeCloseIcon`,`PasscodeShowIcon`,`PickerAction`,`PickerItem`,`SecondaryLink`,`Switch`,`SwitchControl`,`Tab`,`TermsLink``padding``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Menu`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Tab`,`TabIcon`,`TabLabel`,`TermsText`,`Text``paddingBottom``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Menu`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Tab`,`TabIcon`,`TabLabel`,`TermsText`,`Text``paddingLeft``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Menu`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Tab`,`TabIcon`,`TabLabel`,`TermsText`,`Text``paddingRight``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Menu`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Tab`,`TabIcon`,`TabLabel`,`TermsText`,`Text``paddingTop``AccordionItem`,`Action`,`Block`,`BlockAction`,`Button`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Menu`,`MenuAction`,`MenuIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`Tab`,`TabIcon`,`TabLabel`,`TermsText`,`Text``textDecoration``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``textShadow``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``textTransform``AccordionItem`,`Action`,`BlockAction`,`Button`,`Checkbox`,`CheckboxLabel`,`CodeInput`,`DropdownItem`,`Error`,`Input`,`Label`,`Link`,`MenuAction`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Tab`,`TabLabel`,`TermsLink`,`TermsText`,`Text``transition``Action`,`Block`,`BlockAction`,`Button`,`CheckboxInput`,`CheckboxLabel`,`CodeInput`,`Dropdown`,`DropdownItem`,`Error`,`Icon`,`Input`,`InputCloseIcon`,`Label`,`Link`,`MenuAction`,`MenuIcon`,`PasscodeCloseIcon`,`PasscodeShowIcon`,`PickerAction`,`PickerItem`,`RedirectText`,`SecondaryLink`,`Switch`,`SwitchControl`,`Tab`,`TabIcon`,`TabLabel`,`TermsLink`,`TermsText`,`Text`Some exceptions to the properties above are:

- `-webkit-text-fill-color`isn’t compatible with pseudo-classes

[Other Configuration Options](#others)In addition to themes, variables and rules, we have provided additional appearance configuration options to style Elements.

You can customize these by adding them to the appearance object:

`const appearance = {
  labels: 'floating',

  // other configurations such as `theme`, `variables` and `rules`...
}`We currently support the below options:

ConfigurationDescription`labels`Enables switching between labels above form fields and floating labels within the form fields; it can be either`above`or`floating`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Themes](#theme)[Variables](#variables)[Rules](#rules)[Other Configuration Options](#others)Products Used[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`