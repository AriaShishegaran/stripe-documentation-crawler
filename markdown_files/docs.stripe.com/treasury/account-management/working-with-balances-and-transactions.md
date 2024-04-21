htmlWorking with balances and transactions | Stripe Documentation[Skip to content](#main-content)Working with balances and transactions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccount-management%2Fworking-with-balances-and-transactions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccount-management%2Fworking-with-balances-and-transactions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Working with balances and transactions

Learn about Treasury account balances and the effect transactions have on them.Financial accounts have their own balance separate from the balance of the account they’re attached to (platform account or connected account). Balance objects record the amount of funds in a financial account and their state of availability. Transaction and TransactionEntry objects debit or credit the funds in that balance.

## Balances

A financial account has a balance of funds. The sum total of the balance isn’t always available for spending, however, as it might include pending transactions into or out of the financial account. The financial account balance contains three properties that define the availability of its funds:

- `cash`—funds the user can spend right now.
- `inbound_pending`—funds not spendable yet, but that will become available at a later time. The`inbound_pending`property is reserved for future functionality and always has a value of 0.
- `outbound_pending`—funds in the account, but not spendable because they’re being held for pending outbound flows.

Use GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} to retrieve the balance details of a financial account with the associated ID. Provide the Stripe-Account header if the financial account is attached to one of your connected accounts. If the financial account is attached to your platform account, don’t include the Stripe-Account header.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, the response is a FinancialAccount object with a balance hash that details the funds and their availability.

`{
  "object": "treasury.financial_account",
  "id": "{{FINANCIAL_ACCOUNT_ID}}",
  ...
  "balance": {
    // $90 is currently available for use,
    // with an additional $10 held in the outbound_pending sub-balance
    "cash": {"usd": 9000},
    "inbound_pending": {"usd": 0},
    "outbound_pending": {"usd": 1000}
  }
}`### Negative balances and overdrafts

As stated in our custodial account agreement, Stripe doesn’t yet offer an overdraft feature on financial accounts. If your balance is insufficient to cover a transaction, Stripe rejects the transaction where possible. Otherwise, the account moves to a negative balance, which you then need to remediate.

For example, if your financial account balance is less than 100 USD, a 100 USD issuing authorization fails due to insufficient funds because Stripe recognizes the attempted overcharge. However, if your account balance is 50 USD and you pay for a 50 USD meal, then add a 15 USD tip after the initial authorization, the issuing authorization succeeds. Stripe authorizes the charge because the overcharge amount isn’t known. As a result, the 65 USD issuing over capture succeeds and results in a negative 15 USD available balance. You must then add funds to your financial account to avoid subsequent transactions being denied with insufficient funds.

If a connected account on your platform has a financial account with a negative balance and doesn’t add funds to it, you’re responsible for covering the negative amount.

Stripe emails you a monthly reminder if your platform has any associated financial accounts that have had negative balances for more than 15 days. However, you need to regularly monitor account balances and take remediation steps as soon as possible when a balance goes negative. Don’t wait for the reminder email to address a negative balance.

NoteYou can have Treasury financial accounts cover negative payment balances for connected accounts using automatic debits. For more information, see the Negative balances on accounts section of the risk management best practices.

## Transactions

All changes to a balance have a corresponding Transaction object that details money movements. Transactions affect only one balance and are in only one currency (currently, Stripe Treasury supports only USD).

Each transaction points to the balance-affecting money movement object, such as an OutboundTransfer, ReceivedCredit, or ReceivedDebit.

### Transaction state machine

StatusState appliedDescriptionTransitions to`open`initialThis is the initial state for all transactions. The transaction results in updates to the sub-balance amounts, but the current balance isn’t affected until the transaction posts.`posted`or`void``posted`terminalFunds have successfully entered or left the account. The current balance was affected.N/A`void`terminalThe transaction never impacted the balance. For example, a transaction enters this state if an outbound payment was initiated but then canceled before the funds left the account.N/AThe available Transaction endpoints enable you to retrieve specific transactions and list or filter transactions affecting a financial account. There are no webhooks available for transactions, but webhooks are available for the associated money movement objects (for example, OutboundPayments).

## Retrieve a transaction

Use GET/v1/treasury/transactions/{{TRANSACTION_ID}} to retrieve the transaction with the associated ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/transactions/txn_123 \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, the response returns the Transaction object.

