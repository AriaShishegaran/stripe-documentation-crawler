# Reporting categories and types

Learn more about the reporting_category field on BalanceTransaction objects, and how it differs from type and other categorizations. This topic covers:

- Why introduce a new categorization?

[Why introduce a new categorization?](#why-new-categorization)

- Reporting categories reference

[Reporting categories reference](#reference)

## Why introduce a new categorization?

The BalanceTransaction object’s reporting_category field improves on the type field by providing a more-useful grouping for most finance and reporting purposes. The following sections highlight the new field’s advantages.

The reporting_category attribute separates balance transactions with type=adjustment into several different categories, including disputes, dispute reversals, and failed refunds. Additionally, several types of fees and Connect platform-fee refunds are now explicitly categorized with reporting_category=fee.

[Connect](/connect)

If you are separately authorizing and capturing payments, and you capture an amount less than the initial authorization, you will see two balance transactions: one for the full amount of the authorization, and another reversing the uncaptured portion. (Summing the two balance transactions yields the captured portion of the charge.)

[separately authorizing and capturing](/charges/placing-a-hold)

The balance transaction reversing the uncaptured portion has type=refund, just as if you had refunded a portion of a sale at some later time. To allow separate handling of these objects—perhaps counting them against the initial sale amount, rather than as a separate refund—we label these with the distinct reporting category partial_capture_reversal.

Using the type field, balance transactions arising from card-based charges are represented with type=charge, while those made with other payment methods are represented with type=payment. Similarly, refunds and failures for cards versus alternative payment methods have the distinct types refund and payment_refund.

[other payment methods](/payments/payment-methods/overview)

We found that these distinctions made many common reporting tasks unnecessarily awkward, and so reporting_category simplifies these (and other) groups of types, as follows:

We’ve renamed several balance transaction types for greater clarity:

## Reporting categories reference

This reference covers four groups of reporting categories:

- Payments-related reporting categories

[Payments-related reporting categories](#charge_and_payment_related)

- Balance-related reporting categories

[Balance-related reporting categories](#balance_related)

- Issuing-related reporting categories

[Issuing-related reporting categories](#issuing_related)

- Connect-related reporting categories

[Connect-related reporting categories](#connect_related)

These reporting categories are related to creating and refunding charges as part of processing payments.

These reporting categories are related to creating and refunding charges as part of processing payments.

Charges include payments from cards and from other payment methods. If you are separately authorizing and capturing payments, only the captured charges will be included here.

Charges include payments from cards and from other payment methods. If you are separately authorizing and capturing payments, only the captured charges will be included here.

[Charges](/payments/charges-api)

[other payment methods](/sources#supported-payment-methods)

[separately authorizing and capturing](/charges/placing-a-hold)

- Balance transaction type(s): charge, payment, or validation

- Section(s) in the monthly report: Payments (cards), Payments (other)

ACH, direct debit, and other asynchronous payment methods remain in a pending state until they either succeed or fail. You will see a pending balance transaction with the reporting category charge appear when the payment is created in a pending state. A charge_failure will appear if the pending payment later fails.

ACH, direct debit, and other asynchronous payment methods remain in a pending state until they either succeed or fail. You will see a pending balance transaction with the reporting category charge appear when the payment is created in a pending state. A charge_failure will appear if the pending payment later fails.

[ACH, direct debit](/sources#supported-payment-methods)

[asynchronous payment methods](/sources#synchronous-or-asynchronous-confirmation)

- Balance transaction type(s): payment_failure_refund

- Section(s) in the monthly report: Other Adjustments

When a customer disputes a charge, Stripe deducts the disputed amount from your balance.

When a customer disputes a charge, Stripe deducts the disputed amount from your balance.

[disputes a charge](/disputes)

- Balance transaction type(s): adjustmentor adjusted_for_overdraft_transaction

- Section(s) in the monthly report: Disputes

When you win a dispute, the disputed amount is returned to your balance.

When you win a dispute, the disputed amount is returned to your balance.

[win a dispute](/disputes#responding-to-a-dispute)

- Balance transaction type(s): adjustment

- Section(s) in the monthly report: Dispute Reversals

If you are separately authorizing and capturing payments, and you capture an amount less than the initial authorization, you will see a charge for the full authorization amount, and a partial_capture_reversal for the uncaptured portion.

If you are separately authorizing and capturing payments, and you capture an amount less than the initial authorization, you will see a charge for the full authorization amount, and a partial_capture_reversal for the uncaptured portion.

[separately authorizing and capturing](/charges/placing-a-hold)

- Balance transaction type(s): refund

- Section(s) in the monthly report: Payments (cards)

Payments you’ve refunded to your customers. (Does not include charge failures or partial capture reversals, which are listed separately.)

Payments you’ve refunded to your customers. (Does not include charge failures or partial capture reversals, which are listed separately.)

[refunded](/refunds)

- Balance transaction type(s): refundor payment_refund

- Section(s) in the monthly report: Refunds (cards), Refunds (other)

Created when a credit card charge refund fails, and Stripe returns the funds to your balance.This may occur if your customer’s bank or card issuer is unable to correctly process a refund (e.g., due to a closed bank account or a problem with the card).

Created when a credit card charge refund fails, and Stripe returns the funds to your balance.

[credit card charge refund](/refunds)

This may occur if your customer’s bank or card issuer is unable to correctly process a refund (e.g., due to a closed bank account or a problem with the card).

- Balance transaction type(s): refund_failure

- Section(s) in the monthly report: Other Adjustments

These reporting categories are related to changes that affect your Stripe balance, such as payouts, fees, and top-ups.

These reporting categories are related to changes that affect your Stripe balance, such as payouts, fees, and top-ups.

Repayments made to service an anticipation loan in Brazil. These repayments go to the financial institution to whom you have sold your receivables.

Repayments made to service an anticipation loan in Brazil. These repayments go to the financial institution to whom you have sold your receivables.

- Balance transaction type(s): anticipation_repayment

- Section(s) in the monthly report: Anticipation Repayments

Funds used to purchase carbon removal units from Frontier Climate.

Funds used to purchase carbon removal units from Frontier Climate.

- Balance transaction type(s): climate_order_purchaseor climate_reservation_purchase

- Section(s) in the monthly report: Other Adjustments

Funds refunded to your balance when a Climate Order is canceled.

Funds refunded to your balance when a Climate Order is canceled.

- Balance transaction type(s): climate_order_refundor climate_reservation_refund

- Section(s) in the monthly report: Other Adjustments

Funds contributed via Stripe to a cause (currently Stripe Climate).

Funds contributed via Stripe to a cause (currently Stripe Climate).

- Balance transaction type(s): contribution

- Section(s) in the monthly report: Other Adjustments

Fees for Stripe software and services (e.g., for Radar, Connect, Billing, and Identity).

Fees for Stripe software and services (e.g., for Radar, Connect, Billing, and Identity).

[Radar](/radar)

[Connect](/connect)

[Billing](/billing)

[Identity](/identity)

- Balance transaction type(s): stripe_fee

- Section(s) in the monthly report: Other Adjustments

Miscellaneous adjustments to your Stripe balance.

Miscellaneous adjustments to your Stripe balance.

- Balance transaction type(s): adjustment, obligation_outbound, or obligation_reversal_inbound

- Section(s) in the monthly report: Other Adjustments

Funds that a payment network holds in reserve (e.g. to mitigate risk).

Funds that a payment network holds in reserve (e.g. to mitigate risk).

- Balance transaction type(s): payment_network_reserve_hold

- Section(s) in the monthly report: Other Adjustments

Funds that a payment network releases from a reserve.

Funds that a payment network releases from a reserve.

- Balance transaction type(s): payment_network_reserve_release

- Section(s) in the monthly report: Other Adjustments

Payouts from your Stripe balance to your bank account.

Payouts from your Stripe balance to your bank account.

[Payouts](/payouts)

- Balance transaction type(s): payout

- Section(s) in the monthly report: Payouts and Transfers

Funds returned to your balance if a payout fails after it is initially created (e.g., due to an invalid account number or a cancellation). Learn more.

Funds returned to your balance if a payout fails after it is initially created (e.g., due to an invalid account number or a cancellation). Learn more.

[Learn more](/payouts#payout-failures)

- Balance transaction type(s): payout_cancelor payout_failure

- Section(s) in the monthly report: Payouts and Transfers: Failures and Refunds

When Stripe holds your funds in reserve to mitigate risk, two balance transactions are created: one to debit the funds from your balance, and a second to credit the funds back to your balance at the end of the reserve period.

When Stripe holds your funds in reserve to mitigate risk, two balance transactions are created: one to debit the funds from your balance, and a second to credit the funds back to your balance at the end of the reserve period.

- Balance transaction type(s): reserved_funds

- Section(s) in the monthly report: Other Adjustments

Taxes collected by Stripe to be remitted to the appropriate local governments. Typically, this is a tax on Stripe fees.

Taxes collected by Stripe to be remitted to the appropriate local governments. Typically, this is a tax on Stripe fees.

- Balance transaction type(s): tax_fee

- Section(s) in the monthly report: Other Adjustments

Funds you transferred into your Stripe balance from your bank account. Learn more.

Funds you transferred into your Stripe balance from your bank account. Learn more.

[Learn more](/connect/top-ups)

- Balance transaction type(s): topup

- Section(s) in the monthly report: Other Adjustments

If an initially successful top-up fails or is cancelled, the credit to your Stripe balance is reversed. Learn more.

If an initially successful top-up fails or is cancelled, the credit to your Stripe balance is reversed. Learn more.

[Learn more](/connect/top-ups)

- Balance transaction type(s): topup_reversal

- Section(s) in the monthly report: Other Adjustments

When a customer has unreconciled funds within Stripe for more than ninety days, Stripe transfers those funds to your balance.

When a customer has unreconciled funds within Stripe for more than ninety days, Stripe transfers those funds to your balance.

- Balance transaction type(s): transferred_to_balance_transaction

- Section(s) in the monthly report: Other Adjustments

These reporting categories are created as part of using the Issuing API.

These reporting categories are created as part of using the Issuing API.

[Issuing API](/issuing)

When an issued card is used to make a purchase, an authorization is created. If the authorization is approved, a balance transaction is created with the type issuing_authorization_hold to hold the authorized amount in reserve from your account balance, until the authorization is either captured or voided. Some merchants can also update an authorization to request an additional amount (e.g., to extend a hotel booking or add a tip), and this is also represented as a balance transaction with the type issuing_authorization_hold.

When an issued card is used to make a purchase, an authorization is created. If the authorization is approved, a balance transaction is created with the type issuing_authorization_hold to hold the authorized amount in reserve from your account balance, until the authorization is either captured or voided. Some merchants can also update an authorization to request an additional amount (e.g., to extend a hotel booking or add a tip), and this is also represented as a balance transaction with the type issuing_authorization_hold.

[an issued card](/issuing)

[authorization](/issuing/purchases/authorizations)

- Balance transaction type(s): issuing_authorization_hold

- Section(s) in the monthly report: Other Adjustments

When an authorized purchase, made with an issued card, is captured by the merchant, the funds previously held for the authorization (issuing_authorization_hold) are released with a issuing_authorization_release balance transaction. Simultaneously, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance in another balance transaction with the type issuing_transaction.

When an authorized purchase, made with an issued card, is captured by the merchant, the funds previously held for the authorization (issuing_authorization_hold) are released with a issuing_authorization_release balance transaction. Simultaneously, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance in another balance transaction with the type issuing_transaction.

[an issued card](/issuing)

[an issuing transaction](/issuing/transactions)

- Balance transaction type(s): issuing_authorization_release

- Section(s) in the monthly report: Other Adjustments

Credits to your balance for rewards, discounts, and other miscellaneous adjustments.

Credits to your balance for rewards, discounts, and other miscellaneous adjustments.

- Balance transaction type(s): issuing_disbursement

- Section(s) in the monthly report: Other Adjustments

When you dispute an Issuing transaction and funds return to your Stripe balance.

When you dispute an Issuing transaction and funds return to your Stripe balance.

[Issuing transaction](/issuing/transactions)

- Balance transaction type(s): issuing_dispute

- Section(s) in the monthly report: Other Adjustments

When an authorized purchase, made with an issued card, has been authorized and captured by the merchant, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance with a issuing_transaction balance transaction.

When an authorized purchase, made with an issued card, has been authorized and captured by the merchant, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance with a issuing_transaction balance transaction.

[issued card](/issuing)

[an issuing transaction](/issuing/transactions)

- Balance transaction type(s): issuing_transaction

- Section(s) in the monthly report: Other Adjustments

These reporting categories are related to using the Connect API and related APIs, such as instant payouts.

These reporting categories are related to using the Connect API and related APIs, such as instant payouts.

[Connect API](/connect)

[instant payouts](/connect/instant-payouts)

Incrementing available funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

Incrementing available funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

[instant payouts](/connect/instant-payouts)

- Balance transaction type(s): advance

- Section(s) in the monthly report: Other Adjustments

Decrementing pending funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

Decrementing pending funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

[instant payouts](/connect/instant-payouts)

- Balance transaction type(s): advance_funding

- Section(s) in the monthly report: Other Adjustments

If one of your connected accounts has a negative balance for 180 days, Stripe transfers a portion of your balance, to zero out that account’s balance. Learn more.

If one of your connected accounts has a negative balance for 180 days, Stripe transfers a portion of your balance, to zero out that account’s balance. Learn more.

[Learn more](/connect/account-balances#understanding-connected-reserve-balances)

- Balance transaction type(s): connect_collection_transfer

- Section(s) in the monthly report: Reflected in "Reserve" section

If one of your connected accounts’ balances becomes negative, Stripe temporarily reserves a portion of your balance to ensure that funds can be covered.If one of your connected accounts’ previously negative balance becomes less negative due to activity on account, another reserve_transaction is created to release a corresponding portion of the funds held in reserve. Learn more.

If one of your connected accounts’ balances becomes negative, Stripe temporarily reserves a portion of your balance to ensure that funds can be covered.

If one of your connected accounts’ previously negative balance becomes less negative due to activity on account, another reserve_transaction is created to release a corresponding portion of the funds held in reserve. Learn more.

[Learn more](/connect/account-balances#understanding-connected-reserve-balances)

- Balance transaction type(s): reserve_transaction

- Section(s) in the monthly report: Reflected in "Reserve" section

Earnings you’ve generated by collecting platform fees via Stripe Connect charges.

Earnings you’ve generated by collecting platform fees via Stripe Connect charges.

[platform fees](/connect/direct-charges#collecting-fees)

[Stripe Connect charges](/connect/charges)

- Balance transaction type(s): application_fee

- Section(s) in the monthly report: Application Revenue

Platform fees that you have returned to your connected accounts.

Platform fees that you have returned to your connected accounts.

[Platform fees](/connect/direct-charges#collecting-fees)

- Balance transaction type(s): application_fee_refund

- Section(s) in the monthly report: Application Revenue Returned

Funds sent from your balance to the balance of your connected accounts.

Funds sent from your balance to the balance of your connected accounts.

[connected accounts](/connect/separate-charges-and-transfers)

- Balance transaction type(s): transferor recipient_transfer

- Section(s) in the monthly report: Payouts and Transfers

Transfers to your connected accounts that have been cancelled.

Transfers to your connected accounts that have been cancelled.

- Balance transaction type(s): transfer_cancel, transfer_refund, recipient_transfer_cancel, or recipient_transfer_failure

- Section(s) in the monthly report: Payouts and Transfers: Failures and Refunds
