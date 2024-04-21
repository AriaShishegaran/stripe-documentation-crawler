htmlCollect a bank account to enhance Connect payouts | Stripe Documentation[Skip to content](#main-content)Connect payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fconnect-payouts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fconnect-payouts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Collect a bank account to enhance Connect payouts

Collect your connected account's bank account and use account data to enhance payouts.Not sure about which Financial Connections integration to use? See our overview of integration options.

Financial Connections enables you to instantly collect tokenized account and routing numbers to facilitate payouts for your Custom connected accounts, which helps you:

- Increase onboarding conversion by eliminating the need for your connected accounts to leave your website or application to locate their account and routing numbers.
- Reduce payout failure rates by eliminating errors that result from manual entry of account and routing numbers.
- Make sure you don’t need to store sensitive data such as account and routing numbers on your server.
- Save development time by eliminating your need to build bank account manual entry forms.
- Enable your users to connect their accounts in fewer steps with Link, allowing them to save and quickly reuse their bank account details across Stripe merchants.



Optionally, Stripe platforms in the US can request permission from your Custom account to retrieve additional data on their Financial Connections account. Consider accessing balances, transactions, and ownership information to optimize your onboarding process.

Retrieving additional account data can help you:

- Mitigate fraud when onboarding accounts by verifying the ownership details of their bank account, such as the name and address of the account holder.
- Underwrite accounts for financial services that you might offer on your platform with balances and transactions data.

## Get started

For Custom account types, enable Stripe Financial Connections either within the Connect Onboarding for Custom Accounts web form or directly within your own onboarding flow.

Standard and Express account onboarding always use Financial Connections. Access to additional bank account data is unavailable on these account types.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`