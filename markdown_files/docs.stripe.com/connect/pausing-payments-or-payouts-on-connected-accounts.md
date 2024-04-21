htmlPause payments and payouts on connected accounts | Stripe Documentation[Skip to content](#main-content)Pause payments and payouts on accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpausing-payments-or-payouts-on-connected-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpausing-payments-or-payouts-on-connected-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Risk management with Connect](/docs/connect/risk-management)# Pause payments and payouts on connected accounts

Support risk management by controlling the flow of funds into and out of your connected accounts.Platforms can pause payments or payouts on accounts where they’re liable for negative balances, including Express and Custom accounts, through the Connected Account details Dashboard page. Unlike rejecting an account, you can pause payments or payouts regardless of the connected account’s balance. You can unpause payments or payouts at any time through the same page.

![Risk Action Dropdown](https://b.stripecdn.com/docs-statics-srv/assets/risk-action-dropdown.2ae7b4d238c08427d9a9f67fbbeda87f.png)

NoteYou can only pause payments in live mode. The Connected Account details page for a test mode account doesn’t include the payments pause function.

After performing an action on a connected account, you can view the change in the account’s status, which is reflected in the Accounts API. In the API response for the connected account, the charges_enabled or payouts_enabled fields return false depending on the action taken, and the requirements hash has a disabled_reason of platform_paused.

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  ...
  "charges_enabled": false,
  "payouts_enabled": false,
  "requirements": {
    "disabled_reason": "platform_paused"
  }
}`### Filter connected accounts by risk action

By visiting the Connected Account list page, you can filter for the accounts that you have restricted either payments or payouts for.

![Filter by risk action](https://b.stripecdn.com/docs-statics-srv/assets/risk-action-filter.e5de33081fc98d114e3082284a251f6f.png)

### Connected account notifications

Actioned accounts with access to the Express Dashboard see a notice there, explaining that their platform paused payments or payouts on their account, and telling them to direct any questions to their platform.

Actioned accounts without access to a Stripe-hosted Dashboard, including Custom accounts, don’t see any communication from Stripe. You’re responsible for notifying them when you pause their payments or payouts.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`