htmlDebit connected accounts | Stripe Documentation[Skip to content](#main-content)Debit Express and Custom connected accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-debits)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-debits)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Account balance](/docs/connect/account-balances)# Debit connected accounts

Collect funds from a connected account by debiting its Stripe balance.At times, your platform might need to collect funds from your connected accounts:

- To charge the connected account directly for products or services
- To recover funds for a previous refund
- To make other adjustments to connected[account balances](/connect/account-balances)(for example, to correct an error)

When creating and managing connected accounts where your platform is responsible for negative balances, including  Express or Custom accounts, you can debit a connected account’s Stripe balance, transferring funds to your platform balance.

NoteTo bill connected accounts where Stripe is responsible for negative balances, create a customer for each connected account and charge them using Stripe Billing subscriptions.

Stripe supports two approaches for doing so:

- [Charging a connected account](#charging-a-connected-account)for your platform’s products or services
- [Transferring from a connected account](#transferring-from-a-connected-account)to recover funds or make other adjustments

Both approaches create the same flow of funds: a Transfer is created on the connected account and a Payment is created on the platform account.

CautionUsing Account Debits requires getting legally binding consent from your connected accounts. This feature is available in Australia, Canada, Europe, Hong Kong, Japan, New Zealand, and the US. Stripe supports Account Debits only when both your platform and the connected account are in the same region (for example, both are in Japan). If you have interest in other regions, contact the sales team. Using Account Debits incurs an additional cost.

## Requirements

This functionality is only supported for connected accounts where your platform is responsible for negative balances, including Express and Custom accounts. Additionally:

- The connected account and the platform must be in the same region (that is, both must be in Europe or in the US).
- The`currency`value must match the default currency of the connected  account.
- Debiting an account can’t make the connected account balance become negative unless you have[reserves enabled](/connect/account-balances#understanding-connected-reserve-balances)(on by default for all new platforms created after January 31, 2017) and have a bank account in the same currency as the debit.
- If a connected account has a[negative balance](/connect/account-balances#accounting-for-negative-balances), Stripe might auto debit the external account on file, depending on what country the connected account is in.

Avoid setbacks by verifying the bank for the connected account before using Account Debits.

## Charging a connected account

The create a charge API call supports providing a connected account ID as the source value:

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1500 \
  -d currency=usd \
  -d source={{CONNECTED_ACCOUNT_ID}}`The API call returns the Payment created on the platform account (note: it does not return a Charge).

This approach is appropriate for platforms that charge their connected accounts for goods and services (that is, for using the platform). For example, a platform can charge its connected accounts for additional fees or services through their Stripe balance, minimizing any need to collect an additional payment method and allowing for nearly instant availability of the funds.

## Transferring from a connected account

The second method for debiting a connected account is to make a transfer from the connected account to your platform account. Use the Stripe-Account header to authenticate as the connected account and provide your platform’s Stripe account ID as the destination:

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1500 \
  -d currency=usd \
  -d destination={{PLATFORM_STRIPE_ACCOUNT_ID}}`This API call returns the Transfer created on the connected account.

This approach is best for making adjustments within a platform (for example, correcting a payment mistake or recovering any fees you paid to Stripe).

Note that you do need your platform’s Stripe account ID to perform this request. If you don’t know that value already, perform a retrieve account API call using your platform’s API key:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`This API call returns the Account object that represents your platform account.

## See also

- [Creating Direct Charges](/connect/direct-charges)
- [Creating Destination Charges on Your Platform](/connect/destination-charges)
- [Creating Separate Charges and Transfers](/connect/separate-charges-and-transfers)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Requirements](#requirements)[Charging a connected account](#charging-a-connected-account)[Transferring from a connected account](#transferring-from-a-connected-account)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`