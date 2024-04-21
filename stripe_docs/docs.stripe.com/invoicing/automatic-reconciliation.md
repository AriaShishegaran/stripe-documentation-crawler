# Automatic reconciliation

This page covers the Sources-based implementation of credit transfers. We deprecated the Sources API and plan to remove support for local payment methods. If you currently integrate with Credit Transfers, you must migrate to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate to the Payment Methods API](/payments/payment-methods/transitioning)

To start using Invoicing features, log in to the Dashboard and select a Billing plan.

[Billing plan](https://dashboard.stripe.com/settings/billing/plans?utm_source=docs-reconciliation)

​​Businesses often use credit transfer payments for large deals or new business relationships. Credit transfer payments can generate a lot of manual work for your team. Stripe facilitates this process by accepting transfers that pay open invoices.

For each of your customers, Stripe auto-generates a US virtual bank account number that can be paid in USD with ACH credit or wires. When your customer sees an invoice with this virtual bank account, they can send payment to it. ​​Stripe automatically reconciles the payment with the virtual bank account and the invoice. Stripe then marks the invoice as paid.

Using automatic reconciliation means that you don’t need to expose your sensitive bank account details to users or manually reconcile open invoices with your bank. With auto-reconciliation for invoices, Stripe can:

- Match incoming payments with invoice amounts.

- Manage overpayment or underpayment, when the amount paid doesn’t match the invoice.

- Reduce the number of API calls required to transfer funds into Stripe.

- Manage payment retries on open invoices.

## Pay an invoice

If a customer doesn’t have an ach_credit_transfer subhash, Stripe creates one for every invoice. All invoices include instructions on where to send payment. Also, each customer has a unique payment address that’s shared across their invoices. With the ach_credit_transfer subhash, customers can transfer funds through either the US ACH system or domestic wire, and include an invoice number in the memo field.

[ach_credit_transfer](/api/charges/object#charge_object-payment_method_details-ach_credit_transfer)

​​ACH credit transfers only support USD.

As soon as a customer makes a transfer, Stripe matches the payment to an invoice by checking for an invoice number in the memo field of the transfer. We fulfill any invoices that we find a match for. If we can’t find a match, we fulfill the oldest outstanding invoice of the same amount. If we can’t find any outstanding invoice that has the same amount, then we’ll fulfill as many outstanding invoices that can be fulfilled with the transfer amount, starting with the oldest payable invoice. When an invoice is fulfilled, an invoice.paid event occurs (you can receive this event by using webhooks).

[webhooks](/invoicing/integration/workflow-transitions)

You can inspect the status of any ACH credit transfer by viewing the list of payment methods for the customer in the Dashboard. You can also see the status by viewing a customer’s sources in the API:

[Dashboard](https://dashboard.stripe.com/customers)

Stripe returns a list of sources attached to that customer. The source type for an ACH credit transfer has a value of ach_credit_transfer. In the following response example, the ACH credit transfer receiver is awaiting payment from the customer:

Occasionally, customers might want to use payment methods outside of Stripe, such as paper checks. In these situations, Stripe allows you to keep track of your invoice’s payment status. After you receive an invoice payment from a customer outside of Stripe, you can manually mark their invoice as paid:

## Handle exceptions

If your customer pays an amount that doesn’t match an invoice amount, the funds aren’t charged and remain in the Source​ object. If you want to use these funds to fulfill your invoice, you have a few options:

- Overpayment—If a user sends more funds than the invoice requests, Stripe automatically marks the invoice as paid, using the funds that match the open invoice. The remaining funds stay in the Source receiver. You can manually apply these funds to an invoice. If you have multiple matching open invoices, Stripe applies the funds to the oldest invoice.

- Underpayment—In your Subscription and emails settings, you can specify rules around underpayment in the Partial payments section. You can specify that within a certain margin of error, Stripe auto-reconciles invoices and credits the difference.

[Subscription and emails settings](https://dashboard.stripe.com/settings/billing/automatic)

A typical scenario for underpayment might be that a customer’s bank takes funds from the total amount sent. For example, ​​if the customer sends 100 USD to pay their 100 USD invoice, the customer’s bank might take 20 USD, which leaves you with 80 USD. If this difference (which is usually within 20 USD) is acceptable, you can ​​minimize manual effort by specifying this margin ahead of time.

For any other exceptions:

- ​If the receiver has enough money to pay your invoice, you can claim those funds in the Dashboard by clicking the Charge customer button on the invoice, or by calling the Pay invoice endpoint and specifying the ACH credit transfer object as the source.

[Pay invoice](/api#pay_invoice)

- ​​If the funds to pay the invoice are insufficient and you don’t forgive the difference, you can ask your customer to send the remaining amount. You can also void the old invoice, open a new one for the lesser amount, and immediately click Charge customer on it.

If your customer has an ACH credit transfer source with sufficient funds, or a credit card or bank account on file, you can use those sources to pay the invoice by calling the Pay invoice endpoint with the source you want to use.

[Pay invoice](/api#pay_invoice)

## Refund payments

You can refund ACH credit transfer and check payments through either the Dashboard or the API. However, the customer must specify the account to return the funds to. Stripe automatically contacts the customer at the email address provided. As soon as the customer provides us with their account information, we process the refund automatically.

[Dashboard](https://dashboard.stripe.com/payments)

[API](/api#create_refund)

The initial status of the refund is pending. If the refund fails, ​​you’ll receive the charge.refund.updated​ event, and the status of the refund transitions to failed. This means that ​​we couldn’t process the refund, and you must return the funds to your customer outside of Stripe. This is a rare occurrence, which can happen if the refund is sent to an account that has been frozen. Refunds that have been completed have a succeeded status.

## Test payment

If ​​you’re in test mode, you can simulate transferring money into the receiver by updating the owner email on the source to amount_XXXX@any_domain.com, where XXXX is the amount of money you want to simulate transferring. ​​The payment won’t be associated with the invoice unless Stripe has frozen the invoice from editing. This happens either one hour after webhooks have been delivered, or when you’ve sent the customer an email for the invoice. In the Dashboard, you can immediately send an email by clicking the invoice’s Send invoice button.

[webhooks](/webhooks)

A few moments after the update request, you can retrieve the receiver parameter:

If the update request succeeded, the receiver attribute shows the funds:

In this instance, the customer’s open invoice (of the same amount) transitions to paid. It has a corresponding payment object that displays the details of the payment.
