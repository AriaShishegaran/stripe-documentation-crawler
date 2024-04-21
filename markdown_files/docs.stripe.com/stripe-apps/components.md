htmlUI components | Stripe Documentation[Skip to content](#main-content)Components[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# UI components

Use Stripe’s library of components to quickly build your user interface.If your app needs a frontend, use this reference documentation to compose a UI. Stripe’s library of prebuilt components has customizable properties to help you quickly build apps aligned to Stripe best practices. Use components to structure layouts and create graphical or interactive experiences in your apps.

All components are available in Figma at @stripedesign on Figma Community.

## Views

Every view you add needs a view component. These determine which view of your app the user sees at different moments, similar to different HTML pages of a website.

The most common view is ContextView. When a user begins a workflow or task in your app, their view should switch to FocusView to hide the background details. To design your app settings page, use SettingsView. To design a sign in screen, use SignInView.

Some views are root components. ContextView, SettingsView, and SignInView are view roots—the foundational components that contain all other UI elements—whereas FocusView is a child component of ContextView.

ComponentDescription[ContextView](/stripe-apps/components/contextview)ContextView allows apps to render next to Stripe content in a drawer so users can look at them side by side and share context.[SettingsView](/stripe-apps/components/settingsview)Use SettingsView to let users to change details about how the app works with their account.[SignInView](/stripe-apps/components/signinview)Use SignInView to display a sign in screen to users.## Layout

Use layout components to create the structure of your pages and elements.

ComponentDescription[Box](/stripe-apps/components/box)Use boxes to wrap other components and add custom styles and layouts.[Divider](/stripe-apps/components/divider)Render a simple horizontal rule with the divider component.## Navigation

Use navigation components to help users wayfind and interact with your app.

ComponentDescription[Button](/stripe-apps/components/button)Buttons allow users to take actions in Stripe products, and you can use them to direct users’ attention or warn them of outcomes.[ButtonGroup](/stripe-apps/components/buttongroup)Use ButtonGroup to handle the layout for multiple buttons and collapse them into an overflow menu when space is limited.[Link](/stripe-apps/components/link)Links are used for navigating users from one page to another, and for actions that need more subtlety than a button provides.[Menu](/stripe-apps/components/menu)A menu presents a group of actions that a user can choose from, often related to a particular object or context.[Tabs](/stripe-apps/components/tabs)Use tabs to display sections of content.## Content

Use content components to organize and place information within your app.

ComponentDescription[Accordion](/stripe-apps/components/accordion)Use accordions to split long or complex content into collapsible chunks.[Badge](/stripe-apps/components/badge)Use badges to indicate states that an item or object might move through or change to.[Banner](/stripe-apps/components/banner)Use the Banner to show a variety of alerts or messages you want to make explicit to the user.[Chip](/stripe-apps/components/chip)Use chips to display and allow users to manipulate values.[FocusView](/stripe-apps/components/focusview)Use FocusView to open a dedicated space for the end user to complete a specific task.[Icon](/stripe-apps/components/icon)Display an icon graphic in a compatible format.[Img](/stripe-apps/components/img)Display images with the Img UI component.[Inline](/stripe-apps/components/inline)Use the inline component to style inline content such as text.[List](/stripe-apps/components/list)Display a list of information in a variety of preconfigured formats.[Spinner](/stripe-apps/components/spinner)Use the Spinner component to indicate something is loading.[Table](/stripe-apps/components/table)Display rows and columns of data.[Toast](/stripe-apps/components/toast)Inform users of temporary status.[Tooltip](/stripe-apps/components/tooltip)Use Tooltips to provide additional contextual information about a particular element or subject.## Forms

Use form components to compose input fields and controls that require user input. For example, use them to create checklists or to enable users to select settings.

ComponentDescription[Checkbox](/stripe-apps/components/checkbox)Use checkboxes to indicate or control boolean values.[DateField](/stripe-apps/components/datefield)Use DateField to create a date input field.[FormFieldGroup](/stripe-apps/components/formfieldgroup)Group form fields with the FormFieldGroup component.[Radio](/stripe-apps/components/radio)Use Radios to make a selection from a mutually exclusive set of options.[Select](/stripe-apps/components/select)Use Select to pick from a set of options in a dropdown.[Switch](/stripe-apps/components/switch)Similar to Checkboxes, you can use Switches to indicate or control boolean values.[TextArea](/stripe-apps/components/textarea)Use TextArea to create an input field for multiple lines of text.[TextField](/stripe-apps/components/textfield)Use TextField to create a text input field.## Charts

Use chart components to map data points visually. For example, use a chart in your app to help users track payments data or compare progress over time.

ComponentDescription[BarChart](/stripe-apps/components/barchart)A bar chart visualizes data as a series of data points using bars.[LineChart](/stripe-apps/components/linechart)A line chart visualizes data as a series of data points connected into a line.[Sparkline](/stripe-apps/components/sparkline)A type of line chart to display data succinctly as a simple line.## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Views](#views)[Layout](#layout)[Navigation](#navigation)[Content](#content-components)[Forms](#forms)[Charts](#charts)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`