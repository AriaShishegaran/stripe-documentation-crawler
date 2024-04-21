# EPS payments

EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers.

EPS redirects customers to their bank’s website to authenticate a payment and there is immediate notification about the success or failure of a payment.

[authenticate a payment](/payments/payment-methods#customer-actions)

[immediate notification](/payments/payment-methods#payment-notification)

- Customer locationsAustria

Customer locations

Austria

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

Customer selects EPS at checkout

[Customer](/api/customers)

Customer is redirected to EPS and chooses bank

Customer enters account credentials

Customer completes authorization process (with scanner or SMS)

Customer is notified that payment is complete

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t actually have to integrate EPS and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding EPS from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

If your integration requires manually listing payment methods, learn how to manually configure EPS as a payment.

[manually configure EPS as a payment](/payments/eps/accept-a-payment)

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

EPS payments can be refunded up to 180 days after the original payment date.
