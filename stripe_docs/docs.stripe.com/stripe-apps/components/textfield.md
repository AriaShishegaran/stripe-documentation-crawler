# TextField

To add the TextField component to your app:

TextField components support these CSS properties:

[fractional sizing token](/stripe-apps/style#sizing)

[Sizing](/stripe-apps/style#sizing)

TextField components don’t support other CSS. Style them using their props instead.

## Invalid

You can mark a TextField component as invalid by setting the invalid prop on the element. This is purely visual. The default is false.

## Type

type behaves like the type attribute on an <input />, but is restricted to types that allow text. The default is text.

## Size

Changing the size allows you to choose variants with slightly more or slightly less room than the default. In general you don’t want to mix and match different sizes within the same form. The default is medium.

## Disabled and read only

You can mark a field as disabled, which prevents any interaction and changes the styling. Disabled means that no data from that form element is submitted when the form is submitted.

You can also make a field as readOnly. Read-only means any data from within the element will be submitted, but the user can’t change it.

## State management

Use the TextField component as an uncontrolled input:

[uncontrolled input](/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions)

## Width

Set the width of a TextField component using the available values with the css prop:

[the available values](/stripe-apps/style#sizing)

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
