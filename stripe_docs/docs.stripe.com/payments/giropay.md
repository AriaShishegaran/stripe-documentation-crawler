# giropay payments

giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany.

giropay redirects customers to their website to authenticate a payment and there is immediate notification about the success or failure of a payment.

[authenticate a payment](/payments/payment-methods#customer-actions)

[immediate notification](/payments/payment-methods#payment-notification)

- Customer locationsGermany

Customer locations

Germany

- Presentment currencyEUR

Presentment currency

EUR

- Payment confirmationCustomer-authenticated

Payment confirmation

Customer-authenticated

- Payment method familyAuthenticated bank debit

Payment method family

Authenticated bank debit

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

This demo shows the customer experience when using Giropay.

## Get started

You don’t actually have to integrate giropay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding giropay from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

If your integration requires manually listing payment methods, learn how to manually configure giropay as a payment.

[manually configure giropay as a payment](/payments/giropay/accept-a-payment)

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

giropay payments can be refunded up to 180 days after the original payment date.
