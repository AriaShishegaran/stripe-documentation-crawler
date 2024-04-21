# Using manual payouts

If you set the value of schedule.interval to manual, we hold funds in the accountholder’s balance until you specify otherwise. You must pay out the funds within the time period specified below, based on the business’s country:

[schedule.interval](/api/accounts/object#account_object-settings-payouts-schedule)

To trigger a payout of these funds, use the Payouts API.

[Payouts API](/api/payouts/create)

The Payouts API is only for moving funds from a connected Stripe account’s balance into their external account. To move funds between the platform and a connected account, see creating separate charges and transfers or creating destination charges through the platform.

[separate charges and transfers](/connect/separate-charges-and-transfers)

[destination charges](/connect/destination-charges)

Escrow has a precise legal definition, and Stripe doesn’t provide escrow services or support escrow accounts. However, you can control payout timing through manual payouts, which allow you to delay payouts to certain accounts. When using manual payouts, you must pay out funds within the time frame for the business’s country.

Delayed payouts can be useful when a delivery is delayed or when there’s a possibility of a refund.

## Regular payouts

The following example sends 10 USD from a connected account’s Stripe balance to their external account:

With a standard payout, you can move an amount up to the user’s available balance. To find that amount, perform a retrieve balance call on their behalf.

[retrieve balance](/api#retrieve_balance)

Stripe tracks balance contributions from different payment sources in separate balances. The retrieve balance response breaks down the components of each balance by source type. For example, to create a payout specifically for a non-credit-card balance, specify the source_type in your request.

While individual balance components can go negative (such as through refunds or chargebacks), you can’t create payouts for greater than the aggregate available balance.
