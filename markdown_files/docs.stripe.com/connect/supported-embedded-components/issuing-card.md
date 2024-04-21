htmlIssuing card | Stripe Documentation[Skip to content](#main-content)Issuing card[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fissuing-card)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fissuing-card)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# Issuing cardBeta

Show an individual issued card.Renders the details of an individual card issued to your connected accounts.

For full integration details, see Issuing card management.

When creating an Account Session, enable the Issuing card component by specifying issuing_card in the components parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[issuing_card][enabled]"=true`After creating the account session and initializing ConnectJS, you can render the Issuing card component in the front end:

issuing-card.js[JavaScript](#)`// Include this element in your HTML
const issuingCard = stripeConnectInstance.create('issuing-card');
issuingCard.setDefaultCard('{{ISSUING_CARD_ID_ID')
container.appendChild(issuingCard);`This embedded component supports the following attributes:

HTML + JSReactSetterDescriptionType`setDefaultCard`Sets the Issuing[Card](/api/issuing/cards/object#issuing_card_object-id)ID to display upon initial load.`(string) => void``setCardSwitching`Sets whether to render the card dropdown selector. Defaults to true.`(boolean) => void``setFetchEphemeralKey`Sets the callback that fetches the ephemeral key for the card. See[sensitive data display](#sensitive-data-display).`(function) => void`## Request access  Beta

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