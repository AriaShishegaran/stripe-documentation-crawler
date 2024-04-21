# Icon

To add the Icon component to your app:

This is a preview of an Icon component:

Icons support these CSS properties:

[text and icon color token](/stripe-apps/style#text-&-icons)

[Color](/stripe-apps/style#color)

If you don’t specify a fill value, the icon gets its color from its parent.

## Size

Icons use the size prop for sizing. They can have one of five sizes:

- xsmall: 12px

- small: 16px

- medium: 20px (default)

- large: 32px

- xlarge: 64px

## Color and fill

You can give the Icon component color with the fill property of the css prop.

By default, icons are the same color as the text around them.

## Accessibility

By default, there is an aria-hidden attribute on icons (read more about ARIA). In the rare situations the icon has semantic value to screen-reader users, you can manually set aria-hidden={false}. In these situations it’s often a good idea to add an aria-label as well. In general, it’s better to have text labels rather than making visual-only icons important for a workflow.

[read more about ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)

## Icons in Button and Badge components

You can place an Icon component inside of a Button or Badge component.

## Icon reference

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
