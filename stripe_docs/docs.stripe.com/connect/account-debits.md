# Debit connected accounts

At times, your platform might need to collect funds from your connected accounts:

- To charge the connected account directly for products or services

- To recover funds for a previous refund

- To make other adjustments to connected account balances (for example, to correct an error)

[account balances](/connect/account-balances)

When creating and managing connected accounts where your platform is responsible for negative balances, including  Express or Custom accounts, you can debit a connected account’s Stripe balance, transferring funds to your platform balance.

[Express](/connect/express-accounts)

[Custom](/connect/custom-accounts)

To bill connected accounts where Stripe is responsible for negative balances, create a customer for each connected account and charge them using Stripe Billing subscriptions.

[charge them using Stripe Billing subscriptions](/connect/subscriptions#connected-account-platform)

Stripe supports two approaches for doing so:

- Charging a connected account for your platform’s products or services

[Charging a connected account](#charging-a-connected-account)

- Transferring from a connected account to recover funds or make other adjustments

[Transferring from a connected account](#transferring-from-a-connected-account)

Both approaches create the same flow of funds: a Transfer is created on the connected account and a Payment is created on the platform account.

Using Account Debits requires getting legally binding consent from your connected accounts. This feature is available in Australia, Canada, Europe, Hong Kong, Japan, New Zealand, and the US. Stripe supports Account Debits only when both your platform and the connected account are in the same region (for example, both are in Japan). If you have interest in other regions, contact the sales team. Using Account Debits incurs an additional cost.

[sales team](https://stripe.com/contact/sales)

[additional cost](https://stripe.com/connect/pricing)

## Requirements

This functionality is only supported for connected accounts where your platform is responsible for negative balances, including Express and Custom accounts. Additionally:

[Express](/connect/express-accounts)

[Custom](/connect/custom-accounts)

- The connected account and the platform must be in the same region (that is, both must be in Europe or in the US).

- The currency value must match the default currency of the connected  account.

- Debiting an account can’t make the connected account balance become negative unless you have reserves enabled (on by default for all new platforms created after January 31, 2017) and have a bank account in the same currency as the debit.

[reserves enabled](/connect/account-balances#understanding-connected-reserve-balances)

- If a connected account has a negative balance, Stripe might auto debit the external account on file, depending on what country the connected account is in.

[negative balance](/connect/account-balances#accounting-for-negative-balances)

Avoid setbacks by verifying the bank for the connected account before using Account Debits.

[verifying the bank](/ach-deprecated#verifying)

## Charging a connected account

The create a charge API call supports providing a connected account ID as the source value:

[create a charge](/api#create_charge)

The API call returns the Payment created on the platform account (note: it does not return a Charge).

This approach is appropriate for platforms that charge their connected accounts for goods and services (that is, for using the platform). For example, a platform can charge its connected accounts for additional fees or services through their Stripe balance, minimizing any need to collect an additional payment method and allowing for nearly instant availability of the funds.

## Transferring from a connected account

The second method for debiting a connected account is to make a transfer from the connected account to your platform account. Use the Stripe-Account header to authenticate as the connected account and provide your platform’s Stripe account ID as the destination:

This API call returns the Transfer created on the connected account.

This approach is best for making adjustments within a platform (for example, correcting a payment mistake or recovering any fees you paid to Stripe).

Note that you do need your platform’s Stripe account ID to perform this request. If you don’t know that value already, perform a retrieve account API call using your platform’s API key:

[retrieve account](/api#retrieve_account)

This API call returns the Account object that represents your platform account.

## See also

- Creating Direct Charges

[Creating Direct Charges](/connect/direct-charges)

- Creating Destination Charges on Your Platform

[Creating Destination Charges on Your Platform](/connect/destination-charges)

- Creating Separate Charges and Transfers

[Creating Separate Charges and Transfers](/connect/separate-charges-and-transfers)
