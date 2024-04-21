# Create and send a quote

You can use quotes in test mode, but you must upgrade to Invoicing Plus or Billing Scale to unlock full functionality in live mode. See which plan is right for you.

[Invoicing Plus](https://stripe.com/invoicing/pricing)

[Billing Scale](https://stripe.com/billing/pricing)

[is right for you](https://support.stripe.com/questions/how-to-access-quotes)

A quote is a way to show prospective or existing customers the costs for a set of products and services. Quotes show the cost of either a one-off invoice or subscription. When a customer accepts the quote, ​​Stripe automatically creates all relevant invoices and subscriptions. ​​Many sales workflows use this common tool.

[invoice](/api/invoices)

[subscription](/billing/subscriptions/creating)

[Create a quote](#create-quote-dashboard)

## Create a quote

To create a quote in the Stripe Dashboard:

- Go to the Billing tab.

[Billing tab](https://dashboard.stripe.com/billing)

- Click Quick actions > Create quote (or go directly to the quote editor).

[quote editor](https://dashboard.stripe.com/test/quotes/create)

- Select + Add new customer. At a minimum, enter your customer’s Name and Account email. Click Add customer.

- Under Items, add or select a product. (You can also add a coupon.)

- Choose an expiration date.

- Optional Write a memo, and add a custom header and footer. You can set the future default text for the header and footer in the quote template.

[quote template](https://dashboard.stripe.com/settings/billing/quote)

- To preview the quote PDF (which shows the generated quote number) click Download preview.

- Click Finalize quote.

Quote editor

After you finalize the quote, send it to your customer:

- To download the quote, go to Quotes details page > Quote PDF.

- Use an external email address to send the PDF to your customer for review.

[Mark a quote as accepted](#accept-quote-dashboard)

## Mark a quote as accepted

After your customer accepts the quote, bill them by converting the quote into an invoice or subscription.

You can only create one-off invoices if a quote only has one-time prices.

If a quote has at least one recurring price, you can only convert it to a subscription.

- To mark a quote as accepted and create a draft invoice, go to Convert to invoice > Quotes details.

To mark a quote as accepted and create a draft invoice, go to Convert to invoice > Quotes details.

- Use the invoice editor to modify the draft invoice as needed.

Use the invoice editor to modify the draft invoice as needed.

[invoice editor](https://dashboard.stripe.com/test/invoices/create)

- Email the invoice or automatically charge the customer.

Email the invoice or automatically charge the customer.

- In the quote editor, choose a customer and create or select a product with a recurring price.

In the quote editor, choose a customer and create or select a product with a recurring price.

- Enter the quote details and choose to either Start the subscription immediately or Schedule a subscription start date.

Enter the quote details and choose to either Start the subscription immediately or Schedule a subscription start date.

- Finalize the quote. This marks the quote as Accepted.

Finalize the quote. This marks the quote as Accepted.

- Go to Convert to subscription > Quotes details.

Go to Convert to subscription > Quotes details.

- Enter or modify the subscription details, then click Create subscription.

Enter or modify the subscription details, then click Create subscription.

If you schedule the subscription to start immediately, Stripe creates an active subscription along with a draft invoice for the initial payment. Stripe finalizes the draft invoice automatically in one hour. Otherwise, the subscription begins on the scheduled start date. Depending on the subscription’s payment terms, Stripe collects payment by either charging the customer’s payment method on file or sending them an invoice.
