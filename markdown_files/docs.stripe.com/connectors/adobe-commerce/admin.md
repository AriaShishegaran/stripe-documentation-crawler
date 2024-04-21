htmlUsing the Adobe Commerce admin panel | Stripe Documentation[Skip to content](#main-content)Use the admin panel[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce%2Fadmin)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce%2Fadmin)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Adobe Commerce](/docs/connectors/adobe-commerce)# Using the Adobe Commerce admin panel

Learn how to use the Adobe Commerce admin panel to configure the Stripe module for the Adobe Commerce platform.## Issuing refunds

1. Go toSales > Ordersto find the order you want to refund.
2. If you setPayment ActiontoAuthorize Only, the only action you need to take is to press theCancelbutton at the top of the page. However, if you chose toAuthorize and Capture, proceed to the next step.
3. From the left sidebar, clickInvoices, then click on the[invoice](/api/invoices)to refund it.
4. At the top right-hand corner, clickCredit Memo.
5. Adjust the amount (if necessary) and clickRefundat the bottom of the page to perform a live refund. By clickingRefund Offline, you only issue the refund in Adobe Commerce and not in Stripe.

1. For a partial refund, you can adjust theAdjustment Fee. This is the amount you don’t want to refund. In the screenshot above, by setting the adjustment fee to 10 USD, we’re refunding 53.87 USD and 10 USD is kept as a fee. You can ignore theAdjustment Refundfield because we won’t refund an amount that is greater than the original payment of the customer.

The amount is now fully or partially refunded in Stripe and a note appears in the Comments History of the order.

## Authorizing card payments and capturing later

In your card settings, you can set Payment Action to only authorize card payments when placing an order. The bank guarantees the amount and holds it on the customer’s card for up to 7 days. Failure to capture the payment by this time cancels the authorization and releases the funds.

Optionally, you can set Expired Authorizations to attempt to re-authorize the payment in case you miss the 7-day window but it isn’t guaranteed to succeed.

When ready to capture (for example, you shipped the product), follow these steps:

1. Go toSales > Orders.
2. Find the relevant order.
3. ClickInvoice.
4. If you need to issue a partial invoice, adjust the invoice items as shown in the video below. You can reduce the item quantity but not increase it.
5. ClickSubmit Invoiceto capture and finalize the payment.

After clicking Submit Invoice, you can see the captured funds in the Stripe Dashboard.

## Creating orders

You can create an order and charge a customer’s card with details that you’ve received over the phone, directly from the Adobe Commerce admin panel:

1. Go toSales > Orders.
2. At the top right hand side, clickCreate New Order.
3. Choose a customer, the store, and any products for that order.
4. Select a shipping method (if applicable) before filling in payment details.
5. When you’re ready to submit the order, select a saved payment method. Clicking theAdd newbutton redirects you to the customer page in Stripe, where you can securely enter a new payment method.
6. ClickSubmit Order.

![](https://b.stripecdn.com/docs-statics-srv/assets/admin-create-orders.be0947d1846510897ad2fa16e62c72ab.png)

Payment information for admin orders

If you set Payment Action to authorize and capture, we charge the card immediately. If you set Payment Action to authorize only, you must also capture the payment.

## Send an invoice to the customer

When creating a new order from your Adobe Commerce admin, you have the option to send an invoice link to the customer by email:

![](https://b.stripecdn.com/docs-statics-srv/assets/admin-send-invoice.ac36fd329e005e4310d379702bcece25.png)

Send an invoice to the customer

You can change the due date to help keeping track of late payments in your Stripe Dashboard.

Using this method is more secure than paying by card from the Admin Panel as you avoid collecting sensitive payment information over the phone. By opening the link in the email, the customer opens a Hosted Invoice Page which includes a payment form.

## See also

- [Troubleshooting](/connectors/adobe-commerce/troubleshooting)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Issuing refunds](#issuing-refunds)[Authorizing card payments and capturing later](#capturing-later)[Creating orders](#creating-orders)[Send an invoice to the customer](#send-an-invoice-to-the-customer)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`