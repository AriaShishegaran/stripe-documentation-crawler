htmlEmail receipts and paid invoices | Stripe Documentation[Skip to content](#main-content)Email receipts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freceipts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freceipts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)
[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)During the payment# Email receipts and paid invoices

Send payment or refund receipts automatically.Payment LinksCheckoutDirect API or ElementsWith Checkout, you can manually or automatically send customized email receipts or paid invoices.

## Receipt features

### Receipts in test mode

Test payments created using your test API keys don’t automatically send receipts. Instead, you can view or manually send a receipt using the Dashboard.

Each receipt contains a link to view it in a browser, and a unique receipt number that’s useful when looking up payment information.

You can also access the link to view the receipt in a browser through the API in the PaymentIntent’s related Charge object. When you visit the link, the receipt always shows the latest status of that charge–if it has been refunded, the receipt accurately reflects it.

As a security measure, receipt links expire within 30 days. Expired receipt links require the customer to provide the original email address to resend the receipt to that address.

## Automatically send receipts

To enable automated receipts, toggle Successful payments on in your Customer emails settings. Receipts are only sent when a successful payment has been made—no receipt is sent if the payment fails or is declined.

## Manually send receipts

To send receipts in the Dashboard, click Send receipt within the Receipt history section of a Payment details page. You can also hover over a payment within the Payments section of a customer’s page and click the Send receipt icon. To resend an email receipt, input a different email address, or specify a comma-separated list of addresses to send it to several recipients. A record of the last 10 receipts is visible on the payment’s page.

## Customize receipts

Alter the appearance and functionality of your receipts with the following customization options:

- Language: Select the language for your receipts in your[Customer emails settings](https://dashboard.stripe.com/settings/emails).
- Branding: Modify the logo and colors in your[Branding settings](https://dashboard.stripe.com/settings/branding). The upper limit for a custom logo image file size is 512KB. Ideally, the logo should be a square image exceeding 128 x 128 pixels. JPG, PNG, and GIF file types are supported.
- Public information: Specify the public information you want to include, such as your contact number or website address, in your[Public details settings](https://dashboard.stripe.com/settings/public).

To display custom text, use the description attribute on the PaymentIntent. Some examples include:

- Description of goods or services provided.
- Authorization code.
- Subscription information.
- Cancellation policies.

You can see a real-time preview of your email receipt on your Dashboard Branding settings page. To send a test receipt, hover over the preview image and click Send test receipt, then enter your email address.

CautionReceipts pull data from the Charge object generated when the PaymentIntent is confirmed. To update receipt data such as the description after the charge is generated, you must update the Charge. Changes to a confirmed PaymentIntent don’t appear on receipts.

## Refund receipts

When a payment is refunded, Stripe can automatically send a receipt to the same email address provided in the original charge. You can also use the Dashboard to manually send a copy of the refund receipt. To enable automated refund receipts, toggle Refunds on in your Customer emails settings.

## Invoice and subscription payment receipts

Stripe creates a receipt when a customer pays an invoice or makes any subscription payment. Receipts for subscription and invoice payments are itemized to include line items, discounts, and taxes. After payment, the Hosted Invoice Page includes a link to a receipt that the customer can download for their own records.

## Stripe Connect receipts

Receipt settings depend on the charge and account type:

- Destination charges and separate charges and transfers: Receipts use the platform account’s Customer emails, Branding, and Public details settings.


- Direct charges: Receipts use the connected account’s Customer emails, Branding, and Public details settings.



Platform accounts can send a receipt for a connected account by passing receipt_email when making a charge request.

For connected accounts that use the Stripe Dashboard (which includes Standard connected accounts), you can configure receipt settings under Branding. For connected accounts that don’t use the Dashboard (which includes Express and Custom connected accounts), the platform configures receipt settings through settings.branding.

## Automatically send paid invoices

In addition to ordinary receipts, Checkout can generate paid invoices as proof of payment. Invoices have more information than receipts. For subscriptions, Stripe generates invoices automatically, but for one-time payments, you need to enable them.

NoteInvoice creation for one-time payments in Checkout is not an Invoicing feature, and is priced separately. Review this support article to learn more.

To generate invoices, first, in your Customer emails settings, under Email customers about, select Successful payments. Then, when creating a Checkout session, set invoice_creation[enabled] to true.

NoteEnabling invoice_creation isn’t supported if you set payment_intent_data[capture_method] to manual.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=payment \
  -d "invoice_creation[enabled]"=true \
  -d "line_items[0][price]"={{ONE_TIME_PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  --data-urlencode success_url="https://example.com" \
  --data-urlencode cancel_url="https://example.com"`After the payment completes, Stripe sends an invoice summary with links to download the invoice PDF and invoice receipt to the email address your customer provides during checkout.

CautionInvoices for delayed notification payment methods such as Bacs Direct Debit, Bank transfers, Boleto, Canadian pre-authorized debits, Konbini, OXXO, SEPA Direct Debit, SOFORT, or ACH Direct Debit might take longer to send because we send the invoice after successful payment, not upon checkout session completion.

![Screenshot of the invoice PDF that customers can download from the invoice summary email](https://b.stripecdn.com/docs-statics-srv/assets/invoice.9e44668032383601eeec362f38293b7a.png)

The downloadable invoice PDF

![Screenshot of the invoice receipt that customers can download from the invoice summary email](https://b.stripecdn.com/docs-statics-srv/assets/invoice_receipt.4f120ee7363f8e7728fa553a8a24aae3.png)

The downloadable invoice receipt

![Screenshot of the invoice summary email Stripe sends](https://b.stripecdn.com/docs-statics-srv/assets/email.560c2666905531b907f7fcd4f1a0a6dd.png)

The customer email with links to the invoice PDF and receipt

You can also view the invoice in the Dashboard or access it programmatically by listening to the invoice.paid webhook event.

You can use the invoice_data hash inside invoice_creation to further customize the invoice generated by the Checkout Session.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=payment \
  -d "invoice_creation[enabled]"=true \
  -d "invoice_creation[invoice_data][description]"="Invoice for Product X" \
  -d "invoice_creation[invoice_data][metadata][order]"=order-xyz \
  -d "invoice_creation[invoice_data][account_tax_ids][0]"=DE123456789 \
  -d "invoice_creation[invoice_data][custom_fields][0][name]"="Purchase Order" \
  -d "invoice_creation[invoice_data][custom_fields][0][value]"=PO-XYZ \
  -d "invoice_creation[invoice_data][rendering_options][amount_tax_display]"=include_inclusive_tax \
  -d "invoice_creation[invoice_data][footer]"="B2B Inc." \
  -d "line_items[0][price]"={{ONE_TIME_PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  --data-urlencode success_url="https://example.com" \
  --data-urlencode cancel_url="https://example.com"`Review invoice best practices for your region to make sure you’re collecting the right information from your customers. Information like the customer’s billing and shipping addresses, phone number and tax ID appear on the resulting invoice.

## See also

- [Send customer emails](/invoicing/send-email)
- [Automate customer emails](/billing/revenue-recovery/customer-emails)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Receipt features](#receipt-features)[Automatically send receipts](#automatically-send-receipts)[Manually send receipts](#manually-send-receipts-from-dashboard)[Customize receipts](#customizing-receipts)[Refund receipts](#refund-receipts)[Invoice and subscription payment receipts](#invoice-and-subscription-payment-receipts)[Stripe Connect receipts](#receipts-for-stripe-connect)[Automatically send paid invoices](#paid-invoices)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`