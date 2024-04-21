# Send customer emails

Stripe’s invoices are flexible and customizable. Because you know more about your customers and your business than Stripe does, make sure your invoices include all of the required information.

[invoices](/api/invoices)

[customizable](/invoicing/customize)

Set up Stripe to send important email notifications and reminders to your customers. Certain email notifications contain a link to a Stripe-hosted page that customers can use to confirm or update their payment details.

In your Email settings, you can opt out of sending your customers emails for successful payments. If you’re automatically charging a customer and you’ve turned off emails for successful payments, they won’t receive an email receipt.

[Email settings](https://dashboard.stripe.com/settings/emails)

[automatically charging](/invoicing/automatic-charging)

[email receipt](/invoicing/dashboard#invoice-receipts)

If you’re an Invoicing Plus user, you can turn on automatic reminders by going to Send reminders if a one-off invoice hasn’t been paid under Manage advanced invoicing features. When on, select whether you want Stripe to send the reminder before, when, or after the invoice is due. There’s a set of predefined options to choose from.

## Customer emails

You can configure Stripe to send email notifications or reminders to your customer:

- Upon failed payment attempts.

- After Stripe finalizes an invoice.

[finalizes](/invoicing/integration/workflow-transitions#finalized)

- With receipts after invoices are paid.

[receipts](https://dashboard.stripe.com/settings/emails)

- When a payment requires 3D Secure.

[3D Secure](/payments/3d-secure)

- When a card on file is about to expire.

- If a one-off invoice hasn’t been paid. Invoicing Plus

- When a credit note is created.

- When refund is issued.

- When a subscription trial is ending.

- Upon cancellation of subscription.

Before you start sending email notifications and reminders, you can customize your branding.

[branding](https://dashboard.stripe.com/account/branding)

Remind your customers to update their card information

You can send one-off invoice email reminders to your customers using the Dashboard or API. If you’d like to send an email reminder about an expiring card, go to Prevent failed payments.

[Prevent failed payments](https://dashboard.stripe.com/settings/billing/automatic)

To send a one-off invoice email reminder, go to the Invoices page. Click on the customer’s invoice followed by Send invoice. Before you resend an invoice, Stripe shows you a preview of the Hosted Invoice Page. To see the associated invoice PDF, download it from the Invoice details page by clicking Invoice PDF.

[Invoices page](https://dashboard.stripe.com/test/invoices)

[Hosted Invoice Page](/invoicing/hosted-invoice-page)

Hosted Invoice Page

Invoice PDF

You can send email notifications to your customers by configuring your Dashboard settings:

- To send an email notification when a card payment fails, go to Manage failed payments.

[Manage failed payments](https://dashboard.stripe.com/settings/billing/automatic)

- To email finalized invoices, navigate to Manage invoices sent to customers.

[Manage invoices sent to customers](https://dashboard.stripe.com/settings/billing/automatic)

- If you’d like to send an email notification with a receipt after a successful payment, go to your Email settings.

Learn more about how you can use customer emails to recover revenue.

[recover revenue](/billing/revenue-recovery/customer-emails)

If charging a customer’s card on file requires them to complete 3D Secure authentication and you’ve enabled Send a Stripe-hosted link for cardholders to authenticate when required in your 3D Secure settings, Stripe sends an email. The email links to a Stripe-hosted page where they can confirm the payment.

[3D Secure settings](https://dashboard.stripe.com/settings/billing/automatic)

## Additional email recipients

You can provide additional recipients to your customer’s Billing emails (including receipts sent after successful payments) using the Dashboard.

The Stripe API doesn’t currently support adding recipients to Billing emails.

- Go to the Customers page in your Dashboard.

[Customers page](https://dashboard.stripe.com/test/customers)

- Click the customer you want to add email recipients for to open the customer’s detail page.

- Click the Edit link in the Details section of the left pane to open the Update customer dialog.

- In the Billing information section of the Update customer dialog, unselect the Same as account email checkbox.

- (Optional) Set the value of the displayed field to a comma-separated list of emails that should be in the “To” line of Billing emails. If you leave this field blank, Stripe continues to use the account email.

- Click the Add more recipients link to access the Emails to CC field. Set the value of the field to a comma-separated list of email addresses that you want in the CC line of Billing (Invoice and Subscription) emails.

If you add recipients to the Customer using the previous steps, Stripe automatically pre-populates these emails to invoices you send through the Dashboard.

## Change the Stripe invoice template

You can create your own custom email template to replace the Stripe prebuilt email by configuring the invoice template. Stripe applies your custom template to all new invoices.

[configuring the invoice template](https://dashboard.stripe.com/settings/billing/invoice)

## Disable Stripe invoice emails and send your own

Stripe can use webhooks, to notify you of changes to your invoices—when they’re finalized, paid, marked uncollectible, and so on. For each event that you receive, you can construct and deliver your own emails. If you disable finalized invoice emails, Stripe continues to send webhooks as a reminder for your own email solution. To learn more, see Webhooks and invoices.

[webhooks](/webhooks)

[Webhooks and invoices](/billing/subscriptions/webhooks#understand)

## Email PDF attachments

When Stripe emails an invoice, we automatically include a PDF attachment of the same invoice to assist your customer with record keeping. If you turn on emails for successful payments—and an invoice is set to charge automatically—the receipt email includes a PDF attachment of both the original invoice and the invoice receipt. Visit the Invoice settings to disable this behavior.

[Invoice settings](https://dashboard.stripe.com/settings/billing/invoice)

## Email logs

For the customer emails sent within the last 30 days, their logs are available to view within the customer page.

[customer](https://dashboard.stripe.com/customers)

## See also

- Use the Dashboard

[Use the Dashboard](/invoicing/dashboard)

- Customize invoices

[Customize invoices](/invoicing/customize)

- Hosted Invoice Page

[Hosted Invoice Page](/invoicing/hosted-invoice-page)

- Automate customer emails

[Automate customer emails](/billing/revenue-recovery/customer-emails)
