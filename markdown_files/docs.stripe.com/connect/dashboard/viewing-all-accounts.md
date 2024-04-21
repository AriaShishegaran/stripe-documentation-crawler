htmlView all accounts | Stripe Documentation[Skip to content](#main-content)View all accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard%2Fviewing-all-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard%2Fviewing-all-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Dashboard account management](/docs/connect/dashboard)# View all accounts

Learn how to view all of your connected accounts, and filter them by verification status, balance, volume, and other attributes.The accounts overview page provides multiple ways to view your connected accounts. By default, the All accounts tab is selected. However, the other tabs organize accounts according to their status. Each tab includes the number of accounts with that status. When you select a tab, the results in your accounts list update automatically. You can then narrow these results further by using the filter feature on each tab.

## Status tabs and workflows

Selecting different status tabs on the account overview page automatically updates the filters and columns displayed. The interactive table below provides an overview and description of the columns associated with each tab. You can sort many of the columns listed below can also by clicking on the column heading in the Dashboard.

All accountsRestrictedRestricted soonPendingEnabledCompleteThis tab is displayed by default, and is commonly used to see a high-level view of all your connected accounts.

ColumnDescriptionAccountsThe name of the account.StatusThe[account status](/connect/dashboard#status-badges).BalanceThe total of pending and available balances, converted to your platform’s default currency.VolumeThe total gross volume on the account, converted to your platform’s default currency. This is only displayed for Express and Custom accounts.TypeAccount type (Standard, Express, or Custom).Country (icon)An icon representing the account’s country.ConnectedThe date the account connected to your platform.## Filters

Each tab provides a list of accounts based on a shared status, but you can use filters to narrow the results further. When you apply a new filter, the account list updates automatically.

![screenshot of sample filter](https://b.stripecdn.com/docs-statics-srv/assets/filters.09676e78aad7739ba40cc52c335c523e.png)

Filter accounts by country

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Status tabs and workflows](#tabs-workflows)[Filters](#filters)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`