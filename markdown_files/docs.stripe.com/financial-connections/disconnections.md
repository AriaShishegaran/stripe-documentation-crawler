htmlDisconnect a Financial Connections account | Stripe Documentation[Skip to content](#main-content)Disconnections[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fdisconnections)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fdisconnections)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Disconnect a Financial Connections account

Disconnect a user’s Financial Connections Account if you no longer need data access or if your user writes into you requesting disconnection. Alternatively, your users can disconnect their accounts themselves.

Although you can’t refresh data on a disconnected account, you can access previously refreshed account data. Disconnecting an account only removes your ability to refresh data; it doesn’t cause any associated PaymentMethods to become unusable.

To regain access to new account data, your user needs to re-authenticate their account through the authentication flow.

[Disconnect a Financial Connections accountServer-side](#disconnect-an-account)To disconnect an account, use the disconnect API:

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/financial_connections/accounts/{{ACCOUNT_ID}}/disconnect \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`This request returns the account with an updated status to reflect the successful disconnection.

`{
  "id": "fca_zbyrdjTrwcYZJZc6WBs6GPid",
  "object": "financial_connections.account",
  "account_holder": {
    "customer": "cus_NfjonN9919dELB",
    "type": "customer"
  },
  "institution_name": "PNC Bank",
  "status": "disconnected",
  // ...
}`After account disconnection, Stripe emits a financial_connections.account.disconnected webhook.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`