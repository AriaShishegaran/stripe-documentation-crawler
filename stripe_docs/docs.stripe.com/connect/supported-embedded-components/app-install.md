# App installBeta

Renders a component that enables your connected account to install an App.

For full integration details, see Accounting software integrations.

[Accounting software integrations](/stripe-apps/accounting-software-integrations)

When creating an Account Session, enable app_install by specifying app_install in the components parameter.

[creating an Account Session](/api/account_sessions/create)

The app_install component is in private beta, so the Stripe SDKs don’t include it yet. To enable it when creating an account session, use this code snippet with the Stripe beta SDK:

After creating the account session and initializing ConnectJS, you can render the app_install component in the front end:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

This embedded component supports the following parameters:

[here](/stripe-apps/accounting-software-integrations#app-select)

## Request early access  Beta

Sign in to request access to this Connect embedded component in beta.

[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-install)

If you don’t have a Stripe account, you can register now.

[register now](https://dashboard.stripe.com/register)
