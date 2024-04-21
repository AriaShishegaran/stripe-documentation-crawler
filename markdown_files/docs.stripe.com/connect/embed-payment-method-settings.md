htmlEmbed the payment methods settings component | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fembed-payment-method-settings)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fembed-payment-method-settings)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Embed the payment methods settings componentBeta

Embed a payment methods settings component into your website.After you integrate with dynamic payment methods, you can embed the payment methods settings component into your website to allow your users to manage their payment methods without the need to access the Stripe Dashboard.

The component uses the Payment Method Configurations and Account Capabilities APIs to capture your connected accounts’ payment method setting preferences. The component is a low-code, customizable alternative to building a custom payment method settings UI for your connected accounts.

[Enable dynamic payment methods](#enable-dynamic-payment-methods)Follow the steps in upgrading to dynamic payment methods.

[Integrate with Connect embedded components](#integrate-with-connect-embedded-components)Request access to the embedded component beta and learn how to integrate with Payment Method Configurations.

[Have your connected accounts enable payment methods](#have-your-connected-accounts-enable-payment-methods)Your connected accounts can use the component to enable payment methods and provide compliance information without the need to access the Stripe Dashboard. If a connected account needs to provide additional compliance information to use a payment method, the component prompts them for the information and collects it up-front.

NoteThe embedded payment method settings component is currently available for connected accounts in the US that you (the platform) collect updated information from when requirements change. This includes Custom connected accounts.

We support the following payment methods in the embedded component:

Affirm, Afterpay Clearpay, Apple Pay, Bancontact, BLIK, Cards, EPS, giropay, Google Pay, iDEAL, Klarna, Link, P24, Sofort, and Zip.

## See also

- [Connect integration guide](/connect/charges)
- [Upgrading to dynamic payment methods](/connect/dynamic-payment-methods)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Enable dynamic payment methods](#enable-dynamic-payment-methods)[Integrate with Connect embedded components](#integrate-with-connect-embedded-components)[Have your connected accounts enable payment methods](#have-your-connected-accounts-enable-payment-methods)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`