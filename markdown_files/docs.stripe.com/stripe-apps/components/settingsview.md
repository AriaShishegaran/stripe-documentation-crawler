htmlSettingsView | Stripe Documentation[Skip to content](#main-content)SettingsView[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fsettingsview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fsettingsview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# SettingsView

Let users change details about how the app works with their account.You can define a specialized settings view to let users change specific details about how the app works with their account. For example, an app that uses a third-party API like Zendesk could use SettingsView to authorize a user with their Zendesk account. For more details, learn how to add a settings page for your app.

![](https://b.stripecdn.com/docs-statics-srv/assets/settingsview.ca0e43bcc311ea9819da61b2949e6ed1.png)

What SettingsView looks like

SettingsView is a view root component, just like ContextView, containing all other UI elements. It’s the only view that isn’t tied to a specific object, but tied instead to the settings viewport. The settings viewport maps to predefined locations in the Dashboard, outside of the app drawer.

SettingsView renders on the app settings page in the Dashboard after you upload an app. While previewing your app locally, you can preview the SettingsView in the Dashboard at https://dashboard.stripe.com/test/apps/settings-preview.

To use SettingsView, you must add a view with the settings viewport to your app manifest. An application with a settings view would have an app manifest with a ui_extension field that would look something like this:

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
}`### Props

PropTypeDescriptionchildrenRequired`ReactNode`The contents of the SettingsView, usually a Form or some
other content surrounding a form.onSave`((values: { [key: string]: string; }) => void)`If provided, a "Save" button will be rendered with the SettingsView.
This callback will be called when the button is clicked.statusMessage`string`A string to display a status such as "Saved" or "Error"
in the footer of the view.Example![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

This example shows how to fetch settings from an external API, display them, and save changes.

`import {useState, useEffect, useCallback} from 'react';
import {
  Box,
  TextField,
  SettingsView,
} from '@stripe/ui-extension-sdk/ui';

type FormStatus = 'initial' | 'saving' | 'saved' | 'error';

const AppSettings = ({ userContext }: any) => {
  const [storedValue, setStoredValue] = useState<string>('');
  const [status, setStatus] = useState<FormStatus>('initial');

  // use the current user id to retrieve the stored value from an external api
  const key = userContext.id;

  useEffect(() => {
    const fetchSetting = async (key: number) => {
      try {
        const response = await fetch(`https://www.my-api.com/${key}`)
        const storedSettingValue = await response.text()
        if (storedSettingValue) {
          setStoredValue(storedSettingValue)
        }
      } catch (error) {
        console.log('Error fetching setting: ', error)
      }
    };
    fetchSetting(key);
  }, [key]);

  const saveSettings = useCallback(async (values) => {
    setStatus('saving');
    try {
      const { greeting } = values;
      const result = await fetch(
        'https://www.my-api.com/',
        {
          method: 'POST',
          body: JSON.stringify(values)
        }
      );
      await result.text();
      setStatus('saved');
      setStoredValue(greeting);
    } catch (error) {
      console.error(error);
      setStatus('error');
    }
  }, []);

  const getStatusLabel = useCallback(() => {
    switch(status) {
      case 'saving':
        return 'Saving...';
      case 'saved':
        return 'Saved!';
      case 'error':
        return 'Error: There was an error saving your settings.';
      case 'initial':
      default:
        return '';
    }
  }, [status])
  const statusLabel = getStatusLabel();

  return (
    <SettingsView
      onSave={saveSettings}
      statusMessage={statusLabel}
    >
      <Box
        css={{
          padding:'medium',
          backgroundColor: 'container',
        }}
      >
        <Box
          css={{
              font: 'lead'
          }}
        >
          Please enter a greeting
        </Box>
        <Box
          css={{
              marginBottom: 'medium',
              font: 'caption'
          }}
        >
          Saved value: {storedValue || 'None'}
        </Box>
        <TextField
          id="greeting"
          name="greeting"
          type="text"
          label="Greeting:"
          size="medium"
        />
      </Box>
    </SettingsView>
  );
};

export default AppSettings;`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`