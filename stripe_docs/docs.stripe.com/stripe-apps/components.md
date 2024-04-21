# UI components

If your app needs a frontend, use this reference documentation to compose a UI. Stripe’s library of prebuilt components has customizable properties to help you quickly build apps aligned to Stripe best practices. Use components to structure layouts and create graphical or interactive experiences in your apps.

All components are available in Figma at @stripedesign on Figma Community.

[@stripedesign](https://www.figma.com/community/file/1105918844720321397)

## Views

Every view you add needs a view component. These determine which view of your app the user sees at different moments, similar to different HTML pages of a website.

[view you add](/stripe-apps/build-ui)

The most common view is ContextView. When a user begins a workflow or task in your app, their view should switch to FocusView to hide the background details. To design your app settings page, use SettingsView. To design a sign in screen, use SignInView.

Some views are root components. ContextView, SettingsView, and SignInView are view roots—the foundational components that contain all other UI elements—whereas FocusView is a child component of ContextView.

[ContextView](/stripe-apps/components/contextview)

[SettingsView](/stripe-apps/components/settingsview)

[SignInView](/stripe-apps/components/signinview)

## Layout

Use layout components to create the structure of your pages and elements.

[Box](/stripe-apps/components/box)

[Divider](/stripe-apps/components/divider)

## Navigation

Use navigation components to help users wayfind and interact with your app.

[Button](/stripe-apps/components/button)

[ButtonGroup](/stripe-apps/components/buttongroup)

[Link](/stripe-apps/components/link)

[Menu](/stripe-apps/components/menu)

[Tabs](/stripe-apps/components/tabs)

## Content

Use content components to organize and place information within your app.

[Accordion](/stripe-apps/components/accordion)

[Badge](/stripe-apps/components/badge)

[Banner](/stripe-apps/components/banner)

[Chip](/stripe-apps/components/chip)

[FocusView](/stripe-apps/components/focusview)

[Icon](/stripe-apps/components/icon)

[Img](/stripe-apps/components/img)

[Inline](/stripe-apps/components/inline)

[List](/stripe-apps/components/list)

[Spinner](/stripe-apps/components/spinner)

[Table](/stripe-apps/components/table)

[Toast](/stripe-apps/components/toast)

[Tooltip](/stripe-apps/components/tooltip)

## Forms

Use form components to compose input fields and controls that require user input. For example, use them to create checklists or to enable users to select settings.

[Checkbox](/stripe-apps/components/checkbox)

[DateField](/stripe-apps/components/datefield)

[FormFieldGroup](/stripe-apps/components/formfieldgroup)

[Radio](/stripe-apps/components/radio)

[Select](/stripe-apps/components/select)

[Switch](/stripe-apps/components/switch)

[TextArea](/stripe-apps/components/textarea)

[TextField](/stripe-apps/components/textfield)

## Charts

Use chart components to map data points visually. For example, use a chart in your app to help users track payments data or compare progress over time.

[BarChart](/stripe-apps/components/barchart)

[LineChart](/stripe-apps/components/linechart)

[Sparkline](/stripe-apps/components/sparkline)

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
