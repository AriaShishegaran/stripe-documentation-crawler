# Balance transaction types

Balance transactions are our recommended starting point for reporting on your account’s balance activity. We create them for every type of transaction that comes into, or flows out of, your Stripe account’s balance.

You can create reports that make use of balance transactions using the API or Sigma.

[API](/api/)

[Sigma](/stripe-data/query-transactions)

When you first receive a payment in your account, we initially reflect it as a pending balance (less any Stripe fees). This balance becomes available according to your payout schedule. The status attribute on balance transactions indicates the type of the balance.

[status](/api#balance_transaction_object-status)

To classify transactions for accounting purposes, use the reporting_category field instead of the type field.

[accounting purposes](/reports/reporting-categories)

## Balance transaction source

Balance transactions include a source field that contains the ID of the related Stripe object.

[source](/api#balance_transaction_object-source)

Use the API to retrieve additional information about the payment activity that caused the creation of the Balance transaction. Using Sigma, you can also join the balance_transactions table with other tables using the source_id column.

[API](/api/)

[Sigma](/stripe-data/query-transactions)

## Balance transaction types

You can organize balance transaction types into different groups based on the underlying activity that generated the balance transactions.

If you’re not using the Connect API or Issuing API, your balance transactions belong in the first two groups (“related to charges and payments” or “related to Stripe balance changes”).

These balance transaction types are related to creating and refunding charges as part of processing payments.

Created when a credit card charge is created successfully.

[credit card charge](/payments/accept-a-payment-charges)

Created when a local payment method charge is created successfully.

[local payment method](/payments/payment-methods/overview)

ACH, direct debit, and other delayed notification payment methods remain in a pending state until they either succeed or fail. You’ll see a pending Balance transaction of type payment when the payment is created. Another Balance transaction of type payment_failure_refund appears if the pending payment later fails.

[ACH, direct debit](/payments/payment-methods/overview)

[delayed notification payment methods](/payments/payment-methods#payment-notification)

Created when a local payment method refund is initiated.

[local payment method](/payments/payment-methods/overview)

Additionally, if your customer’s bank or card issuer is unable to correctly process a refund (e.g., due to a closed bank account or a problem with the card) Stripe returns the funds to your balance. The returned funds are represented as a Balance transaction with the type payment_refund.

Created when a debit/failure related to a payment is detected from a banking partner. This balance transaction takes funds that were previously credited to the merchant for a payment out of the merchant balance.

Created when a credit card charge refund is initiated.

[credit card charge refund](/refunds)

If you authorize and capture separately and the capture amount is less than the initial authorization, you see a balance transaction of type charge for the full authorization amount and another balance transaction of type refund for the uncaptured portion.

[authorize and capture](/payments/place-a-hold-on-a-payment-method)

Created when a credit card charge refund fails, and Stripe returns the funds to your balance.

[credit card charge refund](/refunds)

This may occur if your customer’s bank or card issuer is unable to correctly process a refund (e.g., due to a closed bank account or a problem with the card).

These balance transaction types are related to changes that affect your Stripe balance such as payouts, fees and top-ups.

Adjustments correspond to additions or deductions from your Stripe balance that are made outside of the normal charge/refund flow. For example, some of the most common reasons for adjustments are:

- Refund failures. If your customer’s bank or card issuer is unable to correctly process a refund (e.g., due to a closed bank account or a problem with the card) Stripe returns the funds to your balance. The returned funds are represented as a Balance transaction with the type adjustment, where the description indicates the related refund object.

- Disputes. When a customer disputes a charge, Stripe deducts the disputed amount from your balance. The deduction is represented as a Balance transaction with the type adjustment, where the source object is a dispute.

[disputes a charge](/disputes)

- Dispute reversals. When you win a dispute, the disputed amount is returned to your balance. The returned funds are represented as a Balance transaction with the type adjustment, where the source object is a dispute.

[win a dispute](/disputes#responding-to-a-dispute)

- In the past, fees for Stripe software and services (e.g., for Radar, Connect and Billing) were represented as adjustments.

- In the past, Connect platform fee refunds were represented as adjustments.

The description field on the Balance transaction describes the purpose of each adjustment.

Repayments made to service an anticipation loan in Brazil. These repayments go to the financial institution to whom you have sold your receivables.

Funds moving into a balance (e.g. Issuing balance) from another balance (e.g. Stripe balance)

Funds moving from your Stripe balance to a different (e.g. Issuing) balance.

Funds used to purchase carbon removal units from Frontier Climate.

Funds refunded to your balance when a Climate Order is canceled.

Funds contributed via Stripe to a cause (currently Stripe Climate).

Obligation for receivable unit received.

Obligation for receivable unit reversed.

Funds that a payment network holds in reserve (e.g. to mitigate risk).

Funds that a payment network releases from a reserve.

Created when a customer has unreconciled funds within Stripe for more than ninety days. This balance transaction transfers those funds to your balance.

Payouts from your Stripe balance to your bank account.

[Payouts](/payouts)

Created when a payout to your bank account is cancelled and the funds are returned to your Stripe balance.

Created when a payout to your bank account fails and the funds are returned to your Stripe balance.

[payout to your bank account fails](/payouts#payout-failures)

When Stripe holds your funds in reserve to mitigate risk, two balance transactions are created: one to debit the funds from your balance, and a second to credit the funds back to your balance at the end of the reserve period.

Fees for Stripe software and services (e.g., for Radar, Connect, Billing, and Identity).

[Radar](/radar)

[Connect](/connect)

[Billing](/billing)

[Identity](/identity)

Stripe currency conversion fee

Taxes collected by Stripe to be remitted to the appropriate local governments. Typically, this is a tax on Stripe fees.

Funds you transferred into your Stripe balance from your bank account. Learn more.

[Learn more](/connect/top-ups)

If an initially successful top-up fails or is cancelled, the credit to your Stripe balance is reversed. Learn more.

[Learn more](/connect/top-ups)

These balance transaction types are created as part of using the Issuing API.

[Issuing API](/issuing)

When an issued card is used to make a purchase, an authorization is created. If the authorization is approved, a balance transaction is created with the type issuing_authorization_hold to hold the authorized amount in reserve from your account balance, until the authorization is either captured or voided. Some merchants can also update an authorization to request an additional amount (e.g., to extend a hotel booking or add a tip), and this is also represented as a balance transaction with the type issuing_authorization_hold.

[an issued card](/issuing)

[authorization](/issuing/purchases/authorizations)

When an authorized purchase, made with an issued card, is captured by the merchant, the funds previously held for the authorization (issuing_authorization_hold) are released with a issuing_authorization_release balance transaction. Simultaneously, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance in another balance transaction with the type issuing_transaction.

[an issued card](/issuing)

[an issuing transaction](/issuing/transactions)

When you dispute an Issuing transaction and funds return to your Stripe balance.

[Issuing transaction](/issuing/transactions)

When an authorized purchase, made with an issued card, has been authorized and captured by the merchant, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance with a issuing_transaction balance transaction.

[issued card](/issuing)

[an issuing transaction](/issuing/transactions)

These balance transaction types are related to using the Connect API and related APIs, such as instant payouts.

[Connect API](/connect)

[instant payouts](/connect/instant-payouts)

Incrementing available funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

[instant payouts](/connect/instant-payouts)

Decrementing pending funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

[instant payouts](/connect/instant-payouts)

Earnings you’ve generated by collecting platform fees via Stripe Connect charges.

[platform fees](/connect/direct-charges#collecting-fees)

[Stripe Connect charges](/connect/charges)

Platform fees that you have returned to your connected accounts.

[Platform fees](/connect/direct-charges#collecting-fees)

If one of your connected accounts has a negative balance for 180 days, Stripe transfers a portion of your balance, to zero out that account’s balance. Learn more.

[Learn more](/connect/account-balances#understanding-connected-reserve-balances)

If one of your connected accounts’ balances becomes negative, Stripe temporarily reserves a portion of your balance to ensure that funds can be covered.

If one of your connected accounts’ previously negative balance becomes less negative due to activity on account, another reserve_transaction is created to release a corresponding portion of the funds held in reserve. Learn more.

[Learn more](/connect/account-balances#understanding-connected-reserve-balances)

Funds sent from your balance to the balance of your connected accounts.

[connected accounts](/connect/separate-charges-and-transfers)

Transfers to your connected accounts that have been cancelled.

Transfers to your connected accounts that failed. Transfer failures add to your platform’s balance and subtract from the connected account’s balance.

Transfers to your connected accounts that you reversed or that were reversed as a result of a failure in payments made through ACH, direct debit, and other delayed notification payment methods. Transfer reversals add to your platform’s balance and subtract from the connected account’s balance.

[reversed](/connect/separate-charges-and-transfers#reversing-transfers)

[payments](/payments/payment-methods/overview)

[delayed notification payment methods](/payments/payment-methods#payment-notification)
