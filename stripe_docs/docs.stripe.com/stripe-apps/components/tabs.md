# Tabs

Tabs are sections of content that display one panel of content at a time. The list of tab elements sits along the top edge of the currently displayed panel.

To add the Tabs component to your app:

## Basic Tabs

## Small Tabs

## Disabled Tabs

## Tab

The TabList component supports the selection of content.  TabList is made up of a collection of Tab components.  Each Tab can be uniquely identified with a tabKey prop. If you render Tab components using a map function, you must still add a key to satisfy the rules of React.

[the rules of React](https://reactjs.org/docs/lists-and-keys.html#keys)

## TabPanel

The TabPanels component supports displaying panels of content with Tabs.  TabPanels is made up of a collection of TabPanel components.  Each TabPanel can be uniquely identified with a tabKey prop. If you render TabPanel components using a map function, you must still add a key to satisfy the rules of React.

[the rules of React](https://reactjs.org/docs/lists-and-keys.html#keys)

## Controlled Tabs

Use the selectedKey prop from Tabs in combination with the tabKey prop from Tab and TabPanel to create a controlled component.

## Unsupported uses

Tabs don’t support conditional content within fragments unless the fragment children are given the same key.

To avoid unsupported uses of Tabs, use components instead of fragments.  Alternatively, give the children of fragments a shared key.

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
