htmlApp viewport | Stripe Documentation[Skip to content](#main-content)App viewport[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-viewport)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fapp-viewport)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# App viewportBeta

Show a view from an installed App.The App viewport renders a view from an installed App.

For full integration details, see Accounting software integrations.

When creating an Account Session, enable app_viewport by specifying app_viewport in the components parameter.

NoteThe app_viewport component is in private beta, so the Stripe SDKs don’t include it yet. To enable it when creating an account session, use this code snippet with the Stripe beta SDK:

main.rb[Ruby](#)`Stripe.api_key = '{{sk_INSERT_YOUR_SECRET_KEY}}'
Stripe.api_version = '2023-10-16; embedded_connect_beta=v2;'
account_session = Stripe::AccountSession.create({
  account: '{{CONNECTED_ACCOUNT_ID}}',
  components: {
    app_viewport: {enabled: true}
  }
})`After creating the account session and initializing ConnectJS, you can render the app_viewport component in the front end:

app_viewport.jsx[React](#)`// Include this React component
import {useCreateComponent, useAttachAttribute} from '@stripe/react-connect-js';
export const ConnectAppViewportWithAttributes = ({
  appId,
  appData
}: {
  appId: string;
}): JSX.Element | null => {
  const {wrapper, component: appViewport} = useCreateComponent(
    'stripe-connect-app-viewport' as any
  );

  useAttachAttribute(appViewport, 'app' as any, appId);
  useAttachAttribute(appViewport, 'appData' as any, appData);

  return wrapper;
};`This embedded component supports the following parameters:

HTML + JSReactSetterTypeDescription`setApp`Sets the ID of the App your connected account can install. See available apps[here](/stripe-apps/accounting-software-integrations#app-select).`string``setAppData``Record<String, String>`Sets data pertaining to your platform consumed by the App.## Request early access  Beta

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