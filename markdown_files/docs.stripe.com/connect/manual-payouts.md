htmlUsing manual payouts | Stripe Documentation[Skip to content](#main-content)Manual payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmanual-payouts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmanual-payouts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Using manual payouts

Send manual payouts to your connected accounts.If you set the value of schedule.interval to manual, we hold funds in the accountholder’s balance until you specify otherwise. You must pay out the funds within the time period specified below, based on the business’s country:

CountryHolding PeriodThailand10 daysUnited States2 yearsAll other countries90 daysTo trigger a payout of these funds, use the Payouts API.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "settings[payouts][schedule][interval]"=manual`The Payouts API is only for moving funds from a connected Stripe account’s balance into their external account. To move funds between the platform and a connected account, see creating separate charges and transfers or creating destination charges through the platform.

NoteEscrow has a precise legal definition, and Stripe doesn’t provide escrow services or support escrow accounts. However, you can control payout timing through manual payouts, which allow you to delay payouts to certain accounts. When using manual payouts, you must pay out funds within the time frame for the business’s country.

Delayed payouts can be useful when a delivery is delayed or when there’s a possibility of a refund.

## Regular payouts

The following example sends 10 USD from a connected account’s Stripe balance to their external account:

Command Line[curl](#)`curl https://api.stripe.com/v1/payouts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd`With a standard payout, you can move an amount up to the user’s available balance. To find that amount, perform a retrieve balance call on their behalf.

Stripe tracks balance contributions from different payment sources in separate balances. The retrieve balance response breaks down the components of each balance by source type. For example, to create a payout specifically for a non-credit-card balance, specify the source_type in your request.

Command Line[curl](#)`curl https://api.stripe.com/v1/payouts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=24784 \
  -d currency=usd \
  -d source_type=bank_account`While individual balance components can go negative (such as through refunds or chargebacks), you can’t create payouts for greater than the aggregate available balance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`