# Payments using the Mirakl connector

We categorize payment methods into seven families. Each family has similar features, a single integration, and common checkout experiences.

[payment methods](/payments/payment-methods/overview)

You can use one of our existing connectors or build your own integration to accept payments.

[existing connectors](/connectors)

[build your own integration](/payments)

When implementing payments, don’t use any of the Connect charge types. The connector takes care of splitting the funds based on your Mirakl orders.

[Connect](/connect)

[splitting the funds](#payment-split)

## Payment creation

Choose the payment method families according to the order workflow most adapted to your use case.

[Cards](/payments/accept-a-payment)

[Bank debits](/payments/bank-debits)

[Bank redirects](/payments/bank-redirects)

[Credit transfers](/payments/sources/credit-transfers)

[Buy now, pay later](/payments/buy-now-pay-later)

[Vouchers](/payments/vouchers)

[Wallets](/payments/wallets)

Below are some additional guidelines for adapting your payment integration to your workflows.

For cards, set the value of capture_method option to manual when completing the PaymentIntent to authorize only. The connector captures the funds automatically as soon as all sellers have accepted or refused their respective orders. The orders must be accepted or refused within 7 days, the validity period of an authorization.

[capture_method](/api/payment_intents/create#create_payment_intent-capture_method)

[captures the funds automatically](#payment-validation)

Because the payment confirmation is immediate for bank redirects, wallets and buy now, pay later, we recommend setting up your orders to be accepted automatically and using refunds when sellers can’t fulfill their order.

For cards, you can authorize only during checkout if you have business rules in place to capture the payment within 7 days. Otherwise, save the card at checkout and authorize later.

[save the card](/payments/save-and-reuse)

For bank debits, you can save the bank account at checkout and initiate the payment after the seller accepts their order.

You can use Stripe Billing to send an invoice to your customers who can then pay using our hosted invoice page.

[send an invoice](/invoicing/dashboard)

[hosted invoice page](/invoicing/hosted-invoice-page)

## Payment validation

To handle the payment validation of your Mirakl orders, you can rely on the built-in job or call the PA01 API yourself if you have specific needs such as offering coupons.

[PA01](https://help.mirakl.net/help/api-doc/operator/mmp.html#PA01)

To enable the built-in job, you have to first map the Mirakl order with the successful Charge by updating the metadata:

The workflow starts when a seller accepts their logistic order.

- The payment validation job fetches newly accepted Mirakl orders.

[payment validation job](/connectors/mirakl/reference#payment-validation)

- The connector validates the payment in Mirakl.

- For cards, the payment is captured when all the logistic orders are accepted or refused.

## Payment split

The workflow starts when the payment is validated on Mirakl and captured on Stripe.

- The payment split job fetches newly validated Mirakl orders.

[payment split job](/connectors/mirakl/reference#payment-split)

- The connector transfers the order amount to the seller after deducting your commission.

## Payment refund

The workflow starts when you request a refund on a Mirakl order.

- The payment refund job fetches newly refunded Mirakl orders.

[payment refund job](/connectors/mirakl/reference#payment-refund)

- The connector creates a refund on Stripe, validates the refund on Mirakl, and then reverses the transfer used to split the payment.

## See also

- Integration steps.

[Integration steps](/connectors/mirakl#integration-steps)
