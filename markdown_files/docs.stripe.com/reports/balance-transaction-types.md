htmlBalance transaction types | Stripe Documentation[Skip to content](#main-content)Balance transaction types[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fbalance-transaction-types)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fbalance-transaction-types)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Basic financial reports](/docs/reports)[Categories and types](/docs/reports/reporting-categories)# Balance transaction types

Learn more about the different types of balance transactions that represent funds moving through your Stripe account.Balance transactions are our recommended starting point for reporting on your account’s balance activity. We create them for every type of transaction that comes into, or flows out of, your Stripe account’s balance.

You can create reports that make use of balance transactions using the API or Sigma.

When you first receive a payment in your account, we initially reflect it as a pending balance (less any Stripe fees). This balance becomes available according to your payout schedule. The status attribute on balance transactions indicates the type of the balance.

To classify transactions for accounting purposes, use the reporting_category field instead of the type field.

## Balance transaction source

Balance transactions include a source field that contains the ID of the related Stripe object.

Use the API to retrieve additional information about the payment activity that caused the creation of the Balance transaction. Using Sigma, you can also join the balance_transactions table with other tables using the source_id column.

## Balance transaction types

You can organize balance transaction types into different groups based on the underlying activity that generated the balance transactions.

If you’re not using the Connect API or Issuing API, your balance transactions belong in the first two groups (“related to charges and payments” or “related to Stripe balance changes”).

### Balance transaction types related to charges and payments

These balance transaction types are related to creating and refunding charges as part of processing payments.

TypeDescriptionchargeCreated when a credit card charge is created successfully.

paymentCreated when a local payment method charge is created successfully.

payment_failure_refundACH, direct debit, and other delayed notification payment methods remain in a pending state until they either succeed or fail. You’ll see a pending Balance transaction of type payment when the payment is created. Another Balance transaction of type payment_failure_refund appears if the pending payment later fails.

payment_refundCreated when a local payment method refund is initiated.

Additionally, if your customer’s bank or card issuer is unable to correctly process a refund (e.g., due to a closed bank account or a problem with the card) Stripe returns the funds to your balance. The returned funds are represented as a Balance transaction with the type payment_refund.

payment_reversalCreated when a debit/failure related to a payment is detected from a banking partner. This balance transaction takes funds that were previously credited to the merchant for a payment out of the merchant balance.

refundCreated when a credit card charge refund is initiated.

If you authorize and capture separately and the capture amount is less than the initial authorization, you see a balance transaction of type charge for the full authorization amount and another balance transaction of type refund for the uncaptured portion.

refund_failureCreated when a credit card charge refund fails, and Stripe returns the funds to your balance.

This may occur if your customer’s bank or card issuer is unable to correctly process a refund (e.g., due to a closed bank account or a problem with the card).

### Balance transaction types related to Stripe balance changes

These balance transaction types are related to changes that affect your Stripe balance such as payouts, fees and top-ups.

TypeDescriptionadjustmentAdjustments correspond to additions or deductions from your Stripe balance that are made outside of the normal charge/refund flow. For example, some of the most common reasons for adjustments are:

- Refund failures. If your customer’s bank or card issuer is unable to correctly processa refund (e.g., due to a closed bank account or a problem with the card) Stripe returns thefunds to your balance. The returned funds are represented as a Balance transaction with thetype`adjustment`, where the description indicates the related refund object.
- Disputes. When a customer[disputes a charge](/disputes), Stripe deducts thedisputed amount from your balance. The deduction is represented as a Balance transactionwith the type`adjustment`, where the source object is a dispute.
- Dispute reversals. When you[win a dispute](/disputes#responding-to-a-dispute), the disputed amount is returned to yourbalance. The returned funds are represented as a Balance transaction with the type`adjustment`, where the source object is a dispute.
- In the past, fees for Stripe software and services (e.g., for Radar, Connect and Billing)were represented as adjustments.
- In the past, Connect platform fee refunds were represented as adjustments.

The description field on the Balance transaction describes the purpose of each adjustment.

anticipation_repaymentRepayments made to service an anticipation loan in Brazil. These repayments go to the financial institution to whom you have sold your receivables.

balance_transfer_inboundFunds moving into a balance (e.g. Issuing balance) from another balance (e.g. Stripe balance)

balance_transfer_outboundFunds moving from your Stripe balance to a different (e.g. Issuing) balance.

climate_order_purchaseFunds used to purchase carbon removal units from Frontier Climate.

climate_order_refundFunds refunded to your balance when a Climate Order is canceled.

contributionFunds contributed via Stripe to a cause (currently Stripe Climate).

obligation_outboundObligation for receivable unit received.

obligation_reversal_inboundObligation for receivable unit reversed.

payment_network_reserve_holdFunds that a payment network holds in reserve (e.g. to mitigate risk).

payment_network_reserve_releaseFunds that a payment network releases from a reserve.

payment_unreconciledCreated when a customer has unreconciled funds within Stripe for more than ninety days. This balance transaction transfers those funds to your balance.

payoutPayouts from your Stripe balance to your bank account.

payout_cancelCreated when a payout to your bank account is cancelled and the funds are returned to your Stripe balance.

payout_failureCreated when a payout to your bank account fails and the funds are returned to your Stripe balance.

reserved_fundsWhen Stripe holds your funds in reserve to mitigate risk, two balance transactions are created: one to debit the funds from your balance, and a second to credit the funds back to your balance at the end of the reserve period.

stripe_feeFees for Stripe software and services (e.g., for Radar, Connect, Billing, and Identity).

stripe_fx_feeStripe currency conversion fee

tax_feeTaxes collected by Stripe to be remitted to the appropriate local governments. Typically, this is a tax on Stripe fees.

topupFunds you transferred into your Stripe balance from your bank account. Learn more.

topup_reversalIf an initially successful top-up fails or is cancelled, the credit to your Stripe balance is reversed. Learn more.

### Balance transaction types related to Issuing

These balance transaction types are created as part of using the Issuing API.

TypeDescriptionissuing_authorization_holdWhen an issued card is used to make a purchase, an authorization is created. If the authorization is approved, a balance transaction is created with the type issuing_authorization_hold to hold the authorized amount in reserve from your account balance, until the authorization is either captured or voided. Some merchants can also update an authorization to request an additional amount (e.g., to extend a hotel booking or add a tip), and this is also represented as a balance transaction with the type issuing_authorization_hold.

issuing_authorization_releaseWhen an authorized purchase, made with an issued card, is captured by the merchant, the funds previously held for the authorization (issuing_authorization_hold) are released with a issuing_authorization_release balance transaction. Simultaneously, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance in another balance transaction with the type issuing_transaction.

issuing_disputeWhen you dispute an Issuing transaction and funds return to your Stripe balance.

issuing_transactionWhen an authorized purchase, made with an issued card, has been authorized and captured by the merchant, an issuing transaction is created, and the purchase amount is deducted from your Stripe balance with a issuing_transaction balance transaction.

### Balance transaction types related to Connect

These balance transaction types are related to using the Connect API and related APIs, such as instant payouts.

TypeDescriptionadvanceIncrementing available funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

advance_fundingDecrementing pending funds for instant payouts. This occurs when you create an instant payout and the requested payout amount is greater than your connected account’s available balance. Funds are added to your available balance and removed from your pending balance to cover the difference.

application_feeEarnings you’ve generated by collecting platform fees via Stripe Connect charges.

application_fee_refundPlatform fees that you have returned to your connected accounts.

connect_collection_transferIf one of your connected accounts has a negative balance for 180 days, Stripe transfers a portion of your balance, to zero out that account’s balance. Learn more.

reserve_transactionIf one of your connected accounts’ balances becomes negative, Stripe temporarily reserves a portion of your balance to ensure that funds can be covered.

If one of your connected accounts’ previously negative balance becomes less negative due to activity on account, another reserve_transaction is created to release a corresponding portion of the funds held in reserve. Learn more.

transferFunds sent from your balance to the balance of your connected accounts.

transfer_cancelTransfers to your connected accounts that have been cancelled.

transfer_failureTransfers to your connected accounts that failed. Transfer failures add to your platform’s balance and subtract from the connected account’s balance.

transfer_refundTransfers to your connected accounts that you reversed or that were reversed as a result of a failure in payments made through ACH, direct debit, and other delayed notification payment methods. Transfer reversals add to your platform’s balance and subtract from the connected account’s balance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Balance transaction source](#source)[Balance transaction types](#types)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`