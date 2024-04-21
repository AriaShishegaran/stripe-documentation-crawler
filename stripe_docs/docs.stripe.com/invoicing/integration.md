# Integrate with the Invoicing API

The Dashboard is the most common way to create invoices. If you’d like to automate invoice creation, you can integrate with the API. Build a full, working Invoicing integration using our sample integration.

[Dashboard](https://dashboard.stripe.com/invoices)

[create invoices](/invoicing/dashboard#create-invoice)

[sample integration](/invoicing/integration/quickstart)

You don’t need to integrate with the Payments API to integrate with the Invoicing API.

[Set up Stripe](#setup)

## Set up Stripe

Use our official libraries for access to the Stripe API:

[Create a product](#create-product)

## Create a product

To create a product, enter its name:

[Create a price](#create-prices)

## Create a price

Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the billing interval (when the price is for a subscription). Like products, if you only have a few prices, it’s preferable to manage them in the Dashboard. Use the unit amount to express prices in the lowest unit of the currency—in this case, cents (10 USD is 1,000 cents, so the unit amount is 1000).

[Prices](/api#prices)

As an alternative, if you don’t need to create a price for your product, you can use the amount parameter during invoice item creation.

[amount](/api/invoiceitems/create#create_invoiceitem-amount)

To create a price and assign it to the product, pass the product ID, unit amount, and currency. In the following example, the price for the “Gold Special” product is 10 USD:

[Create a customer](#create-customer-code)

## Create a customer

The Customer object represents the customer purchasing your product. It’s required for creating an invoice. To create a customer with a name, email, and description, add the following code replacing the values with your own:

[Customer](/api#customer_object)

After you create the customer, store the customer id in your database so that you can use it later. The next step, for example, uses the customer ID to create an invoice.

See Create a customer for additional parameters.

[Create a customer](/api/customers/create)

[Create an invoice](#create-invoice-code)

## Create an invoice

Set the collection_method attribute to send_invoice. For Stripe to mark an invoice as past due, you must add the days_until_due parameter. When you send an invoice, Stripe emails the invoice to the customer with payment instructions.

[collection_method](/api/invoices/object#invoice_object-collection_method)

[days_until_due](/api/invoices/create#create_invoice-days_until_due)

Then, create an invoice item by passing in the customer id, product price, and invoice ID invoice.

The maximum number of invoice items is 250.

If you set auto_advance to false, you can continue to modify the invoice until you finalize it. To finalize a draft invoice, use the Dashboard, send it to the customer, or pay it. You can also use the Finalize API:

[finalize](/invoicing/integration/workflow-transitions)

[Finalize](/api/invoices/finalize)

If you created the invoice in error, void it. You can also mark an invoice as uncollectible.

[void](/invoicing/overview#void)

[uncollectible](/invoicing/overview#uncollectible)

[Accept invoice payment](#accept-invoice-payment)

## Accept invoice payment

Send the invoice to the email address associated with the customer. As soon as the an invoice is sent, Stripe finalizes it. Many jurisdictions consider finalized invoices a legal document making certain fields unalterable. If you send invoices that have already been paid, there’s no reference to the payment in the email.

When you send invoices that have already been paid, the email doesn’t reference the payment. Stripe sends invoices to the email address associated with the customer.

[Handle post-payment events](#handle-payment-events)

## Handle post-payment events

Stripe sends an invoice.paid event when an invoice payment completes. Listen for this event to ensure reliable fulfillment. If your integration relies on only a client-side callback, the customer could lose connection before the callback executes, which would result in the customer being charged without your server being notified. Setting up your integration to listen for asynchronous events is also what enables you to accept different types of payment methods with a single integration.

[invoice.paid](/api/events/types?event_types-invoice.paid)

[different types of payment methods](https://stripe.com/payments/payment-methods-guide)

Successful invoice payments trigger both an invoice.paid and invoice.payment_succeeded event. Both event types contain the same invoice data, so it’s only necessary to listen to one of them to be notified of successful invoice payments. The difference is that invoice.payment_succeeded events are sent for successful invoice payments, but aren’t sent when you mark an invoice as paid_out_of_band. invoice.paid events, on the other hand, are triggered for both successful payments and out of band payments. Because invoice.paid covers both scenarios, we typically recommend listening to invoice.paid rather than invoice.payment_succeeded.

[invoice.paid](/api/events/types?event_types-invoice.paid)

[invoice.payment_succeeded](/api/events/types?event_types-invoice.payment_succeeded)

[paid_out_of_band](/api/invoices/pay#pay_invoice-paid_out_of_band)

Use the Dashboard webhook tool or follow the webhook quickstart to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[Dashboard webhook tool](https://dashboard.stripe.com/webhooks)

[webhook quickstart](/webhooks/quickstart)

In addition to handling the invoice.paid event, we recommend handling two other events when collecting payments with the Payment Element:

[payment_intent.processing](/api/events/types?lang=php#event_types-payment_intent.processing)

[invoice.payment_failed](/api/events/types?lang=php#event_types-payment_intent.payment_failed)

[OptionalCustomize an invoice](#customize-invoices)

## OptionalCustomize an invoice

## See also

- Post-finalization

[Post-finalization](/invoicing/integration/workflow-transitions#post-finalized)

- Use incoming webhooks to get real-time updates

[Use incoming webhooks to get real-time updates](/webhooks)
