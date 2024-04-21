# Customer balance

Your customers might have associated balances that contain two types of funds—cash and credit.

## Cash balances

A customer’s cash balance represents funds that they can use for payment. When they overpay or send an amount using a bank transfer that isn’t automatically reconciled with any outstanding payment, we add these funds to the customer cash balance. You can use these funds for later payments for the same customer, or initiate a refund from their cash balance to return the funds to their bank account, limited to the amount available in the customer balance.

[initiate a refund](/payments/customer-balance/refunding#create-return-dashboard)

You can’t add funds to the customer cash balance directly. This isn’t a balance that customers can top up and is only there as a reconciliation layer—it’s not a digital wallet or e-money. You can’t use the cash balance for any other purpose besides future payments, or returns to the customer it’s associated with.

## Credit balances

In contrast to a cash balance, a credit balance is an Invoices feature that represents liability between you and the customer. You can’t use credit balance funds for payment, but you can apply them to offset future invoices. You can update the customer credit balance by creating an adjustment Customer Balance Transaction. For more information on credit balances, refer to Customer Credit Balance.

[Invoices](/api/invoices)

[Customer Balance Transaction](/api/customer_balance_transactions/object)

[Customer Credit Balance](/invoicing/customer/balance)

## View the customer balance

You can find a customer’s balance with both the API and through the Stripe Dashboard. To view a customer’s balance using the API, first retrieve the customer and then expand the cash_balance field.

To view a customer’s balance in the Dashboard, navigate to the Customer page. The customer’s balance appears in the Payment methods section.

## Make a payment from the cash balance

When your customer has a cash balance, you can use the funds immediately to make a payment up to the available amount. To do this, create a PaymentIntent using the customer_balance payment method type.

When your customer has a cash balance, you can use the funds immediately to make a payment up to the available amount. You can do this by using either the API or the Dashboard.

To make a payment using the API, create a PaymentIntent using the customer_balance payment method type.

The payment succeeds if the cash balance has sufficient funds, and fails otherwise.

To collect more funds from the customer when the cash balance is insufficient, use the customer balance with a bank transfer funding.

[bank transfer funding](/payments/bank-transfers/accept-a-payment)

## List changes to the customer balance

Changes to the customer’s cash balance are modeled as a list of cash balance transactions. You can retrieve these transactions for a customer to see how their cash balance has changed over time.

[cash balance transactions](/api/cash_balance_transactions/object)

## Cash balance transaction types

Cash balance transactions have a type value indicating the type of action that caused the cash balance to change.

[type](/api/cash_balance_transactions/object#customer_cash_balance_transaction_object-type)

[reconciliation](/payments/customer-balance/reconciliation)

[reconciliation](/payments/customer-balance/reconciliation#cash-automatic-reconciliation)

[manual reconciliation](/payments/customer-balance/reconciliation#cash-manual-reconciliation)

[partially funded](/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#handling-underpayments-and-overpayments)

[modified](/api/payment_intents/update)

[canceled](/api/payment_intents/cancel)

[refunded to the customer cash balance](/payments/customer-balance/refunding#refund-customer-balance-payment-customer-balance)

[canceled the refund before the customer submitted their bank details](/payments/customer-balance/refunding#create-return-dashboard-cancel)

[Refund bank transfer payments](/payments/customer-balance/refunding#refund-customer-balance-payment-bank-account)

[OptionalAccess to full sender IBAN for `funded` cash balance transactions](#access-full-sender-iban)

## OptionalAccess to full sender IBAN for `funded` cash balance transactions
