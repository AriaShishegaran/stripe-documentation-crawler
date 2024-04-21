# Hosted Invoice Page

The Hosted Invoice Page provides a secure, private URL where your customers can:

- View the details, amounts, and status of the invoice.

- Pay the invoice using any of the enabled payment methods.

- Download PDF copies of the invoice and receipt.

A sample Hosted Invoice Page

Stripe assigns all invoices a unique URL that you can send to your customer. We host these invoices, which means you can securely collect payments without any extra implementation code.

## Invoice URLs

When you create and send an invoice, Stripe generates a unique URL for the Hosted Invoice Page. The URL includes a secure, long, and random identifier, resembling the following example:

Invoice URLs expire 30 days after the due date. If the invoice doesn’t have a due date, the invoice expires 30 days after it finalizes. In all cases, the expiration window is never longer than 120 days.

Even after expiration, any URLs that the Dashboard displays or a user retrieves through the API are guaranteed to be valid for at least 10 days.

When a URL expires, it no longer loads the intended resource. Instead, Stripe redirects invoiced customers to a page that states that the URL has expired and to contact the merchant. This page also provides the merchant’s contact information.

If you sent an invoice through the Dashboard or API, any email recipients are automatically associated with that invoice. In this case, Stripe redirects the user to a recovery page where they can enter their email address to receive a new copy of the original email with non-expired links.

## Invoice email links

You can configure the invoice email to include a link to the Hosted Invoice Page. When enabled, the Hosted Invoice Page URL appears in:

- Invoice emails as a payment link.

- The footer of invoice PDFs.

- The Invoice API response as hosted_invoice_url.

[hosted_invoice_url](/api/invoices/object#invoice_object-hosted_invoice_url)

To enable the Hosted Invoice Page for all newly created invoices, select the checkbox for Include a Stripe-hosted link to an invoice payment page in the invoice email in the Invoice template.

[Invoice template](https://dashboard.stripe.com/account/billing/invoice)

Enable the Hosted Invoice Page by default

To enable the Hosted Invoice Page on any individual invoice, click the gear icon and select Email invoice with link in the Payment section when you’re editing an invoice. Once selected, Email invoice to customer with link to payment page appears next to the radio button.

You can also generate a link to the Hosted Invoice Page by clicking the gear icon and selecting Send invoice or link manually. (We don’t send an email to your customer when you select this option). After you complete the invoice go to the Details section in your invoice’s details page. Next to Payment page, copy the link and send it manually.

## Page customization

The Hosted Invoice Page is customizable with your:

- Brand color

- Logo

- Icon

You can customize these branding settings in the Dashboard.

[branding settings](https://dashboard.stripe.com/account/branding)

## Set allowed payment methods

From the Hosted Invoice Page, you can configure invoices to allow payment with one or more of the supported payment methods. You can set defaults to apply to all of the newly created invoices from the Invoice template. You can also select the payment method on a per-invoice basis when you’re creating an invoice through the Dashboard.

[supported payment methods](/invoicing/payment-methods)

[Invoice template](https://dashboard.stripe.com/account/billing/invoice)

[creating an invoice](https://dashboard.stripe.com/invoices/create)

With the Hosted Invoice Page, you can display the allowed payment method list to the customer. This gives them the option to choose a payment method that suits them best. Additionally, enabling the Hosted Invoice Page gives the customer the benefit of having Stripe handle complex payment and authentication flows (without any extra implementation effort from you).

For example, the Strong Customer Authentication (SCA) regulation in Europe requires customers to confirm their payment with 3D Secure (3DS). In this case, the Hosted Invoice Page displays the payment confirmation modal to your customer.

[Strong Customer Authentication](/strong-customer-authentication)

[3D Secure](/payments/3d-secure)

## Payment method persistence

Cards, Bacs Direct Debit and BECS Direct Debit details that you enter on the Hosted Invoice Page are stored on the customer for use in subsequent payments. We don’t store single-use payment methods like iDEAL, Bancontact, Sofort, and giropay for reuse.

## Public support information

Invoices include any public information that you specified under Public business information, such as your support email address or business website. Using these settings, you can also choose to include a support phone number in customer-facing documents—like invoice PDFs and emails—or default to your business address.

[Public business information](https://dashboard.stripe.com/settings/public)
