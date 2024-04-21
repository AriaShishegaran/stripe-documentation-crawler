# Elements Appearance API

Stripe Elements supports visual customization, which allows you to match the design of your site with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.

- Start by picking a theme

[theme](#theme)

Get up and running right away by picking the prebuilt theme that most closely resembles your website.

- Customize the theme using variables

[variables](#variables)

Set variables like fontFamily and colorPrimary to broadly customize components appearing throughout each Element.

- If needed, fine-tune individual components and states using rules

[rules](#rules)

For complete control, specify custom CSS properties for individual components appearing in the Element.

The Elements Appearance API doesn’t support individual payment method Elements (such as CardElement). Use the Style object to customize your Element instead.

[Style](/js/appendix/style)

[Themes](#theme)

## Themes

Start customizing Elements by picking from one of the following themes:

- stripe

- night

- flat

[Variables](#variables)

## Variables

Set variables to affect the appearance of many components appearing throughout each Element.

The variables option works like CSS variables. You can specify CSS values for each variable and reference other variables with the var(--myVariable) syntax. You can even inspect the resulting DOM using the DOM explorer in your browser.

[CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

[Elements group](/js/elements_object/create#stripe_elements-options-fonts)

[font-variant-ligatures](http://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-ligatures)

[font-variation-settings](http://developer.mozilla.org/en-US/docs/Web/CSS/font-variation-settings)

[line-height](http://developer.mozilla.org/en-US/docs/Web/CSS/line-height)

[spacedAccordionItems](/js/elements_object/create_payment_element#payment_element_create-options-layout-spacedAccordionItems)

[Rules](#rules)

## Rules

The rules option is a map of CSS-like selectors to CSS properties, allowing granular customization of individual components. After defining your theme and variables, use rules to seamlessly integrate Elements to match the design of your site.

The selector for a rule can target any of the public class names in the Element, as well as the supported states, pseudo-classes, and pseudo-elements for each class. For example, the following are valid selectors:

- .Tab, .Label, .Input

- .Tab:focus

- .Input--invalid, .Label--invalid

- .Input::placeholder

The following are not valid selectors:

- .p-SomePrivateClass, img, only public class names can be targeted

- .Tab .TabLabel, ancestor-descendant relationships in selectors are unsupported

- .Tab--invalid, the .Tab class does not support the --invalid state

Each class name used in a selector supports an allowlist of CSS properties, that you specify using camel case (for example, boxShadow for the box-shadow property).

[supports an allowlist of CSS properties](#supported-css-properties)

[box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)

The following is the complete list of supported class names and corresponding states, pseudo-classes, and pseudo-elements.

Floating Labels can be enabled as an additional configuration option.

[additional configuration option](#others)

User Experience Tip

Make sure your .PickerItem active state stands out amongst the other states.

DO

Use a noticeable, high-contrast primary color, weight, and/or outline to distinguish the active state your customer has already selected.

DON’T

Don’t use two equally weighted options or low-contrast colors for your .PickerItem states because it makes distinguishing which one is active more difficult.

Some exceptions to the properties above are:

- -webkit-text-fill-color isn’t compatible with pseudo-classes

[Other Configuration Options](#others)

## Other Configuration Options

In addition to themes, variables and rules, we have provided additional appearance configuration options to style Elements.

You can customize these by adding them to the appearance object:

We currently support the below options:
