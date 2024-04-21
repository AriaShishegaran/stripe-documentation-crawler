# SettingsView

You can define a specialized settings view to let users change specific details about how the app works with their account. For example, an app that uses a third-party API like Zendesk could use SettingsView to authorize a user with their Zendesk account. For more details, learn how to add a settings page for your app.

[add a settings page](/stripe-apps/app-settings)

What SettingsView looks like

SettingsView is a view root component, just like ContextView, containing all other UI elements. It’s the only view that isn’t tied to a specific object, but tied instead to the settings viewport. The settings viewport maps to predefined locations in the Dashboard, outside of the app drawer.

SettingsView renders on the app settings page in the Dashboard after you upload an app. While previewing your app locally, you can preview the SettingsView in the Dashboard at https://dashboard.stripe.com/test/apps/settings-preview.

[https://dashboard.stripe.com/test/apps/settings-preview](https://dashboard.stripe.com/test/apps/settings-preview)

To use SettingsView, you must add a view with the settings viewport to your app manifest. An application with a settings view would have an app manifest with a ui_extension field that would look something like this:

This example shows how to fetch settings from an external API, display them, and save changes.

## See also

- Design patterns to follow

[Design patterns to follow](/stripe-apps/patterns)

- Style your app

[Style your app](/stripe-apps/style)

- UI testing

[UI testing](/stripe-apps/ui-testing)
