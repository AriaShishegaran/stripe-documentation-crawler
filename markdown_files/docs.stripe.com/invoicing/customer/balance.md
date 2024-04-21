htmlCustomer credit balance | Stripe Documentation[Skip to content](#main-content)Customer credit balance[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fcustomer%2Fbalance)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fcustomer%2Fbalance)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Customers](/docs/invoicing/customer)# Customer credit balance

Learn how to work with customer credit balances.Customer balance typesThis page is about customer credit balances, which are adjustments you can issue to customers that apply to future invoices. Credit balances are different from cash balances. Cash balances are connected to the customer balance payment method. To learn more, see Bank transfer. As explained below, some features work differently for customers with a cash balance.

Every customer has a credit balance. You can use this to issue a:

- Credit adjustment—You owe the customer money.
- Debit adjustment—The customer owes you money.

These adjustments sum up to a credit balance that you can apply to future invoices. Because Stripe computes the credit balance from a ledger—an immutable list of debit and credit transactions—it provides an audit trail of transactions for the customer. The Customer Balance Transactions can refer to the object related to the adjustment, such as a credit note, invoice, or metadata.

Some common use cases for customer credit balances include:

- [Issuing a credit note](/invoicing/dashboard/credit-notes#issuing)to create a credit that reduces the amount due on the next invoice.
- Marking an invoice as paid and moving the amount owed to the credit balance as a debit. This happens when the amount due on an invoice is less than the[minimum chargeable amount](/currencies#minimum-and-maximum-charge-amounts). This functionality only occurs for users without a[cash balance](#cash-balances).

## Credit balances

Keep the following in mind when you work with credit balances:

- The credit balance automatically applies to the next finalized invoice to a customer.
- You ​​can’t choose a specific invoice to apply the credit balance to.
- The credit balance is in the customer’s currency.
- [Customers](/api/customers)with a[cash balance](/api/customers/object#customer_object-cash_balance)can’t keep a positive balance. In other words, they can’t increase the amount due on the next invoice.

## Credits and debits

Credits are negative values (a reduction in the amount the customer owes) that you can apply to the next invoice. Debits, on the other hand, are positive values (an increase in the amount the customer owes) that you can apply to the next invoice.

## Transactions

All modifications to the credit balance are recorded as Transactions. After you create a transaction, you can only update its description or metadata (you can’t edit other properties or delete it).

### Transaction types

All Transactions that you create with the API or in the Dashboard have a type value of adjustment.  A type value of adjustment represents a debit or credit that you manually created for the customer. The following table describes each of the type values:

TypeDescription`adjustment`An explicitly created adjustment transaction to debit or credit the credit balance. This is the only type of transaction that you can create by using API integrations and the Dashboard.`applied_to_invoice`Traces the application of credit against a linked invoice.`credit_note`Traces the creation of credit to a[credit note](/invoicing/dashboard/credit-notes)and ​​its associated invoice.`invoice_too_small`When the amount due on an invoice is less than Stripe’s[minimum chargeable amount](/currencies#minimum-and-maximum-charge-amounts)and the customer does not have a cash balance, the invoice is debited from the credit balance and added to the amount due on the next invoice.`invoice_too_large`When the amount due on an invoice is greater than Stripe’s[maximum chargeable amount](/currencies#minimum-and-maximum-charge-amounts)and the customer does not have a cash balance, the invoice is debited from the credit balance and added to the amount due on the next invoice.`unapplied_from_invoice`Traces the reversal of an applied credit balance from a linked invoice. Paired with an earlier ‘applied_to_invoice’ transaction.`unspent_receiver_credit`When unspent funds in[receiver Sources](/sources#flow-for-customer-action)attached to a customer without cash balance aren’t fully charged after 60 days, Stripe automatically charges them on your behalf and credits your balance. When this happens, Stripe also creates a corresponding credit transaction.`initial`Represents the starting value of the credit balance when a customer is created by using the API with a non-zero credit balance.### Undo a transaction

You can only undo a transaction by creating a corresponding, reversing transaction. For example, if you credit the customer ​​10 USD, you’d have to debit them 10 USD in a new transaction, each canceling the other one out.

## Modify the credit balance

You can modify a customer’s credit balance through both the Dashboard and API.

DashboardAPIYou can modify a customer’s credit balance through the Customers page in the Dashboard by creating a new Customer Balance Transaction adjustment.

In the Customers page, click on the customer and then click Adjust balance under Credit balance. From here, set the Adjustment type, a Currency (only available if the customer doesn’t have a currency set), an Amount, and an internal note.

NoteThe internal note is only visible to Dashboard users.

![](https://b.stripecdn.com/docs-statics-srv/assets/2-Customer-balance.ed7d6df96ba2b8595461e1091e4da7a9.png)

Add a new customer balance transaction adjustment

## Balance transaction history

DashboardAPIAudit a customer’s balance adjustments in the Customers page by scrolling down to the Credit balance section. This section displays the current value of the customer credit balance.

Customer cash balances Customers using the bank transfers payment method have a cash balance object with one or more currencies in the available object. You can use the funds to make payments or pay invoices. Customers with available balances have the following behavior:You can’t create a negative customer cash balance since it represents money sent from the Customer.You can’t finalize a too-small or too-large invoice with the cash balance (for example, creating a subscription for 0.01 USD). Learn more about minimum and maximum amounts.You can delete Customers that have a cash balance, but only if their cash balance is 0.You can’t remove a Customer’s available balance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Credit balances](#working-with-credit-balances)[Credits and debits](#credits-and-debits)[Transactions](#transactions)[Modify the credit balance](#modifying)[Balance transaction history](#auditing)[Customer cash balances](#customer-cash-balances)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`