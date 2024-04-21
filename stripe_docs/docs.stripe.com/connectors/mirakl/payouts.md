# Payouts

The amount and frequency of each payout to your sellers is controlled by Mirakl based on your settings.

[payout](/payouts)

You can customize your billing cycles under Settings > Shops > Billing Cycles. By default, your sellers receive their payouts on the 1st, 11th, and 21st of each month.

## Seller settlement

The workflow starts when Mirakl generates a new invoice.

[invoice](/api/invoices)

- The payout job fetches newly created Mirakl invoices.

[payout job](/connectors/mirakl/reference#payout)

- The connector performs the following actions based on the invoice attributes:

Commissions are already handled during the payment split workflow.

[payment split workflow](/connectors/mirakl/payments#payment-split)

## See also

- Integration steps.

[Integration steps](/connectors/mirakl#integration-steps)
