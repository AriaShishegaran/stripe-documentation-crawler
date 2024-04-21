htmlAlternative Currency Payouts for Connect marketplaces and platforms | Stripe Documentation[Skip to content](#main-content)Alternative Currency Payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Falternative-currency-payouts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Falternative-currency-payouts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Alternative Currency Payouts for Connect marketplaces and platforms

Offer your connected accounts the ability to pay out in alternative currencies.Available in:### Non-Connect users

Are you a direct Stripe Dashboard user looking to pay yourself out in non-primary currencies? See Alternative Currency Payouts for Direct users.

Alternative Currency Payouts allow your connected accounts to maintain balances and make payouts domestically in currencies other than their primary currency, or make payouts non-domestically in the account’s local currency. Connected accounts can hold and payout funds in up to 18 supported currencies needed to pay suppliers, process refunds, and so on, without having to re-convert funds.

## Enable Alternative Currency Payouts

### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies only to Express and Custom accounts.Enable Alternative Currency Payouts in the Connect payouts settings of the Dashboard. Your account must be in a supported region to access these settings.

After you enable Alternative Currency Payouts, your users can access all alternative currencies that are supported in their region. For a full list of supported currencies, see supported alternative currencies.

NoteConnected accounts must be in the same region as your platform to use Alternative Currency Payouts. For example, both you and your connected account could be in Australia, or if you’re in Europe, your connected account could be in any European country.

You can prevent new connected accounts from using Alternative Currency Payouts by disabling it with the same settings in the Dashboard. However, this doesn’t disable it for connected accounts that are already using it. To disable Alternative Currency Payouts for connected accounts that are already using it, use the Delete external bank accounts API to remove the connected account’s external accounts that are in an alternative currency or offshore.

## Add external accounts

After you enable Alternative Currency Payouts, your connected accounts can start using it by adding an alternative currency external account.

DashboardAPIIf your connected account has access to the Express Dashboard, you can send them a Login Link to update their payout methods to add an alternative currency external account.

After your connected account has an external account in an alternative currency, charges presented in that currency accrue towards the alternative currency’s balance. Your connected accounts can pay out their alternative currency balances in the same way as a primary currency balance. However, each supported currency is subject to a payout minimum and fee, as described in the following section.

To learn more about processing charges in multiple currencies with Connect, see Working with multiple currencies.

## Pricing

Stripe charges platforms a 1% fee for all Alternative Currency Payouts made by their users. Each currency has a minimum fee. For a full list of fees, see the supported alternative currencies table.

Stripe deducts your connected accounts’ Alternative Currency Payouts fees from your platform balance in the alternative currency. For example, if your connected account makes an alternative currency payout in USD, we charge the fee to your platform balance in USD when possible. If your platform account doesn’t support the payout currency, Stripe converts the fee to your default currency and deducts it from your primary balance. See conversion on Stripe fees for more details.

## Request early access

Use the following form to request updates on beta features as we expand Alternative Currency Payouts features and regional support.

Interested in getting early access to new Alternative Currency Payouts features?Enter your email address below and our team will contact you when we're ready to provide access.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Enable Alternative Currency Payouts](#enable-alternative-currency-payouts)[Add external accounts](#add-external-accounts)[Pricing](#pricing)[Request early access](#request-early-access)Related Guides[Alternative Currency Payouts for Stripe Dashboard users](/docs/payouts/alternative-currencies)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`