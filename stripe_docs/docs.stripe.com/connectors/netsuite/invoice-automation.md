# Stripe invoice automation

The Stripe Connector for NetSuite automatically syncs the invoices that you create from Stripe Billing subscriptions or Stripe Invoicing into NetSuite. The sync includes details such as credit notes, discounts, uncollectible invoices, taxes, and prorations.

[subscriptions](/billing/subscriptions/overview)

[Stripe Invoicing](/invoicing/overview)

[credit notes](/invoicing/dashboard/credit-notes)

[discounts](/billing/subscriptions/coupons)

[uncollectible invoices](/revenue-recognition/examples#uncollectible)

[taxes](/billing/taxes/collect-taxes)

[prorations](/billing/subscriptions/prorations)

You can complete your accounting workflows entirely in Stripe using the automated process, which means you don’t need to manually reconcile activity. Stripe transaction data syncs at the transaction level in NetSuite, allowing you to use advanced reporting on Stripe data in NetSuite.

When you use the connector with Stripe Billing, the invoice automation process is as follows:

[Stripe Billing](/billing)

- A customer provides their payment information through a Stripe payment flow on your website. This action creates a Stripe Customer object.

- Stripe creates an invoice at the beginning of each billing period, which prompts the connector to create an invoice in NetSuite. The connector also creates a new customer or links to an existing NetSuite customer.

- If you enabled NetSuite revenue recognition, the connector splits revenue over the correct period on the line item level.

- When a customer successfully pays the Stripe invoice, the connector creates a NetSuite Customer Payment and applies it to the corresponding invoice in NetSuite. If payment fails, resulting in a canceled subscription, the connector can automatically close the NetSuite invoice with a credit memo, or whatever action you configure for failed payments.

- The connector automatically syncs refunds and disputes from Stripe to NetSuite, and creates credit memos and customer refunds.

- The connector automatically reconciles Stripe payments against a bank deposit in NetSuite. This includes calculating and recording any processing fees or currency conversion fees.

[automatically reconciles](/connectors/netsuite/deposit-automation)

## See also

- Invoice payment page

[Invoice payment page](/connectors/netsuite/invoice-payment-page)

- Deposit automation

[Deposit automation](/connectors/netsuite/deposit-automation)
