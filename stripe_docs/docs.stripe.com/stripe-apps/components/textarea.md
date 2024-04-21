# TextArea

To add the TextArea component to your app:

TextArea components support these CSS properties:

[fractional sizing token](/stripe-apps/style#sizing)

[Sizing](/stripe-apps/style#sizing)

TextArea components don’t support other CSS. Style them using their props instead.

## Invalid

You can mark a TextArea as invalid by setting the invalid prop on the element. This is purely visual. It defaults to false.

## Resizeable

By default, TextArea is vertically resizable. Users who need more space typically prefer this. If you need to prevent the element from resizing, set resizeable to false.

## Size

Changing the size allows you to choose variants with slightly more or slightly less room than the default. In general you don’t want to mix and match different sizes within the same form. The default is medium.

## Disable and read only

You can mark a field as disabled, which prevents any interaction and changes the styling. Disabled means that no data from that form element is submitted when the form is submitted.

You can also make a field as readOnly. Read-only means any data from within the element is submitted, but the user can’t change it.

## Rows

A TextArea uses rows to control its height rather than using a traditional height in pixels, just like a regular <TextArea />. This allows the element to size itself based on multiples of the font size, rather than a raw pixel value. It prevents text from being partially obscured by default.

The vertical height of your TextArea component also changes depending on what size value you set, because that changes the line height of the text inside the input.

## State management

Use the TextArea component as an uncontrolled input:

[uncontrolled input](/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions)

## Width

Set the width of a TexaArea component using the available values with the css prop:

[the available values](/stripe-apps/style#sizing)

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
