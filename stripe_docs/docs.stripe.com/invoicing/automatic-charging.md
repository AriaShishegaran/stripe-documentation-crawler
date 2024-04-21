# Automatic charging

Stripe can automatically attempt to pay an invoice if the customer has a payment method on file. You can automatically charge a customer when you’re creating an invoice or through the API. When you automatically charge a payment method on file, Stripe doesn’t notify the customer about the invoice. However, if you want to send an email receipt, make sure that you enable the Successful payments option in your Email settings and that you’ve added your customer’s email address.

[invoice](/api/invoices)

[creating an invoice](https://dashboard.stripe.com/invoices/create)

[API](/api/invoices)

[Email settings](https://dashboard.stripe.com/settings/emails)

## Add a payment method

To add a payment method, go to the Customers page and select a customer. Select Add in the Payment methods section to add a card or an ACH debit bank account. You can also add a payment method during invoice creation. If your customer uses multiple payment methods, click the overflow menu () next to the card to make it the default.

[Customers page](https://dashboard.stripe.com/customers)

## See also

- Use the Dashboard

[Use the Dashboard](/invoicing/dashboard)

- Send email reminders

[Send email reminders](/invoicing/send-email)
