# Customer credit balance

This page is about customer credit balances, which are adjustments you can issue to customers that apply to future invoices. Credit balances are different from cash balances. Cash balances are connected to the customer balance payment method. To learn more, see Bank transfer. As explained below, some features work differently for customers with a cash balance.

[invoices](/api/invoices)

[customer balance payment method](/payments/bank-transfers)

[Bank transfer](/invoicing/bank-transfer)

Every customer has a credit balance. You can use this to issue a:

- Credit adjustment—You owe the customer money.

- Debit adjustment—The customer owes you money.

These adjustments sum up to a credit balance that you can apply to future invoices. Because Stripe computes the credit balance from a ledger—an immutable list of debit and credit transactions—it provides an audit trail of transactions for the customer. The Customer Balance Transactions can refer to the object related to the adjustment, such as a credit note, invoice, or metadata.

[Customer Balance Transactions](/api/customer_balance_transactions/object)

[credit note](/invoicing/dashboard/credit-notes)

[metadata](/api/metadata)

Some common use cases for customer credit balances include:

- Issuing a credit note to create a credit that reduces the amount due on the next invoice.

[Issuing a credit note](/invoicing/dashboard/credit-notes#issuing)

- Marking an invoice as paid and moving the amount owed to the credit balance as a debit. This happens when the amount due on an invoice is less than the minimum chargeable amount. This functionality only occurs for users without a cash balance.

[minimum chargeable amount](/currencies#minimum-and-maximum-charge-amounts)

[cash balance](#cash-balances)

## Credit balances

Keep the following in mind when you work with credit balances:

- The credit balance automatically applies to the next finalized invoice to a customer.

- You ​​can’t choose a specific invoice to apply the credit balance to.

- The credit balance is in the customer’s currency.

- Customers with a cash balance can’t keep a positive balance. In other words, they can’t increase the amount due on the next invoice.

[Customers](/api/customers)

[cash balance](/api/customers/object#customer_object-cash_balance)

## Credits and debits

Credits are negative values (a reduction in the amount the customer owes) that you can apply to the next invoice. Debits, on the other hand, are positive values (an increase in the amount the customer owes) that you can apply to the next invoice.

## Transactions

All modifications to the credit balance are recorded as Transactions. After you create a transaction, you can only update its description or metadata (you can’t edit other properties or delete it).

[Transactions](/api/customer_balance_transactions/object)

All Transactions that you create with the API or in the Dashboard have a type value of adjustment.  A type value of adjustment represents a debit or credit that you manually created for the customer. The following table describes each of the type values:

[Transactions](/api/customer_balance_transactions/object)

[type](/api/customer_balance_transactions/object#customer_balance_transaction_object-type)

[credit note](/invoicing/dashboard/credit-notes)

[minimum chargeable amount](/currencies#minimum-and-maximum-charge-amounts)

[maximum chargeable amount](/currencies#minimum-and-maximum-charge-amounts)

[receiver Sources](/sources#flow-for-customer-action)

You can only undo a transaction by creating a corresponding, reversing transaction. For example, if you credit the customer ​​10 USD, you’d have to debit them 10 USD in a new transaction, each canceling the other one out.

## Modify the credit balance

You can modify a customer’s credit balance through both the Dashboard and API.

You can modify a customer’s credit balance through the Customers page in the Dashboard by creating a new Customer Balance Transaction adjustment.

[Customers page](https://dashboard.stripe.com/customers)

[Customer Balance Transaction](/api/customer_balance_transactions/object)

In the Customers page, click on the customer and then click Adjust balance under Credit balance. From here, set the Adjustment type, a Currency (only available if the customer doesn’t have a currency set), an Amount, and an internal note.

The internal note is only visible to Dashboard users.

Add a new customer balance transaction adjustment

## Balance transaction history

Audit a customer’s balance adjustments in the Customers page by scrolling down to the Credit balance section. This section displays the current value of the customer credit balance.

Customer cash balances Customers using the bank transfers payment method have a cash balance object with one or more currencies in the available object. You can use the funds to make payments or pay invoices. Customers with available balances have the following behavior:You can’t create a negative customer cash balance since it represents money sent from the Customer.You can’t finalize a too-small or too-large invoice with the cash balance (for example, creating a subscription for 0.01 USD). Learn more about minimum and maximum amounts.You can delete Customers that have a cash balance, but only if their cash balance is 0.You can’t remove a Customer’s available balance.

## Customer cash balances

Customers using the bank transfers payment method have a cash balance object with one or more currencies in the available object. You can use the funds to make payments or pay invoices. Customers with available balances have the following behavior:

[bank transfers](/payments/bank-transfers)

[cash balance object](/api/customers/object#customer_object-cash_balance)

[make payments](/payments/customer-balance#make-cash-payment)

- You can’t create a negative customer cash balance since it represents money sent from the Customer.

You can’t create a negative customer cash balance since it represents money sent from the Customer.

- You can’t finalize a too-small or too-large invoice with the cash balance (for example, creating a subscription for 0.01 USD). Learn more about minimum and maximum amounts.

You can’t finalize a too-small or too-large invoice with the cash balance (for example, creating a subscription for 0.01 USD). Learn more about minimum and maximum amounts.

[minimum and maximum amounts](/currencies#minimum-and-maximum-charge-amounts)

- You can delete Customers that have a cash balance, but only if their cash balance is 0.

You can delete Customers that have a cash balance, but only if their cash balance is 0.

- You can’t remove a Customer’s available balance.

You can’t remove a Customer’s available balance.
