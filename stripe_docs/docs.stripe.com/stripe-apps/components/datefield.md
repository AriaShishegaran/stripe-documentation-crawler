# DateField

To add the DateField component to your app:

The following shows a preview of a DateField component with a label and a description:

## Size

A DateField at each size will match a TextField at that same size. However, you can’t make a date input wider in the same way that you can TextField.

## Error

You can provide an error message to indicate a problem with the date.

## Disabled

Disable a DateField if the user shouldn’t modify it.

## Hide elements

You can visually hide elements of the DateField component, such as the label or description, while maintaining accessibility for screen readers.

## Events

The onChange prop works similarly to a native <input type="date" /> HTML element. It only returns a value when it’s a valid date. This means that the onChange handler won’t be called on every keystroke, and a DateField can’t be a controlled input.

[controlled input](https://reactjs.org/docs/forms.html#controlled-components)

Event props (beginning with on) besides onChange fire independently for each of the three sections of the DateField component: year, month, and day.

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
