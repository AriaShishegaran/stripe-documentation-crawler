htmlAlternative currencies | Stripe Documentation[Skip to content](#main-content)Alternative currencies[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayouts%2Falternative-currencies)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayouts%2Falternative-currencies)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)
[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[After the payment](/docs/payments/after-the-payment)[Payouts](/docs/payouts)# Alternative currencies

Learn how to pay out in currencies other than your primary currency.Available in:### Connect users

Are you a platform and marketplace interested in offering Alternative Currency Payouts to your users? See Alternative Currency Payouts for Connect users.

## Primary and alternative currency payouts

For businesses with international operations that need to settle and pay out in multiple currencies or to multiple countries, Stripe enables payouts for select currencies and countries in addition to your primary currency and domestic bank.

Examples:

- The primary currency for Stripe accounts in France is EUR. All other currencies fall under alternative currencies.
- The primary currency for Stripe accounts in Hong Kong is HKD. All other currencies fall under alternative currencies.

## Alternative currency payouts

At Stripe, a domestic payout is when you pay out to a bank account that’s domiciled in the same country as your Stripe account. You can make domestic payouts using the primary currency for a Stripe account or with an alternative currency. For example, when you pay out in EUR from an account based in France to a France-domiciled bank account, it’s a domestic payout in the primary currency. However, if you make a payout in any other currency to a France-domiciled bank account, it’s a domestic payout but in an alternative currency.

You can also pay out to certain non-domestic bank accounts in the account’s local currency, subject to applicable fees. For example, when you pay out in USD from a France-based account to a US-domiciled bank account, the non-domestic payout is subject to the fees listed below.

With alternative currency payouts, it’s easier to hold funds in up to 18 supported currencies needed to pay suppliers, process refunds, and so on, without having to re-convert funds or use third-party sites.

Alternative currency payouts are available in select currencies for businesses in Hong Kong, Singapore, Australia, and Europe, including the United Kingdom.

If your business is based in a country that’s not currently eligible for alternative currency payouts, we’d love to hear from you as we work to expand.

## Setting up your bank account for alternative currency payouts

To enable alternative currency payouts, you must configure the currencies and bank accounts in your Dashboard.

First, in your Payout Settings, you need to select the settlement currency you want to receive funds in using the Manage currencies button to start accumulating a balance in that currency.

A settlement currency is the currency your bank account uses, and you must select a settlement currency before adding a bank account in that currency. After you add a bank account in that currency, you can receive the accrued balance.

If you select a settlement currency but don’t add a bank account for that currency, funds still accrue and remain in the account balance in the alternative currency until you add a supported bank account. Additionally, removing a bank account from your Dashboard doesn’t disable the settlement currency, so you can still accrue a balance in that currency. You need to disable a currency to stop accruing a balance in that currency.

### Presentment currency payouts

When the presentment currency differs from any of your enabled settlement currencies, the currencies accepted by any of your bank accounts or debit cards, we automatically convert the payment to your default settlement currency before transferring the funds. View Currency conversions for details.

### Connected Accounts

### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies only to Express and Custom accounts.You can enable your connected accounts to pay out in alternative currencies using the toggle under “Alternative currency payouts” in your Connect payout settings.

## Payout fees & minimum payout amount for alternative currency payouts

Loading a table of settlement currencies## See also

- [Supported currencies](/currencies)
- [Currency conversions](/currencies/conversions)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Primary and alternative currency payouts](#primary-and-alternative-currency-payouts)[Alternative currency payouts](#alternative-currency-payouts)[Setting up your bank account for alternative currency payouts](#setting-up-your-bank-account-for-alternative-currency-payouts)[Payout fees & minimum payout amount for alternative currency payouts](#alternative-currency-payouts-fees)[See also](#see-also)Related Guides[Alternative Currency Payouts for Connect marketplaces and platforms](/docs/connect/alternative-currency-payouts)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`