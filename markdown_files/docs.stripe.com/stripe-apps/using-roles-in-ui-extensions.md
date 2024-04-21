htmlUsing roles in UI extensions | Stripe Documentation[Skip to content](#main-content)Assign roles in UI extensions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fusing-roles-in-ui-extensions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fusing-roles-in-ui-extensions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Using roles in UI extensions

Learn how to include user roles in UI Extensions to tailor functionality to different roles.Stripe Apps UI extensions can read the active user’s role in the Dashboard. Apps can expose different functionality to different user roles.

The UI Extension SDK provides valuable information about the end user of your app. The roles field of the userContext object gives a list of the active user’s roles. You can tailor the app’s content based on the user’s role, using the roles in the user context.

## How to determine the user’s Dashboard role

Extensions have a userContext prop that’s populated with information about the active Dashboard user. This object has a roles field, which is an array of RoleDefinition objects for each role that the active user is attributed to.

A role definition has these fields:

Field nameTypeExampletype‘builtIn’ | ‘custom’builtInSpecifies the role type. Custom roles are only available to[private apps](/stripe-apps/distribution-options#share-with-team-members).namestringDeveloperThe name of the user role.The name field provides the name of the user role, and you can use it to modify the functionality of your UI Extension.

## Custom user roles (private apps only)

Each role definition has a type field, which specifies the role type. The type field can either be ‘builtIn’ or ‘custom’. Because custom roles are specific to a given account, these roles are only available for private apps.

## Tailoring content based on the Dashboard role

A common use of this information is to conditionally display content based on the user role. Below is an example app that shows content tailored to particular user roles.

`import { Badge, Box, Inline, ContextView } from "@stripe/ui-extension-sdk/ui";
import type { ExtensionContextValue } from "@stripe/ui-extension-sdk/context";

const App = ({ userContext }: ExtensionContextValue) => {
  const isAdmin = userContext?.roles?.some(role => role.name === 'Administrator');
  const isDeveloper = !isAdmin && userContext?.roles?.some(role => role.name === 'Developer');
  const isaAnotherRole = !isDeveloper && !isAdmin;

  return (
    <ContextView
      title="Role based access"
    >
      <Box>
        <Box css={{ paddingBottom: 'large'}}>Active user role(s): {userContext?.roles?.map(role => <Badge key={role.name}>{role.name}</Badge>)}</Box>

        { isAdmin && (<Box>Only <Inline css={{ fontWeight: 'semibold' }}>admin</Inline> users can see this message.</Box>) }
        { isDeveloper && (<Box>Only <Inline css={{ fontWeight: 'semibold' }}>developers</Inline> users can see this message.</Box>) }
        { isaAnotherRole && (<Box>Only users who are not admins or developers can see this message.</Box>) }
      </Box>
    </ContextView>
  );
};

export default App;`![A screenshot of the result of the example code above for an Administrator user](https://b.stripecdn.com/docs-statics-srv/assets/roles-example.7fb1048ac4656aee8a39a33d9179ad26.png)

The result of the example app when viewing the app as an Administrator user

## See also

- [Build a UI](/stripe-apps/build-ui)
- [Extension SDK API reference](/stripe-apps/reference/extensions-sdk-api)
- [User roles](/get-started/account/teams/roles)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How to determine the user’s Dashboard role](#how-to-determine-the-user’s-dashboard-role)[Custom user roles (private apps only)](#custom-user-roles-(private-apps-only))[Tailoring content based on the Dashboard role](#tailoring-content-based-on-the-dashboard-role)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`