# Bancontact payments

Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. Customers use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately.

[Customers](/api/customers)

In order to pay with Bancontact, customers are redirected to the Bancontact website or mobile app to authorize the payment and then return to your website where there is immediate notification about the success or failure of the payment.

[authorize the payment](/payments/payment-methods#customer-actions)

[immediate notification](/payments/payment-methods#payment-notification)

- Customer locationsBelgium

Customer locations

Belgium

- Presentment currencyEUR

Presentment currency

EUR

- Payment confirmationCustomer-authenticated

Payment confirmation

Customer-authenticated

- Payment method familyAuthenticated bank-debit

Payment method family

Authenticated bank-debit

- Recurring paymentsvia SEPA Direct Debit

Recurring payments

via SEPA Direct Debit

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportYes

Connect support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

- Dispute supportNo

Dispute support

No

## Payment flows

Customer selects Bancontact at checkout

Customer is redirected to Bancontact and enters credentials

Customer is notified that payment is complete

(Optional) Customer returns back to business’s site for payment confirmation

Customer selects Bancontact at checkout

Customer is redirected to Bancontact and scans QR code

Customer enters pincode

Customer is notified that payment is complete

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t actually have to integrate Bancontact and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Bancontact from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

If you prefer to manually list payment methods or want to save Bancontact details for future payments, see the following guides:

- Manually configure Bancontact as a payment

[Manually configure Bancontact as a payment](/payments/bancontact/accept-a-payment)

- Save Bancontact details for future payments

[Save Bancontact details for future payments](/payments/bancontact/set-up-payment)

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Bancontact payments can be refunded up to 180 days after the original payment date.
