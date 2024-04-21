# No-code quickstart guide

Stripe Invoicing can help you get paid and save time using the Dashboard. Automatically charge your customer’s payment method on file, or email them the invoice with or without a link to a payment page. You can also send the invoice or payment page link manually.

[invoice](/api/invoices)

If you’re interested in managing subscriptions and recurring revenue, see Subscriptions.

[Subscriptions](/billing)

Hosted Invoice Page

Invoice PDF

[Set up your business brandOptional](#establish-business)

## Set up your business brandOptional

Before you start using Stripe Invoicing, help your future customers understand your products and terms of service by establishing your business and customizing how your brand appears.

[establishing your business](https://dashboard.stripe.com/settings/account?support_details)

[customizing how your brand appears](https://dashboard.stripe.com/settings/branding)

Brand your business

[Choose your payment methodsOptional](#payment-methods)

## Choose your payment methodsOptional

By default, customers can pay invoices with any of the payment methods that you enable in your Invoice template. If you’re a first-time user, Stripe automatically enables card, Link, bank transfers, Cash App Pay, and WeChat Pay payment methods. To enable additional payment methods, you need to activate them in your Payment methods settings.

[Invoice template](https://dashboard.stripe.com/settings/billing/invoice)

[Link](/payments/link)

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

In some situations, there might be restrictions that prevent payment methods from being used for an invoice. For instance, a payment method might only operate in one currency, or have limitations on the amount that can be paid. Stripe doesn’t automatically select a payment method when these limitations prevent it from being used. To learn more, see Payment methods.

[Payment methods](/invoicing/payment-methods#supported)

Choose additional payment methods

[How to get paid](#get-paid)

## How to get paid

You can create and send an invoice from the Dashboard. Invoices provide an itemized list of goods and services rendered, which includes the cost, quantity, and taxes. You can also use them as a tool to collect payment. Learn more about using the Dashboard.

[create and send](https://dashboard.stripe.com/invoices/create)

[using the Dashboard](/invoicing/dashboard)

Create and send an invoice

[Set up a custom templateOptional](#custom-templates)

## Set up a custom templateOptional

You can use the Invoice template to customize ​​the content of your invoices. Set a default memo, footer, numbering scheme, and determine your default payment terms. Because you know more about your customers and your business than Stripe does, make sure your invoices include all of the required information. See the full invoice customization guide at Customize invoices.

[Invoice template](https://dashboard.stripe.com/account/billing/invoice)

[Customize invoices](/invoicing/customize)

Configure the Invoice template

Manage tax information

[Track an invoice](#track-invoice)

## Track an invoice

Invoices move through different statuses from the time they’re created to when they’re paid. You can track the status of an invoice on the Invoices page. To let your customer know that the due date for an invoice is approaching, send them an email reminder. For more information on tracking your invoices, see Manage invoices.

[Invoices page](https://dashboard.stripe.com/test/invoices)

[send them an email reminder](/invoicing/send-email)

[Manage invoices](/invoicing/dashboard/manage-invoices)

Track and manage your invoices

[Explore advanced features with Invoicing PlusOptional](#invoicing-plus)

## Explore advanced features with Invoicing PlusOptional

Invoicing Plus includes advanced features to automate how you collect and reconcile invoice payments.

Are you interested in automatic collection and reconciliation features? Upgrade to Invoicing Plus.

[Invoicing Plus](https://stripe.com/invoicing/pricing)

You can automate Stripe Invoicing and get paid faster by choosing to automatically charge your customer’s payment method on file. If you’re a Plus user, let Stripe handle invoice recovery issues.

[automatically charge](/invoicing/automatic-charging)

[invoice recovery](/invoicing/automatic-collection)

Automate invoicing

Using automatic reconciliation means that you don’t need to expose your sensitive bank account details to users or manually reconcile open invoices with your bank. With auto-reconciliation for invoices, Stripe can:

[automatic reconciliation](/invoicing/automatic-reconciliation)

- Match incoming payments with invoice amounts.

- Manage overpayment or underpayment, when the amount paid doesn’t match the invoice.

- Reduce the number of API calls required to transfer funds into Stripe.

- Manage payment retries on open invoices.

Close your books

[Let customers manage their invoicesOptional](#customer-portal)

## Let customers manage their invoicesOptional

Share a link to your customer portal, where customers can log in with their email to manage invoices, view invoice history, update payment information, and so on. Learn how to create and share your customer portal link.

[customer portal](/billing/subscriptions/customer-portal)

[customer portal link](/customer-management/activate-no-code-customer-portal)
