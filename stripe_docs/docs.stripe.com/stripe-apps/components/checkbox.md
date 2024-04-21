# Checkbox

To add the Checkbox component to your app:

Checkbox takes the following props, in addition to all the appropriate native DOM attributes.

[native DOM attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox)

You can set a Checkbox component to different states:

- indeterminate

- disabled

- invalid

## Indeterminate

The Checkbox component can be in an indeterminate state. This is useful when it represents the aggregated state of some other set of checkboxes, of which some may be checked and some may not. Note that this property is purely visual, and does not affect the Checkbox’s underlying checked state.

## Disabled

Checkbox can be disabled. This prevents changes.

## Invalid

You can mark a Checkbox component as invalid. This is a styling-only prop, useful in form validation. It won’t prevent form submission.

## State management

Use the Checkbox component as an uncontrolled input:

[uncontrolled input](/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions)

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
