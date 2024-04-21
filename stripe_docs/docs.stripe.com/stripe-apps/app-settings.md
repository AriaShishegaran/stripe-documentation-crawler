# Add an app settings page

When you upload your app to Stripe, we create an app settings page in the Stripe Dashboard. The rest of the page is open for you to create custom settings.

## The user experience of app settings

An account administrator who installs your app can use the settings page in several ways:

- Configuring your app for their use case: For example, say a business on Stripe wants to synchronize payments data from the last seven days with another application. Your settings page can provide a dropdown menu to let admin users select 1 week as the time period. The configuration applies globally on the account, meaning all users on that Stripe account now see data from the past week in your app.

- Authenticating users: If your app connects to a different application—outside of Stripe—you need a place for Stripe users to log in to the other app, pass credentials, and handle authentication. The settings page is the best place for users to link accounts in this way. For example, an app that uses a third-party API like Zendesk needs a SettingsView to authenticate a user with their Zendesk account.

- Uninstalling an app: The only place to uninstall an app is the settings page. You can’t remove the uninstall button from the settings page. There are also buttons for users to report your app and view its marketplace listing if you have one.

## What you can do with it

By default, the settings page includes buttons for uninstalling and reporting your app, plus various app details. To populate the page with custom settings, use SettingsView. This view root component renders in the settings page. Add UI components, like tabs and form fields, to create the user experience you want.

What SettingsView looks like in the Stripe Dashboard

# How to customize the settings page

Populate your app’s empty settings page by defining a settings view and composing a UI to let your users set up and configure your app.

You have control over the design of your app settings page. In the developer preview mode, the settings page appears as a smaller view. In live mode, your settings page is a full screen.

[Add a settings view](#define-settingsview)

## Add a settings view

Define a settings view with the CLI:

You can name your settings component anything you want. The generated settings view is available in the src/views directory. In the app manifest, your new view is tied to the settings viewport in a ui_extension field:

[app manifest](/stripe-apps/reference/app-manifest)

This code shows how a view is a pairing of a React component plus a specified viewport. In this case, the AppSettings view root component appears on the settings page of the Stripe Dashboard—the settings viewport.

The SettingsView view root component isn’t tied to a specific object, but tied instead to the settings viewport. The settings viewport maps to predefined locations in the Dashboard, outside of the app drawer.

[Preview your settings page](#preview-settings-page)

## Preview your settings page

While previewing your app locally, test your SettingsView at https://dashboard.stripe.com/test/apps/settings-preview to see what it looks like.

[https://dashboard.stripe.com/test/apps/settings-preview](https://dashboard.stripe.com/test/apps/settings-preview)

After you upload your app, your SettingsView renders on the app settings page in the Dashboard. To see it live, go to https://dashboard.stripe.com/settings/apps/YOUR_APPLICATION_ID and replace YOUR_APPLICATION_ID with the ID you specified when creating your app.

[Save the values](#save-the-values)

## Save the values

When a user configures their settings, your app needs to apply those settings. Provide a function to pass to the SettingsView component for handling the save event. Clicking the Save button triggers the save event.

The onSave callback function receives an object of values. This object maps any form elements into key value pairs where the element name attribute is the key and the element value attribute is the value:

[https://www.my-api.com/](https://www.my-api.com/)

For more information, see the SettingsView reference.

[SettingsView reference](/stripe-apps/components/settingsview)

[Store and retrieve settings](#store-and-retrieve-settings)

## Store and retrieve settings

To handle storage and retrieval of the settings values, connect the SettingsView component to an app backend or a third-party service that includes application settings.

[app backend](/stripe-apps/build-backend)

See a settings UI example.

[settings UI example](https://github.com/stripe/stripe-apps/tree/master/examples/settings-view)

[Display a success message](#display-success-message)

## Display a success message

Make sure your UI tells users they’ve successfully saved their settings choices. Use the statusMessage property to display a success message when a user clicks the save button.

An example of SettingsView displaying a status message.

Here’s the code for this example, where a SettingsView generates a status message to the left of the save button:

[https://www.my-api.com/](https://www.my-api.com/)

You can also create your own unique designs to communicate status to your app’s users using UI components.

[UI components](/stripe-apps/components)

## See also

- Extension SDK reference

[Extension SDK reference](/stripe-apps/reference/extensions-sdk-api)

- UI components

[UI components](/stripe-apps/components)

- Build a UI

[Build a UI](/stripe-apps/build-ui)
