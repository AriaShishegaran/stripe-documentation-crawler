# Status transitions and finalization

The following graphic shows the different ways that an invoice can transition from status to status:

Status transitions and finalization

## Transitions and endpoints

The following table outlines the status transitions and their endpoints. It also lists the webhooks that are emitted by the endpoint, and the resulting status for each:

[webhooks](/webhooks)

[DELETE /v1/invoices/:id](/api/invoices/delete)

[POST /v1/invoices/:id/finalize](/api/invoices/finalize)

[POST /v1/invoices/:id/pay](/api/invoices/pay)

[POST /v1/invoices/:id/pay](/api/invoices/pay)

[POST /v1/invoices/:id/send](/api/invoices/send)

[POST /v1/invoices/:id/void](/api/invoices/void)

[POST /v1/invoices/:id/mark_uncollectible](/api/invoices/mark_uncollectible)

[POST /v1/invoices/:id/pay](/api/invoices/pay)

[POST /v1/invoices/:id/pay](/api/invoices/pay)

[POST /v1/invoices/:id/void](/api/invoices/void)

## Finalize draft invoices

When you enable automatic collection, Stripe automatically finalizes, and begins automatic collection of the invoice. We wait an hour after receiving a successful response to the invoice.created event before attempting payment. If we don’t receive a successful response within 72 hours, we attempt to finalize and send the invoice.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

[invoice](/billing/invoices/subscription)

Invoices are initially created with status=draft, and you can only edit them while they’re in this state. When an invoice is ready to be paid, finalize it. Finalizing an invoice sets status=open on the invoice. You can manually finalize an invoice in the Dashboard or by using the Finalize endpoint. If you’ve configured webhook endpoints, you receive an invoice.finalized event when an invoice finalizes.

[Dashboard](/invoicing/dashboard)

[Finalize](/api/invoices/finalize)

[webhook](/webhooks)

In live mode, if your webhook endpoint doesn’t respond properly, Stripe continues retrying the webhook notification for up to 3 days with an exponential back off. In test mode, we retry three times over a few hours. During that time, we won’t attempt to charge the customer unless we receive a successful response. We also send you an email to notify you that the webhook is failing.

[respond properly](/webhooks)

This behavior applies to all webhook endpoints defined on your account, including cases where a Connect application or other third-party service is having trouble handling incoming webhooks.

[Connect application](https://stripe.com/works-with)

## Post-finalization

Finalizing an invoice does the following:

- It allows the invoice to be paid.

- It ensures that an invoice number is present.

- It makes certain properties immutable on the invoice.

[immutable](#immutable)

- It creates an incomplete payment intent for the invoice.

- It generates a unique URL where someone can pay the invoice, and a link to download a PDF of the invoice.

[PDF of the invoice](/api/invoices/object#invoice_object-invoice_pdf)

If an invoice isn’t finalized, you can’t collect payment.

After you finalize an invoice, you can’t change certain fields that pertain to the amount and customer. This is to satisfy the common tax-compliance requirement that finalized invoices be retained—as they were finalized—for a legally required minimum time period.

In some jurisdictions, editing fields that modify the total amount due on an invoice could render the invoice invalid. These are typically fields associated with your account, customer, line items, or taxes. It’s your responsibility to make sure that the invoices you create comply with all applicable laws.

If you require updates to the invoice amount after it finalizes, use credit notes. Credit notes allow you to modify the invoice amount by specifying an adjustment in money owed by the customer. You can issue credit notes for any invoice in an open or paid status. Finalizing the invoice copies the following customer fields to it and makes them immutable:

[credit notes](/invoicing/dashboard/credit-notes)

- invoice.customer_address

[invoice.customer_address](/api/invoices/object#invoice_object-customer_address)

- invoice.customer_email

[invoice.customer_email](/api/invoices/object#invoice_object-customer_email)

- invoice.customer_name

[invoice.customer_name](/api/invoices/object#invoice_object-customer_name)

- invoice.customer_phone

[invoice.customer_phone](/api/invoices/object#invoice_object-customer_phone)

- invoice.customer_shipping

[invoice.customer_shipping](/api/invoices/object#invoice_object-customer_shipping)

- invoice.customer_tax_exempt

[invoice.customer_tax_exempt](/api/invoices/object#invoice_object-customer_tax_exempt)

- invoice.customer_tax_ids

[invoice.customer_tax_ids](/api/invoices/object#invoice_object-customer_tax_ids)

If you want to change a customer-related property on an invoice:

- Void the current invoice.

- Duplicate the voided invoice.

[Duplicate](/invoicing/dashboard#modify-invoice)

- Update the customer information on the new invoice.

By default, Stripe automatically sends invoices when you set collection_method to send_invoice. Stripe doesn’t email invoices in the following cases:

[collection_method](/api/invoices/object#invoice_object-collection_method)

- When charged automatically.

[charged automatically](/invoicing/automatic-charging)

- When automatic collection is turned off for the invoice.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

- When the Email finalized invoices to customers option is turned off.

[Email finalized invoices to customers](https://dashboard.stripe.com/settings/billing/automatic)

If you turn off the Email finalized invoices to customers option, automatic or manual finalization doesn’t send an invoice.

## Asynchronous payments

For more details on using the Payment Intents API to complete 3D Secure authentication, refer to the 3D Secure guide.

[Payment Intents API](/payments/payment-intents)

[3D Secure](/payments/3d-secure)

[3D Secure guide](/payments/3d-secure/authentication-flow#when-to-use-3d-secure)

Some payment methods require customer interaction to complete the payment—for example, a European card or bank transfer may require Strong Customer Authentication (SCA).

[Strong Customer Authentication](/strong-customer-authentication)

Use the invoice’s payment_intent parameter to choose how to handle the response from the payment attempt, which may be either success or requires_action.

[payment_intent](/api/invoices/object#invoice_object-payment_intent)

When the status of the PaymentIntent is requires_action, you must have your user complete a 3D Secure authentication to complete the payment.

[3D Secure authentication](/billing/migration/strong-customer-authentication#scenario-4)

Instead of building this yourself, you can rely on Stripe to handle it for you. Enable reminder emails in the Dashboard so that Stripe can automatically send emails to your customers whenever requires_action occurs. These emails include a link to the Hosted Invoice Page, where a customer can perform all of the actions required to pay the invoice. To learn more about these emails and how to customize them, see Sending email reminders.

[Enable reminder emails](https://dashboard.stripe.com/settings/billing/automatic)

[Hosted Invoice Page](/invoicing/hosted-invoice-page)

[Sending email reminders](/invoicing/send-email)
