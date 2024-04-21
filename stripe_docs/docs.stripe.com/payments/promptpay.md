# PromptPay payments

PromptPay is a Thailand based payment method that allows customers to make a payment using their preferred app from participating banks.

Customers see a QR code when checking out with PromptPay. They complete the payment by scanning it using a Thailand bank app. You receive confirmation from Stripe instantly when they complete the payment.

- Customer locationsThailand

Customer locations

Thailand

- Presentment currencyTHB

Presentment currency

THB

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyReal-time payments

Payment method family

Real-time payments

- Billing supportYes

Billing support

Yes

- Connect supportYes

Connect support

Yes

- Dispute supportNot applicable

Dispute support

Not applicable

- Refunds / Partial refundsYes / Yes

Refunds / Partial refunds

Yes / Yes

## Payment flow

1. Selects PromptPay at checkout

2. Scans displayed QR code with preferred app

3. Authorizes payment

4. Gets notification that payment is complete

[Get started](#get-started)

## Get started

You don’t actually have to integrate PromptPay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding PromptPay from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

- Subscriptions

[Subscriptions](/billing/subscriptions/overview)

Invoices and Subscriptions only support the send_invoice collection method.

[collection method](/api/invoices/object#invoice_object-collection_method)

If you prefer to manually list payment methods, learn how to manually configure PromptPay as a payment.

[manually configure PromptPay as a payment](/payments/promptpay/accept-a-payment)

[Refunds](#refunds)

## Refunds

Stripe supports refunds of PromptPay payments either through the Dashboard or API. To complete a refund, your customer must tell us where to return the funds. Stripe automatically contacts the customer at the email address provided at time of PaymentIntent confirmation and requests refund account information from them. Your customer must provide the account number of the bank account from which the payment was made, or the refund may fail. We will process the refund automatically after receiving the refund account information.

[Dashboard](https://dashboard.stripe.com/payments)

[API](/api#create_refund)

[Statement descriptors](#statement-descriptors)

## Statement descriptors

PromptPay doesn’t support customized statement descriptors, and it ignores the value specified in the statement_descriptor. Customers see the Stripe company name (STRIPE PAYMENTS (THAILAND) LTD) when they complete payments on their banking app. They also see it on bank statements, along with the amount and a unique reference code.

[statement_descriptor](/api/payment_intents/create#create_payment_intent-statement_descriptor)

[Repeated payments](#repeated-payments)

## Repeated payments

After a customer successfully completes a transaction, any attempt to use the same QR code again may result in having the funds deducted from their bank account. If Stripe receives any excess funds from your customers, we reimburse them to your account balance and notify you. You will need to issue the refund to your customers outside of Stripe (for example, with a check, cash, or store credit).

[Disputed payments](#disputed-payments)

## Disputed payments

PromptPay payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment through banking apps. However, cases of irregularities similar to disputes, or other unexpected/repeated payments may arise. Stripe reviews these cases, and may contact you or take other action if required.
