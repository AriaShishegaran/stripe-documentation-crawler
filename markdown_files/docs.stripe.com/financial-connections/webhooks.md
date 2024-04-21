htmlGet real-time updates from Financial Connections with webhooks | Stripe Documentation[Skip to content](#main-content)Webhooks[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fwebhooks)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fwebhooks)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Get real-time updates from Financial Connections with webhooks

Use webhooks to get notifications about activity on Financial Connections accounts.After you collect a Financial Connections Account, you can access account data or listen for account changes with the Financial Connections API and associated webhooks.

Core webhooks notify you of account-level updates and newly created accounts. These include:

- `financial_connections.account.created`
- `financial_connections.account.deactivated`
- `financial_connections.account.reactivated`

Other webhooks notify you when Stripe completes asynchronous data refreshes for accounts that your customers have connected.

EventDescription`financial_connections.account.created`Sent when a customer links a new account. If they link multiple accounts, it emits multiple events (one per account).`financial_connections.account.deactivated`Sent when the[status](/api/financial_connections/accounts/object#financial_connections_account_object-status)of your user’s account moves from`active`to`inactive`. New data refreshes aren’t allowed on`inactive`accounts, but previously refreshed data stays available.`financial_connections.account.reactivated`Sent when the[status](/api/financial_connections/accounts/object#financial_connections_account_object-status)of your user’s account moves from`inactive`to`active`. After an account moves from`inactive`to`active`, you can refresh account data again.`financial_connections.account.disconnected`Sent on account disconnection. See the[disconnections guide](/financial-connections/disconnections)for further detail.`financial_connections.account.refreshed_balance`Sent after a[balance](/financial-connections/balances)refresh is complete.`financial_connections.account.refreshed_ownership`Sent after an[ownership](/financial-connections/ownership)refresh is complete.`financial_connections.account.refreshed_transactions`Sent after a[transaction](/financial-connections/transactions)refresh is complete.## See also

- [Webhook documentation](/webhooks)
- [Event object reference](/api/events)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`