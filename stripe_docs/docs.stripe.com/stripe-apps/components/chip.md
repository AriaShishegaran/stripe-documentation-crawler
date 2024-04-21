# Chip

To add the Chip component to your app:

This is a preview of several Chip components in a ChipList component with different property configurations:

## Suggested chip

To suggest to the user with a plus icon that they add something represented by a chip, pass a callback function to the onAddSuggestion property.

## Chip with dropdown

If you want to allow the user to edit the value of a chip after they’ve made their initial selection, provide an onDropdown callback function to open a selection interface needed for making edits.

## Representing multiple values

When you populate the Chip component’s value property with an array of values, they’re listed within the chip.

## Presenting chips in a list

In many cases, chips aren’t presented on their own—they’re alongside other chips. The ChipList component handles the appropriate spacing and wrapping of chips in a list, and also provides for convenient keyboard navigation of chips using the right and left arrow keys.

## Non-closeable chip

When a Chip represents a required value, it can be useful to present a chip without an add or cancel icon. Exclude the onAddSuggestion and onClose callbacks to present users with a non-closeable chip.

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
