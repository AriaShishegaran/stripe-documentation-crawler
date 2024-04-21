# PayNow payments

PayNow is a Singapore based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions.

Customers see a QR code when checking out with PayNow. They complete the payment by scanning it using a participating app. You receive confirmation from Stripe instantly when they complete the payment.

[a participating app](https://www.abs.org.sg/consumer-banking/pay-now)

- Customer locationsSingapore

Customer locations

Singapore

- Presentment currencySGD

Presentment currency

SGD

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyReal-time payments

Payment method family

Real-time payments

- Billing supportYes

Billing support

Yes

- Payout timingT+1 availability

Payout timing

T+1 availability

- Connect supportYes

Connect support

Yes

- Dispute supportNot applicable

Dispute support

Not applicable

- Refunds / Partial refundsYes / Yes

Refunds / Partial refunds

Yes / Yes

- Pricing1.3%

Pricing

1.3%

[Get started](#refunds)

## Get started

You don’t actually have to integrate PayNow and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding PayNow from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

- Subscriptions

[Subscriptions](/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to manually configure PayNow as a payment.

[manually configure PayNow as a payment](/payments/paynow/accept-a-payment)

[Refunds](#refunds)

## Refunds

You can refund PayNow payments up to 90 days after the original payment. Refunds for PayNow payments are asynchronous and Stripe notifies you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the status of the Refund object transitions to succeeded. If a refund fails, the status of the Refund object transitions to failed and Stripe returns the amount to your Stripe balance. At this point, you need to arrange an alternative way of providing your customer with a refund.

[webhook](/webhooks)

[Refund](/api/refunds/object)

[Statement descriptors](#statement-descriptors)

## Statement descriptors

Customized statement descriptors aren’t supported by PayNow, the value specified in the statement_descriptor is ignored. Stripe’s company name (STRIPE PAYMENTS SINGAPORE PTE. LTD.) is shown when your customers complete payments on their mobile app. It’s also shown on bank statements along with the amount and a Stripe-generated reference code.

[statement_descriptor](/api/payment_intents/create#create_payment_intent-statement_descriptor)

[Repeated payments](#repeated-payments)

## Repeated payments

To prevent your customers from being charged multiple times, after your customer successfully completes a transaction, any subsequent attempts to pay using the same QR code are rejected. The rejection behavior depends on the bank and payment app used by the customer to attempt the transaction. If your customers contact you about repeated payments, you can advise them to check for text messages or notifications from their bank or payment app, which will show that the payment attempt was rejected.

[Billing](#billing)

## Billing

Use Stripe Billing to create PayNow supported subscriptions and invoices.

[Stripe Billing](https://stripe.com/billing)

[subscriptions](/billing/subscriptions/creating)

[invoices](/api/invoices)

PayNow payments don’t support automatically charging invoices. You need to configure invoices and subscriptions with send_invoice collection_method.

[automatically charging](/invoicing/automatic-charging)

[collection_method](/api/invoices/object#invoice_object-collection_method)

[Payout Timing](#payout-timing)

## Payout Timing

By default, it takes 1 day from the time of the transaction for the funds to be available in your Stripe balance. Stripe pays out available funds to your bank account according to the payout schedule set on your Stripe account.

For example, if the payment was made on Wednesday, the funds are available in your Stripe balance on Thursday. If you’re on an automatic daily payout schedule, the funds are paid out on Thursday. If you’re on a weekly (Monday) payout schedule, the funds are paid out on the coming Monday.

[Disputed payments](#disputed-payments)

## Disputed payments

PayNow payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment through participating apps. As a result, there’s no dispute process that can result in a chargeback and funds being withdrawn from your Stripe account.

[Prohibited business categories](#prohibited-business-categories)

## Prohibited business categories

On top of the categories of businesses restricted from using Stripe overall, the following categories are specifically prohibited from using PayNow.

[businesses restricted from using Stripe overall](https://stripe.com/restricted-businesses)

- Petroleum and Petroleum Products

- Fuel Dealers

- Service Stations

- Automated Fuel Dispensers
