htmlTax registrations | Stripe Documentation[Skip to content](#main-content)Tax registrations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Ftax-registrations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Ftax-registrations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# Tax registrationsBeta

Learn how to allow connected accounts to manage their tax registrations for Stripe Tax.BetaThis Connect embedded component is in beta. Request access below.

The Tax registrations component gives your connected accounts control over their tax compliance. Your connected accounts interact with this component by managing their tax registrations directly in your platform. This component is suitable for software platforms, which means that your connected accounts are liable to collect taxes.

If you’re a platform integrating Stripe Tax, you must collect information about the registrations with tax authorities of your connected accounts in the applicable jurisdictions. Your connected accounts need to register with their tax authorities before they add their tax registrations in your platform. To correctly calculate and collect taxes for your platform, you must collect the tax registrations of your connected accounts.

The Tax registrations component uses the Tax Registrations API to display a list of tax registrations to your connected accounts. To calculate tax on their payments in a location, connected accounts need to add their tax registration with the Tax registrations component. If the connected account wish to stop calculating tax in a certain location, they can end the tax registration in the component.

## Requirements

- Your integration must follow the[software platforms guide](/tax/tax-for-platforms)for[Tax on Connect](/tax/connect). This means that your connected accounts are liable to collect taxes.
- If you haven’t already, render the[Tax settings component](/connect/supported-embedded-components/tax-settings). You need both the Tax settings component and the Tax registrations component to provide tax compliance control to your connected accounts.

## Integrate the tax registrations component

When creating an Account Session, enable tax registrations by specifying tax_registrations in the components parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[tax_registrations][enabled]"=true`After creating the account session and initializing ConnectJS, you can render the tax registrations component in the frontend:

taxRegistrationPage.jsx[React](#)`// Include this React component
import {
  ConnectTaxRegistrations,
  ConnectComponentsProvider,
} from "@stripe/react-connect-js";

return (
  <ConnectComponentsProvider connectInstance={stripeConnectInstance}>
    <div>
      <h2>Tax Registrations</h2>
      <ConnectTaxRegistrations />
    </div>
  </ConnectComponentsProvider>
);`## Request early access  Beta

Are you looking to offer sales tax, VAT, and GST compliance to your connected accounts?We plan to offer early access to embedded components for tax, which are UI widgets you can integrate into your platform to enable tax compliance for your connected accounts. To request early access, enter your email below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Tax on Connect](/tax/connect)
- [Tax for software platforms](/tax/tax-for-platforms)
- [Tax settings component](/connect/supported-embedded-components/tax-settings)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Requirements](#requirements)[Integrate the tax registrations component](#integration)[Request early access](#request-access)[See also](#see-also)Products Used[Tax](/tax)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`