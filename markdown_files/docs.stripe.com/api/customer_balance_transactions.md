htmlCustomer Balance Transaction | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Customer Balance Transaction

Each customer has a Balance value, which denotes a debit or credit that’s automatically applied to their next invoice upon finalization. You may modify the value directly by using the update customer API, or by creating a Customer Balance Transaction, which increments or decrements the customer’s balance by the specified amount.

Related guide: Customer balance

Endpoints
# The Customer Balance Transaction object

### Attributes

- idstringUnique identifier for the object.


- amountintegerThe amount of the transaction. A negative value is a credit for the customer’s balance, and a positive value is a debit to the customer’s balance.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customerstringExpandableThe ID of the customer the transaction belongs to.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- ending_balanceintegerThe customer’s balance after the transaction was applied. A negative value decreases the amount due on the customer’s next invoice. A positive value increases the amount due on the customer’s next invoice.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- typeenumTransaction type: adjustment, applied_to_invoice, credit_note, initial, invoice_overpaid, invoice_too_large, invoice_too_small, unspent_receiver_credit, or unapplied_from_invoice. See the Customer Balance page to learn more about transaction types.

Possible enum values`adjustment`An explicitly created adjustment transaction to debit or credit the credit balance.

`applied_to_invoice`Traces the application of credit against a linked Invoice.

`credit_note`Traces the creation of credit to a Credit Note and its associated Invoice.

`initial`The starting value of the customer’s credit balance.

`invoice_overpaid`Credits to the credit balance when an invoice receives payments exceeding the amount due.

`invoice_too_large`Debits to the credit balance when the amount due on an invoice is greater than Stripe’s maximum chargeable amount and the customer does not have a cash balance.

`invoice_too_small`Debits to the credit balance when the amount due on an invoice is less than Stripe’s minimum chargeable amount and the customer does not have a cash balance.

`migration`Funds migrated from the legacy customer credit balance.

`unapplied_from_invoice`Traces the reversal of an applied credit balance from a linked Invoice. Paired with an earlier ‘applied_to_invoice’ transaction.

`unspent_receiver_credit`Unspent funds in receiver Sources that got automatically charged and credited to the balance.

[Show 1 more](#)

### More attributesExpand all

- objectstring
- createdtimestamp
- credit_notenullablestringExpandable
- invoicenullablestringExpandable
- livemodeboolean

The Customer Balance Transaction object`{  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",  "object": "customer_balance_transaction",  "amount": -500,  "created": 1680216086,  "credit_note": null,  "currency": "usd",  "customer": "cus_NcjdgdwZyI9Rj7",  "description": null,  "ending_balance": -500,  "invoice": null,  "livemode": false,  "metadata": {},  "type": "adjustment"}`# Create a customer balance transaction

Creates an immutable transaction that updates the customer’s credit balance.

### Parameters

- amountintegerRequiredThe integer amount in cents to apply to the customer’s credit balance.


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency. Specifies the invoice_credit_balance that this transaction will apply to. If the customer’s currency is not set, it will be updated to this value.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a customer balance transaction object if the call succeeded.

POST/v1/customers/:id/balance_transactionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=-500 \  -d currency=usd`Response`{  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",  "object": "customer_balance_transaction",  "amount": -500,  "created": 1680216086,  "credit_note": null,  "currency": "usd",  "customer": "cus_NcjdgdwZyI9Rj7",  "description": null,  "ending_balance": -500,  "invoice": null,  "livemode": false,  "metadata": {},  "type": "adjustment"}`# Update a customer credit balance transaction

Most credit balance transaction fields are immutable, but you may update its description and metadata.

### Parameters

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns a customer balance transaction object if the call succeeded.

POST/v1/customers/:id/balance_transactions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",  "object": "customer_balance_transaction",  "amount": -500,  "created": 1680216086,  "credit_note": null,  "currency": "usd",  "customer": "cus_NcjdgdwZyI9Rj7",  "description": null,  "ending_balance": -500,  "invoice": null,  "livemode": false,  "metadata": {    "order_id": "6735"  },  "type": "adjustment"}`# Retrieve a customer balance transaction

Retrieves a specific customer balance transaction that updated the customer’s balances.

### Parameters

No parameters.

### Returns

Returns a customer balance transaction object if a valid identifier was provided.

GET/v1/customers/:id/balance_transactions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NcjdgdwZyI9Rj7/balance_transactions/cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "cbtxn_1MrU9qLkdIwHu7ixhdjxGBgI",  "object": "customer_balance_transaction",  "amount": -500,  "created": 1680216086,  "credit_note": null,  "currency": "usd",  "customer": "cus_NcjdgdwZyI9Rj7",  "description": null,  "ending_balance": -500,  "invoice": null,  "livemode": false,  "metadata": {},  "type": "adjustment"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`