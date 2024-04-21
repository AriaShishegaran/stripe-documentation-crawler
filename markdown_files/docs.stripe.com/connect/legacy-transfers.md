htmlControlling bank and debit card transfers | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Flegacy-transfers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Flegacy-transfers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Controlling bank and debit card transfers

Stripe allows platforms to entirely control the transfers for its Custom Connect accounts.CautionThis page describes an older version of Connect. In the latest version of Connect, the legacy transfers endpoint has been deprecated in favor of payouts. The Dashboard’s user interface reflects this change, using the term “payouts” instead of transfers, regardless of your Stripe API version. Refer to bank and debit card payouts for information about the latest version of the Connect API.

### Custom versus Standard accounts

This guide applies solely to Custom accounts, where you are responsible for all communication and interaction with the account holder.

If you’d like to connect to an existing Stripe account, or have Stripe handle details like identity document collection, take a look at Standard accounts.

By default, any charge you make on behalf of a connected account accumulates in the connected account’s Stripe balance and is paid out on a daily rolling basis. However, Stripe offers fine-grained control over this behavior for Custom accounts.

You can:

- Set the destination[bank accounts and debit cards](#bank-accounts)
- Control[how frequently](#payout-information)funds are automatically paid out
- Perform[manual transfers](#using-manual-transfers)
- Send funds[instantly](#instant-payouts)

## Managing bank accounts and debit cards

Custom accounts have an external_accounts property: a list of all bank accounts and debit cards associated with the Stripe account. Any external account is a possible destination for funds.

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "external_accounts": {
    "object": "list",
    "has_more": false,
    "url": "/v1/accounts/acct_14qyt6Alijdnw0EA/external_accounts",
    "data": [
      {
        "id": "{{BANK_ACCOUNT_ID}}",
        "object": "bank_account",
        "account": "acct_14qyt6Alijdnw0EA",
        "account_holder_name": "Jane Austen",
        "account_holder_type": "individual",
        "bank_name": "STRIPE TEST BANK",
        "country": "US",
        "currency": "usd",
        "default_for_currency": false,
        "fingerprint": "sSZ2yLp0EZTH17cF",
        "last4": "6789",
        "metadata": {
        },
        "routing_number": "110000000",
        "status": "new"
      },
      {...},
      {...},
    ],
  ...
}`Destination accounts are added via the external_accounts parameter when creating or updating Stripe accounts. The value should be a bank account or debit card token returned from Stripe.js. Alternatively, you can provide a hash of the bank account details, but using Stripe.js is preferred as it prevents sensitive data from hitting your server.

When using debit cards as a transfer destination, the following restrictions apply:

- Must be a non-prepaid US Visa, Mastercard, or Discover
- Limited to 9,999 USD per transfer on[Instant Payouts](#instant-payouts)
- Generally limited to 3,000 USD per transfer otherwise

## Managing multiple bank and debit accounts

By default, providing a new value for external_accounts while updating a Custom account replaces the existing account with the new one. To add additional bank accounts or debit cards to a connected account, use the Bank Account and Card creation API endpoints.



Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/external_accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d external_account={{BANK_ACCOUNT_TOKEN_ID}}`When working with multiple currencies, Stripe automatically sends transfers to an associated bank account or debit card for its currency, thereby avoiding exchange fees. When there are multiple accounts available for a given currency, Stripe uses the one set as default_for_currency.

Stripe maintains a list of available country/currency combinations for your reference and to help your users choose from the supported options.

## Payout information

When using automatic transfers, the transfer_schedule property on an account indicates how often the Stripe account’s balance is automatically paid out:

`{
  ...
  "transfer_schedule": {
    "delay_days": 7,
    "interval": "daily"
  },
  ...
}`The delay_days property reflects how long it takes charges (or linked transfers) to become available for payout. This field is useful for controlling automatic payouts. For example, if you want your Custom accounts to receive their funds 2 weeks after the charge is made, set interval to daily and delay_days to 14. The default is the lowest permitted value for the account, determined by the connected account’s country. When setting or updating this field, you may pass the string minimum to choose the lowest permitted value.

There are four possible settings for the interval property:

- manualprevents automatic payouts. You will have to manually pay out the account’s balance using the[Transfers API](/api#create_transfer)(acting as the connected account). Also set an account to`manual`to use[Instant Payouts](#instant-payouts).
- dailyautomatically pays out charges`delay_days`days after they’re created. The`delay_days`value cannot be less than your own transfer schedule or less than the default transfer schedule for the account.
- weeklyautomatically pays out the balance once a week, specified by the`weekly_anchor`parameter (a lower-case weekday such asmonday).
- monthlyautomatically pays out the balance once a month, specified by the`monthly_anchor`parameter (a number from 1 to 31).

## Using manual transfers

If you set transfer_schedule[interval] to manual using the Accounts API, Stripe will hold funds in the account holder’s balance until told to pay them out (or until a maximum of 90 days have passed). To trigger a payout of these funds, use the Transfers API.

The Transfers API is only for moving funds from a connected Stripe account’s balance into their external account. To move funds between Stripe accounts, see creating separate charges and transfers or creating destination charges through the platform.

NoteEscrow has a precise legal definition and Stripe does not support escrow accounts. However, we do provide escrow-like behavior through manual transfers. This gives you control over transfer timing, with the ability to delay payouts to Custom accounts for up to 90 days.

Manual transfers can be used as an alternative to escrow when there may be a risk of a delayed delivery, or if there’s the possibility of a refund being needed.

### Standard transfers

As a basic transfer example, to have 10 USD sent from a Custom account’s Stripe balance to their external account:

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -d "amount"=1000 \
  -d "currency"="usd" \
  -d "destination"="default_for_currency"`Setting destination=default_for_currency tells Stripe to transfer to the account’s default bank account or debit card for the given currency.

With a standard transfer, you can payout up to the user’s available balance. To find that amount, perform a retrieve balance call on their behalf.

Stripe tracks balance contributions from different payment sources in separate balances. The retrieve balance response breaks down the components of each balance by source type. For example, if you want to create a transfer specifically for a non-credit-card balance, specify the source_type in your request.

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=24784 \
  -d "currency"="usd" \
  -d "destination"="default_for_currency" \
  -d "source_type"="bank_account"`Note that it is possible for any source’s balance component to go negative (through refunds or chargebacks), and transfers can’t be created for greater than the aggregate available balance.

### Using Instant Payouts

With Instant Payouts, you can immediately send funds to a Custom account’s debit card. Funds typically appear in the associated bank account within 30 minutes, making it possible to go from charge to payout in mere moments.

To use Instant Payouts, specify instant for the method property when creating the transfer:

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -d "amount"=1000 \
  -d "currency"="usd" \
  -d "method"="instant"`Instant Payouts differ from other manual transfers in a couple of ways:

- You can transfer an account’s available balance plus itspendingbalance
- Instant Payouts can be requested on weekends and holidays

Initially, platforms can transfer up to 500 USD per day—in total, across all connected accounts—through Instant Payouts. Contact us if you need this threshold increased.

Instant Payouts is available for all of the largest US banks, but a small percentage of banks do not yet support it. For those banks, you will have to fall back to standard payouts.

When you add a card to an account, Stripe returns a property available_payout_methods in the response, which will be a set containing the payout methods Stripe supports for that card. Only values in this set should be passed as the method when creating a transfer.

`{
  "id": "{{CARD_ID}}",
  "object": "card",
  ...
  "account": "acct_1032D82eZvKYlo2C",
  "available_payout_methods": ["standard", "instant"],
}`If a Custom account’s card does not support Instant Payouts, you should clearly communicate to the owner of that account that they will not receive their payouts instantly.

### Using webhooks with transfers

All transfer activity on connected accounts can be tracked using webhooks. (When using Connect, you should always be using webhooks.) Specific to transfers, you’ll see these events:

- `transfer.created`
- `transfer.updated`
- `transfer.paid`
- `transfer.failed`

For most transfers, these event notifications occur over a series of days. Instant Payouts typically send transfer.paid within 30 minutes.

If a transfer cannot be completed, a transfer.failed event occurs. The event’s  failure_reason property indicates why.

## See also

- [Custom accounts](/connect/custom-accounts)
- [Updating accounts](/connect/updating-service-agreements)
- [Understanding Connect account balances](/connect/account-balances)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Managing bank accounts and debit cards](#bank-accounts)[Managing multiple bank and debit accounts](#multiple-accounts)[Payout information](#payout-information)[Using manual transfers](#using-manual-transfers)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`