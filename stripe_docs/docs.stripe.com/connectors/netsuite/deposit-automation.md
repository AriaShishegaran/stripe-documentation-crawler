# Deposit automation

The Stripe Connector for NetSuite automates the bank reconciliation process by creating bank deposits in NetSuite for all of your Stripe payouts. The connector also automates fee calculation, the refund life cycle, the dispute life cycle, and handling of multiple currencies and subsidiaries. This means you only need to match the bank deposit record to the Stripe deposits on your bank statement. Every automated payment workflow that the connector supports includes deposit automation.

[Stripe payouts](https://support.stripe.com/topics/payouts)

## How it works

When you use the connector, the automated bank reconciliation process occurs daily as follows:

- The connector creates payments and refunds for each Stripe transaction, and posts these transactions in the Undeposited Funds account in NetSuite.

- Stripe notifies the connector that a bank transfer (Stripe payout) has successfully arrived at your bank.

- The connector creates a bank deposit record in NetSuite that contains all of the payments, refunds, and disputes from that day’s bank deposit.

- The connector calculates any fees for processing, currency conversion, disputes, and refunds, and includes these as separate line items that post to your specified expense accounts.

- The connector makes sure that the deposit total and deposit date match your bank statement.

## See also

- Invoice automation

[Invoice automation](/connectors/netsuite/invoice-automation)

- Invoice payment page

[Invoice payment page](/connectors/netsuite/invoice-payment-page)

- Customer payment page

[Customer payment page](/connectors/netsuite/customer-payment-page)
