# Sofort payments

Our financial partners are in the process of deprecating Sofort. New businesses can’t accept Sofort payments. For more information read our support page.

[support page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)

Stripe users in Europe and the United States can use the Payment Intents API—a single integration path for creating payments using any supported method—to accept Sofort payments from customers in the following countries:

[Payment Intents API](/payments/payment-intents)

[Sofort](https://www.sofort.com/)

- Austria

- Belgium

- Germany

- Netherlands

- Spain

Sofort is a single use, delayed notification payment method that requires customers to authenticate their payment. It redirects them to their bank’s portal to authenticate the payment, and it typically takes 2 to 14 days to receive notification of success or failure.

[single use](/payments/payment-methods#usage)

[delayed notification](/payments/payment-methods#payment-notification)

[authenticate](/payments/payment-methods#customer-actions)

Your use of Sofort must comply with our Sofort Terms of Service.

[Sofort Terms of Service](https://stripe.com/sofort/legal)

- Customer locationsEurope

Customer locations

Europe

- Presentment currencyEUR

Presentment currency

EUR

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyBank debit

Payment method family

Bank debit

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

## Payment flow

This demo shows the customer experience when using Sofort.

## Get started

You don’t actually have to integrate Sofort and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Sofort from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

If you prefer to manually list payment methods or want to save Sofort details for future payments, see the following guides:

- Manually configure Sofort as a payment

[Manually configure Sofort as a payment](/payments/sofort/accept-a-payment)

- Save Sofort details for future payments

[Save Sofort details for future payments](/payments/sofort/set-up-payment)

## Disputed payments

The risk of fraud or unrecognized payments is low because the customer must authenticate the payment with their bank. As a result, you won’t have disputes that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Sofort payments can be refunded up to 180 days after the original payment.
