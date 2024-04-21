htmlFocusView | Stripe Documentation[Skip to content](#main-content)FocusView[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ffocusview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ffocusview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# FocusView

Use FocusView to open a dedicated space for the end user to complete a specific task.A FocusView component can be opened from other View components and allows the developer to open a dedicated space for the end user to complete a specific task. Examples include:

- Enter details to create a new entry in a database
- Go through a wizard to decide on next steps
- Confirm that the user wants to take the action they indicated

![](https://b.stripecdn.com/docs-statics-srv/assets/focusview.f2c4048d934cb15b3e9163c82d993624.png)

What FocusView looks like

FocusView must be a child of ContextView. Don’t wrap the FocusView in a conditional, instead use the shown property to control its visible state. For more information, see ContextView.

To add the FocusView component to your app:

`import {FocusView} from '@stripe/ui-extension-sdk/ui';`### Props

PropTypeDescriptionchildrenRequired`ReactNode`The contents of the FocusView.titleRequired`string`The title of the FocusView. This will be displayed at the top
of the drawer under your app's name.confirmCloseMessages`{ title: string; description: string; cancelAction: string; exitAction: string; }`If provided, confirmCloseMessages will be displayed when the user closes the FocusView.footerContent`ReactNode`React node adjacent to any actions in the footer.primaryAction`ReactElement<Component<ButtonProps>>`A primary call to action ("Save" or "Continue") button placed in the footer.secondaryAction`ReactElement<Component<ButtonProps>>`A secondary call to action ("Cancel") button placed in the footer.setShown`((shown: boolean) => void)`Allows the FocusView to manage shown state if a user requests to close the window, or if
it needs to stay open because of the close confirmation dialog.shown`boolean`Whether the FocusView should be shown or not. This property is maintained by a parent view.onCloseDeprecated`(() => void)`(Deprecated, use `setShown` instead) If the user clicks out of the FocusView or presses
the escape button, this informs the extension that the user has closed the view.Close Confirmation Dialog![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When passing confirmCloseMessages, in order for the close confirmation dialog to work properly in every close scenario, pass the setShown prop so the FocusView can manage its shown state. To control when the close confirmation dialog displays, you can use state to conditionally pass confirmCloseMessages to the FocusView, like in the following example:

Example![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

`import { useState } from "react";
import {
  Box,
  Button,
  ContextView,
  FocusView,
  Select,
} from "@stripe/ui-extension-sdk/ui";

type Mood = "Happy" | "Sad";

const confirmCloseMessages = {
  title: "Your mood will not be saved",
  description: "Are you sure you want to exit?",
  cancelAction: "Cancel",
  exitAction: "Exit",
};

const MoodView = () => {
  const [mood, setMood] = useState<Mood>("Happy");
  const [shown, setShown] = useState<boolean>(false);
  const [confirmClose, setConfirmClose] = useState<boolean>(false);

  const open = () => {
    setConfirmClose(true);
    setShown(true);
  };

  const closeWithoutConfirm = () => {
    setConfirmClose(false);
    setShown(false);
  };

  const closeWithConfirm = () => {
    setShown(false);
  };

  const updateMood = (newMood: Mood) => {
    setMood(newMood);
    closeWithoutConfirm();
  };

  return (
    <ContextView
      title="Mood picker"
      description="This section communicates my extension's feelings"
    >
      <FocusView
        title="Pick your mood"
        shown={shown}
        setShown={setShown}
        confirmCloseMessages={confirmClose ? confirmCloseMessages : undefined}
        secondaryAction={<Button onPress={closeWithConfirm}>Cancel</Button>}
      >
        <Select onChange={(e) => updateMood(e.target.value as Mood)}>
          <option label="">Select mood</option>
          <option label="Happy">Happy</option>
          <option label="Sad">Sad</option>
        </Select>
      </FocusView>
      <Box css={{ stack: "x", gap: "medium" }}>
        <Box
          css={{
            font: "subheading",
            color: mood === "Happy" ? "success" : "info",
          }}
        >
          {mood}
        </Box>
        <Button onPress={open}>Change mood</Button>
      </Box>
    </ContextView>
  );
};

export default MoodView;`## See also

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