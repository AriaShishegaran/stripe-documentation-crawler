# FPX payments

Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and 11 other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It’s one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM.

In order to pay with FPX, customers are redirected to their online banking environment where they have to perform two-step authorization. The exact customer experience varies depending on their bank. The FPX payment flow is well understood and intuitive to Malaysian customers.

As part of being regulatory compliant, Stripe requires merchants to provide their Business Registration Number (BRN) to process FPX charges and receive payouts.

- Customer locationsMalaysia

Customer locations

Malaysia

- Presentment currencyMYR

Presentment currency

MYR

- Payment confirmationCustomer-authenticated

Payment confirmation

Customer-authenticated

- Payment method familyAuthenticated bank debit

Payment method family

Authenticated bank debit

- Recurring paymentsNo

Recurring payments

No

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

- Dispute supportNo

Dispute support

No

- Connect supportYes

Connect support

Yes

- Payout timing5 business days

Payout timing

5 business days

## Payment flow

Watch a video

[Watch a video](#payment-flow-video)

Customer selects FPX at checkout

Chooses bank and gets redirected

Customer enters account credentials

Customer completes authorization process

Customer gets notification that payment is complete

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t actually have to integrate FPX and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding FPX from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

If your integration requires manually listing payment methods, learn how to manually configure FPX as a payment.

[manually configure FPX as a payment](/payments/fpx/accept-a-payment)

Check out the FPX sample on GitHub.

[sample on GitHub](https://github.com/stripe-samples/accept-a-payment)

[Disputed payments](#disputed-payments)

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

[Refunds](#refunds)

## Refunds

FPX payments can be refunded up to 60 days after the original payment. Refunds for FPX payments are asynchronous and take approximately 1 week to complete. We’ll notify you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the Refund object’s status transitions to succeeded. A refund can fail if the customer’s bank is unable to process it correctly (for example, the bank account is closed). In the rare instance that a refund fails, the Refund object’s status will transition to failed and we’ll return the amount to your Stripe balance. You’ll then need to arrange an alternative way of providing your customer with a refund.

[webhook](/webhooks)

[Refund](/api/refunds/object)
