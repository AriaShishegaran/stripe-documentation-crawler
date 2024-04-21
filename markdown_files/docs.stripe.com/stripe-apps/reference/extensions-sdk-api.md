htmlExtension SDK API reference | Stripe Documentation[Skip to content](#main-content)Extension SDK[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fextensions-sdk-api)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fextensions-sdk-api)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Extension SDK API reference

An index of all fields, types, and descriptions for the Extension SDK API.UI extensions have access to context props and utility functions that let them interact with an app’s users and the Stripe Dashboard ecosystem. This page documents these values and functions.

## Props

Views are passed props that the extension can use for context on where the extension is being displayed. Your view can take some or all of these props as arguments, and they’re of type ExtensionContextValue.

`import type {ExtensionContextValue} from '@stripe/ui-extension-sdk/context';

const ExampleApp = ({ userContext, environment, oauthContext, appContext}: ExtensionContextValue) => {
  ...
}`### User context

The userContext prop has data about the end user using your app, including these fields:

FieldTypeExamplenamestringJenny RosenThe app user’s nameaccount.countrystringUKThe app user’s countryaccount.idstringacct_1032D82eZvKYlo2CThe app user’s account IDaccount.namestringJenny’s Llama EmporiumThe name of the Stripe accountrolesArray<[RoleDefinition](#roledefinition)>noneA list of the active user’s[user roles](/get-started/account/teams/roles).localestringen-GBThe app user’s system language ID### RoleDefinition

A role definition has these fields:

Field nameTypeExampletype‘builtIn’ | ‘custom’builtInSpecifies the role type. Custom roles are only available to[private apps](/stripe-apps/distribution-options#share-with-team-members).namestringDeveloperThe name of the user role.### Environment

The environment prop has data about the page a user is viewing, including these fields:

FieldTypeExampleviewportIDstringstripe.dashboard.payment.listCurrent viewport rendering your viewmode‘live’ | ‘test’liveThe Stripe API mode the current page is inobjectContext.idstringch_3L0pjB2eZvKYlo2C1u1vZ7aKIn the`ObjectView`objects, this is the ID of the current object the user views in the Dashboard.objectContext.objectstringchargeIn the`ObjectView`objects, this is the type of the current object the user views in the Dashboard.constantsObject`{"API_BASE": "https://api.example.com/v1"}`An object with arbitrary constant values passed from the[app manifest](/stripe-apps/reference/app-manifest)that can be[overridden for local development using the CLI manifest flag](/stripe-apps/reference/app-manifest#extended-manifest).### OAuth context

The oauthContext prop contains information about the current OAuth workflow, if one is underway.

FieldTypeExampleerrorstringnoneOAuth error codecodestringnoneOAuth authorization codestatestringnoneOAuth state used by your appverifierstringnoneOAuth code verifier### App context

The appContext prop contains information about the user’s app install, and has the following fields:

FieldTypeExampleauthorizedPermissionsArray<string>`['event_read', 'charge_write']`App’s current authorized permissionsauthorizedCSP.connectSrcArray<string>`['http://o.ingest.sentry.io/api/']`URLs of permitted third-party APIs. If the URL ends in a slash, all of its children are also permitted.authorizedCSP.imageSrcArray<string>`['https://images.example.com/', 'https://images.example.org']`URLs the[Img](https://stripe.com/stripe-apps/ui-toolkit/components/img)component can load from. If the URL ends in a slash, all of its children are also permitted.## Utility functions

The UI extension SDK provides these functions to help apps interact with the Stripe API and the Dashboard user.

- [clipboardWriteText](#clipboardWriteText)—Write text to the end user’s clipboard.
- [createHttpClient](#createHttpClient)-Get an authenticated Stripe API client.
- [createOAuthState](#createOAuthState)—Obtain values to use when you create an authorization link in an OAuth workflow.
- [fetchStripeSignature](#fetchStripeSignature)—Get a signature from Stripe’s servers.
- [getDashboardUserEmail](#getDashboardUserEmail)—Get the end user’s email address.
- [getUserAuthorizedPermissions](#getUserAuthorizedPermissions)—Get the intersection of the app’s authorized permissions and those of the current Dashboard user.
- [isPermissionAuthorized](#isPermissionAuthorized)—Indicate whether a permission is currently in an app’s authorized permissions.
- [isSourceInAuthorizedCSP](#isSourceInAuthorizedCSP)—Indicate whether a URL is currently in an app’s authorized content security policy.
- [showToast](#showToast)—Show a toast message to the user.
- [useRefreshDashboardData](#useRefreshDashboardData)—Enable your view to update data in the Dashboard.

### clipboardWriteText

Write text to the app user’s clipboard. The user can then paste it as if they had copied it.

ArgumentTypeExampletextstringHello, world!Text to copyTo use this function, first import it from the SDK:

`import {clipboardWriteText} from '@stripe/ui-extension-sdk/utils';`For example, provide a button that copies Hello, world! to the clipboard when pressed. In a real app, you could use this to copy an address, invoice number, or other important detail.

`import {useCallback} from 'react';
import {Button} from '@stripe/ui-extension-sdk/ui';
import {clipboardWriteText} from '@stripe/ui-extension-sdk/utils';

const App = () => {
  const writeToClipboard = useCallback(async () => {
    try {
      await clipboardWriteText('Hello, world!');
      // Writing to the clipboard succeeded
    } catch (e) {
      // Writing to the clipboard failed
    }
  }, []);
  return (
    <Button
      onPress={writeToClipboard}
    >
      Copy to clipboard
    </Button>
  );
};`### createHttpClient

Obtain an authenticated Stripe API client for the installed user’s account. You must use the STRIPE_API_KEY provided by the SDK to give your client the permissions defined in the app manifest.

To use this function, first import it from the SDK and then provide its values to the Stripe constructor from stripe-node.

`import {createHttpClient, STRIPE_API_KEY} from '@stripe/ui-extension-sdk/http_client';
import Stripe from 'stripe';

const stripe = new Stripe(
  STRIPE_API_KEY,
  {
    httpClient: createHttpClient(),
    apiVersion: '2022-11-15'
  }
)`For an example in context, see Build a UI.

### createOAuthState

Obtain state and challenge values to use when you create an authorization link in an OAuth workflow.

To use this function, first import it from the SDK.

`import {createOAuthState} from '@stripe/ui-extension-sdk/utils';`For an example in context, see Add authorization workflows.

### fetchStripeSignature

Get a signature from Stripe’s servers. Your UI extension can use this signature to send signed requests to your app’s backend.

To use this function, first import it from the SDK.

`import {fetchStripeSignature} from '@stripe/ui-extension-sdk/utils';`For more details and an example in context, see server-side logic docs.

### getDashboardUserEmail

Get the app user’s email address.

To use this function, first import it from the SDK.

`import {getDashboardUserEmail} from '@stripe/ui-extension-sdk/utils';`You must also include the user_email_read permission in your app manifest. Add it using a CLI command or edit the app manifest file directly.

Command Line[CLI command](#)`stripe apps grant permission user_email_read "EXPLANATION"`For example, access the app user’s email in a view by getting it using the getDashboardUserEmail function and storing it in a React state variable.

`import {useEffect, useState} from 'react';
import {getDashboardUserEmail} from '@stripe/ui-extension-sdk/utils';

export const useDashboardUserEmail = () => {
  const [email, setEmail] = useState<string | null>(null);

  const fetchEmail = async () => {
    try {
      const {email} = await getDashboardUserEmail();
      setEmail(email);
    } catch(e) {
      console.error(e);
    }
  };

  useEffect(() => {
    fetchEmail();
  }, []);

  return email;
};

const App = () => {
  const dashboardUserEmail = useDashboardUserEmail();
  ...
};`### getUserAuthorizedPermissions

Gets the intersection of the app’s authorized permissions and those of the current Dashboard user.

For instance, if the app’s current authorized permissions are event_read and charge_write, but the current Dashboard user has a view_only role (that is, no edit permissions), calling the function returns the array ['event_read'].

To use this function, first import it from the SDK.

`import {getUserAuthorizedPermissions} from '@stripe/ui-extension-sdk/utils';`### isPermissionAuthorized

Indicate if a permission is in the app’s authorized permissions. Throws an error if the permission isn’t on the app manifest.

ArgumentTypeExamplepermissionstringcharge_readPermission to checkTo use this function, first import it from the SDK.

`import {isPermissionAuthorized} from '@stripe/ui-extension-sdk/utils';`Gating functionality by permission![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

This function can gate app functionality by user authorized permissions.

For instance, on the customer details page, only update customer details if the app user has authorized the customer_write permission.

`import {isPermissionAuthorized} from '@stripe/ui-extension-sdk/utils';

const App = () => {

  const updateCustomer = useCallback(async () => {

    const customerWriteEnabled = await isPermissionAuthorized('customer_write');
    if (customerWriteEnabled){
      await updateCurrentCustomer()
    }
    ...
  })
}`### isSourceInAuthorizedCSP

Indicate if a URL is in the app’s authorized connect sources or image sources.

ArgumentTypeExamplesourcestringhttps://images.example.org/URL to checkTo use this function, first import it from the SDK.

`import {isSourceInAuthorizedCSP} from '@stripe/ui-extension-sdk/utils';`### showToast

Render a toast at the bottom of your view to inform the user about the status of an action. For example, a toast can show a user whether an API call succeeded or failed.

`import {showToast} from '@stripe/ui-extension-sdk/utils';

const App = () => {
  const handleClick = () => {
    fetch(...)
      .then((response) => {
        showToast("Invoice updated", {type: "success"})
        return response.json()
      })
      .catch(() => {
        showToast("Invoice could not be updated", {type: "caution"})
      })
  }

  // Use the `handleClick`...
}`The showToast() function takes two arguments, a message and options. The function is defined as follows:

`type ToastType = "success" | "caution" | "pending" | undefined;
type ToastOptions = { type?: ToastType; action?: string; onAction: () => void; }
(message: string, options?: ToastOptions) => Promise<{
    update: (updateMessage: string, updateOptions?: ToastOptions) => void;
    dismiss: () => void;
}>;`Toast messages can’t exceed 30 characters in length or be empty. If a message is too long or empty, the console logs an error.

Unless they’re of type pending, toasts dismiss automatically.

Is PendingHas ActionTimeout`false``false`4s`false``true`6s`true``false`None`true``true`None`import {showToast} from '@stripe/ui-extension-sdk/utils';

const App = () => {
  const handleClick = async () => {
    const { dismiss, update } = await showToast("Refreshing data", {
      type: "pending",
    });
    try {
      await refreshData();
      dismiss();
    } catch (error) {
      update("Data could not be refreshed", { type: "caution" });
    }
  }

  // Use the `handleClick`...
}`Toasts can also prompt the user to take an action. Clicking the action button automatically dismisses the toast.

`import {showToast} from '@stripe/ui-extension-sdk/utils';

const App = () => {
  const handleClick = async () => {
    let timeout;
    const { dismiss } = await showToast('Message "sent"', {
      action: "Undo",
      onAction: () => {
        clearTimeout(timeout);
        showToast('Message "unsent"');
      },
    });
    timeout = setTimeout(() => {
      sendMessage();
      dismiss();
    }, 3000);
  }

  // Use the `handleClick`...
}`### useRefreshDashboardData

Enable your view to update data in the Dashboard. This function returns another callback function. Store that callback, and call it when Stripe data changes. When you call it, the Dashboard updates to reflect the new values.

To use this function, first import it from the SDK.

`import {useRefreshDashboardData} from '@stripe/ui-extension-sdk/utils';`For instance, on a customer details page, get the callback function that refreshes Dashboard data, and then call it after updating the current customer.

`import {useCallback} from 'react';
import {useRefreshDashboardData} from '@stripe/ui-extension-sdk/utils';

const App = () => {
  const refreshDashboardData = useRefreshDashboardData();

  const updateCustomer = useCallback(async () => {
    try {
      await updateCurrentCustomer();
      await refreshDashboardData();
    } catch (error) {}
  }, [refreshDashboardData]);
}`## See also

- [How UI extensions work](/stripe-apps/how-ui-extensions-work)
- [Viewports reference](/stripe-apps/reference/viewports)
- [Using Roles in UI Extensions](/stripe-apps/using-roles-in-ui-extensions)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Props](#props)[Utility functions](#functions)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`