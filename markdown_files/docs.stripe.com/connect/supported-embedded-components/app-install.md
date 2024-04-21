htmlApp install | Stripe Documentation[Skip to content](#main-content)App install[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-install)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-install)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# App installBeta

Show a button to install an App.Renders a component that enables your connected account to install an App.

For full integration details, see Accounting software integrations.

When creating an Account Session, enable app_install by specifying app_install in the components parameter.

NoteThe app_install component is in private beta, so the Stripe SDKs don’t include it yet. To enable it when creating an account session, use this code snippet with the Stripe beta SDK:

main.rb[Ruby](#)`Stripe.api_key = '{{sk_INSERT_YOUR_SECRET_KEY}}'
Stripe.api_version = '2023-10-16; embedded_connect_beta=v2;'
account_session = Stripe::AccountSession.create({
  account: '{{CONNECTED_ACCOUNT_ID}}',
  components: {
    app_install: {enabled: true}
  }
})`After creating the account session and initializing ConnectJS, you can render the app_install component in the front end:

app_install.jsx[React](#)`// Include this React component
import {useCreateComponent, useAttachAttribute} from '@stripe/react-connect-js';
export const ConnectAppInstallWithAttributes = ({
  appId,
}: {
  appId: string;
}): JSX.Element | null => {
const {wrapper, component: appInstall} = useCreateComponent(
  'stripe-connect-app-install' as any
);

useAttachAttribute(appInstall, 'app' as any, appId);
return wrapper;
};`This embedded component supports the following parameters:

HTML + JSReactSetterTypeDescription`setApp``string`Sets the ID of the App your connected account can install. See available apps[here](/stripe-apps/accounting-software-integrations#app-select).`setOnAppInstallStateFetched``() => void`Stripe sends this event when the component renders.`setOnAppInstallStateChanged``() => void`Stripe sends this event when an app finishes installing or uninstalling.## Request early access  Beta

Sign in to request access to this Connect embedded component in beta.

If you don’t have a Stripe account, you can register now.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`