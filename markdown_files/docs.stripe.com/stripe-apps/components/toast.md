htmlToast | Stripe Documentation[Skip to content](#main-content)Toast[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftoast)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftoast)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Toast

Inform users of temporary status.To add the Toast component to your app:

`import { showToast } from "@stripe/ui-extension-sdk/utils";``const App = () => {
  useEffect(() => {
    showToast('Changes saved', {type: "success"});
  }, [])
};`Render a toast at the bottom of your view to inform the user about the status of an action. For example, a toast can show a user whether an API call succeeded or failed.

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
}`## See also

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