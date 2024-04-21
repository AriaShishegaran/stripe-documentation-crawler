htmlTax settings | Stripe Documentation[Skip to content](#main-content)Tax settings[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Ftax-settings)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Ftax-settings)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# Tax settingsBeta

Learn how to allow connected accounts to set up Stripe Tax.BetaThis Connect embedded component is in beta. Request access below.

The Tax settings component allows your connected accounts to set up Stripe Tax in your platform. Connected accounts can change their head office address and preset tax code with this component. This component is suitable for software platforms, which means that your connected accounts are liable to collect taxes.

To calculate taxes on payments of your connected accounts you have to collect four data points of information:

- The head office address
- The type of product the connected account sells
- The address of the customer
- The registrations of the connected account with the tax authorities

The tax settings component helps you to collect the first two pieces of information of your connected accounts with minimal integration effort.

The embedded tax settings component uses the Tax Settings API to display the head office address and preset tax code to your connected accounts.

## Requirements

- Your integration must follow the[software platforms guide](/tax/tax-for-platforms)for[Tax on Connect](/tax/connect). This means that your connected accounts are liable to collect taxes.
- After integrating the Tax settings component, render the[Tax registrations component](/connect/supported-embedded-components/tax-registrations)to collect tax registration information of your connected accounts. This is a requirement for Tax to calculate tax in a specific location.

## Integrate the tax settings component

When creating an Account Session, enable tax settings by specifying tax_settings in the components parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[tax_settings][enabled]"=true`After creating the account session and initializing ConnectJS, you can render the tax settings component in the frontend:

taxSettingsPage.jsx[React](#)`// Include this React component
import {
  ConnectTaxSettings,
  ConnectComponentsProvider,
} from "@stripe/react-connect-js";

return (
  <ConnectComponentsProvider connectInstance={stripeConnectInstance}>
    <div>
      <h2>Tax Settings</h2>
      <ConnectTaxSettings />
    </div>
  </ConnectComponentsProvider>
);`## Request early access  Beta

Are you looking to offer sales tax, VAT, and GST compliance to your connected accounts?We plan to offer early access to embedded components for tax, which are UI widgets you can integrate into your platform to enable tax compliance for your connected accounts. To request early access, enter your email below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Tax on Connect](/tax/connect)
- [Tax for software platforms](/tax/tax-for-platforms)
- [Tax registrations component](/connect/supported-embedded-components/tax-registrations)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Requirements](#requirements)[Integrate the tax settings component](#integration)[Request early access](#request-access)[See also](#see-also)Products Used[Tax](/tax)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`