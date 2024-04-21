htmlBalances | Stripe Documentation[Skip to content](#main-content)Balances[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fbalances)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fbalances)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# Balances

Show balance information and allow your connected accounts to perform payouts.Renders the balance summary and the payout schedule. It can also allow the connected account to perform instant or manual payouts.

NoteThis component is part of the payouts component.

When creating an Account Session, enable balances by specifying balances in the components parameter. You can enable or disable individual features of the balances component by specifying the features parameter under balances:

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[balances][enabled]"=true \
  -d "components[balances][features][instant_payouts]"=true \
  -d "components[balances][features][standard_payouts]"=true \
  -d "components[balances][features][edit_payout_schedule]"=true`After creating the account session and initializing ConnectJS, you can render the balances component in the front end:

balances.js[JavaScript](#)`// Include this element in your HTML
const balances = stripeConnectInstance.create('balances');
container.appendChild(balances);`Enabling Instant Payouts might require additional steps:

- If your platform collects fees for a connected account, you must set up Instant Payout monetization in the[Dashboard](https://dashboard.stripe.com/settings/connect/payouts/instant-payouts).
- If your platform is liable for a connected account’s negative balances, your platform must be in a supported country and the account must be in the[same country as the platform](/connect/instant-payouts#eligible-connected-accounts).
- If Stripe is liable for a connected account’s negative balances,[Stripe controls eligibility](/payouts/instant-payouts#eligibility-and-daily-volume-limits)for the account.

NoteTo use standard manual payouts, the connected account needs to have their payout schedule set to manual. You can enable payout schedule editing in the payouts component by setting the edit_payout_schedule feature to true.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`