[JSON (commented)](#)`{
  "id": "{{TRANSACTION_ID}}",
  "object": "treasury.transaction",
  "created": "{{Timestamp}}",
  "livemode": false,
  // The FinancialAccount this Transaction impacts
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // The flow responsible for this Transaction. Each Transaction is created
  // synchronously (that is, in the same API request for initiated objects) with
  // its flow.`See all 75 lines### List Transactions

Use GET /v1/treasury/transactions to list transactions for a financial account. Set the required financial_account parameter in the body to the value of the financial account ID to retrieve transactions for. Include additional parameters to filter the results returned.

In addition to the standard set of list parameters, you can filter transactions by the following.

- `status`
- `flow`
- Either`created`or`posted_at`, but not both

`{
  // Standard list parameters
  limit, starting_after, ending_before,
  // Filter by FinancialAccount, required
  financial_account: "{{FINANCIAL_ACCOUNT_ID}}"
  // Filter by status
  status: "open" | "posted" | "void",
  // Filter by flow
  flow: "{{FLOW_OBJECT_ID}}",
  // Order the results by the created or posted_at timestamps, default is `created`.
  // For order_by=posted_at, setting status='posted' is required
  order_by: "created" | "posted_at",
  // created can only be specified with order_by = 'created'
  created: {gt, gte, lt, lte},
  status_transitions: {
    // status_transitions.posted_at can only be specified with order_by = 'posted_at' and status = 'posted'
    posted_at: {gt, gte, lt, lte}
  }
}`The following request retrieves the three most recent transactions created on the financial account that have a status of posted.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/transactions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d limit=3 \
  -d status=posted \
  -d order_by=created`### Webhooks

There are no webhooks for transactions because the various money movements that initiate a transaction have their own webhooks.

## Transaction entries

TransactionEntry objects are the most granular view of money movements that affect a financial account balance. A single flow of money comprises multiple individual money movements, each represented by a transaction. Transactions, in turn, are an aggregation of transaction entries. For example, when initiating an outbound payment of $10.00 at time T, funds are moved from the cash sub-balance to the outbound_pending sub-balance. The following Transaction object response demonstrates this initial event.

`{
  "id": "{{TRANSACTION_ID}}",
  "object": "treasury.transaction",
  "created": "{{T}}",
  ...
  "flow": "{{OUTBOUND_PAYMENT_ID}}",
  "flow_type": "outbound_payment",
  "status": "open",
  "amount": -1000,
  "currency": "usd",`See all 36 linesAfter the outbound payment posts at time T+1, the funds are deducted from outbound_pending and a new transaction entry is added to the transaction. The following Transaction response demonstrates this progression.

`{
  "id": "{{TRANSACTION_ID}}",
  "object": "treasury.transaction",
  "created": "{{T}}",
  ...
  "flow": "{{OUTBOUND_PAYMENT_ID}}",
  "flow_type": "outbound_payment",
  "status": "posted",
  "amount": -1000,
  "currency": "usd",`See all 49 linesAs the preceding responses show, a transaction can contain multiple transaction entries. The available TransactionEntry endpoints enable you to retrieve specific transaction entries and list or filter them for a particular transaction.

A Transaction in the void status won’t have any new transaction entries added to it. A Transaction in the posted status where all balance_impact is to the cash sub-balance won’t have any new transaction entries added to it, either.

### Retrieve transaction entries

Use GET /v1/treasury/transaction_entries/{{TRANSACTIONENTRY_ID}} to retrieve details for the transaction entry with the associated ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/transaction_entries/{{TRANSACTION_ENTRY_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, the response returns a TransactionEntry object with the following form.

`{
  "id": "{{TRANSACTION_ENTRY_ID}}",
  "object": "treasury.transaction_entry",
  "created": "{{Timestamp}}",
  "livemode": false,
  // The FinancialAccount this transaction entry impacts.
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // The transaction that this transaction entry belongs to.
  "transaction": "{{TRANSACTION_ID}}",
  // The flow responsible for this transaction entry.`See all 56 lines### List TransactionEntries

Use GET /v1/treasury/transaction_entries to list the transaction entries for a financial account. Set the required financial_account parameter in the body to the value of the financial account ID to retrieve transaction entries for. Include additional parameters if you want to filter the list.

In addition to the standard set of list parameters, you can filter transaction entries by:

- `transaction`
- Either`created`or`effective_at`, but not both

`{
  // Standard list parameters
  limit, starting_after, ending_before,
  // Filter by FinancialAccount, required
  financial_account: "fa_123"
  // Filter by transaction
  transaction: 'trxn_123',
  // Order the results by the created or effective_at timestamps, default is `created`.
  order_by: "created" | "effective_at",
  // created can only be specified with order_by = 'created'
  created: {gt, gte, lt, lte},
  // effective_at can only be specified with order_by = 'effective_at'
  effective_at: {gt, gte, lt, lte},
}`The following request retrieves the transaction entries created before {{Timestamp}} and orders them by created date.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/transaction_entries \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d order_by=created \
  -d "created[lt]"=1234567890`### Webhooks

There are no webhooks for transaction entries because the various money movements that initiate a transaction entry have their own webhooks.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Balances](#balances)[Transactions](#transactions)[Retrieve a transaction](#retrieve-a-transaction)[Transaction entries](#transaction-entries)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`