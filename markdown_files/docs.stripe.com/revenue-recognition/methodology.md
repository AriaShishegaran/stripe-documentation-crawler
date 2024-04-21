htmlRevenue Recognition methodology | Stripe Documentation[Skip to content](#main-content)How revenue recognition works[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fmethodology)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)# Revenue Recognition methodology

Learn how Revenue Recognition works out of the box within Stripe.Revenue Recognition is integrated with other Stripe objects to provide intelligent default settings for how revenue should be recognized.

Revenue Recognition automatically calculates all transactions that happen within Stripe down to the millisecond, including subscriptions, invoices, one-time payments, refunds, disputes, and so on.

NoteRevenue recognition requirements vary based on a number of factors and the parameters listed above may or may not fit your business. You need to ensure that you understand and comply with the requirements applicable to your business, and that you model your business accordingly.

## Chart of accounts

Revenue recognition is built on top of a double-entry accounting ledger that tracks debits and credits resulting from your business activity.

To get the most out of Revenue Recognition, it helps to understand the default chart of accounts and the debits and credits that impact those accounts.

Income statement accountsBalance sheet accountsAccountDebit/Credit typeDescriptionRevenueRevenue (credit)Recognizable portion of finalized invoices, prorated invoice items, and metered billing that count towards revenue during the month. For example, if an invoice line item is for 90 USD with 10 USD in taxes, the total invoice is 100 USD, but the recognizable portion is only 90 USD.RefundsContra Revenue (debit)Portion of the refunded amount previously recognized. For example, if you issue a 120 USD refund on an annual subscription during the second month, 20 USD for the first 2 months is contra revenue. The remaining 100 USD is adjusted and reflected in your deferred revenue balance in the balance sheet.DisputesContra Revenue (debit)Portion of the disputed amount previously recognized. For example, if there’s a 120 USD dispute on an annual subscription during the second month, 20 USD for the first 2 months is contra revenue. The remaining 100 USD is adjusted and reflected in your deferred revenue balance in the balance sheet.CreditNotesContra Revenue (debit)Portion of the credit note amount previously recognized. For example, if there’s a 120 USD credit note on an annual subscription during the second month, 20 USD for the first 2 months is contra revenue. The remaining 100 USD is adjusted and reflected in your deferred revenue balance in the balance sheet.BadDebtContra Revenue (debit)Previously recognized revenue from invoices that have been marked as uncollectible.VoidsContra Revenue (debit)Previously recognized revenue from invoices that have been voided.UnbilledVoidsContra Revenue (debit)Previously recognized revenue from prorated invoice items that have been deleted. These items are sometimes deleted when they generate unbilled accounts receivable and revenue.TransferContra Revenue (debit)Previously recognized revenue from separate transfers.DiscountsContra Revenue (debit)Recognized revenue from invoices that received discounts. Revenue Recognition discount as contra revenue support is currently in private beta.CustomerBalanceAdjustmentsExpense (debit)Expenses incurred due to manual adjustments to a customer credit balance or exclusion associated with post-paid credit notes on customer balance.ExternalCustomerBalanceAdjustmentsExpense (debit)Expenses incurred due to exclusion associated with post-paid credit notes on external customer balance.UnderpaymentsExpense (debit)Expenses incurred due to transfers that underpay an invoice, as used by the[customer credit balance](/invoicing/bank-transfer#underpayments)payment method or[Sources](/sources/customers).FeesExpenses (debit)Expenses incurred due to Stripe fees. Revenue Recognition Stripe fees support is currently in private beta.RecoverablesGains (credit)Recovered funds that aren’t attributable to revenue. For example, if you have a 120 USD dispute on an annual subscription during the second month, 20 USD for the first 2 months is contra revenue and the remaining 100 USD is adjusted from the deferred revenue balance. If you win the dispute and 120 USD is returned to you, 20 USD is reflected as revenue and the remaining 100 USD is reflected as recoverables.ExclusionGains (credit)Excluded funds that aren’t attributable to revenue. To exclude transactions, set up[exclusion rules](/revenue-recognition/rules/create-a-rule#treatments)or use[exclusion import](/revenue-recognition/data-import#exclusion-import).FxLossLoss (debit)Total loss due to foreign currency exchange rates.ConnectTransferLossLoss (debit)Total loss due to destination charge refund, and the transfer reversal will reverse the ConnectTransferLoss account.## Data modeling for Revenue Recognition

You can better understand Revenue Recognition by understanding the data modeling—see the following descriptions of how Revenue Recognition handles common Stripe resources.

### Subscriptions and Invoicing

Subscriptions and Invoices are higher level resources that contain detailed information about each transaction.

Subscriptions create invoices on each cycle, with each subscription item corresponding to an invoice line item. The period of each line item is automatically populated with the period of the subscription item.

Revenue recognition treats each invoice line item as its own performance obligation. When the invoice finalizes, the total recognizable amount is deferred and subsequently amortized evenly over the period of each invoice line item.

If a period isn’t set on an invoice line item, the amount on that invoice line item is recognized entirely when the invoice is finalized. Use the Data Import feature to configure your invoice data, or set rules to customize when and how invoice line items are recognized.

For more details and examples regarding how Revenue Recognition handles subscriptions and invoices with specific scenarios involving upgrades, downgrades, discounts, taxes, and so on, review the Subscriptions and Invoicing page.

### One-time payments

One-time payments created in the Dashboard or through the Charges and PaymentIntents APIs don’t contain as much information as invoices.

Because no service period or fulfillment information exists for them, by default, one-time payments are recognized immediately when the payment occurs.

Import data to add a service period or split a payment into different revenue recognition schedules. This allows you to customize revenue treatment behavior and configure rules such as payment amount, description, and customer email.

For more details and examples on how Revenue Recognition handles one-time payments, review the One-time payments page.

### Refunds and disputes

Revenue Recognition handles refunds and disputes by generating contra revenue to offset already recognized revenue.

For transactions with both already-recognized and deferred revenue, the recognized portion is added to either the refunds or disputes contra revenue account, which cancels out the deferred revenue.

For more details and examples on how Revenue Recognition handles refunds and disputes, review the Refunds and Disputes page.

### External transactions

You can track revenue collected outside of Stripe using invoices. Configure the invoice as you would any other, and then mark the invoice as paid either directly in the Dashboard, or through the paid_out_of_band option in the API.

Invoices marked as paid outside of Stripe contribute not to the cash account, but rather to the external asset account.

CautionIf you’d like to consolidate your financial data from outside Stripe onto Revenue Recognition, review the Data import page.

### Multi-currency

If your business handles transactions in multiple currencies, accurately recognizing revenue can be complicated.

Revenue Recognition processes transactions and generates journal entries based on your account’s settlement currencies. Transactions with presentment currencies that aren’t supported as settlement currencies are automatically converted to your account’s default settlement currency.

For payments and paid invoices, we use the exchange rate for the actual money movement (that is, reflected on the balance transaction). If you incur a time delay between issuing a bill (for example, an invoice) and it getting paid, the difference in amounts because of changing exchange rates between the two times is added to the FxLoss account.

For more details and examples on how Revenue Recognition handles multiple currencies, review the Multi-currency page.

### Data availability

Revenue Recognition computes your data twice daily, at 0:00am UTC and at 12:00pm UTC.

The data processed at 0:00am UTC encompasses account activity from the prior day’s 12:00pm to that day’s 11:59pm UTC. The 12:00pm UTC update covers activity from 0:00am to 11:59am UTC of the same day.

It can take 16-72 hours to process the data. Users in time zones far from UTC might notice slight delays in reports because late-day activity in PST corresponds to early hours of the following day in UTC.

As an example, you might have account activity occurring on August 1, 2023, from 0:00 am to 11:59 am UTC. You can expect to see this activity reflected in the Revenue Recognition reports by August 4, 2023, at 12:00 pm UTC. Similarly, you can access reports for activity from 12:00 pm to 11:59 pm UTC on August 1, 2023 by August 5, 2023, at 0:00 am UTC.

## Journal entries

Every billing activity in Stripe generates a set of journal entries. A journal entry is a record of a transaction. Each journal entry consists of a debit and a credit account. For example, an entry which finalizes an invoice would debit AccountsReceivable and credit DeferredRevenue. Paying an invoice would debit Cash and credit AccountsReceivable.

These entries may occur in asset, liability, equity, expense, or revenue accounts. You can learn more about the definitions of each account that will appear in a journal entry under our Chart of accounts section.

The table below shows the applicable billing activities for common journal entries. You can export journal entries to CSV using the debits and credits report, which you can find in the Reports tab in the Dashboard. In addition, there are options to download debits and credits reports by the event type, which provide a brief description of the recorded event, making it easier to understand the nature of each journal entry.

CautionThe following table isn’t the complete set of entries. We’ll be periodically updating the entries. If there’s a specific entry that you require assistance with, please create a ticket on our support page.

DebitCreditDefinitionAccountsReceivableDeferredRevenueInvoice being finalizedUnbilledAccountsReceivableUnbilled invoice item being invoicedPassthroughFeesFinalize an invoice with passthrough feesTaxLiabilityFinalize an invoice with taxBadDebtAccountsReceivableMark an invoice as uncollectiblePendingCashMark an invoice with a pending ACH as uncollectibleRecoverablesMark an invoice which is partially paid with customer balance as uncollectibleCashAccountsReceivableInvoice is paidCustomerBalancePaying for a negative customer balanceExclusionCash is excludedPendingCashACH paying invoice is confirmedRecoverablesWinning a dispute for amounts that were previously adjusted from deferred revenue balanceConnectTransferLossCashLoss from a transferCreditNotesAccountsReceivablePrepaid credit note is issued on an unpaid invoiceCustomerBalancePost paid credit note credits customer balanceExternalCustomerBalancePost paid credit note credits external customer balanceCustomerBalanceCustomerBalanceAdjustmentsReduce the amount owned by the customerCustomerBalanceAdjustmentsCustomerBalanceIncrease  the amount owned by the customerDeferredRevenueCashCaused by Refunds and DisputesRevenueRevenue is recognizedExternalAssetAccountsReceivableMark an invoice as paid outside of StripeRefundsCashRefundTaxLiabilityCustomerBalanceCredit note on an invoice with tax, and it credits customer balanceExternalCustomerBalanceCredit note on an invoice with tax, and it credits external customer balanceUnbilledAccountsReceivableRevenueRevenue recognized on unbilled invoice itemUnbilledVoidsUnbilledAccountsReceivableUnbilled invoice item is deletedVoidsAccountsReceivableVoid an invoiceBadDebtVoid an uncollectible invoiceCustomerBalanceVoid an invoice partially paid with customer balanceThe activities above are all based on positive amounts. It is important to note that these billing activities can be reversed. These reverse activities occur when activities are triggered on negative invoice line item amounts.

## Negative Line Item

A negative line item occurs when the value of the line item becomes higher than the amount it is paid for. This occurs typically during a subscription downgrade or upgrade when the product tier changes.

Here is an example of journal entries which contains a negative line item caused by a downgrade:

- On April 1, the invoice is generated for a monthly subscription worth $90 USD and the customer pays for it.
- On April 21, the customer requests a downgrade of their service to a $30 USD subscription. This results in 2 unbilled line items for the remaining time of the subscription.  - il_1  is for the remaining time on new plan worth $10
  - il_2 is for the remaining time of old plan worth $-30


- On May 1, the invoice is generated containing the line items generated by the downgrade as well for the new line item, il_3, representing the month of May. The customer pays for the invoice on the same day.
- On May 4, the customer requests a full refund on the invoice for May, resulting in full refunds on the line item created by the downgrade as well as the new line item for May.  We process the refund.

DateDebitCreditAmountLine Item2022-04-21UnbilledAccountsReceivableRevenue$10il_1RevenueUnbilledAccountsReceivable$30il_22022-05-01AccountsReceivableDeferredRevenue$30il_3CashAccountsReceivable$30il_3DeferredRevenueRevenue$30il_3AccountsReceivableUnbilledAccountsReceivable$10il_1CashAccountsReceivable$10il_1UnbilledAccountsReceivableAccountsReceivable$30il_2AccountsReceivableCash$30il_22022-05-04RefundsCash$10il_1CashRefunds$30il_2RevenueCash$30il_3Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Chart of accounts](#chart-of-accounts)[Data modeling for Revenue Recognition](#data-modeling-for-revenue-recognition)[Journal entries](#journal-entries)[Negative Line Item](#negative-line-item)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`