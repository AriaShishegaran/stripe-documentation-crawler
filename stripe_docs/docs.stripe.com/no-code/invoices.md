# Use invoices

- Compatible with: Customer portal, Hosted Invoice Page

- Requires: Stripe account

- Good for: Professional services, e-commerce businesses, B2B businesses

- Pricing: Pay-as-you-go, Stripe Billing pricing for recurring payments

[Pay-as-you-go](https://stripe.com/pricing)

[Stripe Billing pricing](https://stripe.com/billing/pricing)

Automatically charge your customer’s payment method on file, or email them the invoice with or without a link to a payment page. You can also send the invoice or payment page link manually.

[invoice](/api/invoices)

To learn about managing subscriptions and recurring revenue, see the Subscriptions docs.

[Subscriptions](/billing)

Hosted Invoice Page

Invoice PDF

[Set up your business brandOptional](#establish-business)

## Set up your business brandOptional

Before you start using Stripe Invoicing, help your future customers understand your products and terms of service by adding your business details and customizing how your brand appears.

[adding your business details](https://dashboard.stripe.com/settings/account?support_details)

[customizing how your brand appears](https://dashboard.stripe.com/settings/branding)

Customers see these business and branding details on the Hosted Invoice Page when they pay an invoice online. To let customers manage past invoices and their own billing information, set up the customer portal.

[Hosted Invoice Page](/invoicing/hosted-invoice-page)

[customer portal](/no-code/customer-portal)

Brand your business

[Choose your payment methodsOptional](#payment-methods)

## Choose your payment methodsOptional

By default, customers can pay invoices with any of the payment methods that you enable in your invoice template. If you’re a first-time user, Stripe automatically enables card, Link, bank transfers, Cash App Pay, and WeChat Pay payment methods. To enable additional payment methods, you need to activate them in your Payment methods settings.

[invoice template](https://dashboard.stripe.com/settings/billing/invoice)

[Link](/payments/link)

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

In some situations, restrictions might prevent payment methods from being used for an invoice. For instance, a payment method might only operate in one currency, or have limitations on the amount that can be paid. Stripe doesn’t automatically select a payment method when these limitations prevent it from being used. To learn more, read about supported payment methods.

[supported payment methods](/invoicing/payment-methods#supported)

Choose additional payment methods

[How to get paid](#get-paid)

## How to get paid

You can create and send an invoice from the Dashboard. Invoices provide an itemized list of goods and services rendered, which includes the cost, quantity, and taxes. You can also use them as a tool to collect payment. Learn more.

[create and send](https://dashboard.stripe.com/invoices/create)

[Learn more](/invoicing/dashboard)

Create and send an invoice

[Set up a custom templateOptional](#custom-templates)

## Set up a custom templateOptional

You can use the invoice template to customize ​​the content of your invoices. Set a default memo, footer, and numbering scheme. Determine your default payment terms. Because you know more about your customers and your business than Stripe does, make sure your invoices include all of the required information. See the full invoice customization guide at Customize invoices.

[invoice template](https://dashboard.stripe.com/account/billing/invoice)

[Customize invoices](/invoicing/customize)

Configure the Invoice template

Manage tax information

[Track an invoice](#track-invoice)

## Track an invoice

Invoices move through different statuses from the time they’re created to when they’re paid. Track the status of an invoice on the invoices page in the Dashboard. To let your customer know that the due date for an invoice is approaching, send them an email reminder. Learn more in our invoice management docs.

[invoices page](https://dashboard.stripe.com/test/invoices)

[send them an email reminder](/invoicing/send-email)

[invoice management docs](/invoicing/dashboard/manage-invoices)

Track and manage your invoices

[Automate Invoice Reconciliation and Collection](#invoicing-plus)

## Automate Invoice Reconciliation and Collection

To automate Stripe Invoicing and get paid faster, choose to automatically charge your customer’s payment method on file. You can also let Stripe handle invoice recovery issues.

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
