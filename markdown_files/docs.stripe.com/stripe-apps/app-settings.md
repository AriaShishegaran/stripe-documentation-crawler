htmlAdd an app settings page | Stripe Documentation[Skip to content](#main-content)App settings page[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fapp-settings)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fapp-settings)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Add an app settings page

To let users configure settings for your app, create an app settings page in the Stripe Dashboard.When you upload your app to Stripe, we create an app settings page in the Stripe Dashboard. The rest of the page is open for you to create custom settings.

## The user experience of app settings

An account administrator who installs your app can use the settings page in several ways:

- Configuring your app for their use case: For example, say a business on Stripe wants to synchronize payments data from the last seven days with another application. Your settings page can provide a dropdown menu to let admin users select 1 week as the time period. The configuration applies globally on the account, meaning all users on that Stripe account now see data from the past week in your app.
- Authenticating users: If your app connects to a different application—outside of Stripe—you need a place for Stripe users to log in to the other app, pass credentials, and handle authentication. The settings page is the best place for users to link accounts in this way. For example, an app that uses a third-party API like Zendesk needs a`SettingsView`to authenticate a user with their Zendesk account.
- Uninstalling an app: The only place to uninstall an app is the settings page. You can’t remove the uninstall button from the settings page. There are also buttons for users to report your app and view its marketplace listing if you have one.

## What you can do with it

By default, the settings page includes buttons for uninstalling and reporting your app, plus various app details. To populate the page with custom settings, use SettingsView. This view root component renders in the settings page. Add UI components, like tabs and form fields, to create the user experience you want.

![SettingsView in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/settingsview.ca0e43bcc311ea9819da61b2949e6ed1.png)

What SettingsView looks like in the Stripe Dashboard

# How to customize the settings page

Populate your app’s empty settings page by defining a settings view and composing a UI to let your users set up and configure your app.

You have control over the design of your app settings page. In the developer preview mode, the settings page appears as a smaller view. In live mode, your settings page is a full screen.

[Add a settings view](#define-settingsview)Define a settings view with the CLI:

Command Line`stripe apps add settings`You can name your settings component anything you want. The generated settings view is available in the src/views directory. In the app manifest, your new view is tied to the settings viewport in a ui_extension field:

`{
  ...,
  "ui_extension": {
    "views": [
      ...,
      {
        "viewport": "settings",
        "component": "AppSettings"
      }
    ],
  }
}`This code shows how a view is a pairing of a React component plus a specified viewport. In this case, the AppSettings view root component appears on the settings page of the Stripe Dashboard—the settings viewport.

The SettingsView view root component isn’t tied to a specific object, but tied instead to the settings viewport. The settings viewport maps to predefined locations in the Dashboard, outside of the app drawer.

[Preview your settings page](#preview-settings-page)While previewing your app locally, test your SettingsView at https://dashboard.stripe.com/test/apps/settings-preview to see what it looks like.

After you upload your app, your SettingsView renders on the app settings page in the Dashboard. To see it live, go to https://dashboard.stripe.com/settings/apps/YOUR_APPLICATION_ID and replace YOUR_APPLICATION_ID with the ID you specified when creating your app.

[Save the values](#save-the-values)When a user configures their settings, your app needs to apply those settings. Provide a function to pass to the SettingsView component for handling the save event. Clicking the Save button triggers the save event.

The onSave callback function receives an object of values. This object maps any form elements into key value pairs where the element name attribute is the key and the element value attribute is the value:

`/**
  * An example app settings view that provides two settings fields of first & last name.
  * The fields are combined into a single string value and passed to an external API.
  */
import {SettingsView, TextField} from "@stripe/ui-extension-sdk/ui";

const ExampleAppSettings = () => {
  // Define a callback function to pass to the onSave event.
  const saveSettings = async (values: any) => {
    try {
      // Extract our fields from the values object. The key is the name attribute of the form element.
      const { firstname, lastname } = values;
      // Make a POST request to an external API
      const result = await fetch(
        'https://www.my-api.com/',
        {
          method: 'POST',
          body: JSON.stringify({
            fullName: `${firstname} ${lastname}`,
          }),
        }
      );
      await result.text();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    /* Assign our callback function to the onSave property */
    <SettingsView onSave={saveSettings}>
      { /* A name attribute for each field is required to handle the form data in the onSave callback */ }
      <TextField
        name="firstname"
        label="First name"
      />
      <TextField
        name="lastname"
        label="Last name"
      />
    </SettingsView>
  );
};

export default ExampleAppSettings;`For more information, see the SettingsView reference.

[Store and retrieve settings](#store-and-retrieve-settings)To handle storage and retrieval of the settings values, connect the SettingsView component to an app backend or a third-party service that includes application settings.

See a settings UI example.

[Display a success message](#display-success-message)Make sure your UI tells users they’ve successfully saved their settings choices. Use the statusMessage property to display a success message when a user clicks the save button.

![An example of SettingsView displaying a status message](https://b.stripecdn.com/docs-statics-srv/assets/settingsview-statusmessage.372f7befb8b2104ab42f2cc35ac021d3.png)

An example of SettingsView displaying a status message.

Here’s the code for this example, where a SettingsView generates a status message to the left of the save button:

`import {useState} from 'react';
import {SettingsView, TextField} from "@stripe/ui-extension-sdk/ui";

/**
 * An example app settings view that provides two settings fields of first & last name.
 * The fields are combined into a single string value and passed to an external API.
 * The user is notified of the status of their settings form via the statusMessage property.
 */
const ExampleAppSettings = () => {
  // useState to track the status of the form. Changing the status value triggers a rerender.
  const [status, setStatus] = useState('');

  // Define a callback function to pass to the onSave event.
  const saveSettings = async (values: any) => {
    // Update the form status with a loading message.
    setStatus('Saving...');
    try {
      const { firstname, lastname } = values;
      const result = await fetch(
        'https://www.my-api.com/',
        {
          method: 'POST',
          body: JSON.stringify({
            fullName: `${firstname} ${lastname}`,
          }),
        }
      );
      await result.text();
      // Update the form status with a success message.
      setStatus('Saved!');
    } catch (error) {
      console.error(error);
      // Update the form status with an error message.
      setStatus('There was an error saving your settings.');
    }
  };

  return (
    // Assign our callback function to the onSave property & pass the current value of statusMessage
    <SettingsView
      onSave={saveSettings}
      statusMessage={status}
    >
      <TextField
        name="firstname"
        label="First name"
      />
      <TextField
        name="lastname"
        label="Last name"
      />
    </SettingsView>
  );
};

export default ExampleAppSettings;`You can also create your own unique designs to communicate status to your app’s users using UI components.

## See also

- [Extension SDK reference](/stripe-apps/reference/extensions-sdk-api)
- [UI components](/stripe-apps/components)
- [Build a UI](/stripe-apps/build-ui)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[The user experience of app settings](#the-user-experience-of-app-settings)[What you can do with it](#what-you-can-do-with-it)[Add a settings view](#define-settingsview)[Preview your settings page](#preview-settings-page)[Save the values](#save-the-values)[Store and retrieve settings](#store-and-retrieve-settings)[Display a success message](#display-success-message)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`