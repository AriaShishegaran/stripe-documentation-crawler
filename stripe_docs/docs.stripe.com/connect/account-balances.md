# Understanding Connect account balances

Stripe accounts additionally have separate balances by payment source. But for simplicity’s sake, this page focuses on the broader concept of account balances regardless of the source.

[payment source](/connect/manual-payouts#regular-payouts)

Both your platform account and a connected account are still just Stripe accounts, each with their own, separate account balance.

All Stripe accounts can have balances in two states:

- pending, meaning the funds are not yet available to pay out

- available, meaning the funds can be paid out now

With non-Connect accounts, processing charges increases the Stripe account balance. The charged amount, less any Stripe fees, is initially reflected on the pending balance, and becomes available on a 2-day rolling basis. (This timing can vary by country and account.) Available funds can be paid out to a bank account or debit card. Payouts reduce the Stripe account balance accordingly.

[Payouts](/payouts)

With Connect, your platform account and each connected account has its own pending and available balances. The allocation of funds between them depends on the type of charges that you use.

[Connect](/connect)

[the type of charges](/connect/charges)

Further, a platform account can also have a connect_reserved balance, used to offset negative balances on connected accounts.

## Check a connected account’s balance

To check the balance of a connected account, perform a retrieve balance call authenticated as the connected account. The returned Balance object reflects the pending and available balances.

[retrieve balance](/api/balance/balance_retrieve)

[Balance object](/api#balance_object)

## Accounting for negative balances

To reduce the risk of financial loss, make sure each connected account has a valid bank account.

[bank account](/connect/payouts-connected-accounts)

Some actions, such as refunds and chargebacks, create negative transactions in a Stripe account. Stripe handles negative transactions to optimize for keeping a positive Stripe balance for related accounts:

- If at all possible, Stripe automatically offsets negative transactions against future payments

- Stripe first assigns negative transactions to the account on which the associated charge was made. For example, when charging on a connected account, a refund or chargeback comes from the connected account. When charging on your platform, a refund or chargeback comes from your platform account.

Despite these measures, if a connected account balance becomes negative, ultimate responsibility depends on the account type.

- A connected Standard account is always responsible to cover its negative balances

- For Express and Custom accounts, the platform is responsible to cover negative balances

While an account’s balance is negative, you can’t send payouts to the account’s bank or debit card on their behalf. Stripe will resume sending payouts to the connected account when the account’s Stripe balance is again positive.

If Stripe hasn’t already attempted to debit a connected account’s external account for a negative balance, you can set debit_negative_balances to true to allow Stripe to automatically do so.

[debit_negative_balances](/api/accounts/object#account_object-settings-payouts-debit_negative_balances)

Stripe can’t correct a negative Stripe account balance using a debit card.

Auto debit for negative balances is supported for banks in the following countries:

- Australia

- Canada

- Europe (SEPA countries, which includes the UK)

- New Zealand

- United States

See the Auto Debit FAQ for a detailed breakdown of which countries and account types are supported.

[Auto Debit FAQ](https://support.stripe.com/questions/auto-debit-faq)

Enabling debit_negative_balances triggers debits as needed, even when the connected account is on manual payouts. For more details, see Impact from chargebacks and negative balances.

[Impact from chargebacks and negative balances](/connect/risk-management/best-practices#impact-from-chargebacks-and-negative-balances)

## Understanding connected reserve balances

To ensure funds can be covered, Stripe holds a reserve on your platform account’s available balance to cover any negative available balances across your Custom and Express accounts. Depending on the country that the Custom or Express account is in, Stripe initiates a bank withdrawal on the account’s bank account to cover the negative balance. Although the available balance for the account zeroes out as soon as the withdrawal is posted, the platform reserve for that account is held for an additional 3 business days. You’ll see this reserve reflected in the Dashboard and exported reports (as a reserve transaction).

[negative balance](https://support.stripe.com/questions/negative-balances-in-stripe-handling-by-country)

[Dashboard](https://dashboard.stripe.com/test/balance/overview)

There are three kinds of balance activities related to reserves:

- Funds reserved to cover a negative balance on a connected account. When a connected account’s balance becomes negative, Stripe temporarily reserves a portion of your balance to ensure that funds can be covered by creating a balance transaction with the type reserve_transaction.

- Funds released after a positive balance change on a connected account. When a connected account’s previously negative balance becomes less negative due to activity on that account (for example, through new charges), a corresponding portion of your platform’s reserve balance is released through a balance transaction with the type reserve_transaction.

- Funds collected due to a long-standing negative balance on a connected account. When a connected account holds a negative balance amount for 180 days, Stripe transfers a portion of your balance to zero out that account’s balance by creating a balance transaction with the type connect_collection_transfer.

To see the current reserves held on your account, perform a retrieve balance API call but for your own account (that is, not authorized as another user as in the above).

To clear a connected account’s negative balance, and thereby remove the reserve on your account, send a transfer to the applicable account. If a connected account has a negative balance for more than 180 days, Stripe will automatically transfer your reserves to the connected account to zero out the balance. Dashboard pages and reports show these transfers as Connect collection transfers.

[transfer](/connect/separate-charges-and-transfers)

After a connected account’s balance is cleared through a collection transfer, we recommend that you reject the account to prevent future losses.

[reject](/api#reject_account)

## Holding funds

If your platform needs more granular control over your payout schedule, you can take one of the following approaches:

- Hold funds in the platform balance before sending them to Express or Custom accounts

[sending them to Express or Custom accounts](/connect/separate-charges-and-transfers)

- Keep funds in an Express or Custom account’s balance before proceeding to pay out the funds to a bank account or debit card

[pay out the funds](/connect/manual-payouts)

We recommend platforms hold funds only if you have a clear purpose for holding them and a commitment to complete the payment when an event occurs or a precondition is satisfied. The typical use case for holding funds is on-demand services platforms, where the marketplace usually waits for the service to be completed and confirmed before paying out to the service provider (for example, rentals, delivery services, and ride-sharing).

Platforms should refrain from holding funds arbitrarily, and instead pay out to their connected accounts as soon as they are identified. This is usually when the charge is made. If you aren’t sure about holding funds, speak with your legal advisor.

For compliance reasons, we can hold funds in reserve for a period of time that’s based on the merchant’s country, as shown below:

## See also

- Creating Direct Charges

[Creating Direct Charges](/connect/direct-charges)

- Creating Destination Charges on Your Platform

[Creating Destination Charges on Your Platform](/connect/destination-charges)

- Creating Separate Charges and Transfers

[Creating Separate Charges and Transfers](/connect/separate-charges-and-transfers)
