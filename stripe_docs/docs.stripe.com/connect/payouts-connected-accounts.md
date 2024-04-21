# Payouts to connected accounts

By default, any charge you make on behalf of a connected account accumulates in the connected account’s balance and is paid out on a daily rolling basis. Depending on the configuration of your connected accounts, your platform can manage their payouts as follows:

[charge](/connect/charges)

[balance](/connect/account-balances)

- Schedule the frequency of automatic payouts

[the frequency of automatic payouts](/connect/manage-payout-schedule)

- Perform manual payouts

[manual payouts](/connect/manual-payouts)

- Settle funds instantly

[instantly](/connect/instant-payouts)

- When using destination charges or separate charges and transfers, retain funds in your platform balance

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

In versions of Connect earlier than 2018, payouts were known as bank transfers and used the deprecated transfers API. For information about bank transfers, see the legacy Transfers documentation.

[Transfers](/connect/legacy-transfers)

## Payout management configurations

For connected accounts with access to the full Stripe Dashboard or Express Dashboard, the account holder manages their external payout accounts (bank accounts and debit cards), but the platform can schedule payouts. To schedule payouts for an account that has access to the full Stripe Dashboard, the platform must configure Platform controls for the account.

[payout](/payouts)

[Platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

For connected accounts without access to a Stripe-hosted Dashboard, the platform manages their external payout accounts and can schedule their payouts.

## Supported settlement currencies

To see which currencies you can use to settle funds in a particular country, select that country from the following dropdown.

For a list of supported presentment currencies, see the currencies documentation.

[currencies](/currencies#presentment-currencies)

Platforms can also enable their connected accounts to settle funds and pay out to banks in certain alternative currencies, or pay out to non-domestic bank accounts in the local currency. In some cases, Stripe charges a fee. For more information, see Alternative currency payouts for Connect marketplaces and platforms.

[Alternative currency payouts for Connect marketplaces and platforms](/connect/alternative-currency-payouts)

You can track all payout activity on connected accounts using webhooks by listening for these events:

[webhooks](/webhooks)

- payout.created

- payout.updated

- payout.paid

- payout.failed

For most payouts, event notifications occur over a series of days. Instant payouts typically send payout.paid within 30 minutes.

When a payout can’t be completed, a payout.failed event occurs. The event’s failure_code property indicates the reason. A failed payout also disables the external account involved in that payout, triggering an account.external_account.updated event. No payouts can be made to that external account until the platform updates the connected account’s external accounts.
