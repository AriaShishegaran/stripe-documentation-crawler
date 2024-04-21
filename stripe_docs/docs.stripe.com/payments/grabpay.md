# GrabPay payments

GrabPay is a payment method developed by Grab. GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with.

[Grab](https://www.grab.com/sg/pay/)

In order to pay with GrabPay, customers are redirected to GrabPay’s website, where they have to authenticate the transaction using a one-time password. After authenticating, customers will be redirected back to your website.

- Customer locationsSingapore, Malaysia

Customer locations

Singapore, Malaysia

- Presentment currencySGD, MYR

Presentment currency

SGD, MYR

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyDigital wallet

Payment method family

Digital wallet

- Recurring paymentsNo

Recurring payments

No

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportYes

Connect support

Yes

- Dispute supportNo

Dispute support

No

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

## Payment flow

This demo shows the customer experience when using GrabPay.

## Get started

You don’t actually have to integrate GrabPay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding GrabPay from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

If your integration requires manually listing payment methods, learn how to manually configure GrabPay as a payment.

[manually configure GrabPay as a payment](/payments/grabpay/accept-a-payment)

Check out the GrabPay sample on GitHub.

[sample on GitHub](https://github.com/stripe-samples/accept-a-payment)

[Refunds](#refunds)

## Refunds

GrabPay payments can be refunded up to 90 days after the original payment. Refunds for GrabPay payments are asynchronous and take up to 5 minutes to complete. We will notify you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the Refund object’s status transitions to succeeded. In the rare instance that a refund fails, the Refund object’s status will transition to failed and we will return the amount to your Stripe balance. You will then need to arrange an alternative way of providing your customer with a refund.

[webhook](/webhooks)

[Refund](/api/refunds/object)

[Disputed payments](#disputed-payments)

## Disputed payments

GrabPay payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment with Grab. Therefore, there is no dispute process that can result in a chargeback and funds being withdrawn from your Stripe account.

[Branding guidelines](#branding-guidelines)

## Branding guidelines

Use the branding guidelines provided by GrabPay when building your checkout page. Assets such as logos and buttons are available for download as a zip file.

[branding guidelines](https://stripe.com/files/grabpay/GrabPay_Online_Partners_Brand_Guidelines.pdf)

[as a zip file](https://stripe.com/files/grabpay/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip)
