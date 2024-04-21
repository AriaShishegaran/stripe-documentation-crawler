# Email receipts and paid invoices

With Payment Links, you can manually or automatically send customized email receipts or paid invoices.

[Payment Links](/payment-links)

[paid invoices](#paid-invoices)

## Receipt features

Test payments created using your test API keys don’t automatically send receipts. Instead, you can view or manually send a receipt using the Dashboard.

[test API keys](/keys#test-live-modes)

[Dashboard](https://dashboard.stripe.com/test/payments)

Each receipt contains a link to view it in a browser, and a unique receipt number that’s useful when looking up payment information.

[receipt number](/api#charge_object-receipt_number)

You can also access the link to view the receipt in a browser through the API in the PaymentIntent’s related Charge object. When you visit the link, the receipt always shows the latest status of that charge–if it has been refunded, the receipt accurately reflects it.

[PaymentIntent’s](/payments/payment-intents)

[Charge](/api/charges/object#charge_object-receipt_url)

As a security measure, receipt links expire within 30 days. Expired receipt links require the customer to provide the original email address to resend the receipt to that address.

## Automatically send receipts

To enable automated receipts, toggle Successful payments on in your Customer emails settings. Receipts are only sent when a successful payment has been made—no receipt is sent if the payment fails or is declined.

[Customer emails settings](https://dashboard.stripe.com/settings/emails)

## Manually send receipts

To send receipts in the Dashboard, click Send receipt within the Receipt history section of a Payment details page. You can also hover over a payment within the Payments section of a customer’s page and click the Send receipt icon. To resend an email receipt, input a different email address, or specify a comma-separated list of addresses to send it to several recipients. A record of the last 10 receipts is visible on the payment’s page.

[Dashboard](https://dashboard.stripe.com/payments)

## Customize receipts

Alter the appearance and functionality of your receipts with the following customization options:

- Language: Select the language for your receipts in your Customer emails settings.

[Customer emails settings](https://dashboard.stripe.com/settings/emails)

- Branding: Modify the logo and colors in your Branding settings. The upper limit for a custom logo image file size is 512KB. Ideally, the logo should be a square image exceeding 128 x 128 pixels. JPG, PNG, and GIF file types are supported.

[Branding settings](https://dashboard.stripe.com/settings/branding)

- Public information: Specify the public information you want to include, such as your contact number or website address, in your Public details settings.

[Public details settings](https://dashboard.stripe.com/settings/public)

To display custom text, use the description attribute on the PaymentIntent. Some examples include:

[description](/api/payment_intents/create#create_payment_intent-description)

- Description of goods or services provided.

- Authorization code.

- Subscription information.

- Cancellation policies.

You can see a real-time preview of your email receipt on your Dashboard Branding settings page. To send a test receipt, hover over the preview image and click Send test receipt, then enter your email address.

Receipts pull data from the Charge object generated when the PaymentIntent is confirmed. To update receipt data such as the description after the charge is generated, you must update the Charge. Changes to a confirmed PaymentIntent don’t appear on receipts.

[update the Charge](/api/charges/update)

## Refund receipts

When a payment is refunded, Stripe can automatically send a receipt to the same email address provided in the original charge. You can also use the Dashboard to manually send a copy of the refund receipt. To enable automated refund receipts, toggle Refunds on in your Customer emails settings.

[Customer emails settings](https://dashboard.stripe.com/settings/emails)

## Invoice and subscription payment receipts

Stripe creates a receipt when a customer pays an invoice or makes any subscription payment. Receipts for subscription and invoice payments are itemized to include line items, discounts, and taxes. After payment, the Hosted Invoice Page includes a link to a receipt that the customer can download for their own records.

[invoice](/api/invoices)

[subscription](/billing/subscriptions/creating)

[Hosted Invoice Page](/invoicing/hosted-invoice-page)

## Stripe Connect receipts

Receipt settings depend on the charge and account type:

- Destination charges and separate charges and transfers: Receipts use the platform account’s Customer emails, Branding, and Public details settings.

Destination charges and separate charges and transfers: Receipts use the platform account’s Customer emails, Branding, and Public details settings.

[Destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

- Direct charges: Receipts use the connected account’s Customer emails, Branding, and Public details settings.

Direct charges: Receipts use the connected account’s Customer emails, Branding, and Public details settings.

[Direct charges](/connect/direct-charges)

Platform accounts can send a receipt for a connected account by passing receipt_email when making a charge request.

For connected accounts that use the Stripe Dashboard (which includes Standard connected accounts), you can configure receipt settings under Branding. For connected accounts that don’t use the Dashboard (which includes Express and Custom connected accounts), the platform configures receipt settings through settings.branding.

[Branding](https://dashboard.stripe.com/settings/branding)

[settings.branding](/api/accounts/update#update_account-settings-branding)

## Automatically send paid invoices

In addition to ordinary receipts, Payment Links can generate paid invoices as proof of payment. Invoices have more information than receipts. For subscriptions, Stripe generates invoices automatically, but for one-time payments, you need to enable them.

To generate invoices, toggle Successful payments on in your Customer emails settings. Then, when creating a Payment Link, select Create an invoice PDF in the After payment tab. You can configure your invoice, including adding a memo, footer, and your tax ID in your invoice template settings.

[Customer emails settings](https://dashboard.stripe.com/settings/emails)

[creating a Payment Link](https://dashboard.stripe.com/payment-links/create)

[invoice template settings](https://dashboard.stripe.com/settings/billing/invoice)

After the payment completes, Stripe sends an invoice summary with links to download the invoice PDF and invoice receipt to the email address your customer provides during checkout. You can also view the invoice in the Dashboard or access it programmatically by listening to the invoice.paid webhook event.

[Dashboard](https://dashboard.stripe.com/invoices)

[invoice.paid](/api/events/types#event_types-invoice.paid)

Invoices for delayed notification payment methods such as Bacs Direct Debit, Bank transfers, Boleto, Canadian pre-authorized debits, Konbini, OXXO, SEPA Direct Debit, SOFORT, or ACH Direct Debit might take longer to send because we send the invoice after successful payment, not upon checkout session completion.

[Bacs Direct Debit](/payments/bacs-debit/accept-a-payment)

[Bank transfers](/payments/bank-transfers/accept-a-payment)

[Boleto](/payments/boleto/accept-a-payment)

[Canadian pre-authorized debits](/payments/acss-debit/accept-a-payment)

[Konbini](/payments/konbini/accept-a-payment)

[OXXO](/payments/oxxo/accept-a-payment)

[SEPA Direct Debit](/payments/sepa-debit/accept-a-payment)

[SOFORT](/payments/sofort/accept-a-payment)

[ACH Direct Debit](/payments/ach-debit/accept-a-payment)

The downloadable invoice PDF

The downloadable invoice receipt

The customer email with links to the invoice PDF and receipt

## See also

- Send customer emails

[Send customer emails](/invoicing/send-email)

- Automate customer emails

[Automate customer emails](/billing/revenue-recovery/customer-emails)
