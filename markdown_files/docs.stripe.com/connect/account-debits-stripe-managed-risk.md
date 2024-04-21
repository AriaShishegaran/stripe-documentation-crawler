htmlDebiting accounts on Stripe managed risk | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-debits-stripe-managed-risk)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-debits-stripe-managed-risk)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Debiting accounts on Stripe managed risk

With Connect, your platform can directly debit the Stripe balance of an account on Stripe managed risk.At times, your platform might need to collect funds from your connected accounts:

- To charge the connected account directly for products or services
- To recover funds for a previous refund
- To make other adjustments to connected[account balances](/connect/account-balances)(for example, to correct an error)

When using accounts with Stripe managed risk (also known as Stripe loss liable), you can debit a connected account’s Stripe balance to credit your platform account’s Stripe balance. This creates a Transfer on the connected account and a Payment on the platform account.

CautionUsing Account Debits requires getting legally binding consent from your connected accounts. This feature is available in Australia, Canada, Europe, Hong Kong, Japan, New Zealand, and the US. Stripe supports Account Debits only when both your platform and the connected account are in the same region (for example, both in Japan). If you have interest in other regions, contact the sales team. There’s an additional cost for using Account Debits.

## Requirements

The functional requirements for debiting connected accounts with Stripe managed risk are different from those of Express, Custom, or accounts with platform managed risk. For more information on how to debit the aforementioned accounts, please refer to debiting Express and Custom accounts.

For debiting accounts with Stripe managed risk:

- The connected account and the platform must be in the same region (that is, both must be in Europe or in the US).
- The`currency`value must match the default currency of the connected account.
- If a connected account balance becomes negative as a result of the account debit, we will hold the appropriate amount of reserves on the platform balance. For more information please refer to[understanding connected reserve balances due to accounts with Stripe managed risk](/connect/account-balances#understanding-connected-reserve-balances-created-by-accounts-with-stripe-managed-risk).

To allow for the most seamless experience, verify the connected account’s bank before using Account Debits.

## Transferring from a connected account

To debit connected accounts with Stripe managed risk, create a Transfer from your connected account to your platform account and provide a reference_transaction that initiated the debit. When using reference_transaction, the provided transaction must be a Charge, Payment, or Payout created on the same connected account being debited.

As always, when making an account debit transfer, use the Stripe-Account header to authenticate as the connected account and provide your platform’s Stripe account ID as the destination.

For debiting because of a previous Charge or Payment on the connected account:

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=500 \
  -d currency=usd \
  -d destination={{PLATFORM_STRIPE_ACCOUNT_ID}} \
  -d "reference_transaction[type]"=charge \
  -d "reference_transaction[charge]"={{REFERENCE_TRANSACTION_ID}}`For debiting because of a previous Payout on the connected account:

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=500 \
  -d currency=usd \
  -d destination={{PLATFORM_STRIPE_ACCOUNT_ID}} \
  -d "reference_transaction[type]"=payout \
  -d "reference_transaction[payout]"={{REFERENCE_TRANSACTION_ID}}`If successful, both the preceding API calls return the Transfer created on the connected account. In both cases, the Transfer that is returned corresponds to a Payment created on your platform account.

You must use your platform’s Stripe account ID to perform this request. If you don’t know that value already, perform a retrieve account API call using your platform’s API key:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`This API call returns the Account object that represents your platform account.

## See also

- [Creating Direct Charges](/connect/direct-charges)
- [Creating Destination Charges on Your Platform](/connect/destination-charges)
- [Creating Separate Charges and Transfers](/connect/separate-charges-and-transfers)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Requirements](#requirements)[Transferring from a connected account](#transferring-from-a-connected-account)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`