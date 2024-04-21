# Working with balances and transactions

Financial accounts have their own balance separate from the balance of the account they’re attached to (platform account or connected account). Balance objects record the amount of funds in a financial account and their state of availability. Transaction and TransactionEntry objects debit or credit the funds in that balance.

[Financial accounts](/treasury/account-management/financial-accounts)

## Balances

A financial account has a balance of funds. The sum total of the balance isn’t always available for spending, however, as it might include pending transactions into or out of the financial account. The financial account balance contains three properties that define the availability of its funds:

- cash—funds the user can spend right now.

- inbound_pending—funds not spendable yet, but that will become available at a later time. The inbound_pending property is reserved for future functionality and always has a value of 0.

- outbound_pending—funds in the account, but not spendable because they’re being held for pending outbound flows.

Use GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} to retrieve the balance details of a financial account with the associated ID. Provide the Stripe-Account header if the financial account is attached to one of your connected accounts. If the financial account is attached to your platform account, don’t include the Stripe-Account header.

If successful, the response is a FinancialAccount object with a balance hash that details the funds and their availability.

[FinancialAccount](/api/treasury/financial_accounts)

As stated in our custodial account agreement, Stripe doesn’t yet offer an overdraft feature on financial accounts. If your balance is insufficient to cover a transaction, Stripe rejects the transaction where possible. Otherwise, the account moves to a negative balance, which you then need to remediate.

[custodial account agreement](https://stripe.com/treasury-connect-account/legal)

For example, if your financial account balance is less than 100 USD, a 100 USD issuing authorization fails due to insufficient funds because Stripe recognizes the attempted overcharge. However, if your account balance is 50 USD and you pay for a 50 USD meal, then add a 15 USD tip after the initial authorization, the issuing authorization succeeds. Stripe authorizes the charge because the overcharge amount isn’t known. As a result, the 65 USD issuing over capture succeeds and results in a negative 15 USD available balance. You must then add funds to your financial account to avoid subsequent transactions being denied with insufficient funds.

[over capture](/issuing/purchases/transactions?issuing-capture-type=over_capture)

If a connected account on your platform has a financial account with a negative balance and doesn’t add funds to it, you’re responsible for covering the negative amount.

Stripe emails you a monthly reminder if your platform has any associated financial accounts that have had negative balances for more than 15 days. However, you need to regularly monitor account balances and take remediation steps as soon as possible when a balance goes negative. Don’t wait for the reminder email to address a negative balance.

You can have Treasury financial accounts cover negative payment balances for connected accounts using automatic debits. For more information, see the Negative balances on accounts section of the risk management best practices.

[Negative balances on accounts section](/connect/risk-management/best-practices#negative-balances-on-accounts)

## Transactions

All changes to a balance have a corresponding Transaction object that details money movements. Transactions affect only one balance and are in only one currency (currently, Stripe Treasury supports only USD).

[Transaction](/api/treasury/transactions)

Each transaction points to the balance-affecting money movement object, such as an OutboundTransfer, ReceivedCredit, or ReceivedDebit.

[OutboundTransfer](/api/treasury/outbound_transfers)

[ReceivedCredit](/api/treasury/received_credits)

[ReceivedDebit](/api/treasury/received_debits)

The available Transaction endpoints enable you to retrieve specific transactions and list or filter transactions affecting a financial account. There are no webhooks available for transactions, but webhooks are available for the associated money movement objects (for example, OutboundPayments).

## Retrieve a transaction

Use GET/v1/treasury/transactions/{{TRANSACTION_ID}} to retrieve the transaction with the associated ID.

If successful, the response returns the Transaction object.

Use GET /v1/treasury/transactions to list transactions for a financial account. Set the required financial_account parameter in the body to the value of the financial account ID to retrieve transactions for. Include additional parameters to filter the results returned.

In addition to the standard set of list parameters, you can filter transactions by the following.

[standard set of list parameters](/api/pagination)

- status

- flow

- Either created or posted_at, but not both

The following request retrieves the three most recent transactions created on the financial account that have a status of posted.

There are no webhooks for transactions because the various money movements that initiate a transaction have their own webhooks.

## Transaction entries

TransactionEntry objects are the most granular view of money movements that affect a financial account balance. A single flow of money comprises multiple individual money movements, each represented by a transaction. Transactions, in turn, are an aggregation of transaction entries. For example, when initiating an outbound payment of $10.00 at time T, funds are moved from the cash sub-balance to the outbound_pending sub-balance. The following Transaction object response demonstrates this initial event.

[TransactionEntry](/api/treasury/transaction_entries)

After the outbound payment posts at time T+1, the funds are deducted from outbound_pending and a new transaction entry is added to the transaction. The following Transaction response demonstrates this progression.

As the preceding responses show, a transaction can contain multiple transaction entries. The available TransactionEntry endpoints enable you to retrieve specific transaction entries and list or filter them for a particular transaction.

A Transaction in the void status won’t have any new transaction entries added to it. A Transaction in the posted status where all balance_impact is to the cash sub-balance won’t have any new transaction entries added to it, either.

Use GET /v1/treasury/transaction_entries/{{TRANSACTIONENTRY_ID}} to retrieve details for the transaction entry with the associated ID.

If successful, the response returns a TransactionEntry object with the following form.

Use GET /v1/treasury/transaction_entries to list the transaction entries for a financial account. Set the required financial_account parameter in the body to the value of the financial account ID to retrieve transaction entries for. Include additional parameters if you want to filter the list.

In addition to the standard set of list parameters, you can filter transaction entries by:

[standard set of list parameters](/api/pagination)

- transaction

- Either created or effective_at, but not both

The following request retrieves the transaction entries created before {{Timestamp}} and orders them by created date.

There are no webhooks for transaction entries because the various money movements that initiate a transaction entry have their own webhooks.
