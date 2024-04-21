htmlPayment method settings | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayment-method-settings)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayment-method-settings)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Payment method settingsBeta

Display a configurable list of payment methods that connected accounts can offer during checkout.Render a connected account’s Payment Method Configuration to enable customization of payment methods displayed at checkout. Connected accounts can customize their checkout payment methods and provide the necessary compliance details for their usage.

BetaThis Connect embedded component is in beta. Request access below.

NoteThe embedded payment method settings component is currently available for connected accounts in the US that you (the platform) collect updated information from when requirements change. This includes Custom connected accounts.

We support the following payment methods in the embedded component:

Affirm, Afterpay Clearpay, Apple Pay, Bancontact, BLIK, Cards, EPS, giropay, Google Pay, iDEAL, Klarna, Link, P24, Sofort, and Zip.

The embedded payment method settings uses the Payment Method Configurations and Account Capabilities APIs to display a list of customizable payment methods to your connected accounts. If a connected account requires additional compliance data prior to requesting the payment method capability, the component indicates this and collects the necessary information in advance.

## Requirements

Your integration must use dynamic payment methods to automatically apply the connected account’s preferences during checkout. In prebuilt payment UIs such as Payment Element and Checkout, Stripe handles the logic for displaying eligible payment methods for each transaction.

## Integrate with Payment Method Configurations

When creating an Account Session, enable payment method settings by specifying payment_method_settings in the components parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[payment_method_settings][enabled]"=true`After creating the account session and initializing ConnectJS, you can render the payment method settings component in the frontend:

payment-method-settings.js[JavaScript](#)`// Include this element in your HTML
const paymentMethodSettings = stripeConnectInstance.create('payment-method-settings');
container.appendChild(paymentMethodSettings);`### Platform-level controls

The embedded payment method settings component respects the platform-level defaults that you configure in the Dashboard or the Payment Method Configurations API.

For payment methods that you configure as On by default or Off by default, the connected account can override that preference in the component. If you have set a payment method to Blocked, it’s completely hidden in the component.

### Multiple payment method configurations

The embedded payment method settings component currently shows the connected account’s default payment method configuration. During the beta, the component supports multiple configurations with a component attribute that accepts a configuration ID.

## Request early access  Beta

Sign in to request access to this Connect embedded component in beta.

If you don’t have a Stripe account, you can register here.

## See also

- [Connect integration guide](/connect/charges)
- [Upgrading to dynamic payment methods](/connect/dynamic-payment-methods)
- [Payment Method Configurations API](/connect/payment-method-configurations)
- [Account Capabilities API](/connect/account-capabilities)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Requirements](#requirements)[Integrate with Payment Method Configurations](#integration)[Request early access](#request-access)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`