- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Customer Balance Transaction

[Customer Balance Transaction](/api/customer_balance_transactions)

Each customer has a Balance value, which denotes a debit or credit that’s automatically applied to their next invoice upon finalization. You may modify the value directly by using the update customer API, or by creating a Customer Balance Transaction, which increments or decrements the customer’s balance by the specified amount.

[Balance](/api/customers/object#customer_object-balance)

[update customer API](/api/customers/update)

Related guide: Customer balance

[Customer balance](/billing/customer/balance)

[POST/v1/customers/:id/balance_transactions](/api/customer_balance_transactions/create)

[POST/v1/customers/:id/balance_transactions/:id](/api/customer_balance_transactions/update)

[GET/v1/customers/:id/balance_transactions/:id](/api/customer_balance_transactions/retrieve)

[GET/v1/customers/:id/balance_transactions](/api/customer_balance_transactions/list)

# The Customer Balance Transaction object

[The Customer Balance Transaction object](/api/customer_balance_transactions/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerThe amount of the transaction. A negative value is a credit for the customer’s balance, and a positive value is a debit to the customer’s balance.

The amount of the transaction. A negative value is a credit for the customer’s balance, and a positive value is a debit to the customer’s balance.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customerstringExpandableThe ID of the customer the transaction belongs to.

The ID of the customer the transaction belongs to.

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- ending_balanceintegerThe customer’s balance after the transaction was applied. A negative value decreases the amount due on the customer’s next invoice. A positive value increases the amount due on the customer’s next invoice.

The customer’s balance after the transaction was applied. A negative value decreases the amount due on the customer’s next invoice. A positive value increases the amount due on the customer’s next invoice.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- typeenumTransaction type: adjustment, applied_to_invoice, credit_note, initial, invoice_overpaid, invoice_too_large, invoice_too_small, unspent_receiver_credit, or unapplied_from_invoice. See the Customer Balance page to learn more about transaction types.Possible enum valuesadjustmentAn explicitly created adjustment transaction to debit or credit the credit balance.applied_to_invoiceTraces the application of credit against a linked Invoice.credit_noteTraces the creation of credit to a Credit Note and its associated Invoice.initialThe starting value of the customer’s credit balance.invoice_overpaidCredits to the credit balance when an invoice receives payments exceeding the amount due.invoice_too_largeDebits to the credit balance when the amount due on an invoice is greater than Stripe’s maximum chargeable amount and the customer does not have a cash balance.invoice_too_smallDebits to the credit balance when the amount due on an invoice is less than Stripe’s minimum chargeable amount and the customer does not have a cash balance.migrationFunds migrated from the legacy customer credit balance.unapplied_from_invoiceTraces the reversal of an applied credit balance from a linked Invoice. Paired with an earlier ‘applied_to_invoice’ transaction.unspent_receiver_creditUnspent funds in receiver Sources that got automatically charged and credited to the balance.Show 1 more

Transaction type: adjustment, applied_to_invoice, credit_note, initial, invoice_overpaid, invoice_too_large, invoice_too_small, unspent_receiver_credit, or unapplied_from_invoice. See the Customer Balance page to learn more about transaction types.

[Customer Balance page](/billing/customer/balance#types)

An explicitly created adjustment transaction to debit or credit the credit balance.

Traces the application of credit against a linked Invoice.

Traces the creation of credit to a Credit Note and its associated Invoice.

The starting value of the customer’s credit balance.

Credits to the credit balance when an invoice receives payments exceeding the amount due.

Debits to the credit balance when the amount due on an invoice is greater than Stripe’s maximum chargeable amount and the customer does not have a cash balance.

Debits to the credit balance when the amount due on an invoice is less than Stripe’s minimum chargeable amount and the customer does not have a cash balance.

Funds migrated from the legacy customer credit balance.

Traces the reversal of an applied credit balance from a linked Invoice. Paired with an earlier ‘applied_to_invoice’ transaction.

Unspent funds in receiver Sources that got automatically charged and credited to the balance.

- objectstring

- createdtimestamp

- credit_notenullable stringExpandable

- invoicenullable stringExpandable

- livemodeboolean

# Create a customer balance transaction

[Create a customer balance transaction](/api/customer_balance_transactions/create)

Creates an immutable transaction that updates the customer’s credit balance.

[balance](/billing/customer/balance)

- amountintegerRequiredThe integer amount in cents to apply to the customer’s credit balance.

The integer amount in cents to apply to the customer’s credit balance.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency. Specifies the invoice_credit_balance that this transaction will apply to. If the customer’s currency is not set, it will be updated to this value.

Three-letter ISO currency code, in lowercase. Must be a supported currency. Specifies the invoice_credit_balance that this transaction will apply to. If the customer’s currency is not set, it will be updated to this value.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

[invoice_credit_balance](/api/customers/object#customer_object-invoice_credit_balance)

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a customer balance transaction object if the call succeeded.

# Update a customer credit balance transaction

[Update a customer credit balance transaction](/api/customer_balance_transactions/update)

Most credit balance transaction fields are immutable, but you may update its description and metadata.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a customer balance transaction object if the call succeeded.

# Retrieve a customer balance transaction

[Retrieve a customer balance transaction](/api/customer_balance_transactions/retrieve)

Retrieves a specific customer balance transaction that updated the customer’s balances.

[balances](/billing/customer/balance)

No parameters.

Returns a customer balance transaction object if a valid identifier was provided.
