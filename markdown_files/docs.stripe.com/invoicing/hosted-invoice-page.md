htmlHosted Invoice Page | Stripe Documentation[Skip to content](#main-content)Hosted Invoice Page[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fhosted-invoice-page)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fhosted-invoice-page)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)# Hosted Invoice Page

Use the Hosted Invoice Page to securely collect payment from your customers.The Hosted Invoice Page provides a secure, private URL where your customers can:

- View the details, amounts, and status of the invoice.
- Pay the invoice using any of the enabled payment methods.
- Download PDF copies of the invoice and receipt.

![](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page.3f79f6d4ded5d51047ae2b16270c2c42.png)

A sample Hosted Invoice Page

Stripe assigns all invoices a unique URL that you can send to your customer. We host these invoices, which means you can securely collect payments without any extra implementation code.

## Invoice URLs

When you create and send an invoice, Stripe generates a unique URL for the Hosted Invoice Page. The URL includes a secure, long, and random identifier, resembling the following example:

`https://invoice.stripe.com/i/acct_abcdefghijklmno/test_YWNjdF8xRGZ3UzJDbENJS2xqV3ZzLF9MNGJvMDBzY0xFQ2c1cG1QZzZ6Wk5jV0RXR2lOS1V6LDM0Mjk3NjEz0200wpYOWgBE?s=em`Invoice URLs expire 30 days after the due date. If the invoice doesn’t have a due date, the invoice expires 30 days after it finalizes. In all cases, the expiration window is never longer than 120 days.

NoteEven after expiration, any URLs that the Dashboard displays or a user retrieves through the API are guaranteed to be valid for at least 10 days.

DashboardAPIWhen a URL expires, it no longer loads the intended resource. Instead, Stripe redirects invoiced customers to a page that states that the URL has expired and to contact the merchant. This page also provides the merchant’s contact information.

NoteIf you sent an invoice through the Dashboard or API, any email recipients are automatically associated with that invoice. In this case, Stripe redirects the user to a recovery page where they can enter their email address to receive a new copy of the original email with non-expired links.

## Invoice email links

You can configure the invoice email to include a link to the Hosted Invoice Page. When enabled, the Hosted Invoice Page URL appears in:

- Invoice emails as a payment link.
- The footer of invoice PDFs.
- The Invoice API response as[hosted_invoice_url](/api/invoices/object#invoice_object-hosted_invoice_url).

To enable the Hosted Invoice Page for all newly created invoices, select the checkbox for Include a Stripe-hosted link to an invoice payment page in the invoice email in the Invoice template.

![](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page-default.c99683dc71960790d621bc6e8ba3e064.png)

Enable the Hosted Invoice Page by default

To enable the Hosted Invoice Page on any individual invoice, click the gear icon and select Email invoice with link in the Payment section when you’re editing an invoice. Once selected, Email invoice to customer with link to payment page appears next to the radio button.

You can also generate a link to the Hosted Invoice Page by clicking the gear icon and selecting Send invoice or link manually. (We don’t send an email to your customer when you select this option). After you complete the invoice go to the Details section in your invoice’s details page. Next to Payment page, copy the link and send it manually.

## Page customization

The Hosted Invoice Page is customizable with your:

- Brand color
- Logo
- Icon

You can customize these branding settings in the Dashboard.

## Set allowed payment methods

From the Hosted Invoice Page, you can configure invoices to allow payment with one or more of the supported payment methods. You can set defaults to apply to all of the newly created invoices from the Invoice template. You can also select the payment method on a per-invoice basis when you’re creating an invoice through the Dashboard.

With the Hosted Invoice Page, you can display the allowed payment method list to the customer. This gives them the option to choose a payment method that suits them best. Additionally, enabling the Hosted Invoice Page gives the customer the benefit of having Stripe handle complex payment and authentication flows (without any extra implementation effort from you).

NoteFor example, the Strong Customer Authentication (SCA) regulation in Europe requires customers to confirm their payment with 3D Secure (3DS). In this case, the Hosted Invoice Page displays the payment confirmation modal to your customer.

## Payment method persistence

Cards, Bacs Direct Debit and BECS Direct Debit details that you enter on the Hosted Invoice Page are stored on the customer for use in subsequent payments. We don’t store single-use payment methods like iDEAL, Bancontact, Sofort, and giropay for reuse.

## Public support information

Invoices include any public information that you specified under Public business information, such as your support email address or business website. Using these settings, you can also choose to include a support phone number in customer-facing documents—like invoice PDFs and emails—or default to your business address.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Invoice URLs](#invoice-urls)[Invoice email links](#email-links)[Page customization](#page-customization)[Set allowed payment methods](#set-payment-methods)[Payment method persistence](#payment-method-persistence)[Public support information](#public-support-info)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`